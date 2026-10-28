#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CSO: dos industrias por país y una entidad de control.

    python3 tests/criterio-cso/generar.py          escribe tests/criterio-cso/material/

Cada entidad trae su carpeta comercial al 5 de noviembre de 2026, con el periodo de octubre
cerrado: la tabla de etapas, las metas, la matriz de descuentos, la tabla de cuentas y el plan de
comisiones; tres exportaciones del CRM —el 1 y el 16 de octubre y el 3 de noviembre—, en el formato
de su CRM; el acta del comité comercial con el pronóstico comprometido; la evidencia de cada
oportunidad; las cotizaciones con su descuento y su aprobación; y la liquidación de comisiones de
octubre. Trae también, como las dejarían los otros agentes, las fichas de los contratos de Fidel
(`estado-legal/`) y las facturas emitidas de los cierres de septiembre y octubre de Clara
(`estado-finanzas/`).

Los formatos se reparten: Salesforce por API con su historial de campos, Salesforce desde un
informe con las fechas mes/día, HubSpot en CSV y en Excel, y dos CRM cualquiera con su mapeo de
columnas, uno en CSV y otro en Excel. Colombia y México, dos industrias y un control por país.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal
esperada queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los
documentos escritos: la evidencia de cada oportunidad, el pronóstico comprometido y cada
cotización. El motor no la ve; `evaluar.py` compara lo que el motor levanta contra ella, y una señal
de más cuenta igual que una de menos.

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: un
cierre que se corrió una sola vez, un descuento alto aprobado por un cargo superior, un contrato
firmado cuyo plazo de facturación todavía no vence, un proveedor sin factura —no es un cliente—, un
mejor escenario en el acta más alto que el comprometido, y un correo de contacto en un documento y
en una columna de la exportación que no entran a la ficha. Todo es determinista: el mismo material
cada vez, byte a byte. Los nombres, las cuentas y las cifras son sintéticos.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-sales" / "scripts"))
import ventas as V  # noqa: E402
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import formatos as FMT  # noqa: E402  (Word, Excel y PDF sin dependencias y con fecha fija, los mismos de las demás familias)

N = V.N
SALIDA = AQUI / "material"
HOY, PERIODO = dt.date(2026, 11, 5), "2026-10"
CORTES = [dt.date(2026, 10, 1), dt.date(2026, 10, 16), dt.date(2026, 11, 3)]

ETAPAS = [("Calificación", 1, 10, "", "abierta"), ("Propuesta", 2, 30, "propuesta", "abierta"), ("Negociación", 3, 60, "", "abierta"),
          ("Compromiso", 4, 80, "orden de compra", "abierta"), ("Ganada", 5, 100, "", "ganada"), ("Perdida", 6, 0, "", "perdida")]
PROB = {e[0]: e[2] for e in ETAPAS}
NIVELES = [("1", 10, "ninguno"), ("2", 20, "gerente comercial"), ("3", 30, "gerente general")]
TASA = 3.0

