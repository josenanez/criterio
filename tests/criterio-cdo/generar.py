#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CDO: un banco en Colombia, una aseguradora en el Perú, una cadena
de retail en México y dos entidades de control.

    python3 tests/criterio-cdo/generar.py          escribe tests/criterio-cdo/material/

Cada entidad trae su carpeta de datos al 25 de noviembre de 2026: la política de datos, la de
conservación y el glosario de negocio en `00-referencia/`; la exportación del catálogo y el registro de
bases de datos personales en `10-catalogo/`; el informe de junta de octubre con sus cifras en
`20-informes/`; y el linaje, las cifras de la fuente, las reglas de calidad, sus resultados y los datos
críticos en `30-calidad/`. Ninguna trae un dato personal: el catálogo dice qué conjunto los tiene, y nada
más.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal esperada
queda escrita en `clave.json`, junto con lo que la agente tendría que extraer de los documentos escritos
—cada política con su fecha de revisión, cada plazo de conservación, cada término de los informes y cada
cifra con su corte— y la configuración que deja el setup. El motor no la ve; `evaluar.py` compara lo que
el motor levanta contra ella, y una señal de más cuenta igual que una de menos.

**Cuántas veces.** El banco trae cada defecto tres veces y la aseguradora y el retail, dos (`veces`), cada
repetición en su propia fila (`REP`). Así la familia pasa de 73 señales sembradas, la muestra que pide el piso
del 95 % sin fallas (decisión 0020).

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: una política
que se revisa el mes que viene, un conjunto que conserva datos justo dentro de su plazo, un término del
informe escrito con otras mayúsculas que el del glosario, una cifra que difiere de su fuente dentro de la
tolerancia, una cifra de un mes anterior que el informe presenta con su propio corte, una regla que da
exactamente su umbral y una regla sin corrida sobre un dato que no es crítico. Todo es determinista: el
mismo material cada vez, byte a byte. Los nombres, las empresas y los documentos son inventados.
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import formatos as FMT  # noqa: E402  (Word, Excel y PDF sin dependencias y con fecha fija, los mismos de las demás familias)

SALIDA = AQUI / "material"
HOY, PERIODO = dt.date(2026, 11, 25), "2026-11"
TOLERANCIA = 0.5
TODAS = {"dueno", "clasificacion", "politica", "conservacion", "termino", "personales",
         "sin_fuente", "cifra", "corte", "linaje", "umbral", "corrida", "sin_regla"}

ENTIDADES = [
    {"carpeta": "banca-co", "industria": "banca", "pais": "CO", "id": "901555777", "nombre": "Banco Cordillera Sintético", "moneda": "COP",
     "siembra": set(TODAS), "veces": 3},
    {"carpeta": "seguros-pe", "industria": "seguros", "pais": "PE", "id": "20605557771", "nombre": "Aseguradora Pacífico Sintética", "moneda": "PEN",
     "siembra": set(TODAS), "veces": 2},
    {"carpeta": "retail-mx", "industria": "retail", "pais": "MX", "id": "RCM190305AB1", "nombre": "Retail Central Sintético", "moneda": "MXN",
     "siembra": set(TODAS), "veces": 2},
    {"carpeta": "control-co", "industria": "banca", "pais": "CO", "id": "901666888", "nombre": "Banco Control de Datos Sintético", "moneda": "COP",
     "siembra": set(), "veces": 1},
    {"carpeta": "control-mx", "industria": "retail", "pais": "MX", "id": "RCC200101CD2", "nombre": "Retail Control de Datos Sintético", "moneda": "MXN",
     "siembra": set(), "veces": 1},
]

