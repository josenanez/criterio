#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia EA: lo que calcula el código para Ofelia, la asistente ejecutiva.

    python3 asistente.py <acción> [opciones]       python3 asistente.py --help

Ofelia (criterio-assistant) procesa la oficina de un ejecutivo: su agenda exportada, las sesiones
de los órganos que sigue —convocatoria, material, notas y acta— y la correspondencia guardada. Usa
el núcleo común de las familias (`nucleo.py`), con las reglas de compromiso de Samuel (ADR 0012).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** La agenda en .ics —eventos,
repeticiones y zonas horarias, como la exportan Outlook y Google Calendar— y los encabezados de
cada correo —.eml, o .msg de Outlook— los procesa el código. Los vuelos de cada itinerario los
extrae la agente a la ficha del viaje, y el código los cruza con la agenda. Lo que solo
trae un documento escrito —los acuerdos y los compromisos de un acta, las opciones de una decisión
con su evidencia, qué pide un correo y para cuándo— lo extrae la agente a su ficha, con la cita, y
el código lo cruza.

**Prepara; no recomienda ni decide.** Nada aquí ordena opciones, dice cuál conviene, envía,
acepta ni mueve nada (ADR 0012).

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import datetime as dt
import email
import email.policy
import email.utils
import re
import sys
import tempfile
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None  # type: ignore

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
import texto as T  # noqa: E402
from nucleo import (  # noqa: E402
    _PAIS, _hoy, alerta, escribir_json, fecha, iso, leer_json, marco_reporte, norm, ordenar,
    registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"

DEFECTOS = {
    "thresholds": {
        "material_days_before": 5,        # a estos días de una sesión, su material tiene que estar
        "minutes_days": 15,               # pasados estos días de una sesión, su acta firmada tiene que estar
        "reschedules": 2,                 # un compromiso movido estas veces o más se señala
        "agenda_max_age_days": 7,         # una exportación de la agenda más vieja no da cruces
        "agenda_window_days": 14,         # cuántos días de agenda se miran desde hoy
        "decision_days": 14,              # una decisión pendiente con plazo dentro de estos días se señala
    },
    "timezone": "America/Bogota",
    "office_emails": [],
    "excluded_folders": [],
    "publish_rostrum": False,
    "report": {"language": "es"},
}
SEVERIDAD = {
    "commitment_overdue": 1, "correspondence_unanswered": 1, "meeting_conflict": 1,
    "decision_deadline": 2, "meeting_without_material": 2, "meeting_without_minutes": 2, "commitment_rescheduled": 2,
    "agreement_without_owner": 3, "agreement_without_date": 3,
    "meeting_during_flight": 1, "meeting_while_away": 1, "trip_not_in_agenda": 2,
}
N.SEVERIDAD.update(SEVERIDAD)


def umbral(cfg: dict, k: str):
    return (cfg.get("thresholds") or {}).get(k, DEFECTOS["thresholds"][k])


def zona(cfg: dict):
    nombre = cfg.get("timezone") or DEFECTOS["timezone"]
    try:
        return ZoneInfo(nombre) if ZoneInfo else dt.timezone.utc
    except Exception:
        return None


def revisar_config(cfg: dict, rol: str) -> list[str]:
    p = []
    ent = cfg.get("entity") or {}
    # La oficina se identifica por su ejecutivo, no por la identificación fiscal de la entidad:
    # ningún documento de la oficina la trae, y no se pide (EA-1).
    if not ent.get("name"):
        p.append("entity.name vacío")
    # Ofelia no procesa nada propio de un país —ni facturas ni normas—: el país de la oficina es un
    # dato, no un límite, y no tiene que estar en el registro de países de los demás motores.
    if ent.get("country") and not re.fullmatch(r"[A-Za-z]{2}", str(ent["country"])):
        p.append("entity.country es el código de dos letras del país (ISO 3166), como CO")
    if not (cfg.get("executive") or {}).get("name"):
        p.append("executive.name vacío: el ejecutivo que se asiste")
    if zona(cfg) is None:
        p.append(f"timezone {cfg.get('timezone')!r} no es una zona horaria IANA, como America/Bogota")
    for k, n in (("_docs", "documents"), ("_estado", "state")):
        if cfg.get(k) is None:
            p.append(f"paths.{n} vacío")
    if cfg.get("_docs") and not cfg["_docs"].is_dir():
        p.append(f"la carpeta de documentos {cfg['_docs']} no existe")
    if cfg.get("_docs") and cfg.get("_estado"):
        try:
            cfg["_estado"].resolve().relative_to(cfg["_docs"].resolve())
            p.append("el estado no puede vivir dentro de la carpeta de documentos: ahí lo tomaría por un documento")
        except ValueError:
            pass
    return p


def excluida(ruta: Path, docs: Path, cfg: dict) -> bool:
    r = rel(ruta, docs)
    return any(r == x.strip("/") or r.startswith(x.strip("/") + "/") for x in cfg.get("excluded_folders") or [])


# ================================================================ la agenda: .ics (F-02)

def _desplegar(texto: str) -> list[str]:
    """RFC 5545, 3.1: una línea que empieza con espacio o tabulador continúa la anterior."""
    lineas: list[str] = []
    for l in texto.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if l[:1] in (" ", "\t") and lineas:
            lineas[-1] += l[1:]
        elif l:
            lineas.append(l)
    return lineas


def _prop(linea: str) -> tuple[str, dict, str]:
    cab, _, valor = linea.partition(":")
    partes = cab.split(";")
    params = {}
    for x in partes[1:]:
        k, _, v = x.partition("=")
        params[k.upper()] = v.strip('"')
    return partes[0].upper(), params, valor


# Outlook exporta la zona con su nombre de Windows, no el de la base de datos de zonas (IANA). Las
# de la región y las de las casas matrices más comunes, según la tabla de Unicode CLDR
# (windowsZones.xml); una que no está se declara, no se adivina.
ZONAS_WINDOWS = {
    "SA Pacific Standard Time": "America/Bogota", "Central America Standard Time": "America/Guatemala",
    "Central Standard Time (Mexico)": "America/Mexico_City", "Pacific SA Standard Time": "America/Santiago",
    "Argentina Standard Time": "America/Buenos_Aires", "E. South America Standard Time": "America/Sao_Paulo",
    "SA Western Standard Time": "America/La_Paz", "Venezuela Standard Time": "America/Caracas",
    "Paraguay Standard Time": "America/Asuncion", "Montevideo Standard Time": "America/Montevideo",
    "Eastern Standard Time": "America/New_York", "Central Standard Time": "America/Chicago",
    "Mountain Standard Time": "America/Denver", "Pacific Standard Time": "America/Los_Angeles",
    "GMT Standard Time": "Europe/London", "Romance Standard Time": "Europe/Paris",
    "W. Europe Standard Time": "Europe/Berlin", "UTC": "Etc/UTC",
}


def _zona_de(nombre: str):
    for n in (nombre, ZONAS_WINDOWS.get(nombre)):
        if n and ZoneInfo:
            try:
                return ZoneInfo(n)
            except Exception:
                continue
    return None


def _instante(valor: str, params: dict, tz_defecto) -> tuple[dt.datetime | dt.date | None, str | None]:
    """Un DTSTART o DTEND: fecha sola (todo el día), UTC con Z, con TZID o flotante. Devuelve el
    instante y, si no se pudo, por qué: un evento ambiguo se declara, no se adivina."""
    v = valor.strip()
    try:
        if params.get("VALUE") == "DATE" or re.fullmatch(r"\d{8}", v):
            return dt.date(int(v[:4]), int(v[4:6]), int(v[6:8])), None
        base = dt.datetime.strptime(v.rstrip("Z"), "%Y%m%dT%H%M%S")
    except ValueError:
        return None, f"fecha ilegible: {valor}"
    if v.endswith("Z"):
        return base.replace(tzinfo=dt.timezone.utc), None
    if params.get("TZID"):
        z = _zona_de(params["TZID"])
        return (base.replace(tzinfo=z), None) if z else (None, f"zona horaria desconocida: {params['TZID']}")
    return base.replace(tzinfo=tz_defecto), None


_DIAS = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}