ENTIDADES = [
    {"carpeta": "retail-co", "industria": "retail", "pais": "CO", "id": "901234567", "nombre": "Almacenes del Valle", "moneda": "COP",
     "u": 10_000_000, "n0": 1100, "crm": "salesforce-api", "personas": ("Ana Ruiz", "Luis Mora", "Carla Peña"),
     "clientes": ["Grupo Éxito Andino S.A.", "Comercializadora Norte S.A.S.", "Distribuidora Sur S.A.S.", "Hoteles Caribe S.A.",
                  "Clínica Central S.A.S.", "Colegio Bilingüe S.A.S.", "Constructora Andes S.A.S."],
     "siembra": ["etapa_sin_evidencia", "cierre_historial", "pronostico_sin_respaldo", "descuento_sin_aprobacion", "ganado_sin_contrato"]},
    {"carpeta": "tecnologia-co", "industria": "tecnologia", "pais": "CO", "id": "900876543", "nombre": "Soluciones Digitales Andinas", "moneda": "COP",
     "u": 8_000_000, "n0": 1200, "crm": "hubspot-csv", "personas": ("Diego Lara", "Paula Vega", "Sergio Niño"),
     "clientes": ["Banco Montaña S.A.", "Aseguradora Centro S.A.", "Telecomunicaciones Llano S.A.S.", "Universidad del Río",
                  "Logística Express S.A.S.", "Energía Verde S.A. E.S.P.", "Laboratorios Pacífico S.A."],
     "siembra": ["detenida", "meta_lejos", "firmado_sin_factura", "comision_distinta", "cierre_cortes"]},
    {"carpeta": "control-co", "industria": "retail", "pais": "CO", "id": "900000002", "nombre": "Comercial Control Andina", "moneda": "COP",
     "u": 6_000_000, "n0": 1300, "crm": "generico-csv", "personas": ("Elena Duarte", "Jorge Silva", "Natalia Rincón"),
     "clientes": ["Cliente Control Uno S.A.S.", "Cliente Control Dos S.A.S.", "Cliente Control Tres S.A.", "Cliente Control Cuatro S.A.S.",
                  "Cliente Control Cinco S.A.S.", "Cliente Control Seis S.A.", "Cliente Control Siete S.A.S."],
     "siembra": []},
    {"carpeta": "manufactura-mx", "industria": "manufactura", "pais": "MX", "id": "MBA120315KT4", "nombre": "Manufacturas del Bajío", "moneda": "MXN",
     "u": 120_000, "n0": 1400, "crm": "salesforce-informe", "personas": ("Mariana Soto", "Rodrigo Ibarra", "Lucía Treviño"),
     "clientes": ["Automotriz Norte S.A. de C.V.", "Electrodomésticos del Centro S.A. de C.V.", "Empaques Querétaro S.A. de C.V.",
                  "Ferretera Nacional S.A. de C.V.", "Agroindustrias Jalisco S.A. de C.V.", "Plásticos Monterrey S.A. de C.V.",
                  "Construcciones Puebla S.A. de C.V."],
     "siembra": ["detenida", "etapa_sin_evidencia", "meta_lejos", "firmado_sin_factura", "descuento_fuera_de_matriz"]},
    {"carpeta": "servicios-mx", "industria": "servicios", "pais": "MX", "id": "SPM140708QJ2", "nombre": "Servicios Profesionales Mexicanos", "moneda": "MXN",
     "u": 90_000, "n0": 1500, "crm": "generico-xlsx", "personas": ("Fernando Ruiz", "Daniela Ochoa", "Alberto Cano"),
     "clientes": ["Grupo Financiero Azteca S.A.", "Hospitales del Norte S.A. de C.V.", "Retail Moderno S.A. de C.V.", "Minera Sonora S.A. de C.V.",
                  "Transportes Bajío S.A. de C.V.", "Alimentos Yucatán S.A. de C.V.", "Turismo Riviera S.A. de C.V."],
     "siembra": ["pronostico_sin_respaldo", "ganado_sin_contrato", "comision_distinta", "cierre_cortes"]},
    {"carpeta": "control-mx", "industria": "servicios", "pais": "MX", "id": "CCM101010AB3", "nombre": "Comercial Control de México", "moneda": "MXN",
     "u": 70_000, "n0": 1600, "crm": "hubspot-xlsx", "personas": ("Isabel Méndez", "Óscar Delgado", "Teresa Fuentes"),
     "clientes": ["Cliente Control Norte S.A. de C.V.", "Cliente Control Centro S.A. de C.V.", "Cliente Control Sur S.A. de C.V.",
                  "Cliente Control Golfo S.A. de C.V.", "Cliente Control Pacífico S.A. de C.V.", "Cliente Control Bajío S.A. de C.V.",
                  "Cliente Control Occidente S.A. de C.V."],
     "siembra": []},
]


def tid(e: dict, i: int) -> str:
    """La identificación fiscal de un cliente con la forma de su país: un NIT de nueve dígitos o un
    RFC de persona moral de doce posiciones. Ninguno corresponde a una empresa."""
    if e["pais"] == "MX":
        return f"C{e['carpeta'][:2].upper()}{10 + i:02d}0{1 + i % 9}{1 + i:02d}{chr(65 + i)}{i}{i % 7}"
    return f"{830000000 + e['n0'] * 10 + i}"


