#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CFO: lo que calcula el código para Clara y para Tomás.

    python3 finanzas.py <acción> [opciones]       python3 finanzas.py --help

Clara (criterio-finance) cierra el mes; Tomás (criterio-budget) pone el presupuesto al lado de
la ejecución. Los dos comparten este motor, que vive en criterio-finance y se copia a
criterio-budget con scripts/sincronizar.py: un plugin instalado tiene que correr solo.

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas (balance, mayor,
extractos, auxiliares, presupuesto, compromisos, proyecciones) y las facturas electrónicas las
procesa el código directamente. Lo que solo trae un documento escrito —el estado que alguien
declara, un acta de traslado, un requerimiento que llegó por correo— lo extrae el agente a la
ficha, y el código lo cruza. Cada cifra que muestra un comando sale de aquí.

**Dos archivos por periodo, un dueño cada uno.** `ficha.json` la escribe el agente; el código
no la reescribe. `resultados.json` lo escribe el código; el agente no lo toca. Así cada dato
tiene un solo escritor.

**Los formatos se leen desde su fuente oficial.** Cada campo de factura que se procesa cita su
identificador en `families/criterio-cfo/fuentes.json`: el anexo técnico de la DIAN (F-01) y
la ficha técnica del SRI (F-04, F-09). Un campo que no está ahí no se usa.

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
from nucleo import (  # noqa: E402,F401  · MESES_LARGO lo usa el generador del material
    CRITICIDAD, MESES, MESES_LARGO, TABLAS, Tabla, _PAIS, _cita, _csv, _hoy, _m, _xlsx, alerta, buscar,
    csv_filas, dia_habil, escribir_json, estructura, fecha, fin_de_mes, ident,
    inicio_de_mes, inventario, iso, leer_json, marco_reporte, mon, nit_sin_dv, norm, numero, ordenar, pc,
    redondo, registro_corridas, rel, xlsx_filas,
)
ESTRUCTURA = AQUI / "estructura.json"
RECOMENDADO = AQUI.parent / "skills" / "close-checklist" / "references" / "checklist-recomendado.csv"



# ================================================================ facturas electrónicas

# Cada campo que se procesa, con su identificador en la fuente oficial. scripts/familias.py comprueba
# que cada uno esté en families/criterio-cfo/fuentes.json; uno que no esté no se usa.
CAMPOS_DIAN = {
    "FAD05": "/Invoice/cbc:ID",
    "FAD06": "/Invoice/cbc:UUID",
    "FAD08": "/Invoice/cbc:UUID/@schemeName",
    "FAD09": "/Invoice/cbc:IssueDate",
    "FAJ21": "/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID",
    "FAK21": "/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID",
    "FAS02": "/Invoice/cac:TaxTotal/cbc:TaxAmount",
    "FAS16": "/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID",
    "FAU04": "/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount",
    "FAU14": "/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount",
    "CAD05": "/CreditNote/cbc:ID",
    "CAD06": "/CreditNote/cbc:UUID",
    "CAD09": "/CreditNote/cbc:IssueDate",
    "CAJ21": "/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID",
    "CAK21": "/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID",
    "CAS02": "/CreditNote/cac:TaxTotal/cbc:TaxAmount",
    "CAU04": "/CreditNote/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount",
    "CAU14": "/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount",
    "CBG03": "/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID",
    "CBG04": "/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:UUID",
    "AD-6.4": "/AttachedDocument/cac:Attachment/cac:ExternalReference/cbc:Description",
}
CAMPOS_SRI = {
    "T1": "claveAcceso: 49 dígitos (fecha, tipo, RUC, ambiente, serie, secuencial, código, emisión, verificador)",
    "MOD11": "dígito verificador módulo 11 sobre los 48 dígitos",
    "T3": "codDoc: 01, 03, 04, 05, 06, 07",
    "7.2.3": "autorizacion: estado, numeroAutorizacion, fechaAutorizacion, comprobante en CDATA",
    "IT": "infoTributaria: ruc, claveAcceso, codDoc, estab, ptoEmi, secuencial, razonSocial",
    "IF": "infoFactura: fechaEmision (dd/mm/aaaa), identificacionComprador, totalSinImpuestos",
    "TI": "totalConImpuestos/totalImpuesto: codigo, codigoPorcentaje, baseImponible, valor",
    "T16": "codigo de impuesto 2: IVA",
}
TIPOS_SRI = {"01": "factura", "03": "liquidación de compra", "04": "nota de crédito",
             "05": "nota de débito", "06": "guía de remisión", "07": "comprobante de retención"}


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _h(el, *ruta):
    """El primer descendiente por nombres locales, sin depender del espacio de nombres."""
    actual = el
    for nombre in ruta:
        if actual is None:
            return None
        actual = next((c for c in actual if _local(c.tag) == nombre), None)
    return actual


def _t(el, *ruta) -> str | None:
    x = _h(el, *ruta)
    return (x.text or "").strip() if x is not None and x.text is not None else None


def digito_mod11(digitos48: str) -> int:
    """El verificador de la clave de acceso del SRI (F-04, tabla 1): factores 2 a 7 de derecha a izquierda."""
    total, f = 0, 2
    for ch in reversed(digitos48):
        total += int(ch) * f
        f = 2 if f == 7 else f + 1
    r = 11 - (total % 11)
    return 0 if r == 11 else 1 if r == 10 else r


def clave_acceso(clave: str) -> dict:
    """Lo que dice la clave de acceso por sí sola, y si es válida (F-04, tabla 1)."""
    c = re.sub(r"\D", "", clave or "")
    out = {"valida": False, "motivos": []}
    if len(c) != 49:
        out["motivos"].append(f"la clave de acceso tiene {len(c)} dígitos y deben ser 49")
        return out
    out.update({
        "fecha": iso(fecha(f"{c[0:2]}/{c[2:4]}/{c[4:8]}")), "tipo": c[8:10], "ruc": c[10:23],
        "ambiente": c[23], "serie": c[24:30], "secuencial": c[30:39], "emision": c[47],
    })
    if digito_mod11(c[:48]) != int(c[48]):
        out["motivos"].append("el dígito verificador no cuadra con el módulo 11")
    if out["tipo"] not in TIPOS_SRI:
        out["motivos"].append(f"el tipo {out['tipo']} no está en la tabla 3 de la ficha técnica")
    out["valida"] = not out["motivos"]
    return out


def _dian(raiz, tipo: str) -> dict:
    nc = tipo == "CreditNote"
    supplier = _t(raiz, "AccountingSupplierParty", "Party", "PartyTaxScheme", "CompanyID")
    customer = _t(raiz, "AccountingCustomerParty", "Party", "PartyTaxScheme", "CompanyID")
    iva = otros = 0.0
    for tt in (c for c in raiz if _local(c.tag) == "TaxTotal"):
        monto = numero(_t(tt, "TaxAmount")) or 0.0
        esquema = _t(tt, "TaxSubtotal", "TaxCategory", "TaxScheme", "ID")
        if esquema == "01":                                     # F-01, 6.4: 01 · IVA
            iva += monto
        else:
            otros += monto
    uuid = _h(raiz, "UUID")
    d = {
        "pais": "CO", "fuente": "F-01", "tipo": "nota de crédito" if nc else "factura",
        "numero": _t(raiz, "ID"), "id": _t(raiz, "UUID"),
        "esquema": uuid.get("schemeName") if uuid is not None else None,
        "fecha": iso(fecha(_t(raiz, "IssueDate"))),
        "emisor": nit_sin_dv(supplier), "receptor": nit_sin_dv(customer),
        "base": numero(_t(raiz, "LegalMonetaryTotal", "TaxExclusiveAmount")),
        "iva": round(iva, 2), "otros_impuestos": round(otros, 2),
        "total": numero(_t(raiz, "LegalMonetaryTotal", "PayableAmount")),
        "valores": True,
    }
    if nc:
        d["referencia"] = {"numero": _t(raiz, "BillingReference", "InvoiceDocumentReference", "ID"),
                           "id": _t(raiz, "BillingReference", "InvoiceDocumentReference", "UUID")}
    return d


def _sri(raiz) -> dict:
    it = _h(raiz, "infoTributaria")
    clave = _t(it, "claveAcceso") if it is not None else None
    ca = clave_acceso(clave or "")
    cod = _t(it, "codDoc") if it is not None else None
    estab, pto, sec = (_t(it, x) if it is not None else None for x in ("estab", "ptoEmi", "secuencial"))
    d = {
        "pais": "EC", "fuente": "F-04", "tipo": TIPOS_SRI.get(cod or "", f"tipo {cod}"),
        "cod_doc": cod, "id": clave,
        "numero": "-".join(x for x in (estab, pto, sec) if x) or None,
        "emisor": ident(_t(it, "ruc") if it is not None else None),
        "clave": ca, "valores": False,
    }
    if ca.get("valida"):
        for campo, esperado in (("tipo", cod), ("ruc", _t(it, "ruc")), ("serie", f"{estab}{pto}"),
                                ("secuencial", sec)):
            if esperado and ca[campo] != esperado:
                ca["motivos"].append(f"la clave dice {campo} {ca[campo]} y el comprobante {esperado}")
        ca["valida"] = not ca["motivos"]
    if cod == "01":
        inf = _h(raiz, "infoFactura")
        iva = otros = 0.0
        for ti in (inf.iter() if inf is not None else []):
            if _local(ti.tag) == "totalImpuesto":
                v = numero(_t(ti, "valor")) or 0.0
                if _t(ti, "codigo") == "2":                     # F-04, tabla 16: 2 · IVA
                    iva += v
                else:
                    otros += v
        base = numero(_t(inf, "totalSinImpuestos")) if inf is not None else None
        d.update({
            "fecha": iso(fecha(_t(inf, "fechaEmision"))) if inf is not None else ca.get("fecha"),
            "receptor": ident(_t(inf, "identificacionComprador")) if inf is not None else None,
            "base": base, "iva": round(iva, 2), "otros_impuestos": round(otros, 2),
            "total": round((base or 0) + iva + otros, 2) if base is not None else None,
            "valores": base is not None,
        })
    else:
        # Los otros tipos se identifican por la clave de acceso; sus valores no se cruzan en
        # esta versión, porque el formato de sus campos de valor no está verificado (F-09).
        d.update({"fecha": ca.get("fecha"), "receptor": None})
    return d


def leer_factura(ruta: Path) -> dict:
    """Una factura o nota electrónica de la DIAN o del SRI, con o sin su contenedor."""
    try:
        raiz = ET.parse(ruta).getroot()
    except ET.ParseError as e:
        return {"error": f"XML mal formado: {e}"}
    for _ in range(3):
        nombre = _local(raiz.tag)
        if nombre == "AttachedDocument":                        # F-01, 6.4: el contenedor
            interno = _t(raiz, "Attachment", "ExternalReference", "Description")
        elif nombre in ("autorizacion", "RespuestaAutorizacionComprobante"):   # F-04, 7.2.3
            aut = raiz if nombre == "autorizacion" else next(
                (x for x in raiz.iter() if _local(x.tag) == "autorizacion"), None)
            if aut is not None and (_t(aut, "estado") or "").upper() not in ("AUTORIZADO", ""):
                return {"error": f"el SRI no autorizó el comprobante: {_t(aut, 'estado')}"}
            interno = _t(aut, "comprobante") if aut is not None else None
        else:
            break
        if not interno:
            return {"error": f"el contenedor {nombre} no trae el documento"}
        try:
            raiz = ET.fromstring(interno.encode("utf-8"))
        except ET.ParseError as e:
            return {"error": f"el documento dentro de {nombre} no es XML válido: {e}"}
    nombre = _local(raiz.tag)
    if nombre in ("Invoice", "CreditNote"):
        return _dian(raiz, nombre)
    if _h(raiz, "infoTributaria") is not None:
        return _sri(raiz)
    return {"error": f"no es una factura electrónica de la DIAN ni del SRI (raíz {nombre})"}


# ================================================================ la configuración

DEFECTOS = {
    "thresholds": {
        "reconciling_item_days": 30,      # una partida conciliatoria más vieja se señala
        "bank_match_window_days": 5,      # ventana del cruce por valor y fecha
        "amount_tolerance": None,         # None: la del país (CO 2.00 y 5.00 de IVA, F-01 5.2.1; EC 0.01)
        "variance_pct": 10,               # desviación del ejecutado contra el aprobado al corte
        "committed_pct": 95,              # ejecutado más comprometido contra el aprobado del año
        "forecast_stale_days": 45,        # proyección del área sin actualizar
        "close_window_business_days": 10, # ventana del cierre, en días hábiles después del fin de mes
    },
    "holidays": [],
    "report": {"language": "es"},
    "execution": {"workers": 1},
}
TOLERANCIAS = {"CO": (2.00, 5.00), "EC": (0.01, 0.01)}