def _repeticiones(inicio: dt.datetime, regla: str, desde: dt.datetime, hasta: dt.datetime, excluidas: set) -> tuple[list[dt.datetime], str | None]:
    """Las ocurrencias de un RRULE dentro de la ventana, en la hora local de su zona: una reunión
    semanal de las 9:00 sigue a las 9:00 en su zona aunque cambie la hora (RFC 5545, 3.3.10).
    Lo soportado: FREQ DAILY, WEEKLY o MONTHLY por día del mes, con INTERVAL, COUNT, UNTIL y BYDAY
    semanal. Lo demás se declara."""
    r = dict(x.split("=", 1) for x in regla.split(";") if "=" in x)
    freq = r.get("FREQ")
    if freq not in ("DAILY", "WEEKLY", "MONTHLY") or any(k in r for k in ("BYSETPOS", "BYMONTHDAY", "BYHOUR", "BYWEEKNO", "BYYEARDAY")):
        return [], f"repetición no soportada: {regla}"
    if freq == "MONTHLY" and "BYDAY" in r:
        return [], f"repetición no soportada: {regla}"
    paso = int(r.get("INTERVAL", "1"))
    cuenta = int(r["COUNT"]) if "COUNT" in r else None
    hasta_regla = None
    if "UNTIL" in r:
        u, _ = _instante(r["UNTIL"], {}, inicio.tzinfo)
        hasta_regla = u if isinstance(u, dt.datetime) else (dt.datetime.combine(u, dt.time(23, 59, 59), inicio.tzinfo) if u else None)
    dias = sorted(_DIAS[d[-2:]] for d in r.get("BYDAY", "").split(",") if d[-2:] in _DIAS) if freq == "WEEKLY" else []
    out, n, k = [], 0, 0
    local = inicio.replace(tzinfo=None)
    while k < 5000:
        if freq == "DAILY":
            candidatos = [local + dt.timedelta(days=k * paso)]
        elif freq == "WEEKLY":
            semana = local - dt.timedelta(days=local.weekday()) + dt.timedelta(weeks=k * paso)
            candidatos = [semana + dt.timedelta(days=d) for d in (dias or [local.weekday()])]
            candidatos = [c for c in candidatos if c >= local]
        else:
            m = local.month - 1 + k * paso
            a, mes = local.year + m // 12, m % 12 + 1
            try:
                candidatos = [local.replace(year=a, month=mes)]
            except ValueError:
                candidatos = []
        k += 1
        for c in sorted(candidatos):
            ocur = c.replace(tzinfo=inicio.tzinfo)
            if hasta_regla and ocur > hasta_regla:
                return out, None
            n += 1
            if cuenta is not None and n > cuenta:
                return out, None
            if ocur > hasta:
                return out, None
            if ocur >= desde and ocur not in excluidas:
                out.append(ocur)
    return out, None


def leer_ics(ruta: Path, tz_defecto, desde: dt.datetime, hasta: dt.datetime) -> dict:
    """Los eventos de una exportación, desplegados dentro de la ventana. Cada ocurrencia lleva su
    UID, su resumen y su línea en el archivo para la cita."""
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    eventos, ambiguos, actual, linea_ini = [], [], None, 0
    lineas = _desplegar(texto)
    # Google Calendar declara la zona del calendario en el encabezado: es la de las horas flotantes.
    for l in lineas:
        if l.upper().startswith("X-WR-TIMEZONE:"):
            tz_defecto = _zona_de(l.split(":", 1)[1].strip()) or tz_defecto
            break
    for i, l in enumerate(lineas, start=1):
        if l.upper() == "BEGIN:VEVENT":
            actual, linea_ini = {"props": {}, "exdate": set()}, i
            continue
        if l.upper() == "END:VEVENT" and actual is not None:
            actual["linea"] = linea_ini
            eventos.append(actual)
            actual = None
            continue
        if actual is None:
            continue
        nombre, params, valor = _prop(l)
        if nombre == "EXDATE":
            for v in valor.split(","):
                x, _ = _instante(v, params, tz_defecto)
                if isinstance(x, dt.datetime):
                    actual["exdate"].add(x)
        else:
            actual["props"][nombre] = (params, valor)
    base, cambios, canceladas, ocurrencias = {}, {}, set(), []
    desescapar = lambda x: x.replace("\\,", ",").replace("\\;", ";").replace("\\n", " ").replace("\\N", " ")  # noqa: E731
    for e in eventos:
        p = e["props"]
        uid = (p.get("UID") or ({}, ""))[1] or f"sin-uid-{e['linea']}"
        resumen = desescapar((p.get("SUMMARY") or ({}, ""))[1])
        if norm((p.get("STATUS") or ({}, ""))[1]) == "cancelled":
            # Una ocurrencia cancelada de una serie —así la exporta Google Calendar— la quita de la
            # serie; un evento cancelado entero no entra.
            if "RECURRENCE-ID" in p:
                rid, _ = _instante(p["RECURRENCE-ID"][1], p["RECURRENCE-ID"][0], tz_defecto)
                canceladas.add((uid, rid))
            continue
        ini, err = _instante(p["DTSTART"][1], p["DTSTART"][0], tz_defecto) if "DTSTART" in p else (None, "sin DTSTART")
        if err or ini is None:
            ambiguos.append({"uid": uid, "resumen": resumen, "linea": e["linea"], "motivo": err})
            continue
        fin = None
        if "DTEND" in p:
            fin, err = _instante(p["DTEND"][1], p["DTEND"][0], tz_defecto)
        elif "DURATION" in p:
            m = re.fullmatch(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?)?", p["DURATION"][1].strip())
            if m and isinstance(ini, dt.datetime):
                fin = ini + dt.timedelta(days=int(m.group(1) or 0), hours=int(m.group(2) or 0), minutes=int(m.group(3) or 0))
        todo_el_dia = not isinstance(ini, dt.datetime)
        # Libre: TRANSP:TRANSPARENT (RFC 5545) o el estado de Outlook, X-MICROSOFT-CDO-BUSYSTATUS:FREE.
        libre = (norm((p.get("TRANSP") or ({}, ""))[1]) == "transparent"
                 or norm((p.get("X-MICROSOFT-CDO-BUSYSTATUS") or ({}, ""))[1]) == "free")
        ev = {"uid": uid, "resumen": resumen, "linea": e["linea"], "todo_el_dia": todo_el_dia, "libre": libre,
              "lugar": desescapar((p.get("LOCATION") or ({}, ""))[1]).strip()}
        if "RECURRENCE-ID" in p:
            rid, _ = _instante(p["RECURRENCE-ID"][1], p["RECURRENCE-ID"][0], tz_defecto)
            cambios[(uid, rid)] = (ini, fin, ev)
            continue
        if todo_el_dia:
            if desde.date() <= ini <= hasta.date():
                ocurrencias.append(dict(ev, inicio=ini, fin=fin))
            continue
        dur = (fin - ini) if isinstance(fin, dt.datetime) else dt.timedelta(0)
        if dur <= dt.timedelta(0):
            ambiguos.append({"uid": uid, "resumen": resumen, "linea": e["linea"], "motivo": "sin hora de fin"})
            continue
        base[uid] = (ini, dur, ev)
        if "RRULE" in p:
            occ, err = _repeticiones(ini, p["RRULE"][1], desde - dur, hasta, e["exdate"])
            if err:
                ambiguos.append({"uid": uid, "resumen": resumen, "linea": e["linea"], "motivo": err})
                continue
            for o in occ:
                ocurrencias.append(dict(ev, inicio=o, fin=o + dur, rid=o))
        elif ini < hasta and ini + dur > desde:
            ocurrencias.append(dict(ev, inicio=ini, fin=ini + dur, rid=ini))
    # Una ocurrencia modificada reemplaza a la de su RECURRENCE-ID (RFC 5545, 3.8.4.4); una cancelada la quita.
    ocurrencias = [o for o in ocurrencias if (o["uid"], o.get("rid")) not in canceladas]
    for (uid, rid), (ini, fin, ev) in cambios.items():
        ocurrencias = [o for o in ocurrencias if not (o["uid"] == uid and o.get("rid") == rid)]
        if isinstance(ini, dt.datetime) and isinstance(fin, dt.datetime) and ini < hasta and fin > desde:
            ocurrencias.append(dict(ev, inicio=ini, fin=fin, rid=rid))
    return {"ocurrencias": ocurrencias, "ambiguos": ambiguos}


def exportacion_mas_reciente(docs: Path, cfg: dict) -> tuple[Path | None, dt.date | None]:
    """La exportación de la agenda más reciente, por la fecha de su nombre (AAAA-MM-DD)."""
    mejor = (None, None)
    carpeta = docs / "10-agenda"
    for p in sorted(carpeta.rglob("*.ics")) if carpeta.is_dir() else []:
        if excluida(p, docs, cfg):
            continue
        m = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
        f = fecha(m.group(1)) if m else dt.date.fromtimestamp(p.stat().st_mtime)
        if mejor[1] is None or (f and f > mejor[1]):
            mejor = (p, f)
    return mejor


# ================================================================ la correspondencia: .eml y .msg (F-03)

def leer_correo(ruta: Path) -> dict:
    """Los encabezados que procesa el código (RFC 5322 en un .eml; las propiedades del mensaje en
    un .msg de Outlook, MS-OXMSG): quién, a quién, cuándo, el asunto y con qué mensaje se relaciona.
    El cuerpo lo procesa la agente en su ficha."""
    if ruta.suffix.lower() == ".msg":
        m = T.leer_msg(ruta)
        return {"id": m["id"], "de": m["de"], "para": m["para"], "asunto": m["asunto"],
                "fecha": iso(m["fecha"].date()) if m["fecha"] else None, "responde_a": m["responde_a"]}
    with open(ruta, "rb") as fh:
        m = email.message_from_binary_file(fh, policy=email.policy.default)
    fecha_ = None
    try:
        d = email.utils.parsedate_to_datetime(m["Date"]) if m["Date"] else None
        fecha_ = d.date() if d else None
    except (TypeError, ValueError):
        fecha_ = None
    refs = " ".join(str(m.get(h) or "") for h in ("In-Reply-To", "References"))
    return {"id": str(m.get("Message-ID") or "").strip(), "de": email.utils.parseaddr(str(m.get("From") or ""))[1].lower(),
            "para": [a.lower() for _, a in email.utils.getaddresses([str(m.get("To") or "")])],
            "asunto": str(m.get("Subject") or ""), "fecha": iso(fecha_), "responde_a": re.findall(r"<[^>]+>", refs)}


