#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CISO: lo que calcula el código para Alexis, Guillermo y Amparo.

    python3 seguridad.py <acción> [opciones]       python3 seguridad.py --help

Alexis (criterio-security) procesa el gobierno y los controles: la declaración de aplicabilidad
contra la evidencia de cada control, las revisiones de acceso, las evaluaciones de terceros y las
aceptaciones de riesgo. Guillermo (criterio-vulnerability), las vulnerabilidades: cada hallazgo
del escáner contra el plazo de su severidad, el catálogo KEV, las excepciones, los cierres y la
cobertura de los escaneos. Amparo (criterio-resilience), la respuesta y la recuperación: cada
incidente contra los plazos de la política y la matriz de notificaciones, su revisión posterior y
las pruebas de continuidad y de restauración. Los tres comparten este motor, que vive en
criterio-security y se copia a los otros dos con scripts/sincronizar.py, y el núcleo común de las
familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —la declaración de
aplicabilidad, la tabla de sistemas, el registro de terceros, el de riesgos, el inventario de
activos, las exportaciones del escáner, el catálogo KEV, el seguimiento de la remediación, las
excepciones, la matriz de notificaciones y el calendario de continuidad— las procesa el código. Lo
que solo trae un documento escrito —la evidencia de un control, la revisión de accesos de un
sistema, la evaluación de un tercero, la línea de tiempo de un incidente con sus notificaciones,
su revisión posterior, cada prueba de continuidad— lo extrae el agente a su ficha, con la cita, y
el código lo cruza.

**Los plazos los fija la organización** (ADR 0023): el plazo de corrección de cada severidad, el de
contención de cada incidente, el de su revisión posterior, el de cada notificación y la frecuencia
de cada revisión y de cada prueba salen de su política, de su matriz y de sus registros. Lo único
que viene de una fuente externa es la fecha de corrección del catálogo KEV (F-06), que el catálogo
trae, y la escala de severidad del CVSS (F-05) cuando el escáner da el puntaje y no la severidad.

**Lo que nunca procesa:** credenciales, llaves ni respaldos. `EXCLUIDOS` los deja fuera por
omisión y cada reporte dice qué excluyó. Nada aquí se conecta a un sistema, corre un escaneo, acepta
un riesgo o califica la madurez de la organización.

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
from nucleo import (  # noqa: E402
    _csv, _hoy, _m, _xlsx, alerta, escribir_json, fecha, filas_de, iso, leer_json, marco_reporte,
    norm, numero, ordenar, registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"
SUB = {"alexis": "seguridad", "guillermo": "vulnerabilidades", "amparo": "resiliencia"}
FECHA_EN_NOMBRE = re.compile(r"(\d{4})[-_](\d{2})[-_](\d{2})")
VERDAD = ("si", "s", "yes", "y", "x", "true", "1", "verdadero", "aplica", "aplicable")

# ================================================================ lo que nunca se procesa

# Credenciales, llaves y respaldos: el motor no los abre ni los convierte, y el reporte dice cuáles
# dejó fuera. La configuración puede agregar extensiones (`exclude.extensions`), nunca quitar estas.
EXCLUIDOS = {
    "extensiones": {".pem", ".key", ".pfx", ".p12", ".jks", ".keystore", ".kdbx", ".ppk", ".ovpn", ".asc", ".gpg",
                    ".bak", ".dump", ".sql", ".tar", ".tgz", ".gz", ".zip", ".7z", ".rar", ".vhd", ".vhdx", ".vmdk", ".iso", ".img"},
    "nombres": re.compile(r"^(id_(rsa|dsa|ecdsa|ed25519)|\.env|credencial|password|contrasena|secret|token|llave_privada|private_key)", re.I),
}


def excluidos(docs: Path, cfg: dict) -> list[dict]:
    """Los archivos que el motor deja fuera por ser credenciales, llaves o respaldos."""
    ext = EXCLUIDOS["extensiones"] | {("." + e.lstrip(".")).lower() for e in ((cfg.get("exclude") or {}).get("extensions") or [])}
    out = []
    for p in sorted(docs.rglob("*")) if docs and docs.is_dir() else []:
        if not p.is_file():
            continue
        motivo = None
        if p.suffix.lower() in ext:
            motivo = f"excluido por omisión: {p.suffix.lower()} es una llave, una credencial o un respaldo"
        elif EXCLUIDOS["nombres"].match(norm(p.stem) if not p.name.startswith(".") else p.name):
            motivo = "excluido por omisión: por su nombre es una credencial o una llave"
        if motivo:
            out.append({"archivo": rel(p, docs), "motivo": motivo})
    return out


def _excluido(p: Path, lista: list[dict], docs: Path) -> bool:
    return rel(p, docs) in {x["archivo"] for x in lista}


# ================================================================ las tablas

class Hoja:
    """Una tabla con sus columnas canónicas, por su cabecera o por el mapeo de la configuración, y
    la fila de origen de cada dato para citarla."""

    def __init__(self, ruta: Path, requeridas: list[str], opcionales: list[str], alias: dict, columnas: dict | None = None):
        self.ruta, self.faltan, self.filas, self.mapa = ruta, [], [], {}
        filas = filas_de(ruta)
        fijas = {k: norm(v) for k, v in (columnas or {}).items() if v}
        cand = {c: ([fijas[c]] if c in fijas else alias.get(c, [c])) for c in list(requeridas) + list(opcionales)}
        inicio = 0
        for i, f in enumerate(filas[:15]):
            nf = {norm(x) for x in f}
            if any(set(cand[c]) & nf for c in requeridas):
                inicio = i
                break
        if not filas:
            self.faltan = list(requeridas)
            return
        cab = [norm(x) for x in filas[inicio]]
        for campo, cs in cand.items():
            for c in cs:
                if c in cab and cab.index(c) not in self.mapa.values():
                    self.mapa[campo] = cab.index(c)
                    break
        self.faltan = [c for c in requeridas if c not in self.mapa]
        self.cabecera = filas[inicio]
        for k, f in enumerate(filas[inicio + 1:], start=inicio + 2):
            if not any(str(x).strip() for x in f):
                continue
            fila = {"_fila": k}
            for campo, i in self.mapa.items():
                v = f[i] if i < len(f) else ""
                fila[campo] = v.strip() if isinstance(v, str) else v
            self.filas.append(fila)

    def cita(self, fila: dict, base: Path) -> dict:
        return {"archivo": rel(self.ruta, base), "fila": fila.get("_fila")}


def hallar(carpeta: Path, *patrones: str) -> list[Path]:
    """Las tablas de una carpeta cuyo nombre empieza por alguno de los patrones."""
    if not carpeta.is_dir():
        return []
    pats = [norm(x) for x in patrones]
    return sorted(p for p in carpeta.iterdir() if p.is_file() and not p.name.startswith(".")
                  and p.suffix.lower() in (".csv", ".xlsx") and any(norm(p.stem).startswith(x) for x in pats))


def leer_tabla(docs: Path, carpeta: str, patrones: tuple, requeridas: list, opcionales: list, alias: dict,
               columnas: dict | None, no_proc: list, que: str) -> Hoja | None:
    rutas = hallar(docs / carpeta, *patrones)
    if not rutas:
        no_proc.append({"archivo": f"{carpeta}/", "motivo": f"no está {que}"})
        return None
    t = Hoja(rutas[-1], requeridas, opcionales, alias, columnas)
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        return None
    return t


def si(v) -> bool:
    return norm(v) in VERDAD


def control_id(v) -> str:
    """«A.8.13», «8.13» y «A 8.13 Respaldo» son el mismo control."""
    m = re.search(r"(\d+)\s*[.]\s*(\d+)", str(v or ""))
    return f"{int(m[1])}.{int(m[2])}" if m else norm(v)


PERIODOS = {"diaria": 1, "diario": 1, "semanal": 7, "quincenal": 15, "mensual": 31, "bimestral": 62, "trimestral": 92,
            "cuatrimestral": 123, "semestral": 183, "anual": 366, "daily": 1, "weekly": 7, "monthly": 31,
            "quarterly": 92, "semiannual": 183, "annual": 366, "yearly": 366}


def dias_de(v) -> int | None:
    """Una periodicidad en días: «trimestral», «90», «cada 90 días»."""
    n = norm(v)
    if not n:
        return None
    if n in PERIODOS:
        return PERIODOS[n]
    x = numero(re.sub(r"[^\d.,]", "", str(v)))
    return int(x) if x else None


# ================================================================ las severidades

SEVERIDADES = ("critica", "alta", "media", "baja")
SEV_SINONIMOS = {"critica": "critica", "critical": "critica", "critico": "critica", "urgente": "critica", "urgent": "critica",
                 "alta": "alta", "high": "alta", "alto": "alta", "importante": "alta",
                 "media": "media", "medium": "media", "moderada": "media", "moderate": "media", "medio": "media",
                 "baja": "baja", "low": "baja", "bajo": "baja",
                 "ninguna": "ninguna", "none": "ninguna", "info": "ninguna", "informational": "ninguna",
                 "informativa": "ninguna", "informativo": "ninguna", "log": "ninguna"}


def severidad_cvss(puntaje: float | None) -> str | None:
    """La escala cualitativa del CVSS (F-05, tabla 22): 0.0 ninguna; 0.1–3.9 baja; 4.0–6.9 media;
    7.0–8.9 alta; 9.0–10.0 crítica."""
    if puntaje is None:
        return None
    if puntaje <= 0:
        return "ninguna"
    if puntaje < 4.0:
        return "baja"
    if puntaje < 7.0:
        return "media"
    if puntaje < 9.0:
        return "alta"
    return "critica"


def severidad(texto, puntaje=None) -> str | None:
    """La severidad que dice el escáner o la política; si no la dice, la de su puntaje CVSS."""
    s = SEV_SINONIMOS.get(norm(texto))
    if s:
        return s
    m = re.match(r"^(\d)", norm(texto))
    if m and not puntaje:                                    # «4 - High», niveles numéricos de algunos escáneres
        return None
    return severidad_cvss(numero(puntaje)) if puntaje not in (None, "") else None


# ================================================================ las fechas con hora

def fecha_hora(v) -> dt.datetime | None:
    """«2026-09-14T10:30», «2026-09-14 10:30», «14/09/2026 10:30» o solo la fecha, a medianoche."""
    if v in (None, ""):
        return None
    if isinstance(v, dt.datetime):
        return v
    s = str(v).strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{1,2}):(\d{2}))?", s) or None
    if m:
        try:
            return dt.datetime(int(m[1]), int(m[2]), int(m[3]), int(m[4] or 0), int(m[5] or 0))
        except ValueError:
            return None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})(?:[T ](\d{1,2}):(\d{2}))?", s)
    if m:
        try:
            return dt.datetime(int(m[3]), int(m[2]), int(m[1]), int(m[4] or 0), int(m[5] or 0))
        except ValueError:
            return None
    d = fecha(s)
    return dt.datetime(d.year, d.month, d.day) if d else None