def tolerancias(cfg: dict) -> tuple[float, float]:
    t = (cfg.get("thresholds") or {}).get("amount_tolerance")
    if t is not None:
        return float(t), float(t)
    return TOLERANCIAS.get(((cfg.get("entity") or {}).get("country") or "CO").upper(), (2.00, 5.00))


def umbral(cfg: dict, k: str):
    return (cfg.get("thresholds") or {}).get(k, DEFECTOS["thresholds"][k])




def revisar_config(cfg: dict, rol: str) -> list[str]:
    p = []
    ent = cfg.get("entity") or {}
    for k in ("id", "name", "country", "currency"):
        if not ent.get(k):
            p.append(f"entity.{k} vacío")
    if (ent.get("country") or "").upper() not in ("CO", "EC"):
        p.append("entity.country debe ser CO o EC en esta versión")
    for k in ("_docs", "_estado"):
        if cfg.get(k) is None:
            p.append(f"paths.{k.strip('_').replace('docs', 'documents').replace('estado', 'state')} vacío")
    if cfg.get("_docs") and not cfg["_docs"].is_dir():
        p.append(f"la carpeta de documentos {cfg['_docs']} no existe")
    if cfg.get("_docs") and cfg.get("_estado"):
        try:
            cfg["_estado"].resolve().relative_to(cfg["_docs"].resolve())
            p.append("el estado no puede vivir dentro de la carpeta de documentos: ahí lo tomaría por un documento")
        except ValueError:
            pass
    if rol == "clara":
        c = cfg.get("accounts") or {}
        for k in ("sales", "purchases", "vat_generated", "vat_deductible"):
            if not c.get(k):
                p.append(f"accounts.{k} vacío: sin él no se cruzan las facturas con la contabilidad")
    if rol == "tomas":
        b = cfg.get("budget") or {}
        if not b.get("year"):
            p.append("budget.year vacío")
    return p




# ================================================================ las señales

SEVERIDAD = {
    "trial_balance_unbalanced": 1, "declared_close_vs_evidence": 1, "declared_vs_evidence": 1,
    "ledger_vs_trial_balance": 1, "einvoice_not_recorded": 2, "recorded_without_einvoice": 2,
    "einvoice_amount_mismatch": 2, "einvoice_duplicate": 2, "bank_unreconciled": 2,
    "account_unreconciled": 2, "transfer_without_approval": 2, "forecast_over_approved": 2,
    "variance_over_threshold": 2, "budget_version_mismatch": 2, "spend_without_budget_line": 2,
    "project_budget_mismatch": 3, "committed_near_approved": 3, "close_task_overdue": 2,
    "close_task_done_without_evidence": 2, "audit_request_unanswered": 2, "reconciling_item_aged": 3,
    "reconciliation_stale": 3, "forecast_stale": 3,
}
N.SEVERIDAD.update(SEVERIDAD)


# ================================================================ Clara · el cuadre

def cuadre(cfg: dict, periodo: str) -> dict:
    docs = cfg["_docs"]
    cont = docs / periodo / "10-contabilidad"
    cols = cfg.get("columns") or {}
    out = {"periodo": periodo, "alertas": [], "no_procesado": [], "cuentas": []}
    tb_f = buscar(cont, "balance")
    my_f = buscar(cont, "libro")
    if not tb_f:
        out["no_procesado"].append({"archivo": f"{periodo}/10-contabilidad/", "motivo": "no está el balance de comprobación"})
        return out
    tb = Tabla(tb_f[0], ["cuenta", "debito", "credito"], ["nombre", "saldo_inicial", "saldo_final"], cols.get("trial_balance"))
    if tb.faltan:
        out["no_procesado"].append({"archivo": rel(tb.ruta, docs), "motivo": f"faltan las columnas {', '.join(tb.faltan)}"})
        return out
    plan = {}
    pf = buscar(docs / "00-referencia", "plan")
    if pf:
        pc = Tabla(pf[0], ["cuenta", "naturaleza"], ["nombre"], cols.get("chart"))
        for f in pc.filas:
            plan[str(f["cuenta"]).strip()] = (str(f.get("naturaleza") or "").strip().upper()[:1])
    td = tc = 0.0
    saldos = {}
    for f in tb.filas:
        cta = str(f["cuenta"]).strip()
        d, c = numero(f["debito"]) or 0.0, numero(f["credito"]) or 0.0
        td, tc = td + d, tc + c
        si, sf = numero(f.get("saldo_inicial")), numero(f.get("saldo_final"))
        fila = {"cuenta": cta, "nombre": f.get("nombre"), "debito": d, "credito": c,
                "saldo_inicial": si, "saldo_final": sf, "cita": tb.cita(f, docs)}
        if si is not None and sf is not None:
            fila["descuadre_saldo"] = redondo(si + d - c - sf)
        nat = plan.get(cta) or next((plan[k] for k in sorted(plan, key=len, reverse=True) if cta.startswith(k)), None)
        if nat and sf is not None and ((nat == "D" and sf < -0.005) or (nat == "C" and sf > 0.005)):
            fila["contraria_a_naturaleza"] = nat
        saldos[cta] = fila
        out["cuentas"].append(fila)
    out["total_debitos"], out["total_creditos"] = redondo(td), redondo(tc)
    out["diferencia"] = redondo(td - tc)
    tol = tolerancias(cfg)[0]
    if abs(td - tc) > tol:
        out["alertas"].append(alerta("trial_balance_unbalanced",
                                     f"débitos {mon(td)} y créditos {mon(tc)}: diferencia {mon(td - tc)}",
                                     {"archivo": rel(tb.ruta, docs)}, td - tc, clave="balance"))
    for fila in out["cuentas"]:
        if abs(fila.get("descuadre_saldo") or 0) > tol:
            out["alertas"].append(alerta(
                "ledger_vs_trial_balance",
                f"cuenta {fila['cuenta']}: saldo inicial más movimientos no da el saldo final ({mon(fila['descuadre_saldo'])})",
                fila["cita"], fila["descuadre_saldo"], clave=f"saldo:{fila['cuenta']}"))
    if my_f:
        my = Tabla(my_f[0], ["cuenta", "debito", "credito"], ["fecha", "tercero", "documento", "comprobante", "centro_costo", "descripcion"], cols.get("ledger"))
        if my.faltan:
            out["no_procesado"].append({"archivo": rel(my.ruta, docs), "motivo": f"faltan las columnas {', '.join(my.faltan)}"})
        else:
            mov = {}
            for f in my.filas:
                cta = str(f["cuenta"]).strip()
                d, c = numero(f["debito"]) or 0.0, numero(f["credito"]) or 0.0
                m = mov.setdefault(cta, [0.0, 0.0])
                m[0] += d
                m[1] += c
            # El mayor trae subcuentas; el balance puede traer la cuenta o la subcuenta. Se
            # compara cada cuenta del balance con la suma del mayor de lo que empieza por ella,
            # solo en las cuentas hoja del balance, para no contar dos veces.
            hojas = [k for k in saldos if not any(o != k and o.startswith(k) for o in saldos)]
            for cta in hojas:
                d = sum(v[0] for k, v in mov.items() if k.startswith(cta))
                c = sum(v[1] for k, v in mov.items() if k.startswith(cta))
                f = saldos[cta]
                dif_d, dif_c = d - f["debito"], c - f["credito"]
                if abs(dif_d) > tol or abs(dif_c) > tol:
                    out["alertas"].append(alerta(
                        "ledger_vs_trial_balance",
                        f"cuenta {cta}: el mayor suma débitos {mon(d)} y créditos {mon(c)}; el balance dice {mon(f['debito'])} y {mon(f['credito'])}",
                        [f["cita"], {"archivo": rel(my.ruta, docs)}], dif_d - dif_c, clave=f"mayor:{cta}"))
            sin_tb = sorted(k for k in mov if not any(k.startswith(h) for h in saldos))
            for k in sin_tb:
                out["alertas"].append(alerta("ledger_vs_trial_balance",
                                             f"cuenta {k}: tiene movimientos en el mayor y no está en el balance",
                                             {"archivo": rel(my.ruta, docs)}, mov[k][0] - mov[k][1], clave=f"mayor:{k}"))
    else:
        out["no_procesado"].append({"archivo": f"{periodo}/10-contabilidad/", "motivo": "no está el libro mayor"})
    out["contrarias"] = [f for f in out["cuentas"] if f.get("contraria_a_naturaleza")]
    return out


def saldos_balance(cfg: dict, periodo: str) -> dict:
    tb_f = buscar(cfg["_docs"] / periodo / "10-contabilidad", "balance")
    if not tb_f:
        return {}
    tb = Tabla(tb_f[0], ["cuenta", "debito", "credito"], ["saldo_inicial", "saldo_final", "nombre"],
               (cfg.get("columns") or {}).get("trial_balance"))
    return {str(f["cuenta"]).strip(): (numero(f.get("saldo_final")), tb.cita(f, cfg["_docs"]), f.get("nombre")) for f in tb.filas}


def mayor(cfg: dict, periodo: str) -> Tabla | None:
    my_f = buscar(cfg["_docs"] / periodo / "10-contabilidad", "libro")
    if not my_f:
        return None
    t = Tabla(my_f[0], ["cuenta", "debito", "credito"],
              ["fecha", "tercero", "documento", "comprobante", "centro_costo", "descripcion"],
              (cfg.get("columns") or {}).get("ledger"))
    return None if t.faltan else t


# ================================================================ Clara · bancos

def _movimientos(t: Tabla) -> list[dict]:
    out = []
    for f in t.filas:
        v = numero(f.get("valor"))
        if v is None and ("debito" in f or "credito" in f):
            v = (numero(f.get("credito")) or 0.0) - (numero(f.get("debito")) or 0.0)
        out.append({"fecha": fecha(f.get("fecha")), "valor": v or 0.0, "referencia": (f.get("referencia") or f.get("documento") or "").strip(),
                    "descripcion": f.get("descripcion"), "saldo": numero(f.get("saldo_final")), "_fila": f["_fila"]})
    return out


def _cruzar(banco: list[dict], libros: list[dict], ventana: int) -> tuple[list, list, list]:
    """Tres pasadas: referencia y valor; valor y fecha dentro de la ventana; valor solo, si es único."""
    pares, lb, ll = [], list(banco), list(libros)

    def quitar(b, l, como):
        pares.append((b, l, como))
        lb.remove(b)
        ll.remove(l)
    for b in list(lb):
        if b["referencia"]:
            l = next((x for x in ll if x["referencia"] and ident(x["referencia"]) == ident(b["referencia"])
                      and abs(x["valor"] - b["valor"]) < 0.005), None)
            if l:
                quitar(b, l, "referencia")
    for b in list(lb):
        cand = [x for x in ll if abs(x["valor"] - b["valor"]) < 0.005 and b["fecha"] and x["fecha"]
                and abs((x["fecha"] - b["fecha"]).days) <= ventana]
        if cand:
            quitar(b, min(cand, key=lambda x: abs((x["fecha"] - b["fecha"]).days)), "valor y fecha")
    for b in list(lb):
        cand = [x for x in ll if abs(x["valor"] - b["valor"]) < 0.005]
        if len(cand) == 1 and len([y for y in lb if abs(y["valor"] - b["valor"]) < 0.005]) == 1:
            quitar(b, cand[0], "valor")
    return pares, lb, ll