# ================================================================ las sesiones de los órganos

def sesiones(docs: Path, cfg: dict) -> list[dict]:
    out = []
    base = docs / "organos"
    for org in sorted(x for x in base.iterdir() if x.is_dir()) if base.is_dir() else []:
        for s in sorted(x for x in org.iterdir() if x.is_dir()):
            f = fecha(s.name)
            if not f or excluida(s, docs, cfg):
                continue
            def archivos(sub):
                d = s / sub
                return [rel(p, docs) for p in sorted(d.rglob("*")) if p.is_file() and not p.name.startswith(".")] if d.is_dir() else []
            acta_todo = archivos("40-acta")
            borradores_en_acta = [a for a in acta_todo if "borrador" in norm(Path(a).name)]
            out.append({"organo": org.name, "fecha": f, "carpeta": rel(s, docs),
                        "convocatoria": archivos("10-convocatoria"), "material": archivos("20-material"),
                        "notas": archivos("30-notas"), "acta": [a for a in acta_todo if a not in borradores_en_acta],
                        "borradores_en_acta": borradores_en_acta})
    return out


def fichas_reuniones(estado: Path) -> dict[str, dict]:
    d = estado / "reuniones"
    out = {}
    for p in sorted(d.glob("*.json")) if d.is_dir() else []:
        f = leer_json(p)
        if isinstance(f, dict):
            out[f"{f.get('organ')}:{f.get('date')}"] = f
    return out


def _archivo_cita(cita: str) -> str:
    """El archivo de una cita: lo que va antes de «, línea N» o de «: «texto»»."""
    m = re.match(r"\s*([^,:«]+?\.[A-Za-z0-9]+)\b", cita or "")
    return m.group(1).strip() if m else ""


def revisar_ficha_reunion(f: dict, docs: Path | None = None) -> list[str]:
    p = []
    k = f"{f.get('organ')}:{f.get('date')}"
    if not f.get("organ") or not fecha(f.get("date")):
        p.append(f"{k}: la ficha lleva organ y date (AAAA-MM-DD)")
    for lista, campos in (("agreements", ("id", "what", "source")), ("commitments", ("id", "what", "source")), ("decisions", ("id", "decision", "source"))):
        for i, x in enumerate(f.get(lista) or []):
            falta = [c for c in campos if not x.get(c)]
            if falta:
                p.append(f"{k}: {lista}[{i}] sin {', '.join(falta)}")
    for i, d in enumerate(f.get("decisions") or []):
        for j, o in enumerate(d.get("options") or []):
            if not o.get("option") or not o.get("evidence"):
                p.append(f"{k}: decisions[{i}].options[{j}] lleva option y evidence, con su cita")
            if "rank" in o or "recommended" in o:
                p.append(f"{k}: decisions[{i}].options[{j}]: Ofelia no ordena ni recomienda opciones; quita rank o recommended")
    # Cada cita, relativa a la carpeta de la oficina: una ruta que no existe ahí no la abre nadie (EA-6).
    if docs is not None:
        citas = [x.get("source") for lista in ("agreements", "commitments", "decisions") for x in f.get(lista) or []]
        citas += [r.get("source") for c in f.get("commitments") or [] for r in c.get("reschedules") or []]
        for c in sorted({_archivo_cita(x) for x in citas if x} - {""}):
            if not (docs / c).is_file():
                p.append(f"{k}: la cita {c} no está en la carpeta de la oficina; las rutas van relativas a ella")
    return p


# ================================================================ Ofelia

# ================================================================ los viajes: el itinerario contra la agenda

def _codigo(x) -> str:
    """Un número de vuelo comparable: «AV 9341», «av9341» y «AV-9341» son el mismo."""
    return re.sub(r"[^A-Z0-9]", "", str(x or "").upper())


def _momento(v):
    try:
        m = dt.datetime.fromisoformat(str(v).replace("Z", "+00:00"))
    except ValueError:
        return None
    return m if m.tzinfo else None


VIRTUAL = re.compile(r"https?://|teams|zoom|meet\.|webex|virtual|en l[ií]nea", re.I)


def fichas_viajes(estado: Path) -> tuple[list[dict], list[str]]:
    """Cada viaje de su ficha, con sus vuelos ya como instantes. Un vuelo sin hora con su zona, o
    que llega antes de salir, no se cruza: se dice qué falta."""
    viajes, problemas = [], []
    d = estado / "viajes"
    for p in sorted(d.glob("*.json")) if d.is_dir() else []:
        f = leer_json(p) or {}
        vuelos = []
        for v in f.get("flights") or []:
            sale, llega = _momento(v.get("depart")), _momento(v.get("arrive"))
            if not sale or not llega or llega <= sale or not _codigo(v.get("flight")):
                problemas.append(f"viajes/{p.name}: el vuelo {v.get('flight') or '?'} necesita su número, y la salida y la llegada con fecha, hora y zona (AAAA-MM-DDTHH:MM-05:00)")
                continue
            vuelos.append(dict(v, codigo=_codigo(v.get("flight")), sale=sale, llega=llega))
        if vuelos:
            viajes.append({"ficha": p.name, "archivo": f.get("file"), "viaje": f.get("trip") or p.stem, "vuelos": sorted(vuelos, key=lambda x: x["sale"])})
    return viajes, problemas


