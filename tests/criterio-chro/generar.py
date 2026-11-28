#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CHRO: una entidad de banca, una de retail y una de tecnología,
y dos entidades de control.

    python3 tests/criterio-chro/generar.py          escribe tests/criterio-chro/material/

Cada entidad trae su carpeta de talento al 16 de noviembre de 2026: la política de selección y la
descarga del estándar de ocupaciones en `00-referencia/`, los perfiles de cargo, el registro de
vacantes, una carpeta por candidato con su hoja de vida y sus soportes, el registro de autorizaciones
y la exportación del ATS con la base de talento interna.

**El estándar es sintético y tiene la forma exacta de la descarga oficial.** Las entidades de Colombia
usan un libro con las hojas y las columnas de los perfiles ocupacionales de la CUOC 2026 del DANE
(F-03); las de México, Chile y Perú, una carpeta con los archivos y las columnas de O*NET 31.0 (F-02).
Las ocupaciones llevan códigos con la forma del estándar y nombres marcados como sintéticos: ninguna es
la del estándar real.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal
esperada queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los
documentos escritos —cada perfil con sus tareas y sus requisitos, cada hoja de vida con sus
afirmaciones, sus soportes y lo que llegó y no se debe tratar— y la configuración que deja el setup. El
motor no la ve; `evaluar.py` compara lo que el motor levanta contra ella, y una señal de más cuenta
igual que una de menos.

**La prueba de sesgo.** Cada entidad trae pares de candidatos iguales salvo en un dato protegido —la
fotografía, la fecha de nacimiento, el sexo, el estado civil—: el motor tiene que entregar exactamente
lo mismo para los dos miembros de cada par, salvo el aviso de lo que excluyó.

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: lo que el
perfil excluye del estándar con su motivo, un nivel de estudios por debajo con la experiencia como
alternativa, un conocimiento de «seguridad y salud en el trabajo», una revisión que vence mañana, una
vacante con su propio plazo más largo, una autorización del mismo día de la postulación, un empleo con
el mismo mes y otro día, una certificación que vence después, una conservación que vence hoy, una brecha
entre dos empleos y un diploma escaneado en imagen. Todo es determinista: el mismo material cada vez,
byte a byte. Los nombres, las empresas, las personas y los documentos son inventados.
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-roles" / "scripts"))
import talento as T  # noqa: E402
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import formatos as FMT  # noqa: E402  (Word, Excel y PDF sin dependencias y con fecha fija, los mismos de las demás familias)

SALIDA = AQUI / "material"
HOY, PERIODO = dt.date(2026, 11, 16), "2026-11"
JPG = b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xd9"


RECURSOS = Path(__file__).resolve().parent / "recursos"


def diploma_escaneado(titulo: str) -> bytes:
    """Un diploma escaneado en imagen, con su texto: quien lo abre ve que es el soporte del título.
    La imagen se dibuja una vez y se versiona en recursos/ —un codificador JPEG distinto daría otros
    bytes en otra máquina—; `--recursos` la vuelve a dibujar."""
    ruta = RECURSOS / f"diploma-{slug(titulo)}.jpg"
    if "--recursos" in sys.argv:
        import io
        import unicodedata
        from PIL import Image, ImageDraw, ImageFont
        mayus = lambda t: "".join(c for c in unicodedata.normalize("NFD", t.upper()) if unicodedata.category(c) != "Mn")  # noqa: E731
        im = Image.new("RGB", (900, 600), (250, 248, 240))
        d = ImageDraw.Draw(im)
        d.rectangle((20, 20, 879, 579), outline=(60, 60, 60), width=4)
        f = ImageFont.load_default(size=34)
        for y, t in ((120, "Universidad Sintética del Valle"), (230, "Diploma"), (320, "Otorga el título de"), (390, titulo), (480, "2018")):
            t = mayus(t)
            d.text(((900 - d.textlength(t, font=f)) / 2, y), t, fill=(30, 30, 30), font=f)
        b = io.BytesIO()
        im.save(b, format="JPEG", quality=85)
        RECURSOS.mkdir(exist_ok=True)
        ruta.write_bytes(b.getvalue())
    if not ruta.is_file():
        raise SystemExit(f"falta {ruta.name} en tests/criterio-chro/recursos/: corre generar.py --recursos")
    return ruta.read_bytes()


def slug(t: str) -> str:
    return T.norm(t).replace("_", "-")


def documento(ruta: Path, md: str) -> str:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if ruta.suffix == ".docx":
        FMT.a_docx(md, ruta)
    elif ruta.suffix == ".pdf":
        FMT.a_pdf(md, ruta)
    else:
        ruta.write_text(md, encoding="utf-8")
    return ruta.name


def tabla(ruta: Path, filas: list[list]) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if ruta.suffix == ".xlsx":
        FMT.a_xlsx_tipado(filas, ruta, "Hoja1")
    else:
        ruta.write_text("\n".join(";".join(str(x) for x in f) for f in filas) + "\n", encoding="utf-8")


# ================================================================ los estándares sintéticos

