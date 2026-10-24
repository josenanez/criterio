#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Que cada script de un plugin corra con el Python que trae el equipo de quien lo instala.

    python3 scripts/compatibilidad.py --check

Un plugin instalado corre con el `python3` del equipo, y en un Mac ese puede ser el 3.9 del
sistema. Desde el 3.12 una f-string admite saltos de línea y las mismas comillas dentro de sus
llaves (PEP 701); antes, eso es un error de sintaxis. El 23 de octubre de 2026 una f-string partida
en dos líneas pasó todas las puertas, que corren con un Python nuevo, y el informe no abrió en el
Mac de José. Esta puerta lo busca en el texto, sin depender de qué Python la corre.
"""
from __future__ import annotations

import argparse
import io
import subprocess
import sys
import tokenize
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MINIMO = "3.9"


def _triple(texto: str) -> bool:
    cuerpo = texto.lstrip("rRbBfFuU")
    return cuerpo[:3] in ('"""', "'''")


def revisar(ruta: Path) -> list[str]:
    """Las f-strings de una sola comilla que ocupan más de una línea o repiten su comilla dentro."""
    err = []
    toks = list(tokenize.generate_tokens(io.StringIO(ruta.read_text(encoding="utf-8")).readline))
    inicio = getattr(tokenize, "FSTRING_START", None)
    if inicio is None:  # antes del 3.12 el tokenizador ya rechaza estas formas al compilar
        return []
    pila = []
    for t in toks:
        if t.type == tokenize.FSTRING_START:
            pila.append((t, t.string[-1]))
        elif t.type == tokenize.FSTRING_END and pila:
            abre, comilla = pila.pop()
            if not _triple(abre.string) and t.end[0] != abre.start[0]:
                err.append(f"{ruta.relative_to(RAIZ)}:{abre.start[0]}: una f-string de una línea sigue en la línea {t.end[0]}")
        elif pila and t.type in (tokenize.STRING, tokenize.FSTRING_START) and not _triple(pila[-1][0].string):
            if t.string.lstrip("rRbBfFuU")[:1] == pila[-1][1]:
                err.append(f"{ruta.relative_to(RAIZ)}:{t.start[0]}: una cadena dentro de una f-string usa su misma comilla")
    return err


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.parse_args()
    archivos = subprocess.run(["git", "ls-files", "plugins/*.py", "scripts/*.py", "tests/*.py", "docs/*.py"], cwd=RAIZ,
                              capture_output=True, text=True, check=True).stdout.split()
    err = [e for a in archivos for e in revisar(RAIZ / a)]
    for e in err:
        print(f"  ✗ {e}")
    if not err:
        print(f"  {len(archivos)} scripts sin sintaxis que un Python anterior al 3.12 rechace (el mínimo es el {MINIMO})")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
