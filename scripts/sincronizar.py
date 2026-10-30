#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mantiene iguales los scripts que dos plugins comparten.

    python3 scripts/sincronizar.py            copia y dice qué cambió
    python3 scripts/sincronizar.py --check    no copia; falla si difieren

`criterio-portfolio` y `criterio-project` comparten la aritmética. Dos copias que se separan es
exactamente la deuda que este proyecto no acepta, y la forma de no tenerla **no** es un
módulo compartido: un plugin instalado tiene que correr solo, y un `import` a la ruta
del otro plugin funciona en este repositorio y falla en el equipo de quien lo instaló,
que es el peor sitio para enterarse.

Así que se copia, y la copia se verifica. La fuente vive en `criterio-portfolio/scripts/` y
ahí se edita; la copia lleva una cabecera que lo dice, y `--check` falla si alguien la
editó en el sitio equivocado. Lo corre `tests/coherencia.py`, de modo que una copia
separada rompe la misma puerta que todo lo demás.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "plugins" / "criterio-portfolio" / "scripts"

# Qué comparte cada plugin, y por qué. Lo que no está aquí no se comparte: el informe
# de un proyecto no es el del portafolio recortado.
SCRIPTS = {
    "criterio-project": {
        "portafolio.py": "la aritmética; `compute` ya trabaja proyecto a proyecto",
        "texto.py": "leer un .docx es leer un .docx",
        "rastro.py": "el rastro de cada corrida lo escribe el arnés, igual para los tres",
        "terminos.py": "la aceptación de los términos se registra igual en los tres",
        "raiz.py": "buscar y marcar la carpeta raíz es igual en todos los agentes (ADR 0011)",
    },
    # Alba no calcula plan ni presupuesto —en definición no existen—, pero sí lee las
    # fichas de los proyectos que ejecutan su producto, y el contrato de campo
    # `{value, source, source_date, state}` es el mismo. `producto.py` lo importa de
    # esta copia en vez de reescribirlo: dos definiciones del mismo campo que se
    # separan es la deuda que este proyecto no acepta.
    "criterio-product": {
        "portafolio.py": "el contrato de campo, y leer la ficha del proyecto que ejecuta el producto",
        "texto.py": "una entrevista llega en .docx tanto como un acta",
        "rastro.py": "el rastro de cada corrida lo escribe el arnés, igual para los tres",
        "terminos.py": "la aceptación de los términos se registra igual en los tres",
        "raiz.py": "buscar y marcar la carpeta raíz es igual en todos los agentes (ADR 0011)",
    },
}

# La familia CFO toma de la PMO lo que es igual en cualquier función —leer un documento,
# registrar la aceptación de los términos— y comparte entre sus dos plugins su propio motor.
# La fuente de `finanzas.py` y de `finance-intake` es criterio-finance, donde se editan.
for _p in ("criterio-finance", "criterio-budget", "criterio-treasury", "criterio-legal", "criterio-compliance", "criterio-assistant",
           "criterio-sales", "criterio-revenue", "criterio-security", "criterio-vulnerability", "criterio-resilience"):
    SCRIPTS[_p] = {
        "texto.py": "un acta llega en .docx en finanzas tanto como en proyectos",
        "terminos.py": "la aceptación de los términos se registra igual en todos los agentes",
        "rastro.py": "el rastro de cada corrida lo escribe el arnés, igual en todas las familias (ADR 0010)",
        "raiz.py": "buscar y marcar la carpeta raíz es igual en todos los agentes (ADR 0011)",
    }
# Rostrum sirve lo que escriben todos: la página del informe de la PMO, su historia y la página de
# cada corrida son de quien las escribe, y el servidor las toma de su copia (ADR 0010).
SCRIPTS["criterio-server"] = {
    "informe.py": "la paleta y la página del informe: el servidor las sirve, no las reescribe",
    "portafolio.py": "la historia de las corridas se lee igual que la escribe la PMO",
    "rastro.py": "la página de una corrida es la que escribe el arnés",
    "terminos.py": "la aceptación de los términos se registra igual en todos los agentes",
    "raiz.py": "el mapa dice si la raíz de cada agente está marcada",
}
# El arnés de cada agente: el mismo `hooks.json` que llama a su copia de `rastro.py`.
HOOKS = ("criterio-finance", "criterio-budget", "criterio-treasury", "criterio-legal", "criterio-compliance", "criterio-assistant",
         "criterio-sales", "criterio-revenue", "criterio-security", "criterio-vulnerability", "criterio-resilience")