# Cada ocupación: código, nombre, nivel (CUOC) o zona (O*NET), destrezas y conocimientos —en O*NET con su
# importancia—, funciones, denominaciones y afines.
CUOC = {
    "24111": dict(n="Contadores sintéticos", nivel=4, ciuo="2411", d=[("27", "Análisis de procesos"), ("9", "Evaluación y control de actividades")],
                  c=[("5", "Contabilidad"), ("7", "Legislación tributaria")], f=["Preparar los estados financieros", "Revisar los registros contables"],
                  den=["Contador / Contadora", "Contador público / Contadora pública"], af=["43111"]),
    "33121": dict(n="Analistas de crédito sintéticos", nivel=3, ciuo="3312", d=[("17", "Análisis de necesidades"), ("28", "Criterio y toma de decisiones")],
                  c=[("12", "Finanzas"), ("5", "Contabilidad")], f=["Analizar las solicitudes de crédito", "Verificar la documentación de los solicitantes"],
                  den=["Analista de crédito"], af=["24111"]),
    "43111": dict(n="Auxiliares contables sintéticos", nivel=2, ciuo="4311", d=[("1", "Comprensión de lectura")], c=[("5", "Contabilidad")],
                  f=["Registrar las facturas y los comprobantes"], den=["Auxiliar contable"], af=["24111"]),
    "42111": dict(n="Cajeros de banco sintéticos", nivel=2, ciuo="4211", d=[("4", "Comunicación asertiva")], c=[("40", "Atención al cliente")],
                  f=["Recibir y pagar dinero en la ventanilla"], den=["Cajero de banco / Cajera de banco"], af=["43111"]),
    "12110": dict(n="Directores financieros sintéticos", nivel=4, ciuo="1211", d=[("28", "Criterio y toma de decisiones")], c=[("12", "Finanzas"), ("1", "Gerencia y administración")],
                  f=["Dirigir la planeación financiera"], den=["Director financiero / Directora financiera"], af=["24111"]),
    "25120": dict(n="Desarrolladores de software sintéticos", nivel=4, ciuo="2512", d=[("21", "Programación"), ("18", "Diseño de tecnología")], c=[("30", "Informática")],
                  f=["Desarrollar y probar programas"], den=["Desarrollador de software / Desarrolladora de software"], af=[]),
}
ONET = {
    "41-2011.00": dict(n="Cashiers (synthetic)", zona=2, d=[("2.A.1.b", "Active Listening", 3.8), ("2.A.1.e", "Mathematics", 3.6), ("2.A.1.d", "Speaking", 3.2)],
                       c=[("2.C.1.e", "Customer and Personal Service", 4.1), ("2.C.4.a", "Mathematics", 3.0)], f=["Receive payment from customers"], af=["41-1011.00"]),
    "41-1011.00": dict(n="First-Line Supervisors of Retail Sales Workers (synthetic)", zona=3, d=[("2.B.1.a", "Social Perceptiveness", 3.9), ("2.B.3.a", "Coordination", 3.7)],
                       c=[("2.C.1.c", "Sales and Marketing", 3.8)], f=["Direct and supervise sales workers"], af=["41-2011.00"]),
    "43-5081.00": dict(n="Stockers and Order Fillers (synthetic)", zona=2, d=[("2.A.1.b", "Active Listening", 3.1)], c=[], f=["Receive and store items"], af=[]),
    "15-1252.00": dict(n="Software Developers (synthetic)", zona=4, d=[("2.B.3.e", "Programming", 4.2), ("2.A.2.a", "Critical Thinking", 3.9)],
                       c=[("2.C.3.a", "Computers and Electronics", 4.4)], f=["Write and test code"], af=["15-1232.00"]),
    "15-1232.00": dict(n="Computer User Support Specialists (synthetic)", zona=3, d=[("2.A.1.b", "Active Listening", 3.7), ("2.B.5.a", "Troubleshooting", 3.9)],
                       c=[("2.C.3.a", "Computers and Electronics", 4.0)], f=["Answer user inquiries"], af=["15-1252.00"]),
    "15-1212.00": dict(n="Information Security Analysts (synthetic)", zona=4, d=[("2.A.2.a", "Critical Thinking", 4.0)], c=[("2.C.3.a", "Computers and Electronics", 4.3)],
                       f=["Monitor networks for security breaches"], af=["15-1252.00"]),
}
# Cada cuánto se revisa un perfil: lo fija la política de selección de cada entidad, y de ahí lo toma el setup.
REVISION_MESES = 12
CUOC_ARCHIVO = "00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx"
ONET_CARPETA = "00-referencia/onet-31-0-sintetico"


def escribir_cuoc(ruta: Path, codigos: list[str]) -> None:
    C, N_ = T.CUOC_CODIGO, T.CUOC_NOMBRE
    cab = lambda *x: [["CLASIFICACIÓN ÚNICA DE OCUPACIONES PARA COLOMBIA · VERSIÓN SINTÉTICA PARA PRUEBAS"], ["Código del Gran Grupo", C, N_, *x]]  # noqa: E731
    h = {"Ocupación": [["CLASIFICACIÓN ÚNICA DE OCUPACIONES PARA COLOMBIA · VERSIÓN SINTÉTICA PARA PRUEBAS"],
                       ["Código del Gran Grupo", "Nombre del Gran Grupo", "Código del Subgrupo Principal", "Nombre del Subgrupo Principal",
                        "Código del Subgrupo", "Nombre del Subgrupo", "Código del Grupo Primario", "Nombre del Grupo Primario", C, N_]],
         "Descripción": cab("Descripción de la Ocupación"), "Funciones": cab("Consecutivo de la Función", "Funciones de la Ocupación"),
         "Denominaciones": cab("Código de la Denominación", "Nombre de la Denominación"), "Nivel Competencia": cab("Nivel de Competencia"),
         "Conocimientos": cab("ID", "Nombre del Conocimiento"), "Destrezas": cab("ID", "Nombre de la Destreza"),
         "Ocupaciones Afines": cab("Código de la Ocupación Afin", "Nombre de la Ocupación Afin"),
         "Equivalencias": [["x"], [C, N_, "Código CIUO-08", "Observaciones sobre la CIUO-08"]]}
    for c in codigos:
        o = CUOC[c]
        g = c[0]
        h["Ocupación"].append([g, "x", c[:2], "x", c[:3], "x", c[:4], "x", c, o["n"]])
        h["Descripción"].append([g, c, o["n"], o["f"][0] + "."])
        h["Funciones"] += [[g, c, o["n"], str(i), f + "."] for i, f in enumerate(o["f"], 1)]
        h["Denominaciones"] += [[g, c, o["n"], f"{c}.{i:03d}", d] for i, d in enumerate(o["den"], 1)]
        h["Nivel Competencia"].append([g, c, o["n"], str(o["nivel"])])
        h["Conocimientos"] += [[g, c, o["n"], i, n] for i, n in o["c"]]
        h["Destrezas"] += [[g, c, o["n"], i, n] for i, n in o["d"]]
        h["Ocupaciones Afines"] += [[g, c, o["n"], a, CUOC[a]["n"]] for a in o["af"] if a in codigos]
        h["Equivalencias"].append([c, o["n"], o["ciuo"], "Denominaciones completas"])
    T.escribir_xlsx_hojas(ruta, h)


