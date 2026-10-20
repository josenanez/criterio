#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La hoja de ruta de la familia PMO, en los README.

    python3 scripts/hoja.py           escribe la sección en los dos README de la familia
    python3 scripts/hoja.py --check   falla si el README o la fuente no cuadran

La fuente es una sola: families/criterio-pmo/hoja-de-ruta.json. La lee este script y la lee
el portal. Una versión dice «liberada» solo si está en registro/versiones.json, y una
versión registrada no puede seguir diciendo otra cosa. Las industrias de cada incremento se
nombran por su id: su nombre y lo que traen son de industrias.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FAMILIA = RAIZ / "families" / "criterio-pmo"
FUENTE = FAMILIA / "hoja-de-ruta.json"
INDUSTRIAS = FAMILIA / "industrias.json"
REGISTRO = RAIZ / "registro" / "versiones.json"
INICIO = "<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->"
FIN = "<!-- /hoja de ruta -->"
ESTADOS = ("liberada", "en curso", "siguiente", "reservada")

TEXTO = {
    "es": {"archivo": FAMILIA / "README.es.md", "titulo": "## Hoja de ruta", "antes": "## Los dieciocho skills de la familia",
           "lead": "La familia crece por incrementos. Cada uno es una versión con su prueba completa y su análisis "
                   "estadístico publicados, con las mismas métricas, para que la evolución se pueda comparar.",
           "cab": "| Versión | Estado | Qué entra | Prueba |",
           "estado": {"liberada": "Liberada", "en curso": "En curso", "siguiente": "Siguiente", "reservada": "Reservada"}},
    "en": {"archivo": FAMILIA / "README.md", "titulo": "## Roadmap", "antes": "## The family's eighteen skills",
           "lead": "The family grows in increments. Each one is a version with its full test and its statistical "
                   "analysis published, with the same metrics, so the evolution can be compared.",
           "cab": "| Version | Status | What goes in | Test |",
           "estado": {"liberada": "Released", "en curso": "In progress", "siguiente": "Next", "reservada": "Reserved"}},
}


def clave(v: str) -> tuple:
    return tuple(int(x) for x in v.split("."))


def errores_de(h: dict, ind: dict, registradas: set) -> list:
    e = []
    vs = [i["version"] for i in h["incrementos"]]
    if vs != sorted(vs, key=clave):
        e.append("los incrementos no van en orden de versión")
    if len(set(vs)) != len(vs):
        e.append("una versión aparece dos veces")
    if sum(1 for i in h["incrementos"] if i["estado"] == "en curso") > 1:
        e.append("hay más de un incremento en curso")
    ids = {i["id"]: i for i in ind["industrias"]}
    usadas = []
    for i in h["incrementos"]:
        if i["estado"] not in ESTADOS:
            e.append(f"{i['version']}: estado desconocido «{i['estado']}»")
        if (i["estado"] == "liberada") != (i["version"] in registradas):
            e.append(f"{i['version']}: dice «{i['estado']}» y {'está' if i['version'] in registradas else 'no está'} en el registro de versiones")
        for idioma in ("es", "en"):
            t = i.get(idioma) or {}
            if not (t.get("titulo") and t.get("entra") and t.get("prueba")):
                e.append(f"{i['version']}: le falta el texto en {idioma}")
        for x in i["industrias"]:
            if x not in ids:
                e.append(f"{i['version']}: la industria «{x}» no está en industrias.json")
            usadas.append(x)
    for x, i in ids.items():
        if i["estado"] == "siguiente" and usadas.count(x) != 1:
            e.append(f"la industria siguiente «{x}» tiene que estar en un solo incremento de la hoja de ruta")
    return e


def seccion(h: dict, ind: dict, idioma: str) -> str:
    t = TEXTO[idioma]
    filas = []
    for i in h["incrementos"]:
        tx = i[idioma]
        cuerpo = f"**{tx['titulo']}**" + "".join(f"<br>· {x}" for x in tx["entra"])
        filas.append(f"| {i['version']} | {t['estado'][i['estado']]} | {cuerpo} | {tx['prueba']} |")
    return "\n".join([INICIO, "", t["lead"], "", t["cab"], "|---|---|---|---|", *filas, "", FIN])


def aplicar(texto: str, bloque: str, idioma: str) -> str:
    t = TEXTO[idioma]
    if INICIO in texto:
        a = texto.index(INICIO)
        b = texto.index(FIN, a) + len(FIN)
        return texto[:a] + bloque + texto[b:]
    if t["antes"] not in texto:
        raise SystemExit(f"{t['archivo'].name}: no está «{t['antes']}», donde va la sección")
    return texto.replace(t["antes"], f"{t['titulo']}\n\n{bloque}\n\n{t['antes']}", 1)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    h = json.loads(FUENTE.read_text(encoding="utf-8"))
    ind = json.loads(INDUSTRIAS.read_text(encoding="utf-8"))
    registradas = {v["version"] for v in json.loads(REGISTRO.read_text(encoding="utf-8"))["versiones"]}
    errores = errores_de(h, ind, registradas)
    for idioma, t in TEXTO.items():
        actual = t["archivo"].read_text(encoding="utf-8")
        nuevo = aplicar(actual, seccion(h, ind, idioma), idioma)
        if args.check:
            if INICIO not in actual or nuevo != actual:
                errores.append(f"{t['archivo'].relative_to(RAIZ)}: la hoja de ruta no es la que sale de hoja-de-ruta.json")
        elif nuevo != actual:
            t["archivo"].write_text(nuevo, encoding="utf-8")
            print(f"  {t['archivo'].relative_to(RAIZ)}")
    for e in errores:
        print(f"  ✗ {e}")
    if args.check and not errores:
        print(f"  la hoja de ruta cuadra: {len(h['incrementos'])} incrementos, el registro y las industrias")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