def horas(a: dt.datetime, b: dt.datetime) -> float:
    return round((b - a).total_seconds() / 3600, 1)


def fin_del_dia(d: dt.date) -> dt.datetime:
    return dt.datetime(d.year, d.month, d.day, 23, 59)


# ================================================================ el escáner y el catálogo KEV

# El catálogo KEV, como lo publica CISA (F-06): cada campo que el lector procesa, con su nombre en el
# archivo. La clave es el campo en families/criterio-ciso/fuentes.json; la puerta de las familias
# falla si el motor usa uno que no está verificado.
CAMPOS_KEV = {
    "cveID": "cve",
    "vendorProject": "fabricante",
    "product": "producto",
    "vulnerabilityName": "nombre",
    "dateAdded": "agregada",
    "dueDate": "vence",
    "knownRansomwareCampaignUse": "ransomware",
}

# La exportación de un escáner: ninguna marca entra en la 0.1.0 (ADR 0023). Las cabeceras de uso
# común, y el mapeo del setup (`scanner.columns`) para lo que no coincida.
ALIAS_ESCANER = {
    "activo": ["activo", "host", "hostname", "asset", "asset_name", "ip", "ip_address", "direccion_ip", "dns_name", "netbios_name", "equipo"],
    "vulnerabilidad": ["cve", "cves", "cve_id", "vulnerabilidad", "vulnerability_id", "plugin_id", "plugin", "qid", "id_vulnerabilidad"],
    "titulo": ["titulo", "title", "name", "plugin_name", "vulnerability", "nombre", "vulnerability_title"],
    "severidad": ["severidad", "severity", "risk", "riesgo", "risk_factor"],
    "cvss": ["cvss", "cvss_score", "cvss_base_score", "cvss_v4", "cvss_v4_0_base_score", "cvss_v3_base_score", "cvss_v3", "puntaje_cvss"],
    "primera": ["primera_deteccion", "first_found", "first_seen", "first_detected", "first_discovered", "detectada"],
    "fecha": ["fecha_escaneo", "scan_date", "fecha", "last_seen", "last_found"],
}
CVE = re.compile(r"CVE-\d{4}-\d{4,}", re.I)


def cves(v) -> list[str]:
    return sorted({x.upper() for x in CVE.findall(str(v or ""))})


def vuln_id(v) -> str:
    c = cves(v)
    return c[0] if c else str(v or "").strip()


def es_kev(p: Path) -> bool:
    n = norm(p.stem)
    return n.startswith("known_exploited") or n.startswith("kev") or n.startswith("catalogo_kev")


def catalogo_kev(docs: Path, no_proc: list) -> tuple[dict, str | None]:
    rutas = [p for p in (docs / "50-escaneos").iterdir() if p.is_file() and p.suffix.lower() in (".csv", ".xlsx") and es_kev(p)] \
        if (docs / "50-escaneos").is_dir() else []
    if not rutas:
        no_proc.append({"archivo": "50-escaneos/", "motivo": "no está el catálogo KEV de CISA (known_exploited_vulnerabilities.csv): sin él no se revisa lo explotado"})
        return {}, None
    ruta = sorted(rutas)[-1]
    t = Hoja(ruta, ["cveID", "dueDate"], [k for k in CAMPOS_KEV if k not in ("cveID", "dueDate")],
             {k: [norm(k)] for k in CAMPOS_KEV})
    if t.faltan:
        no_proc.append({"archivo": rel(ruta, docs), "motivo": f"el catálogo no trae {', '.join(t.faltan)} (F-06)"})
        return {}, rel(ruta, docs)
    out = {}
    for f in t.filas:
        c = str(f["cveID"]).strip().upper()
        if CVE.fullmatch(c):
            out[c] = {CAMPOS_KEV[k]: f.get(k) for k in CAMPOS_KEV} | {"vence": fecha(f.get("dueDate")), "agregada": fecha(f.get("dateAdded")),
                                                                      "cita": t.cita(f, docs)}
    return out, rel(ruta, docs)


