#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El análisis estadístico de las pruebas de las familias CFO y CLO, calculado de la evidencia.

    python3 scripts/analisis_familias.py           escribe el análisis de las dos familias
    python3 scripts/analisis_familias.py --check   falla si lo publicado no es lo que sale de la evidencia

Es el mismo análisis de la PMO (scripts/analisis.py), con lo que miden las rondas de estas
familias. Lee solo lo que las rondas dejaron en tests/evidencias/familias/<familia>/ —cada
calificacion.json, sus repetidas y defectos.json— y escribe, en families/criterio-<familia>/analisis/:

    analisis.json         los datos y los textos, en español e inglés: lo lee el portal
    ANALISIS.es.md        el análisis en Markdown, para GitHub
    ANALISIS.md           ídem, en inglés
    evolucion-es.svg …    las dos gráficas, en los dos idiomas

Ninguna cifra se teclea: cada número sale de la evidencia. Las tablas nombran el material por
industria y país, nunca por el nombre de la entidad de prueba. Los números, los márgenes, las
gráficas y el Markdown son los de scripts/analisis.py: aquí no se reescribe ninguno.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import analisis as A  # noqa: E402

_spec = importlib.util.spec_from_file_location("ronda_familia", RAIZ / "tests" / "ronda_familia.py")
RF = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(RF)

L = A.L
REPO = A.REPO
FAM = {
    "cfo": {"titulo": ("familia CFO", "CFO family"), "agentes": {"clara": "Clara", "tomas": "Tomás"}},
    "clo": {"titulo": ("familia CLO", "CLO family"), "agentes": {"fidel": "Fidel", "constanza": "Constanza"}},
}
INDUSTRIA = {"banca": ("Banca", "Banking"), "cooperativas": ("Cooperativas", "Credit unions"), "retail": ("Retail", "Retail"),
             "mineria": ("Minería", "Mining"), "control": ("Control", "Control")}
# Los nombres de los países salen del registro único del motor, no de aquí.
PAIS = {p["codigo"]: (p["nombre"]["es"], p["nombre"]["en"]) for p in json.loads(
    (RAIZ / "plugins" / "criterio-finance" / "scripts" / "paises.json").read_text(encoding="utf-8"))["paises"]}
ORIGEN = {**A.ORIGEN, "arnes": ("Arnés de pruebas", "Test harness")}
SERIES = [("cobertura", "Señales · cobertura", "Signals · coverage", "#d5a84b"),
          ("precision", "Señales · precisión", "Signals · precision", "#4f86c6"),
          ("extraccion", "Extracción · datos", "Extraction · data", "#3f9a6a")]
pct, de, num, margen, wilson, pct_valor, dec = A.pct, A.de, A.num, A.margen, A.wilson, A.pct_valor, A.dec


# ── la evidencia ─────────────────────────────────────────────────────────

def material(sigla: str, carpeta: str, i: int) -> str:
    ind, pais = (x.strip() for x in RF._material(sigla, carpeta).split("·"))
    return f"{INDUSTRIA.get(ind, (ind, ind))[i]} · {PAIS.get(pais, (pais, pais))[i]}"


def cargar(sigla: str):
    base = RAIZ / "tests" / "evidencias" / "familias" / sigla
    corridas = []
    for c in sorted(base.glob("ronda-*/*/calificacion.json")):
        k = json.loads(c.read_text(encoding="utf-8"))
        rep = sum(json.loads(r.read_text(encoding="utf-8")).get("tokens", 0) for r in (c.parent / "repetidas").glob("*.json"))
        s, e = k["senales"], k["extraccion"]
        corridas.append({
            "ronda": int(c.parent.parent.name.split("-")[-1]), "carpeta": c.parent.name,
            "control": RF._material(sigla, c.parent.name).startswith("control"),
            "agentes": k["agentes"], "tokens": k["tokens"], "repetidos": rep,
            "esperadas": s["esperadas"], "acertadas": s["acertadas"], "de_mas": len(s["de_mas"]), "faltantes": len(s["faltantes"]),
            "lista_de_mas": s["de_mas"], "lista_faltantes": s["faltantes"],
            "campos": e["campos"], "bien": e["bien"], "mal": e["mal"],
        })
    defectos = json.loads((base / "defectos.json").read_text(encoding="utf-8"))["defectos"]
    entidades = sorted(d.name for d in (RAIZ / "tests" / f"criterio-{sigla}" / "material").iterdir() if (d / "clave.json").is_file())
    return corridas, defectos, entidades


