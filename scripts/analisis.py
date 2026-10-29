#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El análisis estadístico de las pruebas de la familia PMO, calculado de la evidencia.

    python3 scripts/analisis.py           escribe el análisis
    python3 scripts/analisis.py --check   falla si lo publicado no es lo que sale de la evidencia

Lee solo lo que las rondas dejaron en tests/evidencias/ (resumen.json de cada ronda,
calificaciones.json y defectos.json) y escribe, en families/criterio-pmo/analisis/:

    analisis.json         los datos y los textos, en español e inglés: lo lee el portal
    ANALISIS.es.md        el análisis en Markdown, para GitHub
    ANALISIS.md           ídem, en inglés
    evolucion-es.svg …    las dos gráficas, en los dos idiomas

Ninguna cifra se teclea: cada número y cada frase con número sale de la evidencia, así que
el análisis se actualiza solo con cada ronda nueva y nunca dice algo que los datos no dicen.
Nunca se redondea a 100 % lo que no es 100 %.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EVID = RAIZ / "tests" / "evidencias"
SALIDA = RAIZ / "families" / "criterio-pmo" / "analisis"
REPO = "https://github.com/josenanez/criterio"
L = ("es", "en")

# El nombre corto de cada industria, de families/criterio-pmo/industrias.json: el mismo que usa el portal.
INDUSTRIA = {i["id"]: (i["es"]["corto"], i["en"]["corto"])
             for i in json.loads((RAIZ / "families" / "criterio-pmo" / "industrias.json").read_text(encoding="utf-8"))["industrias"]}
SENAL = {
    "milestone_met_without_evidence": ("Hito dado por cumplido sin evidencia", "Milestone marked met with no evidence"),
    "milestone_overdue": ("Hito vencido", "Overdue milestone"),
    "commitment_overdue": ("Compromiso vencido sin evidencia", "Overdue commitment with no evidence"),
    "commitment_undated": ("Compromiso que nadie fechó", "Commitment nobody dated"),
    "commitment_rescheduled": ("Compromiso prometido una y otra vez", "Commitment promised again and again"),
    "progress_vs_plan": ("Avance declarado que el plan no sostiene", "Declared progress the plan does not support"),
    "declared_vs_evidence": ("Verde que la evidencia no sostiene", "Green the evidence does not support"),
    "declaration_stale": ("Declaración vieja", "Stale declaration"),
    "variance_time": ("Desviación en tiempo", "Time variance"),
    "variance_cost": ("Desviación en costo", "Cost variance"),
    "budget_committed": ("Presupuesto comprometido sin holgura", "Budget committed with no headroom"),
    "rebaseline_unauthorized": ("Línea base movida más de lo autorizado", "Baseline moved beyond what was authorised"),
    "change_without_baseline": ("Cambio aprobado sin línea base nueva", "Approved change with no new baseline"),
    "silent": ("Proyecto sin actividad", "Project with no activity"),
    "contradiction": ("Dos documentos que se contradicen", "Two documents that contradict each other"),
    "governance_change": ("Cambio de patrocinador o comité", "Sponsor or committee change"),
    "pm_vs_pmo": ("Gerente y PMO no dicen lo mismo", "Manager and PMO do not say the same"),
    "vendor_deliverable_late": ("Entregable de proveedor vencido", "Late vendor deliverable"),
    "vendor_accepted_without_evidence": ("Entrega dada por aceptada sin evidencia", "Delivery accepted with no evidence"),
    "vendor_invoiced_without_delivery": ("Facturado sin entregable aceptado", "Invoiced with no accepted deliverable"),
    "vendor_invoiced_over_accepted": ("Facturado por encima de lo aceptado", "Invoiced above what was accepted"),
}
ORIGEN = {"codigo": ("Código", "Code"), "instrucciones": ("Instrucciones del agente", "Agent instructions"),
          "material": ("Material de prueba", "Test material"), "clave": ("Clave de calificación", "Grading key"),
          "arnes": ("Arnés de pruebas", "Test harness"), "agente": ("Comportamiento del modelo", "Model behavior")}
AGENTE = {"vera": "Vera", "samuel": "Samuel", "alba": "Alba", "rostrum": "Rostrum", "todos": ("Los tres", "All three")}
SERIES = [("vera", "Vera · precisión", "Vera · precision", "#d5a84b"),
          ("samuel", "Samuel · compromisos", "Samuel · commitments", "#4f86c6"),
          ("alba", "Alba · cobertura", "Alba · coverage", "#3f9a6a"),
          ("rostrum", "Rostrum · comprobaciones", "Rostrum · checks", "#a46fc9")]


# ── números ──────────────────────────────────────────────────────────────

def wilson(k: int, n: int):
    if not n:
        return None
    z = 1.96
    p, d = k / n, 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (math.floor(1000 * (c - h) + 1e-9) / 10, min(100.0, math.ceil(1000 * (c + h) - 1e-9) / 10))


def pct_valor(k: int, n: int):
    if not n:
        return None
    v = round(1000 * k / n) / 10
    return 99.9 if (k < n and v >= 100) else v


