#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La estructura de carpetas recomendada de la familia PMO, donde la gente la lee.

    python3 scripts/carpetas.py           escribe la sección en los README y en document-intake
    python3 scripts/carpetas.py --check   falla si alguna copia no sale de la fuente

La fuente es una sola: families/criterio-pmo/carpetas.json. La usa el material de prueba
(tests/sintetico/corpus.py) y la recomienda la familia (ADR 0007). Este script la escribe en
los dos README de la familia y en el skill document-intake de los tres plugins, que es lo que
el agente instalado tiene a mano cuando le dice a alguien cómo organizar su carpeta.

Escribe además `scripts/estructura.json` en los tres plugins: la misma estructura en la forma que
usa `raiz.py` para encontrar la carpeta de un proyecto, de un producto o del portafolio por lo que
tiene adentro (ADR 0011). Un proyecto o un producto se reconoce por su código al inicio del nombre.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "families" / "criterio-pmo" / "carpetas.json"
INICIO = "<!-- carpetas: generado por scripts/carpetas.py desde carpetas.json; no se edita a mano -->"
FIN = "<!-- /carpetas -->"

TEXTO = {
    "es": {"titulo": "## La estructura de carpetas recomendada",
           "lead": "Recomendada, no obligatoria: los agentes procesan la carpeta como esté, y las pruebas lo "
                   "comprueban con cuatro disposiciones distintas. Con esta estructura cada documento llega a "
                   "su lugar sin que el agente tenga que deducirlo.",
           "proyecto": "**Cada proyecto**", "producto": "**Cada producto**",
           "cab": "| Carpeta | Qué va |"},
    "en": {"titulo": "## The recommended folder structure",
           "lead": "Recommended, not required: the agents process the folder as it is, and the tests check it with "
                   "four different layouts. With this structure every document lands in its place without the "
                   "agent having to work it out.",
           "proyecto": "**Each project**", "producto": "**Each product**",
           "cab": "| Folder | What goes in it |"},
}
DESTINOS = [
    (RAIZ / "families" / "criterio-pmo" / "README.es.md", "es", "## Instalación de la familia"),
    (RAIZ / "families" / "criterio-pmo" / "README.md", "en", "## Installing the family"),
    (RAIZ / "plugins" / "criterio-portfolio" / "skills" / "document-intake" / "SKILL.md", "es", "## Formatos"),
    (RAIZ / "plugins" / "criterio-project" / "skills" / "document-intake" / "SKILL.md", "es", "## Formatos"),
    (RAIZ / "plugins" / "criterio-product" / "skills" / "document-intake" / "SKILL.md", "es", "## Formatos"),
]


def bloque(f: dict, idioma: str) -> str:
    t = TEXTO[idioma]
    lineas = [INICIO, "", t["lead"], "", f["raiz"][idioma], ""]
    for clase in ("proyecto", "producto"):
        lineas += [t[clase], "", t["cab"], "|---|---|"]
        lineas += [f"| `{b['carpeta']}/` | {b[idioma]} |" for b in f[clase]]
        lineas.append("")
    lineas.append(FIN)
    return "\n".join(lineas)


def aplicar(texto: str, bl: str, idioma: str, antes: str, ruta: Path) -> str:
    if INICIO in texto:
        a = texto.index(INICIO)
        b = texto.index(FIN, a) + len(FIN)
        return texto[:a] + bl + texto[b:]
    if antes not in texto:
        raise SystemExit(f"{ruta.relative_to(RAIZ)}: no está «{antes}», donde va la sección")
    return texto.replace(antes, f"{TEXTO[idioma]['titulo']}\n\n{bl}\n\n{antes}", 1)


CODIGO = r"[A-Z]{2,5}-\d{2,}[^/]*"
PLUGINS_PMO = ("criterio-portfolio", "criterio-project", "criterio-product")


def estructura_json(f: dict) -> str:
    d = {"generado": "por scripts/carpetas.py desde families/criterio-pmo/carpetas.json; no se edita a mano",
         "niveles": [{"id": clase, "ruta": CODIGO, "profundidad": 1, "etiqueta": "<código>/",
                      "carpetas": [{"carpeta": b["carpeta"], "patrones": []} for b in f[clase]]}
                     for clase in ("proyecto", "producto")]}
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    f = json.loads(FUENTE.read_text(encoding="utf-8"))
    errores = []
    for clase in ("proyecto", "producto"):
        nombres = [b["carpeta"] for b in f[clase]]
        if nombres != sorted(nombres):
            errores.append(f"{clase}: las carpetas no van en el orden de su prefijo")
        for b in f[clase]:
            if not (b.get("es") and b.get("en")):
                errores.append(f"{b['carpeta']}: le falta el texto en un idioma")
    for ruta, idioma, antes in DESTINOS:
        actual = ruta.read_text(encoding="utf-8")
        nuevo = aplicar(actual, bloque(f, idioma), idioma, antes, ruta)
        if args.check:
            if INICIO not in actual or nuevo != actual:
                errores.append(f"{ruta.relative_to(RAIZ)}: la estructura no es la que sale de carpetas.json")
        elif nuevo != actual:
            ruta.write_text(nuevo, encoding="utf-8")
            print(f"  {ruta.relative_to(RAIZ)}")
    for plug in PLUGINS_PMO:
        ruta = RAIZ / "plugins" / plug / "scripts" / "estructura.json"
        nuevo = estructura_json(f)
        actual = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
        if actual != nuevo:
            if args.check:
                errores.append(f"{ruta.relative_to(RAIZ)}: no sale de carpetas.json")
            else:
                ruta.write_text(nuevo, encoding="utf-8")
                print(f"  {ruta.relative_to(RAIZ)}")
    for e in errores:
        print(f"  ✗ {e}")
    if args.check and not errores:
        print(f"  la estructura y sus {len(DESTINOS)} copias cuadran")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
