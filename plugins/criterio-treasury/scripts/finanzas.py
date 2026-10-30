#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-finance/scripts/finanzas.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
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
import hashlib
import json
import re
import shutil
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
CAMPOS_SUNAT = {
    "p5-ID": "/Invoice/cbc:ID · serie y número, F###-NNNNNNNN (p. 5 y 30)",
    "p5-UBL": "/Invoice/cbc:UBLVersionID · 2.1 (p. 5)",
    "p5-FECHA": "/Invoice/cbc:IssueDate · aaaa-mm-dd (p. 5 y 31)",
    "p5-TIPO": "/Invoice/cbc:InvoiceTypeCode · 01, factura, catálogo 01 (p. 5)",
    "p7-EMISOR": "/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID · RUC del emisor (p. 7)",
    "p8-ADQUIRENTE": "/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID · documento del adquirente (p. 8)",
    "p12-IMPUESTO": "/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount · monto del tributo (p. 12)",
    "p21-IGV": "TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID · 1000 es IGV, catálogo 05 (p. 13 y 21)",
    "p13-VALOR": "/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount · total valor de venta (p. 13)",
    "p13-TOTAL": "/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount · importe total (p. 13)",
}
CAMPOS_SAT = {
    "p3-RAIZ": "cfdi:Comprobante · espacio de nombres http://www.sat.gob.mx/cfd/4 (Anexo 20, DOF 13-01-2022, p. 3)",
    "p5-VERSION": "Comprobante/@Version · «4.0» (p. 5)",
    "p5-SERIE": "Comprobante/@Serie y @Folio · control interno del emisor, opcionales (p. 5)",
    "p5-FECHA": "Comprobante/@Fecha · AAAA-MM-DDThh:mm:ss (p. 5)",
    "p8-SUBTOTAL": "Comprobante/@SubTotal · suma de los conceptos antes de descuentos e impuestos (p. 8)",
    "p8-TIPO": "Comprobante/@TipoDeComprobante · «I» (Ingreso) o «E» (Egreso) (p. 8 y 11)",
    "p9-MONEDA": "Comprobante/@Moneda · «MXN» en moneda nacional (p. 9)",
    "p10-TOTAL": "Comprobante/@Total · subtotal menos descuentos más impuestos trasladados menos retenidos (p. 10)",
    "p15-EMISOR": "Emisor/@Rfc · 12 posiciones en persona moral, 13 en persona física (p. 15)",
    "p17-RECEPTOR": "Receptor/@Rfc · el RFC del receptor (p. 17)",
    "p37-TRASLADADOS": "Impuestos/@TotalImpuestosTrasladados (p. 37)",
    "p38-TRASLADO": "Impuestos/Traslados/Traslado · @Impuesto 002 es IVA, catálogo c_Impuesto (p. 26 y 38)",
}
CAMPOS_SII = {
    "p12-TIPO": "Encabezado/IdDoc/TipoDTE · 33 es factura electrónica (p. 12)",
    "p12-FOLIO": "Encabezado/IdDoc/Folio · folio autorizado por el SII, hasta 10 dígitos (p. 12)",
    "p12-FECHA": "Encabezado/IdDoc/FchEmis · aaaa-mm-dd (p. 12)",
    "p17-EMISOR": "Encabezado/Emisor/RUTEmisor · con guion y dígito verificador, 0 a 9 o K (p. 17)",
    "p19-RECEPTOR": "Encabezado/Receptor/RUTRecep · el RUT del cliente (p. 19)",
    "p29-NETO": "Encabezado/Totales/MntNeto · suma de los ítems afectos (p. 29)",
    "p30-TASA": "Encabezado/Totales/TasaIVA · en porcentaje (p. 30)",
    "p30-IVA": "Encabezado/Totales/IVA · monto neto por la tasa (p. 30)",
    "p32-TOTAL": "Encabezado/Totales/MntTotal · neto, exento, IVA e impuestos adicionales (p. 32)",
}
CAMPOS_WSFE = {
    "p26-CAB": "FeCAEReq/FeCabReq · PtoVta y CbteTipo: el punto de venta y el tipo de comprobante (p. 26 y 28)",
    "p26-DET": "FeCAEReq/FeDetReq/FECAEDetRequest · el detalle del comprobante (p. 26)",
    "p28-DOC": "FECAEDetRequest/DocTipo y DocNro · el documento del comprador; 80 es CUIT (p. 28 y 77)",
    "p28-NRO": "FECAEDetRequest/CbteDesde · el número del comprobante (p. 28)",
    "p28-FECHA": "FECAEDetRequest/CbteFch · la fecha del comprobante, aaaammdd (p. 28)",
    "p29-TOTAL": "FECAEDetRequest/ImpTotal · el importe total: no gravado, exento, neto gravado, IVA y tributos (p. 29)",
    "p29-NETO": "FECAEDetRequest/ImpNeto, ImpTotConc e ImpOpEx · el neto gravado, el no gravado y el exento (p. 29)",
    "p29-IVA": "FECAEDetRequest/ImpIVA · la suma de los importes del arreglo de IVA (p. 29)",
    "p30-TRIB": "FECAEDetRequest/ImpTrib · la suma de los importes del arreglo de tributos (p. 30)",
    "p37-CAE": "FECAESolicitarResponse/FeDetResp/FEDetResponse · Resultado (A aprobado, R rechazado) y CAE (p. 37 y 78)",
    "p140-TIPOS": "CbteTipo · 1, 6, 11, 51, 201, 206 y 211 son facturas; 3, 8, 13, 53, 203, 208 y 213, notas de crédito (p. 140 y 141)",
}
CAMPOS_DGIPA = {
    "p70-RAIZ": "rFE · la factura electrónica, raíz (A01, p. 70)",
    "p70-ID": "rFE/dId · el CUFE precedido del literal «FE» (A03, p. 70)",
    "p71-TIPO": "gDGen/iDoc · 01 factura de operación interna; 04 y 06, notas de crédito (B06, p. 71)",
    "p71-NUMERO": "gDGen/dNroDF y dPtoFacDF · el número del documento fiscal y su punto de facturación (B07 y B08, p. 71)",
    "p71-FECHA": "gDGen/dFechaEm · la fecha de emisión (B10, p. 71)",
    "p74-EMISOR": "gDGen/gEmis/gRucEmi/dRuc · el RUC del emisor (B3012, p. 74)",
    "p75-RECEPTOR": "gDGen/gDatRec/gRucRec/dRuc · el RUC del receptor (B4022, p. 75)",
    "p82-NETO": "gTot/dTotNeto · la suma de los precios antes de impuesto (D02, p. 82)",
    "p82-ITBMS": "gTot/dTotITBMS · el total del ITBMS (D03, p. 82)",
    "p82-ISC": "gTot/dTotISC · el total del ISC (D04, p. 82)",
    "p83-TOTAL": "gTot/dVTot · el valor total de la factura (D09, p. 83)",
}
CAMPOS_FEL = {
    "XSD-RAIZ": "GTDocumento/SAT/DTE · el documento tributario electrónico, espacio de nombres http://www.sat.gob.gt/dte/fel/0.2.0 (GT_Documento 0.2.1)",
    "XSD-TIPO": "DatosEmision/DatosGenerales/@Tipo · FACT es factura; NCRE, nota de crédito (GT_Documento 0.2.1; Reglas y validaciones 2.1, 1.2)",
    "XSD-FECHA": "DatosEmision/DatosGenerales/@FechaHoraEmision (Reglas y validaciones 2.1, 2.2.1)",
    "XSD-EMISOR": "DatosEmision/Emisor/@NITEmisor (Reglas y validaciones 2.1, 2.2.2)",
    "XSD-RECEPTOR": "DatosEmision/Receptor/@IDReceptor · el NIT o el documento del receptor (Reglas y validaciones 2.1, 2.2.4)",
    "XSD-IMPUESTO": "DatosEmision/Totales/TotalImpuestos/TotalImpuesto · @NombreCorto IVA y @TotalMontoImpuesto (Reglas y validaciones 2.1, 2.4.2)",
    "XSD-GRANTOTAL": "DatosEmision/Totales/GranTotal · el total del documento, con sus impuestos (Reglas y validaciones 2.1, 2.19.2)",
    "XSD-AUTORIZACION": "Certificacion/NumeroAutorizacion · el UUID de la autorización, con @Serie y @Numero (GT_Documento 0.2.1)",
}
CAMPOS_CR = {
    "A1-RAIZ": "FacturaElectronica · espacio de nombres https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/facturaElectronica; NotaCreditoElectronica en el suyo (Anexos y Estructuras 4.4, anexo 1)",
    "A1-CLAVE": "Clave · campo fijo de cincuenta posiciones (anexo 1, II.a)",
    "A1-CONSECUTIVO": "NumeroConsecutivo · campo fijo de veinte posiciones (anexo 1, II.a)",
    "A1-FECHA": "FechaEmision · fecha y hora RFC 3339 (anexo 1, II.a)",
    "A1-EMISOR": "Emisor/Identificacion/Numero · la cédula del emisor (anexo 1, II.a; nota 4)",
    "A1-RECEPTOR": "Receptor/Identificacion/Numero · la cédula del receptor (anexo 1, II.a; nota 4)",
    "A1-MONEDA": "ResumenFactura/CodigoTipoMoneda · CodigoMoneda y TipoCambio (anexo 1, II.c)",
    "A1-VENTANETA": "ResumenFactura/TotalVentaNeta · la venta neta (anexo 1, II.c)",
    "A1-IMPUESTO": "ResumenFactura/TotalImpuesto · el total de impuesto (anexo 1, II.c)",
    "A1-TOTAL": "ResumenFactura/TotalComprobante · el total del comprobante (anexo 1, II.c)",
}
# Honduras no publica un esquema (decisión 0024): la factura es un documento, y el agente la lleva a
# la ficha del cierre con estos campos del Acuerdo 481-2017 (F-37). El motor no procesa un XML.
CAMPOS_HN = {
    "A3-CAI": "Clave de Autorización de Impresión (CAI) · serie alfanumérica que genera la Administración Tributaria (art. 3, def. 7)",
    "A3-RANGO": "Rango autorizado · la cantidad de comprobantes autorizados (art. 3, def. 36; art. 10, num. 5)",
    "A10-LIMITE": "Fecha límite de emisión, vigente (art. 10, num. 4)",
    "A10-CORRELATIVO": "Número correlativo de dieciséis dígitos, NNN-NNN-NN-NNNNNNNN: establecimiento, punto de emisión, tipo de documento (01 = factura) y correlativo (art. 10, num. 7)",
    "A10-EMISOR": "Registro Tributario Nacional (RTN) del emisor (art. 10, num. 1, a)",
    "A11-CLIENTE": "Registro Tributario Nacional del cliente (art. 11, num. 1, b)",
    "A11-FECHA": "Fecha de emisión (art. 11, num. 1, c)",
    "A11-SUBTOTAL": "Subtotales sujetos a los impuestos, discriminados por tarifa (art. 11, num. 1, h)",
    "A11-IMPUESTO": "Impuestos discriminados por tarifa (art. 11, num. 1, i)",
    "A11-TOTAL": "Importe total de la operación (art. 11, num. 1, k)",
}
CORRELATIVO_HN = re.compile(r"^(\d{3})-(\d{3})-(\d{2})-(\d{8})$")
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
        "pais": PAIS_DEL_LECTOR["dian"], "lector": "dian", "fuente": "F-01", "tipo": "nota de crédito" if nc else "factura",
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
        "pais": PAIS_DEL_LECTOR["sri"], "lector": "sri", "fuente": "F-04", "tipo": TIPOS_SRI.get(cod or "", f"tipo {cod}"),
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


def _sunat(raiz, tipo: str) -> dict:
    """La factura UBL 2.1 de la SUNAT (F-13): serie y número en `cbc:ID`, el RUC del emisor y el
    documento del adquirente en `PartyTaxScheme/CompanyID` con el tipo de documento en @schemeID, el
    IGV con el código 1000 del catálogo 05 y el valor de venta en `LineExtensionAmount`. No trae una
    clave única como el CUFE: el comprobante se identifica por el RUC del emisor, su tipo, su serie y
    su número. La nota de crédito se identifica, pero sus valores no se cruzan: su guía no está
    verificada en esta versión. Si un emisor pone el RUC en otro elemento que la guía no dice, el
    tercero queda vacío y el cruce se hace por número; no se adivina."""
    def doc(lado):
        return _t(raiz, lado, "Party", "PartyTaxScheme", "CompanyID")
    emisor, codigo = ident(doc("AccountingSupplierParty")), _t(raiz, "InvoiceTypeCode")
    igv = otros = 0.0
    for tt in (c for c in raiz if _local(c.tag) == "TaxTotal"):
        for st in (c for c in tt if _local(c.tag) == "TaxSubtotal"):
            monto = numero(_t(st, "TaxAmount")) or 0.0
            if _t(st, "TaxCategory", "TaxScheme", "ID") == "1000":    # F-13: catálogo 05, 1000 · IGV
                igv += monto
            else:
                otros += monto
    factura = tipo == "Invoice" and codigo == "01"
    d = {
        "pais": PAIS_DEL_LECTOR["sunat"], "lector": "sunat", "fuente": "F-13",
        "tipo": "factura" if factura else "nota de crédito" if tipo == "CreditNote" else f"tipo {codigo}",
        "numero": _t(raiz, "ID"), "fecha": iso(fecha(_t(raiz, "IssueDate"))),
        "emisor": emisor, "receptor": ident(doc("AccountingCustomerParty")),
        "base": numero(_t(raiz, "LegalMonetaryTotal", "LineExtensionAmount")),
        "iva": round(igv, 2), "otros_impuestos": round(otros, 2),
        "total": numero(_t(raiz, "LegalMonetaryTotal", "PayableAmount")),
        "valores": factura,
    }
    d["id"] = f"{emisor}-{codigo or tipo}-{d['numero']}"
    return d


def _sat(raiz) -> dict:
    """El CFDI 4.0 del SAT de México (F-19): los montos y el tipo son atributos de
    `cfdi:Comprobante`; el RFC del emisor y del receptor, de `Emisor` y `Receptor`; el IVA es el
    traslado con `Impuesto` 002 en el nodo `Impuestos` del comprobante. Serie y folio son de control
    interno y opcionales: el documento se identifica por el RFC del emisor, la serie y el folio, y si
    no los trae, por el emisor, la fecha y el total. El folio fiscal (UUID) del Timbre Fiscal Digital
    no se procesa en esta versión: su estándar no está verificado todavía. Solo el de ingreso (I)
    cruza valores; el de egreso (E) se identifica."""
    a = raiz.attrib
    tipo = a.get("TipoDeComprobante")
    emisor = ident((_h(raiz, "Emisor") if _h(raiz, "Emisor") is not None else raiz).attrib.get("Rfc"))
    receptor = ident((_h(raiz, "Receptor") if _h(raiz, "Receptor") is not None else raiz).attrib.get("Rfc"))
    iva = otros = 0.0
    imp = next((c for c in raiz if _local(c.tag) == "Impuestos"), None)
    for t in (x for x in (imp.iter() if imp is not None else []) if _local(x.tag) == "Traslado"):
        monto = numero(t.attrib.get("Importe")) or 0.0
        if t.attrib.get("Impuesto") == "002":                  # F-19, p. 26: c_Impuesto 002 · IVA
            iva += monto
        else:
            otros += monto
    factura = tipo == "I"
    numero_ = f"{a.get('Serie') or ''}{a.get('Folio') or ''}" or None
    d = {
        "pais": PAIS_DEL_LECTOR["sat"], "lector": "sat", "fuente": "F-19",
        "tipo": "factura" if factura else ("egreso" if tipo == "E" else f"tipo {tipo}"),
        "numero": numero_, "fecha": iso(fecha((a.get("Fecha") or "")[:10])),
        "emisor": emisor, "receptor": receptor,
        "base": numero(a.get("SubTotal")), "iva": round(iva, 2), "otros_impuestos": round(otros, 2),
        "total": numero(a.get("Total")), "valores": factura,
    }
    d["id"] = f"{emisor}-{numero_}" if numero_ else f"{emisor}-{d['fecha']}-{d['total']}"
    return d