def dec(v: float, idioma: str) -> str:
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return s.replace(".", ",") if idioma == "es" else s


def num(n: int, idioma: str) -> str:
    if n < 10000:
        return str(n)
    s = f"{n:,}"
    return s.replace(",", " ") if idioma == "es" else s


def pct(k: int, n: int, idioma: str) -> str:
    v = pct_valor(k, n)
    if v is None:
        return "—"
    return f"{dec(v, idioma)} %" if idioma == "es" else f"{dec(v, idioma)}%"


def margen(ci, idioma: str) -> str:
    if not ci:
        return "—"
    a, b = (dec(x, idioma) for x in ci)
    return f"{a}–{b} %" if idioma == "es" else f"{a}–{b}%"


def de(k: int, n: int, idioma: str) -> str:
    return f"{num(k, idioma)} {'de' if idioma == 'es' else 'of'} {num(n, idioma)}"


# ── la evidencia ─────────────────────────────────────────────────────────

def cargar():
    rondas = []
    for d in (EVID / "rondas").glob("ronda-*"):
        if (d / "resumen.json").is_file():
            rondas.append(json.loads((d / "resumen.json").read_text(encoding="utf-8")))
    rondas.sort(key=lambda r: int(r["ronda"].split("-")[-1]))
    defectos = json.loads((EVID / "defectos.json").read_text(encoding="utf-8"))
    calif = json.loads((EVID / "calificaciones.json").read_text(encoding="utf-8"))
    return rondas, defectos, calif


def por_ronda(r: dict) -> dict:
    I = r["industrias"]
    s = lambda f: sum(f(x) or 0 for x in I)
    ro = [x["rostrum"] for x in I if x.get("rostrum")]
    return {
        "n": int(r["ronda"].split("-")[-1]), "fecha": r["fecha"],
        "version": next((x["vera"].get("version") for x in I if x.get("vera")), None),
        "industrias": len(I), "proyectos": s(lambda x: x["proyectos"]),
        "documentos": s(lambda x: x["documentos"]["total"]), "ejecuciones": s(lambda x: x["comandos"]),
        "contratos": s(lambda x: x["contratos"]), "fugas": s(lambda x: x["fugas"]),
        "minutos": s(lambda x: x["minutos"]), "tokens": s(lambda x: x["tokens"]),
        "vtp": s(lambda x: x["vera"]["aciertos"]), "vfp": s(lambda x: x["vera"]["falsos_positivos"]),
        "vfn": s(lambda x: x["vera"]["falsos_negativos"]),
        "ctrl": s(lambda x: x["vera"].get("controles")), "limpios": s(lambda x: x["vera"].get("controles_limpios")),
        "sok": s(lambda x: x["samuel"]["correctos"]), "stot": s(lambda x: x["samuel"]["total"]),
        "atp": s(lambda x: x["alba"]["aciertos"]), "aesp": s(lambda x: x["alba"]["esperados"]),
        "arep": s(lambda x: x["alba"]["reportados"]),
        "rp": sum(x["pasan"] for x in ro) if ro else None, "rt": sum(x["total"] for x in ro) if ro else None,
        "vera_ic": (r.get("vera") or {}),
        "por_industria": {x["entorno"]: x for x in I},
    }


def calcular():
    rondas, defectos, calif = cargar()
    R = [por_ronda(r) for r in rondas]
    if not R:
        raise SystemExit("no hay rondas en tests/evidencias/rondas")
    U = R[-1]
    T = Counter()
    for r in R:
        for k in ("proyectos", "documentos", "ejecuciones", "contratos", "fugas", "minutos", "tokens", "vtp", "vfp",
                  "vfn", "ctrl", "limpios", "sok", "stot", "atp", "aesp"):
            T[k] += r[k]
        if r["arep"]:
            T["arep"] += r["arep"]
            T["atp_rep"] += r["atp"]
        if r["rt"]:
            T["rp"] += r["rp"]
            T["rt"] += r["rt"]
            T["rondas_rostrum"] += 1
    formatos = Counter()
    for rr in rondas:
        for x in rr["industrias"]:
            formatos.update(x["documentos"]["por_formato"])
    ind = defaultdict(Counter)
    for r in R:
        for e, x in r["por_industria"].items():
            I = ind[e]
            I["vtp"] += x["vera"]["aciertos"]; I["vfp"] += x["vera"]["falsos_positivos"]; I["vfn"] += x["vera"]["falsos_negativos"]
            I["sok"] += x["samuel"]["correctos"]; I["stot"] += x["samuel"]["total"]
            I["atp"] += x["alba"]["aciertos"]; I["aesp"] += x["alba"]["esperados"]
            if x["alba"]["reportados"]:
                I["atp_rep"] += x["alba"]["aciertos"]; I["arep"] += x["alba"]["reportados"]
            if x.get("rostrum"):
                I["rp"] += x["rostrum"]["pasan"]; I["rt"] += x["rostrum"]["total"]
    senales = defaultdict(lambda: Counter())
    rondas_validas = {f"ronda-{r['n']}" for r in R}
    for c in calif:
        if c.get("material") in rondas_validas and c.get("tipo") == "primera":
            for s, v in (c.get("por_senal") or {}).items():
                senales[s]["tp"] += v.get("aciertos", 0); senales[s]["fp"] += v.get("falsos_positivos", 0)
                senales[s]["fn"] += v.get("falsos_negativos", 0)
                if v.get("falsos_positivos"):
                    senales[s]["fp_r" + str(int(c["material"].split("-")[-1]))] += v["falsos_positivos"]
    dpr = Counter(int(d["ronda"]) for d in defectos)   # "0" = antes de la primera ronda
    return R, U, T, formatos, ind, senales, defectos, dpr