def ofelia(cfg: dict, hoy: dt.date) -> dict:
    _PAIS[0] = N.pais_de(cfg)
    docs, estado = cfg["_docs"], cfg["_estado"]
    tz = zona(cfg) or dt.timezone.utc
    al: list[dict] = []
    no_proc: list[dict] = []
    avisos: list[str] = []

    # La agenda: la exportación más reciente, si no es más vieja que el umbral.
    ventana = umbral(cfg, "agenda_window_days")
    desde = dt.datetime.combine(hoy, dt.time(0, 0), tz)
    hasta = desde + dt.timedelta(days=ventana)
    ruta_ics, f_exp = exportacion_mas_reciente(docs, cfg)
    agenda = {"exportacion": rel(ruta_ics, docs) if ruta_ics else None, "fecha_exportacion": iso(f_exp), "vieja": False,
              "desde": iso(hoy), "hasta": iso(hoy + dt.timedelta(days=ventana)), "eventos": [], "cruces": [], "ambiguos": []}
    viajes, problemas_viajes = fichas_viajes(estado)
    filas_viajes = []
    # El bloque de un vuelo en la agenda es el evento que lleva su número en el título.
    es_bloque = lambda o: any(v["codigo"] in _codigo(o["resumen"]) for vj in viajes for v in vj["vuelos"])  # noqa: E731
    if not ruta_ics:
        no_proc.append({"archivo": "10-agenda/", "motivo": "no hay una exportación de la agenda en .ics"})
    else:
        lei = leer_ics(ruta_ics, tz, desde, hasta)
        agenda["ambiguos"] = lei["ambiguos"]
        for a in lei["ambiguos"]:
            no_proc.append({"archivo": f"{agenda['exportacion']}#L{a['linea']}", "motivo": f"«{a['resumen']}»: {a['motivo']}; se declara, no se adivina"})
        ocur = sorted(lei["ocurrencias"], key=lambda o: (str(o["inicio"]), o["uid"]))
        for o in ocur:
            ini = o["inicio"].astimezone(tz) if isinstance(o["inicio"], dt.datetime) else o["inicio"]
            fin = o["fin"].astimezone(tz) if isinstance(o.get("fin"), dt.datetime) else o.get("fin")
            agenda["eventos"].append({"uid": o["uid"], "resumen": o["resumen"], "todo_el_dia": o["todo_el_dia"],
                                      "inicio": ini.isoformat() if hasattr(ini, "isoformat") else None,
                                      "fin": fin.isoformat() if hasattr(fin, "isoformat") else None, "libre": o["libre"], "lugar": o["lugar"]})
        edad = (hoy - f_exp).days if f_exp else None
        if edad is not None and edad > umbral(cfg, "agenda_max_age_days"):
            agenda["vieja"] = True
            avisos.append(f"la agenda exportada es del {iso(f_exp)}, de hace {edad} días: no se calculan cruces hasta que llegue una exportación de los últimos {umbral(cfg, 'agenda_max_age_days')} días")
        else:
            reales = [o for o in ocur if not o["todo_el_dia"] and not o["libre"]]
            for i, a in enumerate(reales):
                for b in reales[i + 1:]:
                    if a["uid"] == b["uid"] and a.get("rid") == b.get("rid"):
                        continue
                    if es_bloque(a) or es_bloque(b):     # contra un vuelo, el cruce lo dice el viaje
                        continue
                    if a["inicio"] < b["fin"] and b["inicio"] < a["fin"]:
                        dia = max(a["inicio"], b["inicio"]).astimezone(tz).date()
                        par = sorted([a["uid"], b["uid"]])
                        hora = lambda x: x.astimezone(tz).strftime("%H:%M")  # noqa: E731
                        cruce = {"fecha": iso(dia), "a": a["resumen"], "b": b["resumen"],
                                 "horas": f"{hora(a['inicio'])}–{hora(a['fin'])} y {hora(b['inicio'])}–{hora(b['fin'])}"}
                        agenda["cruces"].append(cruce)
                        al.append(alerta("meeting_conflict", f"{iso(dia)}: «{a['resumen']}» ({hora(a['inicio'])}–{hora(a['fin'])}) se cruza con «{b['resumen']}» ({hora(b['inicio'])}–{hora(b['fin'])})",
                                         [{"archivo": agenda["exportacion"], "linea": a["linea"]}, {"archivo": agenda["exportacion"], "linea": b["linea"]}],
                                         clave=f"cruce:{iso(dia)}:{par[0]}|{par[1]}"))

    # Los viajes: cada vuelo dentro de la ventana contra la agenda. Con la agenda vieja no se cruzan.
    hora_l = lambda x: x.astimezone(tz).strftime("%Y-%m-%d %H:%M")  # noqa: E731
    reuniones_ag = [o for o in (lei["ocurrencias"] if ruta_ics else []) if not o["todo_el_dia"] and not o["libre"] and not es_bloque(o)]
    for vj in viajes:
        vuelos = vj["vuelos"]
        fila = {"viaje": vj["viaje"], "archivo": vj["archivo"], "vuelos": []}
        # Fuera de su ciudad: de la llegada del primer vuelo a la salida del último, si vuelve a donde salió.
        casa = vuelos[0].get("from") if len(vuelos) >= 2 and norm(vuelos[-1].get("to")) == norm(vuelos[0].get("from")) else None
        fuera = (vuelos[0]["llega"], vuelos[-1]["sale"]) if casa else None
        for v in vuelos:
            en_ag = any(v["codigo"] in _codigo(o["resumen"]) for o in (lei["ocurrencias"] if ruta_ics else []))
            fila["vuelos"].append({"vuelo": v.get("flight"), "de": v.get("from"), "a": v.get("to"), "sale": hora_l(v["sale"]),
                                   "llega": hora_l(v["llega"]), "en_agenda": en_ag})
            if not ruta_ics or agenda["vieja"] or not (desde <= v["sale"] < hasta):
                continue
            cita = {"archivo": v.get("source") or vj["archivo"]}
            if not en_ag:
                al.append(alerta("trip_not_in_agenda", f"el vuelo {v.get('flight')} ({v.get('from')} → {v.get('to')}) sale el {hora_l(v['sale'])} y no está en la agenda: ese tiempo se ve libre",
                                 cita, clave=f"viaje-agenda:{v['codigo']}:{v['sale'].astimezone(tz).date().isoformat()}"))
            for o in reuniones_ag:
                if o["inicio"] < v["llega"] and v["sale"] < o["fin"]:
                    al.append(alerta("meeting_during_flight", f"«{o['resumen']}» ({hora_l(o['inicio'])}) cae durante el vuelo {v.get('flight')}, que sale a las {v['sale'].astimezone(tz).strftime('%H:%M')} y llega a las {v['llega'].astimezone(tz).strftime('%H:%M')}",
                                     [cita, {"archivo": agenda["exportacion"], "linea": o["linea"]}], clave=f"vuelo:{v['codigo']}:{o['uid']}"))
        if fuera and ruta_ics and not agenda["vieja"]:
            for o in reuniones_ag:
                lugar = o.get("lugar") or ""
                presencial = lugar and not VIRTUAL.search(lugar) and norm(casa) in norm(lugar)
                en_vuelo = any(o["inicio"] < v["llega"] and v["sale"] < o["fin"] for v in vuelos)
                if presencial and not en_vuelo and o["inicio"] < fuera[1] and fuera[0] < o["fin"] and desde <= o["inicio"] < hasta:
                    al.append(alerta("meeting_while_away", f"«{o['resumen']}» ({hora_l(o['inicio'])}) es presencial en {casa} ({lugar}) y ese día el viaje a {vuelos[0].get('to')} sigue",
                                     [{"archivo": agenda["exportacion"], "linea": o["linea"]}, {"archivo": vj["archivo"]}],
                                     clave=f"fuera:{o['inicio'].astimezone(tz).date().isoformat()}:{o['uid']}"))
        filas_viajes.append(fila)

    # Las sesiones: material antes, acta después.
    ses = sesiones(docs, cfg)
    fichas = fichas_reuniones(estado)
    problemas = [x for f in fichas.values() for x in revisar_ficha_reunion(f, docs)] + problemas_viajes
    dias_mat, dias_acta = umbral(cfg, "material_days_before"), umbral(cfg, "minutes_days")
    filas_ses = []
    for s in ses:
        k = f"{s['organo']}:{iso(s['fecha'])}"
        faltan = (s["fecha"] - hoy).days
        fila = {"organo": s["organo"], "fecha": iso(s["fecha"]), "carpeta": s["carpeta"], "dias": faltan,
                "material": len(s["material"]), "acta": bool(s["acta"]), "notas": bool(s["notas"]),
                "convocatoria": bool(s["convocatoria"]), "ficha": k in fichas}
        filas_ses.append(fila)
        for b in s["borradores_en_acta"]:
            no_proc.append({"archivo": b, "motivo": "un borrador en 40-acta/ no es el acta: el acta es la que se firma"})
        if 0 <= faltan <= dias_mat and not s["material"]:
            al.append(alerta("meeting_without_material", f"{s['organo']} del {iso(s['fecha'])}: faltan {faltan} días y su material no está en 20-material/",
                             {"archivo": s["carpeta"] + "/20-material/"}, dias=faltan, clave=f"material:{k}"))
        if faltan < -dias_acta and not s["acta"]:
            al.append(alerta("meeting_without_minutes", f"{s['organo']} del {iso(s['fecha'])}: pasaron {-faltan} días y su acta firmada no está en 40-acta/"
                             + (" (lo que hay es un borrador)" if s["borradores_en_acta"] else ""),
                             {"archivo": s["carpeta"] + "/40-acta/"}, dias=-faltan, clave=f"acta:{k}"))
        if s["fecha"] < hoy and k not in fichas and (s["acta"] or s["notas"]):
            no_proc.append({"archivo": s["carpeta"] + "/", "motivo": f"{k} no tiene ficha: corre ea-scan"})

    # Acuerdos, compromisos y decisiones de cada ficha.
    reprog = umbral(cfg, "reschedules")
    acuerdos, compromisos_, decisiones = [], [], []
    for k, f in sorted(fichas.items()):
        organo, fecha_s = f.get("organ"), f.get("date")
        for x in f.get("agreements") or []:
            cita = {"archivo": x.get("source")}
            fila = {"organo": organo, "sesion": fecha_s, "id": x.get("id"), "que": x.get("what"), "quien": x.get("who"), "vence": x.get("due"), "cita": x.get("source")}
            acuerdos.append(fila)
            if not N.valor_campo(x.get("who")):
                al.append(alerta("agreement_without_owner", f"{organo} del {fecha_s}, {x.get('id')}: «{x.get('what')}» no tiene responsable", cita,
                                 clave=f"acuerdo-responsable:{k}:{x.get('id')}"))
            if not N.valor_campo(x.get("due")):
                al.append(alerta("agreement_without_date", f"{organo} del {fecha_s}, {x.get('id')}: «{x.get('what')}» no tiene fecha", cita,
                                 clave=f"acuerdo-fecha:{k}:{x.get('id')}"))
        for c in f.get("commitments") or []:
            r = N.compromisos([c], hoy, reprog)
            estado_c = "cumplido" if N.valor_campo(c.get("state")) == "met" else ("vencido" if r["vencidos"] else ("sin fecha" if r["sin_fecha"] else "abierto"))
            fila = {"organo": organo, "sesion": fecha_s, "id": c.get("id"), "que": N.valor_campo(c.get("what")), "quien": N.valor_campo(c.get("who")),
                    "vence": N.valor_campo(c.get("due_date")), "veces": len(c.get("reschedules") or []), "estado": estado_c,
                    "evidencia": c.get("evidence"), "cita": c.get("source")}
            compromisos_.append(fila)
            cita = {"archivo": c.get("source")}
            for v in r["vencidos"]:
                al.append(alerta("commitment_overdue", f"{organo} del {fecha_s}, {c.get('id')}: «{v['what']}» de {v['who'] or 'nadie'} venció el {v['due']} y ningún documento lo sostiene como cumplido",
                                 cita, responsable=v["who"], dias=v["days"], clave=f"compromiso:{k}:{c.get('id')}"))
            for v in r["reprogramados"]:
                al.append(alerta("commitment_rescheduled", f"{organo} del {fecha_s}, {c.get('id')}: «{v['what']}» se movió {v['times']} veces ({', '.join(str(d) for d in v['dates'])})",
                                 cita, responsable=v["who"], clave=f"reprogramado:{k}:{c.get('id')}"))
            problemas += [f"{k}: {a['field']}: {a['fix']}" for a in r["arreglos"]]
        for d in f.get("decisions") or []:
            limite = fecha(N.valor_campo(d.get("deadline")))
            pendiente = norm(d.get("status") or "pending") in ("pending", "pendiente")
            fila = {"organo": organo, "sesion": fecha_s, "id": d.get("id"), "decision": d.get("decision"), "opciones": d.get("options") or [],
                    "falta_saber": d.get("missing") or [], "plazo": iso(limite), "plazo_fuente": d.get("deadline_source"),
                    "pendiente": pendiente, "dias": (limite - hoy).days if limite else None, "cita": d.get("source")}
            decisiones.append(fila)
            if pendiente and limite and 0 <= (limite - hoy).days <= umbral(cfg, "decision_days"):
                al.append(alerta("decision_deadline", f"{organo}, {d.get('id')}: «{d.get('decision')}» tiene plazo el {iso(limite)}, en {(limite - hoy).days} días, y sigue pendiente",
                                 [{"archivo": d.get("deadline_source") or d.get("source")}], dias=(limite - hoy).days, clave=f"decision:{k}:{d.get('id')}"))

    # Los compromisos de proyecto son de Samuel: se citan de su ficha y no se recalculan (ADR 0012).
    de_proyecto = []
    if cfg.get("pmo_records"):
        base = Path(cfg["pmo_records"]).expanduser()
        if not base.is_absolute() and cfg.get("_raiz"):
            base = cfg["_raiz"] / base
        for p in sorted(base.glob("*.json")) if base.is_dir() else []:
            ficha = leer_json(p) or {}
            for c in ficha.get("commitments") or []:
                de_proyecto.append({"proyecto": ficha.get("project_id") or p.stem, "que": N.valor_campo(c.get("what")),
                                    "quien": N.valor_campo(c.get("who")), "vence": N.valor_campo(c.get("due_date")),
                                    "estado": N.valor_campo(c.get("state")), "cita": f"ficha de Samuel · {p.name}"})

    # La correspondencia: lo que pide respuesta, contra las respuestas guardadas.
    correos, fichas_correo = {}, {}
    carpeta = docs / "20-correspondencia"
    for p in sorted(x for x in carpeta.rglob("*") if x.suffix.lower() in (".eml", ".msg")) if carpeta.is_dir() else []:
        if excluida(p, docs, cfg):
            continue
        try:
            correos[rel(p, docs)] = leer_correo(p)
        except Exception as e:  # un correo ilegible se dice, no se salta en silencio
            no_proc.append({"archivo": rel(p, docs), "motivo": f"correo ilegible: {e}"})
    oficina = {x.lower() for x in cfg.get("office_emails") or []}
    respondidos = {r for c in correos.values() if c["de"] in oficina for r in c["responde_a"]}
    dc = estado / "correspondencia"
    for p in sorted(dc.glob("*.json")) if dc.is_dir() else []:
        f = leer_json(p) or {}
        if f.get("file"):
            fichas_correo[f["file"]] = f
    filas_correo = []
    for archivo, c in correos.items():
        f = fichas_correo.get(archivo)
        if c["de"] in oficina:
            continue
        if f is None:
            no_proc.append({"archivo": archivo, "motivo": "el correo no tiene ficha: corre ea-scan"})
            continue
        respondido = bool(c["id"]) and c["id"] in respondidos
        limite = fecha(N.valor_campo(f.get("due")))
        fila = {"archivo": archivo, "de": c["de"], "asunto": c["asunto"], "recibido": c["fecha"], "pide_respuesta": bool(f.get("asks_reply")),
                "que_pide": f.get("ask"), "plazo": iso(limite), "respondido": respondido, "rutinario": bool(f.get("routine"))}
        filas_correo.append(fila)
        if f.get("asks_reply") and limite and limite < hoy and not respondido:
            al.append(alerta("correspondence_unanswered", f"{c['de']}: «{c['asunto']}» pidió respuesta para el {iso(limite)} y no hay una respuesta guardada",
                             {"archivo": archivo}, dias=(hoy - limite).days, clave=f"correo:{Path(archivo).stem}"))
    for archivo in sorted(set(fichas_correo) - set(correos)):
        no_proc.append({"archivo": archivo, "motivo": "la ficha cita un correo que no está en 20-correspondencia/"})

    # La próxima sesión de cada órgano, para ea-prep: lo abierto de la anterior, el material y las decisiones.
    preparacion = []
    for org in sorted({s["organo"] for s in ses}):
        futuras = [s for s in ses if s["organo"] == org and s["fecha"] >= hoy]
        pasadas = [s for s in ses if s["organo"] == org and s["fecha"] < hoy]
        if not futuras:
            continue
        prox, ant = futuras[0], (pasadas[-1] if pasadas else None)
        ka = f"{org}:{iso(ant['fecha'])}" if ant else None
        abiertos = [c for c in compromisos_ if ka and f"{c['organo']}:{c['sesion']}" == ka and c["estado"] != "cumplido"]
        preparacion.append({"organo": org, "fecha": iso(prox["fecha"]), "carpeta": prox["carpeta"], "material": prox["material"],
                            "convocatoria": prox["convocatoria"], "anterior": iso(ant["fecha"]) if ant else None, "abiertos": abiertos,
                            "decisiones": [d for d in decisiones if d["organo"] == org and d["pendiente"]]})

    pendientes_acta = [x for x in filas_ses if x["dias"] < 0 and not x["acta"]]
    borradores = [rel(p, docs) for p in sorted((docs / "90-borradores").rglob("*")) if p.is_file()] if (docs / "90-borradores").is_dir() else []
    for b in borradores:
        if "borrador" not in norm(Path(b).name):
            no_proc.append({"archivo": b, "motivo": "un archivo en 90-borradores/ sin «BORRADOR» en el nombre"})
    semana = hoy + dt.timedelta(days=7)
    vence = []
    for c in compromisos_:
        if c["estado"] != "cumplido" and fecha(c["vence"]) and -30 <= (fecha(c["vence"]) - hoy).days <= 90:
            vence.append({"fecha": c["vence"], "que": f"{c['id']} · {c['que']}", "caso": c["organo"], "comando": "ea-commitments", "estado": "pendiente"})
    for d in decisiones:
        if d["pendiente"] and d["plazo"] and -30 <= d["dias"] <= 90:
            vence.append({"fecha": d["plazo"], "que": f"{d['id']} · {d['decision']}", "caso": d["organo"], "comando": "ea-prep", "estado": "pendiente"})
    for x in filas_correo:
        if x["pide_respuesta"] and not x["respondido"] and x["plazo"]:
            vence.append({"fecha": x["plazo"], "que": f"respuesta · {x['asunto']}", "caso": "correspondencia", "comando": "ea-mail", "estado": "pendiente"})
    partes = {
        "ea-agenda": {"agenda": agenda, "sesiones": filas_ses, "viajes": filas_viajes, "avisos": avisos},
        "ea-prep": {"sesiones": preparacion,
                    "sin_sesion": [d for d in decisiones if d["pendiente"] and d["organo"] not in {p["organo"] for p in preparacion}]},
        "ea-minutes": {"pendientes": pendientes_acta, "borradores": borradores},
        "ea-commitments": {"compromisos": compromisos_, "acuerdos": acuerdos, "de_proyecto": de_proyecto},
        "ea-mail": {"correos": filas_correo},
        "ea-weekly": {"llego": [x for x in filas_correo if x["recibido"] and 0 <= (hoy - fecha(x["recibido"])).days <= 7],
                      "vence": [v for v in vence if hoy <= fecha(v["fecha"]) <= semana],
                      "preparar": [p for p in preparacion if fecha(p["fecha"]) <= semana]},
    }
    return {"agente": "ofelia", "entidad": cfg.get("entity"), "ejecutivo": cfg.get("executive"), "corte": iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "avisos": avisos,
            "excluidas": cfg.get("excluded_folders") or [], "publica_en_rostrum": bool(cfg.get("publish_rostrum")),
            "preguntas": [], "vence": sorted(vence, key=lambda v: (v["fecha"], v["que"]))}