def _sii(doc) -> dict:
    """El DTE del SII de Chile (F-16): el tipo, el folio y la fecha en `IdDoc`, el RUT del emisor con
    su dígito verificador en `Emisor/RUTEmisor`, el del cliente en `Receptor/RUTRecep` y los montos en
    `Totales`. El formato nombra las áreas del encabezado, no el elemento raíz: el lector busca el
    `Encabezado`, venga suelto, dentro de su `Documento` o en un envío. Los montos van en pesos
    enteros. No trae una clave única: el documento se identifica por el RUT del emisor, el tipo y el
    folio. Solo la factura electrónica (tipo 33) cruza valores; los demás tipos se identifican, pero
    su llenado no está verificado en esta versión."""
    enc = next((x for x in doc.iter() if _local(x.tag) == "Encabezado"), None)
    tipo = _t(enc, "IdDoc", "TipoDTE")
    emisor = ident(_t(enc, "Emisor", "RUTEmisor"))
    factura = tipo == "33"                                      # F-16, p. 12: 33 · Factura Electrónica
    d = {
        "pais": PAIS_DEL_LECTOR["sii"], "lector": "sii", "fuente": "F-16",
        "tipo": "factura" if factura else f"tipo {tipo}",
        "numero": _t(enc, "IdDoc", "Folio"), "fecha": iso(fecha(_t(enc, "IdDoc", "FchEmis"))),
        "emisor": emisor, "receptor": ident(_t(enc, "Receptor", "RUTRecep")),
        "base": numero(_t(enc, "Totales", "MntNeto")), "iva": numero(_t(enc, "Totales", "IVA")) or 0.0,
        "otros_impuestos": 0.0, "total": numero(_t(enc, "Totales", "MntTotal")), "valores": factura,
    }
    d["id"] = f"{emisor}-{tipo}-{d['numero']}"
    return d


def _nfe(inf) -> dict:
    """La NF-e de Brasil (F-21, MOC 7.0, Anexo I): `infNFe` con su `Id`, la chave de acesso precedida
    de «NFe» (A03, p. 8); el modelo, la serie, el número, la fecha y el tipo de operación en `ide`
    (B06 a B11, p. 8 y 9); el CNPJ del emitente y del destinatario (C02, p. 12; E02, p. 14); y los
    totales en `total/ICMSTot` (W02 a W16, p. 58 y 59). El ICMS forma parte del valor de la operación
    (I11, p. 18): el valor total de la nota (vNF) ya lo trae, y la base que cruza con las cuentas de
    ventas o de compras es ese valor sin el ICMS, que va aparte en las cuentas del impuesto. El PIS y
    la COFINS se leen como otros impuestos. Solo el modelo 55 de salida (tpNF 1) cruza valores; la
    autorización de la SEFAZ (el protocolo) no se procesa en esta versión."""
    ide, emit, dest = _h(inf, "ide"), _h(inf, "emit"), _h(inf, "dest")
    tot = _h(inf, "total", "ICMSTot")
    chave = (inf.attrib.get("Id") or "")[3:] if (inf.attrib.get("Id") or "").startswith("NFe") else None
    mod, tp = _t(ide, "mod"), _t(ide, "tpNF")
    vnf = numero(_t(tot, "vNF")) if tot is not None else None
    icms = (numero(_t(tot, "vICMS")) or 0.0) if tot is not None else 0.0
    otros = sum((numero(_t(tot, k)) or 0.0) for k in ("vPIS", "vCOFINS")) if tot is not None else 0.0
    factura = mod == "55" and tp == "1"                        # F-21, B06 p. 8: 55 · NF-e; B11 p. 9: 1 · saída
    numero_ = f"{_t(ide, 'serie')}-{_t(ide, 'nNF')}" if ide is not None else None
    receptor = ident(_t(dest, "CNPJ") or _t(dest, "CPF")) if dest is not None else None
    d = {
        "pais": PAIS_DEL_LECTOR["nfe"], "lector": "nfe", "fuente": "F-21",
        "tipo": "factura" if factura else (f"modelo {mod}" if mod != "55" else "nota de entrada"),
        "numero": numero_, "fecha": iso(fecha((_t(ide, "dhEmi") or "")[:10])),
        "emisor": ident(_t(emit, "CNPJ")) if emit is not None else None, "receptor": receptor,
        "base": round(vnf - icms, 2) if vnf is not None else None, "iva": round(icms, 2),
        "otros_impuestos": round(otros, 2), "total": vnf, "valores": factura,
    }
    d["id"] = chave or f"{d['emisor']}-{numero_}"
    return d


# F-24, p. 140 y 141: los tipos de comprobante de CbteTipo que son facturas y los que son notas de crédito.
WSFE_FACTURA = {"1", "6", "11", "51", "201", "206", "211"}
WSFE_CREDITO = {"3", "8", "13", "53", "203", "208", "213"}


def _wsfe(raiz) -> dict:
    """El comprobante electrónico de ARCA, Argentina (F-24, manual WSFEv1, RG 4291, proyecto FE v4.8):
    la solicitud `FECAESolicitar` con su cabecera `FeCabReq` —el punto de venta y el tipo de
    comprobante— y su detalle `FECAEDetRequest` —el documento del comprador (`DocTipo`, `DocNro`), el
    número, la fecha (`CbteFch`, aaaammdd) y los importes (p. 26 a 30)—, y la respuesta con el CAE
    (p. 37). Como lo archiva el ERP: la solicitud y su respuesta en un solo archivo. El importe neto
    gravado, el no gravado y el exento forman la base; `ImpIVA` es el IVA y `ImpTrib`, los otros
    tributos (p. 29 y 30). Se identifica por su CAE; sin él, por el CUIT del emisor, el tipo, el
    punto de venta y el número. Solo una factura aprobada (`Resultado` A) cruza valores."""
    cab = next((x for x in raiz.iter() if _local(x.tag) == "FeCabReq"), None)
    det = next((x for x in raiz.iter() if _local(x.tag) == "FECAEDetRequest"), None)
    resp = next((x for x in raiz.iter() if _local(x.tag) in ("FEDetResponse", "FECAEDetResponse")), None)
    auth = next((x for x in raiz.iter() if _local(x.tag) == "Auth"), None)
    tipo = _t(cab, "CbteTipo")
    pto, nro = _t(cab, "PtoVta"), _t(det, "CbteDesde")
    numero_ = f"{int(pto):05d}-{int(nro):08d}" if pto and nro and pto.isdigit() and nro.isdigit() else None
    f = _t(det, "CbteFch") or ""
    fecha_ = f"{f[:4]}-{f[4:6]}-{f[6:8]}" if len(f) == 8 and f.isdigit() else None
    emisor = ident(_t(auth, "Cuit")) if auth is not None else None
    aprobada = resp is None or (_t(resp, "Resultado") or "A").upper() == "A"
    base = sum((numero(_t(det, k)) or 0.0) for k in ("ImpNeto", "ImpTotConc", "ImpOpEx"))
    d = {
        "pais": PAIS_DEL_LECTOR["wsfe"], "lector": "wsfe", "fuente": "F-24",
        "tipo": "factura" if tipo in WSFE_FACTURA else ("nota_credito" if tipo in WSFE_CREDITO else f"tipo {tipo}"),
        "numero": numero_, "fecha": fecha_, "emisor": emisor, "receptor": ident(_t(det, "DocNro")),
        "base": round(base, 2), "iva": numero(_t(det, "ImpIVA")) or 0.0, "otros_impuestos": numero(_t(det, "ImpTrib")) or 0.0,
        "total": numero(_t(det, "ImpTotal")), "valores": tipo in WSFE_FACTURA and aprobada,
    }
    cae = _t(resp, "CAE") if resp is not None else None
    d["id"] = cae or f"{emisor}-{tipo}-{numero_}"
    if not aprobada:
        d["error"] = f"ARCA no aprobó el comprobante: Resultado {_t(resp, 'Resultado')}"
    return d


def _dgipa(raiz) -> dict:
    """La factura electrónica de Panamá (F-27, Ficha Técnica de la Factura Electrónica para los
    Proveedores de Autorización Calificados, versión 1.00, abril de 2025): `rFE` con su `dId`, el CUFE
    precedido de «FE» (A03, p. 70); el tipo, el número, el punto de facturación y la fecha en `gDGen`
    (B06 a B10, p. 71); el RUC del emisor y del receptor (B3012, p. 74; B4022, p. 75); y los totales en
    `gTot` (D02 a D09, p. 82 y 83). El ITBMS es el impuesto al valor agregado; el ISC se lee como otro
    impuesto. Solo la factura de operación interna (iDoc 01) cruza valores en esta versión."""
    gd, tot = _h(raiz, "gDGen"), _h(raiz, "gTot")
    tipo = _t(gd, "iDoc")
    did = _t(raiz, "dId") or ""
    numero_ = f"{_t(gd, 'dPtoFacDF')}-{_t(gd, 'dNroDF')}" if gd is not None else None
    d = {
        "pais": PAIS_DEL_LECTOR["dgipa"], "lector": "dgipa", "fuente": "F-27",
        "tipo": "factura" if tipo == "01" else ("nota_credito" if tipo in ("04", "06") else f"tipo {tipo}"),
        "numero": numero_, "fecha": iso(fecha((_t(gd, "dFechaEm") or "")[:10])),
        "emisor": ident(_t(gd, "gEmis", "gRucEmi", "dRuc")), "receptor": ident(_t(gd, "gDatRec", "gRucRec", "dRuc")),
        "base": numero(_t(tot, "dTotNeto")), "iva": numero(_t(tot, "dTotITBMS")) or 0.0,
        "otros_impuestos": numero(_t(tot, "dTotISC")) or 0.0, "total": numero(_t(tot, "dVTot")), "valores": tipo == "01",
    }
    d["id"] = did[2:] if did.startswith("FE") else f"{d['emisor']}-{numero_}"
    return d


def _fel(raiz) -> dict:
    """La FEL de Guatemala (F-30, el esquema GT_Documento 0.2.1 de la SAT, y F-31, Reglas y
    validaciones 2.1): `GTDocumento/SAT/DTE` con los datos generales —el tipo, la fecha y la moneda—,
    el NIT del emisor y el documento del receptor como atributos, los totales con cada impuesto por su
    nombre corto y el gran total, y la certificación con el número de autorización, su serie y su
    número. El gran total trae los impuestos adentro: la base es el gran total sin ellos; el IVA es el
    impuesto de nombre corto IVA y los demás se leen como otros impuestos. Solo la factura (FACT)
    cruza valores en esta versión."""
    em = next((x for x in raiz.iter() if _local(x.tag) == "DatosEmision"), None)
    gen, emi, rec, tot = _h(em, "DatosGenerales"), _h(em, "Emisor"), _h(em, "Receptor"), _h(em, "Totales")
    aut = next((x for x in raiz.iter() if _local(x.tag) == "NumeroAutorizacion"), None)
    tipo = (gen.attrib.get("Tipo") if gen is not None else "") or ""
    iva = otros = 0.0
    for ti in (x for x in (tot.iter() if tot is not None else []) if _local(x.tag) == "TotalImpuesto"):
        m = numero(ti.attrib.get("TotalMontoImpuesto")) or 0.0
        if (ti.attrib.get("NombreCorto") or "").upper() == "IVA":
            iva += m
        else:
            otros += m
    total = numero(_t(tot, "GranTotal"))
    numero_ = f"{aut.attrib.get('Serie')}-{aut.attrib.get('Numero')}" if aut is not None else None
    d = {
        "pais": PAIS_DEL_LECTOR["fel"], "lector": "fel", "fuente": "F-30",
        "tipo": "factura" if tipo == "FACT" else ("nota_credito" if tipo == "NCRE" else f"tipo {tipo}"),
        "numero": numero_, "fecha": iso(fecha(((gen.attrib.get("FechaHoraEmision") if gen is not None else "") or "")[:10])),
        "emisor": ident(emi.attrib.get("NITEmisor")) if emi is not None else None,
        "receptor": ident(rec.attrib.get("IDReceptor")) if rec is not None else None,
        "base": round(total - iva - otros, 2) if total is not None else None, "iva": round(iva, 2), "otros_impuestos": round(otros, 2),
        "total": total, "valores": tipo == "FACT",
    }
    d["id"] = (aut.text or "").strip() if aut is not None and (aut.text or "").strip() else f"{d['emisor']}-{numero_}"
    return d


def _cr(raiz, nombre: str) -> dict:
    """El comprobante electrónico de Costa Rica (F-34, Anexos y Estructuras 4.4 del Ministerio de
    Hacienda): `FacturaElectronica` o `NotaCreditoElectronica`, con su clave de cincuenta posiciones,
    el consecutivo de veinte, la fecha de emisión, la cédula del emisor y la del receptor, y el
    resumen con la moneda, la venta neta, el total de impuesto y el total del comprobante. Solo la
    factura cruza valores; la nota de crédito se identifica y no cruza. La base es la venta neta y el
    impuesto, el total de impuesto (el IVA a la tarifa general del 13 %, F-35)."""
    emi, rec, res = _h(raiz, "Emisor"), _h(raiz, "Receptor"), _h(raiz, "ResumenFactura")
    num = lambda n: _t(_h(n, "Identificacion"), "Numero") if n is not None and _h(n, "Identificacion") is not None else None  # noqa: E731
    factura = nombre == "FacturaElectronica"
    d = {
        "pais": PAIS_DEL_LECTOR["cr"], "lector": "cr", "fuente": "F-34",
        "tipo": "factura" if factura else "nota de crédito",
        "numero": _t(raiz, "NumeroConsecutivo"), "fecha": iso(fecha((_t(raiz, "FechaEmision") or "")[:10])),
        "emisor": ident(num(emi)), "receptor": ident(num(rec)),
        "base": numero(_t(res, "TotalVentaNeta")), "iva": numero(_t(res, "TotalImpuesto")) or 0.0,
        "total": numero(_t(res, "TotalComprobante")), "valores": factura,
    }
    d["id"] = _t(raiz, "Clave") or f"{d['emisor']}-{d['numero']}"
    return d