FUENTE_CFO = RAIZ / "plugins" / "criterio-finance" / "scripts"
SCRIPTS_CFO = {
    "criterio-budget": {
        "finanzas.py": "el motor de los dos: Tomás toma la ejecución de la misma contabilidad que cierra Clara",
        "nucleo.py": "tablas, fechas, inventario, señales y reporte: igual en cualquier función",
        "paises.json": "el registro único de países: ningún motor escribe el nombre de un país",
    },
    "criterio-treasury": {
        "finanzas.py": "el motor de los tres: Áurea toma los extractos que concilia Clara y el balance que ella cierra",
        "nucleo.py": "tablas, fechas, inventario, señales y reporte: igual en cualquier función",
        "paises.json": "el registro único de países: ningún motor escribe el nombre de un país",
    },
}
for _p in ("criterio-legal", "criterio-compliance", "criterio-assistant", "criterio-sales", "criterio-revenue",
           "criterio-security", "criterio-vulnerability", "criterio-resilience"):
    SCRIPTS_CFO[_p] = {"nucleo.py": "tablas, fechas, inventario, señales y reporte: igual en cualquier función",
                       "paises.json": "el registro único de países: ningún motor escribe el nombre de un país"}
# Las reglas de compromiso viven en el núcleo común (ADR 0012): `portafolio.py` lo importa, así que
# va con él a cada plugin que lo trae.
for _p in ("criterio-portfolio", "criterio-project", "criterio-product", "criterio-server"):
    SCRIPTS_CFO[_p] = {"nucleo.py": "las reglas de compromiso, comunes a Samuel, Vera y Ofelia (ADR 0012)",
                       "paises.json": "el registro único de países, que el núcleo carga al importarse"}
# La familia CLO tiene su propio motor, con fuente en criterio-legal.
FUENTE_CLO = RAIZ / "plugins" / "criterio-legal" / "scripts"
SCRIPTS_CLO = {
    "criterio-compliance": {
        "legal.py": "el motor de los dos: Constanza toma de las fichas de Fidel las obligaciones de los contratos",
    },
}
# La familia CCO tiene su propio motor, con fuente en criterio-sales: Valeria toma de las mismas
# exportaciones del CRM lo ganado que Augusto procesa en el embudo.
FUENTE_CCO = RAIZ / "plugins" / "criterio-sales" / "scripts"
SCRIPTS_CCO = {
    "criterio-revenue": {
        "ventas.py": "el motor de los dos: Valeria toma lo ganado de las mismas exportaciones que procesa Augusto",
    },
}
SKILLS_CCO = {
    "criterio-revenue": {
        "sales-intake": "los mismos documentos y la misma estructura",
        "crm-exports": "las mismas exportaciones del CRM, leídas igual",
    },
}
# La familia CISO tiene su propio motor, con fuente en criterio-security: Guillermo y Amparo procesan
# la misma carpeta de seguridad, con la misma referencia, y excluyen lo mismo.
FUENTE_CISO = RAIZ / "plugins" / "criterio-security" / "scripts"
SCRIPTS_CISO = {
    p: {"seguridad.py": "el motor de los tres: la misma carpeta, la misma referencia y lo mismo excluido"}
    for p in ("criterio-vulnerability", "criterio-resilience")
}
SKILLS_CISO = {
    p: {"security-intake": "los mismos documentos y la misma estructura"}
    for p in ("criterio-vulnerability", "criterio-resilience")
}
SKILLS_CLO = {
    "criterio-compliance": {
        "legal-intake": "los mismos documentos y la misma estructura",
    },
}

SKILLS_CFO = {
    "criterio-budget": {
        "finance-intake": "los mismos documentos, la misma estructura y las mismas columnas",
    },
    "criterio-treasury": {
        "finance-intake": "los mismos documentos, la misma estructura y las mismas columnas",
    },
}

# Lo que viaja con cada plugin instalado, byte a byte: los términos que rigen y el registro
# de versiones. Sin cabecera, porque su huella SHA-256 es la que se publica y la que firma
# cada comprobante; una copia que difiera en un byte tendría otra. La fuente es la raíz.
RAIZ_A_PLUGINS = {
    "TERMS.md": ("TERMS.md", "los términos que rigen, en inglés"),
    "TERMS.es.md": ("TERMS.es.md", "los términos que rigen, en español"),
    "registro/versiones.json": ("REGISTRO.json", "el registro de versiones de la familia"),
}
PLUGINS_FAMILIA = ("criterio-portfolio", "criterio-project", "criterio-product", "criterio-finance", "criterio-budget",
                   "criterio-treasury", "criterio-legal", "criterio-compliance", "criterio-assistant", "criterio-server",
                   "criterio-sales", "criterio-revenue", "criterio-security", "criterio-vulnerability", "criterio-resilience")