def responsable(e: dict, nombre: str) -> str:
    """Quién es el responsable de una oportunidad en la exportación: Salesforce exporta su id de
    usuario; HubSpot y los demás, su nombre. La liquidación lo nombra igual."""
    return f"005A0000{N.norm(nombre)[:6]}" if e["crm"].startswith("salesforce") else nombre


def cuenta_crm(e: dict, i: int) -> str:
    """El id de la cuenta como lo exporta cada CRM: el de Salesforce es de 18 caracteres; HubSpot
    exporta el nombre de la empresa asociada; un CRM cualquiera, su código."""
    if e["crm"].startswith("salesforce"):
        return f"001A0000{e['n0']:04d}{i:02d}AaQ"[:18].ljust(18, "Z")
    if e["crm"].startswith("hubspot"):
        return e["clientes"][i]
    return f"CL-{e['n0'] + i}"


def d(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


# ================================================================ el escenario de cada entidad

def escenario(e: dict) -> dict:
    """Las oportunidades, la evidencia, el comité, las cotizaciones, los contratos de Fidel, las
    facturas de Clara y la liquidación: el escenario limpio, y sobre él lo que se siembra."""
    u, n0, s = e["u"], e["n0"], set(e["siembra"])
    p1, p2, p3 = e["personas"]
    op = lambda k: f"OPP-{n0 + k}"  # noqa: E731
    # Cada oportunidad: su cuenta, su responsable, su monto y su estado en cada corte —etapa, fecha de
    # cierre y última actividad—; con `historia`, las veces que el historial de Salesforce dice que se corrió.
    ops = [
        {"k": 1, "nombre": "Renovación de licencias", "c": 0, "resp": p1, "monto": 12 * u,
         "cortes": [("Compromiso", "2026-10-10", "2026-09-28"), ("Ganada", "2026-10-10", "2026-10-10"), ("Ganada", "2026-10-10", "2026-10-10")]},
        {"k": 2, "nombre": "Proyecto de expansión", "c": 1, "resp": p2, "monto": 18 * u,
         "cortes": [("Negociación", "2026-10-25", "2026-09-30"), ("Compromiso", "2026-10-22", "2026-10-14"), ("Ganada", "2026-10-22", "2026-10-22")]},
        {"k": 3, "nombre": "Suministro anual", "c": 2, "resp": p3, "monto": 25 * u,
         "cortes": [("Propuesta", "2026-11-20", "2026-09-25"), ("Negociación", "2026-11-20", "2026-10-15"), ("Compromiso", "2026-11-20", "2026-10-30")]},
        {"k": 4, "nombre": "Servicio de soporte", "c": 3, "resp": p1, "monto": 9 * u,
         "cortes": [("Calificación", "2026-12-10", "2026-09-29"), ("Propuesta", "2026-12-10", "2026-10-12"), ("Propuesta", "2026-12-15", "2026-10-29")]},
        {"k": 5, "nombre": "Ampliación de contrato", "c": 4, "resp": p2, "monto": 7 * u,
         "cortes": [("Calificación", "2026-12-20", "2026-09-26"), ("Calificación", "2026-12-20", "2026-10-11"), ("Calificación", "2026-12-20", "2026-10-27")]},
        {"k": 6, "nombre": "Piloto regional", "c": 5, "resp": p3, "monto": 6 * u,
         "cortes": [("Propuesta", "2026-10-30", "2026-09-27"), ("Negociación", "2026-10-30", "2026-10-13"), ("Perdida", "2026-10-28", "2026-10-28")]},
        # Un cierre que se corrió una vez: el parecido a una señal, en todas las entidades.
        {"k": 7, "nombre": "Implementación por fases", "c": 6, "resp": p1, "monto": 11 * u,
         "cortes": [("Negociación", "2026-11-30", "2026-09-30"), ("Negociación", "2026-11-30", "2026-10-15"), ("Negociación", "2026-12-18", "2026-10-31")]},
    ]
    evid = {op(1): ["propuesta", "orden_compra"], op(2): ["propuesta", "orden_compra"], op(3): ["propuesta", "orden_compra"],
            op(4): ["propuesta"], op(7): ["propuesta"]}
    cerrado = 12 * u + 18 * u
    comite = {"comprometido": round(cerrado * 1.05), "mejor": round(cerrado * 1.6)}
    meta = round(cerrado * 1.05)
    cot = [{"n": 1, "k": 1, "lista": 13.4 * u, "pct": 10, "aprobo": None, "cargo": None, "fecha": None},
           {"n": 2, "k": 2, "lista": 22.0 * u, "pct": 18, "aprobo": "Marta Gil", "cargo": "Gerente comercial", "fecha": "2026-10-05"},
           # Un descuento del nivel 2 aprobado por el gerente general: un cargo superior también aprueba.
           {"n": 3, "k": 3, "lista": 29.0 * u, "pct": 14, "aprobo": "Ricardo Paz", "cargo": "Gerente general", "fecha": "2026-10-20"}]
    # Fidel: el contrato de cada venta ganada, uno de un cliente firmado hace poco y uno con un proveedor.
    contratos = [{"code": f"CTR-{n0 + 1}", "c": 0, "firmado": "2026-10-13", "valor": 12 * u},
                 {"code": f"CTR-{n0 + 2}", "c": 1, "firmado": "2026-10-24", "valor": 18 * u},
                 {"code": f"CTR-{n0 + 3}", "c": 4, "firmado": "2026-10-20", "valor": 5 * u},
                 {"code": f"CTR-{n0 + 9}", "proveedor": True, "firmado": "2026-09-05", "valor": 4 * u}]
    # Clara: las facturas emitidas de cada cierre.
    facturas = [{"n": 1, "c": 0, "fecha": "2026-10-20", "base": 12 * u, "periodo": "2026-10"},
                {"n": 2, "c": 1, "fecha": "2026-10-30", "base": 18 * u, "periodo": "2026-10"},
                {"n": 3, "c": 3, "fecha": "2026-09-12", "base": 2 * u, "periodo": "2026-09"}]
    liq = {p1: 12 * u * TASA / 100, p2: 18 * u * TASA / 100}
    esperado, umbrales = [], {}

    if "etapa_sin_evidencia" in s:      # en compromiso, sin la orden de compra
        evid[op(3)] = ["propuesta"]
        esperado.append(("stage_without_evidence", f"etapa:{op(3)}"))
    if "detenida" in s:                 # sin actividad desde septiembre
        ops[4]["cortes"] = [(st, ci, "2026-09-12") for st, ci, _ in ops[4]["cortes"]]
        esperado.append(("stalled_opportunity", f"detenida:{op(5)}"))
    if "cierre_historial" in s:         # el historial de Salesforce: tres veces
        ops[6]["historia"] = [("2026-10-31", "2026-11-15"), ("2026-11-15", "2026-11-30"), ("2026-11-30", "2026-12-18")]
        ops[6]["cortes"][1] = ("Negociación", "2026-11-30", "2026-10-15")
        esperado.append(("close_date_slipped", f"corre:{op(7)}"))
    if "cierre_cortes" in s:            # de un corte a otro, con un umbral de una vez
        ops[3]["cortes"] = [("Propuesta", "2026-11-15", "2026-09-29"), ("Propuesta", "2026-12-01", "2026-10-12"), ("Propuesta", "2026-12-15", "2026-10-29")]
        umbrales["max_close_moves"] = 1
        esperado.append(("close_date_slipped", f"corre:{op(4)}"))
    if "pronostico_sin_respaldo" in s:
        comite["comprometido"] = round(cerrado * 1.5)
        esperado.append(("forecast_unsupported", f"pronostico:{PERIODO}"))
    if "meta_lejos" in s:
        meta = round(cerrado * 1.4)
        esperado.append(("target_vs_closed", f"meta:{PERIODO}"))
    if "descuento_sin_aprobacion" in s:  # el 22 % es del nivel 3 y lo aprobó un cargo del nivel 2
        cot[2] = dict(cot[2], pct=22, aprobo="Marta Gil", cargo="Gerente comercial")
        esperado.append(("discount_outside_policy", f"descuento:COT-{n0 + 3}"))
    if "descuento_fuera_de_matriz" in s:  # ningún nivel cubre un 35 %
        cot[2] = dict(cot[2], pct=35)
        esperado.append(("discount_outside_policy", f"descuento:COT-{n0 + 3}"))
    if "ganado_sin_contrato" in s:      # una venta ganada el 5 de octubre, sin contrato ni factura
        ops.append({"k": 8, "nombre": "Venta de equipos", "c": 2, "resp": p3, "monto": 5 * u,
                    "cortes": [("Compromiso", "2026-10-05", "2026-09-30"), ("Ganada", "2026-10-05", "2026-10-05"), ("Ganada", "2026-10-05", "2026-10-05")]})
        evid[op(8)] = ["propuesta", "orden_compra"]
        cerrado += 5 * u
        comite["comprometido"] = round(cerrado * (1.5 if "pronostico_sin_respaldo" in s else 1.05))
        meta = round(cerrado * (1.4 if "meta_lejos" in s else 1.05))
        esperado.append(("won_without_contract", f"contrato:{op(8)}"))
    if "firmado_sin_factura" in s:      # firmado el 10 de septiembre con un cliente, sin factura hasta el 10 de octubre
        contratos.append({"code": f"CTR-{n0 + 5}", "c": 5, "firmado": "2026-09-10", "valor": 8 * u})
        esperado.append(("signed_without_invoice", f"factura:CTR-{n0 + 5}"))
    if "comision_distinta" in s:        # se liquidó sobre un monto que no es el de la venta
        liq[p2] = 20 * u * TASA / 100
        esperado.append(("commission_differs_from_plan", f"comision:{PERIODO}:{N.norm(responsable(e, p2))}"))
    return {"ops": ops, "evid": evid, "comite": comite, "meta": meta, "cot": cot, "contratos": contratos, "facturas": facturas,
            "liq": liq, "esperado": esperado, "umbrales": umbrales, "op": op}


# ================================================================ cómo exporta cada CRM

def fmt_fecha(x: str, crm: str) -> str:
    f = d(x)
    if crm == "salesforce-informe":
        return f"{f.month}/{f.day}/{f.year}"
    if crm.startswith("hubspot"):
        return f"{x} 09:00"
    if crm.startswith("generico"):
        return f"{f.day:02d}/{f.month:02d}/{f.year}"
    return x


def exportacion(e: dict, esc: dict, corte: int) -> list[list]:
    crm = e["crm"]
    filas = []
    for o in esc["ops"]:
        st, ci, act = o["cortes"][corte]
        oid, c = esc["op"](o["k"]), o["c"]
        if crm == "salesforce-api":
            filas.append([oid, o["nombre"], cuenta_crm(e, c), f"{o['monto']:.2f}", fmt_fecha(ci, crm), st, PROB[st],
                          "true" if st in ("Ganada", "Perdida") else "false", "true" if st == "Ganada" else "false",
                          fmt_fecha(act, crm), responsable(e, o["resp"]), "2026-08-15T10:00:00.000Z",
                          f"compras@{N.norm(e['clientes'][c])[:12]}.com"])
        elif crm == "salesforce-informe":
            filas.append([oid, o["nombre"], cuenta_crm(e, c), f"{o['monto']:.2f}", fmt_fecha(ci, crm), st, f"{PROB[st]}%",
                          fmt_fecha(act, crm), responsable(e, o["resp"]), fmt_fecha("2026-08-15", crm)])
        elif crm.startswith("hubspot"):
            filas.append([oid, o["nombre"], st, "Ventas", f"{o['monto']:.0f}", fmt_fecha(ci, crm), o["resp"], fmt_fecha("2026-08-15", crm),
                          fmt_fecha(act, crm), cuenta_crm(e, c), f"Contacto {c + 1} (contacto{c + 1}@cliente.com)"])
        else:
            filas.append([oid, o["nombre"], cuenta_crm(e, c), st, f"{o['monto']:.0f}", fmt_fecha(ci, crm), o["resp"], fmt_fecha(act, crm),
                          "Licencias" if o["k"] % 2 else "Servicios"])
    cab = {"salesforce-api": ["Id", "Name", "AccountId", "Amount", "CloseDate", "StageName", "Probability", "IsClosed", "IsWon",
                              "LastActivityDate", "OwnerId", "CreatedDate", "Contact_Email__c"],
           "salesforce-informe": ["Opportunity ID", "Name", "Account ID", "Amount", "Close Date", "Stage", "Probability (%)",
                                  "Last Activity", "Owner ID", "Created Date"],
           "hubspot": ["Record ID", "Deal Name", "Deal Stage", "Pipeline", "Amount", "Close Date", "Deal owner", "Create Date",
                       "Last Activity Date", "Associated Company", "Associated Contact"],
           "generico": ["Código", "Oportunidad", "Cliente", "Fase", "Valor estimado", "Fecha estimada de cierre", "Ejecutivo",
                        "Última gestión", "Línea"]}
    return [cab["hubspot" if crm.startswith("hubspot") else "generico" if crm.startswith("generico") else crm]] + filas


def columnas_crm(e: dict) -> dict:
    """El mapeo que deja el setup: el de un CRM cualquiera, la empresa asociada de HubSpot y la línea."""
    if e["crm"].startswith("generico"):
        return {"id": "Código", "nombre": "Oportunidad", "cuenta": "Cliente", "etapa": "Fase", "monto": "Valor estimado",
                "cierre": "Fecha estimada de cierre", "responsable": "Ejecutivo", "ultima_actividad": "Última gestión", "linea": "Línea"}
    if e["crm"].startswith("hubspot"):
        return {"cuenta": "Associated Company"}
    return {}


# ================================================================ escribir

def _csv(ruta: Path, filas: list[list], sep: str = ",") -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter=sep).writerows(filas)