# Las repeticiones de cada defecto: la segunda vez (2) y la tercera (3), cada una en su propia fila.
REP = {
    "dueno": {2: ("DS-12", "Pagos a proveedores", "Transaccional"), 3: ("DS-13", "Campañas de mercadeo", "Transaccional")},
    "clasificacion": {2: ("DS-22", "Contratos con proveedores", "Proveedores"), 3: ("DS-23", "Inventario de activos", "Transaccional")},
    "personales": {2: ("DS-32", "Beneficiarios", "Clientes"), 3: ("DS-33", "Visitantes de las sedes", "Clientes")},
    "conservacion": {2: ("DS-42", "Candidatos a prácticas", "Candidatos", "2022-01-01"), 3: ("DS-43", "Proveedores históricos", "Proveedores", "2019-01-01")},
    "termino": {2: ("Costo de adquisición", 185_000), 3: ("Tasa de retención", 87.5)},
    "sin_fuente": {2: ("Índice de satisfacción", 8.1), 3: ("Participación de mercado", 12.5)},
    "cifra": {2: ("Depósitos", 5_000_000_000, 5_100_000_000), 3: ("Gastos operacionales", 2_000_000_000, 2_060_000_000)},
    "corte": {2: ("Colocaciones", 7_800_000_000, 7_600_000_000), 3: ("Provisiones", 640_000_000, 610_000_000)},
    "linaje": {2: "Ventas netas", 3: "Margen operacional"},
    "umbral": {2: ("RQ-12", "Cliente.correo", 95, 91.0), 3: ("RQ-13", "Movimiento.fecha", 99, 97.5)},
    "corrida": {2: ("RQ-22", "Cuenta.saldo", 99), 3: ("RQ-23", "Crédito.tasa", 98)},
    "sin_regla": {2: "Cliente.ingresos", 3: "Garantía.valor"},
    "politica": {2: ("Política de conservación", "politica_de_conservacion"), 3: ("Política de calidad de datos", "politica_de_calidad_de_datos")},
}