def suma(cs):
    t = Counter()
    for c in cs:
        for k in ("esperadas", "acertadas", "de_mas", "campos", "bien", "tokens", "repetidos"):
            t[k] += c[k]
    ctrl = [c for c in cs if c["control"]]
    t["controles"], t["limpios"] = len(ctrl), sum(1 for c in ctrl if c["de_mas"] == 0)
    t["corridas"] = len(cs)
    return t


# ── las secciones ────────────────────────────────────────────────────────

def secciones(sigla: str):
    C, D, ENT = cargar(sigla)
    f = lambda i: i == "es"
    ix = lambda i: 0 if f(i) else 1
    rondas = sorted({c["ronda"] for c in C})
    por = {n: [c for c in C if c["ronda"] == n] for n in rondas}
    # la ronda completa: la que corrió todas las entidades del material
    completas = [n for n in rondas if {RF._material(sigla, c["carpeta"]) for c in por[n]} >= {RF._material(sigla, e) for e in ENT}
                 and len(por[n]) >= len(ENT)]
    U = max(completas) if completas else max(rondas)
    # Sin una ronda que cubra todo el material de hoy —porque entró una industria o un país—, la
    # cabecera es la más reciente y dice que es parcial: no se llama completa a lo que no lo es.
    completa = U in completas
    cual = {"es": (f"La ronda completa más reciente, la {U}, sobre las {len(por[U])} entidades del material" if completa else
                   f"La ronda más reciente, la {U}, parcial, sobre {len(por[U])} de las {len(ENT)} entidades del material"),
            "en": (f"The most recent complete round, round {U}, on the material's {len(por[U])} entities" if completa else
                   f"The most recent round, round {U}, partial, on {len(por[U])} of the material's {len(ENT)} entities")}
    T, UT = suma(C), suma(por[U])
    tramo = {"es": f"rondas {rondas[0]}–{rondas[-1]}", "en": f"rounds {rondas[0]}–{rondas[-1]}"}
    S = []
    prec = lambda t: (t["acertadas"], t["acertadas"] + t["de_mas"])

    # 1 · resumen
    S.append({"id": "resumen", "titulo": {"es": "En una mirada", "en": "At a glance"}, "parrafos": {i: [
        (f"{cual['es']}: {de(UT['acertadas'], UT['esperadas'], i)} señales sembradas encontradas "
         f"(margen del 95 %: {margen(wilson(UT['acertadas'], UT['esperadas']), i)}) y {num(UT['de_mas'], i)} de más; {de(UT['bien'], UT['campos'], i)} datos extraídos bien "
         f"({pct(UT['bien'], UT['campos'], i)}, margen del 95 %: {margen(wilson(UT['bien'], UT['campos']), i)}); y {de(UT['limpios'], UT['controles'], i)} entidades de control sin ninguna señal."
         if f(i) else
         f"{cual['en']}: {de(UT['acertadas'], UT['esperadas'], i)} seeded signals found "
         f"(95% margin: {margen(wilson(UT['acertadas'], UT['esperadas']), i)}) and {num(UT['de_mas'], i)} extra; {de(UT['bien'], UT['campos'], i)} data items extracted right "
         f"({pct(UT['bien'], UT['campos'], i)}, 95% margin: {margen(wilson(UT['bien'], UT['campos']), i)}); and {de(UT['limpios'], UT['controles'], i)} control entities with no signal at all."),
        (f"Sumando las {tramo['es']}, {de(T['acertadas'], T['esperadas'], i)} señales encontradas, {num(T['de_mas'], i)} de más y {de(T['bien'], T['campos'], i)} datos bien. "
         "Las rondas repiten el mismo material: no son muestras independientes, y el margen se calcula sobre los casos de cada una."
         if f(i) else
         f"Across {tramo['en']}, {de(T['acertadas'], T['esperadas'], i)} signals found, {num(T['de_mas'], i)} extra and {de(T['bien'], T['campos'], i)} data items right. "
         "The rounds repeat the same material: they are not independent samples, and the margin is computed over each round's cases."),
    ] for i in L}})

    # 2 · método
    inds = lambda i: ", ".join(sorted({material(sigla, c["carpeta"], ix(i)) for c in por[U] if not c["control"]}))
    ctrls = lambda i: ", ".join(sorted({material(sigla, c["carpeta"], ix(i)) for c in por[U] if c["control"]}))
    S.append({"id": "metodo", "titulo": {"es": "Qué se probó y cómo", "en": "What was tested and how"},
              "tabla": {"cab": {"es": ["", ""], "en": ["", ""]}, "filas": {i: [
                  ["Rondas" if f(i) else "Rounds", f"{len(rondas)}; " + ((f"la completa más reciente es la {U}" if completa else f"la más reciente, la {U}, es parcial") if f(i) else
                                                                       (f"the most recent complete one is round {U}" if completa else f"the most recent, round {U}, is partial"))],
                  ["Material" if f(i) else "Material", inds(i)],
                  ["Entidades de control" if f(i) else "Control entities", ctrls(i)],
                  ["Corridas de una entidad" if f(i) else "Entity runs", num(T["corridas"], i)],
                  ["Señales sembradas" if f(i) else "Seeded signals", num(T["esperadas"], i)],
                  ["Datos calificados" if f(i) else "Data items graded", num(T["campos"], i)],
              ] for i in L}},
              "parrafos": {i: [
                  "Cada entidad corre todos los comandos de los dos agentes, con un tope de tokens fijado antes de empezar, sobre un material que trae su clave aparte: el agente nunca la ve. "
                  "Las señales se comparan por su nombre y su clave; la extracción, campo por campo, contra lo que traen los documentos escritos. Las entidades de control no tienen ningún defecto sembrado: cualquier señal en ellas es una falla."
                  if f(i) else
                  "Each entity runs every command of the two agents, with a token cap set before starting, on material whose key is kept apart: the agent never sees it. "
                  "Signals are compared by name and key; extraction, field by field, against what the written documents say. Control entities carry no seeded defect: any signal in them is a failure.",
                  "Cobertura: de las señales sembradas, cuántas encontró. Precisión: de las que levantó, cuántas eran correctas. Margen del 95 %: intervalo de confianza de Wilson sobre los casos."
                  if f(i) else
                  "Coverage: of the seeded signals, how many were found. Precision: of those raised, how many were right. 95% margin: Wilson confidence interval over the cases.",
              ] for i in L}})

    # 3 · acumulado y 5 · la ronda completa
    def filas(t, i):
        return [
            ["Señales · cobertura" if f(i) else "Signals · coverage", de(t["acertadas"], t["esperadas"], i), pct(t["acertadas"], t["esperadas"], i), margen(wilson(t["acertadas"], t["esperadas"]), i)],
            ["Señales · precisión" if f(i) else "Signals · precision", de(*prec(t), i), pct(*prec(t), i), margen(wilson(*prec(t)), i)],
            ["Extracción · datos correctos" if f(i) else "Extraction · data right", de(t["bien"], t["campos"], i), pct(t["bien"], t["campos"], i), margen(wilson(t["bien"], t["campos"]), i)],
            ["Control · sin ninguna señal" if f(i) else "Control · with no signal", de(t["limpios"], t["controles"], i), pct(t["limpios"], t["controles"], i), margen(wilson(t["limpios"], t["controles"]), i)],
        ]
    cab = {"es": ["Métrica", "Casos", "Resultado", "Margen del 95 %"], "en": ["Measure", "Cases", "Result", "95% margin"]}
    S.append({"id": "acumulado", "titulo": {"es": f"Resultados acumulados · {tramo['es']}", "en": f"Cumulative results · {tramo['en']}"},
              "tabla": {"cab": cab, "filas": {i: filas(T, i) for i in L}}})

    # 4 · evolución
    dpr = Counter(d["ronda"] for d in D)
    S.append({"id": "evolucion", "titulo": {"es": "Evolución por ronda", "en": "Round by round"}, "imagen": {i: f"evolucion-{i}.svg" for i in L},
              "tabla": {"cab": {"es": ["Ronda", "Entidades", "Señales · cobertura", "Señales · precisión", "Extracción", "Control sin señales", "Tokens", "Defectos"],
                                "en": ["Round", "Entities", "Signals · coverage", "Signals · precision", "Extraction", "Control with no signal", "Tokens", "Defects"]},
                        "filas": {i: [[str(n), num(len(por[n]), i), pct(suma(por[n])["acertadas"], suma(por[n])["esperadas"], i), pct(*prec(suma(por[n])), i),
                                       pct(suma(por[n])["bien"], suma(por[n])["campos"], i), de(suma(por[n])["limpios"], suma(por[n])["controles"], i),
                                       f"{dec(suma(por[n])['tokens'] / 1e6, i)} M", num(dpr.get(n, 0), i)] for n in rondas] for i in L}},
              "parrafos": {i: [("Una ronda que no corre todas las entidades es parcial: la primera, pequeña, antes de la completa, o una de verificación, que repite las corridas que un defecto corregido dejó pendientes."
                                if f(i) else "A round that does not run every entity is partial: the first, small one, before the complete one, or a verification round, which repeats the runs a fixed defect left pending.")]
                           for i in L} if len(completas) < len(rondas) else None})
    if S[-1]["parrafos"] is None:
        del S[-1]["parrafos"]

    S.append({"id": "ultima", "titulo": {"es": f"La ronda {'completa ' if completa else ''}más reciente · ronda {U}",
                                         "en": f"The most recent {'complete ' if completa else ''}round · round {U}"},
              "tabla": {"cab": cab, "filas": {i: filas(UT, i) for i in L}}})

    # 6 · por material
    S.append({"id": "industrias", "titulo": {"es": f"Por industria y país · ronda {U}", "en": f"By industry and country · round {U}"},
              "tabla": {"cab": {"es": ["Material", "Agentes", "Señales", "De más", "Extracción", "Tokens"],
                                "en": ["Material", "Agents", "Signals", "Extra", "Extraction", "Tokens"]},
                        "filas": {i: [[material(sigla, c["carpeta"], ix(i)), ", ".join(FAM[sigla]["agentes"].get(a, a) for a in c["agentes"]),
                                       de(c["acertadas"], c["esperadas"], i), num(c["de_mas"], i), de(c["bien"], c["campos"], i),
                                       f"{dec(c['tokens'] / 1e6, i)} M"] for c in sorted(por[U], key=lambda c: (c["control"], material(sigla, c["carpeta"], 0)))] for i in L}}})

    # 7 · lo que falló, uno por uno
    fallas = []
    for c in C:
        for x in c["lista_faltantes"]:
            fallas.append((c, ("Señal no encontrada", "Signal missed"), x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)[:80]))
        for x in c["lista_de_mas"]:
            fallas.append((c, ("Señal de más", "Extra signal"), x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)[:80]))
        for x in c["mal"]:
            fallas.append((c, ("Dato calificado como mal", "Data item graded wrong"), f"{x.get('ficha', '')} · {x.get('campo', '')}"))
    # cada dato mal calificado con el defecto que lo explica, del campo «fallas» de defectos.json
    def defectos_de(c, donde):
        return [d for d in D if [c["ronda"], c["carpeta"], donde] in (d.get("fallas") or [])]
    defecto = lambda c, donde: ", ".join(d["id"] for d in defectos_de(c, donde)) or "—"
    origen = lambda c, donde, i: ", ".join(sorted({ORIGEN.get(d["origen"], (d["origen"],) * 2)[ix(i)] for d in defectos_de(c, donde)})) or "—"
    de_la_prueba = sum(1 for c, _, donde in fallas if any(d["origen"] in ("material", "clave", "arnes") for d in defectos_de(c, donde)))
    S.append({"id": "senales", "titulo": {"es": f"Lo que falló, uno por uno · {tramo['es']}", "en": f"What failed, one by one · {tramo['en']}"},
              "parrafos": {i: [(f"{len(fallas)} {'falla' if len(fallas) == 1 else 'fallas'} en {num(T['corridas'], i)} corridas, cada una con el defecto que la explica: "
                                 f"su origen dice si falló el agente o la prueba. Las cifras son las de la calificación original: {de_la_prueba} {'de esas fallas vino' if de_la_prueba == 1 else 'de esas fallas vinieron'} de la prueba "
                                 "—el arnés o la clave—, no del agente, y con la prueba corregida se califican como correctas."
                                if f(i) else f"{len(fallas)} {'failure' if len(fallas) == 1 else 'failures'} in {num(T['corridas'], i)} runs, each with the defect that explains it: "
                                 f"its origin says whether the agent or the test failed. The figures are those of the original grading: {de_la_prueba} of those {'failures' if de_la_prueba != 1 else 'failures'} came from the test "
                                 "—the harness or the key—, not from the agent, and with the test fixed they grade as right.")
                               if fallas else ("Ninguna falla." if f(i) else "No failures.")] for i in L},
              "tabla": {"cab": {"es": ["Ronda", "Material", "Qué", "Dónde", "Defecto", "Origen"], "en": ["Round", "Material", "What", "Where", "Defect", "Origin"]},
                        "filas": {i: [[str(c["ronda"]), material(sigla, c["carpeta"], ix(i)), q[ix(i)], donde, defecto(c, donde), origen(c, donde, i)] for c, q, donde in fallas] for i in L}}})

    # 8 · defectos
    org = Counter(d["origen"] for d in D)
    ag = Counter(a for d in D for a in (d["agentes"] or ["—"]))
    prueba = org.get("material", 0) + org.get("clave", 0) + org.get("arnes", 0)
    ver = sum(1 for d in D if d.get("estado") == "verificado")
    S.append({"id": "defectos", "titulo": {"es": "Defectos", "en": "Defects"}, "imagen": {i: f"defectos-{i}.svg" for i in L},
              "parrafos": {i: [(f"{len(D)} defectos registrados, cada uno con su origen, su corrección y la corrida que la verificó: {ver} verificados y {len(D) - ver} por verificar. "
                                f"{prueba} vinieron del material, la clave o el arnés de pruebas, no de los agentes."
                                if f(i) else
                                f"{len(D)} defects logged, each with its origin, its fix and the run that verified it: {ver} verified and {len(D) - ver} to verify. "
                                f"{prueba} came from the material, the key or the test harness, not from the agents.")] for i in L},
              "tabla": {"cab": {"es": ["Origen", "Defectos"], "en": ["Origin", "Defects"]},
                        "filas": {i: [[ORIGEN.get(k, (k, k))[ix(i)], num(v, i)] for k, v in org.most_common()] for i in L}},
              "tabla2": {"cab": {"es": ["Agente", "Defectos"], "en": ["Agent", "Defects"]},
                         "filas": {i: [[FAM[sigla]["agentes"].get(k, ("Ninguno" if f(i) else "None") if k == "—" else k), num(v, i)] for k, v in ag.most_common()] for i in L}}})

    # 9 · consumo y próximo paso
    tot = T["tokens"] + T["repetidos"]
    S.append({"id": "consumo", "titulo": {"es": "Consumo y próximo paso", "en": "Cost and next step"}, "parrafos": {i: [
        (f"Las {len(rondas)} rondas usaron {dec(tot / 1e6, i)} millones de tokens: {dec(T['tokens'] / 1e6, i)} millones en las corridas calificadas y "
         f"{dec(T['repetidos'] / 1e6, i)} en las que se repitieron después de corregir un defecto. En promedio, {dec(T['tokens'] / 1e6 / T['corridas'], i)} millones por entidad."
         if f(i) else
         f"The {len(rondas)} rounds used {dec(tot / 1e6, i)} million tokens: {dec(T['tokens'] / 1e6, i)} million in the graded runs and "
         f"{dec(T['repetidos'] / 1e6, i)} in the ones repeated after fixing a defect. On average, {dec(T['tokens'] / 1e6 / T['corridas'], i)} million per entity."),
        ("El material es sintético. El próximo paso es el despliegue en una organización, con su propia documentación."
         if f(i) else "The material is synthetic. The next step is deployment in an organisation, with its own documentation."),
    ] for i in L}})

    meta = {"generado_desde": f"tests/evidencias/familias/{sigla}", "ultima_ronda": U, "completa": completa, "rondas": rondas}
    graf = {"evolucion": [{"n": n, "cobertura": pct_valor(suma(por[n])["acertadas"], suma(por[n])["esperadas"]),
                           "precision": pct_valor(*prec(suma(por[n]))), "extraccion": pct_valor(suma(por[n])["bien"], suma(por[n])["campos"])} for n in rondas],
            "defectos": [{"n": n, "defectos": dpr.get(n, 0)} for n in rondas]}
    return meta, S, graf


