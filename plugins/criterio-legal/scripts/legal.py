#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CLO: lo que calcula el código para Fidel y para Constanza.

    python3 legal.py <acción> [opciones]       python3 legal.py --help

Fidel (criterio-legal) procesa lo que la empresa firmó; Constanza (criterio-compliance), la
matriz de obligaciones de la organización contra su evidencia. Los dos comparten este motor,
que vive en criterio-legal y se copia a criterio-compliance con scripts/sincronizar.py, y el
núcleo común de las familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —el registro de
contratos, los pagos, la matriz de atribuciones, la matriz de obligaciones, el índice de
políticas, el registro normativo, los casos del canal— las procesa el código. Lo que solo trae
un documento escrito —cada contrato con sus fechas, firmantes, otrosíes, garantías y
obligaciones; cada póliza; el certificado de la contraparte; lo que declara un informe— lo
extrae el agente a su ficha, con la cita, y el código lo cruza.

**Sin opinión jurídica.** Nada aquí interpreta una cláusula ni una norma, ni califica la validez
de un contrato o de una firma: compara fechas, montos y facultades con lo que dicen los
documentos y la matriz de la organización (ADR 0009).

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
from nucleo import (  # noqa: E402
    ALIAS, CRITICIDAD, Tabla, _PAIS, _csv, _hoy, _m, alerta, buscar, dia_habil, escribir_json, fecha,
    fin_de_mes, iso, leer_json, marco_reporte, mon, norm, numero, ordenar, redondo,
    registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"

ALIAS.update({
    "codigo": ["codigo", "codigo_contrato", "contrato", "id_contrato", "id"],
    "contraparte": ["contraparte", "proveedor", "cliente", "tercero"],
    "objeto": ["objeto", "descripcion"],
    "tipo": ["tipo", "tipo_contrato", "categoria"],
    "inicio": ["inicio", "fecha_inicio", "desde_contrato"],
    "terminacion": ["terminacion", "fecha_terminacion", "fin", "vence", "vencimiento"],
    "contrato": ["contrato", "codigo_contrato", "codigo"],
    "cargo": ["cargo", "rol"],
    "monto_maximo": ["monto_maximo", "tope", "limite", "cuantia"],
    "desde": ["desde", "vigente_desde"],
    "hasta": ["hasta", "vigente_hasta"],
    "obligacion": ["obligacion", "requisito"],
    "fuente": ["fuente", "origen", "norma_contrato_politica"],
    "periodicidad": ["periodicidad", "frecuencia"],
    "politica": ["politica", "nombre_politica"],
    "proxima_revision": ["proxima_revision", "revision", "fecha_revision"],
    "aprobada": ["aprobada", "fecha_aprobacion"],
    "norma": ["norma", "titulo"],
    "registrada": ["registrada", "fecha_registro"],
    "publicada": ["publicada", "fecha_publicacion"],
    "aplica": ["aplica"],
    "evaluacion": ["evaluacion", "fecha_evaluacion", "evaluada"],
    "recibido": ["recibido", "fecha_recepcion", "recepcion"],
    "respondido": ["respondido", "fecha_respuesta", "respuesta"],
})

DEFECTOS = {
    "thresholds": {
        "contract_warning_days": 60,      # un vencimiento dentro de estos días sin decisión se señala
        "notice_warning_days": 30,        # una fecha de preaviso dentro de estos días se señala
        "certificate_max_days": 30,       # antigüedad máxima del certificado de la contraparte al firmar
        "amount_tolerance": 1.0,          # diferencia de montos que no es diferencia
        "case_response_days": 15,         # plazo de respuesta de un caso del canal
        "norm_assessment_days": 30,       # días para evaluar el impacto de una norma registrada
        "renewal_months": 12,             # cuánto se prorroga un contrato con renovación automática si la ficha no lo dice
    },
    "holidays": [],
    "report": {"language": "es"},
    "execution": {"workers": 1},
}
SEVERIDAD = {
    "renewal_notice_missed": 1, "signed_without_authority": 1, "payments_over_value": 1, "contract_expired_active": 1,
    "declared_compliance_vs_evidence": 1, "compliance_obligation_overdue": 1, "report_case_overdue": 1,
    "notice_deadline_near": 2, "contract_expiring": 2, "unsigned_contract": 2, "payment_after_termination": 2,
    "guarantee_missing": 2, "guarantee_expires_early": 2, "contract_obligation_overdue": 2, "register_mismatch": 2,
    "compliance_done_without_evidence": 2, "regulatory_change_unassessed": 2, "applicable_norm_not_in_matrix": 2,
    "contract_obligation_not_in_matrix": 2, "register_differs_from_contract": 3, "counterparty_certificate_stale": 3,
    "compliance_evidence_stale": 3, "obligation_without_owner": 3, "obligation_without_source": 3, "policy_review_overdue": 3,
}
N.SEVERIDAD.update(SEVERIDAD)
VENTANA = {"mensual": 1, "bimestral": 2, "trimestral": 3, "semestral": 6, "anual": 12}
SI = ("si", "sí", "s", "yes", "true", "x", "aplica")


def umbral(cfg: dict, k: str):
    return (cfg.get("thresholds") or {}).get(k, DEFECTOS["thresholds"][k])


def sumar_meses(d: dt.date, meses: int) -> dt.date:
    m = d.month - 1 + meses
    a, m = d.year + m // 12, m % 12 + 1
    import calendar
    return dt.date(a, m, min(d.day, calendar.monthrange(a, m)[1]))


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
    if rol == "constanza" and not cfg.get("period"):
        p.append("period vacío: el periodo de cumplimiento que se evalúa")
    return p


def _evidencia(carpeta: Path, ident_: str, docs: Path) -> list[str]:
    if not carpeta.is_dir():
        return []
    return [rel(p, docs) for p in sorted(carpeta.rglob("*")) if p.is_file() and not p.name.startswith(".")
            and (norm(p.name).startswith(norm(ident_) + "_") or norm(p.stem) == norm(ident_))]


# ================================================================ Fidel · los contratos

def carpetas_contratos(docs: Path) -> dict[str, Path]:
    """Cada carpeta de `contratos/`, por el código con que empieza su nombre."""
    base = docs / "contratos"
    out = {}
    for d in sorted(x for x in base.iterdir() if x.is_dir()) if base.is_dir() else []:
        m = re.match(r"([A-Za-z]+-\d+)", d.name)
        out[(m[1] if m else d.name).upper()] = d
    return out


def fichas_contratos(estado: Path) -> dict[str, dict]:
    base = estado / "contratos"
    out = {}
    for f in sorted(base.glob("*.json")) if base.is_dir() else []:
        d = leer_json(f, {}) or {}
        if d.get("code"):
            out[str(d["code"]).upper()] = d
    return out


def revisar_ficha_contrato(c: dict) -> list[str]:
    p, code = [], c.get("code") or "?"
    for k in ("code", "start", "end", "source"):
        if not c.get(k):
            p.append(f"{code}: falta {k}")
    if numero(c.get("value")) is None:
        p.append(f"{code}: value no es un número")
    if not isinstance(c.get("signed_by_both"), bool):
        p.append(f"{code}: signed_by_both es verdadero o falso, según el documento")
    for k in ("start", "end", "signed_on"):
        if c.get(k) and not fecha(c[k]):
            p.append(f"{code}: {k} no es una fecha; una fecha que nadie dijo se deja vacía")
    for o in c.get("obligations") or []:
        if not o.get("id") or not o.get("source"):
            p.append(f"{code}: cada obligación lleva id y source")
    for g in c.get("guarantees_required") or []:
        if not g.get("type") or not (g.get("until") or g.get("months_after_end") is not None):
            p.append(f"{code}: cada garantía exigida lleva type y until o months_after_end")
    return p


def fin_documentado(c: dict) -> dt.date | None:
    """La terminación que dice el documento: la del contrato o la del último otrosí que la cambió."""
    fin = fecha(c.get("end"))
    for o in sorted(c.get("amendments") or [], key=lambda x: x.get("date") or ""):
        if o.get("new_end") and o.get("signed", True):
            fin = fecha(o["new_end"]) or fin
    return fin


def fin_efectivo(c: dict, hoy: dt.date, cfg: dict) -> dt.date | None:
    """Con renovación automática y sin decisión de terminar, el contrato se prorroga: lo dice el
    contrato, no el agente."""
    fin = fin_documentado(c)
    dec = norm((c.get("decision") or {}).get("action"))
    if fin and c.get("auto_renewal") and dec != "terminar":
        meses = int(c.get("renewal_months") or umbral(cfg, "renewal_months"))
        while fin < hoy:
            fin = sumar_meses(fin, meses)
    return fin


def valor_total(c: dict) -> float:
    return (numero(c.get("value")) or 0.0) + sum(numero(o.get("added_value")) or 0.0 for o in c.get("amendments") or [] if o.get("signed", True))


def fidel(cfg: dict, hoy: dt.date) -> dict:
    _PAIS[0] = N.pais_de(cfg)
    docs, estado = cfg["_docs"], cfg["_estado"]
    fichas = fichas_contratos(estado)
    carpetas = carpetas_contratos(docs)
    problemas = [x for c in fichas.values() for x in revisar_ficha_contrato(c)]
    tol = umbral(cfg, "amount_tolerance")
    dias_v, dias_p = umbral(cfg, "contract_warning_days"), umbral(cfg, "notice_warning_days")
    al: list[dict] = []
    no_proc: list[dict] = []
    cols = cfg.get("columns") or {}

    # El registro contra las carpetas y las fichas.
    registro = {}
    rf = buscar(docs / "10-registro", "registro")
    if rf:
        t = Tabla(rf[0], ["codigo", "valor", "terminacion", "estado"], ["contraparte", "objeto", "tipo", "inicio", "responsable"], cols.get("register"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            for f in t.filas:
                registro[str(f["codigo"]).strip().upper()] = dict(f, cita=t.cita(f, docs))
    else:
        no_proc.append({"archivo": "10-registro/", "motivo": "no está el registro de contratos"})
    filas_registro = []
    for code in sorted(set(carpetas) | set(registro)):
        en_carpeta = code in carpetas and any((carpetas[code] / "10-contrato").glob("*")) if code in carpetas else False
        if code in carpetas and code not in registro:
            al.append(alerta("register_mismatch", f"{code}: el contrato está en la carpeta y no en el registro",
                             {"archivo": rel(carpetas[code], docs) + "/"}, clave=f"carpeta:{code}"))
        if code in registro and not en_carpeta:
            al.append(alerta("register_mismatch", f"{code}: está en el registro y no hay documento en contratos/{code}…/10-contrato/",
                             registro[code]["cita"], clave=f"registro:{code}"))
        c, r = fichas.get(code), registro.get(code)
        fila = {"codigo": code, "contraparte": (r or {}).get("contraparte") or ((c or {}).get("counterparty") or {}).get("name"),
                "estado_declarado": (r or {}).get("estado"), "estado_fechas": None, "diferencias": []}
        if c:
            fe = fin_efectivo(c, hoy, cfg)
            fila["estado_fechas"] = "vigente" if fe and fe >= hoy else "terminado"
            fila["terminacion"] = iso(fin_documentado(c))
        if c and r:
            if norm(r.get("estado")) in ("vigente", "activo", "en_ejecucion") and fila["estado_fechas"] == "terminado":
                al.append(alerta("contract_expired_active", f"{code}: el registro lo reporta {r.get('estado')} y terminó el {fila['terminacion']}",
                                 [r["cita"], {"archivo": c.get("source")}], clave=f"vigente:{code}"))
            vr, vf = numero(r.get("valor")), valor_total(c)
            if vr is not None and abs(vr - vf) > tol:
                fila["diferencias"].append(f"valor {mon(vr)} en el registro y {mon(vf)} en el documento")
            tr, tf = fecha(r.get("terminacion")), fin_documentado(c)
            if tr and tf and tr != tf:
                fila["diferencias"].append(f"terminación {iso(tr)} en el registro y {iso(tf)} en el documento")
            if fila["diferencias"]:
                al.append(alerta("register_differs_from_contract", f"{code}: " + "; ".join(fila["diferencias"]),
                                 [r["cita"], {"archivo": c.get("source")}], clave=f"difiere:{code}"))
        filas_registro.append(fila)
    for code in sorted(set(carpetas) - set(fichas)):
        no_proc.append({"archivo": rel(carpetas[code], docs) + "/", "motivo": f"{code} no tiene ficha: corre contract-scan"})

    # Vencimientos, preavisos y obligaciones.
    calendario = []
    for code, c in sorted(fichas.items()):
        fin = fin_documentado(c)
        dec = norm((c.get("decision") or {}).get("action"))
        cita = {"archivo": c.get("source")}
        if fin:
            calendario.append({"codigo": code, "que": "terminación", "fecha": iso(fin), "dias": (fin - hoy).days})
        if fin and c.get("auto_renewal"):
            limite = fin - dt.timedelta(days=int(c.get("notice_days") or 0))
            calendario.append({"codigo": code, "que": "límite del preaviso", "fecha": iso(limite), "dias": (limite - hoy).days})
            if not dec:
                if 0 <= (limite - hoy).days <= dias_p:
                    al.append(alerta("notice_deadline_near", f"{code}: el preaviso de no renovación vence el {iso(limite)}, en {(limite - hoy).days} días, y nadie decidió",
                                     cita, dias=(limite - hoy).days, clave=f"preaviso:{code}"))
                elif limite < hoy <= fin:
                    al.append(alerta("renewal_notice_missed", f"{code}: el preaviso venció el {iso(limite)} sin decisión; el contrato se prorroga en sus términos el {iso(fin)}",
                                     cita, dias=(hoy - limite).days, clave=f"preaviso:{code}"))
        elif fin and not dec and 0 <= (fin - hoy).days <= dias_v:
            al.append(alerta("contract_expiring", f"{code}: vence el {iso(fin)}, en {(fin - hoy).days} días, sin decisión de renovar o terminar",
                             cita, valor_total(c), dias=(fin - hoy).days, clave=f"vence:{code}"))
        ejec = (carpetas[code] / "40-ejecucion") if code in carpetas else None
        for o in c.get("obligations") or []:
            d = fecha(o.get("due"))
            ev = _evidencia(ejec, o["id"], docs) if ejec else []
            calendario.append({"codigo": code, "que": f"obligación {o['id']} · {o.get('what')}", "fecha": iso(d), "dias": (d - hoy).days if d else None,
                               "evidencia": ev})
            if d and d < hoy and not ev:
                al.append(alerta("contract_obligation_overdue", f"{code} · {o['id']} · {o.get('what')}: venció el {iso(d)} y no hay evidencia en 40-ejecucion/",
                                 {"archivo": o.get("source")}, responsable=o.get("who"), dias=(hoy - d).days, clave=f"obl:{code}:{o['id']}"))

    # Firmas y facultades.
    matriz = []
    mf = buscar(docs / "00-referencia", "matriz-atribuciones")
    if mf:
        t = Tabla(mf[0], ["nombre", "monto_maximo"], ["cargo", "tipo", "desde", "hasta"], cols.get("authority"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            matriz = [dict(f, cita=t.cita(f, docs)) for f in t.filas]
    firmas = []

    def facultad(nombre, tipo, monto, el_dia):
        for f in matriz:
            if norm(f["nombre"]) != norm(nombre):
                continue
            if norm(f.get("tipo")) not in ("", "todos", "todas", norm(tipo)):
                continue
            desde, hasta = fecha(f.get("desde")), fecha(f.get("hasta"))
            if el_dia and ((desde and el_dia < desde) or (hasta and el_dia > hasta)):
                continue
            if (numero(f["monto_maximo"]) or 0) + 0.005 >= monto:
                return f
        return None
    for code, c in sorted(fichas.items()):
        cita = {"archivo": c.get("source")}
        inicio, firmado = fecha(c.get("start")), fecha(c.get("signed_on")) or fecha(c.get("start"))
        propios = [s for s in c.get("signatories") or [] if norm(s.get("party")) in ("entidad", "entity", "la_entidad")]
        valor = numero(c.get("value")) or 0.0
        ok_ = next((s for s in propios if facultad(s.get("name"), c.get("type"), valor, firmado)), None) if matriz else True
        firmas.append({"codigo": code, "firmantes": ", ".join(s.get("name") or "?" for s in propios) or "—", "monto": redondo(valor),
                       "con_facultad": bool(ok_), "firmado_por_las_dos": c.get("signed_by_both")})
        if matriz and propios and not ok_:
            al.append(alerta("signed_without_authority", f"{code}: {', '.join(s.get('name') for s in propios)} firmó por {mon(valor)} y la matriz de atribuciones no le da facultad para ese tipo y monto",
                             [cita] + ([matriz[0]["cita"]] if matriz else []), valor, clave=f"firma:{code}"))
        acumulado = valor
        for o in sorted(c.get("amendments") or [], key=lambda x: x.get("date") or ""):
            acumulado += numero(o.get("added_value")) or 0.0
            if matriz and o.get("signed_by") and numero(o.get("added_value")) and not facultad(o["signed_by"], c.get("type"), acumulado, fecha(o.get("date"))):
                al.append(alerta("signed_without_authority", f"{code} · {o.get('id')}: {o['signed_by']} firmó el otrosí que lleva el contrato a {mon(acumulado)} sin facultad para ese monto",
                                 {"archivo": o.get("source")}, numero(o.get("added_value")), clave=f"firma:{code}:{o.get('id')}"))
            if o.get("signed") is False and fecha(o.get("date")) and fecha(o["date"]) <= hoy:
                al.append(alerta("unsigned_contract", f"{code} · {o.get('id')}: el otrosí no tiene la firma de las dos partes",
                                 {"archivo": o.get("source")}, clave=f"sinfirma:{code}:{o.get('id')}"))
        if c.get("signed_by_both") is False and inicio and inicio <= hoy:
            al.append(alerta("unsigned_contract", f"{code}: el documento no tiene la firma de las dos partes y el contrato empezó el {iso(inicio)}",
                             cita, valor, clave=f"sinfirma:{code}"))
        cert = c.get("counterparty_certificate") or {}
        ce = fecha(cert.get("issued_on"))
        if ce and firmado and (firmado - ce).days > umbral(cfg, "certificate_max_days"):
            al.append(alerta("counterparty_certificate_stale", f"{code}: el certificado de la contraparte tenía {(firmado - ce).days} días cuando se firmó",
                             {"archivo": cert.get("source")}, dias=(firmado - ce).days, clave=f"cert:{code}"))

    # Lo pagado y las garantías.
    pagos: dict[str, list] = {}
    for pf in buscar(docs / "10-registro", "pagos"):
        t = Tabla(pf, ["contrato", "fecha", "valor"], ["documento"], cols.get("payments"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
            continue
        for f in t.filas:
            pagos.setdefault(str(f["contrato"]).strip().upper(), []).append({"fecha": fecha(f["fecha"]), "valor": numero(f["valor"]) or 0.0, "cita": t.cita(f, docs)})
    ejecucion = []
    for code, c in sorted(fichas.items()):
        ps = pagos.get(code, [])
        total, pagado = valor_total(c), sum(p["valor"] for p in ps)
        fe = fin_efectivo(c, hoy, cfg)
        ejecucion.append({"codigo": code, "valor": redondo(total), "pagado": redondo(pagado), "saldo": redondo(total - pagado),
                          "ultimo_pago": iso(max((p["fecha"] for p in ps if p["fecha"]), default=None))})
        if pagado > total + tol:
            al.append(alerta("payments_over_value", f"{code}: pagado {mon(pagado)} contra un valor de {mon(total)} con sus otrosíes",
                             [p["cita"] for p in ps][-2:] + [{"archivo": c.get("source")}], pagado - total, clave=f"pagos:{code}"))
        tarde = [p for p in ps if p["fecha"] and fe and p["fecha"] > fe]
        if tarde:
            al.append(alerta("payment_after_termination", f"{code}: {len(tarde)} pago(s) después de la terminación del {iso(fe)}, por {mon(sum(p['valor'] for p in tarde))}",
                             [p["cita"] for p in tarde][:3], sum(p["valor"] for p in tarde), clave=f"pagofuera:{code}"))
        aportadas = {norm(g.get("type")): g for g in c.get("guarantees_provided") or []}
        for g in c.get("guarantees_required") or []:
            tipo = norm(g.get("type"))
            exigida = fecha(g.get("until")) or (sumar_meses(fin_documentado(c), int(g["months_after_end"])) if fin_documentado(c) and g.get("months_after_end") is not None else None)
            ap = aportadas.get(tipo)
            if not ap:
                al.append(alerta("guarantee_missing", f"{code}: exige la garantía de {g.get('type')} y no hay póliza aportada en 20-garantias/",
                                 {"archivo": g.get("source") or c.get("source")}, clave=f"garantia:{code}:{tipo}"))
            elif exigida and fecha(ap.get("until")) and fecha(ap["until"]) < exigida:
                al.append(alerta("guarantee_expires_early", f"{code}: la póliza de {g.get('type')} vence el {ap['until']} y el contrato la exige hasta el {iso(exigida)}",
                                 {"archivo": ap.get("source")}, dias=(exigida - fecha(ap["until"])).days, clave=f"garantia:{code}:{tipo}"))
    partes = {
        "contract-register": {"contratos": filas_registro},
        "obligations-calendar": {"calendario": sorted((x for x in calendario if x["fecha"]), key=lambda x: x["fecha"])},
        "authority-check": {"firmas": firmas},
        "contract-execution": {"contratos": ejecucion},
    }
    # Lo que vence, para Rostrum (ADR 0010): del calendario, entre 30 días atrás y 90 adelante, sin
    # las obligaciones que ya tienen su evidencia ni los preavisos que alguien ya decidió.
    vence = [{"fecha": x["fecha"], "que": x["que"], "caso": x["codigo"], "comando": "obligations-calendar",
              "estado": "con evidencia" if x.get("evidencia") else ("decidido" if (fichas.get(x["codigo"]) or {}).get("decision") else "pendiente")}
             for x in calendario if x["fecha"] and x["dias"] is not None and -30 <= x["dias"] <= 90]
    vence = sorted((v for v in vence if v["estado"] == "pendiente"), key=lambda v: (v["fecha"], v["caso"], v["que"]))
    return {"agente": "fidel", "entidad": cfg.get("entity"), "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": [], "vence": vence}


# ================================================================ Constanza · el cumplimiento

def _limite_obligacion(v: str, periodo: str, feriados: set) -> dt.date | None:
    s = norm(v)
    m = re.fullmatch(r"d_?(\d+)", s)
    if m:
        return dia_habil(fin_de_mes(periodo), int(m[1]), feriados)
    m = re.fullmatch(r"dia_?(\d+)", s)
    if m:
        sig = fin_de_mes(periodo) + dt.timedelta(days=1)
        import calendar
        return dt.date(sig.year, sig.month, min(int(m[1]), calendar.monthrange(sig.year, sig.month)[1]))
    return fecha(v)


def _periodos_hasta(periodo: str, meses: int) -> list[str]:
    a, m = (int(x) for x in periodo.split("-"))
    out = []
    for k in range(meses):
        mm = m - k
        aa = a + (mm - 1) // 12
        mm = (mm - 1) % 12 + 1
        out.append(f"{aa:04d}-{mm:02d}")
    return out


def constanza(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _PAIS[0] = N.pais_de(cfg)
    docs, estado = cfg["_docs"], cfg["_estado"]
    ficha = leer_json(estado / "cumplimiento" / periodo / "ficha.json", {}) or {}
    problemas = revisar_ficha_cumplimiento(ficha)
    cols = cfg.get("columns") or {}
    feriados = set(cfg.get("holidays") or [])
    al: list[dict] = []
    no_proc: list[dict] = []
    obligaciones = []
    matriz_fuentes = []
    mf = buscar(docs / "00-referencia", "matriz-obligaciones")
    if not mf:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está la matriz de obligaciones"})
    else:
        t = Tabla(mf[0], ["id", "obligacion", "periodicidad", "dia_limite"], ["fuente", "tipo", "responsable", "evidencia_esperada", "criticidad", "estado"],
                  cols.get("obligations"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            periodos = sorted({p.name[len("cumplimiento-"):] for p in docs.iterdir() if p.is_dir() and re.fullmatch(r"cumplimiento-\d{4}-\d{2}", p.name)})
            for f in t.filas:
                oid = str(f["id"]).strip()
                per = norm(f["periodicidad"])
                ventana = VENTANA.get(per)
                lim = _limite_obligacion(f["dia_limite"], periodo, feriados)
                en = [p for p in periodos if p <= periodo]
                con_ev = {p: _evidencia(docs / f"cumplimiento-{p}" / "10-evidencias", oid, docs) for p in en}
                dentro = _periodos_hasta(periodo, ventana) if ventana else en
                ev = [e for p in dentro for e in con_ev.get(p, [])]
                previas = [p for p in en if con_ev.get(p) and p not in dentro]
                declarada = norm(f.get("estado")) in ("cumplida", "cumplido", "hecho", "hecha", "ok", "presentado", "presentada")
                o = {"id": oid, "obligacion": f["obligacion"], "fuente": f.get("fuente"), "responsable": f.get("responsable"),
                     "periodicidad": per, "limite": iso(lim), "criticidad": norm(f.get("criticidad")) or "media", "evidencia": ev,
                     "cita": t.cita(f, docs)}
                if ev:
                    o["estado"] = "cumplida con evidencia"
                elif declarada:
                    o["estado"] = "cumplida sin evidencia"
                elif lim and lim < hoy:
                    o["estado"] = "vencida"
                else:
                    o["estado"] = "en plazo"
                obligaciones.append(o)
                matriz_fuentes.append(str(f.get("fuente") or ""))
                sev = CRITICIDAD.get(o["criticidad"], 2)
                if o["estado"] == "vencida":
                    al.append(alerta("compliance_obligation_overdue", f"{oid} · {f['obligacion']}: venció el {iso(lim)} y no hay evidencia en la ventana de su periodicidad",
                                     o["cita"], responsable=f.get("responsable"), dias=(hoy - lim).days, severidad=sev, clave=f"oblig:{oid}"))
                if o["estado"] == "cumplida sin evidencia":
                    al.append(alerta("compliance_done_without_evidence", f"{oid} · {f['obligacion']}: figura cumplida y no hay evidencia que empiece por {oid}",
                                     o["cita"], responsable=f.get("responsable"), clave=f"oblig:{oid}"))
                if o["estado"] == "en plazo" and ventana and previas:
                    ultima = max(previas)
                    anterior = _periodos_hasta(periodo, 2 * ventana)[ventana:]
                    if ultima not in anterior:
                        al.append(alerta("compliance_evidence_stale", f"{oid} · {f['obligacion']}: la última evidencia es de {ultima}; el ciclo anterior no tiene",
                                         o["cita"], responsable=f.get("responsable"), clave=f"stale:{oid}"))
                elif o["estado"] == "en plazo" and ventana and not previas and en and len(en) > ventana:
                    al.append(alerta("compliance_evidence_stale", f"{oid} · {f['obligacion']}: no hay evidencia en ningún periodo anterior",
                                     o["cita"], responsable=f.get("responsable"), clave=f"stale:{oid}"))
                if not str(f.get("responsable") or "").strip():
                    al.append(alerta("obligation_without_owner", f"{oid} · {f['obligacion']}: no tiene responsable", o["cita"], clave=f"duenio:{oid}"))
                if not str(f.get("fuente") or "").strip():
                    al.append(alerta("obligation_without_source", f"{oid} · {f['obligacion']}: no cita la norma, el contrato o la política de la que sale", o["cita"], clave=f"fuente:{oid}"))
    texto_matriz = norm(" ".join(matriz_fuentes))

    # Las obligaciones de cumplimiento de los contratos (fichas de Fidel).
    # Si la configuración no dice dónde están, son las del estado que Constanza comparte con Fidel
    # (ADR 0010): las fichas de los contratos de la misma entidad.
    rutas = (cfg.get("compliance") or {}).get("contract_records")
    if not rutas and cfg.get("_estado") and (Path(cfg["_estado"]) / "contratos").is_dir():
        rutas = str(Path(cfg["_estado"]) / "contratos")
    contratos = []
    if rutas:
        rp = Path(rutas).expanduser()
        rp = rp if rp.is_absolute() else Path(cfg.get("_raiz") or Path.cwd()) / rp
        for code, c in sorted(fichas_contratos(rp.parent if rp.name == "contratos" else rp).items()):
            for o in c.get("obligations") or []:
                if norm(o.get("kind")) != "cumplimiento":
                    continue
                esta = norm(code) in texto_matriz and norm(o.get("id")) in texto_matriz
                contratos.append({"contrato": code, "obligacion": o.get("id"), "que": o.get("what"), "en_matriz": esta})
                if not esta:
                    al.append(alerta("contract_obligation_not_in_matrix", f"{code} · {o.get('id')} · {o.get('what')}: obligación de cumplimiento del contrato que la matriz no tiene",
                                     {"archivo": o.get("source")}, clave=f"ctrobl:{code}:{o.get('id')}"))

    # Las políticas.
    politicas = []
    pf = buscar(docs / "20-politicas", "indice-politicas")
    if pf:
        t = Tabla(pf[0], ["codigo", "politica", "proxima_revision"], ["version", "responsable", "aprobada"], cols.get("policies"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            for f in t.filas:
                rv = fecha(f["proxima_revision"])
                politicas.append({"codigo": f["codigo"], "politica": f["politica"], "version": f.get("version"), "responsable": f.get("responsable"),
                                  "proxima_revision": iso(rv), "dias": (rv - hoy).days if rv else None})
                if rv and rv < hoy:
                    al.append(alerta("policy_review_overdue", f"{f['codigo']} · {f['politica']}: su revisión vencía el {iso(rv)}",
                                     t.cita(f, docs), responsable=f.get("responsable"), dias=(hoy - rv).days, clave=f"politica:{f['codigo']}"))

    # Las normas.
    normas = []
    nf = buscar(docs / "30-normativa", "registro-normativo")
    filas_n = []
    if nf:
        t = Tabla(nf[0], ["id", "norma", "registrada"], ["publicada", "aplica", "evaluacion", "responsable"], cols.get("regulatory"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            filas_n = [dict(f, cita=t.cita(f, docs)) for f in t.filas]
    vistos = {str(f["id"]).strip() for f in filas_n}
    for x in ficha.get("new_rules") or []:
        if str(x.get("id")) not in vistos:
            filas_n.append({"id": x.get("id"), "norma": x.get("rule"), "registrada": x.get("date"), "aplica": x.get("applies"),
                            "evaluacion": None, "responsable": None, "cita": {"archivo": x.get("source")}})
    for f in filas_n:
        reg = fecha(f.get("registrada"))
        nid = str(f["id"]).strip()
        normas.append({"id": nid, "norma": f["norma"], "registrada": iso(reg), "aplica": f.get("aplica"), "evaluada": bool(str(f.get("evaluacion") or "").strip())})
        if not str(f.get("evaluacion") or "").strip() and reg and (hoy - reg).days > umbral(cfg, "norm_assessment_days"):
            al.append(alerta("regulatory_change_unassessed", f"{nid} · {f['norma']}: registrada el {iso(reg)}, lleva {(hoy - reg).days} días sin evaluación de impacto",
                             f["cita"], responsable=f.get("responsable"), dias=(hoy - reg).days, clave=f"norma:{nid}"))
        if norm(f.get("aplica")) in SI and norm(nid) not in texto_matriz:
            al.append(alerta("applicable_norm_not_in_matrix", f"{nid} · {f['norma']}: aplica y ninguna obligación de la matriz la cita",
                             f["cita"], clave=f"aplica:{nid}"))

    # El canal de denuncias: plazos, sin datos de quién denunció.
    casos = []
    cf = buscar(docs / "40-canal", "casos")
    if cf:
        t = Tabla(cf[0], ["id", "recibido"], ["respondido", "tipo", "estado"], cols.get("cases"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            plazo = umbral(cfg, "case_response_days")
            for f in t.filas:
                rec, res = fecha(f["recibido"]), fecha(f.get("respondido"))
                dias = ((res or hoy) - rec).days if rec else None
                casos.append({"id": f["id"], "tipo": f.get("tipo"), "recibido": iso(rec), "respondido": iso(res), "dias": dias})
                if rec and not res and dias > plazo:
                    al.append(alerta("report_case_overdue", f"caso {f['id']}: recibido el {iso(rec)}, lleva {dias} días sin respuesta y el plazo es de {plazo}",
                                     t.cita(f, docs), dias=dias, clave=f"caso:{f['id']}"))
    dec = ficha.get("declared") or {}
    if norm(dec.get("status")) in ("cumplido", "cumplida", "en_cumplimiento", "compliant", "sin_novedades") and al:
        al.append(alerta("declared_compliance_vs_evidence", f"el informe declara el periodo {dec.get('status')} ({dec.get('source')}) y hay {len(al)} señales abiertas que ese estado no explica",
                         {"archivo": dec.get("source")}, clave="cumplimiento"))
    peso = {"alta": 3, "media": 2, "baja": 1}
    total = sum(peso.get(o["criticidad"], 2) for o in obligaciones)
    hecho = sum(peso.get(o["criticidad"], 2) for o in obligaciones if o["evidencia"])
    orden = {"vencida": 0, "cumplida sin evidencia": 1, "en plazo": 2, "cumplida con evidencia": 3}
    partes = {
        "compliance-status": {"obligaciones": sorted(obligaciones, key=lambda o: (CRITICIDAD.get(o["criticidad"], 2), orden[o["estado"]], o["limite"] or "9999", o["id"])),
                              "avance_con_evidencia_pct": redondo(100 * hecho / total) if total else None, "declarado": dec or None, "contratos": contratos},
        "policy-review": {"politicas": sorted(politicas, key=lambda x: x["proxima_revision"] or "9999")},
        "regulatory-watch": {"normas": normas},
        "reports-cases": {"casos": casos, "plazo": umbral(cfg, "case_response_days")},
    }
    plazo_casos = umbral(cfg, "case_response_days")
    vence = ([{"fecha": o["limite"], "que": f"{o['id']} · {o['obligacion']}", "caso": periodo, "estado": o["estado"],
               "responsable": o.get("responsable"), "comando": "compliance-status"}
              for o in obligaciones if o["limite"] and o["estado"] in ("vencida", "en plazo")]
             + [{"fecha": x["proxima_revision"], "que": f"{x['codigo']} · revisión de {x['politica']}", "caso": periodo,
                 "estado": "vencida" if x["dias"] is not None and x["dias"] < 0 else "en plazo", "responsable": x.get("responsable"),
                 "comando": "policy-review"} for x in politicas if x["proxima_revision"] and x["dias"] is not None and x["dias"] <= 90]
             + [{"fecha": iso(fecha(x["recibido"]) + dt.timedelta(days=plazo_casos)), "que": f"caso {x['id']} · plazo de respuesta",
                 "caso": periodo, "estado": "vencida" if x["dias"] is not None and x["dias"] > plazo_casos else "en plazo",
                 "responsable": None, "comando": "reports-cases"} for x in casos if x["recibido"] and not x["respondido"]])
    return {"agente": "constanza", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(fin_de_mes(periodo)), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [],
            "vence": sorted(vence, key=lambda v: (v["fecha"], v["que"]))}


def revisar_ficha_cumplimiento(f: dict) -> list[str]:
    p = []
    d = f.get("declared")
    if d is not None and (not isinstance(d, dict) or not d.get("status") or not d.get("source")):
        p.append("declared: lleva status, source y date, o no va")
    for i, x in enumerate(f.get("new_rules") or []):
        if not x.get("id") or not x.get("source"):
            p.append(f"new_rules[{i}]: cada norma lleva id, rule, date y source")
    for i, q in enumerate(f.get("questions") or []):
        if not q.get("question") or "answer" not in q:
            p.append(f"questions[{i}]: lleva question y answer")
    return p


# ================================================================ el reporte

NOMBRE = {"fidel": "Fidel", "constanza": "Constanza"}
SENALES_DE = {
    "contract-register": {"register_mismatch", "register_differs_from_contract", "contract_expired_active"},
    "obligations-calendar": {"contract_expiring", "notice_deadline_near", "renewal_notice_missed", "contract_obligation_overdue"},
    "authority-check": {"signed_without_authority", "unsigned_contract", "counterparty_certificate_stale"},
    "contract-execution": {"payments_over_value", "payment_after_termination", "guarantee_missing", "guarantee_expires_early"},
    "compliance-status": {"compliance_obligation_overdue", "compliance_done_without_evidence", "compliance_evidence_stale",
                          "obligation_without_owner", "obligation_without_source", "declared_compliance_vs_evidence",
                          "contract_obligation_not_in_matrix"},
    "policy-review": {"policy_review_overdue"},
    "regulatory-watch": {"regulatory_change_unassessed", "applicable_norm_not_in_matrix"},
    "reports-cases": {"report_case_overdue"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    alcance = f"periodo {r['periodo']}" if r.get("periodo") else f"al {r.get('hoy')}"
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=alcance, cuerpo=_cuerpo, familia="criterio-clo")


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "contract-register":
        l += ["| Contrato | Contraparte | Estado en el registro | Estado según sus fechas | Diferencias |", "|---|---|---|---|---|"]
        l += [f"| {c['codigo']} | {c.get('contraparte') or '—'} | {c.get('estado_declarado') or '—'} | {c.get('estado_fechas') or '—'} | {'; '.join(c['diferencias']) or '—'} |" for c in p["contratos"]]
        l.append("")
    elif comando == "obligations-calendar":
        prox = [x for x in p["calendario"] if x["dias"] is not None and -30 <= x["dias"] <= 90]
        l += ["| Fecha | Contrato | Qué | Días | Evidencia |", "|---|---|---|---|---|"]
        l += [f"| {x['fecha']} | {x['codigo']} | {x['que']} | {x['dias']} | {', '.join('`' + e + '`' for e in x.get('evidencia') or []) or '—'} |" for x in prox]
        l += ["", "Entre 30 días atrás y 90 adelante. La decisión de renovar o terminar es de una persona.", ""]
    elif comando == "authority-check":
        l += ["| Contrato | Firmó por la entidad | Monto | Con facultad | Firma de las dos partes |", "|---|---|---|---|---|"]
        l += [f"| {f['codigo']} | {f['firmantes']} | {_m(f['monto'])} | {'sí' if f['con_facultad'] else 'no'} | {'sí' if f['firmado_por_las_dos'] else 'no'} |" for f in p["firmas"]]
        l += ["", "Sin opinión sobre la validez del contrato ni de la firma: se compara con la matriz de atribuciones de la organización.", ""]
    elif comando == "contract-execution":
        l += ["| Contrato | Valor con otrosíes | Pagado | Saldo | Último pago |", "|---|---|---|---|---|"]
        l += [f"| {c['codigo']} | {_m(c['valor'])} | {_m(c['pagado'])} | {_m(c['saldo'])} | {c['ultimo_pago'] or '—'} |" for c in p["contratos"]]
        l.append("")
    elif comando == "compliance-status":
        dec = p.get("declarado") or {}
        l += [f"**Estado declarado:** {dec.get('status') or 'nadie lo ha declarado'}" + (f" (`{dec.get('source')}`)" if dec.get("source") else "") +
              f" · **Avance con evidencia:** {_m(p.get('avance_con_evidencia_pct'))} % (ponderado por criticidad)", "",
              "| Id | Obligación | Fuente | Responsable | Vence | Estado | Evidencia |", "|---|---|---|---|---|---|---|"]
        l += [f"| {o['id']} | {o['obligacion']} | {o.get('fuente') or '—'} | {o.get('responsable') or '—'} | {o['limite'] or '—'} | {o['estado']} | {', '.join('`' + e + '`' for e in o['evidencia']) or '—'} |" for o in p["obligaciones"]]
        l.append("")
    elif comando == "policy-review":
        l += ["| Código | Política | Versión | Responsable | Próxima revisión | Días |", "|---|---|---|---|---|---|"]
        l += [f"| {x['codigo']} | {x['politica']} | {x.get('version') or '—'} | {x.get('responsable') or '—'} | {x['proxima_revision'] or '—'} | {x['dias'] if x['dias'] is not None else '—'} |" for x in p["politicas"]]
        l.append("")
    elif comando == "regulatory-watch":
        l += ["| Id | Norma | Registrada | Aplica | Evaluada |", "|---|---|---|---|---|"]
        l += [f"| {x['id']} | {x['norma']} | {x['registrada'] or '—'} | {x.get('aplica') or 'por evaluar'} | {'sí' if x['evaluada'] else 'no'} |" for x in p["normas"]]
        l += ["", "Sin opinión sobre el alcance de ninguna norma: si aplica y qué exige lo decide la organización.", ""]
    elif comando == "reports-cases":
        l += ["| Caso | Tipo | Recibido | Respondido | Días |", "|---|---|---|---|---|"]
        l += [f"| {x['id']} | {x.get('tipo') or '—'} | {x['recibido'] or '—'} | {x['respondido'] or 'abierto'} | {x['dias'] if x['dias'] is not None else '—'} |" for x in p["casos"]]
        l += ["", f"Plazo de respuesta configurado: {p['plazo']} días. Sin datos de quién denunció.", ""]
    return l


# ================================================================ cuándo toca qué

def despertar(cfg: dict, rol: str, hoy: dt.date) -> dict:
    corr = registro_corridas(cfg["_estado"])
    ultima = lambda que: max((fecha(c["fecha"]) for c in corr if c["comando"] == que), default=None)  # noqa: E731
    toca, motivo = [], []
    if rol == "fidel":
        r = fidel(cfg, hoy)
        urgentes = [a for a in r["alertas"] if a["signal"] in ("notice_deadline_near", "renewal_notice_missed", "contract_expiring", "contract_obligation_overdue")]
        if urgentes and ultima("obligations-calendar") != hoy:
            toca.append("obligations-calendar")
            motivo.append(f"{len(urgentes)} vencimientos, preavisos u obligaciones en la ventana")
        u = ultima("contract-scan")
        if not u or (hoy - u).days >= 7:
            toca.insert(0, "contract-scan")
            motivo.append("una vez por semana se procesan los contratos")
    else:
        periodo = cfg.get("period")
        r = constanza(cfg, periodo, hoy) if periodo else {"partes": {}}
        cerca = [o for o in (r["partes"].get("compliance-status") or {}).get("obligaciones", []) if o["estado"] in ("en plazo", "vencida") and o["limite"] and (fecha(o["limite"]) - hoy).days <= 7]
        if cerca and ultima("compliance-status") != hoy:
            toca.append("compliance-status")
            motivo.append(f"{len(cerca)} obligaciones vencen en los próximos siete días o ya vencieron")
        u = ultima("compliance-scan")
        if not u or (hoy - u).days >= 7:
            toca.insert(0, "compliance-scan")
            motivo.append("una vez por semana se procesa la carpeta")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


# ================================================================ la línea de comandos

def _rol() -> str:
    return "constanza" if N.plugin(AQUI)["name"] == "criterio-compliance" else "fidel"


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    if rol == "fidel":
        r = fidel(cfg, hoy)
        destino = cfg["_estado"] / "contratos" / "resultados.json"
    else:
        periodo = a.period or cfg.get("period")
        if not periodo:
            raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
        r = constanza(cfg, periodo, hoy)
        destino = cfg["_estado"] / "cumplimiento" / periodo / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Fidel y Constanza.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir",
                                       "compute", "reporte", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=("contratos", "cumplimiento"),
                       revisar_config=revisar_config, calcular=calcular, reporte=reporte, despertar=despertar)


# ================================================================ la prueba del motor

def selftest() -> int:
    fallas = []

    def ok(nombre, obtenido, esperado):
        if obtenido == esperado:
            print(f"  ok  {nombre}")
        else:
            fallas.append(nombre)
            print(f"  FALLA  {nombre}: {obtenido!r} en lugar de {esperado!r}")

    hoy = dt.date(2026, 10, 6)
    ok("un país fuera del registro se rechaza", bool(N.revisar_pais({"country": "XX"})), True)
    ok("los países del registro pasan", [c for c in N.PAISES if N.revisar_pais({"country": c})], [])
    ok("sumar meses al fin de mes", sumar_meses(dt.date(2026, 1, 31), 1), dt.date(2026, 2, 28))
    ok("día 15 del mes siguiente", _limite_obligacion("día 15", "2026-09", set()), dt.date(2026, 10, 15))
    ok("D+5 en días hábiles", _limite_obligacion("D+5", "2026-09", set()), dt.date(2026, 10, 7))
    ok("periodos de una ventana trimestral", _periodos_hasta("2026-02", 3), ["2026-02", "2026-01", "2025-12"])
    c = {"code": "CTR-1", "end": "2026-10-31", "auto_renewal": True, "amendments": [{"new_end": "2026-12-31", "signed": True}]}
    ok("la terminación la cambia el otrosí firmado", fin_documentado(c), dt.date(2026, 12, 31))
    ok("con renovación automática se prorroga", fin_efectivo(dict(c, end="2026-01-31", amendments=[]), hoy, {}), dt.date(2027, 1, 31))
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "legal" / "e1", t / "estado" / "e1"
        _csv(docs / "00-referencia" / "matriz-atribuciones.csv", [["nombre", "cargo", "tipo", "monto_maximo"], ["Ana Gil", "Gerente", "todos", "100000"]])
        _csv(docs / "10-registro" / "registro-contratos.csv", [["codigo", "contraparte", "valor", "inicio", "terminacion", "estado"],
                                                               ["CTR-1", "Proveedor", "150000", "2026-01-01", "2026-10-20", "vigente"]])
        _csv(docs / "10-registro" / "pagos-2026-09.csv", [["contrato", "fecha", "valor"], ["CTR-1", "2026-09-10", "160000"]])
        (docs / "contratos" / "CTR-1-proveedor" / "10-contrato").mkdir(parents=True)
        (docs / "contratos" / "CTR-1-proveedor" / "10-contrato" / "contrato.md").write_text("contrato", encoding="utf-8")
        escribir_json(est / "contratos" / "CTR-1.json", {"code": "CTR-1", "value": 150000, "start": "2026-01-01", "end": "2026-10-20", "signed_on": "2025-12-20",
                                                         "signed_by_both": True, "source": "contratos/CTR-1-proveedor/10-contrato/contrato.md",
                                                         "signatories": [{"name": "Ana Gil", "party": "entidad"}],
                                                         "guarantees_required": [{"type": "cumplimiento", "months_after_end": 4}]})
        cfg = {"entity": {"id": "1", "name": "Prueba", "country": "CO"}, "_docs": docs, "_estado": est}
        r = fidel(cfg, hoy)
        ok("las señales de un contrato con todo mal, y ninguna otra",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("contract_expiring", "vence:CTR-1"), ("guarantee_missing", "garantia:CTR-1:cumplimiento"),
            ("payments_over_value", "pagos:CTR-1"), ("signed_without_authority", "firma:CTR-1")])
        ok("la ficha está completa", r["record_issues"], [])
        md = reporte(r, "contract-execution", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        _csv(docs / "00-referencia" / "matriz-obligaciones.csv", [["id", "obligacion", "fuente", "responsable", "periodicidad", "dia_limite", "criticidad", "estado"],
                                                                  ["OB-1", "Reporte mensual", "Política P-1", "Luis", "mensual", "día 5", "alta", ""],
                                                                  ["OB-2", "Reporte trimestral", "", "", "trimestral", "día 20", "media", "cumplida"]])
        (docs / "cumplimiento-2026-09" / "10-evidencias").mkdir(parents=True)
        cfg["period"] = "2026-09"
        r = constanza(cfg, "2026-09", hoy)
        ok("cumplimiento: vencida, cumplida sin evidencia, sin responsable y sin fuente",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("compliance_done_without_evidence", "oblig:OB-2"), ("compliance_obligation_overdue", "oblig:OB-1"),
            ("obligation_without_owner", "duenio:OB-2"), ("obligation_without_source", "fuente:OB-2")])
        # El contrato de estado común (ADR 0010): la corrida en el formato que sirve Rostrum, y las peticiones.
        ok("lo que vence lo calcula el motor, sin lo que ya tiene evidencia",
           [v["que"] for v in r["vence"]][:1], ["OB-1 · Reporte mensual"])
        (t / "salida.md").write_text("lo que se mostró", encoding="utf-8")
        reg = N.corrida(est, "compliance-status", t / "salida.md", "2026-09", None, hoy, r, "0.0.0")
        c = leer_json(est / "corridas.json", [])[-1]
        ok("la corrida queda en el formato común, con sus hallazgos por caso",
           (reg["id"], c["que"], c["hallazgos"], sorted(c["por_caso"]), c["salida"]),
           ("2026-10-06-compliance-status-1", "compliance-status", 4, ["2026-09"], True))
        ok("y el registro la lee para saber qué toca", N.registro_corridas(est)[-1]["comando"], "compliance-status")
        escribir_json(est / "peticiones" / "p1.json", {"id": "p1", "texto": "¿por qué vence OB-1?", "respondida": None})
        ok("la petición abierta se ve", [p["id"] for p in N.peticiones_abiertas(est)], ["p1"])
        N.responder_peticion(est, "p1", hoy)
        ok("y respondida ya no", N.peticiones_abiertas(est), [])
    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