# ── el texto ─────────────────────────────────────────────────────────────

def secciones():
    R, U, T, formatos, ind, senales, defectos, dpr = calcular()
    f = lambda i: i == "es"
    S = []
    primera = R[0]["n"]
    tramo = {"es": f"rondas {primera}–{U['n']}", "en": f"rounds {primera}–{U['n']}"}
    vic = U["vera_ic"]
    # desde qué ronda las cuatro métricas quedan por encima del 99 %
    def cuatro(r):
        vals = [pct_valor(r["vtp"], r["vtp"] + r["vfp"]), pct_valor(r["sok"], r["stot"]),
                pct_valor(r["atp"], r["aesp"]), pct_valor(r["rp"], r["rt"]) if r["rt"] else None]
        return all(v is not None and v >= 99 for v in vals)
    desde = None
    for r in reversed(R):
        if cuatro(r):
            desde = r["n"]
        else:
            break
    pendientes = [d["id"] for d in defectos if not d.get("verificado_en")]
    fallos_ind = [e for e, x in U["por_industria"].items() if x["vera"]["falsos_negativos"]]

    # 1 · resumen
    S.append({"id": "resumen", "titulo": {"es": "En una mirada", "en": "At a glance"},
              "parrafos": {i: [
                  (f"La versión más reciente probada, {U['version']}, en la ronda {U['n']}: Vera con {pct(U['vtp'], U['vtp'] + U['vfp'], i)} de precisión "
                   f"(margen del 95 %: {margen(vic.get('ic_precision'), i)}) y {pct(U['vtp'], U['vtp'] + U['vfn'], i)} de cobertura; Samuel con {pct(U['sok'], U['stot'], i)} de compromisos correctos; "
                   f"Alba con {pct(U['atp'], U['aesp'], i)} de alertas encontradas; Rostrum con {pct(U['rp'] or 0, U['rt'] or 0, i)} de comprobaciones."
                   if f(i) else
                   f"The most recent version tested, {U['version']}, in round {U['n']}: Vera at {pct(U['vtp'], U['vtp'] + U['vfp'], i)} precision "
                   f"(95% margin: {margen(vic.get('ic_precision'), i)}) and {pct(U['vtp'], U['vtp'] + U['vfn'], i)} coverage; Samuel at {pct(U['sok'], U['stot'], i)} commitments right; "
                   f"Alba at {pct(U['atp'], U['aesp'], i)} of alerts found; Rostrum at {pct(U['rp'] or 0, U['rt'] or 0, i)} of checks."),
                  (f"Sumando las {tramo['es']}, Vera acertó en el {pct(T['vtp'], T['vtp'] + T['vfp'], i)} de las {num(T['vtp'] + T['vfp'], i)} alertas que emitió "
                   f"y encontró el {pct(T['vtp'], T['vtp'] + T['vfn'], i)} de las {num(T['vtp'] + T['vfn'], i)} que había."
                   + (f" Desde la ronda {desde}, las cuatro métricas se mantienen por encima del 99 %." if desde else "")
                   if f(i) else
                   f"Across {tramo['en']}, Vera was right on {pct(T['vtp'], T['vtp'] + T['vfp'], i)} of the {num(T['vtp'] + T['vfp'], i)} alerts she raised "
                   f"and found {pct(T['vtp'], T['vtp'] + T['vfn'], i)} of the {num(T['vtp'] + T['vfn'], i)} there were."
                   + (f" Since round {desde}, all four measures have stayed above 99%." if desde else "")),
              ] for i in L}})

    # 2 · método
    fm = {"md": ("Markdown", "Markdown"), "docx": ("Word", "Word"), "pdf": ("PDF", "PDF"), "xlsx": ("Excel", "Excel"),
          "csv": ("CSV", "CSV"), "json": ("JSON", "JSON"), "txt": ("texto", "text")}
    fmt_txt = {i: ", ".join(f"{fm.get(k, (k, k))[0 if f(i) else 1]} {num(v, i)}" for k, v in formatos.most_common()) for i in L}
    inds = {i: ", ".join(INDUSTRIA[e][0 if f(i) else 1] for e in R[-1]["por_industria"]) for i in L}
    S.append({"id": "metodo", "titulo": {"es": "Qué se probó y cómo", "en": "What was tested and how"},
              "tabla": {"cab": {"es": ["", ""], "en": ["", ""]}, "filas": {i: [
                  ["Periodo" if f(i) else "Period", f"{len(R)} {'rondas' if f(i) else 'rounds'}, {R[0]['fecha']} → {U['fecha']}, {'versiones' if f(i) else 'versions'} {R[0]['version']} → {U['version']}"],
                  ["Industrias" if f(i) else "Industries", inds[i]],
                  ["Proyectos analizados" if f(i) else "Projects analyzed", num(T["proyectos"], i)],
                  ["Documentos procesados" if f(i) else "Documents processed", f"{num(T['documentos'], i)}: {fmt_txt[i]}"],
                  ["Ejecuciones" if f(i) else "Runs", num(T["ejecuciones"], i)],
                  ["Lecturas de la clave" if f(i) else "Reads of the key", num(T["fugas"], i)],
                  ["Proyectos de control" if f(i) else "Control projects", num(T["ctrl"], i)],
              ] for i in L}},
              "parrafos": {i: [
                  "Cada ronda sortea hechos nuevos y escribe una clave que ningún agente ve. Los datos de prueba se construyeron para ser más exigentes que la documentación de una PMO promedio, y cada industria lleva un proyecto sano que no debe levantar ninguna alerta."
                  if f(i) else
                  "Every round draws new facts and writes a key no agent sees. The test data was built to be more demanding than an average PMO's documentation, and every industry carries one healthy project that must raise no alert.",
                  "Precisión: de las alertas emitidas, cuántas eran correctas. Cobertura: de las que había, cuántas encontró. Margen del 95 %: intervalo de confianza de Wilson sobre los casos; para Vera en la última ronda, el que remuestrea proyectos."
                  if f(i) else
                  "Precision: of the alerts raised, how many were right. Coverage: of those there were, how many were found. 95% margin: Wilson confidence interval over the cases; for Vera in the latest round, the one that resamples projects.",
              ] for i in L}})

    # 3 · acumulado
    filas = lambda i: [
        ["Vera · " + ("precisión" if f(i) else "precision"), de(T["vtp"], T["vtp"] + T["vfp"], i), pct(T["vtp"], T["vtp"] + T["vfp"], i), margen(wilson(T["vtp"], T["vtp"] + T["vfp"]), i)],
        ["Vera · " + ("cobertura" if f(i) else "coverage"), de(T["vtp"], T["vtp"] + T["vfn"], i), pct(T["vtp"], T["vtp"] + T["vfn"], i), margen(wilson(T["vtp"], T["vtp"] + T["vfn"]), i)],
        ["Vera · " + ("proyectos de control sin alertas" if f(i) else "control projects with no alerts"), de(T["limpios"], T["ctrl"], i), pct(T["limpios"], T["ctrl"], i), margen(wilson(T["limpios"], T["ctrl"]), i)],
        ["Samuel · " + ("compromisos correctos" if f(i) else "commitments right"), de(T["sok"], T["stot"], i), pct(T["sok"], T["stot"], i), margen(wilson(T["sok"], T["stot"]), i)],
        ["Alba · " + ("cobertura" if f(i) else "coverage"), de(T["atp"], T["aesp"], i), pct(T["atp"], T["aesp"], i), margen(wilson(T["atp"], T["aesp"]), i)],
        ["Alba · " + ("precisión" if f(i) else "precision"), de(T["atp_rep"], T["arep"], i), pct(T["atp_rep"], T["arep"], i), margen(wilson(T["atp_rep"], T["arep"]), i)],
        ["Rostrum · " + ("comprobaciones" if f(i) else "checks") + f" ({T['rondas_rostrum']} {'rondas' if f(i) else 'rounds'})", de(T["rp"], T["rt"], i), pct(T["rp"], T["rt"], i), margen(wilson(T["rp"], T["rt"]), i)],
        ["Contratos cumplidos" if f(i) else "Contracts kept", de(T["contratos"], T["ejecuciones"], i), pct(T["contratos"], T["ejecuciones"], i), margen(wilson(T["contratos"], T["ejecuciones"]), i)],
    ]
    S.append({"id": "acumulado", "titulo": {"es": f"Resultados acumulados · {tramo['es']}", "en": f"Cumulative results · {tramo['en']}"},
              "tabla": {"cab": {"es": ["Agente · métrica", "Casos", "Resultado", "Margen del 95 %"], "en": ["Agent · measure", "Cases", "Result", "95% margin"]},
                        "filas": {i: filas(i) for i in L}},
              "parrafos": {i: ["Los acumulados de Samuel, Alba y Rostrum incluyen las primeras rondas, cuando esas capacidades se estaban construyendo; su valor actual es el de la versión más reciente."
                               if f(i) else "The totals for Samuel, Alba and Rostrum include the first rounds, while those capabilities were being built; their current value is the latest version's."] for i in L}})

    # 4 · evolución
    S.append({"id": "evolucion", "titulo": {"es": "Evolución por ronda", "en": "Round by round"},
              "imagen": {i: f"evolucion-{i}.svg" for i in L},
              "tabla": {"cab": {"es": ["Ronda · versión", "Proyectos", "Documentos", "Vera · precisión", "Samuel", "Alba · cobertura", "Rostrum", "Contratos", "Defectos"],
                                "en": ["Round · version", "Projects", "Documents", "Vera · precision", "Samuel", "Alba · coverage", "Rostrum", "Contracts", "Defects"]},
                        "filas": {i: [[f"{r['n']} · {r['version']}", num(r["proyectos"], i), num(r["documentos"], i),
                                       pct(r["vtp"], r["vtp"] + r["vfp"], i), pct(r["sok"], r["stot"], i), pct(r["atp"], r["aesp"], i),
                                       pct(r["rp"], r["rt"], i) if r["rt"] else ("No medido" if f(i) else "Not measured"),
                                       pct(r["contratos"], r["ejecuciones"], i), num(dpr.get(r["n"], 0), i)] for r in R] for i in L}}})

    # 5 · la versión más reciente
    def fila(nombre, k, n, ci, i):
        return [nombre, de(k, n, i), pct(k, n, i), margen(ci, i)]
    ult = lambda i: [
        fila("Vera · " + ("precisión" if f(i) else "precision"), U["vtp"], U["vtp"] + U["vfp"], vic.get("ic_precision"), i),
        fila("Vera · " + ("cobertura" if f(i) else "coverage"), U["vtp"], U["vtp"] + U["vfn"], vic.get("ic_cobertura"), i),
        fila("Samuel · " + ("compromisos correctos" if f(i) else "commitments right"), U["sok"], U["stot"], wilson(U["sok"], U["stot"]), i),
        fila("Alba · " + ("cobertura" if f(i) else "coverage"), U["atp"], U["aesp"], wilson(U["atp"], U["aesp"]), i),
        fila("Alba · " + ("precisión" if f(i) else "precision"), U["atp"], U["arep"], wilson(U["atp"], U["arep"]), i),
        fila("Rostrum · " + ("comprobaciones" if f(i) else "checks"), U["rp"] or 0, U["rt"] or 0, wilson(U["rp"] or 0, U["rt"] or 0), i),
        fila("Contratos cumplidos" if f(i) else "Contracts kept", U["contratos"], U["ejecuciones"], wilson(U["contratos"], U["ejecuciones"]), i),
    ]
    def fallos(i):
        p = []
        if U["vfp"] == 0:
            p.append("Vera no emitió ninguna alerta falsa." if f(i) else "Vera raised no false alert.")
        if U["vfn"]:
            donde = ", ".join(INDUSTRIA[e][0 if f(i) else 1] for e in fallos_ind)
            p.append(f"Vera no detectó {U['vfn']} alertas, {'todas ' if len(fallos_ind) == 1 else ''}en {donde}." if f(i) else f"Vera missed {U['vfn']} alerts, {'all ' if len(fallos_ind) == 1 else ''}in {donde}.")
        if U["arep"] > U["atp"]:
            k = U['arep'] - U['atp']
            p.append(f"Alba emitió {k} {'alerta que no estaba' if k == 1 else 'alertas que no estaban'} en la clave." if f(i)
                     else f"Alba raised {k} {'alert' if k == 1 else 'alerts'} not in the key.")
        if pendientes:
            p.append((f"Corregidos y por verificar en la próxima ronda: {', '.join(pendientes)}." if f(i)
                      else f"Fixed and to be verified in the next round: {', '.join(pendientes)}."))
        return " ".join(p)
    S.append({"id": "ultima", "titulo": {"es": f"La versión más reciente probada · {U['version']}, ronda {U['n']}",
                                          "en": f"The most recent version tested · {U['version']}, round {U['n']}"},
              "tabla": {"cab": {"es": ["Agente · métrica", "Casos", "Resultado", "Margen del 95 %"], "en": ["Agent · measure", "Cases", "Result", "95% margin"]},
                        "filas": {i: ult(i) for i in L}},
              "parrafos": {i: [fallos(i)] for i in L}})

    # 6 · por industria
    S.append({"id": "industrias", "titulo": {"es": f"Por industria · {tramo['es']}", "en": f"By industry · {tramo['en']}"},
              "tabla": {"cab": {"es": ["Industria", "Vera · precisión", "Vera · cobertura", "Samuel", "Alba · cobertura", "Alba · precisión", "Rostrum"],
                                "en": ["Industry", "Vera · precision", "Vera · coverage", "Samuel", "Alba · coverage", "Alba · precision", "Rostrum"]},
                        "filas": {i: [[INDUSTRIA[e][0 if f(i) else 1], pct(I["vtp"], I["vtp"] + I["vfp"], i), pct(I["vtp"], I["vtp"] + I["vfn"], i),
                                       pct(I["sok"], I["stot"], i), pct(I["atp"], I["aesp"], i), pct(I["atp_rep"], I["arep"], i), pct(I["rp"], I["rt"], i)]
                                      for e, I in sorted(ind.items(), key=lambda kv: list(INDUSTRIA).index(kv[0]))] for i in L}}})

    # 7 · por tipo de alerta
    orden = sorted(senales.items(), key=lambda kv: (kv[1]["tp"] == 0, -kv[1]["tp"], -kv[1]["fp"]))
    limpias = sum(1 for _, v in orden if v["fp"] == 0)
    fp_total = sum(v["fp"] for _, v in orden)
    nunca = [s for s, v in orden if v["tp"] == 0 and v["fp"] > 0]
    def texto_senales(i):
        t = (f"Vera emitió alertas de {len(orden)} tipos; en {limpias} no tuvo una sola alerta falsa, y las {fp_total} falsas se concentran en {len(orden) - limpias}."
             if f(i) else f"Vera raised alerts of {len(orden)} types; {limpias} had not a single false alert, and the {fp_total} false ones sit in {len(orden) - limpias}.")
        for s in nunca:
            v = senales[s]
            rr = sorted(int(k[4:]) for k in v if k.startswith("fp_r"))
            ult_r = [n for n in rr if n == U["n"]]
            t += (f" «{SENAL[s][0]}» todavía no se sostiene: {v['fp']} falsas y ninguna correcta, la última en la ronda {rr[-1]}"
                  + ("." if ult_r else f", ninguna en la ronda {U['n']}. Es la que hay que reforzar.")
                  if f(i) else
                  f" “{SENAL[s][1]}” does not hold yet: {v['fp']} false and none right, the latest in round {rr[-1]}"
                  + ("." if ult_r else f", none in round {U['n']}. It is the one to strengthen."))
        return t
    S.append({"id": "senales", "titulo": {"es": f"Por tipo de alerta · Vera, {tramo['es']}", "en": f"By alert type · Vera, {tramo['en']}"},
              "tabla": {"cab": {"es": ["Tipo de alerta", "Correctas", "Falsas", "No detectadas", "Precisión", "Cobertura"],
                                "en": ["Alert type", "Right", "False", "Missed", "Precision", "Coverage"]},
                        "filas": {i: [[SENAL.get(s, (s, s))[0 if f(i) else 1], num(v["tp"], i), num(v["fp"], i), num(v["fn"], i),
                                       pct(v["tp"], v["tp"] + v["fp"], i), pct(v["tp"], v["tp"] + v["fn"], i)] for s, v in orden] for i in L}},
              "parrafos": {i: [texto_senales(i)] for i in L}})

    # 8 · defectos
    org = Counter(d["origen"] for d in defectos)
    ag = Counter(d["agente"] for d in defectos)
    prueba = org.get("material", 0) + org.get("clave", 0) + org.get("arnes", 0)
    ver = sum(1 for d in defectos if d.get("verificado_en"))
    S.append({"id": "defectos", "titulo": {"es": "Defectos", "en": "Defects"}, "imagen": {i: f"defectos-{i}.svg" for i in L},
              "parrafos": {i: [
                  (f"{len(defectos)} defectos registrados, cada uno con su origen, su corrección y la ronda que la verificó: {ver} verificados y {len(defectos) - ver} por verificar. "
                   f"{prueba} vinieron del material, la clave o el arnés de pruebas, no de los agentes."
                   if f(i) else
                   f"{len(defectos)} defects logged, each with its origin, its fix and the round that verified it: {ver} verified and {len(defectos) - ver} to verify. "
                   f"{prueba} came from the material, the key or the test harness, not from the agents.")] for i in L},
              "tabla": {"cab": {"es": ["Origen", "Defectos"], "en": ["Origin", "Defects"]},
                        "filas": {i: [[ORIGEN.get(k, (k, k))[0 if f(i) else 1], num(v, i)] for k, v in org.most_common()] for i in L}},
              "tabla2": {"cab": {"es": ["Agente", "Defectos"], "en": ["Agent", "Defects"]},
                         "filas": {i: [[(AGENTE.get(k, k) if isinstance(AGENTE.get(k, k), str) else AGENTE[k][0 if f(i) else 1]), num(v, i)] for k, v in ag.most_common()] for i in L}}})

    # 9 · consumo y límites
    mpp = T["minutos"] / T["proyectos"]
    S.append({"id": "consumo", "titulo": {"es": "Tiempo, consumo y próximo paso", "en": "Time, cost and next step"},
              "parrafos": {i: [
                  (f"Las {len(R)} rondas tomaron {num(round(T['minutos'] / 60), i)} horas de ejecución para {num(T['proyectos'], i)} proyectos: "
                   f"{dec(mpp, i)} minutos por proyecto, con todos los comandos de los tres agentes y el servidor. "
                   f"Usaron {num(round(T['tokens'] / 1e6), i)} millones de tokens; en promedio, {num(round(T['tokens'] / 1e6 / len(R)), i)} millones por ronda."
                   if f(i) else
                   f"The {len(R)} rounds took {num(round(T['minutos'] / 60), i)} hours of run time for {num(T['proyectos'], i)} projects: "
                   f"{dec(mpp, i)} minutes per project, with every command of the three agents and the server. "
                   f"They used {num(round(T['tokens'] / 1e6), i)} million tokens; on average, {num(round(T['tokens'] / 1e6 / len(R)), i)} million per round."),
                  ("Las actas, los informes y las síntesis que redacta el modelo de lenguaje (LLM) se verifican por el contrato de cada comando y por la aritmética de sus cifras. "
                   "Si una versión es estable o de laboratorio lo dice esta evidencia, no su número: estable, con el piso del margen del 95 % en 95 % o más en cada agente y ninguna alerta en los proyectos de control (decisión 0020)."
                   if f(i) else
                   "The minutes, reports and syntheses the language model (LLM) writes are checked through each command's contract and the arithmetic of their figures. "
                   "Whether a version is stable or laboratory is said by this evidence, not its number: stable, with the floor of the 95% margin at 95% or more for every agent and no alert in the control projects (decision 0020)."),
              ] for i in L}})
    meta = {"generado_desde": "tests/evidencias", "ultima_ronda": U["n"], "fecha": U["fecha"], "version": U["version"],
            "rondas": [r["n"] for r in R]}
    graf = {"evolucion": [{"n": r["n"], "vera": pct_valor(r["vtp"], r["vtp"] + r["vfp"]), "samuel": pct_valor(r["sok"], r["stot"]),
                           "alba": pct_valor(r["atp"], r["aesp"]), "rostrum": pct_valor(r["rp"], r["rt"]) if r["rt"] else None} for r in R],
            "defectos": [{"n": n, "defectos": dpr.get(n, 0)} for n in sorted(set(dpr) | {r["n"] for r in R})]}
    return meta, S, graf


