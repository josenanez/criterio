#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CLO: cuatro industrias y dos entidades de control.

    python3 tests/criterio-clo/generar.py          escribe tests/criterio-clo/material/

Cada entidad trae su carpeta legal al 6 de octubre de 2026: la matriz de atribuciones y la de
obligaciones, el registro de contratos y la exportación de pagos, el índice de políticas, el
registro normativo y un boletín, el registro de casos del canal, una carpeta por contrato —el
contrato, sus otrosíes, sus pólizas, el certificado de la contraparte y la evidencia de cada
obligación— y tres periodos de cumplimiento, de julio a septiembre, con su evidencia y el
informe del periodo. Dos de las industrias son de Colombia y dos de Ecuador.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su
señal esperada queda escrita en `clave.json`, junto con lo que el agente tendría que extraer
de los documentos escritos: la ficha de cada contrato y la del periodo de cumplimiento. El
motor no la ve; `evaluar.py` compara lo que el motor levanta contra ella, y una señal de más
cuenta igual que una de menos.

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: un
contrato que vence pronto con la decisión registrada, una prórroga automática con su preaviso
decidido, un otrosí que cambia la terminación, una norma recién llegada, un informe que
declara cumplido un periodo que lo está. Todo es determinista: el mismo material cada vez,
byte a byte. Los nombres, las normas y las cifras son sintéticos.
"""
from __future__ import annotations

import copy
import csv
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-legal" / "scripts"))
import legal as L  # noqa: E402

N = L.N


def ruc(tipo: int, semilla: int, i: int) -> str:
    """Un RUC peruano ficticio de once dígitos con su dígito verificador por módulo 11, el mismo del
    material de la CFO. Ninguno corresponde a una empresa."""
    base = f"{tipo:02d}{semilla:02d}{i:06d}"
    r = 11 - sum(int(d) * w for d, w in zip(base, (5, 4, 3, 2, 7, 6, 5, 4, 3, 2))) % 11
    return base + str({10: 0, 11: 1}.get(r, r))


def rut(cuerpo: int) -> str:
    """Un RUT chileno ficticio con su dígito verificador por módulo 11 (10 es K y 11 es 0), el mismo
    del material de la CFO. Ninguno corresponde a una empresa."""
    total, f = 0, 2
    for ch in reversed(str(cuerpo)):
        total += int(ch) * f
        f = 2 if f == 7 else f + 1
    v = 11 - total % 11
    return f"{cuerpo}-{ {10: 'K', 11: '0'}.get(v, str(v)) }"


def rfc(letras: str, fecha_: str, homoclave: str) -> str:
    """Un RFC mexicano ficticio de persona moral, de 12 posiciones, el mismo del material de la CFO.
    Ninguno corresponde a una empresa."""
    return f"{letras[:3].upper()}{fecha_}{homoclave[:3].upper()}"


def id_contraparte(e: dict, i: int) -> str:
    """La identificación de una contraparte con la forma de su país; Colombia y Ecuador conservan la
    numeración con la que se probaron."""
    if e["pais"] == "PE":
        return ruc(20, e["n0"] // 10, i + 1)
    if e["pais"] == "CL":
        return rut(77000000 + e["n0"] * 10 + i)
    if e["pais"] == "MX":
        return rfc("PRV", f"{10 + e['n0'] // 100 % 10:02d}{1 + i % 12:02d}{1 + i:02d}", f"{chr(65 + i)}{e['n0'] // 100 % 10}{i}")
    return f"{800000000 + e['n0'] * 10 + i}"

SALIDA = AQUI / "material"
HOY, PERIODO = dt.date(2026, 10, 6), "2026-09"
PERIODOS = ["2026-07", "2026-08", "2026-09"]

ENTIDADES = [
    {"carpeta": "banca", "industria": "banca", "pais": "CO", "id": "900123456", "nombre": "Banco Andino", "moneda": "COP", "u": 50_000_000, "n0": 100,
     "personas": ("Marta Ríos", "Andrés Vela", "Diana Cruz"),
     "contrapartes": ["Soluciones Andinas S.A.S.", "Papelería Nacional S.A.S.", "Inmobiliaria Centro S.A.", "Licencias del Norte S.A.S.",
                      "Consultores Asociados S.A.S.", "Mantenimientos Unidos S.A.S.", "Seguridad Integral S.A.S."],
     "fidel": ["preaviso_cerca", "firma_sin_facultad", "registro_distinto", "sin_garantia", "obligacion_contrato_vencida"],
     "constanza": ["obligacion_vencida", "sin_responsable", "norma_sin_evaluar", "informe_declara_cumplido", "obligacion_contrato_fuera"]},
    {"carpeta": "cooperativas", "industria": "cooperativas", "pais": "EC", "id": "1790012345001", "nombre": "Cooperativa Sierra Alta", "moneda": "USD", "u": 20_000, "n0": 200,
     "personas": ("Patricio Andrade", "Gabriela Mora", "Esteban Jácome"),
     "contrapartes": ["Sistemas Cooperativos Cía. Ltda.", "Suministros Quito S.A.", "Edificios del Valle S.A.", "Software Andino Cía. Ltda.",
                      "Asesoría Financiera Cía. Ltda.", "Servicios Generales S.A.", "Transporte de Valores S.A."],
     "fidel": ["vencido_vigente", "certificado_viejo", "pagos_de_mas", "contrato_sin_registro"],
     "constanza": ["cumplida_sin_evidencia", "evidencia_vieja", "caso_vencido", "norma_aplica_sin_matriz", "norma_en_boletin"]},
    {"carpeta": "retail", "industria": "retail", "pais": "CO", "id": "900765432", "nombre": "Almacenes Caribe", "moneda": "COP", "u": 40_000_000, "n0": 300,
     "personas": ("Carlos Benítez", "Lucía Ortega", "Felipe Arango"),
     "contrapartes": ["Logística Caribe S.A.S.", "Empaques del Atlántico S.A.S.", "Centro Comercial Mar S.A.", "Punto de Venta Digital S.A.S.",
                      "Mercadeo Integral S.A.S.", "Refrigeración Industrial S.A.S.", "Vigilancia Costera S.A.S."],
     "fidel": ["contrato_por_vencer", "otrosi_sin_facultad", "pago_despues", "garantia_corta", "registro_sin_documento"],
     "constanza": ["sin_fuente", "politica_vencida", "obligacion_vencida", "informe_declara_cumplido"]},
    {"carpeta": "mineria", "industria": "mineria", "pais": "EC", "id": "0990054321001", "nombre": "Minera Cóndor", "moneda": "USD", "u": 50_000, "n0": 400,
     "personas": ("Rodrigo Salazar", "Verónica Paz", "Mauricio León"),
     "contrapartes": ["Perforaciones del Sur S.A.", "Explosivos Técnicos S.A.", "Campamentos Andinos S.A.", "Geodatos Cía. Ltda.",
                      "Ambiental Consultores Cía. Ltda.", "Maquinaria Pesada S.A.", "Laboratorio Minero S.A."],
     "fidel": ["preaviso_vencido", "sin_firma", "sin_garantia", "firma_sin_facultad"],
     "constanza": ["caso_vencido", "evidencia_vieja", "obligacion_contrato_fuera", "norma_sin_evaluar", "cumplida_sin_evidencia"]},
    {"carpeta": "control-co", "industria": "retail", "pais": "CO", "id": "900000001", "nombre": "Distribuidora Control", "moneda": "COP", "u": 30_000_000, "n0": 500,
     "personas": ("Elena Duarte", "Jorge Silva", "Natalia Rincón"),
     "contrapartes": ["Transportes Control S.A.S.", "Insumos Control S.A.S.", "Bodegas Control S.A.", "Software Control S.A.S.",
                      "Asesores Control S.A.S.", "Mantenimiento Control S.A.S.", "Aseo Control S.A.S."],
     "fidel": [], "constanza": []},
    {"carpeta": "control-ec", "industria": "cooperativas", "pais": "EC", "id": "1790000001001", "nombre": "Comercial Control", "moneda": "USD", "u": 15_000, "n0": 600,
     "personas": ("Fernanda Vaca", "Diego Herrera", "Paola Cevallos"),
     "contrapartes": ["Logística Control S.A.", "Proveedora Control S.A.", "Locales Control S.A.", "Datos Control Cía. Ltda.",
                      "Consultora Control Cía. Ltda.", "Servicios Control S.A.", "Custodia Control S.A."],
     "fidel": [], "constanza": []},
    {"carpeta": "banca-pe", "industria": "banca", "pais": "PE", "id": ruc(20, 71, 1), "nombre": "Banco Ribera", "moneda": "PEN", "u": 60_000, "n0": 700,
     "personas": ("Rosa Quispe", "Martín Paredes", "Claudia Salinas"),
     "contrapartes": ["Tecnología Limeña S.A.C.", "Útiles del Pacífico S.A.C.", "Inmuebles Miraflores S.A.", "Licencias Andinas S.A.C.",
                      "Consultoría Integral S.A.C.", "Mantenimiento Total E.I.R.L.", "Seguridad Perú S.A.C."],
     "fidel": ["preaviso_cerca", "firma_sin_facultad", "registro_distinto", "sin_garantia", "obligacion_contrato_vencida"],
     "constanza": ["obligacion_vencida", "sin_responsable", "norma_sin_evaluar", "informe_declara_cumplido", "obligacion_contrato_fuera"]},
    {"carpeta": "mineria-pe", "industria": "mineria", "pais": "PE", "id": ruc(20, 73, 1), "nombre": "Minera Puna Alta", "moneda": "PEN", "u": 180_000, "n0": 800,
     "personas": ("Julio Huamán", "Carmen Rojas", "Óscar Mendoza"),
     "contrapartes": ["Perforaciones Andinas S.A.C.", "Voladuras Técnicas S.A.C.", "Campamentos Sierra S.A.", "Geología Aplicada S.A.C.",
                      "Gestión Ambiental S.A.C.", "Equipos Pesados del Sur S.A.", "Laboratorio Analítico E.I.R.L."],
     "fidel": ["vencido_vigente", "certificado_viejo", "pagos_de_mas", "contrato_sin_registro"],
     "constanza": ["cumplida_sin_evidencia", "evidencia_vieja", "caso_vencido", "norma_aplica_sin_matriz", "norma_en_boletin"]},
    {"carpeta": "control-pe", "industria": "mineria", "pais": "PE", "id": ruc(20, 79, 1), "nombre": "Comercial Control Sur", "moneda": "PEN", "u": 40_000, "n0": 900,
     "personas": ("Silvia Chávez", "Raúl Torres", "Patricia Flores"),
     "contrapartes": ["Transportes Control S.A.C.", "Insumos Control S.A.C.", "Almacenes Control S.A.", "Sistemas Control S.A.C.",
                      "Asesoría Control S.A.C.", "Servicios Control E.I.R.L.", "Limpieza Control S.A.C."],
     "fidel": [], "constanza": []},
    {"carpeta": "retail-cl", "industria": "retail", "pais": "CL", "id": rut(76083001), "nombre": "Tiendas Pacífico", "moneda": "CLP", "u": 12_000_000, "n0": 1000,
     "personas": ("Francisca Muñoz", "Tomás Contreras", "Javiera Soto"),
     "contrapartes": ["Logística Austral SpA", "Envases del Maipo S.A.", "Centro Comercial Costanera S.A.", "Pagos Digitales SpA",
                      "Marketing Integral Ltda.", "Frío Industrial SpA", "Seguridad Andes Ltda."],
     "fidel": ["contrato_por_vencer", "otrosi_sin_facultad", "pago_despues", "garantia_corta", "registro_sin_documento"],
     "constanza": ["sin_fuente", "politica_vencida", "obligacion_vencida", "informe_declara_cumplido"]},
    {"carpeta": "mineria-cl", "industria": "mineria", "pais": "CL", "id": rut(76089001), "nombre": "Minera Atacama Norte", "moneda": "CLP", "u": 45_000_000, "n0": 1100,
     "personas": ("Cristián Vergara", "Daniela Fuentes", "Ignacio Pizarro"),
     "contrapartes": ["Sondajes del Norte SpA", "Explosivos Atacama S.A.", "Campamentos Desierto Ltda.", "Geodatos Chile SpA",
                      "Consultora Ambiental Ltda.", "Maquinaria Minera S.A.", "Laboratorio Químico SpA"],
     "fidel": ["preaviso_vencido", "sin_firma", "sin_garantia", "firma_sin_facultad"],
     "constanza": ["caso_vencido", "evidencia_vieja", "obligacion_contrato_fuera", "norma_sin_evaluar", "cumplida_sin_evidencia"]},
    {"carpeta": "control-cl", "industria": "retail", "pais": "CL", "id": rut(76097001), "nombre": "Comercial Control Andes", "moneda": "CLP", "u": 9_000_000, "n0": 1200,
     "personas": ("Valentina Rojas", "Matías Herrera", "Catalina Díaz"),
     "contrapartes": ["Transportes Control SpA", "Insumos Control Ltda.", "Bodegas Control S.A.", "Software Control SpA",
                      "Asesores Control Ltda.", "Mantención Control SpA", "Aseo Control Ltda."],
     "fidel": [], "constanza": []},
    {"carpeta": "banca-mx", "industria": "banca", "pais": "MX", "id": rfc("BVA", "150301", "K21"), "nombre": "Banco Valle de Anáhuac", "moneda": "MXN", "u": 300_000, "n0": 1300,
     "personas": ("Alejandra Navarro", "Ricardo Treviño", "Mónica Garza"),
     "contrapartes": ["Sistemas Financieros S.A. de C.V.", "Papelería del Centro S.A. de C.V.", "Inmobiliaria Reforma S.A.", "Licencias Digitales S. de R.L.",
                      "Consultoría Integral S.C.", "Mantenimiento Industrial S.A. de C.V.", "Seguridad Privada S.A. de C.V."],
     "fidel": ["contrato_por_vencer", "firma_sin_facultad", "pagos_de_mas", "garantia_corta", "obligacion_contrato_vencida"],
     "constanza": ["obligacion_vencida", "sin_responsable", "norma_en_boletin", "informe_declara_cumplido", "obligacion_contrato_fuera"]},
    {"carpeta": "retail-mx", "industria": "retail", "pais": "MX", "id": rfc("TBA", "180912", "Q37"), "nombre": "Tiendas del Bajío", "moneda": "MXN", "u": 220_000, "n0": 1400,
     "personas": ("Fernando Quiroga", "Sofía Elizondo", "Jorge Salgado"),
     "contrapartes": ["Logística del Bajío S.A. de C.V.", "Empaques de Occidente S.A. de C.V.", "Plaza Comercial León S.A.", "Pagos en Línea S.A.P.I. de C.V.",
                      "Publicidad Integral S.C.", "Refrigeración Comercial S.A. de C.V.", "Vigilancia Industrial S.A. de C.V."],
     "fidel": ["preaviso_vencido", "otrosi_sin_facultad", "pago_despues", "sin_firma", "registro_sin_documento"],
     "constanza": ["sin_fuente", "politica_vencida", "caso_vencido", "cumplida_sin_evidencia", "norma_aplica_sin_matriz"]},
    {"carpeta": "control-mx", "industria": "banca", "pais": "MX", "id": rfc("CCM", "120615", "R59"), "nombre": "Comercial Control Centro", "moneda": "MXN", "u": 150_000, "n0": 1500,
     "personas": ("Gabriela Ríos", "Arturo Medina", "Lorena Castillo"),
     "contrapartes": ["Transportes Control S.A. de C.V.", "Insumos Control S.A. de C.V.", "Bodegas Control S.A.", "Software Control S.A. de C.V.",
                      "Asesores Control S.C.", "Mantenimiento Control S.A. de C.V.", "Limpieza Control S.A. de C.V."],
     "fidel": [], "constanza": []},
]

d = dt.date.fromisoformat


def iso(x: dt.date) -> str:
    return x.isoformat()


def slug(s: str) -> str:
    return L.norm(s).replace("_", "-")[:40].strip("-")


def csv_(ruta: Path, filas: list[list]) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, lineterminator="\n").writerows(filas)


def md(ruta: Path, texto: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto.strip() + "\n", encoding="utf-8")


# ================================================================ los contratos

# Los seis contratos de cada entidad, antes de sembrar nada: tipo, valor en unidades de la
# entidad, inicio, terminación, renovación automática y días de preaviso, y quién firma por la
# entidad (0 la gerencia general, 1 la vicepresidencia financiera).
BASE = [
    {"tipo": "servicios", "valor": 8, "inicio": "2026-01-01", "fin": "2027-03-31", "auto": True, "preaviso": 60, "firma": 0, "cumplimiento": True},
    {"tipo": "suministro", "valor": 4, "inicio": "2025-07-01", "fin": "2027-06-30", "auto": False, "preaviso": 0, "firma": 1,
     "otrosi": {"valor": 1, "fecha": "2026-05-15", "nuevo_fin": "2027-12-31", "firma": 1}},
    {"tipo": "arrendamiento", "valor": 6, "inicio": "2025-02-01", "fin": "2026-12-31", "auto": False, "preaviso": 0, "firma": 0},
    {"tipo": "licencia", "valor": 3, "inicio": "2026-03-01", "fin": "2027-02-28", "auto": True, "preaviso": 30, "firma": 1},
    {"tipo": "consultoria", "valor": 2, "inicio": "2026-02-01", "fin": "2026-11-20", "auto": False, "preaviso": 0, "firma": 1,
     "decision": {"action": "renovar", "date": "2026-09-18"}},
    {"tipo": "mantenimiento", "valor": 5, "inicio": "2025-10-01", "fin": "2026-07-31", "auto": False, "preaviso": 0, "firma": 0},
]
OBJETO = {"servicios": "Prestación de servicios de operación tecnológica", "suministro": "Suministro de papelería e insumos de oficina",
          "arrendamiento": "Arrendamiento de la sede principal", "licencia": "Licencia de uso de software",
          "consultoria": "Consultoría en procesos", "mantenimiento": "Mantenimiento preventivo de instalaciones"}


def meses_antes(x: dt.date, k: int) -> list[dt.date]:
    """El día 10 de los k meses que terminan en el de x."""
    out = []
    for j in range(k - 1, -1, -1):
        m = x.month - 1 - j
        a, m = x.year + m // 12, m % 12 + 1
        out.append(dt.date(a, m, 10))
    return out


def contrato(e: dict, i: int, b: dict) -> dict:
    """La ficha de un contrato y lo que hace falta para escribir sus documentos."""
    u = e["u"]
    code = f"CTR-{e['n0'] + i}"
    contraparte = e["contrapartes"][i - 1]
    carpeta = f"contratos/{code}-{slug(contraparte)}"
    doc = f"{carpeta}/10-contrato/contrato.md"
    inicio, fin = d(b["inicio"]), d(b["fin"])
    firmado = inicio - dt.timedelta(days=5)
    firmante = e["personas"][b["firma"]]
    c = {"code": code, "type": b["tipo"], "counterparty": {"name": contraparte, "id": id_contraparte(e, i)},
         "value": b["valor"] * u, "start": iso(inicio), "end": iso(fin), "signed_on": iso(firmado), "signed_by_both": True,
         "auto_renewal": b["auto"], "notice_days": b["preaviso"] if b["auto"] else None, "renewal_months": 12 if b["auto"] else None,
         "signatories": [{"name": firmante, "role": ["Gerente general", "Vicepresidente financiero", "Director de compras"][b["firma"]], "party": "entidad"},
                         {"name": f"Representante de {contraparte}", "role": "Representante legal", "party": "contraparte"}],
         "amendments": [],
         "guarantees_required": [{"type": "cumplimiento", "months_after_end": 4, "source": f"{doc}, cláusula 9"}],
         "guarantees_provided": [],
         "counterparty_certificate": {"issued_on": iso(firmado - dt.timedelta(days=12)), "source": f"{carpeta}/30-contraparte/certificado.md"},
         "obligations": [],
         "decision": None,
         "source": doc}
    if b.get("otrosi"):
        o = b["otrosi"]
        c["amendments"].append({"id": "OT-1", "date": o["fecha"], "added_value": o["valor"] * u, "new_end": o.get("nuevo_fin"), "signed": True,
                                "signed_by": e["personas"][o["firma"]], "source": f"{carpeta}/10-contrato/otrosi-1.md"})
    if b.get("decision"):
        c["decision"] = dict(b["decision"], source=f"{carpeta}/40-ejecucion/acta-comite-contratos.md")
    return {"ficha": c, "carpeta": carpeta, "registro": True, "estado_registro": None, "valor_registro": None,
            "pagos_factor": 0.3, "pago_tarde": False, "garantia_meses": 4, "sin_evidencia": set(), "cumplimiento": b.get("cumplimiento", False)}


def completar(x: dict) -> None:
    """Lo que se deriva de las fechas, después de sembrar: obligaciones, pólizas y pagos."""
    c = x["ficha"]
    fin = L.fin_documentado(c)
    doc = c["source"]
    o1 = min(d("2026-09-05"), fin - dt.timedelta(days=25))
    c["obligations"] = [{"id": "OBL-1", "what": "Informe mensual de ejecución", "due": iso(o1), "who": c["counterparty"]["name"], "kind": "entrega",
                         "source": f"{doc}, cláusula 5"},
                        {"id": "OBL-2", "what": "Informe final y acta de liquidación", "due": iso(fin), "who": c["counterparty"]["name"], "kind": "entrega",
                         "source": f"{doc}, cláusula 6"}]
    if x["cumplimiento"]:
        c["obligations"].append({"id": "OBL-3", "what": "Reporte de operaciones al oficial de cumplimiento", "due": "2026-09-30",
                                 "who": c["counterparty"]["name"], "kind": "cumplimiento", "source": f"{doc}, cláusula 7"})
    tipos = {g["type"] for g in c["guarantees_provided"]}
    if "cumplimiento" not in tipos and x["garantia_meses"] is not None:
        c["guarantees_provided"].append({"type": "cumplimiento", "until": iso(L.sumar_meses(fin, x["garantia_meses"])), "insurer": "Aseguradora Sintética S.A.",
                                         "source": f"{x['carpeta']}/20-garantias/poliza-cumplimiento.md"})


def pagos(x: dict) -> list[tuple[dt.date, float]]:
    c = x["ficha"]
    fin = L.fin_documentado(c)
    total = L.valor_total(c)
    corte = min(fin, d("2026-09-30"))
    fechas = [f for f in meses_antes(corte, 3) if f <= fin and f >= d(c["start"])]
    cuota = round(total * x["pagos_factor"] / len(fechas), 2)
    out = [(f, cuota) for f in fechas]
    if x["pago_tarde"]:
        out.append((d("2026-09-10"), round(total * 0.05, 2)))
    return out


def documentos_contrato(docs: Path, e: dict, x: dict) -> None:
    c = x["ficha"]
    base = docs / x["carpeta"]
    ent = [s for s in c["signatories"] if s["party"] == "entidad"]
    reno = (f"El contrato se prorrogará automáticamente por periodos de {c['renewal_months']} meses, salvo que una de las partes "
            f"avise por escrito su decisión de no renovarlo con al menos {c['notice_days']} días de anticipación a su terminación."
            if c["auto_renewal"] else "El contrato no se prorroga automáticamente.")
    firmas = ("Firmado por las dos partes el " + c["signed_on"] + ":\n\n" + "\n".join(f"- {s['name']}, {s['role']}, por {'la entidad' if s['party'] == 'entidad' else 'la contraparte'}"
                                                                                     for s in c["signatories"])
              if c["signed_by_both"] else
              f"Firmado el {c['signed_on']} por {ent[0]['name']}, {ent[0]['role']}, por la entidad.\n\nEspacio para la firma de la contraparte: sin firmar.")
    garantias = "\n".join(f"- Garantía de {g['type']}" + (f" vigente hasta {g['until']}." if g.get("until") else f" vigente hasta {g['months_after_end']} meses después de la terminación.")
                          for g in c["guarantees_required"])
    md(base / "10-contrato" / "contrato.md", f"""