# Los skills que son método y no rol. Un riesgo es un riesgo lo mire quien lo mire, y
# la ficha es el contrato de datos de la familia entera. Los que quedan fuera lo hacen
# por alcance, no por casualidad: `portfolio-health` y `portfolio-history` solo tienen
# sentido mirando el conjunto, y un gerente de proyecto no mira el conjunto.
SKILLS = {
    "criterio-project": {
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
    # Ofelia lleva los compromisos de dirección con las mismas reglas que Samuel (ADR 0012).
    "criterio-assistant": {
        "commitment-tracking": "el compromiso vencido, el que nadie fechó y el que se movió: las reglas de Samuel",
    },
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
# La fuente es plugins/{origen}/scripts/{nombre}. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
"""


# En markdown la marca va como comentario HTML: no se ve al leer el skill, se ve al
# abrirlo para editarlo, que es exactamente cuando hace falta.
MARCA_MD = ("<!-- COPIA · la fuente es plugins/{origen}/skills/{nombre}/. "
            "La escribe scripts/sincronizar.py y no se edita aquí. -->\n")


def con_cabecera(texto: str, nombre: str, origen: str = "criterio-portfolio") -> str:
    """La cabecera va después del shebang, si lo hay, para no romper el ejecutable."""
    marca = CABECERA.format(nombre=nombre, origen=origen)
    if texto.startswith("#!"):
        primera, _, resto = texto.partition("\n")
        return f"{primera}\n{marca}{resto}"
    return marca + texto


def con_marca_md(texto: str, nombre: str, origen: str = "criterio-portfolio") -> str:
    """Después del frontmatter, que tiene que seguir siendo lo primero del archivo."""
    marca = MARCA_MD.format(nombre=nombre, origen=origen)
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

    for fuente_dir, origen_plugin, tabla in ((FUENTE_CFO, "criterio-finance", SCRIPTS_CFO),
                                             (FUENTE_CLO, "criterio-legal", SCRIPTS_CLO),
                                             (FUENTE_CCO, "criterio-sales", SCRIPTS_CCO),
                                             (FUENTE_CISO, "criterio-security", SCRIPTS_CISO)):
        for plugin, archivos in sorted(tabla.items()):
            for nombre, porque in sorted(archivos.items()):
                origen = fuente_dir / nombre
                if not origen.exists():
                    estado["problemas"].append(f"falta la fuente {origen.relative_to(RAIZ)}")
                    continue
                texto = origen.read_text(encoding="utf-8")
                # Un JSON no admite comentarios: se copia tal cual, y su campo «nota» dice cuál es la fuente.
                _comparar(RAIZ / "plugins" / plugin / "scripts" / nombre,
                          texto if origen.suffix == ".json" else con_cabecera(texto, nombre, origen_plugin),
                          f"{plugin}/scripts/{nombre}", porque, escribir,
                          origen.stat().st_mode, estado)

    for fuente_dir, origen_plugin, tabla in ((FUENTE.parent, "criterio-portfolio", SKILLS),
                                             (FUENTE_CFO.parent, "criterio-finance", SKILLS_CFO),
                                             (FUENTE_CLO.parent, "criterio-legal", SKILLS_CLO),
                                             (FUENTE_CCO.parent, "criterio-sales", SKILLS_CCO),
                                             (FUENTE_CISO.parent, "criterio-security", SKILLS_CISO)):
        for plugin, skills in sorted(tabla.items()):
            for nombre, porque in sorted(skills.items()):
                carpeta = fuente_dir / "skills" / nombre
                if not carpeta.is_dir():
                    estado["problemas"].append(f"falta el skill fuente {nombre}")
                    continue
                # Un skill es una carpeta: SKILL.md y lo que cuelgue de él. Se copia entero,
                # porque media copia es peor que ninguna.
                for origen in sorted(x for x in carpeta.rglob("*") if x.is_file()):
                    rel = origen.relative_to(carpeta)
                    texto = origen.read_text(encoding="utf-8")
                    if origen.name == "SKILL.md":
                        texto = con_marca_md(texto, nombre, origen_plugin)
                    _comparar(RAIZ / "plugins" / plugin / "skills" / nombre / rel, texto,
                              f"{plugin}/skills/{nombre}/{rel}", porque, escribir,
                              origen.stat().st_mode, estado)

    hooks = FUENTE.parent / "hooks" / "hooks.json"
    for plugin in HOOKS:
        _comparar(RAIZ / "plugins" / plugin / "hooks" / "hooks.json", hooks.read_text(encoding="utf-8"),
                  f"{plugin}/hooks/hooks.json", "el arnés llama a su copia de rastro.py, como en la familia PMO",
                  escribir, 0o644, estado)

    for plugin in PLUGINS_FAMILIA:
        for fuente, (destino, porque) in sorted(RAIZ_A_PLUGINS.items()):
            origen = RAIZ / fuente
            if not origen.exists():
                estado["problemas"].append(f"falta la fuente {fuente}")
                continue
            _comparar(RAIZ / "plugins" / plugin / destino, origen.read_text(encoding="utf-8"),
                      f"{plugin}/{destino}", porque, escribir, 0o644, estado)

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