def md(ruta: Path, texto: str) -> Path:
    """Un documento escrito, en el formato de su extensión: Markdown, Word o PDF con capa de texto."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    texto = texto.strip() + "\n"
    if ruta.suffix == ".docx":
        FMT.a_docx(texto, ruta)
    elif ruta.suffix == ".pdf":
        FMT.a_pdf(texto, ruta)
    else:
        ruta.write_text(texto, encoding="utf-8")
    return ruta


def mon(x: float, e: dict) -> str:
    t = f"{x:,.0f}"
    return "$ " + (t.replace(",", ".") if e["pais"] == "CO" else t)


def una(e: dict) -> dict:
    esc = escenario(e)
    base = SALIDA / e["carpeta"]
    nombre_dir = f"{e['id']}-{N.norm(e['nombre']).replace('_', '-')}"
    docs = base / "comercial" / nombre_dir
    sep = ";" if e["pais"] == "CO" else ","
    _csv(docs / "00-referencia" / "etapas.csv", [["etapa", "orden", "probabilidad", "exige", "tipo"]] + [list(x) for x in ETAPAS], sep)
    _csv(docs / "00-referencia" / "metas.csv", [["periodo", "meta"], ["2026-09", esc["meta"]], [PERIODO, esc["meta"]], ["2026-11", esc["meta"]]], sep)
    _csv(docs / "00-referencia" / "matriz-descuentos.csv", [["nivel", "tope", "aprueba"]] + [list(x) for x in NIVELES], sep)
    _csv(docs / "00-referencia" / "cuentas.csv", [["cuenta", "nombre", "identificacion"]] +
         [[cuenta_crm(e, i), c, tid(e, i)] for i, c in enumerate(e["clientes"])], sep)
    _csv(docs / "00-referencia" / "plan-comisiones.csv", [["linea", "tasa"], ["todas", TASA]], sep)
    # Las tres exportaciones, en el formato de su CRM.
    for k, corte in enumerate(CORTES):
        filas = exportacion(e, esc, k)
        if e["crm"].endswith("xlsx"):
            ruta = docs / "10-crm" / f"oportunidades-{corte.isoformat()}.xlsx"
            ruta.parent.mkdir(parents=True, exist_ok=True)
            import io
            texto = io.StringIO()
            csv.writer(texto).writerows([[str(x) for x in f] for f in filas])
            FMT.a_xlsx(texto.getvalue(), ruta, hoja="Oportunidades")
        else:
            nombre = ("hubspot-crm-exports-deals-" if e["crm"].startswith("hubspot") else "oportunidades-") + corte.isoformat() + ".csv"
            _csv(docs / "10-crm" / nombre, filas, "," if e["crm"].startswith(("salesforce", "hubspot")) else sep)
    hist = [(esc["op"](o["k"]), a, b) for o in esc["ops"] for a, b in o.get("historia", [])]
    if e["crm"] == "salesforce-api":
        _csv(docs / "10-crm" / f"historial-{CORTES[-1].isoformat()}.csv",
             [["OpportunityId", "Field", "OldValue", "NewValue", "CreatedDate"]] +
             [[i, "CloseDate", a, b, f"{a}T12:00:00.000Z"] for i, a, b in hist] +
             [[esc["op"](2), "StageName", "Negociación", "Compromiso", "2026-10-14T12:00:00.000Z"]], ",")
    # El acta del comité: el comprometido y, a su lado, el mejor escenario, que no es el comprometido.
    acta = md(docs / "20-comite" / "acta-comite-2026-10-02.docx", f"""