# Contrato {c['code']}

**Partes:** {e['nombre']} ({N.PAISES[e['pais']]['id_fiscal']} {e['id']}) y {c['counterparty']['name']} ({N.PAISES[e['pais']]['id_fiscal']} {c['counterparty']['id']}).

**Cláusula 1. Objeto.** {OBJETO[c['type']]}. Tipo de contrato: {c['type']}.

**Cláusula 2. Valor.** {c['value']:.0f} {e['moneda']}.

**Cláusula 3. Plazo.** Desde el {c['start']} hasta el {c['end']}.

**Cláusula 4. Renovación.** {reno}

**Cláusula 5. Informe mensual.** El contratista entrega un informe mensual de ejecución; el de agosto, a más tardar el {c['obligations'][0]['due']}.

**Cláusula 6. Liquidación.** A la terminación, el contratista entrega el informe final y se firma el acta de liquidación.
""" + ("""
**Cláusula 7. Cumplimiento.** El contratista reporta al oficial de cumplimiento de la entidad las operaciones del periodo, a más tardar el 30 de septiembre de 2026.
""" if any(o["id"] == "OBL-3" for o in c["obligations"]) else "") + f"""
**Cláusula 9. Garantías.** El contratista constituye a favor de la entidad:

{garantias}

{firmas}
""")
    for o in c["amendments"]:
        md(base / "10-contrato" / "otrosi-1.md", f"""