def bancos(cfg: dict, periodo: str) -> dict:
    docs = cfg["_docs"]
    carpeta = docs / periodo / "20-bancos"
    corte = fin_de_mes(periodo)
    ventana = umbral(cfg, "bank_match_window_days")
    dias_max = umbral(cfg, "reconciling_item_days")
    tol = tolerancias(cfg)[0]
    cols = cfg.get("columns") or {}
    out = {"periodo": periodo, "corte": iso(corte), "cuentas": [], "alertas": [], "no_procesado": []}
    esperadas = set((cfg.get("bank_accounts") or []))
    vistas = set()
    for sub in sorted(p for p in carpeta.iterdir() if p.is_dir()) if carpeta.is_dir() else []:
        vistas.add(sub.name)
        ex, au = buscar(sub, "extracto"), buscar(sub, "auxiliar")
        if not ex or not au:
            falta = "el extracto" if not ex else "el auxiliar de libros"
            out["alertas"].append(alerta("reconciliation_stale", f"{sub.name}: falta {falta} del periodo",
                                         {"archivo": rel(sub, docs) + "/"}, clave=f"banco:{sub.name}"))
            continue
        te = Tabla(ex[0], ["fecha", "valor"], ["referencia", "descripcion", "saldo_final", "documento", "debito", "credito"], cols.get("bank_statement"))
        if te.faltan and "valor" in te.faltan:
            te = Tabla(ex[0], ["fecha", "debito", "credito"], ["referencia", "descripcion", "saldo_final", "documento"], cols.get("bank_statement"))
        ta = Tabla(au[0], ["fecha", "valor"], ["referencia", "documento", "descripcion", "saldo_final", "debito", "credito"], cols.get("bank_book"))
        if ta.faltan and "valor" in ta.faltan:
            ta = Tabla(au[0], ["fecha", "debito", "credito"], ["referencia", "documento", "descripcion", "saldo_final"], cols.get("bank_book"))
        malas = [(t, t.faltan) for t in (te, ta) if t.faltan]
        if malas:
            for t, f in malas:
                out["no_procesado"].append({"archivo": rel(t.ruta, docs), "motivo": f"faltan las columnas {', '.join(f)}"})
            continue
        mb, ml = _movimientos(te), _movimientos(ta)
        ultima = max((m["fecha"] for m in mb if m["fecha"]), default=None)
        if ultima and ultima < inicio_de_mes(periodo):
            out["alertas"].append(alerta("reconciliation_stale",
                                         f"{sub.name}: el extracto llega hasta {ultima}, antes del periodo",
                                         {"archivo": rel(te.ruta, docs)}, clave=f"banco:{sub.name}"))
        sb = next((m["saldo"] for m in sorted(mb, key=lambda m: (m["fecha"] or dt.date.min, m["_fila"]), reverse=True) if m["saldo"] is not None), None)
        sl = next((m["saldo"] for m in sorted(ml, key=lambda m: (m["fecha"] or dt.date.min, m["_fila"]), reverse=True) if m["saldo"] is not None), None)
        if sb is None:
            sb = sum(m["valor"] for m in mb)
        if sl is None:
            sl = sum(m["valor"] for m in ml)
        pares, solo_b, solo_l = _cruzar(mb, ml, ventana)
        transito = [m for m in solo_l if m["valor"] > 0]
        cheques = [m for m in solo_l if m["valor"] < 0]
        nc = [m for m in solo_b if m["valor"] > 0]
        nd = [m for m in solo_b if m["valor"] < 0]
        ajustado_banco = sb + sum(m["valor"] for m in transito) + sum(m["valor"] for m in cheques)
        ajustado_libros = sl + sum(m["valor"] for m in nc) + sum(m["valor"] for m in nd)
        dif = ajustado_banco - ajustado_libros
        abiertas = []
        for m, origen, t in [(m, "libros", ta) for m in solo_l] + [(m, "banco", te) for m in solo_b]:
            dias = (corte - m["fecha"]).days if m["fecha"] else None
            clase = ("consignación en tránsito" if m["valor"] > 0 else "cheque pendiente de cobro") if origen == "libros" else \
                    ("nota crédito sin registrar" if m["valor"] > 0 else "nota débito sin registrar")
            abiertas.append({"fecha": iso(m["fecha"]), "valor": redondo(m["valor"]), "referencia": m["referencia"],
                             "descripcion": m["descripcion"], "clase": clase, "dias": dias,
                             "tramo": None if dias is None else "0-30" if dias <= 30 else "31-60" if dias <= 60 else "61-90" if dias <= 90 else "más de 90",
                             "cita": {"archivo": rel(t.ruta, docs), "fila": m["_fila"]}})
        c = {"cuenta": sub.name, "saldo_banco": redondo(sb), "consignaciones_transito": redondo(sum(m["valor"] for m in transito)),
             "cheques_pendientes": redondo(sum(m["valor"] for m in cheques)), "notas_credito_sin_registrar": redondo(sum(m["valor"] for m in nc)),
             "notas_debito_sin_registrar": redondo(sum(m["valor"] for m in nd)), "saldo_libros": redondo(sl),
             "diferencia_sin_explicar": redondo(dif), "cruzadas": len(pares), "abiertas": abiertas,
             "por_como": {k: sum(1 for p in pares if p[2] == k) for k in ("referencia", "valor y fecha", "valor")}}
        out["cuentas"].append(c)
        for a in abiertas:
            out["alertas"].append(alerta("bank_unreconciled", f"{sub.name}: {a['clase']} del {a['fecha']} por {mon(a['valor'])} ({a['referencia'] or 'sin referencia'})",
                                         a["cita"], a["valor"], dias=a["dias"], clave=f"{sub.name}:{a['cita']['archivo']}:{a['cita']['fila']}"))
            if a["dias"] is not None and a["dias"] > dias_max:
                out["alertas"].append(alerta("reconciling_item_aged", f"{sub.name}: {a['clase']} lleva {a['dias']} días ({a['referencia'] or a['fecha']})",
                                             a["cita"], a["valor"], dias=a["dias"], clave=f"{sub.name}:{a['cita']['archivo']}:{a['cita']['fila']}"))
        if abs(dif) > tol:
            out["alertas"].append(alerta("bank_unreconciled", f"{sub.name}: queda una diferencia sin explicar de {mon(dif)}",
                                         {"archivo": rel(sub, docs) + "/"}, dif, clave=f"{sub.name}:diferencia"))
    for falta in sorted(esperadas - vistas):
        out["alertas"].append(alerta("reconciliation_stale", f"{falta}: no hay carpeta de la cuenta en el periodo",
                                     {"archivo": f"{periodo}/20-bancos/"}, clave=f"banco:{falta}"))
    return out


# ================================================================ Clara · cuentas contra auxiliares