# ================================================================ el reporte

SENALES_DE = {
    "ea-agenda": {"meeting_conflict", "meeting_without_material", "meeting_without_minutes",
                  "meeting_during_flight", "meeting_while_away", "trip_not_in_agenda"},
    "ea-prep": {"decision_deadline", "meeting_without_material"},
    "ea-minutes": {"meeting_without_minutes", "agreement_without_owner", "agreement_without_date"},
    "ea-commitments": {"commitment_overdue", "commitment_rescheduled", "agreement_without_owner", "agreement_without_date"},
    "ea-mail": {"correspondence_unanswered"},
    "ea-weekly": set(SEVERIDAD),
    "ea-scan": set(SEVERIDAD),
}


def reporte(r: dict, comando: str, version: str) -> str:
    ej = (r.get("ejecutivo") or {}).get("name")
    alcance = f"al {r.get('hoy')}" + (f" · oficina de {ej}" if ej else "")
    return marco_reporte(r, comando, version, agente="Ofelia", senales=SENALES_DE.get(comando),
                         alcance=alcance, cuerpo=_cuerpo, familia="criterio-ea")


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    pie = []
    if r.get("excluidas"):
        pie.append(f"Carpetas excluidas, que no se procesaron: {', '.join('`' + x + '`' for x in r['excluidas'])}.")
    pie.append("Se publica en Rostrum." if r.get("publica_en_rostrum") else "No se publica en Rostrum: así lo dice la configuración.")
    if not p:
        return l + pie + [""]
    for a in p.get("avisos") or []:
        l += [f"> {a}", ""]
    if comando == "ea-agenda":
        ag = p["agenda"]
        l += [f"Agenda exportada el {ag['fecha_exportacion'] or '—'} (`{ag['exportacion'] or '—'}`), del {ag['desde']} al {ag['hasta']}.", ""]
        l += ["| Inicio | Fin | Reunión |", "|---|---|---|"]
        l += [f"| {e['inicio'][:16].replace('T', ' ') if e['inicio'] else '—'} | {e['fin'][11:16] if e['fin'] and not e['todo_el_dia'] else 'todo el día'} | {e['resumen']}{' (libre)' if e['libre'] else ''} |" for e in ag["eventos"]]
        l += ["", "| Órgano | Sesión | Días | Material | Acta |", "|---|---|---|---|---|"]
        l += [f"| {s['organo']} | {s['fecha']} | {s['dias']} | {s['material'] or 'no'} | {'sí' if s['acta'] else 'no'} |" for s in p["sesiones"]]
        if p.get("viajes"):
            l += ["", "| Viaje | Vuelo | Ruta | Sale | Llega | En la agenda |", "|---|---|---|---|---|---|"]
            l += [f"| {vj['viaje']} | {v['vuelo']} | {v['de']} → {v['a']} | {v['sale']} | {v['llega'][11:]} | {'sí' if v['en_agenda'] else 'no'} |"
                  for vj in p["viajes"] for v in vj["vuelos"]]
        l.append("")
    elif comando == "ea-prep":
        def ficha_decision(d):
            out = [f"**Decisión {d['id']}: {d['decision']}** — plazo {d['plazo'] or 'sin fecha'}" + (f" (`{d['plazo_fuente']}`)" if d.get("plazo_fuente") else ""), ""]
            for o in d["opciones"]:
                ev = ", ".join("`" + (x.get("archivo") if isinstance(x, dict) else str(x)) + "`" for x in o.get("evidence") or [])
                out.append(f"- {o.get('option')} — evidencia: {ev or 'ninguna'}")
            if d["falta_saber"]:
                out.append(f"- Lo que falta saber: {'; '.join(d['falta_saber'])}")
            return out + [""]
        for s in p["sesiones"]:
            l += [f"### {s['organo']} · {s['fecha']}", "",
                  f"**Material en la carpeta:** {len(s['material'])} archivo(s)" + ("" if s["material"] else " — falta"),
                  f"**Lo que quedó abierto de la sesión del {s['anterior'] or '—'}:**", ""]
            l += [f"- {c['id']} · {c['que']} — {c['quien'] or 'sin responsable'}, {c['vence'] or 'sin fecha'} ({c['estado']})" for c in s["abiertos"]] or ["- Nada abierto."]
            l.append("")
            for d in s["decisiones"]:
                l += ficha_decision(d)
        if p.get("sin_sesion"):
            l += ["### Decisiones pendientes de un órgano sin sesión convocada", ""]
            for d in p["sin_sesion"]:
                l += [f"*{d['organo']}, de la sesión del {d['sesion']}*", ""] + ficha_decision(d)
        l += ["Las opciones van en el orden en que las traen los documentos. Ofelia no las ordena ni dice cuál conviene: la decisión es del órgano.", ""]
    elif comando == "ea-minutes":
        l += ["| Órgano | Sesión | Días | Notas | Acta |", "|---|---|---|---|---|"]
        l += [f"| {s['organo']} | {s['fecha']} | {-s['dias']} | {'sí' if s['notas'] else 'no'} | no |" for s in p["pendientes"]]
        l += ["", "**Borradores en 90-borradores/:** " + (", ".join("`" + b + "`" for b in p["borradores"]) or "ninguno"),
              "", "Cada borrador lleva «BORRADOR» en el nombre y en el texto. El acta es la que se firma; Ofelia nunca la archiva en 40-acta/.", ""]
    elif comando == "ea-commitments":
        l += ["| Órgano | Sesión | Id | Compromiso | Responsable | Vence | Veces movido | Estado |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {c['organo']} | {c['sesion']} | {c['id']} | {c['que']} | {c['quien'] or '—'} | {c['vence'] or '—'} | {c['veces']} | {c['estado']} |" for c in p["compromisos"]]
        if p["de_proyecto"]:
            l += ["", "**De proyecto, citados de la ficha de Samuel y no recalculados:**", "", "| Proyecto | Compromiso | Responsable | Vence | Estado |", "|---|---|---|---|---|"]
            l += [f"| {c['proyecto']} | {c['que']} | {c['quien'] or '—'} | {c['vence'] or '—'} | {c['estado'] or '—'} |" for c in p["de_proyecto"]]
        l += ["", "Cada compromiso es del acta donde nació. Un compromiso solo se da por cumplido con un documento que lo sostenga.", ""]
    elif comando == "ea-mail":
        l += ["| Recibido | De | Asunto | Pide | Plazo | Respuesta guardada |", "|---|---|---|---|---|---|"]
        l += [f"| {c['recibido'] or '—'} | {c['de']} | {c['asunto']} | {c['que_pide'] or ('—' if not c['pide_respuesta'] else 'respuesta')} | {c['plazo'] or '—'} | {'sí' if c['respondido'] else 'no'} |" for c in p["correos"] if c["pide_respuesta"]]
        l += ["", "Los borradores de las respuestas rutinarias quedan en 90-borradores/. Ofelia nunca envía.", ""]
    elif comando == "ea-weekly":
        l += [f"**Llegó esta semana:** {len(p['llego'])} correo(s). **Vence en los próximos siete días:** {len(p['vence'])}. **Por preparar:** {len(p['preparar'])} sesión(es).", ""]
        l += [f"- {v['fecha']} · {v['que']} ({v['caso']})" for v in p["vence"]]
        l += [f"- Preparar {s['organo']} del {s['fecha']}: {len(s['material'])} archivo(s) de material, {len(s['decisiones'])} decisión(es) pendiente(s)" for s in p["preparar"]]
        l.append("")
    return l + pie + [""]