# Otrosí {o['id']} al contrato {c['code']}

Fecha: {o['date']}.

Se adiciona el valor del contrato en {o['added_value']:.0f} {e['moneda']}.""" + (f" Se modifica la terminación del contrato al {o['new_end']}." if o.get("new_end") else "") + f"""

Firmado por las dos partes: {o['signed_by']}, por la entidad, y el representante legal de {c['counterparty']['name']}.
""")
    for g in c["guarantees_provided"]:
        md(base / "20-garantias" / f"poliza-{slug(g['type'])}.md", f"""
# Póliza de {g['type']}

Tomador: {c['counterparty']['name']}. Asegurado: {e['nombre']}. Contrato {c['code']}.

Aseguradora: {g['insurer']}. Vigencia hasta el {g['until']}.
""")
    cert = c["counterparty_certificate"]
    md(base / "30-contraparte" / "certificado.md", f"""
# Certificado de existencia y representación legal

{c['counterparty']['name']}, {N.PAISES[e['pais']]['id_fiscal']} {c['counterparty']['id']}. Representante legal: Representante de {c['counterparty']['name']}.

Expedido el {cert['issued_on']}.
""")
    ej = base / "40-ejecucion"
    ej.mkdir(parents=True, exist_ok=True)
    for o in c["obligations"]:
        if d(o["due"]) <= HOY and o["id"] not in x["sin_evidencia"]:
            md(ej / f"{o['id']}_{slug(o['what'])}.md", f"# {o['what']}\n\nContrato {c['code']}. Entregado el {o['due']}.")
    if c.get("decision"):
        dec = c["decision"]
        md(ej / "acta-comite-contratos.md", f"""
