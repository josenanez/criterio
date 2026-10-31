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
import shutil
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
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/sectores.py")],
     "Tres industrias con el mismo motor de hechos: finanzas, retail y minería"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/formatos.py")],
     "El material en Word, Excel y PDF, y que el plugin lo lea"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/disposiciones.py")],
     "Que el recorrido encuentre los mismos documentos sin importar cómo estén"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/cobertura.py")],
     "Que ninguna señal se quede sin disparar sin que esté declarado por qué"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/resumen.py")],
     "El resumen de las corridas diarias: precisión, cobertura y qué se movió"),
    ("código", [sys.executable, str(RAIZ / "tests/sintetico/regresion.py"), "verificar"],
     "La regresión del motor: cinco semanas de una organización, en cada cambio"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/evidencia.py"), "verificar"],
     "Que el registro de comandos no prometa una evidencia que no está"),
    ("material", [sys.executable, str(RAIZ / "tests/ronda.py"), "verificar"],
     "Que cada defecto registrado diga su origen, su corrección y dónde se verificó"),
    ("material", [sys.executable, str(RAIZ / "tests/banco.py"), "verificar"],
     "Que cada calificación del agente salga de sus conteos, con intervalo y origen"),
    ("código", [sys.executable, str(RAIZ / "tests/cronograma.py"), "--revisar"],
     "Que el Gantt y la curva de Rostrum digan lo que el motor calcula, en la corrida más reciente de cada industria"),
    ("material", [sys.executable, str(RAIZ / "tests/sintetico/funcionalidades.py"),
                  "--verificar"],
     "Que cada comando declare qué produce y qué deja escrito"),

    ("código", [sys.executable, str(PMO / "portafolio.py"), "selftest"],
     "La aritmética, la cadencia, la cola y el contraste entre las dos fichas"),
    ("código", [sys.executable, str(PMO / "texto.py"), "--selftest"],
     "Leer .docx, .xlsx, .pptx y .eml sin dependencias"),
    ("código", [sys.executable, str(PMO / "informe.py"), "--selftest"],
     "El informe: concordancia, formato de cifra, y que ninguna ruta salga en crudo"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-server/scripts/servidor.py"), "--selftest"],
     "Rostrum: rutas, que no se salga de lo que sirve, que no escriba la ficha, y las tres familias en un portal"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-server/scripts/mapa.py"), "--selftest"],
     "El mapa: cada agente por la carpeta de su configuración, y nada que no se haya confirmado"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-server/scripts/robots.py"), "--selftest"],
     "Los robots: cada uno con el gesto de su oficio, el mismo en el navegador y en el GIF, y quieto si se pide"),
    ("código", [sys.executable, str(PMO / "rastro.py"), "--selftest"],
     "Que el arnés deje la página de cada corrida, con lo que el agente mostró y sus cifras"),
    ("código", [sys.executable, str(PMO / "compartir.py"), "--selftest"],
     "Compartir hallazgos: el resumen cuenta comandos y señales del rastro y no lleva ningún dato de una entidad (decisión 0025)"),
    ("código", [sys.executable, str(PMO / "terminos.py"), "--selftest"],
     "Los términos: una aceptación por versión, con comprobante en Markdown y PDF y su huella SHA-256"),
    ("código", [sys.executable, str(PMO / "raiz.py"), "--selftest"],
     "La carpeta raíz: encontrarla por su estructura y su marca, y marcarla solo con permiso"),
    ("material", [sys.executable, str(RAIZ / "scripts/registro.py"), "verificar"],
     "El registro de versiones: cada entrada con su huella y la de la anterior, sin huecos"),
    ("código", [sys.executable, str(RAIZ / "scripts/trafico.py"), "--selftest"],
     "La cuenta de instalaciones: clonadores únicos de la ventana menos los pushes a main de esa misma ventana"),
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
    ("estructura", [sys.executable, str(RAIZ / "scripts/manual.py"), "--check"],
     "Que el manual diga lo que dicen los README y los contratos"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/industrias.py"), "--check"],
     "Que las industrias del README salgan de su fuente y que «probada» sea cierto"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/paises_probados.py"), "--check"],
     "Que la tabla de los países probados de la CFO y de la CLO salga de la evidencia de las rondas"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/carpetas.py"), "--check"],
     "Que la estructura de carpetas recomendada diga lo mismo en sus cinco copias"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/calidad.py"), "--selftest"],
     "Que laboratorio o estable salga de la evidencia con el piso del 95 %, y que cada versión siga la regla de diez por entero"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/hoja.py"), "--check"],
     "Que la hoja de ruta salga de su fuente y diga «liberada» solo de lo registrado"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/analisis.py"), "--check"],
     "Que el análisis estadístico diga lo que dice la evidencia de las rondas"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/analisis_familias.py"), "--check"],
     "Que el análisis estadístico de cada familia con rondas diga lo que dice la evidencia de sus rondas"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/compatibilidad.py"), "--check"],
     "Que cada script corra con el Python que trae el equipo de quien instala el plugin, desde el 3.9"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/soporte.py"), "--check"],
     "Que cada rol tenga el marco que lo define, verificado, y cada familia sus cifras de costo verificadas"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-treasury/scripts/finanzas.py"), "selftest"],
     "La copia de Áurea del motor: caja, pagos, exposición, vencimientos y covenants sobre una entidad mínima"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-finance/scripts/finanzas.py"), "selftest"],
     "El motor de Clara y Tomás: números, fechas, lectores de la DIAN y del SRI, y una entidad mínima"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cfo/generar.py")],
     "El material CFO: cuatro industrias y dos entidades de control, con su clave"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cfo/evaluar.py"), "--agente", "clara"],
     "Que Clara levante cada señal sembrada en el cierre, y ninguna en los controles"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cfo/evaluar.py"), "--agente", "tomas"],
     "Que Tomás levante cada señal sembrada en el presupuesto, y ninguna en los controles"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cfo/evaluar.py"), "--agente", "aurea"],
     "El motor de Áurea contra la clave: caja, pagos, exposición, vencimientos y covenants en cuatro industrias, y nada en los controles"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-legal/scripts/legal.py"), "selftest"],
     "El motor de Fidel y Constanza: fechas, prórrogas, plazos y una entidad mínima con todo mal"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-clo/generar.py")],
     "El material CLO: cuatro industrias y dos entidades de control, con su clave"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-clo/evaluar.py"), "--agente", "fidel"],
     "Que Fidel levante cada señal sembrada en los contratos, y ninguna en los controles"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-clo/evaluar.py"), "--agente", "constanza"],
     "Que Constanza levante cada señal sembrada en el cumplimiento, y ninguna en los controles"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-assistant/scripts/asistente.py"), "selftest"],
     "El motor de Ofelia: la agenda .ics con repeticiones y cambio de hora, el correo, las sesiones y una oficina mínima con todo mal"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-ea/generar.py")],
     "El material EA: dos oficinas con defectos y dos de control, con su clave"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-ea/evaluar.py")],
     "Que Ofelia levante cada señal sembrada en la oficina, ninguna en los controles, y cumpla las reglas de la operación real"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-sales/scripts/ventas.py"), "selftest"],
     "El motor de Augusto y Valeria: los lectores de Salesforce, de HubSpot y de cualquier CRM, las fechas mes/día y una entidad mínima con todo mal"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cco/generar.py")],
     "El material CCO: dos industrias y un control por país en Colombia y México, cada uno con la exportación de su CRM y su clave"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cco/evaluar.py"), "--agente", "augusto"],
     "Que Augusto levante cada señal sembrada en el embudo, el pronóstico y la meta, y ninguna en los controles"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-cco/evaluar.py"), "--agente", "valeria"],
     "Que Valeria levante cada señal sembrada de la venta a la factura, y ninguna en los controles ni un dato de contacto"),
    ("código", [sys.executable, str(RAIZ / "plugins/criterio-security/scripts/seguridad.py"), "selftest"],
     "El motor de Alexis, Guillermo y Amparo: la escala del CVSS, el catálogo KEV, lo que nunca se abre y una entidad mínima con todo mal"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-ciso/generar.py")],
     "El material CISO: banca, retail, salud y tecnología y dos controles, cada uno con su escáner, lo que nunca se abre y su clave"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-ciso/evaluar.py"), "--agente", "alexis"],
     "Que Alexis levante cada señal sembrada en los controles, los accesos, los terceros y los riesgos, y ninguna en los controles"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-ciso/evaluar.py"), "--agente", "guillermo"],
     "Que Guillermo levante cada señal sembrada en las vulnerabilidades, y ninguna en los controles"),
    ("material", [sys.executable, str(RAIZ / "tests/criterio-ciso/evaluar.py"), "--agente", "amparo"],
     "Que Amparo levante cada señal sembrada en los incidentes y las pruebas, y ninguna en los controles"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/familias.py"), "--check"],
     "Que el diseño de cada familia salga de sus fuentes y no se apoye en una por verificar"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/resultados.py"), "--selftest"],
     "Que la página de resultados no deje una puerta sin dueño"),
    ("estructura", [sys.executable, str(RAIZ / "scripts/descargas.py"), "selftest"],
     "el historial de descargas conserva cada día que sale de la ventana de GitHub"),
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
    # El extracto bancario en PDF del material de la CFO se lee con pdftotext, de poppler, como lo
    # lee el motor en el equipo de quien lo usa. Sin él, esas puertas fallan y aquí se dice por qué.
    if not shutil.which("pdftotext"):
        print(color("Falta pdftotext (poppler): las puertas que leen un PDF van a fallar. "
                    "Instálalo con `brew install poppler` (macOS) o `apt install poppler-utils` (Linux).\n", ROJO))

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
    print("tests/criterio-project/EVIDENCIA.md, tests/criterio-product/EVIDENCIA.md,")
    print("tests/criterio-cfo/EVIDENCIA.md, tests/criterio-clo/EVIDENCIA.md, tests/criterio-ea/EVIDENCIA.md,")
    print("tests/criterio-cco/EVIDENCIA.md y tests/criterio-ciso/EVIDENCIA.md —")
    print("incluido lo que todavía no se ha probado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