# Acta del comité comercial · {e['nombre']}

Fecha: 2 de octubre de 2026. Asistentes: {', '.join(e['personas'])} y la gerencia comercial.

## Pronóstico de octubre

Se revisó el embudo con la exportación del 1 de octubre. **El comité compromete para octubre un
pronóstico de ventas de {mon(esc['comite']['comprometido'], e)}.** El mejor escenario, si cierran
todas las negociaciones abiertas, es de {mon(esc['comite']['mejor'], e)}; no se compromete.

## Compromisos

- Enviar las propuestas pendientes antes del 15 de octubre.
- Revisar en el próximo comité las oportunidades que cambiaron de fecha de cierre.
""")
    # La evidencia de cada oportunidad: la propuesta, la orden de compra.
    evidencia = []
    for o in esc["ops"]:
        oid = esc["op"](o["k"])
        for tipo in esc["evid"].get(oid, []):
            nombre = "propuesta" if tipo == "propuesta" else "orden-compra"
            fecha_doc = "2026-09-18" if tipo == "propuesta" else o["cortes"][-1][1] if o["cortes"][-1][0] == "Ganada" else "2026-10-28"
            monto = o["monto"] if tipo == "orden_compra" else round(o["monto"] * 1.08)
            ruta = docs / "30-evidencia" / f"{oid}_{nombre}.{'md' if tipo == 'propuesta' else 'pdf'}"
            cliente = e["clientes"][o["c"]]
            if tipo == "propuesta":
                texto = (f"# Propuesta comercial\n\nOportunidad: {oid} · {o['nombre']}\nCliente: {cliente}\n"
                         f"Fecha de envío: {fecha_doc}\nValor de la propuesta: {mon(monto, e)}\n\n"
                         f"Contacto del cliente: compras@{N.norm(cliente)[:10]}.com · +57 601 555 01{o['k']:02d}\n")
            else:
                texto = (f"# Orden de compra\n\nEmitida por: {cliente}\nReferencia de la oportunidad: {oid}\n"
                         f"Fecha: {fecha_doc}\nValor total: {mon(monto, e)}\n")
            md(ruta, texto)
            evidencia.append({"opportunity": oid, "type": tipo, "amount": monto, "date": fecha_doc,
                              "source": f"30-evidencia/{ruta.name}"})
    # Las cotizaciones, con su descuento y su aprobación.
    quotes = []
    for q in esc["cot"]:
        qid, oid = f"COT-{e['n0'] + q['n']}", esc["op"](q["k"])
        apr = (f"Aprobó el descuento: {q['aprobo']}, {q['cargo'].lower()}, el {q['fecha']}." if q["aprobo"] else
               "Descuento dentro del nivel sin aprobación.")
        cot_ruta = md(docs / "40-cotizaciones" / f"{qid}_cotizacion.pdf", f"""
