#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El material de prueba de la familia CAE: un banco en Colombia, una cooperativa en el Perú, una
aseguradora en Brasil y dos entidades de control.

    python3 tests/criterio-cae/generar.py          escribe tests/criterio-cae/material/

Cada entidad trae su carpeta de auditoría interna al 24 de noviembre de 2026: el estatuto, la
metodología, el equipo y sus cargos anteriores en `00-referencia/`; el universo auditable, la matriz de
riesgos, el plan anual y las actas del comité en `10-plan/`; dos trabajos con su programa, su índice de
papeles, sus papeles y su informe, y las asignaciones, en `20-trabajos/`; y el registro de hallazgos, el
de riesgos aceptados, las evidencias, las explicaciones de atraso y el informe del revisor fiscal o del
supervisor en `30-seguimiento/`.

**La clave la escribe este archivo, no el motor.** Cada defecto se siembra a propósito y su señal
esperada queda escrita en `clave.json`, junto con lo que el agente tendría que extraer de los documentos
escritos —las actas, cada hallazgo de los papeles y del informe, las evidencias, las explicaciones y los
hallazgos externos— y la configuración que deja el setup. El motor no la ve; `evaluar.py` compara lo que
el motor levanta contra ella, y una señal de más cuenta igual que una de menos.

**Las entidades de control no tienen ningún defecto**, y sí los casos que se parecen a uno: un riesgo alto
cubierto por la unidad y no por su código, un ciclo que vence el mes que viene, una evaluación de riesgos
de hace 358 días, una evaluación externa que vence en diciembre, un trabajo de ciberseguridad que empezó
antes de que rigiera su requisito temático, horas del plan iguales a la capacidad, una causa que no se
pudo identificar con su razón, un paso que no aplica con su razón, un papel revisado el mismo día del
informe, un auditor que dejó la unidad hace trece meses, un plan vencido con su explicación, dos
reprogramaciones cuando se permiten dos, una condición parecida en otro proceso, un riesgo aceptado que se
discutió y se resolvió y un hallazgo externo que está en el registro por su referencia. Todo es
determinista: el mismo material cada vez, byte a byte. Los nombres, las empresas, las personas y los
documentos son inventados.
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
HOY, PERIODO = dt.date(2026, 11, 24), "2026-11"

ENTIDADES = [
    {"carpeta": "banca-co", "industria": "banca", "pais": "CO", "id": "901777321", "nombre": "Banco Andino Sintético", "moneda": "COP",
     "siembra": {"riesgo", "unidad", "evaluacion", "area:fraude", "cambio", "atraso", "horas", "tematico", "externa",
                 "programa", "elementos", "papel", "paso", "revision", "informe", "prioridad", "objetividad",
                 "sin_plan", "vencido", "reprogramado", "cierre", "repetido", "aceptado", "externo"}},
    {"carpeta": "cooperativa-pe", "industria": "cooperativas", "pais": "PE", "id": "20601777321", "nombre": "Cooperativa de Ahorro Altiplano Sintética", "moneda": "PEN",
     "siembra": {"riesgo", "unidad", "cambio", "atraso", "tematico", "elementos", "paso", "revision", "informe", "sin_plan", "vencido", "repetido", "externo"}},
    {"carpeta": "seguros-br", "industria": "seguros", "pais": "BR", "id": "31452078000190", "nombre": "Seguradora Atlântica Sintética", "moneda": "BRL",
     "siembra": {"unidad", "evaluacion", "area:cumplimiento", "horas", "externa", "programa", "papel", "prioridad", "objetividad",
                 "reprogramado", "cierre", "aceptado"}},
    {"carpeta": "control-co", "industria": "banca", "pais": "CO", "id": "901888432", "nombre": "Banco Control Sintético", "moneda": "COP", "siembra": set()},
    {"carpeta": "control-pe", "industria": "cooperativas", "pais": "PE", "id": "20602888432", "nombre": "Cooperativa Control Sintética", "moneda": "PEN", "siembra": set()},
]