# ── las gráficas ─────────────────────────────────────────────────────────

FONDO, TINTA, GRIS, FILETE = "#050505", "#f5f4ef", "#8a867e", "#2b2b28"


def svg_evolucion(g, idioma, series=None, titulo=None, subtitulo=None):
    """La gráfica de evolución. La de la PMO por omisión; una familia pasa sus series y sus textos."""
    series = SERIES if series is None else series
    W, H, x0, x1, y0, y1 = 760, 380, 60, 700, 110, 330
    ns = [p["n"] for p in g]
    nmin, nmax = min(ns), max(ns)
    x = lambda n: x0 + (n - nmin) * (x1 - x0) / max(1, nmax - nmin)
    y = lambda v: y1 - v / 100 * (y1 - y0)
    t = titulo[idioma] if titulo else ("Evolución por ronda de las cuatro métricas", "The four measures, round by round")[idioma == "en"]
    sub = subtitulo[idioma] if subtitulo else ("Porcentaje en las 4 industrias. Vera, Samuel y Alba contra la clave; Rostrum por comprobación",
           "Percentage across the 4 industries. Vera, Samuel and Alba against the key; Rostrum by check")[idioma == "en"]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter, Arial, sans-serif" font-size="12">',
           f'<rect width="{W}" height="{H}" fill="{FONDO}"/>',
           f'<text x="{x0}" y="32" font-size="17" fill="{TINTA}">{t}</text>',
           f'<text x="{x0}" y="54" fill="{GRIS}">{sub}</text>']
    for k, (slug, es, en, c) in enumerate(series):
        out.append(f'<line x1="{x0 + k * 165}" x2="{x0 + k * 165 + 18}" y1="78" y2="78" stroke="{c}" stroke-width="3"/>'
                   f'<text x="{x0 + k * 165 + 24}" y="82" fill="{TINTA}">{es if idioma == "es" else en}</text>')
    for v in (0, 25, 50, 75, 100):
        out.append(f'<line x1="{x0}" x2="{x1}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{FILETE}"/>'
                   f'<text x="{x0 - 8}" y="{y(v) + 4:.1f}" text-anchor="end" fill="{GRIS}">{v}{" %" if idioma == "es" else "%"}</text>')
    out.append(f'<line x1="{x0}" x2="{x1}" y1="{y(99):.1f}" y2="{y(99):.1f}" stroke="{GRIS}" stroke-dasharray="4 4"/>'
               f'<text x="{x1 + 6}" y="{y(99) + 4:.1f}" fill="{GRIS}">99{" %" if idioma == "es" else "%"}</text>')
    for n in ns:
        out.append(f'<text x="{x(n):.1f}" y="{y1 + 20}" text-anchor="middle" fill="{GRIS}">R{n}</text>')
    for slug, _, _, c in series:
        pts = [(p["n"], p[slug]) for p in g if p[slug] is not None]
        if not pts:
            continue
        d = " ".join(f"{'L' if j else 'M'}{x(n):.1f},{y(v):.1f}" for j, (n, v) in enumerate(pts))
        out.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2.5"/>')
        out += [f'<circle cx="{x(n):.1f}" cy="{y(v):.1f}" r="3.5" fill="{c}"/>' for n, v in pts]
    out.append("</svg>")
    return "\n".join(out) + "\n"