# ================================================================ cuándo toca qué

def despertar(cfg: dict, rol: str, hoy: dt.date) -> dict:
    corr = registro_corridas(cfg["_estado"])
    ultima = lambda que: max((fecha(c["fecha"]) for c in corr if c["comando"] == que), default=None)  # noqa: E731
    toca, motivo = [], []
    r = ofelia(cfg, hoy)
    u = ultima("ea-scan")
    if not u or (hoy - u).days >= 1:
        toca.append("ea-scan")
        motivo.append("la agenda, las sesiones y la correspondencia se procesan cada día que corre")
    if any(a["signal"] in ("meeting_without_material", "decision_deadline") for a in r["alertas"]) and ultima("ea-prep") != hoy:
        toca.append("ea-prep")
        motivo.append("una sesión entra en la ventana de su material o una decisión en su plazo")
    if any(a["signal"] == "meeting_without_minutes" for a in r["alertas"]) and ultima("ea-minutes") != hoy:
        toca.append("ea-minutes")
        motivo.append("hay actas pendientes")
    if any(a["signal"] == "correspondence_unanswered" for a in r["alertas"]) and ultima("ea-mail") != hoy:
        toca.append("ea-mail")
        motivo.append("hay correspondencia con el plazo vencido")
    w = ultima("ea-weekly")
    if not w or (hoy - w).days >= 7:
        toca.append("ea-weekly")
        motivo.append("un solo resumen a la semana")
    callado = not r["alertas"] and toca == ["ea-scan"]
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": callado}


# ================================================================ la línea de comandos

def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    r = ofelia(cfg, _hoy(a))
    destino = cfg["_estado"] / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Ofelia.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir", "agenda",
                                       "compute", "reporte", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action == "agenda":
        # La agenda normalizada, para que la agente la lea sin procesar el .ics a mano.
        import json
        cfg, _ = N.cargar_config(a.config)
        print(json.dumps(ofelia(cfg, _hoy(a))["partes"]["ea-agenda"]["agenda"], ensure_ascii=False, indent=2))
        return 0
    return N.despachar(a, ap, aqui=AQUI, rol="ofelia", estructura_json=ESTRUCTURA, subcarpetas=("reuniones", "correspondencia"),
                       revisar_config=revisar_config, calcular=calcular, reporte=reporte, despertar=despertar)