# Acta del comité de contratos

Fecha: {dec['date']}.

El comité revisó el contrato {c['code']} con {c['counterparty']['name']}, que termina el {c['end']}, y decidió **{dec['action']}lo**.
""")


# ================================================================ la siembra de Fidel

def sembrar_fidel(e: dict, cs: list[dict], esperado: list) -> None:
    s, u = e["fidel"], e["u"]
    c1, c2, c3, c4, c5, c6 = (x["ficha"] for x in cs[:6])
    if "preaviso_cerca" in s:          # el límite del preaviso cae en 26 días
        c4.update(end="2026-12-31", notice_days=60)
        esperado.append(("notice_deadline_near", f"preaviso:{c4['code']}"))
    if "preaviso_vencido" in s:        # el límite pasó el 1 de octubre sin decisión
        c1.update(end="2026-10-31", notice_days=30)
        esperado.append(("renewal_notice_missed", f"preaviso:{c1['code']}"))
    if "contrato_por_vencer" in s:     # vence en 50 días, sin decisión
        c3.update(end="2026-11-25")
        esperado.append(("contract_expiring", f"vence:{c3['code']}"))
    if "vencido_vigente" in s:         # terminó el 31 de agosto y el registro lo tiene vigente
        c3.update(end="2026-08-31")
        cs[2]["estado_registro"] = "vigente"
        esperado.append(("contract_expired_active", f"vigente:{c3['code']}"))
    if "registro_distinto" in s:       # el registro dice un valor mayor que el del documento
        cs[1]["valor_registro"] = L.valor_total(c2) + u
        esperado.append(("register_differs_from_contract", f"difiere:{c2['code']}"))
    if "obligacion_contrato_vencida" in s:
        cs[3]["sin_evidencia"].add("OBL-1")
        esperado.append(("contract_obligation_overdue", f"obl:{c4['code']}:OBL-1"))
    if "firma_sin_facultad" in s:      # firma el director de compras un contrato de servicios
        c1["signatories"][0].update(name=e["personas"][2], role="Director de compras")
        esperado.append(("signed_without_authority", f"firma:{c1['code']}"))
    if "otrosi_sin_facultad" in s:     # el otrosí lleva el contrato por encima de la facultad de quien lo firma
        c2["amendments"][0]["added_value"] = 7 * u
        esperado.append(("signed_without_authority", f"firma:{c2['code']}:OT-1"))
    if "sin_firma" in s:               # la contraparte no firmó y el contrato ya empezó
        c5["signed_by_both"] = False
        # Quien no firmó no es firmante: la ficha lista solo a la entidad (CLO-7).
        c5["signatories"] = [x for x in c5["signatories"] if x["party"] == "entidad"]
        esperado.append(("unsigned_contract", f"sinfirma:{c5['code']}"))
    if "certificado_viejo" in s:       # el certificado tenía 75 días cuando se firmó
        c4["counterparty_certificate"]["issued_on"] = iso(d(c4["signed_on"]) - dt.timedelta(days=75))
        esperado.append(("counterparty_certificate_stale", f"cert:{c4['code']}"))
    if "pagos_de_mas" in s:
        cs[1]["pagos_factor"] = 1.06
        esperado.append(("payments_over_value", f"pagos:{c2['code']}"))
    if "pago_despues" in s:            # un pago del 10 de septiembre a un contrato que terminó en julio
        cs[5]["pago_tarde"] = True
        esperado.append(("payment_after_termination", f"pagofuera:{c6['code']}"))
    if "sin_garantia" in s:            # exige la de calidad y no hay póliza
        c3["guarantees_required"].append({"type": "calidad", "months_after_end": 12, "source": f"{c3['source']}, cláusula 9"})
        esperado.append(("guarantee_missing", f"garantia:{c3['code']}:calidad"))
    if "garantia_corta" in s:          # la póliza cubre dos meses y el contrato exige cuatro
        cs[0]["garantia_meses"] = 2
        esperado.append(("guarantee_expires_early", f"garantia:{c1['code']}:cumplimiento"))
    if "contrato_sin_registro" in s:   # un séptimo contrato, con su carpeta y sin su fila en el registro
        x = contrato(e, 7, BASE[3])
        x["registro"] = False
        cs.append(x)
        esperado.append(("register_mismatch", f"carpeta:{x['ficha']['code']}"))


# ================================================================ Constanza

def matriz(e: dict, code_c1: str) -> list[dict]:
    p = e["personas"]
    return [
        {"id": "OB-01", "obligacion": "Reporte mensual de operaciones al supervisor", "fuente": "N-2026-01 · Resolución sintética 001 de 2026", "tipo": "reporte",
         "responsable": p[1], "periodicidad": "mensual", "dia_limite": "día 10", "criticidad": "alta", "ev": PERIODOS},
        {"id": "OB-02", "obligacion": "Conciliación de la base de clientes vinculados", "fuente": "Política P-02", "tipo": "registro",
         "responsable": p[1], "periodicidad": "mensual", "dia_limite": "D+5", "criticidad": "media", "ev": PERIODOS},
        {"id": "OB-03", "obligacion": "Informe trimestral del comité de riesgos", "fuente": "Política P-01", "tipo": "reporte",
         "responsable": p[0], "periodicidad": "trimestral", "dia_limite": "día 20", "criticidad": "alta", "ev": ["2026-09"]},
        {"id": "OB-04", "obligacion": "Certificación anual de la junta", "fuente": "Estatutos, artículo 40", "tipo": "certificación",
         "responsable": p[0], "periodicidad": "anual", "dia_limite": "2026-12-31", "criticidad": "media", "ev": []},
        {"id": "OB-05", "obligacion": "Capacitación mensual del personal nuevo", "fuente": "Política P-03", "tipo": "capacitación",
         "responsable": p[2], "periodicidad": "mensual", "dia_limite": "día 20", "criticidad": "baja", "ev": ["2026-07", "2026-08"]},
        {"id": "OB-06", "obligacion": "Reporte de operaciones del contratista de tecnología", "fuente": f"Contrato {code_c1} OBL-3", "tipo": "reporte",
         "responsable": p[1], "periodicidad": "mensual", "dia_limite": "día 5", "criticidad": "alta", "ev": PERIODOS},
        {"id": "OB-07", "obligacion": "Revisión semestral de la matriz de riesgos", "fuente": "Política P-01", "tipo": "registro",
         "responsable": p[0], "periodicidad": "semestral", "dia_limite": "día 30", "criticidad": "media", "ev": ["2026-07"]},
        {"id": "OB-08", "obligacion": "Actualización de datos de proveedores críticos", "fuente": "Política P-04", "tipo": "registro",
         "responsable": p[2], "periodicidad": "mensual", "dia_limite": "día 8", "criticidad": "media", "ev": PERIODOS},
    ]


def sembrar_constanza(e: dict, filas: list[dict], politicas: list[list], normas: list[list], casos: list[list], ext: dict, esperado: list,
                      code_c1: str, docs: Path) -> None:
    s, p = e["constanza"], e["personas"]
    if "obligacion_vencida" in s:      # vencía el 5 de octubre y no hay evidencia de septiembre
        filas.append({"id": "OB-09", "obligacion": "Reporte mensual de quejas", "fuente": "Política P-02", "tipo": "reporte", "responsable": p[2],
                      "periodicidad": "mensual", "dia_limite": "día 5", "criticidad": "alta", "ev": ["2026-07", "2026-08"]})
        esperado.append(("compliance_obligation_overdue", "oblig:OB-09"))
    if "cumplida_sin_evidencia" in s:
        filas.append({"id": "OB-10", "obligacion": "Declaración mensual de origen de fondos", "fuente": "Política P-04", "tipo": "registro", "responsable": p[1],
                      "periodicidad": "mensual", "dia_limite": "día 25", "criticidad": "media", "estado": "cumplida", "ev": ["2026-07", "2026-08"]})
        esperado.append(("compliance_done_without_evidence", "oblig:OB-10"))
    if "evidencia_vieja" in s:         # en plazo, y agosto tampoco tuvo
        filas.append({"id": "OB-11", "obligacion": "Monitoreo mensual de listas restrictivas", "fuente": "Política P-04", "tipo": "registro", "responsable": p[2],
                      "periodicidad": "mensual", "dia_limite": "día 25", "criticidad": "media", "ev": ["2026-07"]})
        esperado.append(("compliance_evidence_stale", "stale:OB-11"))
    if "sin_responsable" in s:
        filas.append({"id": "OB-12", "obligacion": "Registro de conflictos de interés", "fuente": "Política P-03", "tipo": "registro", "responsable": "",
                      "periodicidad": "mensual", "dia_limite": "día 10", "criticidad": "baja", "ev": PERIODOS})
        esperado.append(("obligation_without_owner", "duenio:OB-12"))
    if "sin_fuente" in s:
        filas.append({"id": "OB-13", "obligacion": "Reporte de regalos e invitaciones", "fuente": "", "tipo": "reporte", "responsable": p[2],
                      "periodicidad": "mensual", "dia_limite": "día 10", "criticidad": "baja", "ev": PERIODOS})
        esperado.append(("obligation_without_source", "fuente:OB-13"))
    if "obligacion_contrato_fuera" in s:   # la matriz dejó de citar la obligación del contrato
        next(f for f in filas if f["id"] == "OB-06")["fuente"] = "Política P-01"
        esperado.append(("contract_obligation_not_in_matrix", f"ctrobl:{code_c1}:OBL-3"))
    if "politica_vencida" in s:
        politicas[3][5] = "2026-08-31"
        esperado.append(("policy_review_overdue", "politica:P-03"))
    if "norma_sin_evaluar" in s:
        normas.append(["N-2026-05", "Circular sintética 005 de 2026", "2026-08-05", "2026-08-14", "por evaluar", "", p[1]])
        esperado.append(("regulatory_change_unassessed", "norma:N-2026-05"))
    if "norma_aplica_sin_matriz" in s:
        normas.append(["N-2026-04", "Resolución sintética 004 de 2026", "2026-05-28", "2026-06-01", "sí", "2026-06-20", p[1]])
        esperado.append(("applicable_norm_not_in_matrix", "aplica:N-2026-04"))
    if "norma_en_boletin" in s:        # llegó en un boletín del 25 de agosto y no está en el registro
        md(docs / "30-normativa" / "boletin-2026-08.md", """