def escribir_onet(carpeta: Path, codigos: list[str]) -> None:
    def xl(nombre, filas):
        (carpeta / nombre).parent.mkdir(parents=True, exist_ok=True)
        FMT.a_xlsx_tipado(filas, carpeta / nombre, nombre.split(".")[0])
    xl("Occupation Data.xlsx", [["O*NET-SOC Code", "Title", "Description"]] + [[c, ONET[c]["n"], ONET[c]["f"][0] + "."] for c in codigos])
    xl("Task Statements.xlsx", [["O*NET-SOC Code", "Title", "Task ID", "Task", "Task Type"]] +
       [[c, ONET[c]["n"], str(1000 + i), f, "Core"] for c in codigos for i, f in enumerate(ONET[c]["f"])])
    xl("Job Zones.xlsx", [["O*NET-SOC Code", "Title", "Job Zone", "Date", "Domain Source"]] + [[c, ONET[c]["n"], str(ONET[c]["zona"]), "08/2026", "Analyst"] for c in codigos])
    cab = ["O*NET-SOC Code", "Title", "Element ID", "Element Name", "Scale ID", "Scale Name", "Data Value", "N", "Standard Error",
           "Lower CI Bound", "Upper CI Bound", "Recommend Suppress", "Not Relevant", "Date"]
    for nombre, k in (("Essential Skills.xlsx", "d"), ("Knowledge.xlsx", "c")):
        filas = [cab]
        for c in codigos:
            for i, n, v in ONET[c][k]:
                filas.append([c, ONET[c]["n"], i, n, "IM", "Importance", str(v), "8", "0.1", "", "", "N", "", "08/2026"])
                filas.append([c, ONET[c]["n"], i, n, "LV", "Level", "3.5", "8", "0.1", "", "", "N", "N", "08/2026"])
        xl(nombre, filas)


def tipo(est: str, codigo: str, nombre: str) -> str:
    """Destreza o conocimiento, según la lista del estándar en que está el elemento."""
    o = CUOC[codigo] if est == "cuoc" else ONET[codigo]
    return "destreza" if any(x[1] == nombre for x in o["d"]) else "conocimiento"


# El tipo de cada requisito, con el título con que el perfil lo agrupa: el perfil lo dice, no se adivina.
GRUPOS = [("conocimiento", "Conocimientos"), ("destreza", "Destrezas"), ("estudio", "Estudios"), ("experiencia", "Experiencia"),
          ("certificacion", "Certificaciones"), ("otro", "Otros requisitos")]


def elemento(est: str, codigo: str, nombre: str) -> str:
    """El identificador del elemento del estándar, como lo trae su descarga."""
    if est == "cuoc":
        o = CUOC[codigo]
        for i, n in o["d"]:
            if n == nombre:
                return f"D{i}"
        for i, n in o["c"]:
            if n == nombre:
                return f"C{i}"
    else:
        for k in ("d", "c"):
            for i, n, _ in ONET[codigo][k]:
                if n == nombre:
                    return i
    raise KeyError(nombre)


# ================================================================ las entidades

def R(i, txt, tareas=("T1",), **k):
    return {"id": i, "text": txt, "tasks": list(tareas), **k}