def escaneos(docs: Path, cfg: dict, no_proc: list, excl: list) -> list[dict]:
    """Cada exportación del escáner con su fecha —la del nombre, o la más reciente de sus filas— y
    sus filas: un activo que aparece en una fila, aunque sea informativa, fue escaneado."""
    out = []
    carpeta = docs / "50-escaneos"
    cols = (cfg.get("scanner") or {}).get("columns") or {}
    for p in sorted(carpeta.iterdir()) if carpeta.is_dir() else []:
        if not p.is_file() or p.name.startswith(".") or es_kev(p) or _excluido(p, excl, docs):
            continue
        if p.suffix.lower() not in (".csv", ".xlsx"):
            no_proc.append({"archivo": rel(p, docs), "motivo": "una exportación del escáner se procesa en CSV o Excel"})
            continue
        t = Hoja(p, ["activo", "vulnerabilidad"], ["titulo", "severidad", "cvss", "primera", "fecha"], ALIAS_ESCANER, cols)
        if t.faltan:
            no_proc.append({"archivo": rel(p, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}: dilas en scanner.columns"})
            continue
        m = FECHA_EN_NOMBRE.search(p.name)
        f = dt.date(int(m[1]), int(m[2]), int(m[3])) if m else max((fecha(x.get("fecha")) for x in t.filas if fecha(x.get("fecha"))), default=None)
        if not f:
            no_proc.append({"archivo": rel(p, docs), "motivo": "sin la fecha del escaneo, en el nombre del archivo o en una columna"})
            continue
        filas = []
        sin_sev = 0
        for x in t.filas:
            s = severidad(x.get("severidad"), x.get("cvss"))
            if s is None:
                sin_sev += 1
            filas.append({"activo": str(x["activo"]).strip(), "a": norm(x["activo"]), "vuln": vuln_id(x["vulnerabilidad"]),
                          "cves": cves(x["vulnerabilidad"]) or cves(x.get("titulo")), "titulo": x.get("titulo") or "",
                          "sev": s, "primera": fecha(x.get("primera")), "cita": t.cita(x, docs)})
        if sin_sev:
            no_proc.append({"archivo": rel(p, docs), "motivo": f"{sin_sev} filas sin severidad ni puntaje CVSS: no se les aplica un plazo"})
        out.append({"archivo": rel(p, docs), "fecha": f, "filas": filas, "activos": {x["a"] for x in filas}})
    return sorted(out, key=lambda e: (e["fecha"], e["archivo"]))


# ================================================================ la configuración

DEFECTOS = {
    "thresholds": {"scan_window_days": 30},
    "vulnerability": {"sla_days": {}, "publish": False},
    "incident": {"containment_hours": {}, "review_days": None},
    "report": {"language": "es"},
}
SEVERIDAD = {
    "kev_past_due": 1, "incident_notification_late": 1, "control_without_evidence": 1, "vuln_past_sla": 1,
    "incident_response_late": 2, "risk_acceptance_expired": 2, "vuln_exception_expired": 2, "restore_test_overdue": 2,
    "vuln_closed_without_rescan": 2, "access_review_overdue": 2, "third_party_assessment_overdue": 2,
    "continuity_test_overdue": 2, "control_evidence_stale": 3, "soa_control_unassigned": 3, "asset_not_scanned": 3,
    "incident_without_review": 3,
}
N.SEVERIDAD.update(SEVERIDAD)


def umbral(cfg: dict, k: str):
    return (cfg.get("thresholds") or {}).get(k, DEFECTOS["thresholds"][k])


def plazos(cfg: dict, seccion: str, clave: str) -> dict:
    """Los plazos por severidad de la política, con la severidad canónica."""
    out = {}
    for k, v in ((cfg.get(seccion) or {}).get(clave) or {}).items():
        s = SEV_SINONIMOS.get(norm(k))
        if s in SEVERIDADES and numero(v) is not None:
            out[s] = numero(v)
    return out


def revisar_config(cfg: dict, rol: str) -> list[str]:
    p = []
    ent = cfg.get("entity") or {}
    for k in ("id", "name", "country"):
        if not ent.get(k):
            p.append(f"entity.{k} vacío")
    p += N.revisar_pais(ent)
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
    if not re.fullmatch(r"\d{4}-\d{2}", str(cfg.get("period") or "")):
        p.append("period vacío: el periodo que se evalúa, AAAA-MM")
    if rol == "guillermo":
        sla = plazos(cfg, "vulnerability", "sla_days")
        faltan = [s for s in SEVERIDADES if s not in sla]
        if faltan:
            p.append(f"vulnerability.sla_days: faltan los plazos de {', '.join(faltan)}, en días, como los dice la política de gestión de vulnerabilidades")
    if rol == "amparo":
        cont = plazos(cfg, "incident", "containment_hours")
        faltan = [s for s in SEVERIDADES if s not in cont]
        if faltan:
            p.append(f"incident.containment_hours: faltan los plazos de contención de {', '.join(faltan)}, en horas, como los dice la política de respuesta a incidentes")
        if numero((cfg.get("incident") or {}).get("review_days")) is None:
            p.append("incident.review_days vacío: los días que da la política para la revisión posterior de un incidente cerrado")
    return p


def _ficha(cfg: dict, rol: str, periodo: str) -> dict:
    return leer_json(cfg["_estado"] / SUB[rol] / periodo / "ficha.json", {}) or {}


def _campo(d: dict, *claves):
    for k in claves:
        if d.get(k) not in (None, ""):
            return d[k]
    return None


def _sin_ficha(docs: Path, carpeta: str, citadas: set, excl: list, aviso: str) -> list[str]:
    """Los documentos de una carpeta que la ficha no cita: se le dice a quien la escribe."""
    out = []
    citadas = {str(s).split(",")[0].strip() for s in citadas}       # «10-controles/x.pdf, p. 2» cita el archivo
    base = docs / carpeta
    for p in sorted(x for x in base.rglob("*") if x.is_file() and not x.name.startswith(".")) if base.is_dir() else []:
        if p.suffix.lower() in (".csv", ".xlsx") or _excluido(p, excl, docs):
            continue
        r = rel(p, docs)
        if r not in citadas:
            out.append(f"{r} no está en la ficha: {aviso}")
    return out


# ================================================================ Alexis · el gobierno y los controles

ALIAS_SOA = {"control": ["control", "id_control", "numero", "control_id", "codigo"], "nombre": ["nombre", "nombre_control", "control_name", "titulo"],
             "aplicable": ["aplicable", "aplica", "applicable", "incluido"], "estado": ["estado", "implementacion", "estado_implementacion", "status"],
             "responsable": ["responsable", "dueno", "owner", "propietario"], "periodicidad": ["periodicidad", "frecuencia", "frequency", "cada"],
             "justificacion": ["justificacion", "justification"]}
ALIAS_SISTEMAS = {"sistema": ["sistema", "system", "aplicacion"], "revision_dias": ["revision_dias", "revision_accesos_dias", "frecuencia_revision_dias", "cada_dias", "revision_de_accesos"],
                  "criticidad": ["criticidad", "criticality"], "responsable": ["responsable", "owner", "dueno"]}
ALIAS_TERCEROS = {"tercero": ["tercero", "proveedor", "third_party", "vendor"], "critico": ["critico", "critical", "es_critico"],
                  "evaluacion_dias": ["evaluacion_dias", "frecuencia_evaluacion_dias", "cada_dias", "reevaluacion_dias"],
                  "servicio": ["servicio", "service"]}
ALIAS_RIESGOS = {"riesgo": ["riesgo", "id", "id_riesgo", "codigo", "risk"], "descripcion": ["descripcion", "description"],
                 "decision": ["decision", "tratamiento", "treatment"], "aceptado_por": ["aceptado_por", "aprobado_por", "accepted_by"],
                 "revision": ["revision", "fecha_revision", "revisar_el", "vence", "vigencia", "review_date"]}
OPERANDO = ("implementado", "implementada", "operando", "operativo", "operativa", "en_operacion", "implemented", "operating")


def revisar_ficha_alexis(f: dict) -> list[str]:
    p = []
    for k, (lista, campos) in {"evidence": ("evidence", ("control", "date", "source")),
                               "access_reviews": ("access_reviews", ("system", "date", "source")),
                               "third_party_assessments": ("third_party_assessments", ("third_party", "date", "source"))}.items():
        for i, x in enumerate(f.get(lista) or []):
            for c in campos:
                if x.get(c) in (None, ""):
                    p.append(f"{k}[{i}]: falta {c}")
            if x.get("date") and not fecha(x.get("date")):
                p.append(f"{k}[{i}]: la fecha «{x.get('date')}» no es una fecha")
    for i, q in enumerate(f.get("questions") or []):
        if not (q.get("question") and q.get("answer")):
            p.append(f"questions[{i}]: lleva question y answer")
    return p


def alexis(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _pais(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "alexis", periodo)
    problemas = revisar_ficha_alexis(ficha)
    excl = excluidos(docs, cfg)
    al: list[dict] = []
    no_proc: list[dict] = list(excl)
    cols = cfg.get("columns") or {}

    # La evidencia de cada control, de la ficha.
    evid: dict[str, list] = {}
    for e in ficha.get("evidence") or []:
        d = fecha(e.get("date"))
        if d and d <= hoy:
            evid.setdefault(control_id(e.get("control")), []).append({"fecha": d, "fuente": e.get("source")})
    citadas = {str(x.get("source")) for k in ("evidence", "access_reviews", "third_party_assessments", "reviewed") for x in ficha.get(k) or []}
    for carpeta, que in (("10-controles", "es evidencia de un control; corre security-scan"),
                         ("20-accesos", "es una revisión de accesos; corre security-scan"),
                         ("30-terceros", "es la evaluación de un tercero; corre security-scan")):
        problemas += _sin_ficha(docs, carpeta, citadas, excl, que)

    # 1 · La declaración de aplicabilidad.
    controles = []
    soa = leer_tabla(docs, "00-referencia", ("declaracion", "soa", "aplicabilidad"), ["control", "aplicable"],
                     ["nombre", "estado", "responsable", "periodicidad", "justificacion"], ALIAS_SOA, cols.get("soa"), no_proc,
                     "la declaración de aplicabilidad")
    for x in soa.filas if soa else []:
        cid = control_id(x["control"])
        aplica, opera = si(x.get("aplicable")), norm(x.get("estado")) in OPERANDO
        per = dias_de(x.get("periodicidad"))
        ev = sorted(evid.get(cid, []), key=lambda e: e["fecha"])
        ultima = ev[-1] if ev else None
        vence = ultima["fecha"] + dt.timedelta(days=per) if ultima and per else None
        fila = {"control": cid, "nombre": x.get("nombre") or "", "aplicable": aplica, "estado": x.get("estado") or "",
                "responsable": x.get("responsable") or "", "periodicidad_dias": per, "evidencias": len(ev),
                "ultima": iso(ultima["fecha"]) if ultima else None, "vence": iso(vence)}
        controles.append(fila)
        if not aplica:
            continue
        cita = soa.cita(x, docs)
        nombre = f"{x['control']}{' · ' + x['nombre'] if x.get('nombre') else ''}"
        if not (x.get("responsable") or "").strip():
            al.append(alerta("soa_control_unassigned", f"{nombre}: aplicable y sin responsable en la declaración", cita, clave=f"responsable:{cid}"))
        if opera and not ev:
            al.append(alerta("control_without_evidence", f"{nombre}: figura «{x.get('estado')}» y la ficha no tiene ninguna evidencia de que operó",
                             cita, responsable=x.get("responsable") or None, clave=f"evidencia:{cid}"))
        elif opera and vence and vence < hoy:
            al.append(alerta("control_evidence_stale", f"{nombre}: la evidencia más reciente es del {iso(ultima['fecha'])} y su periodicidad es de {per} días; venció el {iso(vence)}",
                             [cita, {"archivo": ultima["fuente"]}], responsable=x.get("responsable") or None,
                             dias=(hoy - vence).days, clave=f"vigencia:{cid}"))

    # 2 · Las revisiones de acceso.
    revs: dict[str, list] = {}
    for r in ficha.get("access_reviews") or []:
        d = fecha(r.get("date"))
        if d and d <= hoy:
            revs.setdefault(norm(r.get("system")), []).append({"fecha": d, "fuente": r.get("source"), "revisor": r.get("reviewer")})
    sistemas = []
    t = leer_tabla(docs, "00-referencia", ("sistemas",), ["sistema", "revision_dias"], ["criticidad", "responsable"], ALIAS_SISTEMAS,
                   cols.get("systems"), no_proc, "la tabla de sistemas con la frecuencia de su revisión de accesos")
    for x in t.filas if t else []:
        dias = dias_de(x["revision_dias"])
        hechas = sorted(revs.get(norm(x["sistema"]), []), key=lambda e: e["fecha"])
        ultima = hechas[-1] if hechas else None
        vence = ultima["fecha"] + dt.timedelta(days=dias) if ultima and dias else None
        sistemas.append({"sistema": x["sistema"], "cada_dias": dias, "ultima": iso(ultima["fecha"]) if ultima else None, "vence": iso(vence),
                         "responsable": x.get("responsable") or ""})
        if not dias:
            continue
        if not ultima:
            al.append(alerta("access_review_overdue", f"{x['sistema']}: ninguna revisión de accesos registrada; la tabla pide una cada {dias} días",
                             t.cita(x, docs), responsable=x.get("responsable") or None, clave=f"accesos:{norm(x['sistema'])}"))
        elif vence < hoy:
            al.append(alerta("access_review_overdue", f"{x['sistema']}: la última revisión de accesos es del {iso(ultima['fecha'])}; tocaba el {iso(vence)}",
                             [t.cita(x, docs), {"archivo": ultima["fuente"]}], responsable=x.get("responsable") or None,
                             dias=(hoy - vence).days, clave=f"accesos:{norm(x['sistema'])}"))

    # 3 · Las evaluaciones de terceros críticos.
    evals: dict[str, list] = {}
    for r in ficha.get("third_party_assessments") or []:
        d = fecha(r.get("date"))
        if d and d <= hoy:
            evals.setdefault(norm(r.get("third_party")), []).append({"fecha": d, "fuente": r.get("source"), "resultado": r.get("result")})
    terceros = []
    t = leer_tabla(docs, "00-referencia", ("terceros",), ["tercero", "evaluacion_dias"], ["critico", "servicio"], ALIAS_TERCEROS,
                   cols.get("third_parties"), no_proc, "el registro de terceros con la frecuencia de su evaluación")
    for x in t.filas if t else []:
        critico = si(x.get("critico")) if x.get("critico") not in (None, "") else True
        dias = dias_de(x["evaluacion_dias"])
        hechas = sorted(evals.get(norm(x["tercero"]), []), key=lambda e: e["fecha"])
        ultima = hechas[-1] if hechas else None
        vence = ultima["fecha"] + dt.timedelta(days=dias) if ultima and dias else None
        terceros.append({"tercero": x["tercero"], "servicio": x.get("servicio") or "", "critico": critico, "cada_dias": dias,
                         "ultima": iso(ultima["fecha"]) if ultima else None, "resultado": ultima["resultado"] if ultima else None, "vence": iso(vence)})
        if not critico or not dias:
            continue
        if not ultima:
            al.append(alerta("third_party_assessment_overdue", f"{x['tercero']}: tercero crítico sin ninguna evaluación de seguridad registrada; el registro pide una cada {dias} días",
                             t.cita(x, docs), clave=f"tercero:{norm(x['tercero'])}"))
        elif vence < hoy:
            al.append(alerta("third_party_assessment_overdue", f"{x['tercero']}: la última evaluación es del {iso(ultima['fecha'])}; tocaba el {iso(vence)}",
                             [t.cita(x, docs), {"archivo": ultima["fuente"]}], dias=(hoy - vence).days, clave=f"tercero:{norm(x['tercero'])}"))

    # 4 · Las aceptaciones de riesgo.
    riesgos = []
    t = leer_tabla(docs, "40-riesgos", ("registro_riesgos", "riesgos"), ["riesgo", "decision", "revision"], ["descripcion", "aceptado_por"],
                   ALIAS_RIESGOS, cols.get("risks"), no_proc, "el registro de riesgos")
    for x in t.filas if t else []:
        acepta = norm(x["decision"]).startswith(("acept", "accept", "asum", "retener", "retain"))
        rev = fecha(x["revision"])
        riesgos.append({"riesgo": x["riesgo"], "descripcion": x.get("descripcion") or "", "decision": x["decision"],
                        "aceptado_por": x.get("aceptado_por") or "", "revision": iso(rev), "aceptado": acepta})
        if acepta and rev and rev < hoy:
            al.append(alerta("risk_acceptance_expired", f"{x['riesgo']}{' · ' + x['descripcion'] if x.get('descripcion') else ''}: aceptado"
                             f"{' por ' + x['aceptado_por'] if x.get('aceptado_por') else ''} hasta el {iso(rev)}, y no se volvió a revisar",
                             t.cita(x, docs), responsable=x.get("aceptado_por") or None, dias=(hoy - rev).days, clave=f"riesgo:{norm(x['riesgo'])}"))
        elif acepta and not rev:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"fila {x['_fila']}: el riesgo {x['riesgo']} está aceptado sin fecha de revisión"})

    partes = {
        "security-scan": {"evidencia": len(ficha.get("evidence") or []), "revisiones": len(ficha.get("access_reviews") or []),
                          "evaluaciones": len(ficha.get("third_party_assessments") or []), "excluidos": excl},
        "soa-status": {"controles": controles},
        "control-evidence": {"controles": [c for c in controles if c["aplicable"]]},
        "access-reviews": {"sistemas": sistemas},
        "third-parties": {"terceros": terceros},
        "risk-register": {"riesgos": riesgos},
    }
    vence = sorted(({"fecha": c["vence"], "que": f"{c['control']} · la evidencia vence", "caso": c["control"], "estado": "pendiente", "comando": "control-evidence"}
                    for c in controles if c["vence"] and 0 <= (fecha(c["vence"]) - hoy).days <= 30)
                   , key=lambda v: (v["fecha"], v["que"]))
    vence += sorted(({"fecha": s["vence"], "que": f"{s['sistema']} · revisión de accesos", "caso": s["sistema"], "estado": "pendiente", "comando": "access-reviews"}
                     for s in sistemas if s["vence"] and 0 <= (fecha(s["vence"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "alexis", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ Guillermo · las vulnerabilidades

ALIAS_ACTIVOS = {"activo": ["activo", "host", "hostname", "asset", "nombre", "equipo"], "alcance": ["alcance", "en_alcance", "in_scope", "escanear"],
                 "criticidad": ["criticidad", "criticality"], "responsable": ["responsable", "owner", "dueno"], "tipo": ["tipo", "type"]}
ALIAS_SEGUIMIENTO = {"activo": ALIAS_ESCANER["activo"], "vulnerabilidad": ALIAS_ESCANER["vulnerabilidad"],
                     "estado": ["estado", "status", "state"], "cierre": ["fecha_cierre", "cerrada_el", "closed_on", "resuelta_el", "cierre"],
                     "ticket": ["ticket", "caso", "id_ticket", "solicitud"]}
ALIAS_EXCEPCIONES = {"vulnerabilidad": ALIAS_ESCANER["vulnerabilidad"], "activo": ALIAS_ESCANER["activo"],
                     "vence": ["vence", "vencimiento", "valida_hasta", "expira", "expires"], "aprobada_por": ["aprobada_por", "aprobo", "approved_by"]}
CERRADA = ("cerrada", "cerrado", "closed", "resuelta", "resuelto", "remediada", "remediado", "fixed", "corregida", "corregido")


def guillermo(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _pais(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "guillermo", periodo)
    problemas = [f"questions[{i}]: lleva question y answer" for i, q in enumerate(ficha.get("questions") or []) if not (q.get("question") and q.get("answer"))]
    excl = excluidos(docs, cfg)
    al: list[dict] = []
    no_proc: list[dict] = list(excl)
    cols = cfg.get("columns") or {}
    sla = plazos(cfg, "vulnerability", "sla_days")
    publicar = bool((cfg.get("vulnerability") or {}).get("publish"))
    kev, kev_archivo = catalogo_kev(docs, no_proc)
    scans = [e for e in escaneos(docs, cfg, no_proc, excl) if e["fecha"] <= hoy]

    # Lo abierto: lo que encontró el último escaneo de cada activo.
    ultimo: dict[str, dict] = {}
    for e in scans:
        for a in e["activos"]:
            ultimo[a] = e
    primera: dict[tuple, dt.date] = {}
    for e in scans:
        for x in e["filas"]:
            if x["sev"] in (None, "ninguna"):
                continue
            k = (x["a"], x["vuln"])
            d = min(filter(None, [x["primera"], e["fecha"]]))
            primera[k] = min(primera.get(k, d), d)
    abiertas = {}
    for a, e in ultimo.items():
        for x in e["filas"]:
            if x["a"] == a and x["sev"] not in (None, "ninguna"):
                abiertas[(a, x["vuln"])] = dict(x, escaneo=e["archivo"], fecha_escaneo=e["fecha"], desde=primera[(a, x["vuln"])])

    # Las excepciones aprobadas.
    excepciones = []
    t = leer_tabla(docs, "60-remediacion", ("excepciones",), ["vulnerabilidad", "vence"], ["activo", "aprobada_por"], ALIAS_EXCEPCIONES,
                   cols.get("exceptions"), [], "el registro de excepciones")
    for x in t.filas if t else []:
        excepciones.append({"vuln": vuln_id(x["vulnerabilidad"]), "a": norm(x.get("activo")), "activo": x.get("activo") or "",
                            "vence": fecha(x["vence"]), "aprobada_por": x.get("aprobada_por") or "", "cita": t.cita(x, docs)})

    def excepcion(a: str, v: str) -> dict | None:
        return next((x for x in excepciones if x["vuln"] == v and x["a"] in ("", a)), None)

    # 1 · El plazo de cada severidad, y 2 · lo del catálogo KEV.
    filas = []
    for (a, v), x in sorted(abiertas.items()):
        edad = (hoy - x["desde"]).days
        plazo = sla.get(x["sev"])
        exc = excepcion(a, v)
        vigente = bool(exc and exc["vence"] and exc["vence"] >= hoy)
        en_kev = [c for c in (x["cves"] or ([v] if CVE.fullmatch(v) else [])) if c in kev]
        filas.append({"activo": x["activo"], "vulnerabilidad": v, "titulo": x["titulo"], "severidad": x["sev"], "desde": iso(x["desde"]),
                      "dias": edad, "plazo": plazo, "excepcion": iso(exc["vence"]) if exc else None, "kev": en_kev,
                      "kev_vence": iso(kev[en_kev[0]]["vence"]) if en_kev else None})
        if plazo is not None and edad > plazo and not vigente:
            al.append(alerta("vuln_past_sla", f"{x['activo']} · {v}{' · ' + x['titulo'] if x['titulo'] else ''}: {x['sev']}, abierta desde el {iso(x['desde'])} "
                             f"({edad} días) y la política da {int(plazo)} días", x["cita"], dias=edad - int(plazo), clave=f"sla:{a}:{v}"))
        for c in en_kev:
            k = kev[c]
            if k["vence"] and k["vence"] < hoy:
                al.append(alerta("kev_past_due", f"{x['activo']} · {c}: está en el catálogo KEV desde el {iso(k['agregada'])} con corrección al {iso(k['vence'])}, "
                                 f"y el escaneo del {iso(x['fecha_escaneo'])} la sigue encontrando"
                                 + (" · uso conocido en ransomware" if norm(k.get("ransomware")) == "known" else ""),
                                 [x["cita"], k["cita"]], dias=(hoy - k["vence"]).days, clave=f"kev:{a}:{c}"))

    # 3 · Las excepciones vencidas sobre lo que sigue abierto.
    for exc in excepciones:
        if not exc["vence"] or exc["vence"] >= hoy:
            continue
        sigue = [x for (a, v), x in abiertas.items() if v == exc["vuln"] and exc["a"] in ("", a)]
        if sigue:
            donde = exc["activo"] or "todos los activos"
            al.append(alerta("vuln_exception_expired", f"{exc['vuln']} en {donde}: la excepción venció el {iso(exc['vence'])} y la vulnerabilidad sigue abierta en "
                             f"{', '.join(sorted(x['activo'] for x in sigue))}", [exc["cita"]] + [x["cita"] for x in sigue[:2]],
                             responsable=exc["aprobada_por"] or None, dias=(hoy - exc["vence"]).days,
                             clave=f"excepcion:{exc['vuln']}:{exc['a'] or 'todos'}"))

    # 4 · Lo cerrado sin un escaneo que lo pruebe.
    cierres = []
    t = leer_tabla(docs, "60-remediacion", ("seguimiento", "remediacion"), ["activo", "vulnerabilidad", "estado"], ["cierre", "ticket"],
                   ALIAS_SEGUIMIENTO, cols.get("tracker"), no_proc, "el seguimiento de la remediación")
    for x in t.filas if t else []:
        if norm(x["estado"]) not in CERRADA:
            continue
        a, v, cerro = norm(x["activo"]), vuln_id(x["vulnerabilidad"]), fecha(x.get("cierre"))
        if not cerro:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"fila {x['_fila']}: cerrada sin fecha de cierre"})
            continue
        despues = [e for e in scans if e["fecha"] > cerro and a in e["activos"]]
        sigue = next((e for e in despues if any(y["a"] == a and y["vuln"] == v and y["sev"] not in (None, "ninguna") for y in e["filas"])), None)
        cierres.append({"ticket": x.get("ticket") or "", "activo": x["activo"], "vulnerabilidad": v, "cerrada": iso(cerro),
                        "escaneo_posterior": iso(despues[0]["fecha"]) if despues else None, "sigue": iso(sigue["fecha"]) if sigue else None})
        caso = f"{x.get('ticket') + ' · ' if x.get('ticket') else ''}{x['activo']} · {v}"
        if not despues:
            al.append(alerta("vuln_closed_without_rescan", f"{caso}: figura cerrada el {iso(cerro)} y ningún escaneo posterior incluye el activo",
                             t.cita(x, docs), dias=(hoy - cerro).days, clave=f"cierre:{a}:{v}"))
        elif sigue:
            al.append(alerta("vuln_closed_without_rescan", f"{caso}: figura cerrada el {iso(cerro)} y el escaneo del {iso(sigue['fecha'])} la sigue encontrando",
                             [t.cita(x, docs), {"archivo": sigue["archivo"]}], dias=(hoy - cerro).days, clave=f"cierre:{a}:{v}"))

    # 5 · Los activos del inventario sin escaneo en la ventana.
    ventana = int(umbral(cfg, "scan_window_days"))
    desde = hoy - dt.timedelta(days=ventana)
    cobertura = []
    inv = leer_tabla(docs, "00-referencia", ("inventario", "activos"), ["activo"], ["alcance", "criticidad", "responsable", "tipo"], ALIAS_ACTIVOS,
                     cols.get("assets"), no_proc, "el inventario de activos")
    inventariados = set()
    for x in inv.filas if inv else []:
        a = norm(x["activo"])
        inventariados.add(a)
        if x.get("alcance") not in (None, "") and not si(x["alcance"]):
            continue
        visto = max((e["fecha"] for e in scans if a in e["activos"]), default=None)
        cobertura.append({"activo": x["activo"], "criticidad": x.get("criticidad") or "", "ultimo_escaneo": iso(visto),
                          "en_ventana": bool(visto and visto >= desde)})
        if not visto or visto < desde:
            al.append(alerta("asset_not_scanned", f"{x['activo']}: " + (f"el último escaneo que lo incluye es del {iso(visto)}" if visto else "ningún escaneo lo incluye")
                             + f"; la ventana es de {ventana} días", inv.cita(x, docs), responsable=x.get("responsable") or None,
                             dias=(hoy - visto).days if visto else None, clave=f"cobertura:{a}"))
    fuera = sorted({x["activo"] for e in scans for x in e["filas"] if x["a"] not in inventariados}) if inv else []

    fuentes = ["F-05"] + (["F-06"] if kev else [])
    partes = {
        "vuln-scan": {"escaneos": [{"archivo": e["archivo"], "fecha": iso(e["fecha"]), "activos": len(e["activos"]),
                                    "hallazgos": sum(1 for x in e["filas"] if x["sev"] not in (None, "ninguna"))} for e in scans],
                      "kev": {"archivo": kev_archivo, "entradas": len(kev)}, "abiertas": len(abiertas), "excluidos": excl,
                      "fuentes": fuentes, "publicar": publicar},
        "vuln-sla": {"abiertas": filas, "plazos": {s: sla.get(s) for s in SEVERIDADES}, "excepciones": [
            {"vulnerabilidad": x["vuln"], "activo": x["activo"] or "todos", "vence": iso(x["vence"]), "aprobada_por": x["aprobada_por"]} for x in excepciones],
            "fuentes": ["F-05"], "publicar": publicar},
        "kev-check": {"en_kev": [f for f in filas if f["kev"]], "kev": {"archivo": kev_archivo, "entradas": len(kev)}, "fuentes": ["F-06"], "publicar": publicar},
        "scan-coverage": {"activos": cobertura, "ventana": ventana, "fuera_de_inventario": fuera, "cierres": cierres, "publicar": publicar},
    }
    vence = sorted(({"fecha": iso(x["desde"] + dt.timedelta(days=int(sla[x["sev"]]))), "que": f"{x['activo']} · {v} · plazo de {x['sev']}",
                     "caso": v, "estado": "pendiente", "comando": "vuln-sla"}
                    for (a, v), x in abiertas.items() if sla.get(x["sev"]) is not None
                    and 0 <= (x["desde"] + dt.timedelta(days=int(sla[x["sev"]])) - hoy).days <= 15), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "guillermo", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(scans[-1]["fecha"]) if scans else iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence if publicar else []}


# ================================================================ Amparo · la respuesta y la recuperación

ALIAS_MATRIZ = {"destinatario": ["destinatario", "a_quien", "notificar_a", "recipient", "autoridad"], "cuando": ["cuando", "condicion", "aplica", "when", "si"],
                "plazo_horas": ["plazo_horas", "horas", "plazo", "deadline_hours"], "norma": ["norma", "fuente", "regulacion", "base"]}
ALIAS_CALENDARIO = {"prueba": ["prueba", "nombre", "test", "plan"], "tipo": ["tipo", "type"], "frecuencia_dias": ["frecuencia_dias", "cada_dias", "frecuencia", "periodicidad"],
                    "sistema": ["sistema", "system", "respaldo"], "responsable": ["responsable", "owner"]}
CUANDO = {"todos": "todos", "todo": "todos", "siempre": "todos", "all": "todos",
          "critica": "critica", "criticos": "critica", "criticas": "critica", "solo_criticos": "critica",
          "alta_o_mas": "alta", "alta_o_superior": "alta", "critica_o_alta": "alta", "alta_y_critica": "alta",
          "datos_personales": "datos", "personales": "datos", "con_datos_personales": "datos",
          "clientes": "clientes", "clientes_afectados": "clientes", "afecta_clientes": "clientes"}
RESTAURACION = ("restauracion", "restore", "respaldo", "backup")


def revisar_ficha_amparo(f: dict) -> list[str]:
    p = []
    for i, x in enumerate(f.get("incidents") or []):
        for c in ("id", "severity", "detected_at", "source"):
            if x.get(c) in (None, ""):
                p.append(f"incidents[{i}]: falta {c}")
        if x.get("severity") and SEV_SINONIMOS.get(norm(x["severity"])) not in SEVERIDADES:
            p.append(f"incidents[{i}]: la severidad «{x['severity']}» no es crítica, alta, media ni baja")
        for c in ("detected_at", "contained_at"):
            if x.get(c) and not fecha_hora(x[c]):
                p.append(f"incidents[{i}]: {c} «{x[c]}» no es una fecha con hora")
        for j, n in enumerate(x.get("notifications") or []):
            for c in ("to", "at", "source"):
                if n.get(c) in (None, ""):
                    p.append(f"incidents[{i}].notifications[{j}]: falta {c}")
    for k, campos in (("reviews", ("incident", "date", "source")), ("tests", ("test", "date", "source"))):
        for i, x in enumerate(f.get(k) or []):
            for c in campos:
                if x.get(c) in (None, ""):
                    p.append(f"{k}[{i}]: falta {c}")
    for i, q in enumerate(f.get("questions") or []):
        if not (q.get("question") and q.get("answer")):
            p.append(f"questions[{i}]: lleva question y answer")
    return p


def aplica(cuando: str, inc: dict) -> bool:
    return (cuando == "todos" or (cuando == "critica" and inc["sev"] == "critica") or (cuando == "alta" and inc["sev"] in ("critica", "alta"))
            or (cuando == "datos" and inc["datos"]) or (cuando == "clientes" and inc["clientes"]))


def amparo(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _pais(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "amparo", periodo)
    problemas = revisar_ficha_amparo(ficha)
    excl = excluidos(docs, cfg)
    al: list[dict] = []
    no_proc: list[dict] = list(excl)
    cols = cfg.get("columns") or {}
    cont = plazos(cfg, "incident", "containment_hours")
    rev_dias = numero((cfg.get("incident") or {}).get("review_days"))
    corte = fin_del_dia(hoy)
    citadas = {str(x.get("source")) for x in ficha.get("incidents") or []} | \
              {str(n.get("source")) for x in ficha.get("incidents") or [] for n in x.get("notifications") or []} | \
              {str(x.get("source")) for k in ("reviews", "tests", "reviewed") for x in ficha.get(k) or []}
    for carpeta, que in (("70-incidentes", "es parte de un incidente; corre resilience-scan"), ("80-revisiones", "es la revisión de un incidente; corre resilience-scan"),
                         ("90-continuidad", "es una prueba de continuidad o de restauración; corre resilience-scan")):
        problemas += _sin_ficha(docs, carpeta, citadas, excl, que)

    # Los incidentes de la ficha, con su severidad canónica.
    incs = []
    for x in ficha.get("incidents") or []:
        det = fecha_hora(x.get("detected_at"))
        if not det:
            continue
        incs.append({"id": str(x.get("id")), "sev": SEV_SINONIMOS.get(norm(x.get("severity"))), "det": det, "cont": fecha_hora(x.get("contained_at")),
                     "cerrado": fecha(x.get("closed_on")), "datos": bool(x.get("personal_data")), "clientes": bool(x.get("customers_affected")),
                     "notifs": [{"a": n.get("to"), "cuando": fecha_hora(n.get("at")), "fuente": n.get("source")} for n in x.get("notifications") or []],
                     "fuente": x.get("source"), "titulo": x.get("title") or ""})
    revisiones = {}
    for r in ficha.get("reviews") or []:
        d = fecha(r.get("date"))
        if d:
            revisiones.setdefault(str(r.get("incident")), []).append({"fecha": d, "fuente": r.get("source")})

    # 1 · La contención contra el plazo de su severidad, y 3 · la revisión posterior.
    linea = []
    for i in sorted(incs, key=lambda x: (x["det"], x["id"])):
        limite = cont.get(i["sev"])
        tomo = horas(i["det"], i["cont"]) if i["cont"] else None
        rv = sorted(revisiones.get(i["id"], []), key=lambda e: e["fecha"])
        linea.append({"id": i["id"], "titulo": i["titulo"], "severidad": i["sev"], "detectado": i["det"].isoformat(timespec="minutes"),
                      "contenido": i["cont"].isoformat(timespec="minutes") if i["cont"] else None, "horas": tomo, "plazo_horas": limite,
                      "cerrado": iso(i["cerrado"]), "revision": iso(rv[0]["fecha"]) if rv else None})
        cita = {"archivo": i["fuente"]}
        if limite is not None:
            if tomo is not None and tomo > limite:
                al.append(alerta("incident_response_late", f"{i['id']}{' · ' + i['titulo'] if i['titulo'] else ''}: {i['sev']}, contenido en {tomo:g} horas y la política da {limite:g}",
                                 cita, dias=None, clave=f"contencion:{i['id']}"))
            elif tomo is None and horas(i["det"], corte) > limite:
                al.append(alerta("incident_response_late", f"{i['id']}{' · ' + i['titulo'] if i['titulo'] else ''}: {i['sev']}, detectado el {i['det'].isoformat(timespec='minutes')} "
                                 f"y sin contención registrada; la política da {limite:g} horas", cita, clave=f"contencion:{i['id']}"))
        if i["cerrado"] and rev_dias is not None:
            tope = i["cerrado"] + dt.timedelta(days=int(rev_dias))
            if not rv and tope < hoy:
                al.append(alerta("incident_without_review", f"{i['id']}: cerrado el {iso(i['cerrado'])} y sin revisión posterior; la política da {int(rev_dias)} días",
                                 cita, dias=(hoy - tope).days, clave=f"revision:{i['id']}"))
            elif rv and rv[0]["fecha"] > tope:
                al.append(alerta("incident_without_review", f"{i['id']}: cerrado el {iso(i['cerrado'])} y revisado el {iso(rv[0]['fecha'])}, fuera de los {int(rev_dias)} días de la política",
                                 [cita, {"archivo": rv[0]["fuente"]}], dias=(rv[0]["fecha"] - tope).days, clave=f"revision:{i['id']}"))

    # 2 · Las notificaciones de la matriz.
    notifs = []
    t = leer_tabla(docs, "00-referencia", ("matriz_notificaciones", "notificaciones"), ["destinatario", "cuando", "plazo_horas"], ["norma"],
                   ALIAS_MATRIZ, cols.get("notifications"), no_proc, "la matriz de notificaciones")
    reglas = []
    for x in t.filas if t else []:
        c = CUANDO.get(norm(x["cuando"]))
        h = numero(x["plazo_horas"])
        if not c or h is None:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"fila {x['_fila']}: «{x['cuando']}» no es todos, crítica, alta o más, datos personales ni clientes afectados, o el plazo no es un número de horas"})
            continue
        reglas.append({"destinatario": x["destinatario"], "cuando": c, "horas": h, "norma": x.get("norma") or "", "cita": t.cita(x, docs)})
    for i in sorted(incs, key=lambda x: (x["det"], x["id"])):
        for r in reglas:
            if not aplica(r["cuando"], i):
                continue
            tope = i["det"] + dt.timedelta(hours=r["horas"])
            d = norm(r["destinatario"])
            hecha = sorted((n for n in i["notifs"] if n["cuando"] and (d in norm(n["a"]) or norm(n["a"]) in d)), key=lambda n: n["cuando"])
            n = hecha[0] if hecha else None
            notifs.append({"incidente": i["id"], "destinatario": r["destinatario"], "tope": tope.isoformat(timespec="minutes"),
                           "hecha": n["cuando"].isoformat(timespec="minutes") if n else None, "norma": r["norma"],
                           "a_tiempo": bool(n and n["cuando"] <= tope)})
            k = f"notificacion:{i['id']}:{d}"
            if n and n["cuando"] > tope:
                al.append(alerta("incident_notification_late", f"{i['id']} → {r['destinatario']}: notificado el {n['cuando'].isoformat(timespec='minutes')}, "
                                 f"{horas(tope, n['cuando']):g} horas después del plazo de {r['horas']:g} horas{' (' + r['norma'] + ')' if r['norma'] else ''}",
                                 [r["cita"], {"archivo": n["fuente"]}], clave=k))
            elif not n and tope < corte:
                al.append(alerta("incident_notification_late", f"{i['id']} → {r['destinatario']}: la matriz pide notificar en {r['horas']:g} horas"
                                 f"{' (' + r['norma'] + ')' if r['norma'] else ''} y la ficha no registra la notificación",
                                 [r["cita"], {"archivo": i["fuente"]}], clave=k))

    # 4 · Las pruebas de continuidad, de recuperación y de restauración.
    hechas: dict[str, list] = {}
    for x in ficha.get("tests") or []:
        d = fecha(x.get("date"))
        if d and d <= hoy:
            hechas.setdefault(norm(x.get("test")), []).append({"fecha": d, "fuente": x.get("source"), "resultado": x.get("result")})
    pruebas = []
    t = leer_tabla(docs, "00-referencia", ("calendario",), ["prueba", "tipo", "frecuencia_dias"], ["sistema", "responsable"], ALIAS_CALENDARIO,
                   cols.get("calendar"), no_proc, "el calendario de continuidad")
    for x in t.filas if t else []:
        dias = dias_de(x["frecuencia_dias"])
        restaura = norm(x["tipo"]).startswith(RESTAURACION)
        k = norm(x["prueba"])
        lista = sorted(hechas.get(k, []), key=lambda e: e["fecha"])
        ultima = lista[-1] if lista else None
        vence = ultima["fecha"] + dt.timedelta(days=dias) if ultima and dias else None
        pruebas.append({"prueba": x["prueba"], "tipo": x["tipo"], "sistema": x.get("sistema") or "", "cada_dias": dias,
                        "ultima": iso(ultima["fecha"]) if ultima else None, "resultado": ultima["resultado"] if ultima else None, "vence": iso(vence)})
        if not dias or (ultima and vence >= hoy):
            continue
        detalle = (f"{x['prueba']}: ninguna prueba registrada; el calendario pide una cada {dias} días" if not ultima else
                   f"{x['prueba']}: la última prueba es del {iso(ultima['fecha'])}; tocaba el {iso(vence)}")
        kw = {"cita": t.cita(x, docs) if not ultima else [t.cita(x, docs), {"archivo": ultima["fuente"]}],
              "responsable": x.get("responsable") or None, "dias": (hoy - vence).days if ultima else None, "clave": f"prueba:{k}"}
        al.append(alerta("restore_test_overdue", detalle, **kw) if restaura else alerta("continuity_test_overdue", detalle, **kw))

    partes = {
        "resilience-scan": {"incidentes": len(incs), "revisiones": sum(len(v) for v in revisiones.values()), "pruebas": len(ficha.get("tests") or []),
                            "excluidos": excl, "fuentes": ["F-04"]},
        "incident-timeline": {"incidentes": linea, "plazos": {s: cont.get(s) for s in SEVERIDADES}, "revision_dias": rev_dias, "fuentes": ["F-04"]},
        "notifications": {"notificaciones": notifs},
        "continuity-tests": {"pruebas": pruebas},
    }
    vence = sorted(({"fecha": p["vence"], "que": f"{p['prueba']} · prueba", "caso": p["prueba"], "estado": "pendiente", "comando": "continuity-tests"}
                    for p in pruebas if p["vence"] and 0 <= (fecha(p["vence"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "amparo", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence}


def _pais(cfg: dict) -> None:
    N._PAIS[0] = N.pais_de(cfg)


# ================================================================ el reporte

NOMBRE = {"alexis": "Alexis", "guillermo": "Guillermo", "amparo": "Amparo"}
SENALES_DE = {
    "soa-status": {"soa_control_unassigned"},
    "control-evidence": {"control_without_evidence", "control_evidence_stale"},
    "access-reviews": {"access_review_overdue"},
    "third-parties": {"third_party_assessment_overdue"},
    "risk-register": {"risk_acceptance_expired"},
    "vuln-sla": {"vuln_past_sla", "vuln_exception_expired"},
    "kev-check": {"kev_past_due"},
    "scan-coverage": {"asset_not_scanned", "vuln_closed_without_rescan"},
    "incident-timeline": {"incident_response_late", "incident_without_review"},
    "notifications": {"incident_notification_late"},
    "continuity-tests": {"continuity_test_overdue", "restore_test_overdue"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-ciso")


def _si(b) -> str:
    return "sí" if b else "no"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    excl = p.get("excluidos") or []
    if comando == "security-scan":
        l += [f"**En la ficha:** {p['evidencia']} evidencias de controles, {p['revisiones']} revisiones de acceso y {p['evaluaciones']} evaluaciones de terceros.", ""]
    elif comando == "soa-status":
        l += ["| Control | Nombre | Aplicable | Estado | Responsable | Periodicidad |", "|---|---|---|---|---|---|"]
        l += [f"| {c['control']} | {c['nombre']} | {_si(c['aplicable'])} | {c['estado'] or '—'} | {c['responsable'] or '—'} | "
              f"{str(c['periodicidad_dias']) + ' días' if c['periodicidad_dias'] else '—'} |" for c in p["controles"]]
        l += ["", "La declaración la aprueba una persona: aquí se dice qué control aplicable no tiene responsable.", ""]
    elif comando == "control-evidence":
        l += ["| Control | Estado | Evidencias | La más reciente | Vence |", "|---|---|---|---|---|"]
        l += [f"| {c['control']} · {c['nombre']} | {c['estado'] or '—'} | {c['evidencias']} | {c['ultima'] or '—'} | {c['vence'] or '—'} |" for c in p["controles"]]
        l += ["", "Ningún control se declara cumplido aquí: se dice cuál no tiene evidencia de que operó.", ""]
    elif comando == "access-reviews":
        l += ["| Sistema | Cada | Última revisión | Tocaba | Responsable |", "|---|---|---|---|---|"]
        l += [f"| {s['sistema']} | {s['cada_dias'] or '—'} días | {s['ultima'] or '—'} | {s['vence'] or '—'} | {s['responsable'] or '—'} |" for s in p["sistemas"]]
        l.append("")
    elif comando == "third-parties":
        l += ["| Tercero | Servicio | Crítico | Cada | Última evaluación | Resultado | Tocaba |", "|---|---|---|---|---|---|---|"]
        l += [f"| {t['tercero']} | {t['servicio'] or '—'} | {_si(t['critico'])} | {t['cada_dias'] or '—'} días | {t['ultima'] or '—'} | {t['resultado'] or '—'} | {t['vence'] or '—'} |"
              for t in p["terceros"]]
        l.append("")
    elif comando == "risk-register":
        l += ["| Riesgo | Decisión | Aceptado por | Revisión |", "|---|---|---|---|"]
        l += [f"| {x['riesgo']} · {x['descripcion']} | {x['decision']} | {x['aceptado_por'] or '—'} | {x['revision'] or '—'} |" for x in p["riesgos"]]
        l += ["", "Ningún riesgo lo acepta el agente: aquí se dice qué aceptación pasó su fecha de revisión.", ""]
    elif comando == "vuln-scan":
        l += ["| Escaneo | Fecha | Activos | Hallazgos |", "|---|---|---|---|"]
        l += [f"| `{e['archivo']}` | {e['fecha']} | {e['activos']} | {e['hallazgos']} |" for e in p["escaneos"]]
        l += ["", f"**Abiertas en el último escaneo de cada activo:** {p['abiertas']} · **Catálogo KEV:** "
              f"{'`' + p['kev']['archivo'] + '`, ' + str(p['kev']['entradas']) + ' entradas' if p['kev']['archivo'] else 'no está'}.", ""]
    elif comando == "vuln-sla":
        pl = p["plazos"]
        l += ["**Plazos de la política:** " + " · ".join(f"{s} {int(pl[s]) if pl[s] is not None else '—'} días" for s in SEVERIDADES), "",
              "| Activo | Vulnerabilidad | Severidad | Abierta desde | Días | Plazo | Excepción hasta |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['activo']} | {x['vulnerabilidad']}{' · ' + x['titulo'] if x['titulo'] else ''} | {x['severidad']} | {x['desde']} | {x['dias']} | "
              f"{int(x['plazo']) if x['plazo'] is not None else '—'} | {x['excepcion'] or '—'} |" for x in p["abiertas"]]
        l.append("")
    elif comando == "kev-check":
        l += [f"**Catálogo KEV:** {'`' + p['kev']['archivo'] + '`, ' + str(p['kev']['entradas']) + ' entradas' if p['kev']['archivo'] else 'no está'}.", "",
              "| Activo | Vulnerabilidad | Severidad | Abierta desde | Corrección del catálogo |", "|---|---|---|---|---|"]
        l += [f"| {x['activo']} | {', '.join(x['kev'])} | {x['severidad']} | {x['desde']} | {x['kev_vence'] or '—'} |" for x in p["en_kev"]]
        l += ["", "La fecha de corrección es la que trae el catálogo de CISA (F-06); la directiva que la fija obliga a las agencias federales de los Estados Unidos, y el plazo de la organización es el de su política.", ""]
    elif comando == "scan-coverage":
        l += [f"**Ventana:** {p['ventana']} días.", "", "| Activo | Criticidad | Último escaneo | En la ventana |", "|---|---|---|---|"]
        l += [f"| {a['activo']} | {a['criticidad'] or '—'} | {a['ultimo_escaneo'] or '—'} | {_si(a['en_ventana'])} |" for a in p["activos"]]
        if p["fuera_de_inventario"]:
            l += ["", "**Escaneados y fuera del inventario:** " + ", ".join(p["fuera_de_inventario"]) + "."]
        l += ["", "| Ticket | Activo | Vulnerabilidad | Cerrada | Escaneo posterior | La sigue encontrando |", "|---|---|---|---|---|---|"]
        l += [f"| {c['ticket'] or '—'} | {c['activo']} | {c['vulnerabilidad']} | {c['cerrada']} | {c['escaneo_posterior'] or '—'} | {c['sigue'] or 'no'} |" for c in p["cierres"]]
        l.append("")
    elif comando == "resilience-scan":
        l += [f"**En la ficha:** {p['incidentes']} incidentes, {p['revisiones']} revisiones posteriores y {p['pruebas']} pruebas.", ""]
    elif comando == "incident-timeline":
        pl = p["plazos"]
        l += ["**Plazos de contención de la política:** " + " · ".join(f"{s} {pl[s]:g} h" if pl[s] is not None else f"{s} —" for s in SEVERIDADES)
              + (f" · **Revisión posterior:** {int(p['revision_dias'])} días" if p["revision_dias"] is not None else ""), "",
              "| Incidente | Severidad | Detectado | Contenido | Horas | Plazo | Cerrado | Revisión |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {i['id']}{' · ' + i['titulo'] if i['titulo'] else ''} | {i['severidad']} | {i['detectado']} | {i['contenido'] or '—'} | "
              f"{_m(i['horas']) if i['horas'] is not None else '—'} | {_m(i['plazo_horas']) if i['plazo_horas'] is not None else '—'} | {i['cerrado'] or '—'} | {i['revision'] or '—'} |"
              for i in p["incidentes"]]
        l.append("")
    elif comando == "notifications":
        l += ["| Incidente | Destinatario | Norma | Tope | Hecha | A tiempo |", "|---|---|---|---|---|---|"]
        l += [f"| {n['incidente']} | {n['destinatario']} | {n['norma'] or '—'} | {n['tope']} | {n['hecha'] or '—'} | {_si(n['a_tiempo'])} |" for n in p["notificaciones"]]
        l += ["", "La matriz es de la organización: los destinatarios y los plazos que exige cada norma los fija ella. Ninguna notificación la hace el agente.", ""]
    elif comando == "continuity-tests":
        l += ["| Prueba | Tipo | Sistema | Cada | Última | Resultado | Tocaba |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['prueba']} | {x['tipo']} | {x['sistema'] or '—'} | {x['cada_dias'] or '—'} días | {x['ultima'] or '—'} | {x['resultado'] or '—'} | {x['vence'] or '—'} |"
              for x in p["pruebas"]]
        l.append("")
    if excl:
        l += [f"**Excluidos por omisión:** {len(excl)} archivos —credenciales, llaves o respaldos— que el motor no abre: " + ", ".join(f"`{x['archivo']}`" for x in excl) + ".", ""]
    if comando in ("vuln-scan", "vuln-sla", "kev-check", "scan-coverage"):
        l += [("Se publica en Rostrum porque la configuración lo dice." if p.get("publicar") else
               "No se publica en Rostrum: un informe de vulnerabilidades abiertas es un mapa para un atacante (ADR 0023)."), ""]
    return l


# ================================================================ cuándo toca qué

def despertar(cfg: dict, rol: str, hoy: dt.date) -> dict:
    corr = registro_corridas(cfg["_estado"])
    ultima = lambda que: max((fecha(c["fecha"]) for c in corr if c["comando"] == que), default=None)  # noqa: E731
    periodo = cfg.get("period")
    toca, motivo = [], []
    if not periodo:
        return {"toca": [], "motivo": ["falta el periodo en la configuración"], "hoy": iso(hoy), "callado": False}
    docs = cfg["_docs"]
    nueva = lambda carpeta, desde: [p for p in (docs / carpeta).rglob("*") if p.is_file() and (not desde or dt.date.fromtimestamp(p.stat().st_mtime) >= desde)] if (docs / carpeta).is_dir() else []  # noqa: E731
    scan = {"alexis": "security-scan", "guillermo": "vuln-scan", "amparo": "resilience-scan"}[rol]
    carpetas = {"alexis": ("10-controles", "20-accesos", "30-terceros", "40-riesgos"), "guillermo": ("50-escaneos", "60-remediacion"),
                "amparo": ("70-incidentes", "80-revisiones", "90-continuidad")}[rol]
    u = ultima(scan)
    if not u or (hoy - u).days >= 7 or any(nueva(c, u) for c in carpetas) or nueva("00-referencia", u):
        toca.append(scan)
        motivo.append("documentos nuevos o la revisión semanal")
    r = {"alexis": alexis, "guillermo": guillermo, "amparo": amparo}[rol](cfg, periodo, hoy)
    for cmd, senales in SENALES_DE.items():
        if cmd in r["partes"] and any(a["signal"] in senales for a in r["alertas"]) and ultima(cmd) != hoy:
            toca.append(cmd)
            motivo.append(f"{sum(1 for a in r['alertas'] if a['signal'] in senales)} señales abiertas en {N.nombre_comando(cmd).lower()}")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-vulnerability": "guillermo", "criterio-resilience": "amparo"}.get(N.plugin(AQUI)["name"], "alexis")


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    periodo = a.period or cfg.get("period")
    if not periodo:
        raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
    r = {"alexis": alexis, "guillermo": guillermo, "amparo": amparo}[rol](cfg, periodo, hoy)
    destino = cfg["_estado"] / SUB[rol] / periodo / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Alexis, Guillermo y Amparo.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir", "excluidos", "escaneo",
                                       "compute", "reporte", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action == "excluidos":
        docs = a.docs
        cfg = {}
        if a.config:
            cfg, _ = N.cargar_config(a.config)
            docs = docs or cfg["_docs"]
        if not docs:
            ap.error("--docs o --config")
        print(json.dumps(excluidos(docs, cfg), ensure_ascii=False, indent=2))
        return 0
    if a.action == "escaneo":
        if not a.file:
            ap.error("--file es la exportación del escáner")
        cfg = {}
        if a.config:
            cfg, _ = N.cargar_config(a.config)
        t = Hoja(a.file, ["activo", "vulnerabilidad"], ["titulo", "severidad", "cvss", "primera", "fecha"], ALIAS_ESCANER,
                 (cfg.get("scanner") or {}).get("columns"))
        sin_sev = sum(1 for x in t.filas if severidad(x.get("severidad"), x.get("cvss")) is None)
        salida = {"columnas": {k: t.cabecera[i] for k, i in t.mapa.items()} if t.mapa else {}, "faltan": t.faltan, "filas": len(t.filas),
                  "sin_severidad": sin_sev, "fecha_en_el_nombre": bool(FECHA_EN_NOMBRE.search(a.file.name))}
        if t.faltan:
            salida["pregunta"] = (f"La exportación no trae una columna reconocible para {', '.join(t.faltan)}. Di cuál es, con su cabecera tal cual, "
                                  f"en scanner.columns; sin ella no se procesa.")
        print(json.dumps(salida, ensure_ascii=False, indent=2))
        return 0 if not t.faltan else 1
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=tuple(SUB.values()),
                       revisar_config=revisar_config, calcular=calcular, reporte=reporte, despertar=despertar,
                       excluir=lambda docs, cfg: [x["archivo"] for x in excluidos(docs, cfg)])


# ================================================================ la prueba del motor

def selftest() -> int:
    fallas = []

    def ok(nombre, obtenido, esperado):
        if obtenido == esperado:
            print(f"  ok  {nombre}")
        else:
            fallas.append(nombre)
            print(f"  FALLA  {nombre}: {obtenido!r} en lugar de {esperado!r}")

    hoy = dt.date(2026, 10, 15)
    ok("los países del registro pasan", [c for c in N.PAISES if N.revisar_pais({"country": c})], [])
    ok("la escala del CVSS (F-05)", [severidad_cvss(x) for x in (0.0, 0.1, 3.9, 4.0, 6.9, 7.0, 8.9, 9.0, 10.0)],
       ["ninguna", "baja", "baja", "media", "media", "alta", "alta", "critica", "critica"])
    ok("la severidad dicha manda sobre el puntaje", severidad("High", "9.8"), "alta")
    ok("sin severidad, la del puntaje", severidad("", "9.8"), "critica")
    ok("informativa no es una vulnerabilidad", severidad("None", None), "ninguna")
    ok("el mismo control escrito de tres formas", {control_id("A.8.13"), control_id("8.13"), control_id("A 8.13 Respaldo")}, {"8.13"})
    ok("una periodicidad en palabras o en días", [dias_de("trimestral"), dias_de("90"), dias_de("cada 30 días"), dias_de("")], [92, 90, 30, None])
    ok("una fecha con hora", fecha_hora("2026-09-14T10:30"), dt.datetime(2026, 9, 14, 10, 30))
    ok("una fecha con hora, día primero", fecha_hora("14/09/2026 10:30"), dt.datetime(2026, 9, 14, 10, 30))
    ok("los CVE de una celda", cves("CVE-2024-3400, cve-2023-4966"), ["CVE-2023-4966", "CVE-2024-3400"])
    ok("Guillermo sin los plazos de la política: la configuración no pasa",
       any("vulnerability.sla_days" in x for x in revisar_config({"entity": {"id": "1", "name": "x", "country": "CO"}, "period": "2026-10"}, "guillermo")), True)
    ok("Amparo sin los plazos de contención: la configuración no pasa",
       any("incident.containment_hours" in x for x in revisar_config({"entity": {"id": "1", "name": "x", "country": "CO"}, "period": "2026-10"}, "amparo")), True)
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "seguridad" / "e1", t / "estado" / "e1"
        ref = docs / "00-referencia"
        # Lo que nunca se procesa.
        (docs / "10-controles").mkdir(parents=True)
        (docs / "10-controles" / "servidor.pem").write_text("-----BEGIN", encoding="utf-8")
        (docs / "10-controles" / "credenciales-vpn.txt").write_text("x", encoding="utf-8")
        (docs / "10-controles" / "A.8.13_respaldo_2026-09.pdf").write_text("respaldo", encoding="utf-8")
        (docs / "10-controles" / "A.5.15_control-acceso_2026-03.pdf").write_text("acceso", encoding="utf-8")
        ok("las llaves y las credenciales se excluyen por omisión", [x["archivo"] for x in excluidos(docs, {})],
           ["10-controles/credenciales-vpn.txt", "10-controles/servidor.pem"])
        sys.path.insert(0, str(AQUI))
        import texto
        cache = Path(t) / "cache-convertir"
        man = texto.convertir(docs, cache, "10-controles", {x["archivo"] for x in excluidos(docs, {})})
        ok("convertir no deja copia de una credencial ni de una llave (CISO-4)",
           (sorted(p.name for p in cache.rglob("*.md") if p.name.startswith(("credenciales", "servidor"))),
            sorted(f["path"] for f in man["files"] if f.get("reason") == "excluido: no se abre")),
           ([], ["10-controles/credenciales-vpn.txt", "10-controles/servidor.pem"]))
        ref.mkdir(parents=True)
        _xlsx(ref / "declaracion-aplicabilidad.xlsx", [["Control", "Nombre", "Aplicable", "Estado", "Responsable", "Periodicidad"],
                                                      ["A.5.15", "Control de acceso", "Sí", "Implementado", "Ana", "trimestral"],
                                                      ["A.8.13", "Respaldo de la información", "Sí", "Implementado", "Luis", "mensual"],
                                                      ["A.8.16", "Actividades de monitoreo", "Sí", "Implementado", "", "mensual"],
                                                      ["A.7.4", "Monitoreo de la seguridad física", "No", "", "", ""]])
        _csv(ref / "sistemas.csv", [["sistema", "revision_dias", "responsable"], ["Core bancario", "90", "Ana"], ["Correo", "180", "Luis"]])
        _csv(ref / "terceros.csv", [["tercero", "servicio", "critico", "evaluacion_dias"], ["Nube Uno", "hosting", "sí", "365"], ["Papelería", "insumos", "no", "365"],
                                    ["Pagos Dos", "pasarela", "sí", "365"]])
        _csv(docs / "40-riesgos" / "registro-riesgos.csv", [["riesgo", "descripcion", "decision", "aceptado_por", "revision"],
                                                             ["R-01", "Sistema heredado sin soporte", "Aceptar", "Gerente general", "2026-09-30"],
                                                             ["R-02", "Sin doble factor en el correo", "Mitigar", "", "2026-12-31"]])
        escribir_json(est / "seguridad" / "2026-10" / "ficha.json", {
            "evidence": [{"control": "A.8.13", "date": "2026-09-30", "source": "10-controles/A.8.13_respaldo_2026-09.pdf"},
                         {"control": "A.5.15", "date": "2026-03-31", "source": "10-controles/A.5.15_control-acceso_2026-03.pdf"}],
            "access_reviews": [{"system": "Core bancario", "date": "2026-05-10", "reviewer": "Ana", "source": "20-accesos/revision-accesos_core_2026-05-10.pdf"}],
            "third_party_assessments": [{"third_party": "Nube Uno", "date": "2025-12-01", "result": "sin hallazgos", "source": "30-terceros/evaluacion_nube-uno_2025-12-01.pdf"}]})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-10", "_docs": docs, "_estado": est}
        r = alexis(cfg, "2026-10", hoy)
        ok("Alexis: sin evidencia, evidencia vencida, sin responsable, revisión de accesos, tercero y riesgo",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("access_review_overdue", "accesos:core_bancario"), ("access_review_overdue", "accesos:correo"),
            ("control_evidence_stale", "vigencia:5.15"), ("control_without_evidence", "evidencia:8.16"),
            ("risk_acceptance_expired", "riesgo:r_01"), ("soa_control_unassigned", "responsable:8.16"),
            ("third_party_assessment_overdue", "tercero:pagos_dos")])
        ok("Alexis: la ficha está completa y cita lo que hay", r["record_issues"], [])
        ok("Alexis: lo excluido queda en lo no procesado", sum(1 for x in r["no_procesado"] if x["motivo"].startswith("excluido")), 2)
        md = reporte(r, "control-evidence", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        # Guillermo.
        (docs / "50-escaneos").mkdir(parents=True)
        cab = ["Host", "Plugin ID", "CVE", "Name", "Risk", "CVSS v4.0 Base Score", "First Found"]
        _csv(docs / "50-escaneos" / "escaneo-2026-08-20.csv", [cab,
             ["srv-01", "1001", "CVE-2024-3400", "Firewall RCE", "Critical", "10.0", "2026-08-20"],
             ["srv-01", "1002", "CVE-2023-1111", "TLS débil", "Medium", "5.3", "2026-08-20"],
             ["srv-02", "19506", "", "Información del escaneo", "None", "", ""],
             ["srv-03", "1003", "CVE-2022-2222", "Librería vieja", "", "7.5", "2026-06-01"]])
        _csv(docs / "50-escaneos" / "escaneo-2026-10-10.csv", [cab,
             ["srv-01", "1001", "CVE-2024-3400", "Firewall RCE", "Critical", "10.0", "2026-08-20"],
             ["srv-02", "1004", "CVE-2025-5555", "Servidor web", "High", "8.1", "2026-10-10"],
             ["srv-03", "1003", "CVE-2022-2222", "Librería vieja", "", "7.5", "2026-06-01"]])
        _csv(docs / "50-escaneos" / "known_exploited_vulnerabilities.csv",
             [["cveID", "vendorProject", "product", "vulnerabilityName", "dateAdded", "shortDescription", "requiredAction", "dueDate",
               "knownRansomwareCampaignUse", "forensicTriage", "notes", "cwes"],
              ["CVE-2024-3400", "Palo Alto Networks", "PAN-OS", "Command Injection", "2024-04-12", "x", "x", "2024-04-19", "Known", "No", "", "CWE-77"]])
        _csv(ref / "inventario-activos.csv", [["activo", "alcance", "criticidad"], ["srv-01", "sí", "alta"], ["srv-02", "sí", "media"],
                                              ["srv-03", "sí", "media"], ["srv-04", "sí", "alta"], ["laptop-99", "no", "baja"]])
        _csv(docs / "60-remediacion" / "excepciones.csv", [["vulnerabilidad", "activo", "aprobada_por", "vence"], ["CVE-2022-2222", "srv-03", "CISO", "2026-09-30"]])
        _csv(docs / "60-remediacion" / "seguimiento.csv", [["ticket", "activo", "vulnerabilidad", "estado", "fecha_cierre"],
                                                           ["TK-10", "srv-01", "CVE-2023-1111", "Cerrada", "2026-09-01"],
                                                           ["TK-11", "srv-01", "CVE-2024-3400", "Cerrada", "2026-09-15"],
                                                           ["TK-12", "srv-03", "CVE-2022-9999", "Cerrada", "2026-10-12"]])
        cfg["vulnerability"] = {"sla_days": {"Crítica": 15, "Alta": 30, "Media": 90, "Baja": 180}}
        r = guillermo(cfg, "2026-10", hoy)
        ok("Guillermo: plazo, KEV, excepción vencida, cierre sin escaneo que lo pruebe y cobertura",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("asset_not_scanned", "cobertura:srv_04"), ("kev_past_due", "kev:srv_01:CVE-2024-3400"),
            ("vuln_closed_without_rescan", "cierre:srv_01:CVE-2024-3400"), ("vuln_closed_without_rescan", "cierre:srv_03:CVE-2022-9999"),
            ("vuln_exception_expired", "excepcion:CVE-2022-2222:srv_03"), ("vuln_past_sla", "sla:srv_01:CVE-2024-3400"),
            ("vuln_past_sla", "sla:srv_03:CVE-2022-2222")])
        ok("Guillermo: lo que el último escaneo no encontró ya no está abierto",
           sorted((x["activo"], x["vulnerabilidad"]) for x in r["partes"]["vuln-sla"]["abiertas"]),
           [("srv-01", "CVE-2024-3400"), ("srv-02", "CVE-2025-5555"), ("srv-03", "CVE-2022-2222")])
        ok("Guillermo: la severidad de la fila sin severidad sale de su puntaje",
           next(x["severidad"] for x in r["partes"]["vuln-sla"]["abiertas"] if x["activo"] == "srv-03"), "alta")
        ok("Guillermo: lo de vulnerabilidades no se publica por omisión", r["partes"]["vuln-sla"]["publicar"], False)
        # Amparo.
        _csv(ref / "matriz-notificaciones.csv", [["destinatario", "cuando", "plazo_horas", "norma"],
                                                 ["Superintendencia", "crítica", "24", "Circular de ejemplo"],
                                                 ["Autoridad de datos", "datos personales", "72", "Ley de datos de ejemplo"],
                                                 ["Comité de riesgos", "todos", "48", "Política interna"]])
        _csv(ref / "calendario-continuidad.csv", [["prueba", "tipo", "sistema", "frecuencia_dias", "responsable"],
                                                  ["Plan de continuidad del core", "continuidad", "Core bancario", "365", "Ana"],
                                                  ["Restauración del core", "restauración", "Core bancario", "90", "Luis"],
                                                  ["Recuperación del centro alterno", "recuperación", "Centro de datos", "180", "Ana"]])
        cfg["incident"] = {"containment_hours": {"critica": 4, "alta": 24, "media": 72, "baja": 168}, "review_days": 15}
        escribir_json(est / "resiliencia" / "2026-10" / "ficha.json", {
            "incidents": [{"id": "INC-0101", "title": "Ransomware en un servidor", "severity": "crítica", "detected_at": "2026-09-01T08:00",
                           "contained_at": "2026-09-01T15:30", "closed_on": "2026-09-10", "personal_data": True, "customers_affected": False,
                           "notifications": [{"to": "Superintendencia Financiera", "at": "2026-09-02T06:00", "source": "70-incidentes/INC-0101_nota-super.pdf"},
                                             {"to": "Comité de riesgos", "at": "2026-09-01T18:00", "source": "70-incidentes/INC-0101_acta.pdf"}],
                           "source": "70-incidentes/INC-0101_informe.docx"},
                          {"id": "INC-0102", "severity": "media", "detected_at": "2026-10-01T09:00", "contained_at": "2026-10-02T10:00",
                           "closed_on": "2026-10-05", "notifications": [{"to": "Comité de riesgos", "at": "2026-10-04T09:00", "source": "70-incidentes/INC-0102_acta.pdf"}],
                           "source": "70-incidentes/INC-0102_informe.docx"}],
            "reviews": [{"incident": "INC-0102", "date": "2026-10-08", "source": "80-revisiones/INC-0102_revision.pdf"}],
            "tests": [{"test": "Plan de continuidad del core", "date": "2026-02-10", "result": "exitosa", "source": "90-continuidad/prueba-continuidad_2026-02-10.pdf"},
                      {"test": "Restauración del core", "date": "2026-06-01", "result": "exitosa", "source": "90-continuidad/prueba-restauracion_2026-06-01.pdf"}]})
        r = amparo(cfg, "2026-10", hoy)
        ok("Amparo: contención tarde, notificaciones tarde y sin hacer, sin revisión y pruebas vencidas",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("continuity_test_overdue", "prueba:recuperacion_del_centro_alterno"), ("incident_notification_late", "notificacion:INC-0101:autoridad_de_datos"),
            ("incident_notification_late", "notificacion:INC-0102:comite_de_riesgos"),
            ("incident_response_late", "contencion:INC-0101"), ("incident_without_review", "revision:INC-0101"),
            ("restore_test_overdue", "prueba:restauracion_del_core")])
        (t / "salida.md").write_text("lo que se mostró", encoding="utf-8")
        N.corrida(est, "notifications", t / "salida.md", "2026-10", None, hoy, r, "0.0.0")
        c = leer_json(est / "corridas.json", [])[-1]
        ok("la corrida queda en el formato común, con sus hallazgos por caso", (c["que"], c["hallazgos"], "INC-0101" in c["por_caso"]), ("notifications", 6, True))
    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