# Boletín normativo de agosto

Recibido el 2026-08-25.

1. Circular sintética 007 de 2026 (N-2026-07): nuevas reglas de reporte de operaciones en efectivo. Pendiente de evaluar si aplica.
""")
        ext["new_rules"].append({"id": "N-2026-07", "rule": "Circular sintética 007 de 2026", "date": "2026-08-25", "applies": "por evaluar",
                                 "source": "30-normativa/boletin-2026-08.md, punto 1"})
        esperado.append(("regulatory_change_unassessed", "norma:N-2026-07"))
    if "caso_vencido" in s:
        casos.append(["C-003", "2026-08-28", "", "conflicto de interés", "abierto"])
        esperado.append(("report_case_overdue", "caso:C-003"))


# ================================================================ una entidad

def generar(e: dict) -> dict:
    sesion = SALIDA / e["carpeta"]
    ent_dir = f"{e['id']}-{slug(e['nombre'])}"
    docs = sesion / "legal" / ent_dir
    esperado: list[tuple[str, str]] = []
    u, p = e["u"], e["personas"]

    # Fidel
    cs = [contrato(e, i, b) for i, b in enumerate(BASE, 1)]
    sembrar_fidel(e, cs, esperado)
    if e["carpeta"] == "control-ec":   # el control de Ecuador decide su preaviso: renovar, con acta
        cs[3]["ficha"].update(end="2026-12-31", notice_days=60, decision={"action": "renovar", "date": "2026-09-25",
                                                                          "source": f"{cs[3]['carpeta']}/40-ejecucion/acta-comite-contratos.md"})
    for x in cs:
        completar(x)
    for x in cs:
        documentos_contrato(docs, e, x)
    registro = [["codigo", "contraparte", "objeto", "tipo", "valor", "inicio", "terminacion", "estado", "responsable"]]
    filas_pagos = [["contrato", "fecha", "valor", "documento"]]
    for x in cs:
        c = x["ficha"]
        fe = L.fin_efectivo(c, HOY, {})
        if x["registro"]:
            registro.append([c["code"], c["counterparty"]["name"], OBJETO[c["type"]], c["type"], f"{x['valor_registro'] or L.valor_total(c):.2f}",
                             c["start"], iso(L.fin_documentado(c)), x["estado_registro"] or ("vigente" if fe >= HOY else "terminado"), p[1]])
        for k, (f, v) in enumerate(pagos(x), 1):
            filas_pagos.append([c["code"], iso(f), f"{v:.2f}", f"CE-{c['code'][4:]}-{k:02d}"])
    if "registro_sin_documento" in e["fidel"]:
        code = f"CTR-{e['n0'] + 9}"
        registro.append([code, "Publicidad Exterior S.A.S.", "Publicidad en vallas", "servicios", f"{2 * u:.2f}", "2026-01-15", "2027-01-14", "vigente", p[1]])
        esperado.append(("register_mismatch", f"registro:{code}"))
    csv_(docs / "10-registro" / "registro-contratos.csv", registro)
    csv_(docs / "10-registro" / "pagos-2026-09-30.csv", filas_pagos)
    csv_(docs / "00-referencia" / "matriz-atribuciones.csv", [
        ["nombre", "cargo", "tipo", "monto_maximo", "desde", "hasta"],
        [p[0], "Gerente general", "todos", f"{50 * u:.0f}", "2024-01-01", ""],
        [p[1], "Vicepresidente financiero", "todos", f"{10 * u:.0f}", "2024-01-01", ""],
        [p[2], "Director de compras", "suministro", f"{3 * u:.0f}", "2024-01-01", ""],
    ])

    # Constanza
    code_c1 = cs[0]["ficha"]["code"]
    ext = {"declared": None, "new_rules": [], "questions": []}
    filas = matriz(e, code_c1)
    politicas = [["codigo", "politica", "version", "responsable", "aprobada", "proxima_revision"],
                 ["P-01", "Política de gestión de riesgos", "3", p[0], "2026-02-10", "2027-02-10"],
                 ["P-02", "Política de atención al cliente", "2", p[1], "2026-01-20", "2027-01-20"],
                 ["P-03", "Política de conflictos de interés", "4", p[2], "2025-11-15", "2026-11-15"],
                 ["P-04", "Política de conocimiento de proveedores", "1", p[1], "2026-03-01", "2027-03-01"]]
    normas = [["id", "norma", "publicada", "registrada", "aplica", "evaluacion", "responsable"],
              ["N-2026-01", "Resolución sintética 001 de 2026", "2026-03-02", "2026-03-10", "sí", "2026-03-30", p[1]],
              ["N-2026-02", "Circular sintética 002 de 2026", "2026-04-28", "2026-05-02", "no", "2026-05-20", p[1]]]
    casos = [["id", "recibido", "respondido", "tipo", "estado"],
             ["C-001", "2026-08-01", "2026-08-10", "trato al cliente", "cerrado"],
             ["C-002", "2026-09-25", "", "proveedores", "en investigación"]]
    sembrar_constanza(e, filas, politicas, normas, casos, ext, esperado, code_c1, docs)
    if not e["constanza"]:             # en los controles, una norma recién llegada por boletín: 8 días, sin señal
        md(docs / "30-normativa" / "boletin-2026-09.md", """