ENTIDADES = [
 {"carpeta": "banca-co", "industria": "banca", "pais": "CO", "id": "901555123", "nombre": "Banco Cordillera Sintético", "moneda": "COP", "est": "cuoc",
  "ocupaciones": ["24111", "33121", "43111", "42111", "12110"], "siembra": True, "plazo": 45, "conserva": 180,
  "prohibidos": ["edad", "sexo", "estado civil", "fotografía"], "niveles": {"Bachiller": 3, "Técnico laboral": 4, "Tecnólogo": 5, "Profesional": 6, "Especialización": 7},
  "perfiles": [
   dict(id="PC-01", t="Contador", occ="24111", ed="Profesional", last="2025-03-01",
        tasks=["Preparar los estados financieros mensuales", "Revisar los registros contables"],
        reqs=[R("R1", "Contabilidad bajo NIIF", ["T1"], element="Contabilidad", essential=True), R("R2", "Análisis de procesos contables", ["T2"], element="Análisis de procesos", essential=True),
              R("R3", "Evaluación y control de actividades del área", ["T2"], element="Evaluación y control de actividades"),
              R("R4", "Tarjeta profesional de contador vigente", ["T1"], type="certificacion", essential=True)],
        siembra=[("essential_skill_missing", "elemento:PC-01:c7"), ("profile_review_overdue", "revision:PC-01")]),
   dict(id="PC-02", t="Contador de impuestos", occ="24111", ed="Profesional", nxt="2027-03-01",
        tasks=["Preparar los estados financieros mensuales", "Revisar los registros contables"],
        reqs=[R("R1", "Contabilidad bajo NIIF", ["T1"], element="Contabilidad"), R("R2", "Análisis de procesos contables", ["T2"], element="Análisis de procesos"),
              R("R3", "Evaluación y control de actividades del área", ["T2"], element="Evaluación y control de actividades"),
              R("R4", "Legislación tributaria colombiana", ["T1"], element="Legislación tributaria"), R("R5", "Hombre menor de 35 años", [])],
        siembra=[("profiles_overlap", "solape:PC-01:PC-02"), ("requirement_not_allowed", "prohibido:PC-02:R5:edad"),
                 ("requirement_not_allowed", "prohibido:PC-02:R5:sexo"), ("requirement_without_task", "tarea:PC-02:R5")]),
   dict(id="PC-03", t="Auxiliar contable", occ="43111", ed="Profesional", nxt="2027-02-01",
        tasks=["Registrar las facturas y los comprobantes"],
        reqs=[R("R1", "Comprensión de lectura de documentos contables", element="Comprensión de lectura"), R("R2", "Contabilidad básica", element="Contabilidad", essential=True)],
        siembra=[("education_level_inconsistent", "estudios:PC-03")]),
   dict(id="PC-04", t="Analista de crédito", occ="33121", ed="Tecnólogo", nxt="2027-04-01",
        tasks=["Analizar las solicitudes de crédito", "Verificar la documentación de los solicitantes"],
        reqs=[R("R1", "Finanzas y análisis de estados financieros", ["T1"], element="Finanzas", essential=True), R("R2", "Contabilidad", ["T1"], element="Contabilidad"),
              R("R3", "Criterio y toma de decisiones de crédito", ["T1"], element="Criterio y toma de decisiones", essential=True),
              R("R4", "Gozar de buen estado de salud", ["T2"])],
        siembra=[("essential_skill_missing", "elemento:PC-04:d17"), ("requirement_not_allowed", "prohibido:PC-04:R4:salud")]),
   dict(id="PC-05", t="Cajero", occ="42999", ed="Bachiller", nxt="2027-05-01", tasks=["Recibir y pagar dinero en la ventanilla"],
        reqs=[R("R1", "Atención al cliente en ventanilla", essential=True)], siembra=[("profile_without_occupation", "ocupacion:PC-05")]),
   dict(id="PC-06", t="Coordinador de cobranzas", occ=None, ed="Profesional", nxt="2027-05-01", tasks=["Coordinar la gestión de cobranza"],
        reqs=[R("R1", "Experiencia en cobranza de cartera", essential=True), R("R2", "Estado civil casado")],
        siembra=[("profile_without_occupation", "ocupacion:PC-06"), ("requirement_not_allowed", "prohibido:PC-06:R2:estado_civil")]),
   dict(id="PC-07", t="Director financiero", occ="12110", ed="Bachiller", nxt="2027-01-15", tasks=["Dirigir la planeación financiera"],
        reqs=[R("R1", "Finanzas corporativas", element="Finanzas"), R("R2", "Gerencia y administración", element="Gerencia y administración"),
              R("R3", "Criterio y toma de decisiones", element="Criterio y toma de decisiones"), R("R4", "Dominio del inglés de negocios", [])],
        siembra=[("education_level_inconsistent", "estudios:PC-07"), ("requirement_without_task", "tarea:PC-07:R4")]),
  ],
  "vacantes": [("VAC-01", "PC-01", "2026-08-01", "", None, "Lucía Paredes"), ("VAC-02", "PC-04", "2026-10-20", "", None, "Lucía Paredes"),
               ("VAC-03", "PC-03", "2026-02-01", "2026-03-10", None, "Andrés Mora"),
               ("VAC-04", "PC-07", "2026-07-01", "", 90, "Andrés Mora")],
  "vac_siembra": [("vacancy_past_target", "vacante:vac_01"), ("vacancy_past_target", "vacante:vac_04")],
 },
 {"carpeta": "retail-mx", "industria": "retail", "pais": "MX", "id": "TBA110315K21", "nombre": "Tiendas del Bajío Sintéticas", "moneda": "MXN", "est": "onet",
  "ocupaciones": ["41-2011.00", "41-1011.00", "43-5081.00"], "siembra": True, "plazo": 30, "conserva": 120, "umbral": 3.5,
  "prohibidos": ["edad", "sexo", "estado civil", "fotografía", "apariencia"], "niveles": {},
  "perfiles": [
   dict(id="PT-01", t="Cajero de tienda", occ="41-2011.00", ed="Secundaria", last="2025-01-10", tasks=["Cobrar a los clientes en caja"],
        reqs=[R("R1", "Escucha activa con el cliente", element="Active Listening", essential=True), R("R2", "Matemáticas para el arqueo de caja", element="Mathematics", essential=True),
              R("R3", "Buena presencia", [])],
        siembra=[("essential_skill_missing", "elemento:PT-01:2_c_1_e"), ("profile_review_overdue", "revision:PT-01"),
                 ("requirement_not_allowed", "prohibido:PT-01:R3:apariencia"), ("requirement_without_task", "tarea:PT-01:R3")]),
   dict(id="PT-02", t="Cajero de autoservicio", occ="41-2011.00", ed="Secundaria", nxt="2027-02-01", tasks=["Cobrar a los clientes en caja"],
        reqs=[R("R1", "Escucha activa con el cliente", element="Active Listening"), R("R2", "Matemáticas para el arqueo de caja", element="Mathematics"),
              R("R3", "Servicio al cliente", element="Customer and Personal Service")],
        siembra=[("profiles_overlap", "solape:PT-01:PT-02")]),
   dict(id="PT-03", t="Supervisor de tienda", occ="41-1011.00", ed="Licenciatura", nxt="2027-02-01", tasks=["Dirigir y supervisar a los vendedores"],
        reqs=[R("R1", "Coordinación del equipo de ventas", element="Coordination", essential=True), R("R2", "Percepción social", element="Social Perceptiveness"),
              R("R3", "Ventas y mercadeo", element="Sales and Marketing"), R("R4", "Profesar la religión católica")],
        siembra=[("requirement_not_allowed", "prohibido:PT-03:R4:religion")]),
   dict(id="PT-04", t="Almacenista", occ="", ed="Secundaria", nxt="2027-02-01", tasks=["Recibir y acomodar la mercancía"],
        reqs=[R("R1", "Manejo de inventario", essential=True), R("R2", "Mujer entre 20 y 30 años")],
        siembra=[("profile_without_occupation", "ocupacion:PT-04"), ("requirement_not_allowed", "prohibido:PT-04:R2:edad"),
                 ("requirement_not_allowed", "prohibido:PT-04:R2:sexo")]),
  ],
  "vacantes": [("VAC-11", "PT-01", "2026-09-15", "", None, "Mariana Ríos"), ("VAC-12", "PT-03", "2026-10-25", "", None, "Mariana Ríos"),
               ("VAC-13", "PT-02", "2026-03-01", "2026-04-10", None, "Mariana Ríos"),
               ("VAC-14", "PT-04", "2026-10-01", "", None, "Mariana Ríos")],
  "vac_siembra": [("vacancy_past_target", "vacante:vac_11"), ("vacancy_past_target", "vacante:vac_14")],
 },
 {"carpeta": "tecnologia-cl", "industria": "tecnologia", "pais": "CL", "id": "76543210-K", "nombre": "Nube Austral Software Sintética", "moneda": "CLP", "est": "onet",
  "ocupaciones": ["15-1252.00", "15-1232.00", "15-1212.00"], "siembra": True, "plazo": 60, "conserva": 90, "umbral": 3.5,
  "prohibidos": ["edad", "sexo", "estado civil", "fotografía"], "niveles": {},
  "perfiles": [
   dict(id="TI-01", t="Desarrollador de software", occ="15-1252.00", ed="Ingeniería", nxt="2026-10-01", tasks=["Escribir y probar código"],
        reqs=[R("R1", "Programación en Python y Java", element="Programming", essential=True), R("R2", "Pensamiento crítico", element="Critical Thinking")],
        siembra=[("essential_skill_missing", "elemento:TI-01:2_c_3_a"), ("profile_review_overdue", "revision:TI-01")]),
   dict(id="TI-02", t="Analista de soporte", occ="15-1232.00", ed="Técnico", nxt="2027-03-01", tasks=["Atender las consultas de los usuarios"],
        reqs=[R("R1", "Escucha activa", element="Active Listening"), R("R2", "Resolución de fallas", element="Troubleshooting", essential=True),
              R("R3", "Computadores y electrónica", element="Computers and Electronics"), R("R4", "Nivel socioeconómico medio alto", [])],
        siembra=[("requirement_not_allowed", "prohibido:TI-02:R4:socioeconomica"), ("requirement_without_task", "tarea:TI-02:R4")]),
   dict(id="TI-03", t="Analista de seguridad", occ="15-1212.00", ed="Ingeniería", nxt="2027-03-01", tasks=["Vigilar las redes"],
        reqs=[R("R1", "Pensamiento crítico", element="Critical Thinking", essential=True), R("R2", "Computadores y electrónica", element="Computers and Electronics"),
              R("R3", "No pertenecer a ningún sindicato")],
        siembra=[("requirement_not_allowed", "prohibido:TI-03:R3:sindical")]),
   dict(id="TI-04", t="Desarrollador backend", occ="15-1252.00", ed="Ingeniería", nxt="2027-03-01", tasks=["Escribir y probar código"],
        reqs=[R("R1", "Programación en Python y Java", element="Programming"), R("R2", "Pensamiento crítico", element="Critical Thinking"),
              R("R3", "Computadores y electrónica", element="Computers and Electronics")],
        siembra=[("profiles_overlap", "solape:TI-01:TI-04")]),
   dict(id="TI-05", t="Líder técnico", occ="15-9999.00", ed="Ingeniería", nxt="2027-03-01", tasks=["Liderar el equipo de desarrollo"],
        reqs=[R("R1", "Liderazgo técnico", essential=True)], siembra=[("profile_without_occupation", "ocupacion:TI-05")]),
  ],
  "vacantes": [("VAC-21", "TI-01", "2026-08-10", "", None, "Tomás Vidal"), ("VAC-22", "TI-03", "2026-10-30", "", None, "Tomás Vidal"),
               ("VAC-23", "TI-02", "2026-06-01", "2026-07-20", None, "Tomás Vidal"),
               ("VAC-24", "TI-05", "2026-09-01", "", 45, "Tomás Vidal")],
  "vac_siembra": [("vacancy_past_target", "vacante:vac_21"), ("vacancy_past_target", "vacante:vac_24")],
 },
 {"carpeta": "control-co", "industria": "banca", "pais": "CO", "id": "900777888", "nombre": "Cooperativa Control Sintética", "moneda": "COP", "est": "cuoc",
  "ocupaciones": ["24111", "43111", "25120"], "siembra": False, "plazo": 45, "conserva": 180,
  "prohibidos": ["edad", "sexo", "estado civil", "fotografía"], "niveles": {"Bachiller": 3, "Técnico laboral": 4, "Tecnólogo": 5, "Profesional": 6},
  "perfiles": [
   dict(id="PC-11", t="Contador", occ="24111", ed="Profesional", nxt="2026-11-17", tasks=["Preparar los estados financieros", "Revisar los registros contables"],
        reqs=[R("R1", "Contabilidad bajo NIIF", ["T1"], element="Contabilidad", essential=True), R("R2", "Análisis de procesos", ["T2"], element="Análisis de procesos"),
              R("R3", "Evaluación y control de actividades", ["T2"], element="Evaluación y control de actividades"),
              R("R4", "Conocimiento del sistema de gestión de seguridad y salud en el trabajo", ["T2"]),
              R("R5", "Tarjeta profesional de contador vigente", ["T1"], type="certificacion", essential=True)],
        na=[{"element": "Legislación tributaria", "reason": "la lleva el área de impuestos"}], siembra=[]),
   dict(id="PC-12", t="Auxiliar contable", occ="43111", ed="Técnico laboral", nxt="2027-01-01", tasks=["Registrar las facturas y los comprobantes"],
        reqs=[R("R1", "Comprensión de lectura", element="Comprensión de lectura"), R("R2", "Contabilidad básica", element="Contabilidad", essential=True)], siembra=[]),
   dict(id="PC-13", t="Desarrollador de software", occ="25120", ed="Tecnólogo", exp=True, nxt="2027-01-01", tasks=["Desarrollar y probar programas"],
        reqs=[R("R1", "Programación", element="Programación", essential=True), R("R2", "Diseño de tecnología", element="Diseño de tecnología"),
              R("R3", "Informática", element="Informática")], siembra=[]),
  ],
  "vacantes": [("VAC-31", "PC-11", "2026-10-05", "", None, "Rosa Díaz"), ("VAC-32", "PC-13", "2026-08-01", "", 120, "Rosa Díaz"),
               ("VAC-33", "PC-12", "2026-04-01", "2026-05-20", None, "Rosa Díaz")],
  "vac_siembra": [],
 },
 {"carpeta": "control-pe", "industria": "tecnologia", "pais": "PE", "id": "20601234567", "nombre": "Servicios Andinos Control Sintéticos", "moneda": "PEN", "est": "onet",
  "ocupaciones": ["15-1232.00", "41-2011.00"], "siembra": False, "plazo": 40, "conserva": 150, "umbral": 3.5,
  "prohibidos": ["edad", "sexo", "estado civil", "fotografía"], "niveles": {},
  "perfiles": [
   dict(id="SA-01", t="Analista de soporte", occ="15-1232.00", ed="Técnico", nxt="2027-02-01", tasks=["Atender las consultas de los usuarios"],
        reqs=[R("R1", "Escucha activa", element="Active Listening"), R("R2", "Resolución de fallas", element="Troubleshooting", essential=True),
              R("R3", "Computadores y electrónica", element="Computers and Electronics")], siembra=[]),
   dict(id="SA-02", t="Cajero", occ="41-2011.00", ed="Secundaria", nxt="2027-02-01", tasks=["Cobrar a los clientes en caja"],
        reqs=[R("R1", "Escucha activa", element="Active Listening"), R("R2", "Matemáticas", element="Mathematics", essential=True)],
        na=[{"element": "Customer and Personal Service", "reason": "la caja no atiende reclamos: los atiende el área de servicio"}], siembra=[]),
  ],
  "vacantes": [("VAC-41", "SA-01", "2026-10-10", "", None, "Jorge Salas"), ("VAC-43", "SA-02", "2026-11-05", "", None, "Jorge Salas"),
               ("VAC-42", "SA-02", "2026-05-01", "2026-06-19", None, "Jorge Salas")],
  "vac_siembra": [],
 },
]

