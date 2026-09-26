#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mantiene iguales los scripts que dos plugins comparten.

    python3 scripts/sincronizar.py            copia y dice qué cambió
    python3 scripts/sincronizar.py --check    no copia; falla si difieren

`criterio-pmo` y `criterio-pm` comparten la aritmética. Dos copias que se separan es
exactamente la deuda que este proyecto no acepta, y la forma de no tenerla **no** es un
módulo compartido: un plugin instalado tiene que correr solo, y un `import` a la ruta
del otro plugin funciona en este repositorio y falla en el equipo de quien lo instaló,
que es el peor sitio para enterarse.

Así que se copia, y la copia se verifica. La fuente vive en `criterio-pmo/scripts/` y
ahí se edita; la copia lleva una cabecera que lo dice, y `--check` falla si alguien la
editó en el sitio equivocado. Lo corre `tests/coherencia.py`, de modo que una copia
separada rompe la misma puerta que todo lo demás.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "plugins" / "criterio-pmo" / "scripts"

# Qué comparte cada plugin, y por qué. Lo que no está aquí no se comparte: el informe
# de un proyecto no es el del portafolio recortado, y Atril es de la PMO.
COMPARTIDOS = {
    "criterio-pm": {
        "pmo.py": "la aritmética; `compute` ya trabaja proyecto a proyecto",
        "texto.py": "leer un .docx es leer un .docx",
    },
}

CABECERA = """# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-pmo/scripts/{nombre}. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
"""


def con_cabecera(texto: str, nombre: str) -> str:
    """La cabecera va después del shebang, si lo hay, para no romper el ejecutable."""
    marca = CABECERA.format(nombre=nombre)
    if texto.startswith("#!"):
        primera, _, resto = texto.partition("\n")
        return f"{primera}\n{marca}{resto}"
    return marca + texto


def revisar(escribir: bool) -> int:
    problemas, tocados, iguales = [], [], 0
    for plugin, archivos in sorted(COMPARTIDOS.items()):
        destino = RAIZ / "plugins" / plugin / "scripts"
        for nombre, porque in sorted(archivos.items()):
            origen = FUENTE / nombre
            if not origen.exists():
                problemas.append(f"falta la fuente {origen.relative_to(RAIZ)}")
                continue
            esperado = con_cabecera(origen.read_text(encoding="utf-8"), nombre)
            copia = destino / nombre
            actual = copia.read_text(encoding="utf-8") if copia.exists() else None

            if actual == esperado:
                iguales += 1
                print(f"  igual   {plugin}/{nombre}   · {porque}")
                continue
            if not escribir:
                falta = "no existe" if actual is None else "difiere de la fuente"
                problemas.append(f"{plugin}/scripts/{nombre} {falta}")
                continue
            destino.mkdir(parents=True, exist_ok=True)
            copia.write_text(esperado, encoding="utf-8")
            copia.chmod(origen.stat().st_mode)
            tocados.append(f"{plugin}/{nombre}")
            print(f"  copiado {plugin}/{nombre}   · {porque}")

    if problemas:
        print()
        for x in problemas:
            print(f"  FALLA  {x}")
        print("\nCorre  python3 scripts/sincronizar.py  para ponerlas al día.")
        return 1
    print(f"\n{iguales} al día" + (f", {len(tocados)} actualizadas" if tocados else ""))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Sincroniza los scripts compartidos.")
    ap.add_argument("--check", action="store_true",
                    help="no copia; falla si alguna difiere")
    args = ap.parse_args()
    print("Scripts compartidos" + (" · solo verificación" if args.check else ""))
    return revisar(escribir=not args.check)


if __name__ == "__main__":
    sys.exit(main())