# Cotización {qid}

Oportunidad: {oid}
Precio de lista: {mon(q['lista'], e)}
Descuento: {q['pct']} %
{apr}
""")
        quotes.append({"id": qid, "opportunity": oid, "list_amount": round(q["lista"]), "discount_pct": q["pct"],
                       "approved_by": q["aprobo"], "approver_role": q["cargo"].lower() if q["cargo"] else None,
                       "approved_on": q["fecha"], "source": f"40-cotizaciones/{cot_ruta.name}"})
    _csv(docs / "50-comisiones" / f"liquidacion-{PERIODO}.csv", [["responsable", "liquidado"]] +
         [[responsable(e, r), round(v)] for r, v in esc["liq"].items()], sep)
    # Las fichas de Fidel y de Clara, como ellos las escriben.
    legal = base / "estado-legal" / nombre_dir / "contratos"
    for c in esc["contratos"]:
        cp = ({"name": f"Proveedor {e['n0']} S.A.S.", "id": f"{870000000 + e['n0']}" if e["pais"] == "CO" else f"PRV{e['n0']}0101AB1"}
              if c.get("proveedor") else {"name": e["clientes"][c["c"]], "id": tid(e, c["c"])})
        N.escribir_json(legal / f"{c['code']}.json", {
            "code": c["code"], "counterparty": cp, "value": c["valor"], "start": c["firmado"], "end": "2027-12-31",
            "signed_on": c["firmado"], "signed_by_both": True, "source": f"contratos/{c['code']}/10-contrato/contrato.pdf"})
    fin = base / "estado-finanzas" / nombre_dir / "cierre"
    for per in ("2026-09", PERIODO):
        emitidas = [{"numero": f"FE-{e['n0'] + f['n']}", "id": f"cufe-{e['n0']}-{f['n']}", "fecha": f["fecha"], "receptor": tid(e, f["c"]),
                     "base": f["base"], "total": round(f["base"] * (1.19 if e["pais"] == "CO" else 1.16)), "tipo": "factura",
                     "archivo": f"{per}/30-facturacion/emitidas/fe-{e['n0'] + f['n']}.xml"}
                    for f in esc["facturas"] if f["periodo"] == per]
        N.escribir_json(fin / per / "resultados.json", {"agente": "clara", "periodo": per,
                                                        "partes": {"einvoice-check": {"periodo": per, "emitidas": emitidas}}})
    ent = {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]}
    paths = {"documents": f"comercial/{nombre_dir}", "state": f"estado-comercial/{nombre_dir}"}
    fmt = "salesforce" if e["crm"].startswith("salesforce") else "hubspot" if e["crm"].startswith("hubspot") else "generico"
    crm = {"format": fmt, "columns": columnas_crm(e), "date_order": "mdy" if e["crm"] == "salesforce-informe" else "dmy"}
    clave = {
        "entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "crm": e["crm"], "hoy": HOY.isoformat(), "periodo": PERIODO,
        "siembra": e["siembra"],
        "config": {
            "augusto": {"entity": ent, "paths": paths, "period": PERIODO, "crm": crm, "thresholds": dict(esc["umbrales"])},
            "valeria": {"entity": ent, "paths": paths, "period": PERIODO, "crm": crm, "thresholds": dict(esc["umbrales"]),
                        "revenue": {"contract_records": f"estado-legal/{nombre_dir}/contratos", "invoice_records": f"estado-finanzas/{nombre_dir}",
                                    "publish_commissions": False}},
        },
        "extraccion": {
            "comercial": {"evidence": evidencia, "declared_forecast": {"value": esc["comite"]["comprometido"], "date": "2026-10-02",
                                                                       "source": f"20-comite/{acta.name}"}, "questions": []},
            "ingresos": {"quotes": quotes, "questions": []},
        },
        "esperado": [{"signal": a, "key": b} for a, b in sorted(esc["esperado"])],
    }
    N.escribir_json(base / "clave.json", clave)
    return clave


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    for e in ENTIDADES:
        c = una(e)
        print(f"  {e['carpeta']:15} {e['pais']}  {e['crm']:19} {len(c['esperado'])} señales sembradas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