# Grupo D: Ecuador, con el retail. La misma tienda que la de México —sus perfiles, sus requisitos y lo que
# se siembra—, con su país, su moneda, su reclutadora y sus vacantes: lo que se prueba es que Norma y
# Cándido lean la ley de datos de Ecuador (datos_sensibles.json) sobre los mismos documentos.
def _retail_ec():
    import copy
    e = copy.deepcopy(next(x for x in ENTIDADES if x["carpeta"] == "retail-mx"))
    e.update(carpeta="retail-ec", pais="EC", id="1792345678001", nombre="Almacenes del Pacífico Sintéticos", moneda="USD")
    e["vacantes"] = [(v.replace("VAC-1", "VAC-5"), pf, a, b, c, "Gabriela Andrade") for v, pf, a, b, c, _ in e["vacantes"]]
    e["vac_siembra"] = [(t, k.replace("vac_1", "vac_5")) for t, k in e["vac_siembra"]]
    return e


ENTIDADES.insert(3, _retail_ec())

# Los candidatos de cada entidad: su vacante, lo que afirma, sus soportes y lo que siembra. `par` marca la
# prueba de sesgo: el segundo miembro es el primero con un dato protegido de más, nada más.
def candidatos(e: dict) -> list[dict]:
    v = {x[0]: x for x in e["vacantes"]}
    pv = [x[0] for x in e["vacantes"]]
    abierta, abierta2, cerrada = pv[0], pv[1], pv[2]
    perf = {p["id"]: p for p in e["perfiles"]}
    p1 = perf[v[abierta][1]]
    cert = next((r for r in p1["reqs"] if r.get("type") == "certificacion"), None)
    ess = [r for r in p1["reqs"] if r.get("essential") and r.get("type") != "certificacion"]
    pref = {"banca-co": "1", "retail-mx": "2", "tecnologia-cl": "3", "control-co": "4", "control-pe": "5", "retail-ec": "6"}[e["carpeta"]]
    C = lambda n: f"CAN-{pref}{n:02d}"  # noqa: E731
    base_emp = {"empresa": "Comercial Andina Sintética", "desde": "2019-03", "hasta": "2022-08", "cert_desde": "2019-03-01", "cert_hasta": "2022-08-31"}

    def cand(n, vac, **k):
        d = {"id": C(n), "vac": vac, "recibido": "2026-09-05" if vac != cerrada else "2026-02-10", "autoriza": "same", "titulo": True, "titulo_soporte": True,
             "empleo": dict(base_emp), "cert": cert is not None and vac == abierta, "cert_vence": "2027-06-30", "cert_soporte": True,
             "evid": [r["id"] for r in (ess if vac == abierta else [r for r in perf[v[vac][1]]["reqs"] if r.get("essential")])], "protegidos": [],
             "estado": "Entrevista", "fecha_estado": "2026-10-01", "foto_soporte": False, "siembra": []}
        d.update(k)
        return d
    if not e["siembra"]:
        L = [cand(1, abierta), cand(2, abierta, autoriza="same"),
             cand(3, abierta, empleo=dict(base_emp, cert_desde="2019-03-20", cert_hasta="2022-08-05")),   # el mismo mes, otro día
             cand(4, abierta, cert_vence="2026-11-30"),                                                     # vence después
             cand(5, abierta, empleo=dict(base_emp, hasta="2020-12", cert_hasta="2020-12-31"), segundo=True),  # una brecha
             cand(6, abierta, foto_soporte=True),                                                           # un diploma escaneado en imagen
             cand(7, abierta, protegidos=[]), cand(8, abierta, protegidos=["sexo"], siembra=[("protected_data_received", f"protegido:{C(8)}:sexo")]),
             cand(9, cerrada, estado="No seleccionado", fecha_estado=(HOY - dt.timedelta(days=e["conserva"])).isoformat(), recibido=v[cerrada][2]),
             cand(10, abierta2, recibido="2026-11-01")]
        # Un dato que llegó y se excluye no es un defecto del candidato: es el aviso. En el control se espera
        # solo ese aviso, para que el par de sesgo exista también aquí.
        return L
    L = [cand(1, abierta, evid=[r["id"] for r in ess[1:]], siembra=[("requirement_not_evidenced", f"requisito:{C(1)}:{ess[0]['id']}")]),
         cand(2, abierta, titulo_soporte=False, protegidos=["fotografia"], siembra=[("claim_without_support", f"soporte:{C(2)}:K1"),
                                                                                      ("protected_data_received", f"protegido:{C(2)}:fotografia")]),
         cand(3, abierta, empleo=dict(base_emp, cert_hasta="2021-12-31"), siembra=[("employment_dates_differ", f"fechas:{C(3)}:K2")]),
         cand(4, abierta, autoriza=None, siembra=[("consent_missing", f"autorizacion:{C(4)}")]),
         cand(5, abierta, protegidos=[]), cand(6, abierta, protegidos=["fotografia", "fecha_de_nacimiento"],
                                               siembra=[("protected_data_received", f"protegido:{C(6)}:fotografia"),
                                                        ("protected_data_received", f"protegido:{C(6)}:fecha_de_nacimiento")]),
         cand(7, abierta2, autoriza="tarde", siembra=[("consent_missing", f"autorizacion:{C(7)}")]),
         cand(8, abierta2, titulo=False, empleo=None, evid=[], siembra=[(("requirement_not_evidenced", f"requisito:{C(8)}:{r['id']}"))
                                                                      for r in perf[v[abierta2][1]]["reqs"] if r.get("essential")]),
         cand(9, cerrada, estado="No seleccionado", fecha_estado=(HOY - dt.timedelta(days=e["conserva"] + 40)).isoformat(), recibido=v[cerrada][2],
              siembra=[("retention_exceeded", f"conservacion:{C(9)}")])]
    if cert:
        L.append(cand(10, abierta, cert_vence="2026-06-30", siembra=[("certification_expired", f"certificacion:{C(10)}:K3")]))
        L.append(cand(11, abierta, cert_soporte=False, siembra=[("claim_without_support", f"soporte:{C(11)}:K3")]))
    else:
        L.append(cand(10, abierta, empleo=dict(base_emp, desde="2018-01", cert_desde="2018-06-01"), siembra=[("employment_dates_differ", f"fechas:{C(10)}:K2")]))
    return L