def svg_defectos(g, idioma, subtitulo=None):
    W, H, x0, x1, y0, y1 = 760, 340, 60, 720, 80, 290
    pico = max(p["defectos"] for p in g) or 1
    banda = (x1 - x0) / len(g)
    total = sum(p["defectos"] for p in g)
    t = ("Defectos encontrados por ronda", "Defects found per round")[idioma == "en"]
    sub = subtitulo(total)[idioma] if subtitulo else (f"{total} en total; R0 son los encontrados antes de la primera ronda", f"{total} in total; R0 are those found before the first round")[idioma == "en"]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter, Arial, sans-serif" font-size="12">',
           f'<rect width="{W}" height="{H}" fill="{FONDO}"/>',
           f'<text x="{x0}" y="32" font-size="17" fill="{TINTA}">{t}</text>',
           f'<text x="{x0}" y="54" fill="{GRIS}">{sub}</text>']
    for k, p in enumerate(g):
        xi = x0 + k * banda
        h = p["defectos"] / pico * (y1 - y0)
        c = "#d5a84b" if k == len(g) - 1 else "#4a4740"
        out.append(f'<rect x="{xi + banda * 0.2:.1f}" y="{y1 - h:.1f}" width="{banda * 0.6:.1f}" height="{h:.1f}" fill="{c}"/>'
                   f'<text x="{xi + banda / 2:.1f}" y="{y1 - h - 6:.1f}" text-anchor="middle" fill="{TINTA}">{p["defectos"]}</text>'
                   f'<text x="{xi + banda / 2:.1f}" y="{y1 + 18}" text-anchor="middle" fill="{GRIS}">R{p["n"]}</text>')
    out.append(f'<line x1="{x0}" x2="{x1}" y1="{y1}" y2="{y1}" stroke="{GRIS}"/></svg>')
    return "\n".join(out) + "\n"