# ================================================================ la prueba del motor

def ics(*eventos: str, tz: str = "") -> str:
    return "BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//Criterio//prueba//ES\r\n" + tz + "".join(eventos) + "END:VCALENDAR\r\n"


def vevent(uid: str, resumen: str, inicio: str, fin: str, *, tzid: str | None = None, extra: str = "") -> str:
    p = f";TZID={tzid}" if tzid else ""
    return (f"BEGIN:VEVENT\r\nUID:{uid}\r\nSUMMARY:{resumen}\r\nDTSTART{p}:{inicio}\r\nDTEND{p}:{fin}\r\n{extra}END:VEVENT\r\n")


def selftest() -> int:
    fallas = []

    def ok(nombre, obtenido, esperado):
        if obtenido == esperado:
            print(f"  ok  {nombre}")
        else:
            fallas.append(nombre)
            print(f"  FALLA  {nombre}: {obtenido!r} en lugar de {esperado!r}")

    bog = ZoneInfo("America/Bogota")
    hoy = dt.date(2026, 10, 26)
    desde = dt.datetime.combine(hoy, dt.time(0), bog)
    hasta = desde + dt.timedelta(days=14)
    ok("una línea doblada se despliega", _desplegar("SUMMARY:Comité de\r\n  presidencia\r\n"), ["SUMMARY:Comité de presidencia"])
    # Una semanal de las 9:00 en Nueva York sigue a las 9:00 allá: en Bogotá pasa de las 8:00 a las
    # 9:00 cuando Estados Unidos deja el horario de verano (1 de noviembre de 2026).
    t = ics(vevent("ny", "Llamada con Nueva York", "20261027T090000", "20261027T100000", tzid="America/New_York", extra="RRULE:FREQ=WEEKLY;COUNT=3\r\n"))
    with tempfile.TemporaryDirectory() as tmp:
        x = Path(tmp) / "a.ics"
        x.write_text(t, encoding="utf-8")
        occ = leer_ics(x, bog, desde, hasta)["ocurrencias"]
        ok("la repetición sigue la hora de su zona a través del cambio de hora",
           [o["inicio"].astimezone(bog).strftime("%m-%d %H:%M") for o in occ], ["10-27 08:00", "11-03 09:00"])
        x.write_text(ics(vevent("m", "Mensual", "20261005T100000", "20261005T110000", tzid="America/Bogota", extra="RRULE:FREQ=MONTHLY;BYDAY=1MO\r\n")), encoding="utf-8")
        ok("una repetición no soportada se declara", [a["motivo"][:26] for a in leer_ics(x, bog, desde, hasta)["ambiguos"]], ["repetición no soportada: F"])
        x.write_text(ics(vevent("d", "Diaria", "20261026T080000", "20261026T083000", tzid="America/Bogota",
                                extra="RRULE:FREQ=DAILY;COUNT=5\r\nEXDATE;TZID=America/Bogota:20261027T080000\r\n"),
                         "BEGIN:VEVENT\r\nUID:d\r\nRECURRENCE-ID;TZID=America/Bogota:20261028T080000\r\nSUMMARY:Diaria movida\r\n"
                         "DTSTART;TZID=America/Bogota:20261028T090000\r\nDTEND;TZID=America/Bogota:20261028T093000\r\nEND:VEVENT\r\n"), encoding="utf-8")
        ok("EXDATE quita una ocurrencia y RECURRENCE-ID la mueve",
           sorted(o["inicio"].strftime("%d %H:%M") for o in leer_ics(x, bog, desde, hasta)["ocurrencias"]), ["26 08:00", "28 09:00", "29 08:00", "30 08:00"])

        t = Path(tmp)
        docs, est = t / "direccion" / "presidencia", t / "estado"
        (docs / "10-agenda").mkdir(parents=True)
        (docs / "10-agenda" / "agenda-2026-10-25.ics").write_text(ics(
            vevent("a", "Comité de presidencia", "20261028T150000Z", "20261028T170000Z"),
            vevent("b", "Visita del regulador", "20261028T160000Z", "20261028T163000Z"),
            vevent("c", "Bloque libre", "20261028T150000Z", "20261028T170000Z", extra="TRANSP:TRANSPARENT\r\n")), encoding="utf-8")
        for org, f, mat, acta in (("junta", "2026-10-29", False, False), ("junta", "2026-09-24", True, False), ("comite", "2026-10-01", True, True)):
            s = docs / "organos" / org / f
            (s / "10-convocatoria").mkdir(parents=True)
            if mat:
                (s / "20-material").mkdir()
                (s / "20-material" / "informe.pdf").write_text("x")
            (s / "40-acta").mkdir()
            (s / "40-acta" / ("acta.pdf" if acta else "acta-BORRADOR.md")).write_text("x")
        escribir_json(est / "reuniones" / "comite-2026-10-01.json", {
            "organ": "comite", "date": "2026-10-01", "source": "organos/comite/2026-10-01/40-acta/acta.pdf",
            "agreements": [{"id": "A-1", "what": "Aprobar la política de viajes", "who": "", "due": "2026-11-15", "source": "organos/comite/2026-10-01/40-acta/acta.pdf"}],
            "commitments": [{"id": "C-1", "who": "Laura", "what": "Informe de cartera", "due_date": "2026-10-15", "state": "open",
                             "reschedules": [{"due_date": "2026-10-08"}, {"due_date": "2026-10-15"}], "original_due_date": "2026-10-01",
                             "source": "organos/comite/2026-10-01/40-acta/acta.pdf"}],
            "decisions": [{"id": "D-1", "decision": "Proveedor del centro de datos", "source": "organos/comite/2026-10-01/40-acta/acta.pdf",
                           "deadline": "2026-11-02", "deadline_source": "organos/comite/2026-10-01/40-acta/acta.pdf", "status": "pending",
                           "options": [{"option": "Renovar", "evidence": [{"archivo": "a.pdf"}]}, {"option": "Licitar", "evidence": [{"archivo": "b.pdf"}]}]}]})
        (docs / "20-correspondencia").mkdir()
        (docs / "20-correspondencia" / "2026-10-10-regulador.eml").write_text(
            "Message-ID: <r1@sfc.test>\nFrom: Regulador <oficios@regulador.test>\nTo: presidencia@banco.test\nDate: Sat, 10 Oct 2026 09:00:00 -0500\nSubject: Requerimiento 45\n\nResponder antes del 20.\n", encoding="utf-8")
        (docs / "20-correspondencia" / "2026-10-12-cliente.eml").write_text(
            "Message-ID: <c1@cliente.test>\nFrom: cliente@cliente.test\nTo: presidencia@banco.test\nDate: Mon, 12 Oct 2026 09:00:00 -0500\nSubject: Reunión\n\nPido cita.\n", encoding="utf-8")
        (docs / "20-correspondencia" / "2026-10-13-respuesta.eml").write_text(
            "Message-ID: <p1@banco.test>\nIn-Reply-To: <c1@cliente.test>\nFrom: presidencia@banco.test\nTo: cliente@cliente.test\nDate: Tue, 13 Oct 2026 09:00:00 -0500\nSubject: Re: Reunión\n\nCon gusto.\n", encoding="utf-8")
        escribir_json(est / "correspondencia" / "regulador.json", {"file": "20-correspondencia/2026-10-10-regulador.eml", "asks_reply": True, "ask": "Respuesta al requerimiento", "due": "2026-10-20"})
        escribir_json(est / "correspondencia" / "cliente.json", {"file": "20-correspondencia/2026-10-12-cliente.eml", "asks_reply": True, "ask": "Una cita", "due": "2026-10-16"})
        cfg = {"entity": {"name": "Banco de prueba", "country": "CO"}, "executive": {"name": "Presidencia"},
               "timezone": "America/Bogota", "office_emails": ["presidencia@banco.test"], "_docs": docs, "_estado": est}
        ok("la configuración pasa", revisar_config(cfg, "ofelia"), [])
        r = ofelia(cfg, hoy)
        ok("las señales de una oficina con todo mal, y ninguna otra", sorted((a["signal"], a["key"]) for a in r["alertas"]), [
            ("agreement_without_owner", "acuerdo-responsable:comite:2026-10-01:A-1"),
            ("commitment_overdue", "compromiso:comite:2026-10-01:C-1"),
            ("commitment_rescheduled", "reprogramado:comite:2026-10-01:C-1"),
            ("correspondence_unanswered", "correo:2026-10-10-regulador"),
            ("decision_deadline", "decision:comite:2026-10-01:D-1"),
            ("meeting_conflict", "cruce:2026-10-28:a|b"),
            ("meeting_without_material", "material:junta:2026-10-29"),
            ("meeting_without_minutes", "acta:junta:2026-09-24")])
        ok("un borrador en 40-acta no cuenta como acta, y se dice", sum("un borrador en 40-acta" in x["motivo"] for x in r["no_procesado"]), 2)
        ok("el informe no se publica en Rostrum por omisión", r["publica_en_rostrum"], False)
        md = reporte(r, "ea-prep", "0.0.0")
        ok("la ficha de la decisión trae las opciones sin ordenarlas", ("Renovar" in md and "Licitar" in md and md.index("Renovar") < md.index("Licitar")), True)
        ok("una oficina de un país fuera del registro de los demás motores pasa",
           revisar_config(dict(cfg, entity={"name": "Oficina", "country": "AR"}), "ofelia"), [])
        ok("sin identificación fiscal, la oficina pasa y el encabezado no la inventa",
           (revisar_config(dict(cfg, _docs=docs, _estado=est), "ofelia"), "(None)" in md), ([], False))
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        ok("una cita fuera de la carpeta de la oficina se corrige",
           any("relativas a ella" in x for x in revisar_ficha_reunion(
               {"organ": "comite", "date": "2026-10-01", "agreements": [{"id": "A-1", "what": "x", "source": "direccion/otra/acta.md, línea 2"}]}, docs)), True)
        ok("una ficha que ordena opciones se corrige", any("no ordena ni recomienda" in x for x in revisar_ficha_reunion(
            {"organ": "o", "date": "2026-01-01", "decisions": [{"id": "D", "decision": "x", "source": "s", "options": [{"option": "a", "evidence": ["e"], "rank": 1}]}]})), True)
        # Una agenda vieja avisa y no da cruces.
        (docs / "10-agenda" / "agenda-2026-10-25.ics").rename(docs / "10-agenda" / "agenda-2026-10-10.ics")
        r = ofelia(cfg, hoy)
        ok("una agenda vieja avisa y no calcula cruces", ([a for a in r["alertas"] if a["signal"] == "meeting_conflict"], bool(r["avisos"])), ([], True))
        cfg["excluded_folders"] = ["20-correspondencia"]
        ok("una carpeta excluida no se procesa", [a for a in ofelia(cfg, hoy)["alertas"] if a["signal"] == "correspondence_unanswered"], [])

        # Outlook: la zona con su nombre de Windows y el estado «libre» propio; Google: la zona del
        # calendario en el encabezado y una ocurrencia cancelada de una serie.
        x = Path(tmp) / "outlook.ics"
        x.write_text(ics(vevent("w", "Semanal", "20261027T090000", "20261027T100000", tzid="SA Pacific Standard Time", extra="RRULE:FREQ=WEEKLY;COUNT=2\r\n"),
                         vevent("f", "Libre en Outlook", "20261027T090000", "20261027T100000", tzid="Eastern Standard Time",
                                extra="X-MICROSOFT-CDO-BUSYSTATUS:FREE\r\n")), encoding="utf-8")
        occ = leer_ics(x, dt.timezone.utc, desde, hasta)["ocurrencias"]
        ok("Outlook: la zona de Windows se traduce y BUSYSTATUS:FREE es libre",
           sorted((o["inicio"].astimezone(bog).strftime("%m-%d %H:%M"), o["libre"]) for o in occ),
           [("10-27 08:00", True), ("10-27 09:00", False), ("11-03 09:00", False)])
        x = Path(tmp) / "google.ics"
        x.write_text("BEGIN:VCALENDAR\r\nX-WR-TIMEZONE:America/Guayaquil\r\n"
                     + "".join(ics(vevent("g", "Comité", "20261026T140000Z", "20261026T150000Z", extra="RRULE:FREQ=WEEKLY;COUNT=3\r\nLOCATION:Sala 2\\, Quito\r\n")).splitlines(True)[1:-1])
                     + "BEGIN:VEVENT\r\nUID:g\r\nRECURRENCE-ID:20261102T140000Z\r\nSTATUS:CANCELLED\r\nDTSTART:20261102T140000Z\r\nDTEND:20261102T150000Z\r\nEND:VEVENT\r\n"
                     + vevent("h", "Flotante", "20261028T090000", "20261028T100000") + "END:VCALENDAR\r\n", encoding="utf-8")
        occ = leer_ics(x, dt.timezone.utc, desde, hasta)["ocurrencias"]
        ok("Google: la ocurrencia cancelada sale de la serie, la hora flotante toma la zona del calendario y el lugar se lee",
           sorted((o["uid"], o["inicio"].astimezone(bog).strftime("%m-%d %H:%M"), o["lugar"]) for o in occ),
           [("g", "10-26 09:00", "Sala 2, Quito"), ("h", "10-28 09:00", "")])     # la del 2 de noviembre, cancelada
        # El .msg de Outlook: los mismos encabezados que un .eml, y la respuesta lo cierra.
        cfg["excluded_folders"] = []
        T.escribir_msg(docs / "20-correspondencia" / "2026-10-11-junta.msg", mid="<j1@junta.test>", de="junta@junta.test", para=["presidencia@banco.test"],
                       asunto="Convocatoria", fecha=dt.datetime(2026, 10, 11, 14, 0, tzinfo=dt.timezone.utc), cuerpo="Confirmar antes del 15.")
        ok("un .msg se lee como un .eml", {k: v for k, v in leer_correo(docs / "20-correspondencia" / "2026-10-11-junta.msg").items() if k != "responde_a"},
           {"id": "<j1@junta.test>", "de": "junta@junta.test", "para": ["presidencia@banco.test"], "asunto": "Convocatoria", "fecha": "2026-10-11"})
        escribir_json(est / "correspondencia" / "junta.json", {"file": "20-correspondencia/2026-10-11-junta.msg", "asks_reply": True, "due": "2026-10-15"})
        ok("un .msg sin respuesta se señala", "correo:2026-10-11-junta" in {a["key"] for a in ofelia(cfg, hoy)["alertas"]}, True)
        T.escribir_msg(docs / "20-correspondencia" / "2026-10-12-r-junta.msg", mid="<r9@banco.test>", de="presidencia@banco.test", para=["junta@junta.test"],
                       asunto="RE: Convocatoria", fecha=dt.datetime(2026, 10, 12, 14, 0, tzinfo=dt.timezone.utc), cuerpo="Confirmado.", responde="<j1@junta.test>")
        ok("la respuesta en .msg lo cierra", "correo:2026-10-11-junta" in {a["key"] for a in ofelia(cfg, hoy)["alertas"]}, False)
        # Los viajes: el itinerario contra la agenda.
        for f in (docs / "10-agenda").glob("*.ics"):
            f.unlink()
        (docs / "10-agenda" / "agenda-2026-10-25.ics").write_text(ics(
            vevent("v2", "Vuelo AV 9342 Quito–Bogotá", "20261029T180000", "20261029T193500", tzid="America/Bogota"),
            vevent("cena", "Cena del gremio", "20261029T183000", "20261029T200000", tzid="America/Bogota", extra="LOCATION:Club El Nogal\\, Bogotá\r\n"),
            vevent("rie", "Comité de riesgos", "20261028T100000", "20261028T110000", tzid="America/Bogota", extra="LOCATION:Sede principal\\, Bogotá\r\n"),
            vevent("cor", "Banco corresponsal", "20261028T150000", "20261028T160000", tzid="America/Bogota", extra="LOCATION:Av. Amazonas\\, Quito\r\n"),
            vevent("tea", "Comité de crédito", "20261028T120000", "20261028T130000", tzid="America/Bogota", extra="LOCATION:Microsoft Teams\r\n")), encoding="utf-8")
        escribir_json(est / "viajes" / "quito.json", {"file": "30-viajes/2026-10-27-quito.md", "trip": "Quito", "flights": [
            {"flight": "AV9341", "from": "Bogotá", "to": "Quito", "depart": "2026-10-27T06:00-05:00", "arrive": "2026-10-27T07:35-05:00", "source": "30-viajes/2026-10-27-quito.md, línea 5"},
            {"flight": "AV 9342", "from": "Quito", "to": "Bogota", "depart": "2026-10-29T18:00-05:00", "arrive": "2026-10-29T19:35-05:00", "source": "30-viajes/2026-10-27-quito.md, línea 6"}]})
        r = ofelia(cfg, hoy)
        ok("el viaje contra la agenda: el vuelo que no está, la reunión durante el vuelo y la presencial en casa estando fuera",
           sorted((a["signal"], a["key"]) for a in r["alertas"] if a["signal"] in ("trip_not_in_agenda", "meeting_during_flight", "meeting_while_away", "meeting_conflict")),
           [("meeting_during_flight", "vuelo:AV9342:cena"), ("meeting_while_away", "fuera:2026-10-28:rie"), ("trip_not_in_agenda", "viaje-agenda:AV9341:2026-10-27")])
        escribir_json(est / "viajes" / "malo.json", {"file": "30-viajes/x.md", "flights": [{"flight": "AV1", "depart": "2026-10-27T06:00", "arrive": "2026-10-27T07:00"}]})
        ok("un vuelo sin zona horaria no se cruza: se pide", any("AV1" in x for x in ofelia(cfg, hoy)["record_issues"]), True)
    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