def hoja_de_vida(c: dict, e: dict, perfil: dict) -> str:
    l = [f"# Hoja de vida · {c['id']}", "", f"Postulación a la vacante {c['vac']} · recibida el {c['recibido']}", "",
         "Nombre: Persona Sintética " + c["id"][-3:], "Correo: candidato." + c["id"][-3:].lower() + "@ejemplo.invalid", ""]
    if "fecha_de_nacimiento" in c["protegidos"]:
        l += ["Fecha de nacimiento: 14 de marzo de 1991", ""]
    if "sexo" in c["protegidos"]:
        l += ["Sexo: femenino", ""]
    if "fotografia" in c["protegidos"]:
        l += ["[Fotografía adjunta en la hoja de vida]", ""]
    l += ["## Perfil profesional", "", "Experiencia en " + ", ".join(r["text"].lower() for r in perfil["reqs"] if r["id"] in c["evid"]) + "." if c["evid"] else "Experiencia general.", ""]
    l += ["## Estudios", ""]
    if c["titulo"]:
        l.append(f"- {e['titulo_ej']} · Universidad Sintética del Valle · 2018")
    l += ["", "## Experiencia", ""]
    if c["empleo"]:
        l.append(f"- Analista en {c['empleo']['empresa']} · desde {c['empleo']['desde']} hasta {c['empleo']['hasta']}")
    if c.get("segundo"):
        l.append("- Analista en Servicios del Norte Sintéticos · desde 2022-06 hasta 2026-08")
    if c["cert"]:
        l += ["", "## Certificaciones", "", f"- {next(r['text'] for r in perfil['reqs'] if r.get('type') == 'certificacion')} · vence {c['cert_vence']}"]
    return "\n".join(l) + "\n"