def _hn(x: dict, tol_iva: float) -> dict:
    """Una factura de Honduras, desde la ficha del cierre (decisión 0024; F-37, Acuerdo 481-2017,
    artículos 10 y 11): el agente la extrae del documento, con su cita, y aquí se valida su forma.
    El número correlativo es el del artículo 10 y su tipo, 01; el ISV es el 15 % de lo gravado (F-38).
    Devuelve la factura como la de cualquier lector, con `fuera` si cae fuera de su autorización
    —fuera del rango autorizado o emitida después de la fecha límite—, o `error` si no se procesa."""
    num = str(x.get("number") or "").strip()
    m = CORRELATIVO_HN.match(num)
    if not m:
        return {"error": f"el número {num or '(vacío)'} no tiene la forma NNN-NNN-NN-NNNNNNNN del Acuerdo 481-2017, art. 10"}
    if m.group(3) != "01":
        return {"solo": True, "tipo": f"documento tipo {m.group(3)}", "numero": num}
    rango = x.get("authorized_range") or {}
    desde, hasta = CORRELATIVO_HN.match(str(rango.get("from") or "")), CORRELATIVO_HN.match(str(rango.get("to") or ""))
    if not (desde and hasta and x.get("cai") and x.get("issue_deadline")):
        return {"error": f"la factura {num} no trae su CAI, su rango autorizado y su fecha límite de emisión (art. 10)"}
    f_emi, f_lim = fecha(x.get("date")), fecha(x.get("issue_deadline"))
    base, isv, total = numero(x.get("taxable")), numero(x.get("isv")), numero(x.get("total"))
    if f_emi is None or base is None or isv is None:
        return {"error": f"la factura {num} no trae su fecha de emisión, su subtotal gravado y su ISV (art. 11)"}
    tasa = FACTURA["HN"]["iva"]
    if abs(isv - base * tasa) > tol_iva:
        return {"error": f"en la factura {num} el ISV ({mon(isv)}) no es el {tasa * 100:g} % del subtotal gravado ({mon(base)}): revisa la extracción"}
    motivos = []
    prefijo = m.group(1, 2, 3)
    if desde.group(1, 2, 3) != prefijo or hasta.group(1, 2, 3) != prefijo or not (int(desde.group(4)) <= int(m.group(4)) <= int(hasta.group(4))):
        motivos.append(f"está fuera del rango autorizado {rango.get('from')} a {rango.get('to')}")
    if f_lim is None:
        return {"error": f"la fecha límite de emisión de la factura {num} no es una fecha: {x.get('issue_deadline')}"}
    if f_emi > f_lim:
        motivos.append(f"se emitió el {iso(f_emi)}, después de su fecha límite de emisión, el {iso(f_lim)}")
    return {
        "pais": "HN", "lector": "hn", "fuente": "F-37", "tipo": "factura", "numero": num, "fecha": iso(f_emi),
        "emisor": ident(x.get("issuer_rtn")), "receptor": ident(x.get("customer_rtn")), "base": base, "iva": isv,
        "total": total, "valores": True, "id": f"{x['cai']}:{num}", "cai": x["cai"], "fuera": motivos,
    }


def facturas_documento(cfg: dict, periodo: str, ficha: dict, tol_iva: float) -> tuple[list[dict], list[dict], list[dict]]:
    """Las facturas de un país sin esquema (Honduras): cada documento de `30-facturacion/` tiene que
    estar en la ficha, con su cita; el que no está, no se procesó. Devuelve las leídas, las que no
    se procesaron y las que se identificaron sin cruzar valores."""
    docs = cfg["_docs"]
    carpeta = docs / periodo / "30-facturacion"
    en_ficha = {str(x.get("source") or "").split("#")[0].strip(): (k, x) for k, x in (ficha.get("invoices") or {}).items()}
    leidas, no_proc, solo = [], [], []
    for lado in ("emitidas", "recibidas"):
        for p in sorted(x for x in (carpeta / lado).rglob("*") if x.is_file() and not x.name.startswith(".")) if (carpeta / lado).is_dir() else []:
            r = rel(p, docs)
            if r not in en_ficha:
                no_proc.append({"archivo": r, "motivo": "la factura no está en la ficha del cierre: el agente la extrae con su CAI, su rango autorizado y su fecha límite (decisión 0024)"})
                continue
            d = _hn(en_ficha[r][1], tol_iva)
            if "error" in d:
                no_proc.append({"archivo": r, "motivo": d["error"]})
            elif d.get("solo"):
                solo.append({"archivo": r, "tipo": d["tipo"], "numero": d["numero"]})
            else:
                d["lado"], d["archivo"] = lado, r
                leidas.append(d)
    return leidas, no_proc, solo


def leer_factura(ruta: Path) -> dict:
    """Una factura o nota electrónica de cualquier país del registro, con o sin su contenedor."""
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
        # Las dos son UBL 2.1. La de la DIAN trae el CUFE en `cbc:UUID` (F-01); la de la SUNAT no
        # trae UUID y declara `UBLVersionID` 2.1 (F-13).
        if _h(raiz, "UUID") is None and _t(raiz, "UBLVersionID") == "2.1":
            return _sunat(raiz, nombre)
        return _dian(raiz, nombre)
    if _h(raiz, "infoTributaria") is not None:
        return _sri(raiz)
    if nombre == "Comprobante" and raiz.attrib.get("Version") == "4.0":   # F-19: el CFDI 4.0 del SAT
        return _sat(raiz)
    if any(_local(x.tag) == "Encabezado" for x in raiz.iter()):   # F-16: el DTE del SII
        return _sii(raiz)
    inf = next((x for x in raiz.iter() if _local(x.tag) == "infNFe"), None)
    if inf is not None:                                         # F-21: la NF-e, suelta o dentro de nfeProc
        return _nfe(inf)
    if any(_local(x.tag) == "FECAEDetRequest" for x in raiz.iter()):   # F-24: el comprobante de ARCA
        return _wsfe(raiz)
    if nombre == "rFE":                                          # F-27: la factura electrónica de Panamá
        return _dgipa(raiz)
    if nombre == "GTDocumento":                                  # F-30: la FEL de Guatemala
        return _fel(raiz)
    if nombre in ("FacturaElectronica", "NotaCreditoElectronica") and "comprobanteselectronicos.go.cr" in raiz.tag:   # F-34
        return _cr(raiz, nombre)
    return {"error": f"no es una factura electrónica de ningún país del registro (raíz {nombre})"}


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
        "cash_forecast_pct": 10,          # Áurea: la caja real contra la proyectada
        "maturity_days": 30,              # Áurea: una obligación o inversión que vence dentro de N días
        "covenant_margin_pct": 10,        # Áurea: a menos de este margen del límite, el covenant está en riesgo
    },
    "holidays": [],
    "report": {"language": "es"},
    "execution": {"workers": 1},
}
# Lo propio de la familia CFO en cada país viene de su registro (paises.json): la factura
# electrónica —su lector, su fuente técnica, el nombre de su clave única— y la tolerancia de los
# cuadres. Cada lector dice de qué país es por su nombre, no por un código escrito aquí.
FACTURA = {c: p["factura"] for c, p in N.PAISES.items()}
PAIS_DEL_LECTOR = {f["lector"]: c for c, f in FACTURA.items()}


def tolerancias(cfg: dict) -> tuple[float, float]:
    t = (cfg.get("thresholds") or {}).get("amount_tolerance")
    if t is not None:
        return float(t), float(t)
    return tuple(FACTURA.get(N.pais_de(cfg), FACTURA[N.POR_OMISION])["tolerancia"])


def umbral(cfg: dict, k: str):
    return (cfg.get("thresholds") or {}).get(k, DEFECTOS["thresholds"][k])




def revisar_config(cfg: dict, rol: str) -> list[str]:
    p = []
    ent = cfg.get("entity") or {}
    for k in ("id", "name", "country", "currency"):
        if not ent.get(k):
            p.append(f"entity.{k} vacío")
    p += N.revisar_pais(ent)
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
    if rol == "aurea" and not cfg.get("period"):
        p.append("period vacío: Áurea trabaja sobre el periodo del cierre")
    if rol == "tomas":
        b = cfg.get("budget") or {}
        if not b.get("year"):
            p.append("budget.year vacío")
    return p




# ================================================================ las señales

