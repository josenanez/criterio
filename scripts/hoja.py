#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La hoja de ruta de cada familia, en su documentación.

    python3 scripts/hoja.py           escribe la sección en los dos README de cada familia y la hoja de
                                      ruta completa, docs/hoja-de-ruta.es.md y docs/hoja-de-ruta.md
    python3 scripts/hoja.py --check   falla si un documento o una fuente no cuadran

La fuente es una por familia: families/criterio-<sigla>/hoja-de-ruta.json. La lee este script y
la lee el portal. Una versión dice «liberada» solo si está en registro/versiones.json, y una
versión registrada no puede seguir diciendo otra cosa. Un incremento puede no tener versión
todavía: la lleva cuando entra en una. Las industrias de cada incremento se nombran por su id:
su nombre y lo que traen son de industrias.json, que hoy solo tiene la PMO.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REGISTRO = RAIZ / "registro" / "versiones.json"
INICIO = "<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->"
FIN = "<!-- /hoja de ruta -->"
ESTADOS = ("liberada", "en curso", "siguiente", "reservada")

LEAD = {"es": "La familia crece por incrementos. Cada uno es una versión con su prueba completa y su análisis "
              "estadístico publicados, con las mismas métricas, para que la evolución se pueda comparar.",
        "en": "The family grows in increments. Each one is a version with its full test and its statistical "
              "analysis published, with the same metrics, so the evolution can be compared."}
CAB = {"es": "| Versión | Estado | Qué entra | Prueba |", "en": "| Version | Status | What goes in | Test |"}
ESTADO = {"es": {"liberada": "Liberada", "en curso": "En curso", "siguiente": "Siguiente", "reservada": "Reservada"},
          "en": {"liberada": "Released", "en curso": "In progress", "siguiente": "Next", "reservada": "Reserved"}}
SIN_VERSION = {"es": "Incremento {n}", "en": "Increment {n}"}


def _familia(sigla: str, docs: dict) -> dict:
    d = RAIZ / "families" / f"criterio-{sigla}"
    return {"sigla": sigla, "fuente": d / "hoja-de-ruta.json", "industrias": d / "industrias.json",
            "docs": {i: {"archivo": d / a, "titulo": t, "antes": antes} for i, (a, t, antes) in docs.items()}}


FAMILIAS = [
    _familia("pmo", {"es": ("README.es.md", "## Hoja de ruta", "## Los dieciocho skills de la familia"),
                     "en": ("README.md", "## Roadmap", "## The family's eighteen skills")}),
    _familia("cfo", {"es": ("README.es.md", "## Hoja de ruta", "## Los doce skills de la familia"),
                     "en": ("README.md", "## Roadmap", "## The family's twelve skills")}),
    _familia("clo", {"es": ("README.es.md", "## Hoja de ruta", "## Los diez skills de la familia"),
                     "en": ("README.md", "## Roadmap", "## The family's ten skills")}),
    _familia("ea", {"es": ("README.es.md", "## Hoja de ruta", "## Los seis skills de la familia"),
                    "en": ("README.md", "## Roadmap", "## The family's six skills")}),
    _familia("cso", {"es": ("README.es.md", "## Hoja de ruta", "## Los ocho skills de la familia"),
                     "en": ("README.md", "## Roadmap", "## The family's eight skills")}),
]


def clave(v: str) -> tuple:
    return tuple(int(x) for x in v.split("."))


def nombre(i: dict) -> str:
    return i["version"] or f"incremento {i['incremento']}"


