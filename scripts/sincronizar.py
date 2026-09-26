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
# de un proyecto no es el del portafolio recortado, y Rostrum es de la PMO.
SCRIPTS = {
    "criterio-pm": {
        "pmo.py": "la aritmética; `compute` ya trabaja proyecto a proyecto",
        "texto.py": "leer un .docx es leer un .docx",
    },
    # Alba no calcula plan ni presupuesto —en definición no existen—, pero sí lee las
    # fichas de los proyectos que ejecutan su producto, y el contrato de campo
    # `{value, source, source_date, state}` es el mismo. `producto.py` lo importa de
    # esta copia en vez de reescribirlo: dos definiciones del mismo campo que se
    # separan es la deuda que este proyecto no acepta.
    "criterio-product": {
        "pmo.py": "el contrato de campo, y leer la ficha del proyecto que ejecuta el producto",
        "texto.py": "una entrevista llega en .docx tanto como un acta",
    },
}

# Los skills que son método y no rol. Un riesgo es un riesgo lo mire quien lo mire, y
# la ficha es el contrato de datos de la familia entera. Los que quedan fuera lo hacen
# por alcance, no por casualidad: `portfolio-health` y `portfolio-history` solo tienen
# sentido mirando el conjunto, y un gerente de proyecto no mira el conjunto.
SKILLS = {
    "criterio-pm": {
        "project-record": "la ficha: el contrato de datos de toda la familia",
        "document-intake": "qué documento hay que releer y cuál no",
        "commitment-tracking": "la función central de Samuel",
        "raid-taxonomy": "un riesgo es un riesgo lo mire quien lo mire",
        "baseline-variance": "la desviación se calcula igual en un proyecto que en cuarenta",
        "governance-artifacts": "acta, comité, control de cambios y cierre",
        "vendor-control": "contrato contra recibo contra facturación",
        "project-diagnosis": "el diagnóstico desde cero de un proyecto",
    },
    # Lo que Alba comparte es la costura con el resto de la familia: la ficha que nace
    # con el acta, el acta misma, qué documento hay que releer, y la taxonomía a la que
    # se muda un supuesto el día que nadie lo verifica.
    "criterio-product": {
        "project-record": "la ficha nace con el acta, y Alba es quien la crea",
        "document-intake": "una entrevista es un documento, y también envejece",
        "governance-artifacts": "el acta de constitución es la costura con el agente de proyecto",
        "raid-taxonomy": "un supuesto que nadie verifica se vuelve un riesgo, y ahí se registra",
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


# En markdown la marca va como comentario HTML: no se ve al leer el skill, se ve al
# abrirlo para editarlo, que es exactamente cuando hace falta.
MARCA_MD = ("<!-- COPIA · la fuente es plugins/criterio-pmo/skills/{nombre}/. "
            "La escribe scripts/sincronizar.py y no se edita aquí. -->\n")


def con_cabecera(texto: str, nombre: str) -> str:
    """La cabecera va después del shebang, si lo hay, para no romper el ejecutable."""
    marca = CABECERA.format(nombre=nombre)
    if texto.startswith("#!"):
        primera, _, resto = texto.partition("\n")
        return f"{primera}\n{marca}{resto}"
    return marca + texto


def con_marca_md(texto: str, nombre: str) -> str:
    """Después del frontmatter, que tiene que seguir siendo lo primero del archivo."""
    marca = MARCA_MD.format(nombre=nombre)
    if texto.startswith("---\n"):
        fin = texto.find("\n---\n", 4)
        if fin != -1:
            corte = fin + len("\n---\n")
            return texto[:corte] + marca + texto[corte:]
    return marca + texto


def _comparar(copia: Path, esperado: str, etiqueta: str, porque: str,
              escribir: bool, modo: int, estado: dict) -> None:
    actual = copia.read_text(encoding="utf-8") if copia.exists() else None
    if actual == esperado:
        estado["iguales"] += 1
        print(f"  igual   {etiqueta}   · {porque}")
        return
    if not escribir:
        falta = "no existe" if actual is None else "difiere de la fuente"
        estado["problemas"].append(f"{etiqueta} {falta}")
        return
    copia.parent.mkdir(parents=True, exist_ok=True)
    copia.write_text(esperado, encoding="utf-8")
    copia.chmod(modo)
    estado["tocados"].append(etiqueta)
    print(f"  copiado {etiqueta}   · {porque}")


def revisar(escribir: bool) -> int:
    estado = {"problemas": [], "tocados": [], "iguales": 0}

    for plugin, archivos in sorted(SCRIPTS.items()):
        for nombre, porque in sorted(archivos.items()):
            origen = FUENTE / nombre
            if not origen.exists():
                estado["problemas"].append(f"falta la fuente {origen.relative_to(RAIZ)}")
                continue
            _comparar(RAIZ / "plugins" / plugin / "scripts" / nombre,
                      con_cabecera(origen.read_text(encoding="utf-8"), nombre),
                      f"{plugin}/scripts/{nombre}", porque, escribir,
                      origen.stat().st_mode, estado)

    for plugin, skills in sorted(SKILLS.items()):
        for nombre, porque in sorted(skills.items()):
            carpeta = FUENTE.parent / "skills" / nombre
            if not carpeta.is_dir():
                estado["problemas"].append(f"falta el skill fuente {nombre}")
                continue
            # Un skill es una carpeta: SKILL.md y lo que cuelgue de él. Se copia entero,
            # porque media copia es peor que ninguna.
            for origen in sorted(x for x in carpeta.rglob("*") if x.is_file()):
                rel = origen.relative_to(carpeta)
                texto = origen.read_text(encoding="utf-8")
                if origen.name == "SKILL.md":
                    texto = con_marca_md(texto, nombre)
                _comparar(RAIZ / "plugins" / plugin / "skills" / nombre / rel, texto,
                          f"{plugin}/skills/{nombre}/{rel}", porque, escribir,
                          origen.stat().st_mode, estado)

    if estado["problemas"]:
        print()
        for x in estado["problemas"]:
            print(f"  FALLA  {x}")
        print("\nCorre  python3 scripts/sincronizar.py  para ponerlas al día.")
        return 1
    n = len(estado["tocados"])
    print(f"\n{estado['iguales']} al día" + (f", {n} actualizadas" if n else ""))
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
