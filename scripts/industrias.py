#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las industrias de prueba de la familia, en el README.

    python3 scripts/industrias.py           escribe la sección en los dos README
    python3 scripts/industrias.py --check   falla si el README o la fuente no cuadran

La fuente es una sola: families/criterio-pmo/industrias.json. La lee este script y la
lee el portal. Una industria dice «probada» solo si tiene perfil en
tests/sintetico/sectores.py y corrió en la última ronda; una industria con perfil que no
diga «probada» también falla. Las rondas y los proyectos no se escriben a mano: salen de
tests/evidencias/rondas/.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FAMILIA = RAIZ / "families" / "criterio-pmo"
FUENTE = FAMILIA / "industrias.json"
RONDAS = RAIZ / "tests" / "evidencias" / "rondas"
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import sectores  # noqa: E402

INICIO = "<!-- industrias: generado por scripts/industrias.py desde industrias.json; no se edita a mano -->"
FIN = "<!-- /industrias -->"

TEXTO = {
    "es": {"archivo": "README.es.md", "antes": "## Los dieciocho skills de la familia",
           "titulo": "## Las industrias de prueba",
           "lead": "Probada en {n} industrias de Suramérica, con {p} proyectos por industria en la última ronda. "
                   "Las siguientes entran de dos en dos, cada una con su versión y su ronda completa.",
           "cab": "| Industria | Estado | Qué trae a las pruebas |",
           "probada": "Probada · rondas {r}", "siguiente": "Incremento {i} · versión {v}"},
    "en": {"archivo": "README.md", "antes": "## The family's eighteen skills",
           "titulo": "## The test industries",
           "lead": "Tested in {n} South American industries, with {p} projects per industry in the latest round. "
                   "The next ones come in two at a time, each with its own version and full round.",
           "cab": "| Industry | Status | What it brings to the tests |",
           "probada": "Tested · rounds {r}", "siguiente": "Increment {i} · version {v}"},
}


def rondas() -> list[tuple[int, dict]]:
    salida = []
    for d in RONDAS.glob("ronda-*"):
        m = re.fullmatch(r"ronda-(\d+)", d.name)
        if m and (d / "resumen.json").exists():
            salida.append((int(m.group(1)), json.loads((d / "resumen.json").read_text(encoding="utf-8"))))
    return sorted(salida, key=lambda x: x[0])


def tramo(numeros: list[int]) -> str:
    """1, 2, 3, 5 → «1–3, 5»."""
    partes, ini, ant = [], None, None
    for n in sorted(numeros):
        if ini is None:
            ini = ant = n
        elif n == ant + 1:
            ant = n
        else:
            partes.append(f"{ini}–{ant}" if ant != ini else str(ini))
            ini = ant = n
    if ini is not None:
        partes.append(f"{ini}–{ant}" if ant != ini else str(ini))
    return ", ".join(partes)


def validar(fuente: dict, hist: list[tuple[int, dict]]) -> list[str]:
    errores = []
    ids = [i["id"] for i in fuente["industrias"]]
    if len(ids) != len(set(ids)):
        errores.append("industrias.json repite un id")
    probadas = {i["id"] for i in fuente["industrias"] if i["estado"] == "probada"}
    perfiles = set(sectores.PERFILES)
    for falta in sorted(perfiles - probadas):
        errores.append(f"{falta} tiene perfil en sectores.py y no figura como probada")
    for sobra in sorted(probadas - perfiles):
        errores.append(f"{sobra} dice «probada» y no tiene perfil en sectores.py")
    if hist:
        ultima = {x["entorno"] for x in hist[-1][1]["industrias"]}
        for i in sorted(probadas - ultima):
            errores.append(f"{i} dice «probada» y no corrió en la ronda {hist[-1][0]}")
    for i in fuente["industrias"]:
        if i["estado"] not in ("probada", "siguiente"):
            errores.append(f"{i['id']}: estado desconocido «{i['estado']}»")
        if i["estado"] == "siguiente" and not (i.get("incremento") and i.get("version")):
            errores.append(f"{i['id']}: una industria siguiente lleva incremento y versión")
        for idioma in ("es", "en"):
            if not (i.get(idioma, {}).get("nombre") and i[idioma].get("trae")):
                errores.append(f"{i['id']}: le falta el texto en {idioma}")
    return errores


def seccion(fuente: dict, hist: list[tuple[int, dict]], idioma: str) -> str:
    t = TEXTO[idioma]
    ultima = hist[-1][1]["industrias"] if hist else []
    proyectos = sorted({x["proyectos"] for x in ultima})
    p = proyectos[0] if len(proyectos) == 1 else f"{proyectos[0]}–{proyectos[-1]}"
    probadas = [i for i in fuente["industrias"] if i["estado"] == "probada"]
    filas = []
    for i in fuente["industrias"]:
        if i["estado"] == "probada":
            r = tramo([n for n, d in hist if any(x["entorno"] == i["id"] for x in d["industrias"])])
            estado = t["probada"].format(r=r)
        else:
            estado = t["siguiente"].format(i=i["incremento"], v=i["version"])
        filas.append(f"| {i[idioma]['nombre']} | {estado} | {i[idioma]['trae']} |")
    return "\n".join([INICIO, "", t["lead"].format(n=len(probadas), p=p), "", t["cab"], "|---|---|---|",
                      *filas, "", FIN])


def aplicar(texto: str, bloque: str, idioma: str) -> str:
    t = TEXTO[idioma]
    if INICIO in texto:
        a = texto.index(INICIO)
        b = texto.index(FIN, a) + len(FIN)
        return texto[:a] + bloque + texto[b:]
    if t["antes"] not in texto:
        raise SystemExit(f"{t['archivo']}: no está «{t['antes']}», donde va la sección")
    return texto.replace(t["antes"], f"{t['titulo']}\n\n{bloque}\n\n{t['antes']}", 1)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    fuente = json.loads(FUENTE.read_text(encoding="utf-8"))
    hist = rondas()
    errores = validar(fuente, hist)
    for idioma, t in TEXTO.items():
        ruta = FAMILIA / t["archivo"]
        actual = ruta.read_text(encoding="utf-8")
        nuevo = aplicar(actual, seccion(fuente, hist, idioma), idioma)
        if args.check:
            if INICIO not in actual or nuevo != actual:
                errores.append(f"{t['archivo']}: la sección de industrias no es la que sale de industrias.json")
        elif nuevo != actual:
            ruta.write_text(nuevo, encoding="utf-8")
            print(f"  {ruta.relative_to(RAIZ)}")
    for e in errores:
        print(f"  ✗ {e}")
    if not errores and args.check:
        print(f"  {len(fuente['industrias'])} industrias, la fuente y los dos README cuadran")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