def una(e: dict) -> dict:
    raiz = SALIDA / e["carpeta"]
    base = f"{T.norm(e['id']).replace('_', '')}-{slug(e['nombre'])}"
    docs_rel, estado_rel = f"talento/{base}", f"estado-talento/{base}"
    docs = raiz / docs_rel
    e["titulo_ej"] = {"banca-co": "Contador público", "retail-mx": "Licenciatura en administración", "retail-ec": "Licenciatura en administración de empresas", "tecnologia-cl": "Ingeniería en informática",
                      "control-co": "Contador público", "control-pe": "Técnico en computación"}[e["carpeta"]]
    # La referencia: la política de selección y el estándar. Con O*NET, la política dice desde qué
    # importancia una destreza o un conocimiento es exigible: O*NET no marca ninguno como esencial, y el
    # setup lo toma de aquí (CHRO-8).
    exigible = (f"\n\n## El estándar de ocupaciones\n\nCon O*NET, una destreza o un conocimiento es exigible para un cargo "
                f"desde una importancia de {str(e['umbral']).replace('.', ',')} sobre 5.") if e["est"] == "onet" else ""
    documento(docs / "00-referencia" / "politica-de-seleccion.pdf", f"""# Política de selección · {e['nombre']}

## Plazos

- Una vacante se cubre en un máximo de {e['plazo']} días calendario desde su apertura, salvo que el registro de vacantes fije otro plazo.
- Los datos de un candidato que no quedó en el cargo se conservan {e['conserva']} días desde que termina su proceso; después se suprimen.
- Cada perfil de cargo se revisa cada {REVISION_MESES} meses desde su última revisión, salvo que el perfil fije otra fecha.

## Lo que no se pide

Ningún perfil de cargo pide {', '.join(e['prohibidos'])}.

## Autorización

Ninguna hoja de vida se procesa sin la autorización de tratamiento de datos del candidato, registrada antes de recibir sus datos.{exigible}
""")
    if e["est"] == "cuoc":
        escribir_cuoc(docs / CUOC_ARCHIVO, e["ocupaciones"])
        estandar = {"name": "cuoc", "file": CUOC_ARCHIVO}
    else:
        escribir_onet(docs / ONET_CARPETA, e["ocupaciones"])
        estandar = {"name": "onet", "file": ONET_CARPETA, "importance_threshold": e["umbral"]}
    esperado: list[tuple] = []
    # Los perfiles.
    perfiles = []
    for p in e["perfiles"]:
        ruta = f"10-perfiles/{p['id']}_{slug(p['t'])}.docx"
        tasks = [{"id": f"T{i}", "text": t} for i, t in enumerate(p["tasks"], 1)]
        reqs = []
        for r in p["reqs"]:
            x = {k: v for k, v in r.items()}
            x["source"] = ruta
            if x.get("element") and p.get("occ") and (p["occ"] in CUOC or p["occ"] in ONET):
                x.setdefault("type", tipo(e["est"], p["occ"], x["element"]))
                x["element"] = elemento(e["est"], p["occ"], x["element"])
            x.setdefault("type", "experiencia" if x["text"].lower().startswith("experiencia") else "conocimiento" if x.get("element") else "otro")
            reqs.append(x)
        f = {"id": p["id"], "title": p["t"], "source": ruta, "occupation": {"standard": e["est"], "code": p.get("occ") or ""},
             "education": {"label": p["ed"], "source": ruta}, "experience_alternative": bool(p.get("exp")), "tasks": tasks, "requirements": reqs}
        if p.get("na"):
            f["not_applicable"] = p["na"]
        if p.get("last"):
            f["last_review"] = p["last"]
        if p.get("nxt"):
            f["next_review"] = p["nxt"]
        perfiles.append(f)
        md = [f"# Perfil de cargo · {p['id']} · {p['t']}", "", f"**Ocupación ({e['est'].upper()}):** {p.get('occ') or 'sin código'}", "",
              f"**Nivel de estudios:** {p['ed']}" + (" o experiencia equivalente" if p.get("exp") else ""), "", "## Funciones", ""]
        md += [f"- {t['id']}. {t['text']}" for t in tasks] + ["", "## Requisitos", ""]
        for t, titulo in GRUPOS:
            grupo = [r for r in reqs if r["type"] == t]
            if grupo:
                md += [f"### {titulo}", ""] + [f"- {r['id']}. {r['text']}" + (" (indispensable)" if r.get("essential") else "")
                                               + (f" — apoya {', '.join(r['tasks'])}" if r["tasks"] else "") for r in grupo] + [""]
        if p.get("na"):
            md += ["", "## Lo que no aplica", ""] + [f"- {n['element']}: {n['reason']}" for n in p["na"]]
        md += ["", f"**Última revisión:** {p.get('last') or '—'} · **Próxima revisión:** {p.get('nxt') or f'cada {REVISION_MESES} meses'}"]
        documento(docs / ruta, "\n".join(md) + "\n")
        esperado += p["siembra"]
    # Las vacantes.
    tabla(docs / "20-vacantes" / "registro-vacantes.xlsx", [["Vacante", "Perfil", "Apertura", "Cierre", "Estado", "Plazo días", "Responsable"]] +
          [[v, p, dt.date.fromisoformat(a), dt.date.fromisoformat(c) if c else "", "cubierta" if c else "abierta", pl or "", r] for v, p, a, c, pl, r in e["vacantes"]])
    esperado += e["vac_siembra"]
    # Los candidatos.
    perf = {p["id"]: p for p in e["perfiles"]}
    vac = {x[0]: x for x in e["vacantes"]}
    fichas, autoriz, ats, pares = [], [["candidato", "fecha", "finalidad"]], [["Candidate ID", "Requisition ID", "Applied Date", "Stage", "Last Activity"]], []
    cs = candidatos(e)
    for c in cs:
        p = perf[vac[c["vac"]][1]]
        pf = next(x for x in perfiles if x["id"] == p["id"])
        car = f"30-candidatos/{c['vac']}/{c['id']}/"
        cv = car + "hoja-de-vida.pdf"
        documento(docs / cv, hoja_de_vida(c, e, p))
        claims, evid = [], []
        if c["titulo"]:
            sop = None
            if c["titulo_soporte"]:
                sop = car + ("diploma.jpg" if c["foto_soporte"] else "diploma.pdf")
                if c["foto_soporte"]:
                    (docs / sop).write_bytes(diploma_escaneado(e["titulo_ej"]))
                else:
                    documento(docs / sop, f"# Diploma\n\nOtorga el título de {e['titulo_ej']} · Universidad Sintética del Valle · 2018\n")
            claims.append({"id": "K1", "type": "titulo", "text": e["titulo_ej"], "cv_source": cv, "support": sop})
        if c["empleo"]:
            sop = car + "certificado-laboral.pdf"
            documento(docs / sop, f"# Certificado laboral\n\n{c['empleo']['empresa']} certifica que la persona trabajó como analista desde el "
                                  f"{c['empleo']['cert_desde']} hasta el {c['empleo']['cert_hasta']}.\n")
            claims.append({"id": "K2", "type": "empleo", "text": f"Analista en {c['empleo']['empresa']}", "cv_source": cv, "support": sop,
                           "from": c["empleo"]["desde"], "to": c["empleo"]["hasta"], "support_from": c["empleo"]["cert_desde"], "support_to": c["empleo"]["cert_hasta"]})
        if c.get("segundo"):
            sop = car + "certificado-laboral-2.pdf"
            documento(docs / sop, "# Certificado laboral\n\nServicios del Norte Sintéticos certifica que la persona trabajó como analista desde el 2022-06-01 hasta el 2026-08-31.\n")
            claims.append({"id": "K4", "type": "empleo", "text": "Analista en Servicios del Norte Sintéticos", "cv_source": cv, "support": sop,
                           "from": "2022-06", "to": "2026-08", "support_from": "2022-06-01", "support_to": "2026-08-31"})
        if c["cert"]:
            r = next(x for x in pf["requirements"] if x.get("type") == "certificacion")
            sop = None
            if c["cert_soporte"]:
                sop = car + "tarjeta-profesional.pdf"
                documento(docs / sop, f"# Certificación\n\n{r['text']} · vigente hasta el {c['cert_vence']}\n")
            # El vencimiento, del soporte o, si no llegó, de la hoja de vida (cv-record).
            claims.append({"id": "K3", "type": "certificacion", "text": r["text"], "cv_source": cv, "support": sop, "requirement": r["id"],
                           "expires": c["cert_vence"]})
        for rid in c["evid"]:
            evid.append({"requirement": rid, "source": cv + ", p. 1"})
        # Cada afirmación se numera en el orden en que la hoja de vida la hace (cv-record).
        for i, k in enumerate(claims, 1):
            k["id"] = f"K{i}"
        # La certificación es la evidencia de su requisito: en su soporte o, si no llegó, en la hoja de vida.
        cert_k = next((k for k in claims if k["type"] == "certificacion"), None)
        if cert_k:
            evid.append({"requirement": cert_k["requirement"], "source": cert_k["support"] or cv + ", p. 1"})
        # Lo que llegó y no se debe tratar, con dónde está: la fotografía, en la hoja de vida que la
        # anuncia y en su archivo.
        prot = [{"type": t, "source": cv} for t in c["protegidos"]]
        if "fotografia" in c["protegidos"]:
            (docs / car / "foto.jpg").write_bytes(JPG)
            prot.append({"type": "fotografia", "source": car + "foto.jpg"})
        f = {"id": c["id"], "vacancy": c["vac"], "folder": car, "cv": cv, "received": c["recibido"], "claims": claims, "evidence": evid}
        if prot:
            f["protected"] = prot
        fichas.append(f)
        if c["autoriza"] == "same":
            autoriz.append([c["id"], c["recibido"], "Selección de personal"])
        elif c["autoriza"] == "tarde":
            autoriz.append([c["id"], (dt.date.fromisoformat(c["recibido"]) + dt.timedelta(days=12)).isoformat(), "Selección de personal"])
        ats.append([c["id"], c["vac"], c["recibido"], c["estado"], c["fecha_estado"]])
        esperado += c["siembra"]
    # Los pares de la prueba de sesgo: dos candidatos seguidos de la misma vacante, uno con un dato protegido de más.
    ids = [c["id"] for c in cs]
    for a, b in zip(ids, ids[1:]):
        ca, cb = next(c for c in cs if c["id"] == a), next(c for c in cs if c["id"] == b)
        igual = {k: v for k, v in ca.items() if k not in ("id", "protegidos", "siembra")} == {k: v for k, v in cb.items() if k not in ("id", "protegidos", "siembra")}
        if igual and not ca["protegidos"] and cb["protegidos"]:
            pares.append([a, b])
    tabla(docs / "40-autorizaciones" / "registro-autorizaciones.csv", autoriz)
    tabla(docs / "50-ats" / "exportacion-ats.csv", ats)
    codigos = e["ocupaciones"]
    tabla(docs / "50-ats" / "base-interna.csv", [["persona", "ocupacion", "cargo", "area"]] +
          [[f"P-{i + 1:02d}", c, "Cargo interno sintético", "Operaciones"] for i, c in enumerate(codigos)])
    ent = {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]}
    comun = {"entity": ent, "paths": {"documents": docs_rel, "state": estado_rel}, "period": PERIODO, "standard": estandar}
    cfg = {"norma": dict(comun, education={"levels": e["niveles"]}, profiles={"review_months": REVISION_MESES}, overlap={"share": 0.5},
                         selection={"prohibited_requirements": e["prohibidos"]}),
           "candido": dict(comun, selection={"vacancy": {"target_days": e["plazo"]}, "data": {"retention_days": e["conserva"]}, "publish": False})}
    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "estandar": e["est"], "ocupaciones": len(e["ocupaciones"]),
             "hoy": HOY.isoformat(), "periodo": PERIODO,
             "siembra": bool(e["siembra"]), "config": cfg, "extraccion": {"perfiles": {"profiles": perfiles}, "seleccion": {"candidates": fichas}},
             "pares": pares, "esperado": [{"signal": s, "key": k} for s, k in esperado]}
    (raiz / "clave.json").write_text(json.dumps(clave, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return clave


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    total = 0
    for e in ENTIDADES:
        c = una(e)
        total += len(c["esperado"])
        print(f"  {e['carpeta']:<15} {e['pais']}  {e['est']:<5} {len(c['esperado']):>3} señales esperadas · {len(c['pares'])} pares de sesgo")
    print(f"\n  {len(ENTIDADES)} entidades, {total} señales en la clave, en tests/criterio-chro/material/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