# ── el Markdown ──────────────────────────────────────────────────────────

def tabla_md(cab, filas):
    cab = [c or " " for c in cab]
    return "\n".join(["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)] + ["| " + " | ".join(str(c) for c in f) + " |" for f in filas])


def markdown(meta, S, idioma):
    es = idioma == "es"
    otro = "ANALISIS.md" if es else "ANALISIS.es.md"
    out = ["# " + ("Análisis estadístico de las pruebas · familia PMO" if es else "Statistical analysis of the tests · PMO family"), "",
           (f"Generado por `scripts/analisis.py` desde `tests/evidencias/` · ronda más reciente: {meta['ultima_ronda']} ({meta['fecha']}), versión probada {meta['version']} · "
            f"[English]({otro})" if es else
            f"Generated by `scripts/analisis.py` from `tests/evidencias/` · latest round: {meta['ultima_ronda']} ({meta['fecha']}), version tested {meta['version']} · "
            f"[Español]({otro})"), "",
           ("No se edita a mano: cada cifra sale de la evidencia y el análisis se regenera con cada ronda." if es else
            "Not edited by hand: every figure comes from the evidence and the analysis is regenerated with every round."), ""]
    for s in S:
        out += ["## " + s["titulo"][idioma], ""]
        if s.get("imagen"):
            out += [f"![{s['titulo'][idioma]}]({s['imagen'][idioma]})", ""]
        for p in (s.get("parrafos") or {}).get(idioma, []):
            out += [p, ""]
        for k in ("tabla", "tabla2"):
            if s.get(k):
                out += [tabla_md(s[k]["cab"][idioma], s[k]["filas"][idioma]), ""]
    out += ["---", "", (f"La evidencia completa de cada ronda: [`tests/evidencias/`]({REPO}/tree/main/tests/evidencias)." if es else
                       f"The full evidence of every round: [`tests/evidencias/`]({REPO}/tree/main/tests/evidencias)."), ""]
    return "\n".join(out)


def archivos():
    meta, S, graf = secciones()
    salida = {"analisis.json": json.dumps({"meta": meta, "secciones": S}, ensure_ascii=False, indent=1) + "\n",
              "ANALISIS.es.md": markdown(meta, S, "es"), "ANALISIS.md": markdown(meta, S, "en")}
    for i in L:
        salida[f"evolucion-{i}.svg"] = svg_evolucion(graf["evolucion"], i)
        salida[f"defectos-{i}.svg"] = svg_defectos(graf["defectos"], i)
    return salida


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    malos = []
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, contenido in archivos().items():
        ruta = SALIDA / nombre
        if a.check:
            if not ruta.is_file() or ruta.read_text(encoding="utf-8") != contenido:
                malos.append(nombre)
        elif not ruta.is_file() or ruta.read_text(encoding="utf-8") != contenido:
            ruta.write_text(contenido, encoding="utf-8")
            print(f"  {ruta.relative_to(RAIZ)}")
    for m in malos:
        print(f"  ✗ {m} no es el que sale de la evidencia: corre python3 scripts/analisis.py")
    if a.check and not malos:
        print("  el análisis es el que sale de la evidencia")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