# ── los archivos ─────────────────────────────────────────────────────────

def markdown(sigla, meta, S, idioma):
    es = idioma == "es"
    otro = "ANALISIS.md" if es else "ANALISIS.es.md"
    t = FAM[sigla]["titulo"][0 if es else 1]
    ev = meta["generado_desde"]
    out = ["# " + (f"Análisis estadístico de las pruebas · {t}" if es else f"Statistical analysis of the tests · {t}"), "",
           (f"Generado por `scripts/analisis_familias.py` desde `{ev}/` · ronda {'completa ' if meta.get('completa', True) else ''}más reciente: {meta['ultima_ronda']} · [English]({otro})" if es else
            f"Generated by `scripts/analisis_familias.py` from `{ev}/` · most recent {'complete ' if meta.get('completa', True) else ''}round: {meta['ultima_ronda']} · [Español]({otro})"), "",
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
                out += [A.tabla_md(s[k]["cab"][idioma], s[k]["filas"][idioma]), ""]
    out += ["---", "", (f"La evidencia completa de cada ronda: [`{ev}/`]({REPO}/tree/main/{ev})." if es else
                       f"The full evidence of every round: [`{ev}/`]({REPO}/tree/main/{ev})."), ""]
    return "\n".join(out)


def archivos(sigla):
    meta, S, graf = secciones(sigla)
    salida = {"analisis.json": json.dumps({"meta": meta, "secciones": S}, ensure_ascii=False, indent=1) + "\n",
              "ANALISIS.es.md": markdown(sigla, meta, S, "es"), "ANALISIS.md": markdown(sigla, meta, S, "en")}
    tit = {"es": "Evolución por ronda", "en": "Round by round"}
    sub = {"es": "Porcentaje en las entidades de cada ronda, contra la clave", "en": "Percentage across each round's entities, against the key"}
    for i in L:
        salida[f"evolucion-{i}.svg"] = A.svg_evolucion(graf["evolucion"], i, SERIES, tit, sub)
        salida[f"defectos-{i}.svg"] = A.svg_defectos(graf["defectos"], i, lambda n: {"es": f"{n} en total, por la ronda en que se encontraron", "en": f"{n} in total, by the round they were found in"})
    return salida


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    malos = []
    for sigla in FAM:
        dest = RAIZ / "families" / f"criterio-{sigla}" / "analisis"
        dest.mkdir(parents=True, exist_ok=True)
        for nombre, contenido in archivos(sigla).items():
            ruta = dest / nombre
            igual = ruta.is_file() and ruta.read_text(encoding="utf-8") == contenido
            if a.check and not igual:
                malos.append(f"criterio-{sigla}/{nombre}")
            elif not a.check and not igual:
                ruta.write_text(contenido, encoding="utf-8")
                print(f"  {ruta.relative_to(RAIZ)}")
    for m in malos:
        print(f"  ✗ {m} no es el que sale de la evidencia: corre python3 scripts/analisis_familias.py")
    if a.check and not malos:
        print("  el análisis de la CFO y la CLO es el que sale de la evidencia")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