# Boletín normativo de septiembre

Recibido el 2026-09-28.

1. Circular sintética 009 de 2026 (N-2026-09): ajustes al formato de reporte mensual. Pendiente de evaluar si aplica.
""")
        ext["new_rules"].append({"id": "N-2026-09", "rule": "Circular sintética 009 de 2026", "date": "2026-09-28", "applies": "por evaluar",
                                 "source": "30-normativa/boletin-2026-09.md, punto 1"})
    cab = ["id", "obligacion", "fuente", "tipo", "responsable", "periodicidad", "dia_limite", "evidencia_esperada", "criticidad", "estado"]
    csv_(docs / "00-referencia" / "matriz-obligaciones.csv",
         [cab] + [[f["id"], f["obligacion"], f["fuente"], f["tipo"], f["responsable"], f["periodicidad"], f["dia_limite"],
                   f"Archivo que empieza por {f['id']}", f["criticidad"], f.get("estado", "")] for f in filas])
    for f in filas:
        for per in f["ev"]:
            md(docs / f"cumplimiento-{per}" / "10-evidencias" / f"{f['id']}_{slug(f['obligacion'])}-{per}.md",
               f"# {f['obligacion']}\n\nPeriodo {per}. Evidencia de {f['id']}.")
    csv_(docs / "20-politicas" / "indice-politicas.csv", politicas)
    for row in politicas[1:]:
        md(docs / "20-politicas" / f"politica-{row[0].lower()}-{slug(row[1])}.md", f"# {row[1]}\n\nCódigo {row[0]}, versión {row[2]}, aprobada el {row[4]}.")
    csv_(docs / "30-normativa" / "registro-normativo.csv", normas)
    csv_(docs / "40-canal" / "casos.csv", casos)
    declara = "cumplido" if ("informe_declara_cumplido" in e["constanza"] or not e["constanza"]) else "con observaciones"
    md(docs / "cumplimiento-2026-09" / "20-reportes" / "informe-cumplimiento-2026-09.md", f"""