METODOLOGIA = """# Metodología de auditoría interna · {nombre}

**Aprobada por el comité de auditoría.** Versión vigente desde el 15 de enero de 2026.

## Ciclos de rotación

Cada unidad del universo auditable se audita según su nivel de riesgo: crítico y alto, cada 12 meses;
medio, cada 24 meses; bajo, cada 36 meses. Un riesgo calificado alto o crítico en la matriz de riesgos
tiene que estar cubierto por un trabajo del plan anual.

## Escala de prioridad de los hallazgos

La prioridad sale del impacto por la probabilidad, cada uno de 1 a 5: alta desde 15, media desde 8 y
baja desde 1.

## Seguimiento

La fecha de un plan de acción se puede correr hasta dos veces. Un cierre lo valida auditoría con la
evidencia de su implementación.

## Evaluaciones

La última evaluación de riesgos que sostiene el plan es del {evaluacion}. La última evaluación externa
de calidad terminó el {externa}.
"""


def _pdf(md: str, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    FMT.a_pdf(md, ruta)


def _xlsx(filas: list[list], ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    FMT.a_xlsx_tipado(filas, ruta)


def _pesos(x: int) -> str:
    return "$" + f"{x:,}".replace(",", ".")


def _hoja(h: dict) -> str:
    """La hoja de un hallazgo en su papel de trabajo."""
    filas = [f"Criterio: {h['criteria']}", f"Condición: {h['condition']}"]
    if h["cause"]:
        filas.append(f"Causa: {h['cause']}")
    if h["cause_unknown_reason"]:
        filas.append(f"Por qué no se identificó la causa: {h['cause_unknown_reason']}")
    filas += [f"Efecto: {h['effect']}", f"Impacto (de 1 a 5, según la metodología): {h['impact']}",
              f"Probabilidad (de 1 a 5, según la metodología): {h['likelihood']}", f"Prioridad que asigna el auditor: {h['priority']}",
              f"Papeles que lo soportan: {', '.join(h['workpapers'])}"]
    filas += [f"Monto: {_pesos(x)}" for x in h["figures"]]
    return f"\n## Hallazgo {h['id']}\n\n" + "\n".join(f"- {f}" for f in filas) + "\n"


def construir(e: dict) -> dict:
    """La carpeta de una entidad y su clave."""
    s = e["siembra"]
    control = not s
    raiz = SALIDA / e["carpeta"]
    nombre_carpeta = f"{e['id']}-{e['nombre'].lower().replace(' ', '-').replace('á', 'a').replace('â', 'a').replace('í', 'i').replace('é', 'e').replace('ó', 'o').replace('ú', 'u')}"
    docs = raiz / "auditoria" / nombre_carpeta
    esperado = []

    def esp(signal: str, key: str) -> None:
        esperado.append({"signal": signal, "key": key})

    # ------------------------------------------------------------ 00-referencia
    evaluacion = "2025-09-15" if "evaluacion" in s else "2025-12-01"   # 435 días o 358 (control)
    externa = "2021-03-31" if "externa" in s else "2021-12-15"         # venció en marzo o vence en diciembre (control)
    if "evaluacion" in s:
        esp("risk_assessment_outdated", "evaluacion_de_riesgos")
    if "externa" in s:
        esp("external_assessment_overdue", "evaluacion_externa")
    _pdf(METODOLOGIA.format(nombre=e["nombre"], evaluacion=evaluacion, externa=externa), docs / "00-referencia" / "metodologia-de-auditoria.pdf")
    _pdf(f"# Estatuto de auditoría interna · {e['nombre']}\n\nLa auditoría interna reporta funcionalmente al comité de auditoría, que aprueba el plan anual y sus cambios.\n",
              docs / "00-referencia" / "estatuto-de-auditoria.pdf")
    horas_equipo = 2000
    _xlsx([["Auditor", "Horas disponibles"], ["Ana Ríos", 1000], ["Luis Peña", 1000]], docs / "00-referencia" / "equipo.xlsx")
    # Luis tuvo a su cargo Tecnología: hasta después de empezar el trabajo (siembra) o hasta más de trece meses antes (control).
    hasta = "2026-06-30" if "objetividad" in s else "2024-11-30"
    _xlsx([["Auditor", "Unidad", "Desde", "Hasta"], ["Luis Peña", "Tecnología", "2021-01-01", hasta]], docs / "00-referencia" / "cargos_anteriores.xlsx")

    # ------------------------------------------------------------ 10-plan
    universo = [["Unidad", "Nombre", "Nivel", "Último trabajo"],
                ["U-01", "Crédito", "Alto", "2025-10-15"],
                ["U-02", "Tecnología", "Alto", "2025-10-01"],
                ["U-03", "Tesorería", "Medio", "2023-03-10" if "unidad" in s else "2024-12-20"],
                ["U-04", "Nómina", "Bajo", "2024-05-01"],
                ["U-05", "Cumplimiento", "Alto", "2025-12-01"],
                ["U-06", "Proveedores", "Medio", "2025-01-15"],
                ["U-10", "Canales físicos", "Bajo", "" if "unidad" in s and e["carpeta"] != "seguros-br" else "2024-05-01"]]
    if "unidad" in s:
        esp("auditable_unit_overdue", "unidad:U-03")
        if e["carpeta"] != "seguros-br":
            esp("auditable_unit_overdue", "unidad:U-10")
    _xlsx(universo, docs / "10-plan" / "universo_auditable.xlsx")
    matriz = [["Riesgo", "Descripción", "Calificación", "Unidad"],
              ["R-01", "Pérdida por riesgo de crédito", "Alto", "U-01"],
              ["R-02", "Ataque a los canales digitales", "Crítico", "U-02"],
              ["R-03", "Fraude en pagos a proveedores", "Alto", "U-06" if not control else "U-07"],
              ["R-04", "Lavado de activos", "Crítico", "U-05"],
              ["R-05", "Error en la liquidación de nómina", "Medio", "U-04"]]
    if "riesgo" in s:
        matriz.append(["R-06", "Pérdida de información de clientes", "Crítico", "U-09"])
        esp("high_risk_not_covered", "riesgo:R-06")
    _xlsx(matriz, docs / "10-plan" / "matriz_de_riesgos.xlsx")

    plan = [["Trabajo", "Nombre", "Unidad", "Riesgos", "Tipo", "Tema", "Inicio", "Cierre", "Estado", "Horas", "Requisito temático", "Cambio"],
            ["TR-01", "Crédito comercial", "U-01", "R-01", "Aseguramiento", "Crédito", "2026-02-02", "2026-04-30", "Terminado", 500, "", ""],
            ["TR-02", "Ciberseguridad de canales", "U-02", "R-02", "Aseguramiento", "Ciberseguridad; TI",
             "2026-03-02" if "tematico" in s else "2026-01-20", "2026-05-29", "Terminado", 400, "", ""]]
    if "tematico" in s:
        esp("topical_requirement_missing", "tematico:TR-02:ciberseguridad")
    cumplimiento = "Cumplimiento; SARLAFT" if "area:cumplimiento" not in s else "Lavado de activos"
    plan.append(["TR-03", "Prevención de lavado", "U-05", "R-04", "Aseguramiento", cumplimiento, "2026-06-01", "2026-12-18", "En curso", 300, "", ""])
    fraude = "Proveedores; fraude" if "area:fraude" not in s else "Proveedores"
    plan.append(["TR-04", "Pagos a proveedores", "U-06" if not control else "U-07", "" if control else "R-03", "Aseguramiento", f"{fraude}; terceros",
                 "2026-09-21", "2026-12-11", "En curso", 300, "Terceros", ""])
    if "area:fraude" in s:
        esp("plan_area_not_considered", "area:fraude")
    if "area:cumplimiento" in s:
        esp("plan_area_not_considered", "area:cumplimiento")
    plan.append(["TR-05", "Tesorería", "U-03", "", "Aseguramiento", "Tesorería", "2026-08-03", "2026-09-30", "Cancelado", 200, "", "Cancelado"])
    # El atraso: un trabajo planeado que tenía que empezar el 2 de noviembre (siembra) o que empieza en diciembre (control).
    plan.append(["TR-06", "Nómina", "U-04", "R-05", "Aseguramiento", "Nómina", "2026-11-02" if "atraso" in s else "2026-12-01", "2027-01-29", "Planeado",
                 200, "", "Agregado"])
    if "atraso" in s:
        esp("engagement_behind_schedule", "atraso:TR-06")
    if "cambio" in s:
        esp("plan_change_unapproved", "cambio:TR-06")
    # Las horas: el plan activo suma 1.700 más TR-07; con la siembra supera las 2.000 del equipo, en el control las iguala.
    plan.append(["TR-07", "Gobierno corporativo", "U-08", "", "Consultoría", "Gobierno", "2026-10-05", "2026-12-18", "En curso", 500 if "horas" in s else 300, "", ""])
    if "horas" in s:
        esp("plan_hours_exceed_capacity", "horas")
    _xlsx(plan, docs / "10-plan" / "plan_anual_2026.xlsx")
    _pdf(f"# Acta 07-2026 del comité de auditoría · {e['nombre']}\n\n15 de julio de 2026. El comité aprueba cancelar el trabajo TR-05, Tesorería, "
              f"porque el área cambia de sistema en el segundo semestre.\n", docs / "10-plan" / "actas" / "acta-07-2026.pdf")
    aprobaciones = [{"engagement": "TR-05", "change": "cancela", "approved_by": "Comité de auditoría", "date": "2026-07-15",
                     "source": "10-plan/actas/acta-07-2026.pdf"}]
    if "cambio" not in s:
        _pdf(f"# Acta 10-2026 del comité de auditoría · {e['nombre']}\n\n20 de octubre de 2026. El comité aprueba agregar el trabajo TR-06, Nómina, "
                  f"al plan anual.\n", docs / "10-plan" / "actas" / "acta-10-2026.pdf")
        aprobaciones.append({"engagement": "TR-06", "change": "agrega", "approved_by": "Comité de auditoría", "date": "2026-10-20",
                             "source": "10-plan/actas/acta-10-2026.pdf"})

    # ------------------------------------------------------------ 20-trabajos
    engagements = []
    revisados = []
    asignaciones = [["Trabajo", "Auditor", "Unidad", "Inicio"], ["TR-01", "Ana Ríos", "Crédito", "2026-02-02"],
                    ["TR-02", "Luis Peña", "Tecnología", "2026-03-02" if "tematico" in s else "2026-01-20"]]
    if "objetividad" in s:
        esp("auditor_reviews_own_work", "objetividad:TR-02:luis_pena")
    _xlsx(asignaciones, docs / "20-trabajos" / "asignaciones.xlsx")
    for tid, carpeta, unidad in (("TR-01", "TR-01_credito-comercial", "Crédito"), ("TR-02", "TR-02_ciberseguridad", "Tecnología")):
        base = docs / "20-trabajos" / carpeta
        uno = tid == "TR-01"
        pasos = [["Paso", "Objetivo", "Papel", "No aplica"], ["P1", "Entender el proceso y sus controles", "PT-01", ""],
                 ["P2", "Probar los controles clave", "PT-02", ""], ["P3", "Probar una muestra de operaciones", "PT-03", ""]]
        if uno and "paso" in s:
            pasos.append(["P4", "Revisar las provisiones", "", ""])
            esp("procedure_not_executed", f"paso:{tid}:P4")
        else:
            pasos.append(["P4", "Revisar los castigos", "", "No hubo castigos en el periodo"])
        _xlsx(pasos, base / "programa_de_trabajo.xlsx")
        informe = "2026-04-30" if uno else "2026-05-29"
        rev_pt3 = ["", ""] if (uno and "revision" in s) else ["Ana Ríos", informe]
        if uno and "revision" in s:
            esp("workpaper_not_reviewed", f"revision:{tid}:PT-03")
        primero = "2026-02-09" if uno else "2026-03-09"
        _xlsx([["Papel", "Paso", "Fecha", "Revisado por", "Fecha revisión", "Aprobado por", "Fecha aprobación"],
                           ["PT-01", "P1", primero, "Ana Ríos", "2026-03-02" if uno else "2026-03-16", "Jefa de auditoría", "2026-03-04" if uno else "2026-03-18"],
                           ["PT-02", "P2", "2026-03-10" if uno else "2026-04-06", "Ana Ríos", "2026-03-20" if uno else "2026-04-20", "Jefa de auditoría", "2026-03-23" if uno else "2026-04-22"],
                           ["PT-03", "P3", "2026-03-24" if uno else "2026-05-04", rev_pt3[0], rev_pt3[1], "Jefa de auditoría", informe]],
                          base / "indice_de_papeles.xlsx")
        aprobado = ("2026-03-16" if "programa" in s and not uno else (dt.date.fromisoformat(primero) - dt.timedelta(days=3)).isoformat())
        if "programa" in s and not uno:
            esp("work_program_not_approved", f"programa:{tid}")
        _pdf(f"# Aprobación del programa de trabajo {tid}\n\nLa jefa de auditoría aprueba el programa el {aprobado}.\n", base / "aprobacion-del-programa.pdf")
        hall = []
        rep = []
        if uno:
            h1 = {"id": "H-01", "criteria": "Política de crédito, numeral 4.2", "condition": "12 de 60 créditos desembolsados sin garantía constituida",
                  "cause": "" if "elementos" in s else "El desembolso no espera la constancia de la garantía",
                  "cause_unknown_reason": None, "effect": "Pérdida esperada sin cobertura", "impact": 4, "likelihood": 4,
                  "priority": "Media" if "prioridad" in s else "Alta", "workpapers": ["PT-03"], "figures": [1_200_000_000],
                  "source": f"20-trabajos/{carpeta}/PT-03.pdf"}
            if "elementos" in s:
                esp("finding_element_missing", f"elementos:{tid}:H-01")
            if "prioridad" in s:
                esp("rating_inconsistent", f"prioridad:{tid}:H-01")
            h2 = {"id": "H-02", "criteria": "Manual de garantías, numeral 2", "condition": "Avalúos con más de tres años sin actualizar",
                  "cause": "" if control else "El sistema no avisa el vencimiento del avalúo",
                  "cause_unknown_reason": "La gerencia no entregó el registro de avalúos a tiempo" if control else None,
                  "effect": "Garantías con valor desactualizado", "impact": 3, "likelihood": 3, "priority": "Media",
                  "workpapers": ["PT-09"] if "papel" in s else ["PT-02"], "figures": [450_000_000], "source": f"20-trabajos/{carpeta}/PT-02.pdf"}
            if "papel" in s:
                esp("finding_without_workpaper", f"papel:{tid}:H-02")
            hall = [h1, h2]
            rep = [{"id": "H-01", "priority": h1["priority"],
                    "figures": [1_200_000_000], "source": f"20-trabajos/{carpeta}/informe.pdf"},
                   {"id": "H-02", "priority": "Media", "figures": [450_000_000] if "informe" not in s else [540_000_000],
                    "source": f"20-trabajos/{carpeta}/informe.pdf"}]
            if "informe" in s:
                esp("report_differs_from_workpapers", f"informe:{tid}:H-02")
        else:
            hall = [{"id": "H-03", "criteria": "Política de seguridad de la información, numeral 7", "condition": "Cuentas privilegiadas sin revisión trimestral",
                     "cause": "La revisión depende de una persona", "cause_unknown_reason": None, "effect": "Accesos indebidos sin detectar",
                     "impact": 4, "likelihood": 2, "priority": "Media", "workpapers": ["PT-02"], "figures": [], "source": f"20-trabajos/{carpeta}/PT-02.pdf"}]
            rep = [{"id": "H-03", "priority": "Media", "figures": [], "source": f"20-trabajos/{carpeta}/informe.pdf"}]
        # Cada hallazgo, escrito en el papel que lo cita como su fuente: lo que el agente procesa. Un
        # elemento que falta —la causa— no se escribe; la razón por la que no se identificó, sí.
        for pt in ("PT-01", "PT-02", "PT-03"):
            hojas = "".join(_hoja(h) for h in hall if h["source"] == f"20-trabajos/{carpeta}/{pt}.pdf")
            _pdf(f"# Papel de trabajo {pt} · {tid} · {unidad}\n\nPreparado por el equipo de auditoría interna.\n" + hojas, base / f"{pt}.pdf")
        _pdf(f"# Informe de auditoría {tid} · {unidad}\n\nFecha del informe: {informe}.\n\n" +
                  "\n".join(f"- {h['id']}: prioridad {h['priority']}." + "".join(f" Monto: {_pesos(x)}." for x in h["figures"]) for h in rep) + "\n",
             base / "informe.pdf")
        citados = {h["source"] for h in hall}
        revisados += [f"20-trabajos/{carpeta}/{pt}.pdf" for pt in ("PT-01", "PT-02", "PT-03") if f"20-trabajos/{carpeta}/{pt}.pdf" not in citados]
        engagements.append({"id": tid, "program_approved": aprobado, "program_source": f"20-trabajos/{carpeta}/aprobacion-del-programa.pdf",
                            "report_date": informe, "report_source": f"20-trabajos/{carpeta}/informe.pdf", "findings": hall, "report_findings": rep})

    # ------------------------------------------------------------ 30-seguimiento
    seg = docs / "30-seguimiento"
    reg = [["Hallazgo", "Trabajo", "Origen", "Proceso", "Condición", "Prioridad", "Comunicado", "Plan", "Responsable", "Fecha compromiso",
            "Reprogramaciones", "Estado", "Fecha cierre", "Validado por", "Referencia externa"],
           ["H-20", "TR-90", "Interna", "Crédito", "Créditos desembolsados sin garantía constituida", "Alta", "2025-04-30", "Exigir la constancia", "Gerencia de crédito",
            "2025-09-30", 0, "Cerrado", "2025-09-15", "Ana Ríos", ""]]
    evidencias = [{"finding": "H-20", "date": "2025-09-12", "what": "Procedimiento de desembolso actualizado", "source": "30-seguimiento/H-20/evidencia.pdf"}]
    _pdf("# Evidencia H-20 · Procedimiento de desembolso actualizado\n\nFecha: 2025-09-12.\n\nProcedimiento de desembolso con la constancia de la garantía como requisito.\n",
         seg / "H-20" / "evidencia.pdf")
    # H-01 vuelve: la misma condición en el mismo proceso que H-20, cerrado en 2025.
    reg.append(["H-01", "TR-01", "Interna", "Crédito" if "repetido" in s else "Garantías", "Créditos desembolsados sin garantía constituida", "Alta", "2026-04-30",
                "Bloquear el desembolso sin constancia", "Gerencia de crédito", "2026-12-31", 0, "Abierto", "", "", ""])
    if "repetido" in s:
        esp("finding_repeated", "repetido:H-01:H-20")
    reg.append(["H-02", "TR-01", "Interna", "Garantías", "Avalúos con más de tres años sin actualizar", "Media", "2026-04-30", "Actualizar los avalúos",
                "" if "sin_plan" in s else "Gerencia de garantías", "2026-12-15", 0, "Abierto", "", "", ""])
    if "sin_plan" in s:
        esp("action_plan_missing", "plan:H-02")
    # H-03 venció el 30 de septiembre: sin evidencia ni explicación (siembra) o con su explicación (control).
    reg.append(["H-03", "TR-02", "Interna", "Tecnología", "Cuentas privilegiadas sin revisión trimestral", "Media", "2026-05-29", "Revisión trimestral automatizada",
                "Gerencia de tecnología", "2026-09-30", 2 if "reprogramado" not in s else 3, "Abierto", "", "", ""])
    if "vencido" in s:
        esp("action_plan_overdue", "vencido:H-03")
    else:
        _pdf("# Explicación del atraso H-03 · El proveedor entrega en diciembre\n\nFecha: 2026-10-01.\n\nEl proveedor entrega la automatización el 15 de diciembre de 2026.\n",
             seg / "H-03" / "explicacion-del-atraso.pdf")
    if "reprogramado" in s:
        esp("due_date_extended_repeatedly", "reprogramado:H-03")
    # H-21: cerrado con validación; sin evidencia (siembra) o con ella (control).
    reg.append(["H-21", "TR-91", "Interna", "Tesorería", "Conciliaciones bancarias sin firma del revisor", "Baja", "2025-06-30", "Firma electrónica", "Tesorería",
                "2025-10-31", 0, "Cerrado", "2025-10-20", "Ana Ríos", ""])
    if "cierre" in s:
        esp("closure_without_evidence", "cierre:H-21")
    else:
        _pdf("# Evidencia H-21 · Conciliaciones firmadas\n\nFecha: 2025-10-18.\n\nConciliaciones de octubre firmadas por el revisor.\n", seg / "H-21" / "evidencia.pdf")
        evidencias.append({"finding": "H-21", "date": "2025-10-18", "what": "Conciliaciones firmadas", "source": "30-seguimiento/H-21/evidencia.pdf"})
    reg.append(["RF-01", "", "Revisor fiscal", "Nómina", "Horas extra pagadas sin aprobación", "Media", "2026-06-15", "Aprobación en el sistema", "Gestión humana",
                "2026-12-31", 0, "Abierto", "", "", "RF-01"])
    _xlsx(reg, seg / "registro_hallazgos.xlsx")
    acep = [["Riesgo", "Descripción", "Fecha", "Por encima del apetito", "Discutido alta dirección", "Resuelto", "Escalado consejo"],
            ["RA-01", "Sistema central sin soporte del fabricante", "2026-06-01", "Sí", "" if "aceptado" in s else "2026-06-10",
             "" if "aceptado" in s else "Sí", ""],
            ["RA-02", "Demora en un reporte interno", "2026-06-01", "No", "", "", ""]]
    if "aceptado" in s:
        esp("risk_accepted_not_escalated", "aceptado:RA-01")
    _xlsx(acep, seg / "riesgos_aceptados.xlsx")
    externos = [{"id": "RF-01", "issuer": "Revisor fiscal", "title": "Horas extra pagadas sin aprobación", "source": "30-seguimiento/informe_revisor_fiscal_2026.pdf"}]
    texto_externo = "- RF-01: horas extra pagadas sin aprobación.\n"
    if "externo" in s:
        externos.append({"id": "RF-02", "issuer": "Revisor fiscal", "title": "Caja menor sin arqueo", "source": "30-seguimiento/informe_revisor_fiscal_2026.pdf"})
        texto_externo += "- RF-02: caja menor sin arqueo en el trimestre.\n"
        esp("external_finding_untracked", "externo:RF-02")
    _pdf(f"# Informe del revisor fiscal 2026 · {e['nombre']}\n\n{texto_externo}", seg / "informe_revisor_fiscal_2026.pdf")
    explicaciones = [] if "vencido" in s else [{"finding": "H-03", "date": "2026-10-01", "what": "El proveedor entrega en diciembre",
                                                 "source": "30-seguimiento/H-03/explicacion-del-atraso.pdf"}]

    def cfg(rol: str) -> dict:
        return {"version": "0.1", "role": rol, "entity": {"id": e["id"], "name": e["nombre"], "country": e["pais"], "currency": e["moneda"]},
                "paths": {"documents": f"auditoria/{nombre_carpeta}", "state": f"estado-auditoria/{nombre_carpeta}"}, "period": PERIODO, "publish_rostrum": False,
                "methodology": {"cycles_months": {"Crítico": 12, "Alto": 12, "Medio": 24, "Bajo": 36}, "high_ratings": ["Alto", "Crítico"],
                                "risk_assessment_date": evaluacion, "risk_assessment_source": "00-referencia/metodologia-de-auditoria.pdf",
                                "external_assessment_date": externa, "external_assessment_source": "00-referencia/metodologia-de-auditoria.pdf",
                                "plan_approver": "Comité de auditoría", "priority": {"levels": [["Alta", 15], ["Media", 8], ["Baja", 1]]},
                                "max_reschedules": 2},
                "columns": {}, "report": {"language": "es"}, "execution": {"workers": 1}}

    clave = {"entidad": e["nombre"], "industria": e["industria"], "pais": e["pais"], "hoy": HOY.isoformat(), "periodo": PERIODO, "siembra": bool(s),
             "config": {"prudencia": cfg("plan"), "justo": cfg("trabajos"), "remedios": cfg("seguimiento")},
             "extraccion": {"plan": {"approvals": aprobaciones, "reviewed": [], "questions": []},
                            "trabajos": {"engagements": engagements, "reviewed": revisados, "questions": []},
                            "seguimiento": {"evidence": evidencias, "delay_explanations": explicaciones, "external_findings": externos,
                                            "reviewed": [], "questions": []}},
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
