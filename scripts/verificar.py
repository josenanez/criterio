#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corre todo lo que verifica este repositorio, y dice qué probó cada cosa.

    python3 scripts/verificar.py            todo
    python3 scripts/verificar.py --rapido    salta la regeneración del material

Existe por una razón concreta: **quien audita esto no debería tener que leer un
README para saber qué correr.** Una puerta es lo que una persona ejecuta; nueve
puertas sueltas es una lista que alguien va a correr a medias.

Todo corre con la librería estándar y sin instalar nada. Si algo aquí necesitara una
dependencia, la propiedad que hace auditable a este repositorio se habría roto.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PMO = RAIZ / "plugins" / "criterio-portfolio" / "scripts"
PM = RAIZ / "plugins" / "criterio-project" / "scripts"
PRODUCT = RAIZ / "plugins" / "criterio-product" / "scripts"

# Cada puerta con lo que prueba. El texto no es decoración: es lo que le dice a quien
# audita por qué esa puerta existe, y es lo primero que se queda viejo si alguien
# cambia lo que la puerta hace sin cambiar lo que dice.
PUERTAS = [
    ("material", [sys.executable, str(RAIZ / "tests/criterio-portfolio/generar.py")],
     "El portafolio sintético: seis proyectos, con un control negativo"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-project/generar.py")],
     "Un proyecto visto desde adentro: dos proyectos, siete minutas"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-product/generar.py")],
     "Lo que hay antes del proyecto: dos productos, con un control negativo"),

    ("material", [sys.executable, str(RAIZ / "tests/sintetico/corpus.py"), "--selftest"],
     "El motor del material: la estructura de referencia y las cuatro disposiciones"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/disposiciones.py")],
     "Que el recorrido encuentre los mismos documentos sin importar cómo estén"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/cobertura.py")],
     "Que ninguna señal se quede sin disparar sin que esté declarado por qué"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/resumen.py")],
     "El resumen de las corridas diarias: precisión, cobertura y qué se movió"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/evidencia.py"), "verificar"],
     "Que el registro de comandos no prometa una evidencia que no está"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/funcionalidades.py"),
                  "--verificar"],
     "Que cada comando declare qué produce y qué deja escrito"),

    ("código", [sys.executable, str(PMO / "portafolio.py"), "selftest"],
     "La aritmética, la cadencia, la cola y el contraste entre las dos fichas"),
    ("código", [sys.executable, str(PMO / "texto.py"), "--selftest"],
     "Leer .docx, .xlsx, .pptx y .eml sin dependencias"),
    ("código", [sys.executable, str(PMO / "informe.py"), "--selftest"],
     "El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo"),
    ("código", [sys.executable, str(PMO / "servidor.py"), "--selftest"],
     "Rostrum: rutas, que no se salga de la carpeta, y que no escriba la ficha"),
    ("código", [sys.executable, str(PMO / "rastro.py"), "--selftest"],
     "Que el arnés deje la página de cada corrida, con lo que el agente mostró y sus cifras"),
    ("código", [sys.executable, str(PM / "portafolio.py"), "selftest"],
     "La copia de la aritmética corre sola, sin tocar el otro plugin"),
    ("código", [sys.executable, str(PM / "texto.py"), "--selftest"],
     "La copia de la conversión, igual"),
    ("código", [sys.executable, str(PRODUCT / "producto.py"), "selftest"],
     "El registro de requerimiento: evidencia, supuestos, trazas y la cifra del negocio"),

    ("respuestas", [sys.executable, str(RAIZ / "tests/criterio-portfolio/grade.py")],
     "Vera contra respuestas escritas a mano, incluido el control negativo"),
    ("respuestas", [sys.executable, str(RAIZ / "tests/criterio-project/grade.py")],
     "Samuel contra respuestas escritas leyendo las minutas"),
    ("respuestas", [sys.executable, str(RAIZ / "tests/criterio-product/grade.py")],
     "Alba contra respuestas escritas leyendo la definición y las entrevistas"),

    ("estructura", [sys.executable, str(RAIZ / "tests/coherencia.py")],
     "Que la documentación y el código digan lo mismo"),
    ("estructura", [sys.executable, str(RAIZ / "tests/contratos.py")],
     "Que cada comando y cada skill cumplan su contrato"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/validate_plugins.py")],
     "Que el marketplace y cada plugin estén completos"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/sincronizar.py"), "--check"],
     "Que las copias compartidas no se hayan separado"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/resultados.py"), "--selftest"],
     "Que la página de resultados no deje una puerta sin dueño"),
]

VERDE, ROJO, GRIS = "\033[32m", "\033[31m", "\033[90m"
FIN = "\033[0m"


def color(texto, c):
    return f"{c}{texto}{FIN}" if sys.stdout.isatty() else texto


def correr(nombre, cmd, porque, rapido):
    if rapido and nombre == "material":
        print(f"  {color('salta', GRIS)}  {Path(cmd[-1]).parent.name}/{Path(cmd[-1]).name}")
        return None
    etiqueta = f"{Path(cmd[1]).parent.name}/{Path(cmd[1]).name}"
    if len(cmd) > 2 and not cmd[2].startswith("-"):
        etiqueta += f" {cmd[2]}"
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=RAIZ)
    ms = int((time.time() - t0) * 1000)
    bien = r.returncode == 0
    print(f"  {color('verde' if bien else 'ROJO ', VERDE if bien else ROJO)}  "
          f"{etiqueta:44} {ms:>5} ms")
    print(f"         {color(porque, GRIS)}")
    if not bien:
        for linea in (r.stdout + r.stderr).strip().splitlines()[-12:]:
            print(f"         {linea}")
    return bien


def main() -> int:
    ap = argparse.ArgumentParser(description="Corre todo lo que verifica Criterio.")
    ap.add_argument("--rapido", action="store_true",
                    help="no regenera el material sintético")
    args = ap.parse_args()

    print("\nCriterio · verificación completa")
    print("La librería estándar y nada más.\n")

    resultados, seccion = [], None
    for nombre, cmd, porque in PUERTAS:
        if nombre != seccion:
            seccion = nombre
            print(f"{nombre.upper()}")
        r = correr(nombre, cmd, porque, args.rapido)
        if r is not None:
            resultados.append((cmd, r))
        print()

    malas = [c for c, ok in resultados if not ok]
    total = len(resultados)
    if malas:
        print(color(f"{len(malas)} de {total} en rojo", ROJO))
        for c in malas:
            print(f"   {' '.join(str(x) for x in c[1:])}")
        return 1
    print(color(f"{total} puertas en verde", VERDE))
    print("\nQué prueba cada corrida y qué no, en tests/criterio-portfolio/EVIDENCIA.md,")
    print("tests/criterio-project/EVIDENCIA.md y tests/criterio-product/EVIDENCIA.md —")
    print("incluido lo que todavía no se ha probado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