def _pdf(md: str, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    FMT.a_pdf(md, ruta)


def _xlsx(filas: list[list], ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    FMT.a_xlsx_tipado(filas, ruta)


def _norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return "_".join(x for x in __import__("re").split(r"[^a-z0-9]+", s) if x)


def _pesos(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


def construir(e: dict) -> dict:
    """La carpeta de una entidad y su clave."""
    s = e["siembra"]

    def veces(tipo: str) -> list[int]:
        """Las repeticiones de un defecto sembrado, cada una en su propia fila."""
        return list(range(2, e["veces"] + 1)) if tipo in s else []

    raiz = SALIDA / e["carpeta"]
    nombre_carpeta = f"{e['id'].lower()}-{_norm(e['nombre']).replace('_', '-')}"
    docs = raiz / "datos" / nombre_carpeta
    esperado = []

    def esp(signal: str, key: str) -> None:
        esperado.append({"signal": signal, "key": key})

    # ------------------------------------------------------------ 00-referencia
    revision_datos = "2025-06-30" if "politica" in s else "2026-12-15"   # vencida o el mes que viene (control)
    if "politica" in s:
        esp("policy_review_overdue", "politica:politica_de_datos")
    _pdf(f"# Política de datos · {e['nombre']}\n\nAprobada por la junta directiva el 2024-06-30.\n\nPróxima revisión: {revision_datos}.\n\n"
         "Cada conjunto del catálogo tiene un dueño de negocio y una clasificación de confidencialidad: pública, interna, confidencial o restringida.\n\n"
         f"Una cifra de un informe de dirección no puede diferir de su fuente en más del {TOLERANCIA:g} % al mismo corte.\n",
         docs / "00-referencia" / "politica_de_datos.pdf")
    revision_cons = "2026-03-01" if 2 in veces("politica") else "2027-09-01"
    for i in veces("politica"):
        esp("policy_review_overdue", f"politica:{REP['politica'][i][1]}")
    _pdf(f"# Política de conservación · {e['nombre']}\n\nAprobada por la junta directiva el 2025-09-01.\n\nPróxima revisión: {revision_cons}.\n\n"
         "## Plazos de conservación\n\n- Clientes: 120 meses.\n- Transaccional: 120 meses.\n- Candidatos: 24 meses.\n- Proveedores: 60 meses.\n",
         docs / "00-referencia" / "politica_de_conservacion.pdf")
    if 3 in veces("politica"):
        _pdf(f"# Política de calidad de datos · {e['nombre']}\n\nAprobada por la junta directiva el 2023-05-15.\n\nPróxima revisión: 2025-05-15.\n\n"
             "Cada dato crítico tiene al menos una regla de calidad, con su umbral, que corre cada mes.\n",
             docs / "00-referencia" / "politica_de_calidad_de_datos.pdf")
    # Las cifras que se agregan al informe con las repeticiones: las que el glosario sí define.
    glosario_extra = ([[REP["sin_fuente"][i][0], "Indicador de gestión del informe", "Planeación"] for i in veces("sin_fuente")]
                      + [[REP["cifra"][i][0], "Saldo al cierre del mes", "Finanzas"] for i in veces("cifra")]
                      + [[REP["corte"][i][0], "Saldo al cierre del mes", "Finanzas"] for i in veces("corte")])
    _xlsx([["Término", "Definición", "Dueño"],
           ["Cartera vencida", "Saldo de los créditos con más de 30 días de mora", "Riesgo"],
           ["Clientes activos", "Clientes con al menos una transacción en los últimos 90 días", "Comercial"],
           ["Ventas netas", "Ventas menos devoluciones y descuentos", "Finanzas"]] +
          ([] if "termino" in s else [["Margen operacional", "Utilidad operacional sobre ingresos", "Finanzas"]]) + glosario_extra,
          docs / "00-referencia" / "glosario.xlsx")
    politicas = [{"name": "Política de datos", "approved": "2024-06-30", "next_review": revision_datos, "source": "00-referencia/politica_de_datos.pdf"},
                 {"name": "Política de conservación", "approved": "2025-09-01", "next_review": revision_cons, "source": "00-referencia/politica_de_conservacion.pdf"}]
    if 3 in veces("politica"):
        politicas.append({"name": "Política de calidad de datos", "approved": "2023-05-15", "next_review": "2025-05-15",
                          "source": "00-referencia/politica_de_calidad_de_datos.pdf"})
    plazos = [{"type": t, "months": n, "source": "00-referencia/politica_de_conservacion.pdf"}
              for t, n in (("Clientes", 120), ("Transaccional", 120), ("Candidatos", 24), ("Proveedores", 60))]

    # ------------------------------------------------------------ 10-catalogo
    # Candidatos: 24 meses. Sembrado: desde 2023-06-01 (más de 24); control: desde 2025-01-01 (justo dentro).
    cand = "2023-06-01" if "conservacion" in s else "2025-01-01"
    if "conservacion" in s:
        esp("retention_exceeded", "conservacion:DS-04")
    cat = [["Conjunto", "Nombre", "Dueño", "Clasificación", "Tipo", "Datos personales", "Dato más antiguo", "Sistema"],
           ["DS-01", "Clientes", "Gerencia comercial", "Confidencial", "Clientes", "Sí", "2018-03-01", "CRM"],
           ["DS-02", "Movimientos", "" if "dueno" in s else "Gerencia de operaciones", "Restringida", "Transaccional", "No", "2017-01-01", "Core"],
           ["DS-03", "Proveedores", "Compras", "" if "clasificacion" in s else "Interna", "Proveedores", "Sí", "2023-01-01", "ERP"],
           ["DS-04", "Candidatos", "Gestión humana", "Confidencial", "Candidatos", "Sí", cand, "ATS"],
           ["DS-05", "Indicadores de gestión", "Planeación", "Interna", "Transaccional", "No", "2020-01-01", "Bodega"]]
    for i in veces("dueno"):
        cid, nom, tipo = REP["dueno"][i]
        cat.append([cid, nom, "", "Interna", tipo, "No", "2024-01-01", "ERP"])
        esp("dataset_without_owner", f"dueno:{cid}")
    for i in veces("clasificacion"):
        cid, nom, tipo = REP["clasificacion"][i]
        cat.append([cid, nom, "Compras", "", tipo, "No", "2024-01-01", "ERP"])
        esp("dataset_without_classification", f"clasificacion:{cid}")
    for i in veces("personales"):
        cid, nom, tipo = REP["personales"][i]
        cat.append([cid, nom, "Gerencia comercial", "Confidencial", tipo, "Sí", "2022-01-01", "CRM"])
        esp("personal_data_unregistered", f"personales:{cid}")
    for i in veces("conservacion"):
        cid, nom, tipo, antiguo = REP["conservacion"][i]
        cat.append([cid, nom, "Gestión humana" if tipo == "Candidatos" else "Compras", "Interna", tipo, "No", antiguo, "Archivo"])
        esp("retention_exceeded", f"conservacion:{cid}")
    if "dueno" in s:
        esp("dataset_without_owner", "dueno:DS-02")
    if "clasificacion" in s:
        esp("dataset_without_classification", "clasificacion:DS-03")
    _xlsx(cat, docs / "10-catalogo" / "catalogo_datos.xlsx")
    registro = [["Conjunto", "Número de registro", "Fecha de registro"], ["DS-01", "RB-0001", "2019-04-01"], ["DS-04", "RB-0002", "2021-05-10"]]
    if "personales" not in s:
        registro.append(["DS-03", "RB-0003", "2023-02-01"])
    else:
        esp("personal_data_unregistered", "personales:DS-03")
    _xlsx(registro, docs / "10-catalogo" / "registro_de_bases_personales.xlsx")

    # ------------------------------------------------------------ 20-informes
    # Las cifras del informe de junta de octubre, con corte al 31 de octubre.
    corte, anterior = "2026-10-31", "2026-09-30"
    fuente = {"Cartera vencida": {corte: 1_250_000_000, anterior: 1_180_000_000},
              "Clientes activos": {corte: 84_200, anterior: 83_100},
              "Ventas netas": {corte: 9_400_000_000, anterior: 9_150_000_000},
              "Margen operacional": {corte: 3_400_000_000, anterior: 3_150_000_000}}
    cifras = {
        "Cartera vencida": fuente["Cartera vencida"][anterior] if "corte" in s else fuente["Cartera vencida"][corte],
        "Clientes activos": 84_200,
        "Ventas netas": 9_520_000_000 if "cifra" in s else 9_420_000_000,          # 1,3 % (sembrado) o 0,21 % (control: dentro de la tolerancia)
        "Margen operacional": fuente["Margen operacional"][corte],
    }
    if "corte" in s:
        esp("cutoff_mismatch", "corte:informe_junta_2026_10:cartera_vencida")
    if "cifra" in s:
        esp("figure_differs_from_source", "cifra:informe_junta_2026_10:ventas_netas")
    for i in veces("cifra"):
        nom, fte, rep_ = REP["cifra"][i]
        fuente[nom] = {corte: fte, anterior: round(fte * 0.97)}
        cifras[nom] = rep_
        esp("figure_differs_from_source", f"cifra:informe_junta_2026_10:{_norm(nom)}")
    for i in veces("corte"):
        nom, fte, ant = REP["corte"][i]
        fuente[nom] = {corte: fte, anterior: ant}
        cifras[nom] = ant
        esp("cutoff_mismatch", f"corte:informe_junta_2026_10:{_norm(nom)}")
    for i in veces("termino"):                         # en la fuente y bien, pero el glosario no la define
        nom, v = REP["termino"][i]
        fuente[nom] = {corte: v, anterior: v}
        cifras[nom] = v
        esp("term_not_in_glossary", f"termino:{_norm(nom)}")
    lineas = [(k, v) for k, v in cifras.items()]
    for i in veces("sin_fuente"):                      # el glosario la define, y nada la sostiene
        nom, v = REP["sin_fuente"][i]
        lineas.append((nom, v))
        esp("figure_without_source", f"fuente:informe_junta_2026_10:{_norm(nom)}")
    if "sin_fuente" in s:
        lineas.append(("Índice de rotación", 4.2))
        esp("figure_without_source", "fuente:informe_junta_2026_10:indice_de_rotacion")
    inf = "20-informes/informe_junta_2026-10.pdf"
    _pdf(f"# Informe de gestión a la junta directiva · octubre de 2026\n\n{e['nombre']}. Cifras con corte al 31 de octubre de 2026.\n\n"
         "| Indicador | Valor |\n|---|---|\n" + "\n".join(f"| {k} | {_pesos(v) if v >= 1000 else str(v).replace('.', ',')} |" for k, v in lineas) + "\n",
         docs / inf)
    terminos = [{"term": k, "source": inf} for k, _ in lineas]
    if "termino" in s:
        esp("term_not_in_glossary", "termino:margen_operacional")
    if "sin_fuente" in s:
        # «Índice de rotación» tampoco está en el glosario: el mismo informe siembra las dos.
        esp("term_not_in_glossary", "termino:indice_de_rotacion")
    figures = [{"indicator": k, "value": v, "cutoff": corte, "source": inf} for k, v in lineas]

    # ------------------------------------------------------------ 30-calidad
    lin = [["Indicador", "Paso", "Sistema de origen", "Conjunto"],
           ["Cartera vencida", "1", "Core", "DS-02"], ["Cartera vencida", "2", "Bodega", "DS-05"],
           ["Clientes activos", "1", "CRM", "DS-01"], ["Clientes activos", "2", "" if "linaje" in s else "Bodega", "DS-05"],
           ["Ventas netas", "1", "ERP", "DS-05"], ["Margen operacional", "1", "ERP", "DS-05"]]
    if "linaje" in s:
        esp("lineage_broken", "linaje:clientes_activos:2")
    for i in veces("linaje"):                          # el segundo paso, sin su sistema de origen
        lin.append([REP["linaje"][i], "2", "", "DS-05"])
        esp("lineage_broken", f"linaje:{_norm(REP['linaje'][i])}:2")
    _xlsx(lin, docs / "30-calidad" / "linaje.xlsx")
    _xlsx([["Indicador", "Corte", "Valor"]] + [[k, c, v] for k, vs in fuente.items() for c, v in sorted(vs.items(), reverse=True)],
          docs / "30-calidad" / "cifras_fuente.xlsx")
    reglas = [["Regla", "Dato", "Umbral"], ["RQ-01", "Cliente.documento", 99], ["RQ-02", "Movimiento.valor", 98], ["RQ-03", "Crédito.fecha_desembolso", 97],
              ["RQ-04", "Proveedor.correo", 90]]
    reglas += [[REP["umbral"][i][0], REP["umbral"][i][1], REP["umbral"][i][2]] for i in veces("umbral")]
    reglas += [[REP["corrida"][i][0], REP["corrida"][i][1], REP["corrida"][i][2]] for i in veces("corrida")]
    _xlsx(reglas, docs / "30-calidad" / "reglas_calidad.xlsx")
    resultados = [["Regla", "Periodo", "Resultado"], ["RQ-01", PERIODO, 99.6], ["RQ-02", PERIODO, 96.1 if "umbral" in s else 98.0]]
    if "umbral" in s:
        esp("quality_rule_below_threshold", "umbral:RQ-02")
    if "corrida" not in s:
        resultados.append(["RQ-03", PERIODO, 97.4])
    else:
        esp("quality_rule_not_run", "corrida:RQ-03")
    for i in veces("umbral"):
        resultados.append([REP["umbral"][i][0], PERIODO, REP["umbral"][i][3]])
        esp("quality_rule_below_threshold", f"umbral:{REP['umbral'][i][0]}")
    for i in veces("corrida"):
        esp("quality_rule_not_run", f"corrida:{REP['corrida'][i][0]}")
    # RQ-04 no corrió, y Proveedor.correo no es crítico: no es una señal.
    _xlsx(resultados, docs / "30-calidad" / "resultados_calidad.xlsx")
    criticos = [["Dato", "Dueño"], ["Cliente.documento", "Comercial"], ["Movimiento.valor", "Operaciones"], ["Crédito.fecha_desembolso", "Crédito"]]
    criticos += [[REP["corrida"][i][1], "Finanzas"] for i in veces("corrida")]
    for i in veces("sin_regla"):
        criticos.append([REP["sin_regla"][i], "Riesgo"])
        esp("critical_data_without_rule", f"critico:{_norm(REP['sin_regla'][i])}")
    if "sin_regla" in s:
        criticos.append(["Crédito.calificación", "Riesgo"])
        esp("critical_data_without_rule", "critico:credito_calificacion")
    _xlsx(criticos, docs / "30-calidad" / "datos_criticos.xlsx")

    def cfg(rol: str) -> dict:
        return {"version": "0.1", "role": rol, "entity": {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]},
                "paths": {"documents": f"datos/{nombre_carpeta}", "state": f"estado-datos/{nombre_carpeta}"}, "period": PERIODO, "publish_rostrum": True,
                "methodology": {"tolerance_pct": TOLERANCIA}, "columns": {}, "report": {"language": "es"}, "execution": {"workers": 1}}

    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "hoy": HOY.isoformat(), "periodo": PERIODO, "siembra": bool(s),
             "config": {"custodia": cfg("gobierno"), "ariadna": cfg("calidad")},
             "extraccion": {"gobierno": {"policies": politicas, "retention": plazos, "report_terms": terminos, "reviewed": [], "questions": []},
                            "calidad": {"figures": figures, "reviewed": [], "questions": []}},
             "esperado": sorted(esperado, key=lambda x: (x["signal"], x["key"]))}
    (raiz / "clave.json").write_text(json.dumps(clave, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return clave


def main() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    for e in ENTIDADES:
        c = construir(e)
        print(f"  {e['carpeta']:<15} {e['pais']}  {len(c['esperado']):>3} señales sembradas" + (" · control" if not c["siembra"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