SEVERIDAD = {
    "trial_balance_unbalanced": 1, "declared_close_vs_evidence": 1, "declared_vs_evidence": 1,
    "ledger_vs_trial_balance": 1, "einvoice_not_recorded": 2, "recorded_without_einvoice": 2,
    "einvoice_amount_mismatch": 2, "einvoice_duplicate": 2, "invoice_outside_authorization": 2, "bank_unreconciled": 2,
    "account_unreconciled": 2, "transfer_without_approval": 2, "forecast_over_approved": 2,
    "variance_over_threshold": 2, "budget_version_mismatch": 2, "spend_without_budget_line": 2,
    "project_budget_mismatch": 3, "committed_near_approved": 3, "close_task_overdue": 2,
    "close_task_done_without_evidence": 2, "audit_request_unanswered": 2, "reconciling_item_aged": 3,
    "reconciliation_stale": 3, "forecast_stale": 3,
    "cash_below_minimum": 1, "payment_without_approval": 1, "signatory_without_authority": 1, "covenant_at_risk": 1,
    "cash_vs_forecast": 2, "fx_exposure_over_limit": 2, "maturity_near": 2,
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


def cuentas_de_factura(docs: Path, periodo: str) -> dict:
    """Las cuentas que cruzan las facturas, sacadas de los datos y no del nombre de la cuenta: las
    del mayor que registran el número de una factura del periodo. En cada registro, la línea por la
    base es de ventas o compras, la del impuesto es del IVA o IGV, y la del total —cartera,
    proveedores, bancos— es la contrapartida y no cuenta. Devuelve los prefijos de cuatro dígitos con
    cuántas facturas los sostienen; es una propuesta para que la persona confirme."""
    from collections import Counter
    my = mayor({"_docs": docs}, periodo)
    if my is None:
        return {"error": f"no hay libro mayor en {periodo}/10-contabilidad/ para proponer las cuentas"}
    lados = {"emitidas": ("sales", "vat_generated"), "recibidas": ("purchases", "vat_deductible")}
    facturas = {lado: {} for lado in lados}
    for lado in lados:
        d_lado = docs / periodo / "30-facturacion" / lado
        for p in sorted(d_lado.rglob("*.xml")) if d_lado.is_dir() else []:
            d = leer_factura(p)
            if "error" not in d and d.get("valores", True) and d.get("base") is not None:
                facturas[lado][ident(d["numero"])] = d
    out = {k: Counter() for par in lados.values() for k in par}
    for f in my.filas:
        doc, cta = ident(f.get("documento")), str(f.get("cuenta") or "").strip()
        if not doc or not cta:
            continue
        v = abs((numero(f.get("debito")) or 0.0) - (numero(f.get("credito")) or 0.0))
        for lado, (base_k, iva_k) in lados.items():
            d = facturas[lado].get(doc)
            if not d:
                continue
            total = d.get("total") or (d["base"] + (d.get("iva") or 0))
            cerca = min((("base", d["base"]), ("iva", d.get("iva") or 0.0), ("total", total)), key=lambda x: abs(v - x[1]))[0]
            if cerca != "total":
                out[base_k if cerca == "base" else iva_k][cta[:4]] += 1
    return {k: [{"prefijo": c, "facturas": n} for c, n in sorted(v.items(), key=lambda x: (-x[1], x[0]))] for k, v in out.items()}


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
        ex, au = buscar(sub, "extracto", pdf=True), buscar(sub, "auxiliar")
        if not ex or not au:
            falta = "el extracto" if not ex else "el auxiliar de libros"
            out["alertas"].append(alerta("reconciliation_stale", f"{sub.name}: falta {falta} del periodo",
                                         {"archivo": rel(sub, docs) + "/"}, clave=f"banco:{sub.name}"))
            continue
        try:
            te = Tabla(ex[0], ["fecha", "valor"], ["referencia", "descripcion", "saldo_final", "documento", "debito", "credito"], cols.get("bank_statement"))
            if te.faltan and "valor" in te.faltan:
                te = Tabla(ex[0], ["fecha", "debito", "credito"], ["referencia", "descripcion", "saldo_final", "documento"], cols.get("bank_statement"))
        except ValueError as e:      # un PDF sin texto o sin pdftotext: se dice, no se adivina
            out["no_procesado"].append({"archivo": rel(ex[0], docs), "motivo": str(e)})
            continue
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


def facturas(cfg: dict, periodo: str, ficha: dict | None = None) -> dict:
    docs = cfg["_docs"]
    carpeta = docs / periodo / "30-facturacion"
    tol, tol_iva = tolerancias(cfg)
    pais = N.pais_de(cfg)
    ac = cfg.get("accounts") or {}
    out = {"periodo": periodo, "facturas": 0, "alertas": [], "no_procesado": [], "solo_identidad": [],
           "sin_documento": [], "cruzadas": 0, "fuentes": sorted(FACTURA[N.pais_de(cfg)]["fuentes"])}
    leidas = []
    if FACTURA[pais].get("documento"):
        leidas, out["no_procesado"], out["solo_identidad"] = facturas_documento(cfg, periodo, ficha or {}, tol_iva)
        for d in leidas:
            # Una factura recibida fuera de su autorización no sustenta el crédito fiscal del ISV
            # (decisión 0024): se pone al lado del registro que la usa, si lo hay.
            if d["lado"] == "recibidas" and d["fuera"]:
                out["alertas"].append(alerta("invoice_outside_authorization", f"factura recibida {d['numero']} del {d['emisor']}: " + "; ".join(d["fuera"]),
                                             {"archivo": d["archivo"]}, d.get("total"), clave=f"cai:{d['archivo']}"))
    for lado in ("emitidas", "recibidas") if not FACTURA[pais].get("documento") else ():
        for p in sorted((carpeta / lado).rglob("*.xml")) if (carpeta / lado).is_dir() else []:
            d = leer_factura(p)
            if "error" in d:
                out["no_procesado"].append({"archivo": rel(p, docs), "motivo": d["error"]})
                continue
            if d.get("lector") == "sri" and not d["clave"]["valida"]:
                out["no_procesado"].append({"archivo": rel(p, docs), "motivo": "; ".join(d["clave"]["motivos"])})
                continue
            d["lado"], d["archivo"] = lado, rel(p, docs)
            leidas.append(d)
    out["facturas"] = len(leidas)
    # Las facturas emitidas del periodo, para quien las cruza sin volver a procesarlas: Valeria, de la
    # familia CCO, pone cada contrato firmado con un cliente al lado de su factura (ADR 0019).
    out["emitidas"] = [{"numero": d.get("numero"), "id": d.get("id"), "fecha": d.get("fecha"), "receptor": d.get("receptor"),
                        "base": d.get("base"), "total": d.get("total"), "tipo": d["tipo"], "archivo": d["archivo"]}
                       for d in leidas if d["lado"] == "emitidas" and d["tipo"] == "factura"]
    por_id = {}
    for d in leidas:
        por_id.setdefault(d.get("id") or d["archivo"], []).append(d)
    for k, v in por_id.items():
        if len(v) > 1:
            out["alertas"].append(alerta("einvoice_duplicate", f"el mismo {FACTURA[v[0]['pais']]['clave']} aparece en {len(v)} archivos ({v[0]['numero']})",
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
        if d["tipo"] not in ("factura", "nota de crédito", "liquidación de compra") or not d.get("valores", True):
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
                partes.append(f"{FACTURA[d['pais']]['impuesto']} {mon(signo * (d['iva'] or 0))} en el XML y {mon(r['iva'])} en libros")
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
        declarada = N.canon(f.get("estado")) in ("cumplida", "cumplido", "hecho", "hecha", "completada", "completado", "cerrada", "ok", "done")
        tareas[tid] = {"id": tid, "tarea": f["tarea"], "area": f.get("area"), "responsable": f["responsable"],
                       "limite": iso(_limite(f["dia_limite"], periodo, feriados)), "criticidad": N.canon(f.get("criticidad")) or "media",
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
                         "responsable": x.get("responsable"), "declarado": N.canon(x.get("estado")), "cita": t.cita(x, docs)}
    for r in (ficha.get("audit_requests") or []):
        rid = str(r.get("id") or "").strip()
        if rid and rid not in reqs:
            reqs[rid] = {"id": rid, "solicitud": r.get("request"), "fecha": r.get("date"), "limite": r.get("due"),
                         "responsable": r.get("owner"), "declarado": N.canon(r.get("status")), "cita": {"archivo": r.get("source")}}
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
    _PAIS[0] = N.pais_de(cfg)
    estado = cfg["_estado"] / "cierre" / periodo
    ficha = leer_json(estado / "ficha.json", {}) or {}
    problemas = revisar_ficha_cierre(ficha)
    partes = {
        "ledger-check": cuadre(cfg, periodo), "bank-reconcile": bancos(cfg, periodo),
        "account-reconcile": cuentas(cfg, periodo), "einvoice-check": facturas(cfg, periodo, ficha),
        "close-status": checklist(cfg, periodo, hoy), "audit-pack": auditoria(cfg, periodo, hoy, ficha),
    }
    alertas = [a for p in partes.values() for a in p["alertas"]]
    dec = (ficha.get("declared") or {})
    if N.canon(dec.get("status")) in ("cerrado", "cerrada", "closed"):
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
    fs = f.get("invoices")
    if fs is not None and not isinstance(fs, dict):
        p.append("invoices: va por el RTN del emisor y el número correlativo, {\"08019002265431:000-001-01-00000123\": {...}}")
    for k, x in (fs or {}).items() if isinstance(fs, dict) else ():
        if not isinstance(x, dict) or not x.get("source"):
            p.append(f"invoices[{k}]: cada factura lleva su source, el documento del que se extrajo")
        elif f"{x.get('issuer_rtn')}:{x.get('number')}" != k:
            p.append(f"invoices[{k}]: la llave es el RTN del emisor y el número correlativo, {x.get('issuer_rtn')}:{x.get('number')}")
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
    _PAIS[0] = N.pais_de(cfg)
    estado = cfg["_estado"] / "presupuesto" / anio
    ficha = leer_json(estado / "ficha.json", {}) or {}
    problemas = revisar_ficha_presupuesto(ficha) + escritos_sin_citar(cfg, anio, ficha)
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
        if norm(dcl.get("says")) not in ("dentro", "dentro_del_presupuesto", "within", "within_budget", "en_presupuesto", "dentro_do_orcamento"):
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
        rp = rp if rp.is_absolute() else Path(cfg.get("_raiz") or Path.cwd()) / rp
        fichas_pmo = sorted(rp.glob("*.json")) if rp.is_dir() else []
        if not fichas_pmo:
            no_proc.append({"archivo": str(pmo), "motivo": "la configuración apunta a las fichas de la familia PMO y ahí no hay ninguna: el presupuesto de los proyectos no se cruzó"})
        for r in fichas_pmo:
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


ESCRITOS = {".md", ".txt", ".docx", ".pdf", ".eml"}


def _fuentes(x) -> set[str]:
    """Cada `source` de la ficha, a cualquier profundidad."""
    if isinstance(x, dict):
        return ({str(x["source"])} if x.get("source") else set()) | {s for v in x.values() for s in _fuentes(v)}
    if isinstance(x, list):
        return {s for v in x for s in _fuentes(v)}
    return set()


def escritos_sin_citar(cfg: dict, anio: str, f: dict) -> list[str]:
    """Las actas y lo que escriben las áreas son lo único que el agente lleva a la ficha: un escrito de
    `30-proyecciones/` o de `40-actas/` que la ficha no cita es uno que nadie procesó. Si no trae nada
    para la ficha, va en `reviewed` con el motivo; así no se calla."""
    docs, citadas = cfg["_docs"], _fuentes(f)
    out = []
    for sub in ("30-proyecciones", "40-actas"):
        d = docs / f"presupuesto-{anio}" / sub
        for x in sorted(d.rglob("*")) if d.is_dir() else []:
            r = rel(x, docs)
            if x.is_file() and x.suffix.lower() in ESCRITOS and not x.name.startswith(".") and r not in citadas:
                out.append(f"{r}: documento escrito que la ficha no cita; extrae lo que diga, o anótalo en reviewed con el motivo")
    return out


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
    for i, r in enumerate(f.get("reviewed") or []):
        if not r.get("source") or not r.get("note"):
            p.append(f"reviewed[{i}]: lleva source y note, el motivo por el que no trae nada para la ficha")
    for i, q in enumerate(f.get("questions") or []):
        if not q.get("question") or "answer" not in q:
            p.append(f"questions[{i}]: lleva question y answer")
    return p


# ================================================================ Áurea · la tesorería (ADR 0016)
#
# Contrasta la caja contra su mínimo y su proyección, cada pago programado contra quién puede
# aprobarlo, y la deuda contra su vencimiento y lo que exige su contrato. Procesa exportaciones —el
# extracto del periodo que también concilia Clara, el programa de pagos, el flujo proyectado— y la
# política, la matriz de firmas y el registro de la deuda de `00-referencia/`. Nunca mueve dinero ni
# entra a un portal bancario. Los covenants salen del balance del mismo periodo que cierra Clara: el
# motor no recalcula la contabilidad, la toma.

def _citas(*cs) -> list[dict]:
    return [c for c in cs if c]


def _referencia(cfg: dict, patron: str, requeridas: list[str], opcionales: list[str] = ()) -> Tabla | None:
    f = buscar(cfg["_docs"] / "00-referencia", patron)
    if not f:
        return None
    t = Tabla(f[0], requeridas, opcionales)
    return None if t.faltan else t


def politica(cfg: dict) -> dict:
    """La política de tesorería: caja mínima por cuenta y consolidada, aprobadores por monto, límite
    de exposición y tasa de referencia por moneda. Una fila por regla: concepto, referencia, valor."""
    out = {"caja_minima": {}, "aprobadores": [], "limite_exposicion": {}, "tasa": {}, "cita": {}}
    t = _referencia(cfg, "politica", ["concepto", "referencia", "valor"])
    if t is None:
        return out
    for f in t.filas:
        c, ref, v = N.canon(f["concepto"]).replace(" ", "_"), str(f["referencia"]).strip(), numero(f["valor"])
        if v is None:
            continue
        cita = t.cita(f, cfg["_docs"])
        if c == "caja_minima":
            out["caja_minima"][ref.lower()] = v
            out["cita"][f"caja:{ref.lower()}"] = cita
        elif c == "aprobadores":
            out["aprobadores"].append((numero(ref) or 0.0, int(v), cita))
        elif c == "limite_exposicion":
            out["limite_exposicion"][ref.upper()] = v
            out["cita"][f"exposicion:{ref.upper()}"] = cita
        elif c == "tasa":
            out["tasa"][ref.upper()] = v
    out["aprobadores"].sort(key=lambda x: x[0])
    return out


def _saldo_final(ruta: Path) -> tuple[float | None, int | None, str | None]:
    """El último saldo del extracto, con su fila y, si el extracto la trae, su moneda."""
    try:
        t = Tabla(ruta, ["fecha"], ["saldo_final", "valor", "moneda"])
    except ValueError:
        return None, None, None
    if t.faltan or not t.filas:
        return None, None, None
    con = [f for f in t.filas if numero(f.get("saldo_final")) is not None]
    if not con:
        return None, None, None
    ult = max(con, key=lambda f: (fecha(f.get("fecha")) or dt.date.min, f["_fila"]))
    return numero(ult["saldo_final"]), ult["_fila"], (str(ult.get("moneda") or "").strip().upper() or None)


def caja(cfg: dict, periodo: str, pol: dict) -> dict:
    docs, out = cfg["_docs"], {"cuentas": [], "alertas": [], "no_procesado": []}
    monedas = {k.lower(): v.upper() for k, v in ((cfg.get("treasury") or {}).get("currencies") or {}).items()}
    funcional = ((cfg.get("entity") or {}).get("currency") or "").upper()
    carpeta = docs / periodo / "20-bancos"
    proy_f = buscar(docs / periodo / "60-tesoreria", "flujo")
    proy = {}
    if proy_f:
        tp = Tabla(proy_f[0], ["cuenta", "saldo_proyectado"])
        if tp.faltan:
            out["no_procesado"].append({"archivo": rel(proy_f[0], docs), "motivo": f"le faltan {', '.join(tp.faltan)}"})
        else:
            proy = {str(f["cuenta"]).strip().lower(): (numero(f["saldo_proyectado"]), tp.cita(f, docs)) for f in tp.filas}
    consolidado, exposicion = 0.0, {}
    for sub in sorted(x for x in carpeta.iterdir() if x.is_dir()) if carpeta.is_dir() else []:
        ex = buscar(sub, "extracto", pdf=True)
        if not ex:
            out["no_procesado"].append({"archivo": rel(sub, docs), "motivo": "no está el extracto"})
            continue
        saldo, fila, del_extracto = _saldo_final(ex[0])
        if saldo is None:
            out["no_procesado"].append({"archivo": rel(ex[0], docs), "motivo": "el extracto no trae saldo"})
            continue
        # La moneda: la que fija la configuración; si no, la que dice el extracto; si no, la funcional.
        cuenta = sub.name.lower()
        moneda = monedas.get(cuenta) or del_extracto or funcional
        cita = {"archivo": rel(ex[0], docs), "fila": fila}
        tasa = 1.0 if moneda == funcional else pol["tasa"].get(moneda)
        en_funcional = saldo * tasa if tasa else None
        if en_funcional is not None:
            consolidado += en_funcional
        if moneda != funcional:
            exposicion.setdefault(moneda, [0.0, []])
            exposicion[moneda][0] += en_funcional or 0.0
            exposicion[moneda][1].append(cita)
        minimo = pol["caja_minima"].get(cuenta)
        p, pcita = proy.get(cuenta, (None, None))
        fila_c = {"cuenta": sub.name, "moneda": moneda, "saldo": redondo(saldo), "minimo": minimo, "proyectado": p,
                  "desviacion_pct": redondo(100 * (saldo - p) / abs(p)) if p else None, "cita": cita}
        out["cuentas"].append(fila_c)
        if minimo is not None and saldo < minimo:
            out["alertas"].append(alerta("cash_below_minimum", f"{sub.name}: saldo {mon(saldo)} {moneda}, bajo el mínimo de {mon(minimo)}",
                                         _citas(cita, pol["cita"].get(f"caja:{cuenta}")), monto=minimo - saldo, clave=f"caja:{cuenta}"))
        if p and abs(saldo - p) / abs(p) * 100 > umbral(cfg, "cash_forecast_pct"):
            out["alertas"].append(alerta("cash_vs_forecast", f"{sub.name}: saldo {mon(saldo)} contra {mon(p)} proyectado ({pc(100 * (saldo - p) / abs(p), True)})",
                                         _citas(cita, pcita), monto=abs(saldo - p), clave=f"proyeccion:{cuenta}"))
    out["consolidado"] = redondo(consolidado)
    minimo = pol["caja_minima"].get("consolidado")
    if minimo is not None and out["cuentas"] and consolidado < minimo:
        out["alertas"].append(alerta("cash_below_minimum", f"la caja consolidada, {mon(consolidado)} {funcional}, está bajo el mínimo de {mon(minimo)}",
                                     pol["cita"].get("caja:consolidado"), monto=minimo - consolidado, clave="caja:consolidado"))
    out["exposicion"] = []
    for moneda, (valor, citas) in sorted(exposicion.items()):
        lim = pol["limite_exposicion"].get(moneda)
        out["exposicion"].append({"moneda": moneda, "en_funcional": redondo(valor), "limite": lim})
        if moneda not in pol["tasa"]:
            out["no_procesado"].append({"archivo": "00-referencia/", "motivo": f"la política no trae la tasa de {moneda}: su exposición no se calcula"})
        elif lim is not None and abs(valor) > lim:
            out["alertas"].append(alerta("fx_exposure_over_limit", f"la posición en {moneda} equivale a {mon(valor)} {funcional}, sobre el límite de {mon(lim)}",
                                         _citas(*citas, pol["cita"].get(f"exposicion:{moneda}")), monto=abs(valor) - lim, clave=f"exposicion:{moneda}"))
    return out


def pagos(cfg: dict, periodo: str, pol: dict) -> dict:
    """Cada pago programado contra los aprobadores que pide la política para su monto y contra la
    matriz de firmas: el mismo patrón de quién firmó con qué facultad que usa Fidel."""
    docs, out = cfg["_docs"], {"pagos": [], "alertas": [], "no_procesado": []}
    pf = buscar(docs / periodo / "60-tesoreria", "programa")
    if not pf:
        return out
    t = Tabla(pf[0], ["id", "valor"], ["fecha", "beneficiario", "moneda", "aprobado_por"])
    if t.faltan:
        out["no_procesado"].append({"archivo": rel(pf[0], docs), "motivo": f"le faltan {', '.join(t.faltan)}"})
        return out
    mf = _referencia(cfg, "matriz", ["nombre", "monto_maximo"], ["cargo"])
    firmas = {norm(f["nombre"]): (numero(f["monto_maximo"]), mf.cita(f, docs)) for f in mf.filas} if mf else {}
    if mf is None:
        out["no_procesado"].append({"archivo": "00-referencia/", "motivo": "no está la matriz de firmas: no se revisa quién aprobó"})
    for f in t.filas:
        valor = numero(f["valor"]) or 0.0
        quienes = [x.strip() for x in re.split(r"[;,/]| y ", str(f.get("aprobado_por") or "")) if x.strip()]
        pide = max((n for desde, n, _ in pol["aprobadores"] if valor >= desde), default=1)
        cita = t.cita(f, docs)
        out["pagos"].append({"id": f["id"], "fecha": iso(fecha(f.get("fecha"))), "beneficiario": f.get("beneficiario"),
                             "valor": redondo(valor), "aprobado_por": quienes, "pide": pide, "cita": cita})
        if len(quienes) < pide:
            pol_cita = next((c for desde, n, c in reversed(pol["aprobadores"]) if valor >= desde), None)
            out["alertas"].append(alerta("payment_without_approval",
                                         f"pago {f['id']} a {f.get('beneficiario') or '—'} por {mon(valor)}: {len(quienes)} de {pide} aprobaciones que pide la política",
                                         _citas(cita, pol_cita), monto=valor, clave=f"pago:{f['id']}"))
        if mf is None:
            continue
        for q in quienes:
            maximo, fcita = firmas.get(norm(q), (None, None))
            if maximo is None or valor > maximo:
                motivo = "no está en la matriz de firmas" if maximo is None else f"firma hasta {mon(maximo)}"
                out["alertas"].append(alerta("signatory_without_authority", f"pago {f['id']} por {mon(valor)}: lo aprobó {q}, que {motivo}",
                                             _citas(cita, fcita), monto=valor, responsable=q, clave=f"firma:{f['id']}:{norm(q)}"))
    return out


def deuda(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    """Los vencimientos de la deuda y las inversiones, y cada covenant calculado desde el balance del
    periodo que cierra Clara."""
    docs, out = cfg["_docs"], {"obligaciones": [], "covenants": [], "alertas": [], "no_procesado": []}
    rd = _referencia(cfg, "registro_deuda", ["obligacion", "vencimiento"], ["tipo", "contraparte", "saldo", "moneda"])
    if rd is not None:
        dias_max = umbral(cfg, "maturity_days")
        for f in rd.filas:
            v = fecha(f["vencimiento"])
            dias = (v - hoy).days if v else None
            out["obligaciones"].append({"obligacion": f["obligacion"], "tipo": N.canon(f.get("tipo")) or "deuda", "contraparte": f.get("contraparte"),
                                        "saldo": numero(f.get("saldo")), "moneda": f.get("moneda"), "vence": iso(v), "dias": dias,
                                        "cita": rd.cita(f, docs)})
            if dias is not None and 0 <= dias <= dias_max:
                out["alertas"].append(alerta("maturity_near", f"{f['obligacion']} ({f.get('tipo') or 'deuda'}, {f.get('contraparte') or '—'}) vence el {iso(v)}, en {dias} días",
                                             rd.cita(f, docs), monto=numero(f.get("saldo")), dias=dias, clave=f"vence:{norm(f['obligacion'])}"))
    cv = _referencia(cfg, "covenants", ["obligacion", "indicador", "numerador", "denominador", "operador", "limite"])
    if cv is None:
        return out
    saldos = saldos_balance(cfg, periodo)
    if not saldos:
        out["no_procesado"].append({"archivo": f"{periodo}/10-contabilidad/", "motivo": "no está el balance del periodo: los covenants no se calculan"})
        return out
    margen = umbral(cfg, "covenant_margin_pct")

    def suma(prefijos: str) -> float:
        ps = [p.strip() for p in re.split(r"[;,+ ]+", str(prefijos)) if p.strip()]
        return abs(sum(s for c, (s, _, _) in saldos.items() if s is not None and any(c.startswith(p) for p in ps)))
    for f in cv.filas:
        num, den, lim = suma(f["numerador"]), suma(f["denominador"]), numero(f["limite"])
        op = str(f["operador"]).strip()
        if not den or lim is None or op not in ("<=", ">="):
            out["no_procesado"].append({"archivo": rel(cv.ruta, docs), "motivo": f"fila {f['_fila']}: el covenant no se puede calcular"})
            continue
        valor = num / den
        # Cruzar es pasar el límite; acercarse, quedar a menos del margen de él.
        cruza = valor > lim if op == "<=" else valor < lim
        cerca = (not cruza) and (abs(lim - valor) / abs(lim) * 100 <= margen)
        estado = "incumplido" if cruza else ("en riesgo" if cerca else "cumple")
        out["covenants"].append({"obligacion": f["obligacion"], "indicador": f["indicador"], "valor": round(valor, 2),
                                 "operador": op, "limite": lim, "estado": estado, "cita": cv.cita(f, docs)})
        if cruza or cerca:
            out["alertas"].append(alerta("covenant_at_risk",
                                         f"{f['obligacion']} · {f['indicador']}: {valor:.2f} contra el límite {op} {lim:g} ({estado}), desde el balance de {periodo}",
                                         cv.cita(f, docs), severidad=1 if cruza else 2,
                                         clave=f"covenant:{norm(f['obligacion'])}:{norm(f['indicador'])}"))
    return out


def aurea(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _PAIS[0] = N.pais_de(cfg)
    estado = cfg["_estado"] / "tesoreria" / periodo
    ficha = leer_json(estado / "ficha.json", {}) or {}
    pol = politica(cfg)
    partes = {"cash-position": caja(cfg, periodo, pol), "payment-check": pagos(cfg, periodo, pol), "debt-watch": deuda(cfg, periodo, hoy)}
    no_proc = [x for p in partes.values() for x in p.pop("no_procesado")]
    if not pol["caja_minima"] and not pol["aprobadores"]:
        no_proc.append({"archivo": "00-referencia/", "motivo": "no está la política de tesorería: sin ella no hay mínimo de caja ni aprobadores por monto"})
    alertas = [a for p in partes.values() for a in p["alertas"]]
    # Para la vista de lo que vence de Rostrum, con la misma forma que la de Clara (ADR 0010).
    vence = sorted(({"fecha": o["vence"], "que": f"{o['obligacion']} · {o['tipo']}", "caso": periodo, "estado": "por vencer",
                     "responsable": o.get("contraparte"), "comando": "debt-watch"}
                    for o in partes["debt-watch"]["obligaciones"] if o["dias"] is not None and 0 <= o["dias"] <= umbral(cfg, "maturity_days")),
                   key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "aurea", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(fin_de_mes(periodo)),
            "hoy": iso(hoy), "partes": partes, "alertas": ordenar(alertas), "no_procesado": no_proc,
            "record_issues": [], "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ el reporte, en el formato común

NOMBRE = {"clara": "Clara", "tomas": "Tomás", "aurea": "Áurea"}
SENALES_DE = {
    "ledger-check": {"trial_balance_unbalanced", "ledger_vs_trial_balance"},
    "bank-reconcile": {"bank_unreconciled", "reconciling_item_aged", "reconciliation_stale"},
    "account-reconcile": {"account_unreconciled", "reconciliation_stale"},
    "einvoice-check": {"einvoice_not_recorded", "recorded_without_einvoice", "einvoice_amount_mismatch", "einvoice_duplicate", "invoice_outside_authorization"},
    "close-status": {"close_task_overdue", "close_task_done_without_evidence", "declared_close_vs_evidence"},
    "audit-pack": {"audit_request_unanswered"},
    "variance-report": {"variance_over_threshold", "committed_near_approved", "spend_without_budget_line", "declared_vs_evidence", "project_budget_mismatch"},
    "forecast": {"forecast_over_approved", "forecast_stale", "budget_version_mismatch"},
    "transfer-log": {"transfer_without_approval"},
    "cash-position": {"cash_below_minimum", "cash_vs_forecast", "fx_exposure_over_limit"},
    "payment-check": {"payment_without_approval", "signatory_without_authority"},
    "debt-watch": {"covenant_at_risk", "maturity_near"},
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
    elif comando == "cash-position" and p:
        l += [f"**Caja consolidada:** {_m(p.get('consolidado'))}", "",
              "| Cuenta | Moneda | Saldo | Mínimo | Proyectado | Desviación % |", "|---|---|---|---|---|---|"]
        l += [f"| {c['cuenta']} | {c['moneda']} | {_m(c['saldo'])} | {_m(c['minimo'])} | {_m(c['proyectado'])} | {_m(c['desviacion_pct'])} |" for c in p["cuentas"]]
        if p.get("exposicion"):
            l += ["", "| Moneda | Posición en moneda funcional | Límite |", "|---|---|---|"]
            l += [f"| {x['moneda']} | {_m(x['en_funcional'])} | {_m(x['limite'])} |" for x in p["exposicion"]]
        l += ["", "Áurea no mueve dinero ni entra a un portal bancario: procesa las exportaciones.", ""]
    elif comando == "payment-check" and p:
        l += ["| Pago | Fecha | Beneficiario | Valor | Aprobado por | Pide |", "|---|---|---|---|---|---|"]
        l += [f"| {x['id']} | {x['fecha'] or '—'} | {x['beneficiario'] or '—'} | {_m(x['valor'])} | {', '.join(x['aprobado_por']) or '—'} | {x['pide']} |" for x in p["pagos"]]
        l.append("")
    elif comando == "debt-watch" and p:
        if p.get("covenants"):
            l += ["| Obligación | Indicador | Valor | Límite | Estado |", "|---|---|---|---|---|"]
            l += [f"| {c['obligacion']} | {c['indicador']} | {c['valor']:.2f} | {c['operador']} {c['limite']:g} | {c['estado']} |" for c in p["covenants"]]
            l.append("")
        l += ["| Obligación | Tipo | Contraparte | Saldo | Vence | Días |", "|---|---|---|---|---|---|"]
        l += [f"| {o['obligacion']} | {o['tipo']} | {o['contraparte'] or '—'} | {_m(o['saldo'])} | {o['vence'] or '—'} | {o['dias'] if o['dias'] is not None else '—'} |" for o in sorted(p["obligaciones"], key=lambda o: (o['dias'] is None, o['dias']))]
        l += ["", "Áurea no recomienda una inversión, un financiamiento ni una cobertura: la decisión es de una persona.", ""]
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
    elif rol == "aurea":
        # La tesorería corre cuando hay pagos programados en los próximos días o una obligación que
        # entra en la ventana de vencimiento; si no, una vez por semana.
        u = ultima("treasury-scan")
        if u != hoy:
            r = aurea(cfg, cfg.get("period"), hoy) if cfg.get("period") else None
            pronto = [x for x in (r["partes"]["payment-check"]["pagos"] if r else []) if x["fecha"] and 0 <= (fecha(x["fecha"]) - hoy).days <= 5]
            if pronto:
                toca, motivo = ["treasury-scan", "payment-check", "cash-position"], [f"hay {len(pronto)} pagos programados en los próximos cinco días"]
            elif r and r["vence"]:
                toca, motivo = ["treasury-scan", "debt-watch"], [f"{len(r['vence'])} obligaciones entran en la ventana de vencimiento"]
            elif not u or (hoy - u).days >= 7:
                toca, motivo = ["treasury-scan"], ["una vez por semana"]
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
    return {"criterio-budget": "tomas", "criterio-treasury": "aurea"}.get(N.plugin(AQUI)["name"], "clara")


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    if rol in ("clara", "aurea"):
        periodo = a.period or cfg.get("period")
        if not periodo:
            raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
        r = (clara if rol == "clara" else aurea)(cfg, periodo, hoy)
        destino = cfg["_estado"] / ("cierre" if rol == "clara" else "tesoreria") / periodo / "resultados.json"
    else:
        anio = str(a.year or (cfg.get("budget") or {}).get("year"))
        corte = a.period or (cfg.get("budget") or {}).get("cut") or f"{anio}-{hoy.month:02d}"
        r = tomas(cfg, anio, corte, hoy)
        destino = cfg["_estado"] / "presupuesto" / anio / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Clara, Tomás y Áurea.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir",
                                       "compute", "reporte", "factura", "cuentas", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action == "factura":
        print(json.dumps(leer_factura(a.file), ensure_ascii=False, indent=2))
        return 0
    if a.action == "cuentas":
        if not a.docs or not a.period:
            ap.error("cuentas: --docs <carpeta de la entidad> --period AAAA-MM")
        print(json.dumps(cuentas_de_factura(Path(a.docs), a.period), ensure_ascii=False, indent=2))
        return 0
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=("cierre", "presupuesto", "tesoreria"),
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


def leer_factura_texto(xml: str, carpeta: Path) -> dict:
    """Para las pruebas: lee un XML escrito en una cadena."""
    p = carpeta / "_prueba.xml"
    p.write_text(xml, encoding="utf-8")
    try:
        return leer_factura(p)
    finally:
        p.unlink()


def factura_sunat(numero_: str, fecha_: str, ruc: str, receptor: str, base: float, igv: float) -> str:
    """Una factura UBL 2.1 de la SUNAT con lo que procesa el lector (F-13), para las pruebas y el material."""
    m = 'currencyID="PEN"'
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" '
            'xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" '
            'xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">'
            f'<cbc:UBLVersionID>2.1</cbc:UBLVersionID><cbc:CustomizationID>2.0</cbc:CustomizationID><cbc:ID>{numero_}</cbc:ID>'
            f'<cbc:IssueDate>{fecha_}</cbc:IssueDate><cbc:InvoiceTypeCode listAgencyName="PE:SUNAT">01</cbc:InvoiceTypeCode>'
            '<cbc:DocumentCurrencyCode>PEN</cbc:DocumentCurrencyCode>'
            f'<cac:AccountingSupplierParty><cac:Party><cac:PartyTaxScheme><cbc:CompanyID schemeID="6">{ruc}</cbc:CompanyID></cac:PartyTaxScheme></cac:Party></cac:AccountingSupplierParty>'
            f'<cac:AccountingCustomerParty><cac:Party><cac:PartyTaxScheme><cbc:CompanyID schemeID="6">{receptor}</cbc:CompanyID></cac:PartyTaxScheme></cac:Party></cac:AccountingCustomerParty>'
            f'<cac:TaxTotal><cbc:TaxAmount {m}>{igv:.2f}</cbc:TaxAmount><cac:TaxSubtotal><cbc:TaxableAmount {m}>{base:.2f}</cbc:TaxableAmount>'
            f'<cbc:TaxAmount {m}>{igv:.2f}</cbc:TaxAmount><cac:TaxCategory><cac:TaxScheme><cbc:ID>1000</cbc:ID><cbc:Name>IGV</cbc:Name>'
            '<cbc:TaxTypeCode>VAT</cbc:TaxTypeCode></cac:TaxScheme></cac:TaxCategory></cac:TaxSubtotal></cac:TaxTotal>'
            f'<cac:LegalMonetaryTotal><cbc:LineExtensionAmount {m}>{base:.2f}</cbc:LineExtensionAmount>'
            f'<cbc:TaxInclusiveAmount {m}>{base + igv:.2f}</cbc:TaxInclusiveAmount><cbc:PayableAmount {m}>{base + igv:.2f}</cbc:PayableAmount>'
            '</cac:LegalMonetaryTotal></Invoice>')


def factura_sat(serie: str, folio: str, fecha_: str, emisor: str, receptor: str, subtotal: float, iva: float) -> str:
    """Un CFDI 4.0 de ingreso con lo que procesa el lector (F-19), para las pruebas y el material."""
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/4" '
            f'Version="4.0" Serie="{serie}" Folio="{folio}" Fecha="{fecha_}T10:00:00" SubTotal="{subtotal:.2f}" Moneda="MXN" '
            f'Total="{subtotal + iva:.2f}" TipoDeComprobante="I" Exportacion="01" LugarExpedicion="06600">'
            f'<cfdi:Emisor Rfc="{emisor}" Nombre="EMISOR DE PRUEBA" RegimenFiscal="601"/>'
            f'<cfdi:Receptor Rfc="{receptor}" Nombre="RECEPTOR DE PRUEBA" DomicilioFiscalReceptor="06600" RegimenFiscalReceptor="601" UsoCFDI="G03"/>'
            f'<cfdi:Conceptos><cfdi:Concepto ClaveProdServ="84111506" Cantidad="1" ClaveUnidad="E48" Descripcion="Servicio" ValorUnitario="{subtotal:.2f}" Importe="{subtotal:.2f}" ObjetoImp="02">'
            f'<cfdi:Impuestos><cfdi:Traslados><cfdi:Traslado Base="{subtotal:.2f}" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="{iva:.2f}"/></cfdi:Traslados></cfdi:Impuestos>'
            '</cfdi:Concepto></cfdi:Conceptos>'
            f'<cfdi:Impuestos TotalImpuestosTrasladados="{iva:.2f}"><cfdi:Traslados><cfdi:Traslado Base="{subtotal:.2f}" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="{iva:.2f}"/></cfdi:Traslados></cfdi:Impuestos>'
            '</cfdi:Comprobante>')


def cnpj(raiz: str) -> str:
    """Un CNPJ con sus dos dígitos verificadores por módulo 11 (pesos de 2 a 9 de derecha a izquierda;
    un resto de 0 o 1 da 0), para que el material tenga la forma de uno real. Ninguno corresponde a una
    empresa: la raíz de ocho dígitos la pone el material."""
    base = f"{int(raiz):08d}0001"
    for _ in range(2):
        tot = sum(int(c) * (2 + i % 8) for i, c in enumerate(reversed(base)))
        r = tot % 11
        base += "0" if r < 2 else str(11 - r)
    return base


def chave_nfe(cuf: str, fecha_: str, emisor: str, serie: str, nnf: str, cnf: str) -> str:
    """La chave de acesso de 44 dígitos de una NF-e de prueba, en el orden de sus campos (F-21: cUF B02,
    año y mes, CNPJ C02, mod B06, serie B07, nNF B08, tpEmis B22, cNF B03 y cDV B23). El dígito
    verificador es el módulo 11 que pide B23; su regla completa está en el MOC, Visión General, y el
    lector no lo valida en esta versión."""
    k = f"{cuf}{fecha_[2:4]}{fecha_[5:7]}{emisor:0>14}55{int(serie):03d}{int(nnf):09d}1{int(cnf):08d}"
    tot = sum(int(c) * (2 + i % 8) for i, c in enumerate(reversed(k)))
    r = tot % 11
    return k + ("0" if r < 2 else str(11 - r))


def factura_nfe(serie: str, nnf: str, fecha_: str, emisor: str, receptor: str, base: float, icms: float,
                pis: float = 0.0, cofins: float = 0.0, cuf: str = "35", cmun: str = "3550308") -> str:
    """Una NF-e modelo 55 de salida, autorizada, con lo que procesa el lector (F-21), para las pruebas y
    el material: el ICMS va dentro del valor de la operación (I11, p. 18), así que vProd y vNF son la
    base más el ICMS, y el ICMS es la alícuota sobre ese valor."""
    vnf = round(base + icms, 2)
    alic = round(100 * icms / vnf, 2) if vnf else 0.0
    ch = chave_nfe(cuf, fecha_, emisor, serie, nnf, f"{int(nnf) * 7 % 10**8:08d}")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">'
            f'<NFe><infNFe Id="NFe{ch}" versao="4.00"><ide><cUF>{cuf}</cUF><cNF>{ch[35:43]}</cNF><natOp>Venda de mercadoria</natOp>'
            f'<mod>55</mod><serie>{int(serie)}</serie><nNF>{int(nnf)}</nNF><dhEmi>{fecha_}T10:00:00-03:00</dhEmi><tpNF>1</tpNF>'
            f'<idDest>1</idDest><cMunFG>{cmun}</cMunFG><tpImp>1</tpImp><tpEmis>1</tpEmis><cDV>{ch[-1]}</cDV><tpAmb>1</tpAmb>'
            '<finNFe>1</finNFe><indFinal>0</indFinal><indPres>9</indPres><procEmi>0</procEmi><verProc>1.0</verProc></ide>'
            f'<emit><CNPJ>{emisor}</CNPJ><xNome>EMITENTE DE TESTE</xNome><enderEmit><xLgr>Rua de Teste</xLgr><nro>100</nro>'
            f'<xBairro>Centro</xBairro><cMun>{cmun}</cMun><xMun>Sao Paulo</xMun><UF>SP</UF></enderEmit><IE>110042490114</IE><CRT>3</CRT></emit>'
            f'<dest><CNPJ>{receptor}</CNPJ><xNome>DESTINATARIO DE TESTE</xNome><indIEDest>1</indIEDest></dest>'
            f'<det nItem="1"><prod><cProd>001</cProd><cEAN>SEM GTIN</cEAN><xProd>Mercadoria</xProd><NCM>84713012</NCM><CFOP>5102</CFOP>'
            f'<uCom>UN</uCom><qCom>1.0000</qCom><vUnCom>{vnf:.2f}</vUnCom><vProd>{vnf:.2f}</vProd><cEANTrib>SEM GTIN</cEANTrib><uTrib>UN</uTrib>'
            f'<qTrib>1.0000</qTrib><vUnTrib>{vnf:.2f}</vUnTrib><indTot>1</indTot></prod>'
            f'<imposto><ICMS><ICMS00><orig>0</orig><CST>00</CST><modBC>3</modBC><vBC>{vnf:.2f}</vBC><pICMS>{alic:.2f}</pICMS><vICMS>{icms:.2f}</vICMS></ICMS00></ICMS>'
            f'<PIS><PISAliq><CST>01</CST><vBC>{vnf:.2f}</vBC><pPIS>0.65</pPIS><vPIS>{pis:.2f}</vPIS></PISAliq></PIS>'
            f'<COFINS><COFINSAliq><CST>01</CST><vBC>{vnf:.2f}</vBC><pCOFINS>3.00</pCOFINS><vCOFINS>{cofins:.2f}</vCOFINS></COFINSAliq></COFINS></imposto></det>'
            f'<total><ICMSTot><vBC>{vnf:.2f}</vBC><vICMS>{icms:.2f}</vICMS><vICMSDeson>0.00</vICMSDeson><vFCP>0.00</vFCP><vBCST>0.00</vBCST><vST>0.00</vST>'
            f'<vFCPST>0.00</vFCPST><vFCPSTRet>0.00</vFCPSTRet><vProd>{vnf:.2f}</vProd><vFrete>0.00</vFrete><vSeg>0.00</vSeg><vDesc>0.00</vDesc><vII>0.00</vII>'
            f'<vIPI>0.00</vIPI><vIPIDevol>0.00</vIPIDevol><vPIS>{pis:.2f}</vPIS><vCOFINS>{cofins:.2f}</vCOFINS><vOutro>0.00</vOutro><vNF>{vnf:.2f}</vNF></ICMSTot></total>'
            '<transp><modFrete>9</modFrete></transp><pag><detPag><tPag>15</tPag><vPag>' f'{vnf:.2f}' '</vPag></detPag></pag></infNFe></NFe>'
            f'<protNFe versao="4.00"><infProt><tpAmb>1</tpAmb><chNFe>{ch}</chNFe><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo></infProt></protNFe>'
            '</nfeProc>')


def cuit(prefijo: int, dni: int) -> str:
    """Un CUIT de once dígitos con su dígito verificador por módulo 11 (pesos 5, 4, 3, 2, 7, 6, 5, 4,
    3, 2), para que el material tenga la forma de uno real. Un número cuyo dígito sería 10 se salta.
    Ninguno corresponde a una empresa."""
    while True:
        base = f"{prefijo:02d}{dni:08d}"
        r = 11 - sum(int(c) * w for c, w in zip(base, (5, 4, 3, 2, 7, 6, 5, 4, 3, 2))) % 11
        if r != 10:
            return base + str(0 if r == 11 else r)
        dni += 1


def factura_wsfe(pto: int, nro: int, fecha_: str, emisor: str, receptor: str, neto: float, iva: float,
                 tributos: float = 0.0, tipo: int = 1, cae: str | None = None) -> str:
    """Un comprobante de ARCA como lo archiva el ERP: la solicitud FECAESolicitar y su respuesta con el
    CAE, en un solo archivo (F-24, p. 26 a 37), para las pruebas y el material. Factura A (CbteTipo 1)
    a un CUIT (DocTipo 80), con el IVA al 21 % (AlicIva Id 5, p. 77)."""
    f = fecha_.replace("-", "")
    total = round(neto + iva + tributos, 2)
    cae = cae or f"{(int(emisor[-6:]) * 7919 + nro * 104729) % 10**14:014d}"
    trib = (f"<ar:Tributos><ar:Tributo><ar:Id>99</ar:Id><ar:Desc>Ingresos brutos</ar:Desc><ar:BaseImp>{neto:.2f}</ar:BaseImp>"
            f"<ar:Alic>{round(100 * tributos / neto, 2) if neto else 0}</ar:Alic><ar:Importe>{tributos:.2f}</ar:Importe></ar:Tributo></ar:Tributos>") if tributos else ""
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<ComprobanteAutorizado xmlns:ar="http://ar.gov.afip.dif.FEV1/">'
            f'<ar:FECAESolicitar><ar:Auth><ar:Cuit>{emisor}</ar:Cuit></ar:Auth><ar:FeCAEReq>'
            f'<ar:FeCabReq><ar:CantReg>1</ar:CantReg><ar:PtoVta>{pto}</ar:PtoVta><ar:CbteTipo>{tipo}</ar:CbteTipo></ar:FeCabReq>'
            f'<ar:FeDetReq><ar:FECAEDetRequest><ar:Concepto>1</ar:Concepto><ar:DocTipo>80</ar:DocTipo><ar:DocNro>{receptor}</ar:DocNro>'
            f'<ar:CbteDesde>{nro}</ar:CbteDesde><ar:CbteHasta>{nro}</ar:CbteHasta><ar:CbteFch>{f}</ar:CbteFch>'
            f'<ar:ImpTotal>{total:.2f}</ar:ImpTotal><ar:ImpTotConc>0</ar:ImpTotConc><ar:ImpNeto>{neto:.2f}</ar:ImpNeto><ar:ImpOpEx>0</ar:ImpOpEx>'
            f'<ar:ImpTrib>{tributos:.2f}</ar:ImpTrib><ar:ImpIVA>{iva:.2f}</ar:ImpIVA><ar:MonId>PES</ar:MonId><ar:MonCotiz>1</ar:MonCotiz>'
            f'<ar:CondicionIVAReceptorId>1</ar:CondicionIVAReceptorId>{trib}'
            f'<ar:Iva><ar:AlicIva><ar:Id>5</ar:Id><ar:BaseImp>{neto:.2f}</ar:BaseImp><ar:Importe>{iva:.2f}</ar:Importe></ar:AlicIva></ar:Iva>'
            '</ar:FECAEDetRequest></ar:FeDetReq></ar:FeCAEReq></ar:FECAESolicitar>'
            f'<FECAESolicitarResponse><FECAESolicitarResult><FeCabResp><Cuit>{emisor}</Cuit><PtoVta>{pto}</PtoVta><CbteTipo>{tipo}</CbteTipo>'
            f'<FchProceso>{f}</FchProceso><CantReg>1</CantReg><Resultado>A</Resultado><Reproceso>N</Reproceso></FeCabResp>'
            f'<FeDetResp><FEDetResponse><Concepto>1</Concepto><DocTipo>80</DocTipo><DocNro>{receptor}</DocNro><CbteDesde>{nro}</CbteDesde>'
            f'<CbteHasta>{nro}</CbteHasta><Resultado>A</Resultado><CAE>{cae}</CAE><CbteFch>{f}</CbteFch><CAEFchVto>{f}</CAEFchVto>'
            '</FEDetResponse></FeDetResp></FECAESolicitarResult></FECAESolicitarResponse></ComprobanteAutorizado>')


def ruc_pa(n: int) -> str:
    """Un RUC de persona jurídica de Panamá, ficticio, con la forma tomo-folio-asiento. Su dígito
    verificador va en su propio campo (B3013, p. 74) y el lector no lo valida. Ninguno corresponde a
    una empresa."""
    return f"155{n % 1000000:06d}-2-{2010 + n % 15}"


def factura_dgipa(pto: str, nro: int, fecha_: str, emisor: str, receptor: str, neto: float, itbms: float) -> str:
    """Una factura electrónica de Panamá, de operación interna (iDoc 01), con lo que procesa el lector
    (F-27, p. 70 a 83), para las pruebas y el material. El CUFE de prueba es un número de 64 dígitos
    que sale de sus datos; su regla completa (6.1) no se valida en esta versión."""
    cufe = hashlib.sha256(f"{pto}{nro}{emisor}{fecha_}".encode()).hexdigest()
    cufe = "".join(str(int(c, 16) % 10) for c in cufe)
    total = round(neto + itbms, 2)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rFE xmlns="http://dgi-fep.mef.gob.pa"><dVerForm>1.00</dVerForm>'
            f'<dId>FE{cufe}</dId><gDGen><iAmb>1</iAmb><iTpEmis>01</iTpEmis><iDoc>01</iDoc><dNroDF>{nro:010d}</dNroDF>'
            f'<dPtoFacDF>{pto}</dPtoFacDF><dSeg>{nro * 7919 % 999999999:09d}</dSeg><dFechaEm>{fecha_}T10:00:00-05:00</dFechaEm>'
            f'<gEmis><gRucEmi><dTipoRuc>2</dTipoRuc><dRuc>{emisor}</dRuc><dDV>45</dDV></gRucEmi><dNombEm>EMISOR DE PRUEBA</dNombEm></gEmis>'
            f'<gDatRec><iTipoRec>01</iTipoRec><gRucRec><dTipoRuc>2</dTipoRuc><dRuc>{receptor}</dRuc><dDV>12</dDV></gRucRec>'
            '<dNombRec>RECEPTOR DE PRUEBA</dNombRec><cPaisRec>PA</cPaisRec></gDatRec></gDGen>'
            f'<gItem><dSecItem>1</dSecItem><dDescProd>Servicio</dDescProd><dCantCodInt>1</dCantCodInt>'
            f'<gPrecios><dPrUnit>{neto:.2f}</dPrUnit><dPrItem>{neto:.2f}</dPrItem><dValTotItem>{total:.2f}</dValTotItem></gPrecios>'
            f'<gITBMSItem><dTasaITBMS>01</dTasaITBMS><dValITBMS>{itbms:.2f}</dValITBMS></gITBMSItem></gItem>'
            f'<gTot><dTotNeto>{neto:.2f}</dTotNeto><dTotITBMS>{itbms:.2f}</dTotITBMS><dTotGravado>{itbms:.2f}</dTotGravado>'
            f'<dVTot>{total:.2f}</dVTot><dTotRec>{total:.2f}</dTotRec><iPzPag>2</iPzPag><dNroItems>1</dNroItems><dVTotItems>{total:.2f}</dVTotItems></gTot></rFE>')


def cedula_cr(n: int) -> str:
    """Una cédula jurídica de Costa Rica ficticia, de diez caracteres, con el prefijo 3-101 de las
    sociedades anónimas (F-34, nota 4). Ninguna corresponde a una empresa."""
    return f"3101{n % 1000000:06d}"


def rtn_hn(n: int) -> str:
    """Un RTN ficticio de catorce dígitos para el material de Honduras: el motor no valida su forma,
    porque el Acuerdo 481-2017 no la define; solo lo compara entre la factura y los libros."""
    return f"0801{n % 10**10:010d}"


def cai_hn(semilla: str) -> str:
    """Una CAI ficticia: «serie alfanumérica» (F-37, art. 3, def. 7), en seis grupos."""
    h = hashlib.sha1(semilla.encode()).hexdigest().upper()
    return "-".join([h[0:6], h[6:12], h[12:18], h[18:24], h[24:30], h[30:32]])


def factura_cr(consecutivo: str, fecha_: str, emisor: str, receptor: str, base: float, iva: float) -> str:
    """Una factura electrónica de Costa Rica en la versión 4.4, con lo que procesa el lector (F-34),
    para las pruebas y el material. La clave tiene sus cincuenta posiciones: el país, la fecha, la
    cédula del emisor en doce, el consecutivo, la situación y el código de seguridad."""
    a, m, dd = fecha_[2:4], fecha_[5:7], fecha_[8:10]
    seguridad = f"{int(hashlib.sha256(f'{emisor}{consecutivo}'.encode()).hexdigest(), 16) % 10**8:08d}"
    clave = f"506{dd}{m}{a}{emisor.zfill(12)}{consecutivo}1{seguridad}"
    total = round(base + iva, 2)
    ns = "https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.4/facturaElectronica"
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<FacturaElectronica xmlns="{ns}">'
            f'<Clave>{clave}</Clave><ProveedorSistemas>{emisor}</ProveedorSistemas><CodigoActividadEmisor>620100</CodigoActividadEmisor>'
            f'<NumeroConsecutivo>{consecutivo}</NumeroConsecutivo><FechaEmision>{fecha_}T10:00:00-06:00</FechaEmision>'
            f'<Emisor><Nombre>EMISOR DE PRUEBA</Nombre><Identificacion><Tipo>02</Tipo><Numero>{emisor}</Numero></Identificacion></Emisor>'
            f'<Receptor><Nombre>RECEPTOR DE PRUEBA</Nombre><Identificacion><Tipo>02</Tipo><Numero>{receptor}</Numero></Identificacion></Receptor>'
            '<CondicionVenta>01</CondicionVenta><DetalleServicio><LineaDetalle><NumeroLinea>1</NumeroLinea><Cantidad>1</Cantidad>'
            f'<UnidadMedida>Sp</UnidadMedida><Detalle>Servicio</Detalle><PrecioUnitario>{base:.5f}</PrecioUnitario><MontoTotal>{base:.5f}</MontoTotal>'
            f'<SubTotal>{base:.5f}</SubTotal><BaseImponible>{base:.5f}</BaseImponible><Impuesto><Codigo>01</Codigo><CodigoTarifaIVA>08</CodigoTarifaIVA>'
            f'<Tarifa>13</Tarifa><Monto>{iva:.5f}</Monto></Impuesto><ImpuestoNeto>{iva:.5f}</ImpuestoNeto><MontoTotalLinea>{total:.5f}</MontoTotalLinea>'
            '</LineaDetalle></DetalleServicio><ResumenFactura><CodigoTipoMoneda><CodigoMoneda>CRC</CodigoMoneda><TipoCambio>1</TipoCambio></CodigoTipoMoneda>'
            f'<TotalServGravados>{base:.5f}</TotalServGravados><TotalGravado>{base:.5f}</TotalGravado><TotalVenta>{base:.5f}</TotalVenta>'
            f'<TotalVentaNeta>{base:.5f}</TotalVentaNeta><TotalImpuesto>{iva:.5f}</TotalImpuesto><TotalComprobante>{total:.5f}</TotalComprobante>'
            '</ResumenFactura></FacturaElectronica>')


def nit_gt(n: int) -> str:
    """Un NIT de Guatemala ficticio, con un último carácter calculado por módulo 11 (10 es K) para que
    tenga la forma de uno real. El lector no lo valida. Ninguno corresponde a una empresa."""
    base = str(n)
    r = (11 - sum(int(c) * (i + 2) for i, c in enumerate(reversed(base))) % 11) % 11
    return base + ("K" if r == 10 else str(r))


def factura_fel(serie: str, numero_: int, fecha_: str, emisor: str, receptor: str, base: float, iva: float) -> str:
    """Una FEL de Guatemala, factura (FACT), certificada, con lo que procesa el lector (F-30), para las
    pruebas y el material. El gran total trae el IVA adentro."""
    total = round(base + iva, 2)
    uuid = hashlib.sha256(f"{serie}{numero_}{emisor}".encode()).hexdigest().upper()
    uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:32]}"
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<dte:GTDocumento xmlns:dte="http://www.sat.gob.gt/dte/fel/0.2.0" Version="0.1">'
            '<dte:SAT ClaseDocumento="dte"><dte:DTE ID="DatosCertificados"><dte:DatosEmision ID="DatosEmision">'
            f'<dte:DatosGenerales Tipo="FACT" FechaHoraEmision="{fecha_}T10:00:00-06:00" CodigoMoneda="GTQ"/>'
            f'<dte:Emisor NITEmisor="{emisor}" NombreEmisor="EMISOR DE PRUEBA" CodigoEstablecimiento="1" AfiliacionIVA="GEN"/>'
            f'<dte:Receptor IDReceptor="{receptor}" NombreReceptor="RECEPTOR DE PRUEBA"/>'
            '<dte:Items><dte:Item NumeroLinea="1" BienOServicio="S"><dte:Cantidad>1</dte:Cantidad><dte:Descripcion>Servicio</dte:Descripcion>'
            f'<dte:PrecioUnitario>{total:.2f}</dte:PrecioUnitario><dte:Precio>{total:.2f}</dte:Precio><dte:Descuento>0</dte:Descuento>'
            f'<dte:Impuestos><dte:Impuesto><dte:NombreCorto>IVA</dte:NombreCorto><dte:CodigoUnidadGravable>1</dte:CodigoUnidadGravable>'
            f'<dte:MontoGravable>{base:.2f}</dte:MontoGravable><dte:MontoImpuesto>{iva:.2f}</dte:MontoImpuesto></dte:Impuesto></dte:Impuestos>'
            f'<dte:Total>{total:.2f}</dte:Total></dte:Item></dte:Items>'
            f'<dte:Totales><dte:TotalImpuestos><dte:TotalImpuesto NombreCorto="IVA" TotalMontoImpuesto="{iva:.2f}"/></dte:TotalImpuestos>'
            f'<dte:GranTotal>{total:.2f}</dte:GranTotal></dte:Totales></dte:DatosEmision></dte:DTE>'
            f'<dte:Certificacion><dte:NITCertificador>12521337</dte:NITCertificador><dte:NombreCertificador>CERTIFICADOR DE PRUEBA</dte:NombreCertificador>'
            f'<dte:NumeroAutorizacion Serie="{serie}" Numero="{numero_}">{uuid}</dte:NumeroAutorizacion>'
            f'<dte:FechaHoraCertificacion>{fecha_}T10:00:05-06:00</dte:FechaHoraCertificacion></dte:Certificacion></dte:SAT></dte:GTDocumento>')