def cuentas(cfg: dict, periodo: str) -> dict:
    docs = cfg["_docs"]
    carpeta = docs / periodo / "10-contabilidad" / "auxiliares"
    corte = fin_de_mes(periodo)
    tol = tolerancias(cfg)[0]
    saldos = saldos_balance(cfg, periodo)
    out = {"periodo": periodo, "cuentas": [], "alertas": [], "no_procesado": []}
    conciliar = [str(x) for x in ((cfg.get("accounts") or {}).get("reconcile") or [])]
    vistas = set()
    for f in sorted(p for p in carpeta.iterdir() if p.is_file() and p.suffix.lower() in TABLAS) if carpeta.is_dir() else []:
        cta = re.match(r"[0-9]+", f.stem)
        if not cta:
            out["no_procesado"].append({"archivo": rel(f, docs), "motivo": "el nombre no empieza por el número de la cuenta"})
            continue
        cta = cta.group(0)
        vistas.add(cta)
        t = Tabla(f, ["valor"], ["fecha", "tercero", "documento", "descripcion", "saldo_final"], (cfg.get("columns") or {}).get("subledger"))
        if t.faltan:
            out["no_procesado"].append({"archivo": rel(f, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
            continue
        partidas = []
        for x in t.filas:
            d = fecha(x.get("fecha"))
            dias = (corte - d).days if d else None
            partidas.append({"tercero": x.get("tercero"), "documento": x.get("documento"), "fecha": iso(d),
                             "valor": numero(x["valor"]) or 0.0, "dias": dias,
                             "tramo": None if dias is None else "0-30" if dias <= 30 else "31-60" if dias <= 60 else "61-90" if dias <= 90 else "más de 90",
                             "cita": t.cita(x, docs)})
        aux = sum(p["valor"] for p in partidas)
        sm = saldos.get(cta)
        mayor_v = sm[0] if sm else None
        c = {"cuenta": cta, "nombre": sm[2] if sm else None, "saldo_mayor": redondo(mayor_v), "saldo_auxiliar": redondo(aux),
             "diferencia": redondo((mayor_v or 0) - aux) if mayor_v is not None else None, "partidas": len(partidas),
             "por_tramo": {k: redondo(sum(p["valor"] for p in partidas if p["tramo"] == k)) for k in ("0-30", "31-60", "61-90", "más de 90")},
             "cita": [sm[1] if sm else None, {"archivo": rel(f, docs)}]}
        out["cuentas"].append(c)
        if mayor_v is None:
            out["no_procesado"].append({"archivo": rel(f, docs), "motivo": f"la cuenta {cta} no está en el balance del periodo"})
        elif abs(mayor_v - aux) > tol:
            out["alertas"].append(alerta("account_unreconciled",
                                         f"cuenta {cta}: el mayor dice {mon(mayor_v)} y el auxiliar suma {mon(aux)}",
                                         c["cita"], mayor_v - aux, clave=f"cuenta:{cta}"))
    for cta in sorted(set(conciliar) - vistas):
        out["alertas"].append(alerta("reconciliation_stale", f"cuenta {cta}: no hay auxiliar del periodo para conciliarla",
                                     {"archivo": f"{periodo}/10-contabilidad/auxiliares/"}, clave=f"cuenta:{cta}"))
    return out


# ================================================================ Clara · facturas contra contabilidad

def _empieza(cta: str, prefijos) -> bool:
    return any(str(cta).startswith(str(p)) for p in prefijos or [])


def facturas(cfg: dict, periodo: str) -> dict:
    docs = cfg["_docs"]
    carpeta = docs / periodo / "30-facturacion"
    tol, tol_iva = tolerancias(cfg)
    ac = cfg.get("accounts") or {}
    out = {"periodo": periodo, "facturas": 0, "alertas": [], "no_procesado": [], "solo_identidad": [],
           "sin_documento": [], "cruzadas": 0, "fuentes": sorted({"F-01" if ((cfg.get('entity') or {}).get('country') or 'CO').upper() == 'CO' else "F-04"})}
    leidas = []
    for lado in ("emitidas", "recibidas"):
        for p in sorted((carpeta / lado).rglob("*.xml")) if (carpeta / lado).is_dir() else []:
            d = leer_factura(p)
            if "error" in d:
                out["no_procesado"].append({"archivo": rel(p, docs), "motivo": d["error"]})
                continue
            if d.get("pais") == "EC" and not d["clave"]["valida"]:
                out["no_procesado"].append({"archivo": rel(p, docs), "motivo": "; ".join(d["clave"]["motivos"])})
                continue
            d["lado"], d["archivo"] = lado, rel(p, docs)
            leidas.append(d)
    out["facturas"] = len(leidas)
    por_id = {}
    for d in leidas:
        por_id.setdefault(d.get("id") or d["archivo"], []).append(d)
    for k, v in por_id.items():
        if len(v) > 1:
            out["alertas"].append(alerta("einvoice_duplicate", f"el mismo {'CUFE' if v[0]['pais'] == 'CO' else 'número de clave de acceso'} aparece en {len(v)} archivos ({v[0]['numero']})",
                                         [{"archivo": x["archivo"]} for x in v], v[0].get("total"), clave=f"xml:{k}"))
    my = mayor(cfg, periodo)
    if my is None:
        out["no_procesado"].append({"archivo": f"{periodo}/10-contabilidad/", "motivo": "sin libro mayor no se cruzan las facturas"})
        return out
    # Los registros: por documento y tercero, la base en las cuentas de ventas o de compras y el
    # impuesto en las del IVA, con el asiento de cada línea para ver si se registró dos veces.
    reg = {}
    for f in my.filas:
        cta = str(f["cuenta"]).strip()
        d, c = numero(f["debito"]) or 0.0, numero(f["credito"]) or 0.0
        if _empieza(cta, ac.get("sales")):
            lado, campo, v = "emitidas", "base", c - d
        elif _empieza(cta, ac.get("purchases")):
            lado, campo, v = "recibidas", "base", d - c
        elif _empieza(cta, ac.get("vat_generated")) and not _empieza(cta, ac.get("vat_deductible")):
            lado, campo, v = "emitidas", "iva", c - d
        elif _empieza(cta, ac.get("vat_deductible")) and not _empieza(cta, ac.get("vat_generated")):
            lado, campo, v = "recibidas", "iva", d - c
        elif _empieza(cta, ac.get("vat_generated")):            # la misma cuenta para los dos
            lado, campo, v = ("emitidas", "iva", c - d) if c >= d else ("recibidas", "iva", d - c)
        else:
            continue
        doc = ident(f.get("documento"))
        if not doc:
            if campo == "base":
                out["sin_documento"].append({"cuenta": cta, "valor": redondo(v), "cita": my.cita(f, docs)})
            continue
        r = reg.setdefault((lado, doc), {"base": 0.0, "iva": 0.0, "terceros": set(), "asientos": set(), "citas": [],
                                         "documento": str(f.get("documento")).strip()})
        r[campo] += v
        if f.get("tercero"):
            r["terceros"].add(nit_sin_dv(f["tercero"]))
        if f.get("comprobante") and campo == "base":
            r["asientos"].add(str(f["comprobante"]).strip())
        r["citas"].append(my.cita(f, docs))
    vistos = set()
    for d in leidas:
        if d["tipo"] not in ("factura", "nota de crédito", "liquidación de compra") or (d["pais"] == "EC" and not d.get("valores")):
            out["solo_identidad"].append({"archivo": d["archivo"], "tipo": d["tipo"], "numero": d["numero"]})
            continue
        clave = (d["lado"], ident(d["numero"]))
        r = reg.get(clave)
        tercero = d["receptor"] if d["lado"] == "emitidas" else d["emisor"]
        if r is None:
            out["alertas"].append(alerta("einvoice_not_recorded", f"{d['tipo']} {d['lado'][:-2]}a {d['numero']} del {d['fecha']} por {mon(d.get('total') or 0)} sin registro contable",
                                         {"archivo": d["archivo"]}, d.get("total"), clave=f"xml:{d['archivo']}"))
            continue
        vistos.add(clave)
        out["cruzadas"] += 1
        signo = -1 if d["tipo"] == "nota de crédito" else 1
        db, di = r["base"] - signo * (d["base"] or 0), r["iva"] - signo * (d["iva"] or 0)
        if abs(db) > tol or abs(di) > tol_iva:
            partes = []
            if abs(db) > tol:
                partes.append(f"base {mon(signo * (d['base'] or 0))} en el XML y {mon(r['base'])} en libros")
            if abs(di) > tol_iva:
                partes.append(f"IVA {mon(signo * (d['iva'] or 0))} en el XML y {mon(r['iva'])} en libros")
            out["alertas"].append(alerta("einvoice_amount_mismatch", f"{d['tipo']} {d['numero']}: " + "; ".join(partes),
                                         [{"archivo": d["archivo"]}] + r["citas"][:3], db + di, clave=f"xml:{d['archivo']}"))
        if tercero and r["terceros"] and tercero not in r["terceros"]:
            out["no_procesado"].append({"archivo": d["archivo"], "motivo": f"el tercero del registro ({', '.join(sorted(r['terceros']))}) no es el del XML ({tercero}): cruzado por número, para revisar"})
        if len(r["asientos"]) > 1:
            out["alertas"].append(alerta("einvoice_duplicate", f"{d['tipo']} {d['numero']} registrada en {len(r['asientos'])} asientos ({', '.join(sorted(r['asientos']))})",
                                         r["citas"][:4], r["base"], clave=f"reg:{d['lado']}:{ident(d['numero'])}"))
    for (lado, doc), r in sorted(reg.items()):
        if (lado, doc) in vistos or abs(r["base"]) < 0.005:
            continue
        out["alertas"].append(alerta("recorded_without_einvoice", f"documento {r['documento']} en las cuentas de {'ventas' if lado == 'emitidas' else 'compras'} por {mon(r['base'])} sin factura electrónica en {lado}/",
                                     r["citas"][:3], r["base"], clave=f"reg:{lado}:{doc}"))
    return out


# ================================================================ Clara · el checklist y el estado del cierre

def _limite(v: str, periodo: str, feriados: set) -> dt.date | None:
    s = str(v or "").strip().upper().replace(" ", "")
    m = re.fullmatch(r"D\+?(\d+)", s)
    if m:
        return dia_habil(fin_de_mes(periodo), int(m[1]), feriados)
    return fecha(v)


def checklist(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    docs = cfg["_docs"]
    feriados = set(cfg.get("holidays") or [])
    out = {"periodo": periodo, "hoy": iso(hoy), "tareas": [], "alertas": [], "no_procesado": [],
           "aprobado": bool((cfg.get("checklist") or {}).get("approved"))}
    cf = buscar(docs / "00-referencia", "checklist")
    cc = cfg.get("checklist") or {}
    industria = norm(cc.get("industry"))
    if not cf and cc.get("source") == "recomendado" and RECOMENDADO.is_file():
        # El recomendado es un borrador del plugin, no un documento de la organización: se
        # filtra por industria en el estado, y el reporte dice que no está aprobado.
        filas = [f for f in csv_filas(RECOMENDADO)]
        cab, cuerpo = filas[0], [f for f in filas[1:] if f and norm(f[0]) in ("todas", industria)]
        cf = [cfg["_estado"] / "cierre" / periodo / "checklist-recomendado.csv"]
        _csv(cf[0], [cab[1:]] + [f[1:] for f in cuerpo])
        out["recomendado"] = True
    if not cf:
        out["no_procesado"].append({"archivo": "00-referencia/", "motivo": "no está el checklist del cierre"})
        return out
    t = Tabla(cf[0], ["id", "tarea", "responsable", "dia_limite"], ["area", "depende_de", "evidencia_esperada", "criticidad", "estado"],
              (cfg.get("columns") or {}).get("checklist"))
    if t.faltan:
        out["no_procesado"].append({"archivo": rel(cf[0], docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
        return out
    soportes = docs / periodo / "40-soportes"
    archivos = sorted(p for p in soportes.rglob("*") if p.is_file() and not p.name.startswith(".")) if soportes.is_dir() else []
    tareas = {}
    for f in t.filas:
        tid = str(f["id"]).strip()
        ev = [rel(p, docs) for p in archivos if norm(p.name).startswith(norm(tid) + "_") or norm(p.stem) == norm(tid)]
        declarada = norm(f.get("estado")) in ("cumplida", "cumplido", "hecho", "hecha", "completada", "completado", "cerrada", "ok", "done")
        tareas[tid] = {"id": tid, "tarea": f["tarea"], "area": f.get("area"), "responsable": f["responsable"],
                       "limite": iso(_limite(f["dia_limite"], periodo, feriados)), "criticidad": norm(f.get("criticidad")) or "media",
                       "depende_de": [x.strip() for x in re.split(r"[,;\s]+", str(f.get("depende_de") or "")) if x.strip()],
                       "evidencia_esperada": f.get("evidencia_esperada"), "declarada_cumplida": declarada,
                       "evidencia": ev, "cita": t.cita(f, docs)}
    peso = {"alta": 3, "media": 2, "baja": 1}
    for x in tareas.values():
        lim = fecha(x["limite"])
        if x["evidencia"]:
            x["estado"] = "cumplida con evidencia"
        elif x["declarada_cumplida"]:
            x["estado"] = "cumplida sin evidencia"
        elif lim and lim < hoy:
            x["estado"] = "vencida"
        else:
            x["estado"] = "en plazo"
        pend = [d for d in x["depende_de"] if d in tareas and not tareas[d]["evidencia"]]
        if x["estado"] in ("en plazo", "vencida") and pend:
            x["bloqueada_por"] = pend
            if x["estado"] == "en plazo":
                x["estado"] = "bloqueada por otra"
    total = sum(peso.get(x["criticidad"], 2) for x in tareas.values())
    hecho = sum(peso.get(x["criticidad"], 2) for x in tareas.values() if x["evidencia"])
    out["avance_con_evidencia_pct"] = redondo(100 * hecho / total) if total else None
    out["avance_declarado_pct"] = redondo(100 * sum(peso.get(x["criticidad"], 2) for x in tareas.values() if x["evidencia"] or x["declarada_cumplida"]) / total) if total else None
    # La ruta crítica: la cadena más larga de tareas sin evidencia, siguiendo sus dependencias.
    memo = {}

    def cadena(tid, vistos=()):
        if tid in memo:
            return memo[tid]
        x = tareas[tid]
        previas = [cadena(d, vistos + (tid,)) for d in x["depende_de"] if d in tareas and d not in vistos and not tareas[d]["evidencia"]]
        memo[tid] = max(previas, key=len, default=[]) + [tid]
        return memo[tid]
    pendientes = [k for k, x in tareas.items() if not x["evidencia"]]
    out["ruta_critica"] = max((cadena(k) for k in pendientes), key=len, default=[])
    orden = {"vencida": 0, "cumplida sin evidencia": 1, "bloqueada por otra": 2, "en plazo": 3, "cumplida con evidencia": 4}
    out["tareas"] = sorted(tareas.values(), key=lambda x: (CRITICIDAD.get(x["criticidad"], 2), orden[x["estado"]], x["limite"] or "9999", x["id"]))
    for x in out["tareas"]:
        dias = (hoy - fecha(x["limite"])).days if x["limite"] else None
        if x["estado"] == "vencida" or (x["estado"] == "bloqueada por otra" and dias and dias > 0):
            out["alertas"].append(alerta("close_task_overdue", f"{x['id']} · {x['tarea']}: venció el {x['limite']} y no tiene evidencia",
                                         x["cita"], responsable=x["responsable"], dias=dias, severidad=CRITICIDAD.get(x["criticidad"], 2), clave=f"tarea:{x['id']}"))
        if x["estado"] == "cumplida sin evidencia":
            out["alertas"].append(alerta("close_task_done_without_evidence", f"{x['id']} · {x['tarea']}: figura cumplida y no hay soporte en {periodo}/40-soportes/ que empiece por {x['id']}",
                                         x["cita"], responsable=x["responsable"], severidad=CRITICIDAD.get(x["criticidad"], 2), clave=f"tarea:{x['id']}"))
    return out


# ================================================================ Clara · el paquete del auditor

def auditoria(cfg: dict, periodo: str, hoy: dt.date, ficha: dict) -> dict:
    """Cada requerimiento contra su respuesta y su soporte. El índice llega en una tabla del
    auditor (`requerimientos/`), y lo que llegó en Word, PDF o correo lo extrae el agente a la ficha."""
    docs = cfg["_docs"]
    base = docs / periodo / "50-auditoria"
    out = {"periodo": periodo, "requerimientos": [], "alertas": [], "no_procesado": []}
    reqs = {}
    for f in buscar(base / "requerimientos", ""):
        t = Tabla(f, ["id", "solicitud"], ["fecha", "dia_limite", "responsable", "estado"], (cfg.get("columns") or {}).get("audit"))
        if t.faltan:
            out["no_procesado"].append({"archivo": rel(f, docs), "motivo": f"faltan las columnas {', '.join(t.faltan)}"})
            continue
        for x in t.filas:
            rid = str(x["id"]).strip()
            reqs[rid] = {"id": rid, "solicitud": x["solicitud"], "fecha": iso(fecha(x.get("fecha"))), "limite": iso(fecha(x.get("dia_limite"))),
                         "responsable": x.get("responsable"), "declarado": norm(x.get("estado")), "cita": t.cita(x, docs)}
    for r in (ficha.get("audit_requests") or []):
        rid = str(r.get("id") or "").strip()
        if rid and rid not in reqs:
            reqs[rid] = {"id": rid, "solicitud": r.get("request"), "fecha": r.get("date"), "limite": r.get("due"),
                         "responsable": r.get("owner"), "declarado": norm(r.get("status")), "cita": {"archivo": r.get("source")}}
    resp = base / "respuestas"
    archivos = sorted(p for p in resp.rglob("*") if p.is_file() and not p.name.startswith(".")) if resp.is_dir() else []
    for rid, r in sorted(reqs.items()):
        r["respuesta"] = [rel(p, docs) for p in archivos if norm(p.name).startswith(norm(rid) + "_") or norm(p.stem) == norm(rid)]
        lim = fecha(r["limite"])
        if r["respuesta"]:
            r["estado"] = "respondido con soporte"
        elif r["declarado"] in ("respondido", "respondida", "entregado", "entregada", "cerrado", "cerrada"):
            r["estado"] = "respondido sin soporte"
        elif lim and lim < hoy:
            r["estado"] = "vencido"
        else:
            r["estado"] = "sin responder"
        out["requerimientos"].append(r)
        if r["estado"] != "respondido con soporte":
            dias = (hoy - lim).days if lim else None
            vencido = lim is not None and lim < hoy
            if r["estado"] == "respondido sin soporte" or vencido:
                out["alertas"].append(alerta("audit_request_unanswered", f"{rid} · {r['solicitud']}: {r['estado']}" + (f", venció el {r['limite']}" if vencido else ""),
                                             r["cita"], responsable=r["responsable"], dias=dias, clave=f"req:{rid}"))
    return out


# ================================================================ Clara · todo el periodo

def clara(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _PAIS[0] = ((cfg.get("entity") or {}).get("country") or "CO").upper()
    estado = cfg["_estado"] / "cierre" / periodo
    ficha = leer_json(estado / "ficha.json", {}) or {}
    problemas = revisar_ficha_cierre(ficha)
    partes = {
        "ledger-check": cuadre(cfg, periodo), "bank-reconcile": bancos(cfg, periodo),
        "account-reconcile": cuentas(cfg, periodo), "einvoice-check": facturas(cfg, periodo),
        "close-status": checklist(cfg, periodo, hoy), "audit-pack": auditoria(cfg, periodo, hoy, ficha),
    }
    alertas = [a for p in partes.values() for a in p["alertas"]]
    dec = (ficha.get("declared") or {})
    if norm(dec.get("status")) in ("cerrado", "cerrada", "closed"):
        abiertas = [a for a in alertas]
        if abiertas:
            alertas.append(alerta("declared_close_vs_evidence",
                                  f"el cierre se reporta cerrado ({dec.get('source')}, {dec.get('date')}) y hay {len(abiertas)} señales abiertas que ese estado no explica",
                                  {"archivo": dec.get("source")}, clave="cierre"))
    partes["close-status"]["declarado"] = dec or None
    return {"agente": "clara", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(fin_de_mes(periodo)),
            "hoy": iso(hoy), "partes": partes, "alertas": ordenar(alertas), "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence_clara(partes, periodo)}


def vence_clara(partes: dict, periodo: str) -> list[dict]:
    """Lo del cierre que tiene fecha y no está cumplido con su evidencia, para la vista de lo
    que vence de Rostrum: la tarea y el requerimiento del auditor, con su estado (ADR 0010)."""
    out = [{"fecha": x["limite"], "que": f"{x['id']} · {x['tarea']}", "caso": periodo, "estado": x["estado"],
            "responsable": x.get("responsable"), "comando": "close-status"}
           for x in partes["close-status"].get("tareas", []) if x.get("limite") and x.get("estado") != "cumplida con evidencia"]
    out += [{"fecha": x["limite"], "que": f"{x['id']} · {x.get('solicitud')}", "caso": periodo, "estado": x.get("estado"),
             "responsable": x.get("responsable"), "comando": "audit-pack"}
            for x in partes["audit-pack"].get("requerimientos", []) if x.get("limite") and x.get("estado") != "respondido con soporte"]
    return sorted(out, key=lambda v: (v["fecha"], v["que"]))


def revisar_ficha_cierre(f: dict) -> list[str]:
    p = []
    d = f.get("declared")
    if d is not None:
        if not isinstance(d, dict) or not d.get("status"):
            p.append("declared: lleva status, source y date, o no va")
        elif not d.get("source"):
            p.append("declared.status sin source: una declaración se cita")
    for i, r in enumerate(f.get("audit_requests") or []):
        if not r.get("id") or not r.get("source"):
            p.append(f"audit_requests[{i}]: cada requerimiento lleva id y source")
    for i, q in enumerate(f.get("questions") or []):
        if not q.get("question") or "answer" not in q:
            p.append(f"questions[{i}]: lleva question y answer")
    return p


# ================================================================ Tomás · el presupuesto

def _version(p: Path) -> tuple[int, str | None]:
    m = re.search(r"v(\d+)", p.stem, re.I)
    f = re.search(r"(\d{4}-\d{2}-\d{2})", p.stem)
    return (int(m[1]) if m else 0, f[1] if f else None)


def versiones(cfg: dict, anio: str) -> list[dict]:
    docs = cfg["_docs"]
    out = []
    for p in buscar(docs / f"presupuesto-{anio}" / "10-aprobado", ""):
        t = Tabla(p, ["area", "linea"], ["cuenta", "total", "centro_costo"], (cfg.get("columns") or {}).get("budget"), meses=True)
        if t.faltan:
            out.append({"archivo": rel(p, docs), "error": f"faltan las columnas {', '.join(t.faltan)}"})
            continue
        lineas = {}
        for f in t.filas:
            k = (str(f["area"]).strip(), str(f["linea"]).strip())
            meses = {m: (v or 0.0) for m, v in (f.get("_meses") or {}).items()}
            total = numero(f.get("total"))
            if total is None:
                total = sum(meses.values())
            l = lineas.setdefault(k, {"area": k[0], "linea": k[1], "total": 0.0, "meses": {m: 0.0 for m in range(1, 13)}, "citas": []})
            l["total"] += total
            for m, v in meses.items():
                l["meses"][m] += v
            l["citas"].append(t.cita(f, docs))
        n, fch = _version(p)
        out.append({"archivo": rel(p, docs), "version": n, "fecha": fch, "lineas": lineas, "con_meses": bool(t.meses)})
    return sorted(out, key=lambda v: (v.get("version", 0), v.get("fecha") or ""))


def vigente(vs: list[dict], ficha: dict, cfg: dict) -> dict | None:
    """La versión vigente: la más reciente, salvo que la configuración fije otra. Que cada cambio
    respecto de la anterior tenga su acta lo dice `traslados`, no esta elección."""
    buenas = [v for v in vs if "error" not in v]
    fija = (cfg.get("budget") or {}).get("approved_version")
    if fija is not None:
        return next((v for v in buenas if v["version"] == int(fija)), None)
    return buenas[-1] if buenas else None


def mapeo(cfg: dict) -> list[dict]:
    docs = cfg["_docs"]
    f = buscar(docs / "00-referencia", "mapeo")
    if not f:
        return []
    t = Tabla(f[0], ["cuenta", "area", "linea"], ["centro_costo"], (cfg.get("columns") or {}).get("budget_map"))
    return [{"cuenta": str(x["cuenta"]).strip(), "centro_costo": str(x.get("centro_costo") or "").strip(),
             "area": str(x["area"]).strip(), "linea": str(x["linea"]).strip()} for x in t.filas] if not t.faltan else []


def _a_linea(cta: str, cc: str, mp: list[dict]):
    cand = [m for m in mp if cta.startswith(m["cuenta"]) and (not m["centro_costo"] or m["centro_costo"] == cc)]
    if not cand:
        return None
    m = max(cand, key=lambda m: (len(m["cuenta"]), bool(m["centro_costo"])))
    return (m["area"], m["linea"])


def ejecucion(cfg: dict, anio: str, corte: str) -> dict:
    """Lo ejecutado por línea y mes, desde la contabilidad de cada periodo del año hasta el corte."""
    docs = cfg["_docs"]
    mp = mapeo(cfg)
    gasto = [str(x) for x in ((cfg.get("budget") or {}).get("expense_prefixes") or ["5", "6", "7"])]
    out = {"lineas": {}, "sin_linea": [], "periodos": [], "no_procesado": []}
    if not mp:
        out["no_procesado"].append({"archivo": "00-referencia/", "motivo": "no está el mapeo de cuentas a líneas presupuestales"})
    for p in sorted(x for x in docs.iterdir() if x.is_dir() and re.fullmatch(rf"{anio}-\d{{2}}", x.name)):
        if p.name > corte:
            continue
        my = mayor(cfg, p.name)
        if my is None:
            continue
        out["periodos"].append(p.name)
        mes = int(p.name[-2:])
        for f in my.filas:
            cta = str(f["cuenta"]).strip()
            if not _empieza(cta, gasto):
                continue
            v = (numero(f["debito"]) or 0.0) - (numero(f["credito"]) or 0.0)
            k = _a_linea(cta, str(f.get("centro_costo") or "").strip(), mp)
            if k is None:
                out["sin_linea"].append({"periodo": p.name, "cuenta": cta, "centro_costo": f.get("centro_costo"), "valor": redondo(v), "cita": my.cita(f, docs)})
                continue
            l = out["lineas"].setdefault(k, {"meses": {}, "citas": []})
            l["meses"][mes] = l["meses"].get(mes, 0.0) + v
            if len(l["citas"]) < 3:
                l["citas"].append(my.cita(f, docs))
    return out


def compromisos(cfg: dict, anio: str) -> dict:
    docs = cfg["_docs"]
    fs = buscar(docs / f"presupuesto-{anio}" / "20-compromisos", "")
    if not fs:
        return {"archivo": None, "lineas": {}, "fecha": None}
    p = sorted(fs, key=lambda x: _version(x)[1] or "")[-1]
    t = Tabla(p, ["area", "linea", "saldo"], ["numero", "fecha", "proveedor", "valor"], (cfg.get("columns") or {}).get("commitments"))
    out = {"archivo": rel(p, docs), "fecha": _version(p)[1], "lineas": {}, "error": None}
    if t.faltan:
        out["error"] = f"faltan las columnas {', '.join(t.faltan)}"
        return out
    for f in t.filas:
        k = (str(f["area"]).strip(), str(f["linea"]).strip())
        out["lineas"][k] = out["lineas"].get(k, 0.0) + (numero(f["saldo"]) or 0.0)
    return out


def proyecciones(cfg: dict, anio: str) -> list[dict]:
    docs = cfg["_docs"]
    out = []
    for p in buscar(docs / f"presupuesto-{anio}" / "30-proyecciones", ""):
        t = Tabla(p, ["area", "linea", "proyeccion"], ["version"], (cfg.get("columns") or {}).get("forecast"))
        if t.faltan:
            out.append({"archivo": rel(p, docs), "error": f"faltan las columnas {', '.join(t.faltan)}"})
            continue
        out.append({"archivo": rel(p, docs), "fecha": _version(p)[1],
                    "filas": [{"area": str(f["area"]).strip(), "linea": str(f["linea"]).strip(), "proyeccion": numero(f["proyeccion"]),
                               "version": (str(f.get("version") or "").strip() or None), "cita": t.cita(f, docs)} for f in t.filas]})
    return out


def traslados(vs: list[dict], ficha: dict) -> dict:
    """Cada cambio entre dos versiones, contra el acta que lo aprueba."""
    buenas = [v for v in vs if "error" not in v]
    actas = [a for a in (ficha.get("minutes") or []) if a.get("type") in ("traslado", "adicion", "reduccion", "transfer", "addition", "reduction")]
    usados = set()
    out = {"cambios": [], "alertas": [], "actas_sin_cambio": []}
    for ant, nue in zip(buenas, buenas[1:]):
        claves = sorted(set(ant["lineas"]) | set(nue["lineas"]))
        baja = [(k, nue["lineas"].get(k, {}).get("total", 0.0) - ant["lineas"].get(k, {}).get("total", 0.0)) for k in claves]
        baja = [(k, d) for k, d in baja if abs(d) > 0.005]
        neto = sum(d for _, d in baja)
        for k, d in baja:
            acta = None
            for i, a in enumerate(actas):
                for j, mv in enumerate(a.get("movements") or []):
                    lado = "from" if d < 0 else "to"
                    if (i, j, lado) in usados:
                        continue
                    x = mv.get(lado) or {}
                    v = numero(mv.get("amount")) or 0.0
                    if (x.get("area"), x.get("line")) == k and abs(abs(d) - v) < 0.5:
                        acta = (i, j, lado, a)
                        break
                if acta:
                    break
            cambio = {"de": nue["archivo"], "contra": ant["archivo"], "area": k[0], "linea": k[1], "valor": redondo(d),
                      "tipo": "traslado" if abs(neto) < 0.5 else ("adición" if neto > 0 else "reducción"),
                      "acta": acta[3].get("source") if acta else None, "estado": "con acta" if acta else "sin acta"}
            if acta:
                usados.add(acta[:3])
            out["cambios"].append(cambio)
            if not acta:
                out["alertas"].append(alerta("transfer_without_approval", f"{k[0]} · {k[1]}: cambió {mon(d)} entre la versión {ant['version']} y la {nue['version']} sin acta que lo apruebe",
                                             [{"archivo": nue["archivo"]}, {"archivo": ant["archivo"]}], d, clave=f"traslado:{nue['version']}:{k[0]}:{k[1]}"))
    for i, a in enumerate(actas):
        for j, mv in enumerate(a.get("movements") or []):
            # Un traslado toca dos líneas; una adición o una reducción, una sola.
            lados = [x for x in ("from", "to") if mv.get(x)]
            if any((i, j, x) not in usados for x in lados):
                out["actas_sin_cambio"].append({"acta": a.get("source"), "movimiento": mv})
    return out


def tomas(cfg: dict, anio: str, corte: str, hoy: dt.date) -> dict:
    _PAIS[0] = ((cfg.get("entity") or {}).get("country") or "CO").upper()
    estado = cfg["_estado"] / "presupuesto" / anio
    ficha = leer_json(estado / "ficha.json", {}) or {}
    problemas = revisar_ficha_presupuesto(ficha)
    alertas, no_proc = [], []
    vs = versiones(cfg, anio)
    for v in vs:
        if "error" in v:
            no_proc.append({"archivo": v["archivo"], "motivo": v["error"]})
    vig = vigente(vs, ficha, cfg)
    if vig is None:
        return {"agente": "tomas", "anio": anio, "corte": corte, "alertas": [], "no_procesado": no_proc + [{"archivo": f"presupuesto-{anio}/10-aprobado/", "motivo": "no hay un presupuesto que procesar"}],
                "record_issues": problemas, "partes": {}}
    ej = ejecucion(cfg, anio, corte)
    no_proc += ej["no_procesado"]
    co = compromisos(cfg, anio)
    if co.get("error"):
        no_proc.append({"archivo": co["archivo"], "motivo": co["error"]})
    mes_corte = int(corte[-2:])
    var_pct, com_pct = umbral(cfg, "variance_pct"), umbral(cfg, "committed_pct")
    filas = []
    for k, l in sorted(vig["lineas"].items()):
        aprob_corte = sum(v for m, v in l["meses"].items() if m <= mes_corte) if vig["con_meses"] else l["total"] * mes_corte / 12
        e = ej["lineas"].get(k, {"meses": {}, "citas": []})
        ejec = sum(e["meses"].values())
        comp = co["lineas"].get(k, 0.0)
        desv = ejec - aprob_corte
        pct = 100 * desv / aprob_corte if aprob_corte else None
        f = {"area": k[0], "linea": k[1], "aprobado": redondo(l["total"]), "aprobado_al_corte": redondo(aprob_corte), "ejecutado": redondo(ejec),
             "comprometido": redondo(comp), "disponible": redondo(l["total"] - ejec - comp), "desviacion": redondo(desv),
             "desviacion_pct": redondo(pct), "distribucion_mensual": vig["con_meses"], "cita": l["citas"][:1] + e["citas"][:2]}
        # Las dos proyecciones, cada una con su supuesto.
        meses_rest = 12 - mes_corte
        prom = ejec / mes_corte if mes_corte else 0.0
        f["proyeccion_ritmo"] = redondo(ejec + max(prom * meses_rest, comp))
        f["proyeccion_plan"] = redondo(ejec + sum(v for m, v in l["meses"].items() if m > mes_corte)) if vig["con_meses"] else redondo(ejec + l["total"] * meses_rest / 12)
        filas.append(f)
        if pct is not None and abs(pct) > var_pct:
            alertas.append(alerta("variance_over_threshold", f"{k[0]} · {k[1]}: ejecutado {mon(ejec)} contra {mon(aprob_corte)} aprobado al corte ({pc(pct, signo=True)} %)",
                                  f["cita"], desv, clave=f"var:{k[0]}:{k[1]}"))
        if l["total"] and 100 * (ejec + comp) / l["total"] >= com_pct:
            alertas.append(alerta("committed_near_approved", f"{k[0]} · {k[1]}: ejecutado más comprometido es {pc(100 * (ejec + comp) / l['total'])} % de lo aprobado en el año",
                                  f["cita"], ejec + comp - l["total"], clave=f"com:{k[0]}:{k[1]}"))
    por_linea = {(f["area"], f["linea"]): f for f in filas}
    for s in ej["sin_linea"]:
        alertas.append(alerta("spend_without_budget_line", f"cuenta {s['cuenta']}{' · centro ' + str(s['centro_costo']) if s.get('centro_costo') else ''}: {mon(s['valor'])} en {s['periodo']} sin línea presupuestal",
                              s["cita"], s["valor"], clave=f"sinlinea:{s['periodo']}:{s['cuenta']}:{s.get('centro_costo') or ''}"))
    for k in sorted(set(co["lineas"]) - set(vig["lineas"])):
        alertas.append(alerta("spend_without_budget_line", f"{k[0]} · {k[1]}: comprometido {mon(co['lineas'][k])} en una línea que el presupuesto no tiene",
                              {"archivo": co["archivo"]}, co["lineas"][k], clave=f"sinlinea:comp:{k[0]}:{k[1]}"))
    # Proyecciones de las áreas: la más reciente de cada línea.
    stale = umbral(cfg, "forecast_stale_days")
    pr = proyecciones(cfg, anio)
    ultima = {}
    for p in pr:
        if "error" in p:
            no_proc.append({"archivo": p["archivo"], "motivo": p["error"]})
            continue
        for x in p["filas"]:
            k = (x["area"], x["linea"])
            if k not in ultima or (p["fecha"] or "") > (ultima[k]["fecha"] or ""):
                ultima[k] = dict(x, fecha=p["fecha"], archivo=p["archivo"])
            if x["version"] and str(x["version"]).lower().lstrip("v") != str(vig["version"]):
                alertas.append(alerta("budget_version_mismatch", f"{p['archivo']}: {x['area']} · {x['linea']} usa la versión {x['version']} y la aprobada es la {vig['version']}",
                                      x["cita"], clave=f"version:{p['archivo']}:{x['area']}:{x['linea']}"))
    for k, x in sorted(ultima.items()):
        f = por_linea.get(k)
        if f:
            f["proyeccion_area"] = redondo(x["proyeccion"])
            f["proyeccion_area_fecha"] = x["fecha"]
        d = fecha(x["fecha"])
        if d and (hoy - d).days > stale:
            alertas.append(alerta("forecast_stale", f"{k[0]} · {k[1]}: la proyección del área es del {x['fecha']}, hace {(hoy - d).days} días",
                                  x["cita"], dias=(hoy - d).days, clave=f"stale:{k[0]}:{k[1]}"))
    for f in filas:
        base_proy = f.get("proyeccion_area") if f.get("proyeccion_area") is not None else f["proyeccion_ritmo"]
        if base_proy is not None and base_proy > (f["aprobado"] or 0) + 0.5:
            quien = "la del área" if f.get("proyeccion_area") is not None else "la calculada al ritmo (el área no entregó la suya)"
            alertas.append(alerta("forecast_over_approved", f"{f['area']} · {f['linea']}: la proyección al cierre, {quien}, es {mon(base_proy)} y lo aprobado {mon(f['aprobado'])}",
                                  f["cita"], base_proy - f["aprobado"], clave=f"proy:{f['area']}:{f['linea']}"))
    for inf in (ficha.get("reports") or []):
        v = str(inf.get("budget_version") or "").lower().lstrip("v")
        if v and v != str(vig["version"]):
            alertas.append(alerta("budget_version_mismatch", f"{inf.get('source')}: el informe usa la versión {inf.get('budget_version')} y la aprobada es la {vig['version']}",
                                  {"archivo": inf.get("source")}, clave=f"version:{inf.get('source')}"))
    # Lo que cada área declara, contra los números.
    for dcl in (ficha.get("area_statements") or []):
        if norm(dcl.get("says")) not in ("dentro", "dentro_del_presupuesto", "within", "within_budget", "en_presupuesto"):
            continue
        area = str(dcl.get("area") or "").strip()
        fs = [f for f in filas if f["area"] == area]
        fuera = [f for f in fs if (f["desviacion_pct"] or 0) > var_pct or (f.get("proyeccion_area") or f["proyeccion_ritmo"] or 0) > (f["aprobado"] or 0) + 0.5]
        if fuera:
            alertas.append(alerta("declared_vs_evidence", f"{area} se reporta dentro del presupuesto ({dcl.get('source')}) y {len(fuera)} línea(s) no lo sostienen: " + ", ".join(f["linea"] for f in fuera),
                                  {"archivo": dcl.get("source")}, sum(f["desviacion"] or 0 for f in fuera), clave=f"declara:{area}"))
    tr = traslados(vs, ficha)
    alertas += tr["alertas"]
    # Los proyectos de la familia PMO: su presupuesto contra el que tiene asignado el área.
    pmo = (cfg.get("budget") or {}).get("pmo_records")
    proyectos = []
    if pmo:
        rp = Path(pmo).expanduser()
        rp = rp if rp.is_absolute() else Path.cwd() / rp
        for r in sorted(rp.glob("*.json")) if rp.is_dir() else []:
            ficha_p = leer_json(r, {}) or {}
            code = ((ficha_p.get("identity") or {}).get("code") or {}).get("value")
            apr = numero(((ficha_p.get("money") or {}).get("approved") or {}).get("value"))
            linea = next((f for f in filas if code and ident(f["linea"]) == ident(code)), None)
            proyectos.append({"codigo": code, "ficha": str(r), "aprobado_ficha": apr, "asignado_area": linea["aprobado"] if linea else None})
            if linea and apr is not None and abs(apr - (linea["aprobado"] or 0)) > 0.5:
                alertas.append(alerta("project_budget_mismatch", f"{code}: la ficha del proyecto dice {mon(apr)} y el área tiene asignado {mon(linea['aprobado'])}",
                                      [{"archivo": r.name}] + linea["cita"][:1], apr - linea["aprobado"], clave=f"pry:{code}"))
    partes = {
        "variance-report": {"version_vigente": vig["version"], "archivo_vigente": vig["archivo"], "lineas": filas, "sin_linea": ej["sin_linea"],
                            "periodos": ej["periodos"], "compromisos": co.get("archivo"), "proyectos": proyectos},
        "forecast": {"lineas": [{k: f.get(k) for k in ("area", "linea", "aprobado", "ejecutado", "comprometido", "proyeccion_area", "proyeccion_area_fecha", "proyeccion_ritmo", "proyeccion_plan")} for f in filas],
                     "supuestos": {"ritmo": "el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido",
                                   "plan": "el ejecutado más lo que falta del aprobado según su distribución mensual"}},
        "transfer-log": tr,
        "budget-committee-pack": {"compromisos_comite": ficha.get("committee_commitments") or []},
    }
    # El presupuesto no tiene fechas que venzan en su ficha: lo que vence en el año es del cierre.
    return {"agente": "tomas", "entidad": cfg.get("entity"), "anio": anio, "corte": corte, "hoy": iso(hoy),
            "version_vigente": vig["version"], "partes": partes, "alertas": ordenar(alertas), "no_procesado": no_proc,
            "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": []}


def revisar_ficha_presupuesto(f: dict) -> list[str]:
    p = []
    for i, a in enumerate(f.get("minutes") or []):
        if not a.get("source") or not a.get("type"):
            p.append(f"minutes[{i}]: cada acta lleva type y source")
        for j, mv in enumerate(a.get("movements") or []):
            if numero(mv.get("amount")) is None:
                p.append(f"minutes[{i}].movements[{j}]: amount no es un número")
    for i, s in enumerate(f.get("area_statements") or []):
        if not s.get("area") or not s.get("source"):
            p.append(f"area_statements[{i}]: lleva area, says y source")
    for i, q in enumerate(f.get("questions") or []):
        if not q.get("question") or "answer" not in q:
            p.append(f"questions[{i}]: lleva question y answer")
    return p


# ================================================================ el reporte, en el formato común

NOMBRE = {"clara": "Clara", "tomas": "Tomás"}
SENALES_DE = {
    "ledger-check": {"trial_balance_unbalanced", "ledger_vs_trial_balance"},
    "bank-reconcile": {"bank_unreconciled", "reconciling_item_aged", "reconciliation_stale"},
    "account-reconcile": {"account_unreconciled", "reconciliation_stale"},
    "einvoice-check": {"einvoice_not_recorded", "recorded_without_einvoice", "einvoice_amount_mismatch", "einvoice_duplicate"},
    "close-status": {"close_task_overdue", "close_task_done_without_evidence", "declared_close_vs_evidence"},
    "audit-pack": {"audit_request_unanswered"},
    "variance-report": {"variance_over_threshold", "committed_near_approved", "spend_without_budget_line", "declared_vs_evidence", "project_budget_mismatch"},
    "forecast": {"forecast_over_approved", "forecast_stale", "budget_version_mismatch"},
    "transfer-log": {"transfer_without_approval"},
}




def reporte(r: dict, comando: str, version: str) -> str:
    """El reporte en el orden común (`nucleo.reporte`), con el resultado propio de cada comando."""
    ent = r.get("entidad") or {}
    alcance = f"periodo {r['periodo']}" if r.get("periodo") else f"presupuesto {r.get('anio')}, corte {r.get('corte')}"
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")),
                         senales=SENALES_DE.get(comando), alcance=alcance, cuerpo=_cuerpo,
                         extra=f" · **Aprueba:** {ent.get('approver')}" if ent.get("approver") else "",
                         familia="criterio-cfo")


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if comando == "ledger-check" and p:
        l += [f"Débitos {_m(p.get('total_debitos'))} · créditos {_m(p.get('total_creditos'))} · diferencia {_m(p.get('diferencia'))}.", ""]
        if p.get("contrarias"):
            l += ["| Cuenta | Nombre | Saldo final | Naturaleza |", "|---|---|---|---|"]
            l += [f"| {c['cuenta']} | {c.get('nombre') or ''} | {_m(c['saldo_final'])} | {'débito' if c['contraria_a_naturaleza'] == 'D' else 'crédito'} |" for c in p["contrarias"]]
            l.append("")
    elif comando == "bank-reconcile" and p:
        l += ["| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |",
              "|---|---|---|---|---|---|---|---|"]
        l += [f"| {c['cuenta']} | {_m(c['saldo_banco'])} | {_m(c['consignaciones_transito'])} | {_m(c['cheques_pendientes'])} | {_m(c['notas_credito_sin_registrar'])} | {_m(c['notas_debito_sin_registrar'])} | {_m(c['saldo_libros'])} | {_m(c['diferencia_sin_explicar'])} |" for c in p["cuentas"]]
        l.append("")
        for c in p["cuentas"]:
            if c["abiertas"]:
                l += [f"**{c['cuenta']} · partidas abiertas por antigüedad**", "", "| Fecha | Clase | Referencia | Valor | Días | Tramo |", "|---|---|---|---|---|---|"]
                l += [f"| {a['fecha']} | {a['clase']} | {a['referencia'] or '—'} | {_m(a['valor'])} | {a['dias']} | {a['tramo']} |" for a in sorted(c["abiertas"], key=lambda a: -(a["dias"] or 0))]
                l.append("")
    elif comando == "account-reconcile" and p:
        l += ["| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |", "|---|---|---|---|---|---|---|---|---|"]
        l += [f"| {c['cuenta']} | {c.get('nombre') or ''} | {_m(c['saldo_mayor'])} | {_m(c['saldo_auxiliar'])} | {_m(c['diferencia'])} | " + " | ".join(_m(c["por_tramo"][k]) for k in ("0-30", "31-60", "61-90", "más de 90")) + " |" for c in p["cuentas"]]
        l.append("")
    elif comando == "einvoice-check" and p:
        l += [f"{p['facturas']} facturas y notas electrónicas procesadas · {p['cruzadas']} cruzadas con su registro · {len(p['solo_identidad'])} identificadas solo por la clave de acceso · {len(p['sin_documento'])} líneas de ventas o compras sin número de documento.", "",
              "Sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona.", ""]
    elif comando == "close-status" and p:
        dec = p.get("declarado") or {}
        l += [f"**Estado declarado:** {dec.get('status') or 'nadie lo ha declarado'}" + (f" ({_cita({'archivo': dec.get('source')})}, {dec.get('date')})" if dec.get("source") else "") +
              f" · **Avance con evidencia:** {_m(p.get('avance_con_evidencia_pct'))} % · **Avance declarado:** {_m(p.get('avance_declarado_pct'))} % (ponderados por criticidad)", ""]
        if not p.get("aprobado"):
            l += ["El checklist no está aprobado: el estado se calcula, y una persona tiene que aprobarlo antes de darlo por bueno.", ""]
        l += ["| Id | Tarea | Responsable | Vence | Criticidad | Estado | Evidencia |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['id']} | {x['tarea']} | {x['responsable']} | {x['limite'] or '—'} | {x['criticidad']} | {x['estado']}{' (' + ', '.join(x['bloqueada_por']) + ')' if x.get('bloqueada_por') else ''} | {', '.join('`' + e + '`' for e in x['evidencia']) or '—'} |" for x in p["tareas"]]
        l += ["", f"**Ruta crítica del cierre:** {' → '.join(p['ruta_critica']) or 'no queda nada pendiente'}", ""]
    elif comando == "audit-pack" and p:
        l += ["| Requerimiento | Solicitud | Responsable | Vence | Estado | Respuesta |", "|---|---|---|---|---|---|"]
        l += [f"| {x['id']} | {x['solicitud']} | {x['responsable'] or '—'} | {x['limite'] or '—'} | {x['estado']} | {', '.join('`' + e + '`' for e in x['respuesta']) or '—'} |" for x in p["requerimientos"]]
        l += ["", "El índice no mueve ni copia archivos: cita dónde está cada uno.", ""]
    elif comando == "variance-report" and p:
        l += [f"Versión vigente: **{p['version_vigente']}** (`{p['archivo_vigente']}`) · periodos procesados: {', '.join(p['periodos']) or 'ninguno'}", "",
              "| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |", "|---|---|---|---|---|---|---|---|---|"]
        l += [f"| {f['area']} | {f['linea']} | {_m(f['aprobado'])} | {_m(f['aprobado_al_corte'])} | {_m(f['ejecutado'])} | {_m(f['comprometido'])} | {_m(f['disponible'])} | {_m(f['desviacion'])} | {_m(f['desviacion_pct'])} |"
              for f in sorted(p["lineas"], key=lambda f: -abs(f["desviacion_pct"] or 0))]
        l.append("")
    elif comando == "forecast" and p:
        l += ["| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |", "|---|---|---|---|---|---|"]
        l += [f"| {f['area']} | {f['linea']} | {_m(f['aprobado'])} | {_m(f.get('proyeccion_area'))}{' (' + f['proyeccion_area_fecha'] + ')' if f.get('proyeccion_area_fecha') else ''} | {_m(f['proyeccion_ritmo'])} | {_m(f['proyeccion_plan'])} |" for f in p["lineas"]]
        l += ["", f"**Al ritmo:** {p['supuestos']['ritmo']}. **Al plan:** {p['supuestos']['plan']}.", ""]
    elif comando == "transfer-log" and p:
        l += ["| Versión | Área | Línea | Valor | Tipo | Acta | Estado |", "|---|---|---|---|---|---|---|"]
        l += [f"| `{c['de']}` | {c['area']} | {c['linea']} | {_m(c['valor'])} | {c['tipo']} | {('`' + c['acta'] + '`') if c['acta'] else '—'} | {c['estado']} |" for c in p["cambios"]]
        if p["actas_sin_cambio"]:
            l += ["", "**Actas sin cambio aplicado:** " + "; ".join(f"`{x['acta']}`" for x in p["actas_sin_cambio"])]
        l.append("")
    elif comando == "budget-committee-pack" and p:
        l += ["Los puntos de decisión son las señales de arriba. Cada una lleva su cifra y su cita; quién decide lo dice el acta del comité.", ""]
        if p["compromisos_comite"]:
            l += ["| Compromiso del comité anterior | Responsable | Estado | Evidencia |", "|---|---|---|---|"]
            l += [f"| {c.get('what')} | {c.get('owner') or '—'} | {c.get('status') or '—'} | {c.get('evidence') or '—'} |" for c in p["compromisos_comite"]]
            l.append("")
    return l


# ================================================================ cuándo toca qué



def despertar(cfg: dict, rol: str, hoy: dt.date) -> dict:
    estado = cfg["_estado"]
    corr = registro_corridas(estado)
    ultima = lambda que: max((fecha(c["fecha"]) for c in corr if c["comando"] == que), default=None)  # noqa: E731
    toca, motivo = [], []
    if rol == "clara":
        periodo = cfg.get("period")
        fin = fin_de_mes(periodo) if periodo else None
        ventana = dia_habil(fin, umbral(cfg, "close_window_business_days"), set(cfg.get("holidays") or [])) if fin else None
        u = ultima("close-scan")
        if fin and fin < hoy <= ventana:
            if u != hoy:
                toca, motivo = ["close-scan", "close-status"], [f"estamos en la ventana del cierre de {periodo}, hasta el {ventana}: corre a diario"]
        elif not u or (hoy - u).days >= 7:
            toca, motivo = ["close-scan"], ["fuera de la ventana del cierre corre una vez por semana"]
    else:
        b = cfg.get("budget") or {}
        anio = str(b.get("year"))
        hechos = {c.get("caso") for c in corr if c["comando"] == "budget-scan"}
        periodos = sorted(x.name for x in cfg["_docs"].iterdir() if x.is_dir() and re.fullmatch(rf"{anio}-\d{{2}}", x.name)
                          and buscar(x / "10-contabilidad", "libro")) if cfg["_docs"].is_dir() else []
        nuevos = [p for p in periodos if p not in hechos]
        if nuevos:
            toca += ["budget-scan", "variance-report", "forecast"]
            motivo.append(f"hay contabilidad nueva: {', '.join(nuevos)}")
        for c in b.get("committee_dates") or []:
            d = fecha(c)
            if d and 0 <= (d - hoy).days <= 5 and (ultima("budget-committee-pack") or dt.date.min) < hoy - dt.timedelta(days=5):
                toca.append("budget-committee-pack")
                motivo.append(f"el comité es el {d}")
        u = ultima("budget-scan")
        if not toca and (not u or (hoy - u).days >= 7):
            toca, motivo = ["budget-scan"], ["una vez por semana, por los compromisos"]
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}




# ================================================================ la línea de comandos



def _rol() -> str:
    return "tomas" if N.plugin(AQUI)["name"] == "criterio-budget" else "clara"


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    if rol == "clara":
        periodo = a.period or cfg.get("period")
        if not periodo:
            raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
        r = clara(cfg, periodo, hoy)
        destino = cfg["_estado"] / "cierre" / periodo / "resultados.json"
    else:
        anio = str(a.year or (cfg.get("budget") or {}).get("year"))
        corte = a.period or (cfg.get("budget") or {}).get("cut") or f"{anio}-{hoy.month:02d}"
        r = tomas(cfg, anio, corte, hoy)
        destino = cfg["_estado"] / "presupuesto" / anio / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Clara y Tomás.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir",
                                       "compute", "reporte", "factura", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action == "factura":
        print(json.dumps(leer_factura(a.file), ensure_ascii=False, indent=2))
        return 0
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=("cierre", "presupuesto"),
                       revisar_config=revisar_config, calcular=calcular, reporte=reporte, despertar=despertar)


# ================================================================ la prueba del motor



def factura_dian(numero_: str, cufe: str, fecha_: str, emisor: str, receptor: str, base: float, iva: float, nota_de: str | None = None) -> str:
    raiz = "CreditNote" if nota_de else "Invoice"
    ref = (f"<cac:BillingReference><cac:InvoiceDocumentReference><cbc:ID>{nota_de}</cbc:ID><cbc:UUID schemeName=\"CUFE-SHA384\">x</cbc:UUID>"
           f"</cac:InvoiceDocumentReference></cac:BillingReference>") if nota_de else ""
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<{raiz} xmlns="urn:oasis:names:specification:ubl:schema:xsd:{raiz}-2" '
            'xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" '
            'xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">'
            f'<cbc:ID>{numero_}</cbc:ID><cbc:UUID schemeName="{"CUDE" if nota_de else "CUFE"}-SHA384">{cufe}</cbc:UUID><cbc:IssueDate>{fecha_}</cbc:IssueDate>{ref}'
            f'<cac:AccountingSupplierParty><cac:Party><cac:PartyTaxScheme><cbc:CompanyID schemeID="1" schemeName="31">{emisor}</cbc:CompanyID></cac:PartyTaxScheme></cac:Party></cac:AccountingSupplierParty>'
            f'<cac:AccountingCustomerParty><cac:Party><cac:PartyTaxScheme><cbc:CompanyID schemeName="31">{receptor}</cbc:CompanyID></cac:PartyTaxScheme></cac:Party></cac:AccountingCustomerParty>'
            f'<cac:TaxTotal><cbc:TaxAmount currencyID="COP">{iva:.2f}</cbc:TaxAmount><cac:TaxSubtotal><cbc:TaxableAmount currencyID="COP">{base:.2f}</cbc:TaxableAmount>'
            f'<cbc:TaxAmount currencyID="COP">{iva:.2f}</cbc:TaxAmount><cac:TaxCategory><cbc:Percent>19.00</cbc:Percent><cac:TaxScheme><cbc:ID>01</cbc:ID><cbc:Name>IVA</cbc:Name></cac:TaxScheme></cac:TaxCategory></cac:TaxSubtotal></cac:TaxTotal>'
            f'<cac:LegalMonetaryTotal><cbc:LineExtensionAmount currencyID="COP">{base:.2f}</cbc:LineExtensionAmount><cbc:TaxExclusiveAmount currencyID="COP">{base:.2f}</cbc:TaxExclusiveAmount>'
            f'<cbc:TaxInclusiveAmount currencyID="COP">{base + iva:.2f}</cbc:TaxInclusiveAmount><cbc:PayableAmount currencyID="COP">{base + iva:.2f}</cbc:PayableAmount></cac:LegalMonetaryTotal></{raiz}>')


def contenedor_dian(interno: str) -> str:
    interno = interno.split("?>", 1)[1] if interno.startswith("<?xml") else interno
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<AttachedDocument xmlns="urn:oasis:names:specification:ubl:schema:xsd:AttachedDocument-2" '
            'xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" '
            'xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">'
            f'<cac:Attachment><cac:ExternalReference><cbc:MimeCode>text/xml</cbc:MimeCode><cbc:Description><![CDATA[{interno}]]></cbc:Description>'
            '</cac:ExternalReference></cac:Attachment></AttachedDocument>')


def clave_sri(fecha_: dt.date, tipo: str, ruc: str, serie: str, secuencial: str, codigo: str = "12345678", ambiente: str = "2") -> str:
    c = f"{fecha_:%d%m%Y}{tipo}{ruc}{ambiente}{serie}{secuencial}{codigo}1"
    return c + str(digito_mod11(c))


def factura_sri(fecha_: dt.date, ruc: str, estab: str, pto: str, sec: str, comprador: str, base: float, iva: float, autorizada: bool = True, tipo: str = "01") -> str:
    clave = clave_sri(fecha_, tipo, ruc, estab + pto, sec)
    raiz = {"01": "factura", "04": "notaCredito"}.get(tipo, "comprobante")
    info = (f"<infoFactura><fechaEmision>{fecha_:%d/%m/%Y}</fechaEmision><identificacionComprador>{comprador}</identificacionComprador>"
            f"<totalSinImpuestos>{base:.2f}</totalSinImpuestos><totalDescuento>0.00</totalDescuento><totalConImpuestos><totalImpuesto><codigo>2</codigo>"
            f"<codigoPorcentaje>4</codigoPorcentaje><baseImponible>{base:.2f}</baseImponible><valor>{iva:.2f}</valor></totalImpuesto></totalConImpuestos></infoFactura>") if tipo == "01" else ""
    comp = (f'<{raiz} id="comprobante" version="1.1.0"><infoTributaria><ambiente>2</ambiente><tipoEmision>1</tipoEmision><razonSocial>Proveedor</razonSocial>'
            f"<ruc>{ruc}</ruc><claveAcceso>{clave}</claveAcceso><codDoc>{tipo}</codDoc><estab>{estab}</estab><ptoEmi>{pto}</ptoEmi><secuencial>{sec}</secuencial>"
            f"</infoTributaria>{info}</{raiz}>")
    if not autorizada:
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + comp
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<autorizacion><estado>AUTORIZADO</estado>'
            f"<numeroAutorizacion>{clave}</numeroAutorizacion><fechaAutorizacion>{fecha_.isoformat()}T10:00:00</fechaAutorizacion><ambiente>PRODUCCIÓN</ambiente>"
            f"<comprobante><![CDATA[{comp}]]></comprobante></autorizacion>")


def selftest() -> int:
    fallas = []

    def ok(nombre, obtenido, esperado):
        if obtenido == esperado:
            print(f"  ok  {nombre}")
        else:
            fallas.append(nombre)
            print(f"  FALLA  {nombre}: {obtenido!r} en lugar de {esperado!r}")

    ok("número con coma decimal", numero("1.234.567,89"), 1234567.89)
    ok("número con punto decimal", numero("1,234,567.89"), 1234567.89)
    ok("número entre paréntesis", numero("(1.500,00)"), -1500.0)
    ok("miles con punto", numero("1.500.000"), 1500000.0)
    ok("fecha dd/mm/aaaa", fecha("21/10/2012"), dt.date(2012, 10, 21))
    ok("fecha serie de Excel", fecha("45930"), dt.date(2025, 9, 30))
    ok("D+3 en días hábiles", _limite("D+3", "2026-09", set()), dt.date(2026, 10, 5))
    # El ejemplo de la ficha técnica del SRI (F-09): la clave 2110201101179214673900110020010000000011234567813
    ok("módulo 11 del ejemplo del SRI", digito_mod11("211020110117921467390011002001000000001123456781"), 3)
    ca = clave_acceso("2110201101179214673900110020010000000011234567813")
    ok("la clave del ejemplo es válida", (ca["valida"], ca["tipo"], ca["ruc"], ca["serie"]), (True, "01", "1792146739001", "002001"))
    ok("una clave con un dígito cambiado no", clave_acceso("2110201101179214673900110020010000000011234567814")["valida"], False)

    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        x = t / "a.xml"
        x.write_text(contenedor_dian(factura_dian("SETP990000001", "a" * 96, "2026-09-10", "900123456", "800765432-1", 1000000, 190000)), encoding="utf-8")
        f = leer_factura(x)
        ok("DIAN en su contenedor", (f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["esquema"]),
           ("SETP990000001", "900123456", "800765432", 1000000.0, 190000.0, "CUFE-SHA384"))
        x.write_text(factura_dian("NC-1", "b" * 96, "2026-09-12", "900123456", "800765432", 100000, 19000, nota_de="SETP990000001"), encoding="utf-8")
        f = leer_factura(x)
        ok("DIAN nota crédito con su referencia", (f["tipo"], f["referencia"]["numero"]), ("nota de crédito", "SETP990000001"))
        x.write_text(factura_sri(dt.date(2026, 9, 15), "1792146739001", "001", "002", "000000123", "0990000000001", 500.0, 75.0), encoding="utf-8")
        f = leer_factura(x)
        ok("SRI autorizada", (f["numero"], f["base"], f["iva"], f["clave"]["valida"], f["fecha"]), ("001-002-000000123", 500.0, 75.0, True, "2026-09-15"))
        x.write_text("<x/>", encoding="utf-8")
        ok("un XML que no es factura", "error" in leer_factura(x), True)
        y = t / "b.xlsx"
        _xlsx(y, [["cuenta", "nombre", "debito"], ["1105", "", 10], ["1110", "Bancos", 5]])
        ok("xlsx con celda vacía en su columna", xlsx_filas(y)[1], ["1105", "", "10"])

        # Una entidad mínima: cuadra salvo lo sembrado.
        docs, est = t / "finanzas" / "e1", t / "estado" / "e1"
        p = docs / "2026-09"
        _csv(docs / "00-referencia" / "plan-de-cuentas.csv", [["cuenta", "nombre", "naturaleza"], ["1", "Activo", "D"], ["2", "Pasivo", "C"], ["4", "Ingresos", "C"], ["5", "Gastos", "D"], ["1305", "Clientes", "D"]])
        _csv(docs / "00-referencia" / "checklist-cierre.csv", [["id", "tarea", "area", "responsable", "dia_limite", "depende_de", "evidencia_esperada", "criticidad", "estado"],
                                                               ["C-01", "Conciliar bancos", "Tesorería", "Ana", "D+2", "", "conciliación firmada", "alta", "cumplida"],
                                                               ["C-02", "Cuadrar cartera", "Contabilidad", "Luis", "D+3", "C-01", "auxiliar", "media", ""],
                                                               ["C-03", "Revisar IVA", "Impuestos", "Eva", "D+9", "", "papel de trabajo", "media", "cumplida"]])
        _csv(p / "40-soportes" / "C-03-iva.csv", [["x"], ["1"]])
        _csv(p / "10-contabilidad" / "balance-comprobacion.csv", [["cuenta", "nombre", "saldo_inicial", "debito", "credito", "saldo_final"],
                                                                  ["1110", "Bancos", "1000", "1190000", "50", "1190950"], ["1305", "Clientes", "0", "0", "0", "0"],
                                                                  ["240801", "IVA", "0", "0", "190000", "-190000"], ["4135", "Ventas", "0", "0", "1000000", "-1000000"],
                                                                  ["5305", "Gastos bancarios", "0", "50", "0", "50"]])
        _csv(p / "10-contabilidad" / "libro-mayor.csv", [["fecha", "comprobante", "cuenta", "tercero", "documento", "debito", "credito", "centro_costo"],
                                                         ["2026-09-10", "V-1", "1110", "800765432", "SETP990000001", "1190000", "0", ""],
                                                         ["2026-09-10", "V-1", "4135", "800765432", "SETP990000001", "0", "1000000", ""],
                                                         ["2026-09-10", "V-1", "240801", "800765432", "SETP990000001", "0", "190000", ""],
                                                         ["2026-09-30", "B-1", "5305", "", "", "50", "0", "ADM"],
                                                         ["2026-09-30", "B-1", "1110", "", "", "0", "50", ""]])
        (p / "30-facturacion" / "emitidas").mkdir(parents=True)
        (p / "30-facturacion" / "emitidas" / "fe1.xml").write_text(factura_dian("SETP990000001", "c" * 96, "2026-09-10", "900123456", "800765432", 1000000, 190000), encoding="utf-8")
        _csv(p / "20-bancos" / "andino-1234" / "extracto.csv", [["fecha", "referencia", "descripcion", "valor", "saldo"],
                                                                ["2026-09-12", "T-55", "Transferencia", "1190000", "1191000"],
                                                                ["2026-09-30", "", "Comisión", "-50", "1190950"],
                                                                ["2026-09-30", "", "Intereses", "12", "1190962"]])
        _csv(p / "20-bancos" / "andino-1234" / "auxiliar-libros.csv", [["fecha", "documento", "descripcion", "valor", "saldo"],
                                                                       ["2026-09-10", "SETP990000001", "Cobro", "1190000", "1191000"],
                                                                       ["2026-09-30", "B-1", "Comisión", "-50", "1190950"]])
        cfg = {"entity": {"id": "900123456", "name": "Prueba", "country": "CO", "currency": "COP"}, "period": "2026-09",
               "accounts": {"sales": ["41"], "purchases": ["14", "51", "52", "61"], "vat_generated": ["2408"], "vat_deductible": ["2408"], "reconcile": ["1305"]},
               "_docs": docs, "_estado": est}
        r = clara(cfg, "2026-09", dt.date(2026, 10, 6))
        senales = sorted({a["signal"] for a in r["alertas"]})
        ok("cuadre sin hallazgos", [a for a in r["alertas"] if a["signal"] in ("trial_balance_unbalanced", "ledger_vs_trial_balance")], [])
        ok("la factura cruza con su registro", r["partes"]["einvoice-check"]["cruzadas"], 1)
        b = r["partes"]["bank-reconcile"]["cuentas"][0]
        ok("banco: los intereses quedan como nota crédito sin registrar", (b["notas_credito_sin_registrar"], b["diferencia_sin_explicar"]), (12.0, 0.0))
        ok("checklist: C-01 cumplida sin evidencia y C-02 vencida", sorted((a["signal"], a["key"]) for a in r["alertas"] if a["signal"].startswith("close_task")),
           [("close_task_done_without_evidence", "tarea:C-01"), ("close_task_overdue", "tarea:C-02")])
        ok("cartera sin auxiliar: conciliación desactualizada", any(a["signal"] == "reconciliation_stale" and a["key"] == "cuenta:1305" for a in r["alertas"]), True)
        ok("las señales esperadas, y ninguna otra", senales, ["bank_unreconciled", "close_task_done_without_evidence", "close_task_overdue", "reconciliation_stale"])
        md = reporte(r, "bank-reconcile", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])

        # Tomás: presupuesto con dos versiones y un traslado sin acta.
        pr = docs / "presupuesto-2026"
        _csv(docs / "00-referencia" / "mapeo-presupuesto.csv", [["cuenta", "centro_costo", "area", "linea"], ["5305", "ADM", "Administración", "Gastos bancarios"]])
        cab = ["area", "linea"] + MESES
        _csv(pr / "10-aprobado" / "presupuesto-2026-v1-2026-01-15.csv", [cab, ["Administración", "Gastos bancarios"] + [10] * 12, ["Administración", "Papelería"] + [100] * 12])
        _csv(pr / "10-aprobado" / "presupuesto-2026-v2-2026-06-30.csv", [cab, ["Administración", "Gastos bancarios"] + [10] * 6 + [5] * 6, ["Administración", "Papelería"] + [100] * 6 + [105] * 6])
        cfg["budget"] = {"year": "2026"}
        rt = tomas(cfg, "2026", "2026-09", dt.date(2026, 10, 6))
        ok("traslado sin acta en las dos líneas", sorted(a["key"] for a in rt["alertas"] if a["signal"] == "transfer_without_approval"),
           ["traslado:2:Administración:Gastos bancarios", "traslado:2:Administración:Papelería"])
        ok("los dos cambios son un traslado: el total no cambia", {c["tipo"] for c in rt["partes"]["transfer-log"]["cambios"]}, {"traslado"})
        ok("ejecutado de septiembre en su línea", next(f["ejecutado"] for f in rt["partes"]["variance-report"]["lineas"] if f["linea"] == "Gastos bancarios"), 50.0)
        ficha = {"minutes": [{"type": "traslado", "source": "presupuesto-2026/40-actas/acta-03.docx",
                              "movements": [{"from": {"area": "Administración", "line": "Gastos bancarios"}, "to": {"area": "Administración", "line": "Papelería"}, "amount": 30}]}]}
        escribir_json(est / "presupuesto" / "2026" / "ficha.json", ficha)
        rt = tomas(cfg, "2026", "2026-09", dt.date(2026, 10, 6))
        ok("con el acta, el traslado queda aprobado", [a for a in rt["alertas"] if a["signal"] == "transfer_without_approval"], [])

        inv = inventario(docs, None, estructura(ESTRUCTURA))
        ok("inventario: nada fuera de la estructura en la entidad de prueba", inv["fuera_de_lugar"] if ESTRUCTURA.is_file() else [], [])

    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