# Informe de cumplimiento · septiembre de 2026

Fecha: 2026-10-05. Presenta: {p[1]}, oficial de cumplimiento.

Estado del periodo: **{declara}**.
""")
    ext["declared"] = {"status": declara, "date": "2026-10-05", "source": "cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md"}
    if "informe_declara_cumplido" in e["constanza"]:
        esperado.append(("declared_compliance_vs_evidence", "cumplimiento"))

    entidad = {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]}
    rutas = {"documents": f"legal/{ent_dir}", "state": f"estado-legal/{ent_dir}"}
    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "hoy": iso(HOY), "periodo": PERIODO,
             "siembra": {"fidel": e["fidel"], "constanza": e["constanza"]},
             "config": {"fidel": {"entity": entidad, "paths": rutas},
                        "constanza": {"entity": entidad, "paths": rutas, "period": PERIODO,
                                      "compliance": {"contract_records": f"estado-legal/{ent_dir}/contratos"}}},
             "extraccion": {"contratos": {x["ficha"]["code"]: x["ficha"] for x in cs}, "cumplimiento": ext},
             "esperado": sorted(({"signal": a, "key": b} for a, b in set(esperado)), key=lambda z: (z["signal"], z["key"]))}
    (sesion / "clave.json").write_text(json.dumps(clave, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return clave


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    total = 0
    for e in ENTIDADES:
        c = generar(copy.deepcopy(e))
        total += len(c["esperado"])
        n = len(e["fidel"]) + len(e["constanza"])
        print(f"  {e['carpeta']:13} {e['pais']}  {n:2} defectos sembrados · {len(c['esperado']):2} señales esperadas")
    print(f"\n  {len(ENTIDADES)} entidades, {total} señales en la clave, en {SALIDA.relative_to(RAIZ)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