def errores_de(h: dict, ind: dict, registradas: set) -> list:
    e = []
    vs = [i["version"] for i in h["incrementos"] if i["version"]]
    if vs != sorted(vs, key=clave):
        e.append("los incrementos no van en orden de versión")
    if len(set(vs)) != len(vs):
        e.append("una versión aparece dos veces")
    ns = [i["incremento"] for i in h["incrementos"] if i.get("incremento") is not None]
    if ns != sorted(ns) or len(set(ns)) != len(ns):
        e.append("los incrementos no van en orden o uno se repite")
    if sum(1 for i in h["incrementos"] if i["estado"] == "en curso") > 1:
        e.append("hay más de un incremento en curso")
    ids = {i["id"]: i for i in ind["industrias"]}
    usadas = []
    for i in h["incrementos"]:
        if i["estado"] not in ESTADOS:
            e.append(f"{nombre(i)}: estado desconocido «{i['estado']}»")
        if (i["estado"] == "liberada") != (i["version"] in registradas):
            e.append(f"{nombre(i)}: dice «{i['estado']}» y {'está' if i['version'] in registradas else 'no está'} en el registro de versiones")
        for idioma in ("es", "en"):
            t = i.get(idioma) or {}
            if not (t.get("titulo") and t.get("entra") and t.get("prueba")):
                e.append(f"{nombre(i)}: le falta el texto en {idioma}")
        for x in i["industrias"]:
            if x not in ids:
                e.append(f"{nombre(i)}: la industria «{x}» no está en industrias.json")
            usadas.append(x)
    for x, i in ids.items():
        if i["estado"] == "siguiente" and usadas.count(x) != 1:
            e.append(f"la industria siguiente «{x}» tiene que estar en un solo incremento de la hoja de ruta")
    return e


def seccion(h: dict, idioma: str) -> str:
    filas = []
    for i in h["incrementos"]:
        tx = i[idioma]
        cuerpo = f"**{tx['titulo']}**" + "".join(f"<br>· {x}" for x in tx["entra"])
        v = i["version"] or SIN_VERSION[idioma].format(n=i["incremento"])
        filas.append(f"| {v} | {ESTADO[idioma][i['estado']]} | {cuerpo} | {tx['prueba']} |")
    return "\n".join([INICIO, "", LEAD[idioma], "", CAB[idioma], "|---|---|---|---|", *filas, "", FIN])


def aplicar(texto: str, bloque: str, doc: dict) -> str:
    if INICIO in texto:
        a = texto.index(INICIO)
        b = texto.index(FIN, a) + len(FIN)
        return texto[:a] + bloque + texto[b:]
    if doc["antes"] not in texto:
        raise SystemExit(f"{doc['archivo'].relative_to(RAIZ)}: no está «{doc['antes']}», donde va la sección")
    return texto.replace(doc["antes"], f"{doc['titulo']}\n\n{bloque}\n\n{doc['antes']}", 1)


# ---------------------------------------------------------------- la hoja de ruta completa

def CALIDAD(sigla: str) -> dict:
    """La etiqueta de cada familia, de scripts/calidad.py: sale de la evidencia de sus rondas."""
    sys.path.insert(0, str(RAIZ / "scripts"))
    import calidad
    return calidad.calidad(sigla)


