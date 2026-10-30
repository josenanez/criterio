#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-sales/scripts/ventas.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
# -*- coding: utf-8 -*-
"""El motor de la familia CSO: lo que calcula el código para Augusto y para Valeria.

    python3 ventas.py <acción> [opciones]       python3 ventas.py --help

Augusto (criterio-sales) procesa el embudo y el pronóstico; Valeria (criterio-revenue), la venta
hasta la factura: el descuento contra su política, lo ganado contra lo firmado y lo facturado, y la
comisión contra el plan. Los dos comparten este motor, que vive en criterio-sales y se copia a
criterio-revenue con scripts/sincronizar.py, y el núcleo común de las familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —las exportaciones del
CRM, el historial de campos, las etapas, las metas, la matriz de descuentos, la tabla de cuentas, el
plan y la liquidación de comisiones— las procesa el código. Lo que solo trae un documento escrito
—cada documento de evidencia de una oportunidad, el pronóstico comprometido del acta del comité,
cada cotización con su descuento y su aprobación— lo extrae el agente a su ficha, con la cita, y el
código lo cruza.

**Las exportaciones, desde su fuente.** Salesforce por el nombre de cada campo o su etiqueta (F-02,
y su historial F-03), HubSpot por la etiqueta de cada propiedad (F-04, F-05), Dynamics 365 Sales
por la etiqueta o el nombre lógico de cada columna (F-06, F-07), Zoho CRM por la etiqueta de cada
campo (F-08, F-09), y cualquier otro CRM en CSV o Excel con el mapeo de columnas que deja el setup.
Cada campo que se procesa de uno de esos CRM está en `CAMPOS_SALESFORCE`,
`CAMPOS_SALESFORCE_HISTORIA`, `CAMPOS_HUBSPOT`, `CAMPOS_DYNAMICS` y `CAMPOS_ZOHO`, con el
identificador con que lo verifica su fuente en families/criterio-cso/fuentes.json; la puerta de las
familias falla si el motor usa uno que no está verificado.

**Lo que cruza familias va por las fichas** (ADR 0019): el contrato lo dice la ficha de Fidel y la
factura la de Clara. Este motor no procesa un contrato ni una factura electrónica.

**Sin calificar personas.** Nada aquí ordena ni compara a quienes venden: dice qué oportunidad no
tiene evidencia y qué comisión no es la del plan.

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
    ALIAS, Tabla, _PAIS, _csv, _hoy, _m, _xlsx, alerta, buscar, escribir_json, fecha, filas_de,
    fin_de_mes, ident, inicio_de_mes, iso, leer_json, marco_reporte, mon, norm, numero, ordenar,
    redondo, registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"

# ================================================================ las exportaciones del CRM

# Cada campo que el lector procesa, con el identificador con que lo verifica su fuente: la clave es
# el campo en families/criterio-cso/fuentes.json; el valor, el dato canónico y las cabeceras con
# que llega —el nombre del campo de la API o de Data Loader, y su etiqueta en un informe—, ya
# normalizadas (minúscula, sin tildes, con guion bajo).
CAMPOS_SALESFORCE = {
    "Id": ("id", ["id", "opportunity_id"]),
    "Name": ("nombre", ["name"]),
    "AccountId": ("cuenta", ["accountid", "account_id"]),
    "Amount": ("monto", ["amount"]),
    "CloseDate": ("cierre", ["closedate", "close_date"]),
    "StageName": ("etapa", ["stagename", "stage"]),
    "Probability": ("probabilidad", ["probability"]),
    "ForecastCategoryName": ("categoria", ["forecastcategoryname", "forecast_category"]),
    "IsClosed": ("cerrada", ["isclosed", "closed"]),
    "IsWon": ("ganada", ["iswon", "won"]),
    "LastActivityDate": ("ultima_actividad", ["lastactivitydate", "last_activity"]),
    "OwnerId": ("responsable", ["ownerid", "owner_id"]),
    "CreatedDate": ("creada", ["createddate", "created_date"]),
    "CurrencyIsoCode": ("moneda", ["currencyisocode", "opportunity_currency"]),
}
CAMPOS_SALESFORCE_HISTORIA = {
    "OpportunityId": ("id", ["opportunityid", "opportunity_id"]),
    "Field": ("campo", ["field"]),
    "OldValue": ("anterior", ["oldvalue", "old_value"]),
    "NewValue": ("nuevo", ["newvalue", "new_value"]),
}
# HubSpot no fija el nombre de la columna de la empresa asociada (F-05): la dice la configuración.
CAMPOS_HUBSPOT = {
    "Record ID": ("id", ["record_id"]),
    "Deal Name": ("nombre", ["deal_name"]),
    "Deal Stage": ("etapa", ["deal_stage"]),
    "Pipeline": ("pipeline", ["pipeline"]),
    "Amount": ("monto", ["amount"]),
    "Close Date": ("cierre", ["close_date"]),
    "Deal owner": ("responsable", ["deal_owner"]),
    "Create Date": ("creada", ["create_date"]),
    "Last Activity Date": ("ultima_actividad", ["last_activity_date"]),
    "Deal probability": ("probabilidad", ["deal_probability"]),
    "Forecast category": ("categoria", ["forecast_category"]),
    "Currency": ("moneda", ["currency"]),
}
# Dynamics 365 Sales: la exportación a Excel de una vista de oportunidades trae la etiqueta de cada
# columna de la tabla (F-06, F-07), o su nombre lógico si sale por la API. El estado —abierta, ganada
# o perdida— lo dice «Status» (statecode: Open, Won, Lost); la etapa del proceso de la entidad,
# «Pipeline Phase». La cuenta llega con el nombre del registro asociado.
CAMPOS_DYNAMICS = {
    "opportunityid": ("id", ["opportunityid", "opportunity"]),
    "name": ("nombre", ["name", "topic"]),
    "parentaccountid": ("cuenta", ["parentaccountid", "account", "customerid", "potential_customer"]),
    "estimatedvalue": ("monto", ["estimatedvalue", "est_revenue"]),
    "estimatedclosedate": ("cierre", ["estimatedclosedate", "est_close_date"]),
    "stepname": ("etapa", ["stepname", "pipeline_phase"]),
    "statecode": ("estado", ["statecode", "status"]),
    "closeprobability": ("probabilidad", ["closeprobability", "probability"]),
    "msdyn_forecastcategory": ("categoria", ["msdyn_forecastcategory", "forecast_category"]),
    "ownerid": ("responsable", ["ownerid", "owner"]),
    "transactioncurrencyid": ("moneda", ["transactioncurrencyid", "currency"]),
}
# Zoho CRM: la exportación del módulo de negocios trae la etiqueta de cada campo estándar (F-08) y,
# si no se quita, el id del registro (F-09). La última actividad no está entre los campos estándar
# de la fuente: si la exportación la trae, la dice el mapeo del setup.
CAMPOS_ZOHO = {
    "Record ID": ("id", ["record_id"]),
    "Deal Name": ("nombre", ["deal_name"]),
    "Account Name": ("cuenta", ["account_name"]),
    "Amount": ("monto", ["amount"]),
    "Closing Date": ("cierre", ["closing_date"]),
    "Stage": ("etapa", ["stage"]),
    "Probability": ("probabilidad", ["probability"]),
    "Deal Owner": ("responsable", ["deal_owner"]),
}
# El estado de Dynamics (statecode), como lo exporta: el valor de la opción o su etiqueta.
ESTADO_GANADA, ESTADO_PERDIDA = {"won", "1", "ganada", "ganado"}, {"lost", "2", "perdida", "perdido"}
# Cualquier otro CRM: las cabeceras en español más comunes; el resto lo dice el mapeo del setup.
CAMPOS_GENERICO = {
    "id": ["id", "id_oportunidad", "oportunidad_id", "codigo", "codigo_oportunidad"],
    "nombre": ["nombre", "oportunidad", "nombre_oportunidad", "negocio"],
    "cuenta": ["cuenta", "cliente", "id_cuenta", "empresa"],
    "etapa": ["etapa", "fase", "estado_oportunidad"],
    "monto": ["monto", "valor", "importe"],
    "cierre": ["cierre", "fecha_cierre", "fecha_de_cierre", "cierre_esperado"],
    "responsable": ["responsable", "propietario", "vendedor", "ejecutivo"],
    "ultima_actividad": ["ultima_actividad", "fecha_ultima_actividad"],
    "creada": ["creada", "fecha_creacion"],
    "linea": ["linea", "linea_negocio", "linea_de_negocio"],
    "probabilidad": ["probabilidad"],
}
REQUERIDOS = ("id", "etapa", "monto", "cierre")
VERDAD = ("true", "1", "si", "sí", "yes", "x", "verdadero")
FECHA_EN_NOMBRE = re.compile(r"(\d{4})[-_](\d{2})[-_](\d{2})")


def formato(cabecera: list[str]) -> str:
    """El CRM de una exportación, por sus columnas: HubSpot trae «Deal Stage» y «Record ID»;
    Dynamics, la fecha estimada de cierre («Est. close date» o `estimatedclosedate`); Zoho, «Deal
    Name» con «Closing Date»; Salesforce, «StageName» (API) o «Stage» con «Close Date» (un
    informe). Lo demás es genérico."""
    c = set(cabecera)
    if "deal_stage" in c and "record_id" in c:
        return "hubspot"
    if c & {"estimatedclosedate", "est_close_date"}:
        return "dynamics"
    if "closing_date" in c and "deal_name" in c:
        return "zoho"
    if "stagename" in c or ("stage" in c and "close_date" in c):
        return "salesforce"
    if {"field", "oldvalue"} <= c or {"field", "old_value"} <= c:
        return "historia"
    return "generico"


def _mapa(cab: list[str], fmt: str, columnas: dict | None) -> dict[str, int]:
    """El índice de cada dato canónico en la cabecera. El mapeo de la configuración manda sobre
    todo: dice, por ejemplo, qué columna trae la empresa asociada en HubSpot o la línea de negocio."""
    out: dict[str, int] = {}
    tabla = {"salesforce": CAMPOS_SALESFORCE, "hubspot": CAMPOS_HUBSPOT, "dynamics": CAMPOS_DYNAMICS, "zoho": CAMPOS_ZOHO,
             "historia": CAMPOS_SALESFORCE_HISTORIA}.get(fmt)
    variantes = {canon: cs for canon, cs in tabla.values()} if tabla else dict(CAMPOS_GENERICO)
    for canon, col in (columnas or {}).items():
        if norm(col) in cab:
            out[canon] = cab.index(norm(col))
    for canon, cs in variantes.items():
        if canon in out:
            continue
        for v in cs:
            if v in cab and cab.index(v) not in out.values():
                out[canon] = cab.index(v)
                break
    return out


def _cabecera(filas: list[list[str]]) -> int:
    """La primera fila que parece una cabecera: la que trae una etapa o un campo de historial."""
    for i, f in enumerate(filas[:15]):
        n = {norm(x) for x in f}
        if n & {"stagename", "stage", "deal_stage", "pipeline_phase", "stepname", "etapa", "fase", "field"} or n & set(CAMPOS_GENERICO["etapa"]):
            return i
    return 0


def orden_fechas(valores: list[str], preferencia: str = "dmy") -> str:
    """Un informe de Salesforce exporta las fechas en el formato de quien lo exporta: 10/20/2026 o
    20/10/2026. Si una fecha de la columna lo resuelve —un día mayor que 12— se usa ese; si no, el
    de la configuración (`crm.date_order`)."""
    for v in valores:
        m = re.match(r"^(\d{1,2})[/.-](\d{1,2})[/.-]\d{4}", str(v).strip())
        if m and int(m[1]) > 12:
            return "dmy"
        if m and int(m[2]) > 12:
            return "mdy"
    return preferencia


def fecha_crm(v, orden: str) -> dt.date | None:
    s = str(v or "").strip()
    m = re.match(r"^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})", s)
    if m and orden == "mdy":
        try:
            return dt.date(int(m[3]), int(m[1]), int(m[2]))
        except ValueError:
            return None
    return fecha(s)


def fecha_de_nombre(ruta: Path) -> dt.date | None:
    m = FECHA_EN_NOMBRE.search(ruta.name)
    if not m:
        return None
    try:
        return dt.date(int(m[1]), int(m[2]), int(m[3]))
    except ValueError:
        return None


def leer_exportacion(ruta: Path, cfg: dict) -> dict:
    """Una exportación de oportunidades o de historial, con su formato, su fecha y cada fila con su
    número para citarla. Ningún dato de contacto entra: solo las columnas que el motor procesa."""
    crm = cfg.get("crm") or {}
    filas = filas_de(ruta)
    if not filas:
        return {"ruta": ruta, "error": "la exportación está vacía"}
    i = _cabecera(filas)
    cab = [norm(x) for x in filas[i]]
    fmt = formato(cab)
    if crm.get("format") and fmt not in ("historia",) and crm["format"] != fmt and not (crm["format"] == "generico"):
        return {"ruta": ruta, "error": f"la configuración dice {crm['format']} y las columnas son de {fmt}"}
    mapa = _mapa(cab, fmt, crm.get("columns"))
    if fmt == "historia":
        faltan = [k for k in ("id", "campo", "anterior", "nuevo") if k not in mapa]
    else:
        faltan = [k for k in REQUERIDOS if k not in mapa]
    out = {"ruta": ruta, "formato": fmt, "fecha": fecha_de_nombre(ruta), "faltan": faltan, "filas": [], "columnas": sorted(mapa)}
    # Una columna que parece la última actividad y no está mapeada (Zoho no la tiene entre sus campos
    # estándar, F-08): sin ella, lo que no cambió de un corte a otro se da por detenido (CCO-4).
    if fmt != "historia" and "ultima_actividad" not in mapa:
        usadas = set(mapa.values())
        out["actividad_sin_mapear"] = [filas[i][j] for j, c in enumerate(cab)
                                       if j not in usadas and ("activ" in c or "gestion" in c)]
    if faltan:
        return out
    cuerpo = [f for f in filas[i + 1:] if any(str(x).strip() for x in f)]
    orden = orden_fechas([f[mapa[k]] for f in cuerpo for k in ("cierre", "ultima_actividad", "creada")
                          if k in mapa and mapa[k] < len(f)], crm.get("date_order", "dmy"))
    for k, f in enumerate(filas[i + 1:], start=i + 2):
        if not any(str(x).strip() for x in f):
            continue
        d = {"_fila": k}
        for canon, j in mapa.items():
            d[canon] = f[j].strip() if j < len(f) and isinstance(f[j], str) else (f[j] if j < len(f) else "")
        for canon in ("cierre", "ultima_actividad", "creada"):
            if canon in d:
                d[canon] = fecha_crm(d[canon], orden)
        out["filas"].append(d)
    return out


def exportaciones(cfg: dict) -> tuple[list[dict], list[dict], list[dict]]:
    """Las exportaciones de oportunidades de `10-crm/`, de la más vieja a la más nueva, el historial
    si llega, y lo que no se pudo procesar."""
    docs = cfg["_docs"]
    carpeta = docs / "10-crm"
    snaps, historia, no_proc = [], [], []
    for p in sorted(x for x in carpeta.iterdir() if x.is_file() and x.suffix.lower() in N.TABLAS and not x.name.startswith(".")) if carpeta.is_dir() else []:
        try:
            e = leer_exportacion(p, cfg)
        except (ValueError, KeyError) as ex:
            no_proc.append({"archivo": rel(p, docs), "motivo": str(ex)})
            continue
        if e.get("error"):
            no_proc.append({"archivo": rel(p, docs), "motivo": e["error"]})
        elif e["faltan"]:
            no_proc.append({"archivo": rel(p, docs), "motivo": f"faltan las columnas {', '.join(e['faltan'])}: el mapeo de la configuración (`crm.columns`) dice cuál es cada una"})
        elif e["formato"] == "historia":
            historia.append(e)
        elif not e["fecha"]:
            no_proc.append({"archivo": rel(p, docs), "motivo": "sin la fecha de la exportación en el nombre (AAAA-MM-DD): sin ella no se sabe qué cambió"})
        else:
            snaps.append(e)
    if not snaps and carpeta.is_dir():
        no_proc.append({"archivo": "10-crm/", "motivo": "no hay una exportación de oportunidades con su fecha"})
    elif not carpeta.is_dir():
        no_proc.append({"archivo": "10-crm/", "motivo": "no está la carpeta de las exportaciones del CRM"})
    return sorted(snaps, key=lambda e: e["fecha"]), historia, no_proc


# ================================================================ las tablas de referencia

ALIAS.update({
    "etapa": ["etapa", "stage", "fase"],
    "orden": ["orden", "order", "posicion"],
    "probabilidad": ["probabilidad", "probability"],
    "exige": ["exige", "documento", "documentos", "evidencia"],
    "tipo_etapa": ["tipo", "estado_etapa", "clase"],
    "periodo": ["periodo", "mes", "period"],
    "meta": ["meta", "objetivo", "cuota", "target"],
    "linea": ["linea", "linea_negocio", "linea_de_negocio"],
    "nivel": ["nivel", "level"],
    "tope": ["tope", "tope_pct", "descuento_maximo", "maximo"],
    "aprueba": ["aprueba", "aprobador", "cargo_aprueba"],
    "cuenta": ["cuenta", "id_cuenta", "account_id", "record_id", "cuenta_crm"],
    "nombre_cuenta": ["nombre", "nombre_cuenta", "razon_social"],
    "identificacion": ["identificacion", "nit", "rfc", "id_fiscal"],
    "tasa": ["tasa", "tasa_pct", "porcentaje", "comision_pct"],
    "liquidado": ["liquidado", "comision", "valor_liquidado", "monto"],
})
GANADA, PERDIDA, ABIERTA = "ganada", "perdida", "abierta"
TIPOS_DOC = {"propuesta": "propuesta", "orden_compra": "orden_compra", "orden_de_compra": "orden_compra",
             "acta_aceptacion": "acta_aceptacion", "acta_de_aceptacion": "acta_aceptacion"}
# Cómo se dice cada uno en un reporte: «la orden de compra», no «orden compra».
NOMBRE_DOC = {"propuesta": "la propuesta", "orden_compra": "la orden de compra", "acta_aceptacion": "el acta de aceptación"}


def pct(x) -> str:
    """Un porcentaje como se lee en el país de la entidad: 22 %, 12,5 %; nunca 22.0 %."""
    if x is None:
        return "—"
    t = f"{x:.1f}".rstrip("0").rstrip(".")
    return t.replace(".", ",") if N.PAISES.get(_PAIS[0], {}).get("decimal") == "," else t


def tipo_doc(v) -> str:
    n = norm(v)
    return TIPOS_DOC.get(n, n)


def etapas(cfg: dict, no_proc: list) -> dict[str, dict]:
    """La tabla de etapas: por cada etapa, su orden, su probabilidad, si es abierta, ganada o
    perdida, y los documentos que exige ella y todas las anteriores."""
    docs = cfg["_docs"]
    f = buscar(docs / "00-referencia", "etapas")
    if not f:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está la tabla de etapas"})
        return {}
    t = Tabla(f[0], ["etapa", "orden", "probabilidad"], ["exige", "tipo_etapa"], (cfg.get("columns") or {}).get("stages"))
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        return {}
    filas = sorted(t.filas, key=lambda x: numero(x["orden"]) or 0)
    out, acumulado = {}, []
    for x in filas:
        tipo = norm(x.get("tipo_etapa")) or ABIERTA
        tipo = GANADA if tipo in ("ganada", "ganado", "won", "closed_won") else PERDIDA if tipo in ("perdida", "perdido", "lost", "closed_lost") else ABIERTA
        propios = [tipo_doc(d) for d in re.split(r"[+,;/]", str(x.get("exige") or "")) if norm(d)]
        if tipo != PERDIDA:
            acumulado = acumulado + [d for d in propios if d not in acumulado]
        out[norm(x["etapa"])] = {"etapa": x["etapa"], "orden": numero(x["orden"]) or 0, "probabilidad": numero(x["probabilidad"]) or 0.0,
                                 "tipo": tipo, "exige": list(acumulado) if tipo != PERDIDA else [], "cita": t.cita(x, docs)}
    return out


def _cuentas(cfg: dict, no_proc: list) -> dict[str, str]:
    """La tabla de cuentas: el id o el nombre de cada cuenta del CRM, con la identificación del cliente."""
    docs = cfg["_docs"]
    f = buscar(docs / "00-referencia", "cuentas")
    if not f:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está la tabla de cuentas: sin ella no se cruza lo ganado con Fidel ni con Clara"})
        return {}
    t = Tabla(f[0], ["cuenta", "identificacion"], ["nombre_cuenta"], (cfg.get("columns") or {}).get("accounts"))
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        return {}
    out = {}
    for x in t.filas:
        out[norm(x["cuenta"])] = ident(x["identificacion"])
        if x.get("nombre_cuenta"):
            out.setdefault(norm(x["nombre_cuenta"]), ident(x["identificacion"]))
    return out


# ================================================================ las oportunidades

def oportunidad(f: dict, fmt: str, et: dict) -> dict:
    """Una fila de la exportación, con su estado —abierta, ganada o perdida— y su probabilidad, de
    la tabla de etapas. Si la exportación trae ganada y cerrada (Salesforce) o el estado (Dynamics),
    esos mandan."""
    e = et.get(norm(f.get("etapa"))) or {}
    tipo = e.get("tipo", ABIERTA)
    if str(f.get("estado") or "").strip():          # Dynamics: el statecode manda
        est = norm(f["estado"])
        tipo = GANADA if est in ESTADO_GANADA else PERDIDA if est in ESTADO_PERDIDA else ABIERTA
    elif "ganada" in f and str(f.get("ganada")).strip():
        ganada = norm(f["ganada"]) in VERDAD
        cerrada = norm(f.get("cerrada")) in VERDAD if "cerrada" in f else ganada
        tipo = GANADA if ganada else PERDIDA if cerrada else ABIERTA
    return {"id": str(f["id"]).strip(), "nombre": f.get("nombre"), "cuenta": f.get("cuenta"), "etapa": f.get("etapa"),
            "monto": numero(f.get("monto")) or 0.0, "cierre": f.get("cierre"), "responsable": f.get("responsable"),
            "ultima_actividad": f.get("ultima_actividad"), "linea": f.get("linea"), "tipo": tipo,
            "probabilidad": e.get("probabilidad"), "exige": e.get("exige") or [], "etapa_conocida": bool(e),
            "_fila": f["_fila"]}


def embudo(cfg: dict, no_proc: list) -> dict:
    """Cada exportación como un corte del embudo, y la historia de cada oportunidad entre cortes."""
    snaps, historia, np_ = exportaciones(cfg)
    no_proc += np_
    et = etapas(cfg, no_proc)
    docs = cfg["_docs"]
    cortes = []
    for s in snaps:
        ops = {}
        for f in s["filas"]:
            o = oportunidad(f, s["formato"], et)
            o["cita"] = {"archivo": rel(s["ruta"], docs), "fila": f["_fila"]}
            ops[o["id"]] = o
        cortes.append({"fecha": s["fecha"], "formato": s["formato"], "archivo": rel(s["ruta"], docs), "ops": ops,
                       "actividad": "ultima_actividad" in s["columnas"]})
    desconocidas = sorted({o["etapa"] for c in cortes[-1:] for o in c["ops"].values() if not o["etapa_conocida"]} - {None, ""}) if et else []
    for x in desconocidas:
        no_proc.append({"archivo": cortes[-1]["archivo"], "motivo": f"la etapa «{x}» no está en la tabla de etapas"})
    # Las veces que se corrió cada cierre, del historial si llega (F-03) o de un corte a otro.
    corridas: dict[str, list] = {}
    if historia:
        for h in historia:
            for f in h["filas"]:
                if norm(f["campo"]) not in ("closedate", "close_date"):
                    continue
                a, b = fecha(f["anterior"]), fecha(f["nuevo"])
                if a and b and b > a:
                    corridas.setdefault(str(f["id"]).strip(), []).append({"de": iso(a), "a": iso(b), "cita": {"archivo": rel(h["ruta"], docs), "fila": f["_fila"]}})
    else:
        for prev, cur in zip(cortes, cortes[1:]):
            for k, o in cur["ops"].items():
                p = prev["ops"].get(k)
                if p and p["cierre"] and o["cierre"] and o["cierre"] > p["cierre"]:
                    corridas.setdefault(k, []).append({"de": iso(p["cierre"]), "a": iso(o["cierre"]), "cita": o["cita"]})
    # El último cambio de cada oportunidad entre cortes: etapa, monto o cierre.
    cambio: dict[str, dt.date] = {}
    for prev, cur in zip([None] + cortes[:-1], cortes):
        for k, o in cur["ops"].items():
            p = prev["ops"].get(k) if prev else None
            if p is None or (p["etapa"], p["monto"], p["cierre"]) != (o["etapa"], o["monto"], o["cierre"]):
                cambio[k] = cur["fecha"]
    return {"cortes": cortes, "etapas": et, "corridas": corridas, "cambio": cambio}


# ================================================================ las fichas de cada periodo

CONTACTO = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+|\+?\d[\d ()-]{8,}\d")


def _con_contacto(d) -> bool:
    """Un correo o un teléfono en la ficha: los datos de contacto de los clientes no entran (ADR 0019)."""
    texto = json.dumps({k: v for k, v in (d or {}).items() if k not in ("source", "cite")}, ensure_ascii=False) if isinstance(d, dict) else str(d)
    return bool(CONTACTO.search(re.sub(r'"(source|date|approved_on|amount|list_amount|value|discount_pct)": "?[^,}]*', "", texto)))


def revisar_ficha_augusto(f: dict) -> list[str]:
    p = []
    for i, e in enumerate(f.get("evidence") or []):
        for k in ("opportunity", "type", "source"):
            if not e.get(k):
                p.append(f"evidence[{i}]: falta {k}")
        if e.get("date") and not fecha(e["date"]):
            p.append(f"evidence[{i}]: date no es una fecha; una fecha que nadie dijo se deja vacía")
        if e.get("amount") not in (None, "") and numero(e.get("amount")) is None:
            p.append(f"evidence[{i}]: amount no es un número")
        if _con_contacto(e):
            p.append(f"evidence[{i}]: trae un correo o un teléfono; los datos de contacto de los clientes no entran a la ficha")
    d = f.get("declared_forecast")
    if d is not None and (not isinstance(d, dict) or numero(d.get("value")) is None or not d.get("source")):
        p.append("declared_forecast: lleva value, source y date, o no va")
    for i, q in enumerate(f.get("questions") or []):
        if not q.get("question") or "answer" not in q:
            p.append(f"questions[{i}]: lleva question y answer")
    return p


def revisar_ficha_valeria(f: dict) -> list[str]:
    p = []
    for i, q in enumerate(f.get("quotes") or []):
        qid = q.get("id") or f"quotes[{i}]"
        for k in ("id", "opportunity", "source"):
            if not q.get(k):
                p.append(f"{qid}: falta {k}")
        if numero(q.get("discount_pct")) is None:
            p.append(f"{qid}: discount_pct no es un número; un descuento que el documento no trae es 0")
        if q.get("approved_on") and not fecha(q["approved_on"]):
            p.append(f"{qid}: approved_on no es una fecha")
        if _con_contacto(q):
            p.append(f"{qid}: trae un correo o un teléfono; los datos de contacto de los clientes no entran a la ficha")
    for i, q in enumerate(f.get("questions") or []):
        if not q.get("question") or "answer" not in q:
            p.append(f"questions[{i}]: lleva question y answer")
    return p


# ================================================================ la configuración

DEFECTOS = {
    "thresholds": {
        "stalled_days": 30,             # días sin actividad que detienen una oportunidad abierta
        "max_close_moves": 2,           # veces que puede correrse una fecha de cierre antes de señalarse
        "forecast_tolerance_pct": 10,   # cuánto puede superar lo comprometido a lo que lo sostiene
        "target_threshold_pct": 15,     # cuánto puede apartarse lo cerrado de la meta prorrateada
        "contract_grace_days": 15,      # días desde el cierre ganado para que el contrato esté firmado
        "won_lookback_days": 90,        # hasta cuántos días atrás se mira una oportunidad ganada
        "invoice_days": 30,             # plazo de facturación de un contrato firmado
        "signed_lookback_days": 120,    # hasta cuántos días atrás se mira un contrato firmado
        "commission_tolerance": 1.0,    # diferencia de una comisión que no es diferencia
    },
    "crm": {"format": None, "columns": {}, "date_order": "dmy"},
    "report": {"language": "es"},
}
SEVERIDAD = {
    "forecast_unsupported": 1, "won_without_contract": 1, "commission_differs_from_plan": 1,
    "signed_without_invoice": 1, "discount_outside_policy": 2, "stage_without_evidence": 2,
    "target_vs_closed": 2, "close_date_slipped": 3, "stalled_opportunity": 3,
}
N.SEVERIDAD.update(SEVERIDAD)


def umbral(cfg: dict, k: str):
    return (cfg.get("thresholds") or {}).get(k, DEFECTOS["thresholds"][k])


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
        p.append("period vacío: el periodo comercial que se evalúa, AAAA-MM")
    fmt = (cfg.get("crm") or {}).get("format")
    if fmt not in (None, "salesforce", "hubspot", "dynamics", "zoho", "generico"):
        p.append("crm.format es salesforce, hubspot, dynamics, zoho o generico")
    # En HubSpot la empresa asociada va en su propia columna, con un nombre que la exportación no
    # fija (F-05): sin decir cuál es, lo ganado no se cruza con lo facturado (CSO-3).
    if fmt == "hubspot" and not ((cfg.get("crm") or {}).get("columns") or {}).get("cuenta"):
        p.append("crm.columns.cuenta vacío: en HubSpot la empresa asociada va en su propia columna; di cuál es con su cabecera tal cual")
    if rol == "valeria":
        rv = cfg.get("revenue") or {}
        for k in ("contract_records", "invoice_records"):
            if not rv.get(k):
                p.append(f"revenue.{k} vacío: dónde están las fichas de {'Fidel' if k == 'contract_records' else 'Clara'}")
    return p


def _ruta(cfg: dict, v) -> Path | None:
    if not v:
        return None
    p = Path(v).expanduser()
    return p if p.is_absolute() else Path(cfg.get("_raiz") or Path.cwd()) / p


def rango(periodo: str, hoy: dt.date) -> tuple[dt.date, dt.date, float]:
    """El inicio y el fin del periodo, y la fracción transcurrida al corte."""
    ini, fin = inicio_de_mes(periodo), fin_de_mes(periodo)
    dias = (fin - ini).days + 1
    pasados = max(0, min((min(hoy, fin) - ini).days + 1, dias))
    return ini, fin, pasados / dias


# ================================================================ Augusto · el pronóstico

def augusto(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _PAIS[0] = N.pais_de(cfg)
    docs, estado = cfg["_docs"], cfg["_estado"]
    ficha = leer_json(estado / "comercial" / periodo / "ficha.json", {}) or {}
    problemas = revisar_ficha_augusto(ficha)
    al: list[dict] = []
    no_proc: list[dict] = []
    em = embudo(cfg, no_proc)
    cortes = em["cortes"]
    ini, fin, frac = rango(periodo, hoy)
    ultimo = cortes[-1] if cortes else {"ops": {}, "fecha": None, "archivo": None, "formato": None}
    ops = ultimo["ops"]
    # La evidencia que el agente llevó a la ficha, por oportunidad y tipo.
    evid: dict[str, dict[str, list]] = {}
    for e in ficha.get("evidence") or []:
        evid.setdefault(str(e.get("opportunity")).strip(), {}).setdefault(tipo_doc(e.get("type")), []).append(e)
    # Lo que está en 30-evidencia/ y no en la ficha: se le dice a quien la escribe.
    carpeta = docs / "30-evidencia"
    en_ficha = {str(e.get("source")) for e in ficha.get("evidence") or []}
    for p in sorted(x for x in carpeta.rglob("*") if x.is_file() and not x.name.startswith(".")) if carpeta.is_dir() else []:
        r = rel(p, docs)
        if r not in en_ficha and any(norm(p.name).startswith(norm(k) + "_") for k in ops):
            problemas.append(f"{r} es evidencia de una oportunidad del embudo y no está en la ficha: corre pipeline-scan")

    def con_evidencia(o: dict) -> list[str]:
        """Los documentos que exige su etapa y que la ficha no tiene."""
        return [d for d in o["exige"] if d not in evid.get(o["id"], {})]

    # 1 · Etapa sin evidencia, 2 · detenida, 3 · cierre que se corre.
    filas = []
    dias_det, moves = umbral(cfg, "stalled_days"), umbral(cfg, "max_close_moves")
    for k, o in sorted(ops.items()):
        if o["tipo"] == PERDIDA:
            continue
        en_periodo = o["cierre"] and ini <= o["cierre"] <= fin
        faltan = con_evidencia(o)
        # La última actividad la dice el CRM; si su exportación no la trae, el último corte en que la
        # oportunidad cambió de etapa, de monto o de fecha de cierre.
        ultima = o["ultima_actividad"] if ultimo.get("actividad") else em["cambio"].get(k)
        dias = (hoy - ultima).days if ultima else None
        veces = em["corridas"].get(k, [])
        fila = {"id": k, "nombre": o["nombre"], "etapa": o["etapa"], "monto": redondo(o["monto"]), "cierre": iso(o["cierre"]),
                "tipo": o["tipo"], "falta": faltan, "dias_sin_actividad": dias, "veces_corrido": len(veces)}
        filas.append(fila)
        if faltan and (o["tipo"] == ABIERTA or en_periodo):
            al.append(alerta("stage_without_evidence", f"{k} · {o['nombre'] or ''}: está en «{o['etapa']}» y la ficha no tiene {', '.join(NOMBRE_DOC.get(f, f.replace('_', ' ')) for f in faltan)}",
                             o["cita"], o["monto"], clave=f"etapa:{k}"))
        if o["tipo"] == ABIERTA and dias is not None and dias > dias_det:
            al.append(alerta("stalled_opportunity", f"{k} · {o['nombre'] or ''}: abierta en «{o['etapa']}», sin actividad desde el {iso(ultima)} ({dias} días)",
                             o["cita"], o["monto"], dias=dias, clave=f"detenida:{k}"))
        if o["tipo"] == ABIERTA and len(veces) > moves:
            al.append(alerta("close_date_slipped", f"{k} · {o['nombre'] or ''}: la fecha de cierre se corrió {len(veces)} veces, de {veces[0]['de']} a {veces[-1]['a']}",
                             [v["cita"] for v in veces][-3:], o["monto"], clave=f"corre:{k}"))

    # 4 · Pronóstico sin respaldo.
    cerrado = sum(o["monto"] for o in ops.values() if o["tipo"] == GANADA and o["cierre"] and ini <= o["cierre"] <= min(fin, hoy))
    abiertas = [o for o in ops.values() if o["tipo"] == ABIERTA and o["cierre"] and ini <= o["cierre"] <= fin]
    pond_ev = sum(o["monto"] * (o["probabilidad"] or 0) / 100 for o in abiertas if not con_evidencia(o))
    pond_sin = sum(o["monto"] * (o["probabilidad"] or 0) / 100 for o in abiertas if con_evidencia(o))
    respaldo = cerrado + pond_ev
    dec = ficha.get("declared_forecast") or {}
    comprometido = numero(dec.get("value")) if dec else None
    tol = umbral(cfg, "forecast_tolerance_pct")
    if comprometido is not None and comprometido > respaldo * (1 + tol / 100) + 0.005:
        al.append(alerta("forecast_unsupported", f"{periodo}: se comprometieron {mon(comprometido)} y lo cerrado más lo ponderado con evidencia suma {mon(respaldo)}; la tolerancia es {tol} %",
                         [{"archivo": dec.get("source")}] + ([{"archivo": ultimo["archivo"]}] if ultimo["archivo"] else []),
                         comprometido - respaldo, clave=f"pronostico:{periodo}"))
    elif comprometido is None:
        no_proc.append({"archivo": "20-comite/", "motivo": f"la ficha no trae el pronóstico comprometido de {periodo}: sin él no se compara"})

    # 5 · Meta contra lo cerrado, por línea si la meta la trae; nunca por persona.
    metas = []
    mf = buscar(docs / "00-referencia", "metas")
    if mf:
        t = Tabla(mf[0], ["periodo", "meta"], ["linea"], (cfg.get("columns") or {}).get("targets"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            umb = umbral(cfg, "target_threshold_pct")
            for x in t.filas:
                if str(x["periodo"]).strip()[:7] != periodo:
                    continue
                linea = str(x.get("linea") or "").strip()
                meta = numero(x["meta"]) or 0.0
                esperado = meta * frac
                cer = sum(o["monto"] for o in ops.values() if o["tipo"] == GANADA and o["cierre"] and ini <= o["cierre"] <= min(fin, hoy)
                          and (not linea or norm(o["linea"]) == norm(linea)))
                desv = (cer - esperado) / esperado * 100 if esperado else None
                metas.append({"linea": linea or "total", "meta": redondo(meta), "esperado": redondo(esperado), "cerrado": redondo(cer),
                              "desviacion_pct": redondo(desv)})
                if desv is not None and abs(desv) > umb:
                    al.append(alerta("target_vs_closed", f"{periodo}{' · ' + linea if linea else ''}: cerrado {mon(cer)} contra {mon(esperado)} esperado al corte ({pct(frac * 100)} % del periodo de una meta de {mon(meta)}): {pct(desv)} %",
                                     t.cita(x, docs), cer - esperado, clave=f"meta:{periodo}" + (f":{norm(linea)}" if linea else "")))
    else:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está la tabla de metas"})

    # Qué cambió entre la exportación anterior y la última.
    cambios = {"nuevas": [], "ganadas": [], "perdidas": [], "etapa": [], "monto": [], "cierre": []}
    if len(cortes) > 1:
        prev = cortes[-2]["ops"]
        for k, o in sorted(ops.items()):
            p = prev.get(k)
            if not p:
                cambios["nuevas"].append(k)
                continue
            if o["tipo"] != p["tipo"] and o["tipo"] in (GANADA, PERDIDA):
                cambios["ganadas" if o["tipo"] == GANADA else "perdidas"].append(k)
            elif o["etapa"] != p["etapa"]:
                cambios["etapa"].append(f"{k}: {p['etapa']} → {o['etapa']}")
            if o["monto"] != p["monto"]:
                cambios["monto"].append(f"{k}: {mon(p['monto'])} → {mon(o['monto'])}")
            if o["cierre"] != p["cierre"]:
                cambios["cierre"].append(f"{k}: {iso(p['cierre'])} → {iso(o['cierre'])}")
    partes = {
        "pipeline-scan": {"exportaciones": [{"archivo": c["archivo"], "fecha": iso(c["fecha"]), "formato": c["formato"], "oportunidades": len(c["ops"])} for c in cortes],
                          "cambios": cambios, "evidencia": len(ficha.get("evidence") or []), "fuentes": _fuentes(cortes)},
        "pipeline-check": {"oportunidades": filas, "fuentes": _fuentes(cortes)},
        "forecast-check": {"comprometido": redondo(comprometido), "fuente": dec.get("source"), "cerrado": redondo(cerrado),
                           "ponderado_con_evidencia": redondo(pond_ev), "ponderado_sin_evidencia": redondo(pond_sin), "respaldo": redondo(respaldo),
                           "diferencia": redondo(comprometido - respaldo) if comprometido is not None else None,
                           "abiertas": [{"id": o["id"], "nombre": o["nombre"], "etapa": o["etapa"], "monto": redondo(o["monto"]), "probabilidad": o["probabilidad"],
                                         "ponderado": redondo(o["monto"] * (o["probabilidad"] or 0) / 100), "con_evidencia": not con_evidencia(o), "cierre": iso(o["cierre"])}
                                        for o in sorted(abiertas, key=lambda o: (o["cierre"], o["id"]))]},
        "target-check": {"metas": metas, "transcurrido_pct": redondo(frac * 100)},
    }
    # Lo que vence, para Rostrum: las oportunidades abiertas que cierran en los próximos 30 días sin su evidencia.
    vence = sorted(({"fecha": iso(o["cierre"]), "que": f"{o['id']} · cierre esperado sin {', '.join(con_evidencia(o))}", "caso": periodo,
                     "estado": "pendiente", "comando": "pipeline-check"}
                    for o in ops.values() if o["tipo"] == ABIERTA and o["cierre"] and 0 <= (o["cierre"] - hoy).days <= 30 and con_evidencia(o)),
                   key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "augusto", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(ultimo["fecha"]) if ultimo["fecha"] else iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence}


def _fuentes(cortes: list[dict]) -> list[str]:
    f = {"salesforce": "F-02", "hubspot": "F-04", "dynamics": "F-06", "zoho": "F-08"}
    return sorted({f[c["formato"]] for c in cortes if c["formato"] in f})


# ================================================================ Valeria · de la venta a la factura

def fichas_fidel(ruta: Path | None) -> dict[str, dict]:
    """Las fichas de los contratos que escribe Fidel (criterio-legal), tal como están en su estado."""
    if not ruta:
        return {}
    base = ruta if ruta.name == "contratos" or any(ruta.glob("*.json")) else ruta / "contratos"
    out = {}
    for f in sorted(base.glob("*.json")) if base.is_dir() else []:
        d = leer_json(f, {}) or {}
        if d.get("code"):
            out[str(d["code"]).upper()] = dict(d, _archivo=f.name)
    return out


def facturas_clara(ruta: Path | None) -> tuple[list[dict], set[str]]:
    """Las facturas emitidas que Clara (criterio-finance) dejó en cada cierre, y los periodos que
    cubren: una factura de un periodo que Clara no ha cerrado no se puede dar por ausente."""
    if not ruta:
        return [], set()
    base = ruta / "cierre" if (ruta / "cierre").is_dir() else ruta
    out, periodos = [], set()
    for f in sorted(base.glob("*/resultados.json")) if base.is_dir() else []:
        d = leer_json(f, {}) or {}
        ec = ((d.get("partes") or {}).get("einvoice-check") or {})
        if "emitidas" not in ec:
            continue
        periodos.add(f.parent.name)
        for x in ec["emitidas"]:
            out.append(dict(x, _periodo=f.parent.name))
    return out, periodos


def _firmado(c: dict) -> dt.date | None:
    return fecha(c.get("signed_on")) or fecha(c.get("start"))


def valeria(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _PAIS[0] = N.pais_de(cfg)
    docs, estado = cfg["_docs"], cfg["_estado"]
    ficha = leer_json(estado / "ingresos" / periodo / "ficha.json", {}) or {}
    problemas = revisar_ficha_valeria(ficha)
    al: list[dict] = []
    no_proc: list[dict] = []
    cols = cfg.get("columns") or {}
    em = embudo(cfg, no_proc)
    ops = em["cortes"][-1]["ops"] if em["cortes"] else {}
    ini, fin, _ = rango(periodo, hoy)
    tol = umbral(cfg, "commission_tolerance")

    # 6 · Descuento fuera de política.
    niveles = []
    mf = buscar(docs / "00-referencia", "matriz-descuentos")
    if mf:
        t = Tabla(mf[0], ["nivel", "tope"], ["aprueba"], cols.get("discounts"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            niveles = sorted(({"nivel": x["nivel"], "tope": numero(x["tope"]) or 0.0, "aprueba": norm(x.get("aprueba")),
                              "quien": str(x.get("aprueba") or "").strip(), "cita": t.cita(x, docs)} for x in t.filas),
                             key=lambda n: n["tope"])
    else:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está la matriz de descuentos"})
    cotizaciones = []
    for q in ficha.get("quotes") or []:
        d = numero(q.get("discount_pct")) or 0.0
        k = next((i for i, n in enumerate(niveles) if n["tope"] + 1e-9 >= d), None)
        nivel = niveles[k] if k is not None else None
        pide = nivel["aprueba"] if nivel else None
        validos = {n["aprueba"] for n in niveles[k:]} - {"", "ninguno", "ninguna", "no"} if k is not None else set()
        tiene = norm(q.get("approver_role"))
        ok_ = bool(niveles) and nivel is not None and (pide in ("", "ninguno", "ninguna", "no") or tiene in validos)
        lista = numero(q.get("list_amount"))
        cotizaciones.append({"id": q.get("id"), "oportunidad": q.get("opportunity"), "descuento_pct": d, "nivel": nivel["nivel"] if nivel else None,
                             "pide": pide or None, "aprobo": q.get("approved_by"), "cargo": q.get("approver_role"), "dentro": ok_})
        if niveles and not ok_:
            motivo = (f"ningún nivel de la matriz cubre un descuento de {pct(d)} %" if nivel is None else
                      f"el {pct(d)} % cae en el nivel {nivel['nivel']}, que pide la aprobación de {nivel['quien'] or pide}, y " +
                      (f"lo aprobó {q.get('approved_by')} como {q.get('approver_role')}" if q.get("approved_by") else "no tiene aprobación"))
            al.append(alerta("discount_outside_policy", f"{q.get('id')} · {q.get('opportunity')}: {motivo}",
                             [{"archivo": q.get("source")}] + ([nivel["cita"]] if nivel else []),
                             (lista or 0) * d / 100 if lista else None, clave=f"descuento:{q.get('id')}"))

    # Las cuentas, los contratos de Fidel y las facturas de Clara.
    cuentas = _cuentas(cfg, no_proc)
    rv = cfg.get("revenue") or {}
    fidel = fichas_fidel(_ruta(cfg, rv.get("contract_records")))
    emitidas, cubiertos = facturas_clara(_ruta(cfg, rv.get("invoice_records")))
    if rv.get("contract_records") and not fidel:
        no_proc.append({"archivo": str(rv["contract_records"]), "motivo": "no hay fichas de contratos de Fidel ahí"})
    if rv.get("invoice_records") and not cubiertos:
        no_proc.append({"archivo": str(rv["invoice_records"]), "motivo": "no hay cierres de Clara con sus facturas emitidas ahí"})
    por_cliente: dict[str, list] = {}
    for c in fidel.values():
        por_cliente.setdefault(ident((c.get("counterparty") or {}).get("id")), []).append(c)
    fact_de: dict[str, list] = {}
    for x in emitidas:
        fact_de.setdefault(ident(x.get("receptor")), []).append(x)

    def id_de(o: dict) -> str | None:
        return cuentas.get(norm(o.get("cuenta"))) if o.get("cuenta") else None

    # 7 · Ganado sin contrato.
    gracia, mirar = umbral(cfg, "contract_grace_days"), umbral(cfg, "won_lookback_days")
    ganadas = []
    sin_cuenta = set()
    for k, o in sorted(ops.items()):
        if o["tipo"] != GANADA or not o["cierre"] or (hoy - o["cierre"]).days > mirar or o["cierre"] > hoy:
            continue
        tid = id_de(o)
        fila = {"id": k, "nombre": o["nombre"], "cuenta": o["cuenta"], "monto": redondo(o["monto"]), "cierre": iso(o["cierre"]),
                "contrato": None, "factura": None}
        ganadas.append(fila)
        if not tid:
            sin_cuenta.add(str(o.get("cuenta") or "(sin cuenta)"))
            continue
        cs = [c for c in por_cliente.get(tid, []) if c.get("signed_by_both") is True and _firmado(c) and _firmado(c) <= hoy
              and (not fecha(c.get("end")) or fecha(c["end"]) >= o["cierre"])]
        if cs:
            fila["contrato"] = cs[0]["code"]
        elif fidel and (hoy - o["cierre"]).days > gracia:
            al.append(alerta("won_without_contract", f"{k} · {o['nombre'] or ''}: ganada el {iso(o['cierre'])} por {mon(o['monto'])} y las fichas de Fidel no tienen un contrato firmado con el cliente {tid}",
                             o["cita"], o["monto"], dias=(hoy - o["cierre"]).days, clave=f"contrato:{k}"))
        fs = [x for x in fact_de.get(tid, []) if fecha(x.get("fecha")) and fecha(x["fecha"]) >= o["cierre"]]
        fila["factura"] = fs[0].get("numero") if fs else None
    for x in sorted(sin_cuenta):
        no_proc.append({"archivo": "00-referencia/cuentas", "motivo": f"la cuenta «{x}» de una oportunidad ganada no está en la tabla de cuentas: sin su identificación no se cruza"})

    # 8 · Firmado sin factura: los contratos con un cliente de la tabla de cuentas.
    clientes = set(cuentas.values())
    plazo, mirar_f = umbral(cfg, "invoice_days"), umbral(cfg, "signed_lookback_days")
    contratos = []
    for code, c in sorted(fidel.items()):
        tid = ident((c.get("counterparty") or {}).get("id"))
        s = _firmado(c)
        if tid not in clientes or c.get("signed_by_both") is not True or not s or s > hoy or (hoy - s).days > mirar_f:
            continue
        limite = s + dt.timedelta(days=plazo)
        fs = [x for x in fact_de.get(tid, []) if fecha(x.get("fecha")) and s <= fecha(x["fecha"]) <= limite]
        cubierto = limite.strftime("%Y-%m") in cubiertos or limite <= max((fin_de_mes(p) for p in cubiertos), default=dt.date.min)
        fila = {"codigo": code, "cliente": tid, "firmado": iso(s), "limite": iso(limite), "factura": fs[0].get("numero") if fs else None,
                "estado": "facturado" if fs else ("vencido" if limite < hoy and cubierto else "en plazo" if limite >= hoy else "sin cierre de Clara")}
        contratos.append(fila)
        if not fs and limite < hoy and cubierto:
            al.append(alerta("signed_without_invoice", f"{code}: firmado con el cliente {tid} el {iso(s)} y las fichas de Clara no tienen una factura emitida a ese cliente hasta el {iso(limite)}",
                             {"archivo": f"contratos/{c['_archivo']}"}, numero(c.get("value")), dias=(hoy - limite).days, clave=f"factura:{code}"))
        elif not fs and limite < hoy:
            no_proc.append({"archivo": f"contratos/{c['_archivo']}", "motivo": f"el plazo de facturación venció el {iso(limite)} y Clara todavía no cerró ese periodo: no se da por ausente"})

    # 9 · Comisión distinta del plan, sobre lo ganado en el periodo y ya facturado.
    plan, liquidacion, comisiones = {}, [], []
    pf = buscar(docs / "00-referencia", "plan-comisiones")
    if pf:
        t = Tabla(pf[0], ["tasa"], ["linea"], cols.get("commission_plan"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            plan = {norm(x.get("linea")) or "todas": numero(x["tasa"]) or 0.0 for x in t.filas}
    else:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está el plan de comisiones"})
    lf = buscar(docs / "50-comisiones", f"liquidacion-{periodo}")
    if lf and plan:
        t = Tabla(lf[0], ["responsable", "liquidado"], [], cols.get("commission_settlement"))
        if t.faltan:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        else:
            liquidacion = [dict(x, cita=t.cita(x, docs)) for x in t.filas]
    elif plan:
        no_proc.append({"archivo": "50-comisiones/", "motivo": f"no está la liquidación de {periodo}"})
    if liquidacion:
        base: dict[str, dict] = {}
        for k, o in sorted(ops.items()):
            if o["tipo"] != GANADA or not o["cierre"] or not (ini <= o["cierre"] <= fin):
                continue
            tid = id_de(o)
            facturada = bool(tid and [x for x in fact_de.get(tid, []) if fecha(x.get("fecha")) and o["cierre"] <= fecha(x["fecha"]) <= hoy])
            tasa = plan.get(norm(o["linea"]), plan.get("todas"))
            b = base.setdefault(norm(o["responsable"]), {"responsable": o["responsable"], "esperado": 0.0, "oportunidades": []})
            if facturada and tasa is not None:
                b["esperado"] += o["monto"] * tasa / 100
                b["oportunidades"].append(k)
        vistos = set()
        for x in liquidacion:
            r = norm(x["responsable"])
            vistos.add(r)
            esperado = base.get(r, {}).get("esperado", 0.0)
            liq = numero(x["liquidado"]) or 0.0
            comisiones.append({"responsable": x["responsable"], "esperado": redondo(esperado), "liquidado": redondo(liq), "diferencia": redondo(liq - esperado),
                               "oportunidades": base.get(r, {}).get("oportunidades", [])})
            if abs(liq - esperado) > tol:
                al.append(alerta("commission_differs_from_plan", f"{periodo} · {x['responsable']}: se liquidaron {mon(liq)} y el plan da {mon(esperado)} sobre lo ganado y facturado ({', '.join(base.get(r, {}).get('oportunidades', [])) or 'nada'})",
                                 x["cita"], liq - esperado, clave=f"comision:{periodo}:{r}"))
        for r, b in sorted(base.items()):
            if r not in vistos and b["esperado"] > tol:
                comisiones.append({"responsable": b["responsable"], "esperado": redondo(b["esperado"]), "liquidado": 0.0, "diferencia": redondo(-b["esperado"]), "oportunidades": b["oportunidades"]})
                al.append(alerta("commission_differs_from_plan", f"{periodo} · {b['responsable']}: el plan da {mon(b['esperado'])} sobre lo ganado y facturado ({', '.join(b['oportunidades'])}) y la liquidación no lo trae",
                                 {"archivo": rel(lf[0], docs)}, -b["esperado"], clave=f"comision:{periodo}:{r}"))
    publicar = bool(rv.get("publish_commissions"))
    partes = {
        "deal-scan": {"cotizaciones": len(cotizaciones), "exportacion": em["cortes"][-1]["archivo"] if em["cortes"] else None},
        "discount-check": {"cotizaciones": cotizaciones, "niveles": [{k: v for k, v in n.items() if k != "cita"} for n in niveles]},
        "won-to-invoice": {"ganadas": ganadas, "contratos": contratos, "plazo": plazo},
        "commission-check": {"comisiones": comisiones, "plan": plan, "publicar": publicar},
    }
    vence = sorted(({"fecha": x["limite"], "que": f"{x['codigo']} · plazo de facturación", "caso": periodo, "estado": "pendiente", "comando": "won-to-invoice"}
                    for x in contratos if x["estado"] == "en plazo" and (fecha(x["limite"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "valeria", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(min(fin, hoy)), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ el reporte

NOMBRE = {"augusto": "Augusto", "valeria": "Valeria"}
SENALES_DE = {
    "pipeline-check": {"stage_without_evidence", "stalled_opportunity", "close_date_slipped"},
    "forecast-check": {"forecast_unsupported"},
    "target-check": {"target_vs_closed"},
    "discount-check": {"discount_outside_policy"},
    "won-to-invoice": {"won_without_contract", "signed_without_invoice"},
    "commission-check": {"commission_differs_from_plan"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-cso")


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "pipeline-scan":
        l += ["| Exportación | Fecha | Formato | Oportunidades |", "|---|---|---|---|"]
        l += [f"| `{x['archivo']}` | {x['fecha']} | {x['formato']} | {x['oportunidades']} |" for x in p["exportaciones"]]
        c = p["cambios"]
        l += ["", f"**Desde la exportación anterior:** {len(c['nuevas'])} nuevas, {len(c['ganadas'])} ganadas, {len(c['perdidas'])} perdidas, "
              f"{len(c['etapa'])} cambios de etapa, {len(c['monto'])} de monto y {len(c['cierre'])} de fecha de cierre. "
              f"**Evidencia en la ficha:** {p['evidencia']} documentos.", ""]
        for k, t in (("etapa", "Etapa"), ("monto", "Monto"), ("cierre", "Fecha de cierre")):
            if c[k]:
                l += [f"- **{t}:** " + "; ".join(c[k])]
        l.append("")
    elif comando == "pipeline-check":
        l += ["| Oportunidad | Etapa | Monto | Cierre | Falta | Días sin actividad | Veces corrido |", "|---|---|---|---|---|---|---|"]
        l += [f"| {o['id']} · {o['nombre'] or ''} | {o['etapa']} | {_m(o['monto'])} | {o['cierre'] or '—'} | {', '.join(x.replace('_', ' ') for x in o['falta']) or '—'} | "
              f"{o['dias_sin_actividad'] if o['dias_sin_actividad'] is not None else '—'} | {o['veces_corrido']} |" for o in p["oportunidades"]]
        l += ["", "Sin calificar a quien lleva cada oportunidad: la señal es de la oportunidad, no de la persona.", ""]
    elif comando == "forecast-check":
        l += [f"**Comprometido:** {_m(p['comprometido'])}" + (f" (`{p['fuente']}`)" if p.get("fuente") else "") +
              f" · **Cerrado:** {_m(p['cerrado'])} · **Ponderado con evidencia:** {_m(p['ponderado_con_evidencia'])} · "
              f"**Ponderado sin evidencia:** {_m(p['ponderado_sin_evidencia'])} · **Respaldo:** {_m(p['respaldo'])} · **Diferencia:** {_m(p['diferencia'])}", "",
              "| Oportunidad | Etapa | Monto | Probabilidad | Ponderado | Con evidencia | Cierre |", "|---|---|---|---|---|---|---|"]
        l += [f"| {o['id']} · {o['nombre'] or ''} | {o['etapa']} | {_m(o['monto'])} | {_m(o['probabilidad'])} % | {_m(o['ponderado'])} | {'sí' if o['con_evidencia'] else 'no'} | {o['cierre']} |" for o in p["abiertas"]]
        l += ["", "El pronóstico que se compromete es de una persona; aquí solo se dice qué lo sostiene.", ""]
    elif comando == "target-check":
        l += [f"**Transcurrido del periodo:** {_m(p['transcurrido_pct'])} %", "",
              "| Línea | Meta | Esperado al corte | Cerrado | Desviación |", "|---|---|---|---|---|"]
        l += [f"| {x['linea']} | {_m(x['meta'])} | {_m(x['esperado'])} | {_m(x['cerrado'])} | {_m(x['desviacion_pct'])} % |" for x in p["metas"]]
        l += ["", "Por línea, nunca por persona. La meta la fija una persona.", ""]
    elif comando == "deal-scan":
        l += [f"**Cotizaciones en la ficha:** {p['cotizaciones']} · **Exportación:** `{p['exportacion'] or '—'}`", ""]
    elif comando == "discount-check":
        l += ["| Cotización | Oportunidad | Descuento | Nivel | Pide | Aprobó | Cargo | Dentro de la política |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {q['id']} | {q['oportunidad']} | {_m(q['descuento_pct'])} % | {q['nivel'] or '—'} | {q['pide'] or '—'} | {q['aprobo'] or '—'} | {q['cargo'] or '—'} | {'sí' if q['dentro'] else 'no'} |" for q in p["cotizaciones"]]
        l += ["", "Ningún descuento lo aprueba el agente: aquí se dice cuál no tiene la aprobación que pide la matriz.", ""]
    elif comando == "won-to-invoice":
        l += ["| Oportunidad ganada | Cuenta | Monto | Ganada | Contrato (Fidel) | Factura (Clara) |", "|---|---|---|---|---|---|"]
        l += [f"| {g['id']} · {g['nombre'] or ''} | {g['cuenta'] or '—'} | {_m(g['monto'])} | {g['cierre']} | {g['contrato'] or '—'} | {g['factura'] or '—'} |" for g in p["ganadas"]]
        l += ["", "| Contrato | Cliente | Firmado | Plazo de facturación | Factura | Estado |", "|---|---|---|---|---|---|"]
        l += [f"| {c['codigo']} | {c['cliente']} | {c['firmado']} | {c['limite']} | {c['factura'] or '—'} | {c['estado']} |" for c in p["contratos"]]
        l += ["", f"Plazo de facturación configurado: {p['plazo']} días. Los contratos y las facturas son los de las fichas de Fidel y de Clara: no se vuelven a procesar.", ""]
    elif comando == "commission-check":
        l += ["| Responsable | Da el plan | Liquidado | Diferencia | Base |", "|---|---|---|---|---|"]
        l += [f"| {c['responsable']} | {_m(c['esperado'])} | {_m(c['liquidado'])} | {_m(c['diferencia'])} | {', '.join(c['oportunidades']) or '—'} |" for c in p["comisiones"]]
        l += ["", ("Se publica en Rostrum porque la configuración lo dice." if p.get("publicar") else
                   "No se publica en Rostrum: son la remuneración de personas identificables (ADR 0019)."), ""]
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
    if rol == "augusto":
        u = ultima("pipeline-scan")
        if nueva("10-crm", u) or nueva("20-comite", u) or not u or (hoy - u).days >= 7:
            toca.append("pipeline-scan")
            motivo.append("una exportación o un acta nueva, o la revisión semanal del embudo")
        r = augusto(cfg, periodo, hoy)
        if r["alertas"] and ultima("pipeline-check") != hoy:
            toca.append("pipeline-check")
            motivo.append(f"{len(r['alertas'])} señales abiertas en el embudo")
        if 0 <= (fin_de_mes(periodo) - hoy).days <= 7 and ultima("forecast-check") != hoy:
            toca.append("forecast-check")
            motivo.append("el periodo cierra en los próximos siete días")
    else:
        u = ultima("deal-scan")
        if nueva("40-cotizaciones", u) or not u or (hoy - u).days >= 7:
            toca.append("deal-scan")
            motivo.append("cotizaciones nuevas, o la revisión semanal")
        r = valeria(cfg, periodo, hoy)
        if any(a["signal"] in ("won_without_contract", "signed_without_invoice") for a in r["alertas"]) and ultima("won-to-invoice") != hoy:
            toca.append("won-to-invoice")
            motivo.append("una venta ganada sin contrato o un contrato sin factura")
        if nueva("50-comisiones", ultima("commission-check")):
            toca.append("commission-check")
            motivo.append("llegó la liquidación de comisiones")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


# ================================================================ la línea de comandos

def _rol() -> str:
    return "valeria" if N.plugin(AQUI)["name"] == "criterio-revenue" else "augusto"


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    periodo = a.period or cfg.get("period")
    if not periodo:
        raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
    r = (augusto if rol == "augusto" else valeria)(cfg, periodo, hoy)
    destino = cfg["_estado"] / ("comercial" if rol == "augusto" else "ingresos") / periodo / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Augusto y Valeria.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir", "exportacion",
                                       "compute", "reporte", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action == "exportacion":
        if not a.file:
            ap.error("--file es la exportación del CRM")
        cfg = {"crm": {}}
        if a.config:
            cfg, _ = N.cargar_config(a.config)
        e = leer_exportacion(a.file, cfg)
        salida = {"formato": e.get("formato"), "fecha": iso(e.get("fecha")), "faltan": e.get("faltan"), "error": e.get("error"),
                  "filas": len(e.get("filas") or [])}
        if e.get("actividad_sin_mapear"):
            col = e["actividad_sin_mapear"][0]
            salida["pregunta"] = (f"La exportación trae «{col}» y la última actividad no está mapeada. Si es la fecha de la última "
                                  f"gestión de cada oportunidad, regístrala en crm.columns.ultima_actividad; sin ella, una "
                                  f"oportunidad que no cambió de un corte a otro se da por detenida aunque se gestione.")
        print(json.dumps(salida, ensure_ascii=False, indent=2))
        return 0 if not e.get("error") and not e.get("faltan") else 1
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=("comercial", "ingresos"),
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

    hoy = dt.date(2026, 10, 20)
    ok("los países del registro pasan", [c for c in N.PAISES if N.revisar_pais({"country": c})], [])
    ok("HubSpot se reconoce por sus columnas", formato(["record_id", "deal_name", "deal_stage", "close_date", "amount"]), "hubspot")
    ok("HubSpot sin la columna de la empresa asociada: la configuración no pasa",
       any("crm.columns.cuenta" in x for x in revisar_config({"entity": {"id": "1", "name": "x", "country": "CO"}, "period": "2026-10",
                                                               "crm": {"format": "hubspot", "columns": {}}}, "augusto")), True)
    ok("Salesforce por API", formato(["id", "name", "stagename", "closedate", "amount"]), "salesforce")
    ok("Salesforce por un informe", formato(["opportunity_id", "stage", "close_date", "amount"]), "salesforce")
    ok("Dynamics por su exportación a Excel", formato(["topic", "account", "est_revenue", "est_close_date", "pipeline_phase", "status"]), "dynamics")
    ok("Dynamics por su API", formato(["opportunityid", "name", "estimatedvalue", "estimatedclosedate", "stepname", "statecode"]), "dynamics")
    ok("Zoho por su exportación", formato(["record_id", "deal_name", "account_name", "amount", "closing_date", "stage"]), "zoho")
    with tempfile.TemporaryDirectory() as tmp:
        z = Path(tmp) / "Deals_2026_10_01.csv"
        _csv(z, [["Record ID", "Deal Name", "Account Name", "Amount", "Closing Date", "Stage", "Last Activity Time"],
                 ["OPP-1", "Uno", "Cliente", "100", "01/12/2026", "Propuesta", "20/09/2026 10:30"]])
        ok("Zoho: la última actividad sin mapear se pregunta (CCO-4)", leer_exportacion(z, {"crm": {}}).get("actividad_sin_mapear"), ["Last Activity Time"])
        ok("Zoho: mapeada, no se pregunta",
           leer_exportacion(z, {"crm": {"columns": {"ultima_actividad": "Last Activity Time"}}}).get("actividad_sin_mapear"), None)
    ok("en Dynamics el estado manda sobre la etapa: Won es ganada",
       oportunidad({"id": "1", "etapa": "Negociación", "estado": "Won", "monto": "10", "_fila": 2}, "dynamics", {})["tipo"], GANADA)
    ok("en Dynamics, Lost es perdida y Open sigue abierta",
       [oportunidad({"id": "1", "etapa": "x", "estado": v, "monto": "1", "_fila": 2}, "dynamics", {})["tipo"] for v in ("Lost", "Open")], [PERDIDA, ABIERTA])
    ok("el historial de campos", formato(["opportunityid", "field", "oldvalue", "newvalue"]), "historia")
    ok("lo demás es genérico", formato(["codigo", "etapa", "valor", "fecha_cierre"]), "generico")
    ok("10/20/2026 es mes, día", orden_fechas(["10/20/2026", "11/02/2026"]), "mdy")
    ok("20/10/2026 es día, mes", orden_fechas(["20/10/2026"]), "dmy")
    ok("sin un día mayor que 12, el de la configuración", orden_fechas(["02/03/2026"], "mdy"), "mdy")
    ok("la fecha en el nombre de la exportación", fecha_de_nombre(Path("oportunidades-2026-10-15.csv")), dt.date(2026, 10, 15))
    ok("un correo en la ficha se dice", _con_contacto({"opportunity": "OPP-101", "note": "ana@cliente.com"}), True)
    ok("un monto no es un teléfono", _con_contacto({"opportunity": "OPP-101", "amount": "120000000", "source": "x.pdf"}), False)
    ok("el periodo transcurrido", round(rango("2026-10", hoy)[2], 4), round(20 / 31, 4))
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "comercial" / "e1", t / "estado" / "e1"
        _csv(docs / "00-referencia" / "etapas.csv", [["etapa", "orden", "probabilidad", "exige", "tipo"],
                                                      ["Calificación", "1", "10", "", "abierta"], ["Propuesta", "2", "40", "propuesta", "abierta"],
                                                      ["Negociación", "3", "70", "", "abierta"], ["Ganada", "4", "100", "orden de compra", "ganada"],
                                                      ["Perdida", "5", "0", "", "perdida"]])
        _csv(docs / "00-referencia" / "metas.csv", [["periodo", "meta"], ["2026-10", "100000000"]])
        _csv(docs / "00-referencia" / "matriz-descuentos.csv", [["nivel", "tope", "aprueba"], ["1", "10", "ninguno"], ["2", "20", "gerente comercial"], ["3", "30", "gerente general"]])
        _csv(docs / "00-referencia" / "cuentas.csv", [["cuenta", "nombre", "identificacion"], ["ACC-1", "Cliente Uno", "900100100"], ["ACC-2", "Cliente Dos", "900200200"]])
        _csv(docs / "00-referencia" / "plan-comisiones.csv", [["linea", "tasa"], ["todas", "3"]])
        _xlsx_ruta = docs / "10-crm" / "oportunidades-2026-10-01.xlsx"
        _xlsx_ruta.parent.mkdir(parents=True, exist_ok=True)
        _xlsx(_xlsx_ruta, [["Record ID", "Deal Name", "Deal Stage", "Close Date", "Amount", "Deal owner", "Last Activity Date", "Associated Company"],
                           ["OPP-101", "Uno", "Negociación", "2026-10-10", "50000000", "Ana", "2026-09-30", "ACC-1"],
                           ["OPP-102", "Dos", "Propuesta", "2026-10-25", "80000000", "Luis", "2026-08-01", "ACC-2"]])
        _csv(docs / "10-crm" / "oportunidades-2026-10-15.csv", [["Record ID", "Deal Name", "Deal Stage", "Close Date", "Amount", "Deal owner", "Last Activity Date", "Associated Company"],
                                                                ["OPP-101", "Uno", "Ganada", "2026-10-12", "50000000", "Ana", "2026-10-12", "ACC-1"],
                                                                ["OPP-102", "Dos", "Propuesta", "2026-11-30", "80000000", "Luis", "2026-08-01", "ACC-2"]])
        (docs / "30-evidencia").mkdir(parents=True)
        (docs / "30-evidencia" / "OPP-102_propuesta.pdf").write_text("propuesta", encoding="utf-8")
        _csv(docs / "50-comisiones" / "liquidacion-2026-10.csv", [["responsable", "liquidado"], ["Ana", "2000000"]])
        escribir_json(est / "comercial" / "2026-10" / "ficha.json", {"evidence": [{"opportunity": "OPP-102", "type": "propuesta", "amount": 80000000, "date": "2026-09-20", "source": "30-evidencia/OPP-102_propuesta.pdf"}],
                                                                   "declared_forecast": {"value": 120000000, "source": "20-comite/acta-2026-10-02.pdf", "date": "2026-10-02"}})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-10", "_docs": docs, "_estado": est,
               "crm": {"format": "hubspot", "columns": {"cuenta": "Associated Company"}}, "thresholds": {"max_close_moves": 0, "contract_grace_days": 5}}
        r = augusto(cfg, "2026-10", hoy)
        ok("el embudo: ganada sin orden de compra, detenida, cierre corrido, pronóstico sin respaldo y meta",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("close_date_slipped", "corre:OPP-102"), ("forecast_unsupported", "pronostico:2026-10"), ("stage_without_evidence", "etapa:OPP-101"),
            ("stalled_opportunity", "detenida:OPP-102"), ("target_vs_closed", "meta:2026-10")])
        ok("la ficha está completa", r["record_issues"], [])
        ok("lo que cambió entre exportaciones", (r["partes"]["pipeline-scan"]["cambios"]["ganadas"], r["partes"]["pipeline-scan"]["cambios"]["cierre"]),
           (["OPP-101"], ["OPP-101: 2026-10-10 → 2026-10-12", "OPP-102: 2026-10-25 → 2026-11-30"]))
        md = reporte(r, "pipeline-check", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        # Valeria: las fichas de Fidel y de Clara, tal como ellos las escriben.
        legal, cfo = t / "estado-legal" / "contratos", t / "estado-cfo"
        escribir_json(legal / "CTR-109.json", {"code": "CTR-109", "counterparty": {"name": "Cliente Dos", "id": "900200200"}, "signed_by_both": True,
                                             "signed_on": "2026-08-10", "start": "2026-08-10", "end": "2027-08-09", "value": 30000000})
        escribir_json(cfo / "cierre" / "2026-09" / "resultados.json", {"partes": {"einvoice-check": {"emitidas": []}}})
        escribir_json(cfo / "cierre" / "2026-10" / "resultados.json", {"partes": {"einvoice-check": {"emitidas": [
            {"numero": "FE-100", "fecha": "2026-10-14", "receptor": "900100100", "total": 59500000, "archivo": "2026-10/30-facturacion/emitidas/fe-100.xml"}]}}})
        escribir_json(est / "ingresos" / "2026-10" / "ficha.json", {"quotes": [
            {"id": "COT-101", "opportunity": "OPP-101", "list_amount": 60000000, "discount_pct": 18, "approved_by": "Pedro", "approver_role": "jefe de ventas", "source": "40-cotizaciones/COT-101.pdf"},
            {"id": "COT-102", "opportunity": "OPP-102", "list_amount": 80000000, "discount_pct": 8, "source": "40-cotizaciones/COT-102.pdf"},
            {"id": "COT-103", "opportunity": "OPP-102", "list_amount": 80000000, "discount_pct": 15, "approved_by": "Marta", "approver_role": "Gerente general",
             "approved_on": "2026-10-05", "source": "40-cotizaciones/COT-103.pdf"}]})
        cfg["revenue"] = {"contract_records": str(legal), "invoice_records": str(cfo)}
        r = valeria(cfg, "2026-10", hoy)
        ok("la venta: descuento sin la aprobación que pide, ganado sin contrato, firmado sin factura y la comisión",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("commission_differs_from_plan", "comision:2026-10:ana"), ("discount_outside_policy", "descuento:COT-101"),
            ("signed_without_invoice", "factura:CTR-109"), ("won_without_contract", "contrato:OPP-101")])
        ok("la comisión que da el plan: 3 % de lo ganado y facturado", r["partes"]["commission-check"]["comisiones"][0]["esperado"], 1500000.0)
        ok("las comisiones no se publican por omisión", r["partes"]["commission-check"]["publicar"], False)
        ok("un cargo superior también aprueba, y el nivel sin aprobación no la pide",
           [(q["id"], q["dentro"]) for q in r["partes"]["discount-check"]["cotizaciones"]], [("COT-101", False), ("COT-102", True), ("COT-103", True)])
        (t / "salida.md").write_text("lo que se mostró", encoding="utf-8")
        reg = N.corrida(est, "won-to-invoice", t / "salida.md", "2026-10", None, hoy, r, "0.0.0")
        c = leer_json(est / "corridas.json", [])[-1]
        ok("la corrida queda en el formato común, con sus hallazgos por caso",
           (reg["id"], c["que"], c["hallazgos"], sorted(c["por_caso"])), ("2026-10-20-won-to-invoice-1", "won-to-invoice", 4, ["2026-10", "COT-101", "CTR-109", "OPP-101"]))
    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