def rfc(letras: str, fecha_: str, homoclave: str) -> str:
    """Un RFC de persona moral ficticio, de 12 posiciones (F-19, p. 15). Ninguno corresponde a una empresa."""
    return f"{letras[:3].upper()}{fecha_}{homoclave[:3].upper()}"


def rut(cuerpo: int) -> str:
    """Un RUT con su dígito verificador por módulo 11 (factores 2 a 7 de derecha a izquierda; 10 es K
    y 11 es 0), para que el material tenga la forma de uno real. Ninguno corresponde a una empresa."""
    total, f = 0, 2
    for ch in reversed(str(cuerpo)):
        total += int(ch) * f
        f = 2 if f == 7 else f + 1
    r = 11 - total % 11
    return f"{cuerpo}-{ {10: 'K', 11: '0'}.get(r, str(r)) }"


def factura_sii(folio: str, fecha_: str, emisor: str, receptor: str, neto: float, iva: float) -> str:
    """Un DTE del SII, factura electrónica (tipo 33), con lo que procesa el lector (F-16), para las
    pruebas y el material. Los montos van en pesos enteros."""
    n, i = round(neto), round(iva)
    return ('<?xml version="1.0" encoding="ISO-8859-1"?>\n<DTE version="1.0" xmlns="http://www.sii.cl/SiiDte"><Documento ID="F' + folio + 'T33">'
            f'<Encabezado><IdDoc><TipoDTE>33</TipoDTE><Folio>{folio}</Folio><FchEmis>{fecha_}</FchEmis></IdDoc>'
            f'<Emisor><RUTEmisor>{emisor}</RUTEmisor><RznSoc>Emisor de prueba</RznSoc></Emisor>'
            f'<Receptor><RUTRecep>{receptor}</RUTRecep><RznSocRecep>Receptor de prueba</RznSocRecep></Receptor>'
            f'<Totales><MntNeto>{n}</MntNeto><TasaIVA>19</TasaIVA><IVA>{i}</IVA><MntTotal>{n + i}</MntTotal></Totales>'
            '</Encabezado></Documento></DTE>')


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
    # Las rutas de la configuración no dependen de dónde esté parada la sesión.
    import os
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        raiz_t = Path(t).resolve()
        c = raiz_t / ".criterio" / "finanzas" / "1" / "config.json"
        N.escribir_json(c, {"paths": {"documents": "docs", "state": "estado"}})
        (raiz_t / "otra").mkdir()
        antes = os.getcwd()
        os.chdir(raiz_t / "otra")
        try:
            cfg_t, _ = N.cargar_config(c)
        finally:
            os.chdir(antes)
        ok("rutas desde la carpeta de .criterio, no desde la sesión", (cfg_t["_docs"], cfg_t["_estado"]), (raiz_t / "docs", raiz_t / "estado"))
    # El ejemplo de la ficha técnica del SRI (F-09): la clave 2110201101179214673900110020010000000011234567813
    ok("módulo 11 del ejemplo del SRI", digito_mod11("211020110117921467390011002001000000001123456781"), 3)
    # El registro único de países: la factura tiene un lector por cada país del registro, y un
    # país fuera del registro se rechaza con la lista de los que sí están.
    ok("la factura cubre los países del registro", sorted(FACTURA), sorted(N.PAISES))
    ok("un país fuera del registro se rechaza", N.revisar_pais({"country": "XX"}), [f"entity.country debe ser uno de {', '.join(N.PAISES)} en esta versión"])
    ok("un país del registro pasa", N.revisar_pais({"country": "ec"}), [])
    for c, p in N.PAISES.items():
        _PAIS[0] = c
        ok(f"las cifras de {p['nombre']['es']} llevan su separador decimal", mon(1234567.891)[-3], p["decimal"])
    _PAIS[0] = N.POR_OMISION
    ok("cada lector de factura es de un país del registro", sorted(PAIS_DEL_LECTOR.values()), sorted(N.PAISES))
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
        x.write_text(factura_sunat("F001-00000123", "2026-09-15", "20123456789", "20987654321", 1000.0, 180.0), encoding="utf-8")
        f = leer_factura(x)
        ok("SUNAT: factura UBL 2.1 con su IGV", (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["total"], f["fecha"]),
           ("sunat", "factura", "F001-00000123", "20123456789", "20987654321", 1000.0, 180.0, 1180.0, "2026-09-15"))
        ok("SUNAT: el comprobante se identifica por RUC, tipo, serie y número", f["id"], "20123456789-01-F001-00000123")
        x.write_text(factura_sii("1234", "2026-09-15", rut(76123456), rut(77654321), 1000000, 190000), encoding="iso-8859-1")
        f = leer_factura(x)
        ok("SII: el DTE tipo 33 con su IVA, en pesos enteros", (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["total"], f["fecha"]),
           ("sii", "factura", "1234", "761234560", "776543217", 1000000.0, 190000.0, 1190000.0, "2026-09-15"))
        ok("SII: el documento se identifica por RUT, tipo y folio", f["id"], "761234560-33-1234")
        ok("SII: el dígito verificador K", rut(10000013), "10000013-K")
        x.write_text(factura_sat("A", "1001", "2026-09-15", rfc("ABC", "260101", "AA1"), rfc("XYZ", "250505", "BB2"), 10000.0, 1600.0), encoding="utf-8")
        f = leer_factura(x)
        ok("SAT: el CFDI 4.0 de ingreso con su IVA", (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["total"], f["fecha"]),
           ("sat", "factura", "A1001", "ABC260101AA1", "XYZ250505BB2", 10000.0, 1600.0, 11600.0, "2026-09-15"))
        ok("SAT: el CFDI se identifica por el RFC del emisor, la serie y el folio", f["id"], "ABC260101AA1-A1001")
        f = leer_factura_texto(factura_nfe("1", "4521", "2026-09-15", cnpj(12345678), cnpj(87654321), 8200.0, 1800.0, 65.0, 300.0), t)
        ok("NF-e: modelo 55 de salida, con el ICMS dentro del valor de la nota",
           (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["otros_impuestos"], f["total"], f["fecha"]),
           ("nfe", "factura", "1-4521", cnpj(12345678), cnpj(87654321), 8200.0, 1800.0, 365.0, 10000.0, "2026-09-15"))
        ok("NF-e: se identifica por su chave de acesso, de 44 dígitos, con el CNPJ del emitente adentro",
           (len(f["id"]), f["id"][6:20] == cnpj(12345678)), (44, True))
        ok("NF-e: una de entrada se identifica y no cruza valores",
           leer_factura_texto(factura_nfe("1", "9", "2026-09-15", cnpj(12345678), cnpj(87654321), 82.0, 18.0).replace("<tpNF>1</tpNF>", "<tpNF>0</tpNF>"), t)["valores"], False)
        ok("CNPJ: sus dos dígitos verificadores por módulo 11, como en 11.222.333/0001-81", cnpj(11222333), "11222333000181")
        f = leer_factura_texto(factura_wsfe(12, 4521, "2026-09-15", cuit(30, 71234567), cuit(30, 50001234), 10000.0, 2100.0, 150.0), t)
        ok("ARCA: la factura A con su IVA al 21 % y un tributo, aprobada",
           (f["lector"], f["tipo"], f["numero"], f["receptor"], f["base"], f["iva"], f["otros_impuestos"], f["total"], f["fecha"], f["valores"]),
           ("wsfe", "factura", "00012-00004521", cuit(30, 50001234), 10000.0, 2100.0, 150.0, 12250.0, "2026-09-15", True))
        ok("ARCA: se identifica por su CAE, de 14 dígitos", len(f["id"]), 14)
        ok("ARCA: una nota de crédito A se identifica y no cruza valores",
           leer_factura_texto(factura_wsfe(12, 7, "2026-09-15", cuit(30, 71234567), cuit(30, 50001234), 100.0, 21.0, tipo=3), t)[["tipo", "valores"][0]], "nota_credito")
        ok("ARCA: un comprobante rechazado no cruza valores",
           leer_factura_texto(factura_wsfe(12, 8, "2026-09-15", cuit(30, 71234567), cuit(30, 50001234), 100.0, 21.0).replace(
               "<Resultado>A</Resultado><CAE>", "<Resultado>R</Resultado><CAE>"), t)["valores"], False)
        ok("CUIT: el dígito verificador por módulo 11, como en 20-11111111-2", cuit(20, 11111111), "20111111112")
        f = leer_factura_texto(factura_dgipa("001", 4521, "2026-09-15", ruc_pa(101), ruc_pa(202), 10000.0, 700.0), t)
        ok("DGI de Panamá: la factura de operación interna con su ITBMS",
           (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["total"], f["fecha"], f["valores"]),
           ("dgipa", "factura", "001-0000004521", ident(ruc_pa(101)), ident(ruc_pa(202)), 10000.0, 700.0, 10700.0, "2026-09-15", True))
        ok("DGI de Panamá: se identifica por su CUFE, sin el literal FE", (len(f["id"]), f["id"].isdigit()), (64, True))
        f = leer_factura_texto(factura_fel("A1B2C3D4", 123456, "2026-09-15", nit_gt(1234567), nit_gt(7654321), 10000.0, 1200.0), t)
        ok("FEL de Guatemala: la factura certificada, con el IVA dentro del gran total",
           (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["total"], f["fecha"], f["valores"]),
           ("fel", "factura", "A1B2C3D4-123456", ident(nit_gt(1234567)), ident(nit_gt(7654321)), 10000.0, 1200.0, 11200.0, "2026-09-15", True))
        ok("FEL de Guatemala: se identifica por el UUID de su autorización", len(f["id"]), 36)
        f = leer_factura_texto(factura_cr("00100001010000004521", "2026-09-15", cedula_cr(101), cedula_cr(202), 10000.0, 1300.0), t)
        ok("Costa Rica 4.4: la factura electrónica, con la venta neta, el impuesto y el total",
           (f["lector"], f["tipo"], f["numero"], f["emisor"], f["receptor"], f["base"], f["iva"], f["total"], f["fecha"], f["valores"]),
           ("cr", "factura", "00100001010000004521", ident(cedula_cr(101)), ident(cedula_cr(202)), 10000.0, 1300.0, 11300.0, "2026-09-15", True))
        ok("Costa Rica 4.4: se identifica por su clave de cincuenta posiciones", (len(f["id"]), f["id"][:3]), (50, "506"))
        nc = factura_cr("00100001030000000007", "2026-09-15", cedula_cr(101), cedula_cr(202), 10.0, 1.3).replace("FacturaElectronica", "NotaCreditoElectronica")
        ok("Costa Rica 4.4: la nota de crédito se identifica y no cruza valores", (leer_factura_texto(nc, t)["tipo"], leer_factura_texto(nc, t)["valores"]), ("nota de crédito", False))
        hn = {"number": "000-001-01-00000120", "cai": "3E5A1C-7B2D90-4F11A8-0C6E3B-92D4F7-11", "date": "2026-09-15",
              "authorized_range": {"from": "000-001-01-00000001", "to": "000-001-01-00000500"}, "issue_deadline": "2026-12-31",
              "issuer_rtn": "08019002265431", "customer_rtn": "08019010017725", "taxable": 10000.0, "isv": 1500.0, "total": 11500.0}
        f = _hn(hn, 0.01)
        ok("Honduras: la factura desde la ficha, dentro de su autorización",
           (f["lector"], f["tipo"], f["numero"], f["base"], f["iva"], f["total"], f["fecha"], f["fuera"], f["id"].endswith(":000-001-01-00000120")),
           ("hn", "factura", "000-001-01-00000120", 10000.0, 1500.0, 11500.0, "2026-09-15", [], True))
        ok("Honduras: fuera del rango autorizado y emitida después de la fecha límite",
           len(_hn({**hn, "number": "000-001-01-00000501", "date": "2027-01-02"}, 0.01)["fuera"]), 2)
        ok("Honduras: otro establecimiento no está en el rango", len(_hn({**hn, "number": "001-001-01-00000120"}, 0.01)["fuera"]), 1)
        ok("Honduras: un correlativo sin la forma del artículo 10 no se procesa", "error" in _hn({**hn, "number": "0001-01-120"}, 0.01), True)
        ok("Honduras: un tipo distinto de 01 se identifica y no cruza", _hn({**hn, "number": "000-001-03-00000007"}, 0.01).get("solo"), True)
        ok("Honduras: un ISV que no es el 15 % de lo gravado vuelve a la extracción", "error" in _hn({**hn, "isv": 1300.0}, 0.01), True)
        ok("Honduras: sin CAI ni rango no se procesa", "error" in _hn({**hn, "cai": ""}, 0.01), True)
        ok("Honduras: la ficha lleva las facturas por el RTN del emisor y su número correlativo",
           (revisar_ficha_cierre({"invoices": {"08019002265431:000-001-01-00000121": {**hn, "source": "x.pdf"}}})[0].startswith("invoices[08019002265431:000-001-01-00000121]"),
            revisar_ficha_cierre({"invoices": {"08019002265431:000-001-01-00000120": {**hn, "source": "x.pdf"}}})), (True, []))
        ok("SAT: un CFDI de otra versión no se lee como 4.0", "error" in leer_factura_texto(factura_sat("A", "1", "2026-09-15", "ABC260101AA1", "XYZ250505BB2", 1, 0.16).replace('Version="4.0"', 'Version="3.3"'), t), True)
        ok("la DIAN sigue siendo la DIAN", leer_factura_texto(factura_dian("SETP1", "c" * 96, "2026-09-10", "900123456", "800765432", 10, 1.9), t)["lector"], "dian")
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
        ok("las cuentas que cruzan salen de los datos: la base, el IVA, y no la contrapartida",
           {k: [x["prefijo"] for x in v] for k, v in cuentas_de_factura(docs, "2026-09").items()},
           {"sales": ["4135"], "vat_generated": ["2408"], "purchases": [], "vat_deductible": []})
        b = r["partes"]["bank-reconcile"]["cuentas"][0]
        ok("banco: los intereses quedan como nota crédito sin registrar", (b["notas_credito_sin_registrar"], b["diferencia_sin_explicar"]), (12.0, 0.0))
        # El mismo extracto, como lo entrega el banco: un PDF con texto y las cifras con punto de miles.
        exc = p / "20-bancos" / "andino-1234" / "extracto.csv"
        guardado = exc.read_bytes()
        exc.unlink()
        N._pdf_tabla(exc.with_suffix(".pdf"), ["Banco Andino · Extracto", "Cuenta 1234 · 2026-09"],
                     [["Fecha", "Referencia", "Descripción", "Valor", "Saldo"],
                      ["2026-09-12", "T-55", "Transferencia", "1.190.000,00", "1.191.000,00"],
                      ["2026-09-30", "", "Comisión", "-50,00", "1.190.950,00"],
                      ["2026-09-30", "", "Intereses", "12,00", "1.190.962,00"]],
                     [(40, "i"), (100, "i"), (170, "i"), (470, "d"), (555, "d")])
        if shutil.which("pdftotext"):
            bp = bancos(cfg, "2026-09")["cuentas"][0]
            ok("banco: el extracto en PDF da la misma conciliación que en CSV",
               {k: v for k, v in bp.items() if k != "abiertas"}, {k: v for k, v in b.items() if k != "abiertas"})
            ok("banco: cada partida del PDF cita el PDF y su fila", [(a["cita"]["archivo"], a["cita"]["fila"]) for a in bp["abiertas"]],
               [("2026-09/20-bancos/andino-1234/extracto.pdf", 4)])
        exc.with_suffix(".pdf").write_bytes(b"%PDF-1.4\n%%EOF\n")
        bp = bancos(cfg, "2026-09")
        ok("banco: un PDF sin texto no se adivina: queda en lo no procesado y sin señales", (bp["cuentas"], len(bp["no_procesado"]), bp["alertas"]),
           ([], 1, []))
        exc.with_suffix(".pdf").unlink()
        exc.write_bytes(guardado)
        ok("checklist: C-01 cumplida sin evidencia y C-02 vencida", sorted((a["signal"], a["key"]) for a in r["alertas"] if a["signal"].startswith("close_task")),
           [("close_task_done_without_evidence", "tarea:C-01"), ("close_task_overdue", "tarea:C-02")])
        ok("cartera sin auxiliar: conciliación desactualizada", any(a["signal"] == "reconciliation_stale" and a["key"] == "cuenta:1305" for a in r["alertas"]), True)
        ok("las señales esperadas, y ninguna otra", senales, ["bank_unreconciled", "close_task_done_without_evidence", "close_task_overdue", "reconciliation_stale"])
        md = reporte(r, "bank-reconcile", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        ok("el reporte dice la señal y el comando en palabras, con su código al lado",
           ("Hay movimientos del extracto sin su registro" in md and "(`bank_unreconciled`)" in md
            and md.startswith("# Conciliación bancaria") and "**Comando:** `bank-reconcile`" in md) if N.NOMBRES else True, True)

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
        ok("el acta citada no queda como escrito sin citar", [x for x in rt["record_issues"] if "acta-03" in x], [])
        (pr / "30-proyecciones").mkdir(parents=True, exist_ok=True)
        (pr / "30-proyecciones" / "correo-administracion.md").write_text("Vamos dentro del presupuesto.", encoding="utf-8")
        rt = tomas(cfg, "2026", "2026-09", dt.date(2026, 10, 6))
        ok("un correo de un área que la ficha no cita queda en record_issues (CFO-6)",
           [x.split(":")[0] for x in rt["record_issues"]], ["presupuesto-2026/30-proyecciones/correo-administracion.md"])
        ficha["reviewed"] = [{"source": "presupuesto-2026/30-proyecciones/correo-administracion.md", "note": "no dice nada del presupuesto"}]
        escribir_json(est / "presupuesto" / "2026" / "ficha.json", ficha)
        ok("anotado en reviewed con su motivo, deja de señalarse", tomas(cfg, "2026", "2026-09", dt.date(2026, 10, 6))["record_issues"], [])

        inv = inventario(docs, None, estructura(ESTRUCTURA))
        ok("inventario: nada fuera de la estructura en la entidad de prueba", inv["fuera_de_lugar"] if ESTRUCTURA.is_file() else [], [])

    # Áurea: la caja contra su mínimo y su proyección, los pagos contra quién puede aprobarlos y la
    # deuda contra su vencimiento y sus covenants, sobre una entidad mínima con todo mal.
    with tempfile.TemporaryDirectory() as t:
        docs, est = Path(t) / "docs", Path(t) / "estado"
        p = docs / "2026-09"
        _csv(p / "10-contabilidad" / "balance-comprobacion.csv", [["cuenta", "nombre", "debito", "credito", "saldo_final"],
             ["1105", "Caja", "0", "0", "300"], ["1305", "Clientes", "0", "0", "500"], ["2105", "Obligaciones financieras", "0", "0", "-450"],
             ["2205", "Proveedores", "0", "0", "-150"], ["3105", "Capital", "0", "0", "-200"]])
        _csv(p / "20-bancos" / "andino-1234" / "extracto.csv", [["fecha", "referencia", "descripcion", "valor", "saldo"],
             ["2026-09-01", "A", "Saldo", "1000", "1000"], ["2026-09-30", "B", "Pago", "-900", "100"]])
        _csv(p / "20-bancos" / "exterior-9001" / "extracto.csv", [["fecha", "referencia", "descripcion", "valor", "saldo"],
             ["2026-09-30", "C", "Saldo", "50", "50"]])
        _csv(docs / "00-referencia" / "politica-tesoreria.csv", [["concepto", "referencia", "valor"],
             ["caja_minima", "andino-1234", "200"], ["caja_minima", "consolidado", "300000"], ["aprobadores", "0", "1"],
             ["aprobadores", "1000", "2"], ["limite_exposicion", "USD", "100000"], ["tasa", "USD", "4000"]])
        _csv(docs / "00-referencia" / "matriz-firmas.csv", [["nombre", "cargo", "monto_maximo"], ["Ana Ruiz", "Tesorera", "5000"], ["Luis Mora", "Gerente", "50000"]])
        _csv(p / "60-tesoreria" / "programa-pagos.csv", [["id", "fecha", "beneficiario", "valor", "aprobado_por"],
             ["P-1", "2026-10-02", "Proveedor A", "800", "Ana Ruiz"], ["P-2", "2026-10-03", "Proveedor B", "3000", "Ana Ruiz"],
             ["P-3", "2026-10-03", "Proveedor C", "20000", "Ana Ruiz; Pedro Gil"]])
        _csv(p / "60-tesoreria" / "flujo-proyectado.csv", [["cuenta", "saldo_proyectado"], ["andino-1234", "400"]])
        _csv(docs / "00-referencia" / "registro-deuda.csv", [["obligacion", "tipo", "contraparte", "saldo", "vencimiento"],
             ["Crédito 01", "deuda", "Banco Uno", "450", "2026-10-20"], ["CDT 07", "inversion", "Banco Dos", "300", "2027-03-01"]])
        _csv(docs / "00-referencia" / "covenants.csv", [["obligacion", "indicador", "numerador", "denominador", "operador", "limite"],
             ["Crédito 01", "Razón corriente", "11;13", "21;22", ">=", "1.25"], ["Crédito 01", "Endeudamiento", "2", "1", "<=", "0.7"]])
        cfg = {"entity": {"id": "1", "name": "Prueba", "country": N.POR_OMISION, "currency": "COP"}, "period": "2026-09",
               "_docs": docs, "_estado": est, "treasury": {"currencies": {"exterior-9001": "USD"}}}
        ra = aurea(cfg, "2026-09", dt.date(2026, 10, 1))
        claves = sorted((a["signal"], a["key"]) for a in ra["alertas"])
        ok("Áurea: caja bajo el mínimo en la cuenta y en el consolidado",
           [k for s, k in claves if s == "cash_below_minimum"], ["caja:andino-1234", "caja:consolidado"])
        ok("Áurea: la caja real contra la proyectada", [k for s, k in claves if s == "cash_vs_forecast"], ["proyeccion:andino-1234"])
        ok("Áurea: la exposición en dólares, convertida con la tasa de la política", [k for s, k in claves if s == "fx_exposure_over_limit"], ["exposicion:USD"])
        ok("Áurea: el pago de 3.000 pide dos aprobaciones y tiene una",
           [k for s, k in claves if s == "payment_without_approval"], ["pago:P-2"])
        ok("Áurea: quien aprobó sin facultad o sin estar en la matriz",
           [k for s, k in claves if s == "signatory_without_authority"], ["firma:P-3:ana_ruiz", "firma:P-3:pedro_gil"])
        ok("Áurea: el crédito vence en 19 días; el CDT, no", [k for s, k in claves if s == "maturity_near"], ["vence:credito_01"])
        ok("Áurea: uno cerca del límite y otro que lo cruza, calculados desde el balance",
           [(c["indicador"], c["valor"], c["estado"]) for c in ra["partes"]["debt-watch"]["covenants"]],
           [("Razón corriente", 1.33, "en riesgo"), ("Endeudamiento", 0.75, "incumplido")])
        ok("Áurea: lo que vence va a la vista de Rostrum", [v["que"] for v in ra["vence"]], ["Crédito 01 · deuda"])
        md = reporte(ra, "payment-check", "0.0")
        ok("Áurea: el reporte nombra las señales del comando", "payment_without_approval" in md and "Áurea" in md, True)
        # Sin la moneda en la configuración, la del extracto: la exposición no depende de que alguien la diga (CFO-5).
        _csv(p / "20-bancos" / "exterior-9001" / "extracto.csv", [["fecha", "referencia", "descripcion", "valor", "saldo", "moneda"],
             ["2026-09-30", "C", "Saldo", "50", "50", "USD"]])
        cfg["treasury"] = {"currencies": {}}
        ra = aurea(cfg, "2026-09", dt.date(2026, 10, 1))
        ok("Áurea: la moneda del extracto cuando la configuración no la dice",
           [a["key"] for a in ra["alertas"] if a["signal"] == "fx_exposure_over_limit"], ["exposicion:USD"])

    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