COMPLETA = {"es": RAIZ / "docs" / "hoja-de-ruta.es.md", "en": RAIZ / "docs" / "hoja-de-ruta.md"}
T = {
    "es": {"titulo": "# La hoja de ruta de Criterio", "otro": "[English](hoja-de-ruta.md)",
           "intro": ("Todas las familias en un solo documento. Se genera con `scripts/hoja.py` desde la hoja de ruta de "
                     "cada familia (`families/criterio-<sigla>/hoja-de-ruta.json`), el registro de versiones "
                     "(`registro/versiones.json`) y las decisiones de alcance (`docs/decisions/`): no se edita a mano."),
           "reglas": ["**Cada familia lleva su propia versión** (decisión 0017) y sube solo cuando ella cambia.",
                      "**Diez versiones por entero** (decisión 0020): de x.0 a x.9, y después la x+1.0. La 0.10, la 0.11 "
                      "y la 0.12 son las únicas excepciones: quien está ahí sube a la 1.0.",
                      "**Laboratorio o estable lo dice la evidencia, no el número:** estable, si la corrida más reciente "
                      "de cada entidad del material tiene el piso del margen del 95 % en 95 % o más, en señales y en datos, "
                      "y ningún control levanta una señal; si no, laboratorio. Lo calcula `scripts/calidad.py`.",
                      "**Un incremento es una versión con su prueba completa** y su análisis estadístico, con las mismas "
                      "métricas que las anteriores."],
           "resumen": "## Dónde está cada familia hoy",
           "cab": "| Familia | Agentes | Versión | Calidad | Lo siguiente |", "sep": "|---|---|---|---|---|",
           "sinSigue": "—", "porFamilia": "## Cada familia, incremento por incremento",
           "vienen": "## Las familias que vienen",
           "vienenLead": "Cada una entra con su decisión de alcance: aceptada, se diseña; propuesta, espera su turno, sin fecha.",
           "cabV": "| Decisión | Familia | Estado |", "rostrum": "Rostrum · el portal de todas las familias", "construccion": "En construcción",
           "estadoADR": {"propuesta": "Propuesta", "aceptada": "Aceptada"},
           "calidad": {"estable": "Estable", "laboratorio": "Laboratorio"}},
    "en": {"titulo": "# Criterio's roadmap", "otro": "[Español](hoja-de-ruta.es.md)",
           "intro": ("Every family in one document. It is generated by `scripts/hoja.py` from each family's roadmap "
                     "(`families/criterio-<sigla>/hoja-de-ruta.json`), the version register (`registro/versiones.json`) "
                     "and the scope decisions (`docs/decisions/`): it is not edited by hand."),
           "reglas": ["**Each family carries its own version** (decision 0017) and only goes up when it changes.",
                      "**Ten versions per whole number** (decision 0020): from x.0 to x.9, and then x+1.0. 0.10, 0.11 and "
                      "0.12 are the only exceptions: whoever is there goes up to 1.0.",
                      "**Laboratory or stable is said by the evidence, not the number:** stable if each entity's most "
                      "recent run in the material has the floor of the 95% margin at 95% or more, for signals and data, "
                      "and no control raises a signal; otherwise laboratory. `scripts/calidad.py` calculates it.",
                      "**An increment is a version with its full test** and its statistical analysis, with the same "
                      "metrics as the earlier ones."],
           "resumen": "## Where each family is today",
           "cab": "| Family | Agents | Version | Quality | Next |", "sep": "|---|---|---|---|---|",
           "sinSigue": "—", "porFamilia": "## Each family, increment by increment",
           "vienen": "## The families to come",
           "vienenLead": "Each one comes in with its scope decision: accepted, it is being designed; proposed, it waits its turn, with no date.",
           "cabV": "| Decision | Family | Status |", "rostrum": "Rostrum · the portal for every family", "construccion": "In construction",
           "estadoADR": {"propuesta": "Proposed", "aceptada": "Accepted"},
           "calidad": {"estable": "Stable", "laboratorio": "Laboratory"}},
}


def completa(idioma: str, entradas: list) -> str:
    t = T[idioma]
    ultima = entradas[-1]
    filas, secciones = [], []
    for f in FAMILIAS:
        if not f["fuente"].is_file():
            continue
        fam = json.loads((RAIZ / "families" / f"criterio-{f['sigla']}" / "familia.json").read_text(encoding="utf-8"))
        h = json.loads(f["fuente"].read_text(encoding="utf-8"))
        nombre = f"Criterio {f['sigla'].upper()} · {fam['nombre'][idioma]}"
        agentes = ", ".join(a["nombre"] for a in fam["agentes"])
        liberadas = [i for i in h["incrementos"] if i["estado"] == "liberada"]
        sigue = next((i for i in h["incrementos"] if i["estado"] in ("en curso", "siguiente")), None)
        sig = (f"{sigue['version'] or SIN_VERSION[idioma].format(n=sigue['incremento'])} · {sigue[idioma]['titulo']}"
               if sigue else t["sinSigue"])
        # Una familia que todavía no se libera no tiene versión: está en construcción.
        version = (ultima["familias"].get(f["sigla"], t["construccion"]) if "familias" in ultima
                   else ultima["version"])
        filas.append(f"| {nombre} | {agentes} | {version} | {t['calidad'][CALIDAD(f['sigla'])['etiqueta']]} | {sig} |")
        tabla = seccion(h, idioma).split("\n")[4:-2]          # sin los marcadores ni el texto de entrada
        secciones += [f"### {nombre}", "", *tabla, ""]
    rost = ultima.get("familias", {}).get("rostrum", ultima["version"])
    filas.append(f"| {t['rostrum']} | — | {rost} | — | {t['sinSigue']} |")
    vienen = []
    for d in sorted((RAIZ / "docs" / "decisions").glob("*-scope-*.md")):
        texto = d.read_text(encoding="utf-8")
        estado = (re.search(r"\*\*Estado:\*\* (\w+)", texto) or [None, ""])[1]
        cab = texto.splitlines()[0].lstrip("# ")
        num, _, resto = cab.partition(" · ")
        m = re.search(r" a (.+ \((\w+)\))$", resto)      # «…: el alcance se amplía a datos (CDO)»
        # Una familia que viene: su alcance está propuesto o aceptado, y todavía no tiene su carpeta.
        if estado not in ("propuesta", "aceptada") or not m or (RAIZ / "families" / f"criterio-{m.group(2).lower()}").is_dir():
            continue
        familia = m.group(1)[0].upper() + m.group(1)[1:]
        vienen.append(f"| [{num}](decisions/{d.name}) | {familia} | {t['estadoADR'].get(estado, estado)} |")
    partes = [t["titulo"], "", t["otro"], "", t["intro"], "", *[f"- {r}" for r in t["reglas"]], "",
              t["resumen"], "", t["cab"], t["sep"], *filas, "", t["porFamilia"], "", *secciones]
    if vienen:
        partes += [t["vienen"], "", t["vienenLead"], "", t["cabV"], "|---|---|---|", *vienen, ""]
    return "\n".join(partes).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    entradas = json.loads(REGISTRO.read_text(encoding="utf-8"))["versiones"]
    errores, resumen = [], []
    for f in FAMILIAS:
        if not f["fuente"].is_file():
            continue
        # Las versiones de esta familia en el registro: cada familia lleva la suya (decisión 0017);
        # una entrada anterior a la decisión tiene una sola versión para todas.
        # Una familia que no está en la última entrada todavía no se ha liberado: ninguna versión es suya.
        # Las entradas anteriores a la decisión son de las familias que ya estaban en la primera que
        # anota una versión por familia; una familia que nació después solo tiene las suyas.
        liberada = f["sigla"] in entradas[-1].get("familias", {f["sigla"]: None})
        primera = next((e["familias"] for e in entradas if "familias" in e), {})
        antigua = f["sigla"] in primera
        registradas = ({e["familias"][f["sigla"]] if "familias" in e else e["version"] for e in entradas
                        if ("familias" in e and f["sigla"] in e["familias"]) or ("familias" not in e and antigua)}
                       if liberada else set())
        h = json.loads(f["fuente"].read_text(encoding="utf-8"))
        ind = json.loads(f["industrias"].read_text(encoding="utf-8")) if f["industrias"].is_file() else {"industrias": []}
        errores += [f"{f['sigla'].upper()} · {e}" for e in errores_de(h, ind, registradas)]
        for idioma, doc in f["docs"].items():
            actual = doc["archivo"].read_text(encoding="utf-8")
            nuevo = aplicar(actual, seccion(h, idioma), doc)
            if args.check:
                if INICIO not in actual or nuevo != actual:
                    errores.append(f"{doc['archivo'].relative_to(RAIZ)}: la hoja de ruta no es la que sale de hoja-de-ruta.json")
            elif nuevo != actual:
                doc["archivo"].write_text(nuevo, encoding="utf-8")
                print(f"  {doc['archivo'].relative_to(RAIZ)}")
        resumen.append(f"{f['sigla'].upper()} {len(h['incrementos'])} incrementos")
    for idioma, archivo in COMPLETA.items():
        nuevo = completa(idioma, entradas)
        actual = archivo.read_text(encoding="utf-8") if archivo.is_file() else ""
        if args.check:
            if nuevo != actual:
                errores.append(f"{archivo.relative_to(RAIZ)}: no es la que sale de las hojas de ruta y el registro")
        elif nuevo != actual:
            archivo.write_text(nuevo, encoding="utf-8")
            print(f"  {archivo.relative_to(RAIZ)}")
    for e in errores:
        print(f"  ✗ {e}")
    if args.check and not errores:
        print(f"  la hoja de ruta cuadra: {' · '.join(resumen)}, con el registro y las industrias")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
