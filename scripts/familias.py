#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El diseño de las familias, escrito desde sus tres fuentes.

    python3 scripts/familias.py           escribe FUENTES.es.md, las tablas de DISENO.es.md, los
                                          bloques de los README y del skill de documentos de cada
                                          plugin, y la estructura que usa el motor
    python3 scripts/familias.py --check   falla si alguna copia no sale de las fuentes, o si las
                                          fuentes no cuadran entre sí

Cada familia tiene tres fuentes en families/criterio-<familia>/, y cada cosa tiene una sola:
  fuentes.json    las fuentes técnicas, normativas y las cifras de terceros, con su estado
  carpetas.json   la estructura de carpetas recomendada (ADR 0007)
  familia.json    los agentes, sus comandos con entrada, proceso y reporte, y sus señales

Escribe además `plugins/criterio-server/scripts/agentes.json`: los agentes de todas las familias
—también los de la PMO, desde families/criterio-pmo/familia.json— con su plugin, su área, sus
grupos y sus comandos, que es de donde Rostrum los saca (ADR 0010). Ningún nombre de agente se
escribe a mano en el servidor, y cada comando que existe en un plugin tiene que estar ahí.

El portal las publica con scripts/criterio-familias.mjs. Lo que comprueba
además de las copias: que cada carpeta citada por un comando exista en la estructura, que cada
fuente citada por un comando esté verificada (ADR 0006, regla 1), que cada campo que lee un motor
esté verificado en su fuente y que la numeración vaya de diez en diez.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
AVISO = "generado por scripts/familias.py; no se edita a mano"
P = RAIZ / "plugins"

# Las familias salen de families/criterio-<sigla>/familia.json, en su `orden`: ninguna se escribe aquí.
# Lo que cambia de una a otra —su ADR, dónde van sus cifras, su intake, su motor— está en su
# bloque `generador`; la de la PMO no lo trae, porque sus fuentes las escribe scripts/soporte.py.
def todas() -> list[dict]:
    fams = [json.loads(f.read_text(encoding="utf-8")) | {"dir": f.parent}
            for f in (RAIZ / "families").glob("criterio-*/familia.json")]
    return sorted(fams, key=lambda fa: fa["orden"])


def construida(fa: dict) -> bool:
    """Una familia en diseño todavía no tiene plugin: no entra a Rostrum ni a su página."""
    return all((P / a["plugin"]).is_dir() for a in fa["agentes"])


def config(fa: dict) -> dict:
    g = fa["generador"]
    intake = g.get("intake")
    return {"dir": fa["dir"], "adr": fa["adr"], "cifras_en": g["cifras_en"],
            "intake": (P / intake["skill"].split("/")[0] / "skills" / intake["skill"].split("/")[1] / "SKILL.md",
                       intake["texto"]) if intake else None,
            "estructuras": g.get("estructuras") or [],
            "motor": P / g["motor"] if g.get("motor") else None,
            "lectores": g.get("lectores") or {}}


FAMILIAS = {fa["sigla"]: fa for fa in todas() if "generador" in fa}
F: dict = {}          # la familia en curso
CLAVE = [""]


def cargar(nombre: str) -> dict:
    return json.loads((F["dir"] / nombre).read_text(encoding="utf-8"))


def poner(texto: str, nombre: str, contenido: str, ruta: Path) -> str:
    """Reemplaza el bloque entre sus marcas. La marca de apertura se busca por su prefijo, así
    que cambiar el aviso no deja huérfano ningún bloque."""
    pre = f"<!-- {CLAVE[0]}:{nombre} · "
    fin = f"<!-- /{CLAVE[0]}:{nombre} -->"
    if pre not in texto or fin not in texto:
        raise SystemExit(f"{ruta.relative_to(RAIZ)}: faltan las marcas de «{CLAVE[0]}:{nombre}»")
    a = texto.index(pre)
    b = texto.index(fin, a) + len(fin)
    return texto[:a] + f"{pre}{AVISO} -->\n{contenido}\n{fin}" + texto[b:]


def celda(s: str) -> str:
    return s.replace("|", "\\|")


# ---------------------------------------------------------------- las fuentes

def estado(f: dict) -> str:
    e = "Verificada" if f["estado"] == "verificada" else "Por verificar"
    return f"{e}: {f['nota']}" if f.get("nota") else e


def fuentes_md(fu: dict) -> str:
    l = [f"# criterio-{CLAVE[0]} · las fuentes", "",
         f"<!-- {AVISO}, desde fuentes.json -->", "",
         "Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la",
         "fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el",
         "material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en",
         "[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.", "",
         "**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se",
         "conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre",
         f"ella hasta verificarla ([ADR {F['adr'][:4]}](../../docs/decisions/{F['adr']}), regla 1).", ""]
    for s in fu["secciones"]:
        l += [f"## {s['titulo']}", "",
              "| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |", "|---|---|---|---|---|---|---|"]
        for f in s["fuentes"]:
            enl = " · ".join(f"[{t}]({u})" for t, u in f["enlaces"])
            l.append(f"| {f['id']} | {celda(f['fuente'])} | {celda(f['version'])} | {enl} | {f['consultada']} "
                     f"| {celda(estado(f))} | {celda(f['uso'])} |")
        l.append("")
    con_campos = [f for s in fu["secciones"] for f in s["fuentes"] if f.get("campos")]
    if con_campos:
        l += ["## Los campos que procesa el motor", "",
              "Cada campo de factura que lee `finanzas.py` está aquí con su identificador en la fuente. La",
              "puerta falla si el motor usa uno que no está, o uno por verificar.", ""]
        for f in con_campos:
            l += [f"**{f['id']} · {f['fuente']}**", "", "| Id | Campo | Estado |", "|---|---|---|"]
            l += [f"| {c['id']} | {celda(c['campo'])} | {'Verificado' if c['estado'] == 'verificado' else 'Por verificar'} |" for c in f["campos"]]
            l.append("")
    l += ["## Cifras de terceros", "",
          "| Id | Cifra | Fuente | Año | Muestra | Estado |", "|---|---|---|---|---|---|"]
    for c in fu["cifras"]:
        l.append(f"| {c['id']} | **{c['valor']['es']}** {celda(c['cifra']['es'])} | [{celda(c['fuente'])}]({c['enlace']}) "
                 f"| {c['anio']} | {celda(c['muestra']['es'])} | {celda(estado(c))} |")
    l += ["", "## Cómo se agrega una fuente", "",
          "1. Se agrega en `fuentes.json` con el siguiente identificador libre —F-NN para fuentes técnicas",
          "   y normativas, C-NN para cifras de terceros— y la fila entera: versión, enlace al emisor, fecha",
          "   de consulta, estado y uso. Después se corre `python3 scripts/familias.py`.",
          "2. Un campo de factura que procese el motor va en la lista de campos de su fuente, con su",
          "   identificador en el anexo; la puerta falla si el motor usa uno que no está verificado.",
          "3. Mientras diga «por verificar», nada se construye sobre ella: la puerta falla si un comando",
          "   la cita.",
          "4. Cuando una fuente cambia de versión, se agrega la nueva fila y la anterior se marca como",
          "   reemplazada, sin borrarla: el material de prueba generado con ella sigue citándola.", ""]
    return "\n".join(l)


def cifras_diseno(fu: dict, i: str = "es") -> str:
    ver = [c for c in fu["cifras"] if c["estado"] == "verificada"]
    pend = [c for c in fu["cifras"] if c["estado"] != "verificada"]
    ids = ", ".join(f"{c['id']} ({c['fuente'].split(',')[0]})" for c in ver)
    if i == "en":
        t = (f"Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) "
             f"(Spanish). Verified: {ids}.")
        if pend:
            t += " To be verified, and out of any publication until they are: " + ", ".join(c["id"] for c in pend) + "."
        return t
    t = (f"Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). "
         f"Verificadas: {ids}.")
    if pend:
        t += " Por verificar, y fuera de cualquier publicación hasta verificarse: " + ", ".join(c["id"] for c in pend) + "."
    return t


EN_PALABRAS = {"es": {1: "el", 2: "los dos", 3: "los tres", 4: "los cuatro"}, "en": {1: "the", 2: "the two", 3: "the three", 4: "the four"}}


def cifras_readme(fu: dict, i: str) -> str:
    cab = ("| Cifra | Fuente |" if i == "es" else "| Figure | Source |")
    l = [cab, "|---|---|"]
    for c in fu["cifras"]:
        if c["estado"] != "verificada":
            continue
        l.append(f"| **{c['valor'][i]}** {celda(c['cifra'][i])} | [{celda(c['fuente'])}, {c['anio']}]({c['enlace']}) — "
                 f"{celda(c['muestra'][i])} |")
    return "\n".join(l)


# ---------------------------------------------------------------- la familia

# Los encabezados de las tablas del diseño, en los dos idiomas: el diseño en inglés sale de las
# mismas fuentes que el español (cada texto de familia.json y carpetas.json trae los dos).
CABECERAS = {
    "es": {"agentes": "| Rol | Agente | Plugin | Qué hace |", "senales": "| Señal | Se levanta cuando |",
           "comandos": "| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |",
           "carpetas": "| Carpeta | Qué va | Agente |"},
    "en": {"agentes": "| Role | Agent | Plugin | What it does |", "senales": "| Signal | Raised when |",
           "comandos": "| # | Command | Input | Process (calculated by the code) | Report |",
           "carpetas": "| Folder | What goes in | Agent |"},
}


def agentes_md(fa: dict, i: str = "es") -> str:
    l = [CABECERAS[i]["agentes"], "|---|---|---|---|"]
    for a in fa["agentes"]:
        l.append(f"| {a['rol'][i]} | **{a['nombre']}** — {a['origen'][i]} | `{a['plugin']}` | {a['hace'][i]} |")
    return "\n".join(l)


def senales_md(fa: dict, i: str = "es") -> str:
    l = []
    for a in fa["agentes"]:
        l += [f"**{a['nombre']} · {a['rol'][i]}**", "", CABECERAS[i]["senales"], "|---|---|"]
        l += [f"| `{s['id']}` | {celda(s[i])} |" for s in a["senales"]]
        l.append("")
    return "\n".join(l).rstrip()


def comandos_md(a: dict, i: str = "es") -> str:
    l = [CABECERAS[i]["comandos"], "|---|---|---|---|---|"]
    for c in a["comandos"]:
        e = c[i]
        l.append(f"| {c['n']} | `{c['id']}` | {celda(e['entrada'])} | {celda(e['proceso'])} | {celda(e['reporte'])} |")
    return "\n".join(l)


def carpetas_md(ca: dict, fa: dict, i: str = "es") -> str:
    nombres = {a["id"]: a["nombre"] for a in fa["agentes"]}
    niveles = ca["niveles"]
    # Bajo la entidad: sus carpetas propias, después cada nivel con las suyas.
    items = [(f"{c['carpeta']}/", []) for c in niveles[0]["carpetas"]]
    items += [(n["carpeta"], [f"{c['carpeta']}/" for c in n["carpetas"]]) for n in niveles[1:]]
    arbol = [ca["raiz"]["carpeta"], f"└── {niveles[0]['carpeta']}"]
    for k, (nombre, hijos) in enumerate(items):
        ultimo = k == len(items) - 1
        arbol.append(f"    {'└── ' if ultimo else '├── '}{nombre}")
        for j, h in enumerate(hijos):
            arbol.append(f"    {'    ' if ultimo else '│   '}{'└── ' if j == len(hijos) - 1 else '├── '}{h}")
    arbol.append(ca["estado"]["carpeta"])
    l = [ca["raiz"][i], "", "```", *arbol, "```", ""]
    for n in niveles:
        l += [f"**`{n['carpeta']}`** · {n[i]}", "", CABECERAS[i]["carpetas"], "|---|---|---|"]
        for c in n["carpetas"]:
            l.append(f"| `{c['carpeta']}/` | {celda(c[i])} | {', '.join(nombres[x] for x in c['agentes'])} |")
        l.append("")
    l.append(f"**`{ca['estado']['carpeta']}`** · {ca['estado'][i]}.")
    return "\n".join(l)


# Los números en palabras, para los títulos que cuentan: «Los nueve comandos» sale del plugin, no
# de quien escribe, y una puerta compara cada cifra escrita en palabras con la que cuenta el código.
NUMEROS = {
    "es": {1: "un", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve",
           10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince", 16: "dieciséis",
           17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte"},
    "en": {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
           10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
           17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"},
}


def palabra(n: int, i: str) -> str:
    return NUMEROS[i][n]


def skills_de(plugin: str) -> list[str]:
    base = P / plugin / "skills"
    return sorted(d.name for d in base.iterdir() if (d / "SKILL.md").is_file()) if base.is_dir() else []


def cuenta(a: dict) -> tuple[int, int]:
    return len(a["comandos"]), len(skills_de(a["plugin"]))


def comandos_readme(a: dict, i: str) -> str:
    """La tabla de comandos de la página del agente, con la forma de las de la familia PMO: el
    comando con su prefijo y lo que entrega. De aquí la toma también el manual de los comandos."""
    n = len(a["comandos"])
    if i == "es":
        l = [f"### Los {palabra(n, i)} comandos", "",
             f"> Se escriben con el prefijo del plugin: `/{a['plugin']}:` y autocompletar hace el resto. Es la única "
             "forma que resuelve en una sesión de Claude Code.", "", "| Comando | Qué hace |", "|---|---|"]
    else:
        l = [f"### The {palabra(n, i)} commands", "",
             f"> They are typed with the plugin prefix: `/{a['plugin']}:` and autocomplete does the rest. It is the "
             "only form that resolves in a Claude Code session.", "", "| Command | What it does |", "|---|---|"]
    l += [f"| `/{a['plugin']}:{c['id']}` | {celda(c[i]['entrega'])} |" for c in a["comandos"]]
    return "\n".join(l)


def duenio(skill: str, fa: dict) -> dict:
    """El agente dueño de un skill es el primero de la familia que lo trae; los demás llevan copia."""
    return next(a for a in fa["agentes"] if skill in skills_de(a["plugin"]))


def de_quien(skill: str, a: dict, fa: dict, i: str) -> str:
    d = duenio(skill, fa)
    otros = [x["nombre"] for x in fa["agentes"] if x is not a and x is not d and skill in skills_de(x["plugin"])]
    y = " y " if i == "es" else " and "
    if d is a:
        tambien = [x["nombre"] for x in fa["agentes"] if x is not a and skill in skills_de(x["plugin"])]
        base = "Propio" if i == "es" else "Own"
        if tambien:
            base += (" · también en " if i == "es" else " · also in ") + y.join(tambien)
        return base
    base = f"Copia de {d['nombre']}" if i == "es" else f"Copy of {d['nombre']}'s"
    if otros:
        base += (" · también en " if i == "es" else " · also in ") + y.join(otros)
    return base


def skills_readme(a: dict, fa: dict, i: str) -> str:
    nombres = skills_de(a["plugin"])
    if i == "es":
        l = [f"### Los {palabra(len(nombres), i)} skills", "",
             "Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan "
             "como un manual.", "", "| Skill | Qué encapsula | De quién es |", "|---|---|---|"]
    else:
        l = [f"### The {palabra(len(nombres), i)} skills", "",
             "They load on their own when the subject comes up. They are the knowledge the commands share, and they "
             "are consulted like a manual.", "", "| Skill | What it encapsulates | Whose it is |", "|---|---|---|"]
    l += [f"| `{n}` | {celda(fa['skills'][n][i])} | {de_quien(n, a, fa, i)} |" for n in nombres]
    return "\n".join(l)


# ---------------------------------------------------------------- la página de la familia

# Rostrum en las tablas de cada familia: es el mismo para todas, así que su fila no sale de
# ninguna familia.
ROSTRUM = {
    "es": {"rol": "el portal", "hace": "Publicar lo que escriben los agentes donde el equipo lo vea, y recibir la pregunta de quien no abre una carpeta",
           "nunca": "**No escribe en el estado ni recalcula nada**, y no decide nada"},
    "en": {"rol": "the portal", "hace": "Publishing what the agents write where the team will see it, and taking the question from whoever will not open a folder",
           "nunca": "**Never writes the state or recalculates anything**, and decides nothing"},
}


def _readme(plugin: str, i: str) -> str:
    return f"../../plugins/{plugin}/README{'.es' if i == 'es' else ''}.md"


def familia_agentes(fa: dict, i: str) -> str:
    """De qué responde cada agente, qué nunca hace, su página y sus pruebas."""
    if i == "es":
        l = ["| | De qué responde | Lo que nunca hace | Su página | Sus pruebas |", "|---|---|---|---|---|"]
    else:
        l = ["| | What it answers for | What it never does | Its page | Its tests |", "|---|---|---|---|---|"]
    res = "resultados" if i == "es" else "results"
    for a in fa["agentes"]:
        nc, ns = cuenta(a)
        cs = f"{nc} comandos, {ns} skills" if i == "es" else f"{nc} commands, {ns} skills"
        l.append(f"| **{a['nombre']}** · {a['rol'][i].lower() if a['rol'][i] != 'FP&A' else 'FP&A'} | {celda(a['hace'][i])} | "
                 f"{celda(a['nunca'][i])} | [{a['plugin']}]({_readme(a['plugin'], i)}) · {cs} | "
                 f"[{res}](../../tests/{a['plugin']}/RESULTADOS.md) |")
    r = ROSTRUM[i]
    dos = "2 comandos, uno para todas las familias" if i == "es" else "2 commands, one for every family"
    l.append(f"| **Rostrum** · {r['rol']} | {r['hace']} | {r['nunca']} | [criterio-server]({_readme('criterio-server', i)}) · "
             f"{dos} | [{res}](../../tests/criterio-server/RESULTADOS.md) |")
    return "\n".join(l)


def _mayus(t: str) -> str:
    return t[:1].upper() + t[1:]


def configuracion(fa: dict, i: str) -> str:
    """Dónde se ve cada agente, qué le hace falta configurado y cada cuánto corre: sale de sus
    comandos, el primero y el último de cada uno."""
    ag = fa["agentes"]
    fila = lambda k, xs: f"| **{k}** | " + " | ".join(xs) + " |"
    ent = "entidad" if i == "es" else "entity"
    if i == "es":
        l = ["| | " + " | ".join(a["nombre"] for a in ag) + " |", "|---|" + "---|" * len(ag),
             fila("Se instala", [f"`{a['plugin']}`" for a in ag]),
             fila("Instancias", [fa["instancia"][i] for a in ag]),
             fila("Se configura con", [f"`/{a['plugin']}:{a['comandos'][0]['id']}`" for a in ag]),
             fila("Cuánto tarda eso", ["Quince minutos" for a in ag]),
             fila("Qué le tienes que decir", [celda(_mayus(a["comandos"][0][i]["entrada"].split("Preguntas: ", 1)[-1])) for a in ag]),
             fila("Dónde queda", [f"`.criterio/{a['area']}/<{ent}>/config.json`, escrito por el comando" for a in ag]),
             fila("El que se le pone a un reloj", [f"`/{a['plugin']}:{a['comandos'][-1]['id']}`" for a in ag]),
             fila("Qué toca cada día", [celda(a["comandos"][-1][i]["proceso"]) for a in ag]),
             fila("Qué lo despierta además del reloj", ["Una pregunta que alguien dejó en Rostrum" for a in ag])]
    else:
        l = ["| | " + " | ".join(a["nombre"] for a in ag) + " |", "|---|" + "---|" * len(ag),
             fila("Installs as", [f"`{a['plugin']}`" for a in ag]),
             fila("Instances", [fa["instancia"][i] for a in ag]),
             fila("Configured with", [f"`/{a['plugin']}:{a['comandos'][0]['id']}`" for a in ag]),
             fila("How long that takes", ["Fifteen minutes" for a in ag]),
             fila("What you have to tell it", [celda(_mayus(a["comandos"][0][i]["entrada"].split("Questions: ", 1)[-1])) for a in ag]),
             fila("Where it lands", [f"`.criterio/{a['area']}/<{ent}>/config.json`, written by the command" for a in ag]),
             fila("The one you put on a clock", [f"`/{a['plugin']}:{a['comandos'][-1]['id']}`" for a in ag]),
             fila("What it does each day", [celda(a["comandos"][-1][i]["proceso"]) for a in ag]),
             fila("What wakes it besides the clock", ["A question somebody left in Rostrum" for a in ag])]
    return "\n".join(l)


def skills_familia(fa: dict, i: str) -> str:
    todos = sorted(fa["skills"])
    ag = fa["agentes"]
    compartidos = [s for s in todos if sum(s in skills_de(a["plugin"]) for a in ag) > 1]
    n = palabra(len(todos), i).capitalize()
    if i == "es":
        l = [f"{n} skills distintos entre {EN_PALABRAS['es'].get(len(fa['agentes']), len(fa['agentes']))} agentes. **Los que comparten son copias literales, no un módulo "
             "importado**: un plugin instalado tiene que correr solo. `scripts/sincronizar.py` las copia y "
             "`scripts/sincronizar.py --check` falla si se separan." if compartidos else f"{n} skills distintos entre {EN_PALABRAS['es'].get(len(fa['agentes']), len(fa['agentes']))} agentes.", ""]
    else:
        l = [f"{n} distinct skills across {EN_PALABRAS['en'].get(len(fa['agentes']), len(fa['agentes']))} agents. **The ones they share are literal copies, not an imported "
             "module**: an installed plugin has to run on its own. `scripts/sincronizar.py` copies them and "
             "`scripts/sincronizar.py --check` fails if they drift." if compartidos else f"{n} distinct skills across {EN_PALABRAS['en'].get(len(fa['agentes']), len(fa['agentes']))} agents.", ""]
    l += ["| Skill | " + " | ".join(a["nombre"] for a in ag) + " |", "|---|" + ":--:|" * len(ag)]
    l += [f"| `{s}` | " + " | ".join("●" if s in skills_de(a["plugin"]) else "·" for a in ag) + " |" for s in todos]
    return "\n".join(l)


def ronda_completa(sigla: str):
    """La ronda con el agente con la que todas las entidades del material quedaron corridas al menos
    una vez, o None. Un país nuevo entra con su propia ronda, sin repetir los que ya pasaron: por eso
    se cuenta lo corrido en todas las rondas, no en una sola. Sale de lo publicado en
    tests/evidencias/familias/: el estado no se escribe a mano."""
    material = RAIZ / "tests" / f"criterio-{sigla}" / "material"
    entidades = {d.name for d in material.iterdir() if d.is_dir()} if material.is_dir() else set()
    base = RAIZ / "tests" / "evidencias" / "familias" / sigla
    corridas: set[str] = set()
    for d in sorted(base.glob("ronda-*"), key=lambda x: int(x.name.split("-")[1])) if base.is_dir() else []:
        corridas |= {c.name for c in d.iterdir() if c.is_dir()}
        if entidades and entidades <= corridas:
            return int(d.name.split("-")[1])
    return None


def estado_familia(fa: dict, i: str) -> str:
    if i == "es":
        l = ["| Agente | Se instala | Su prueba |", "|---|---|---|"]
    else:
        l = ["| Agent | Installs as | Its test |", "|---|---|---|"]
    for a in fa["agentes"]:
        nc, ns = cuenta(a)
        cs = f"{nc} comandos, {ns} skills" if i == "es" else f"{nc} commands, {ns} skills"
        n = ronda_completa(fa["sigla"])
        if n:
            pr = (f"El motor, probado; con el agente, todas las entidades del material, hasta la ronda {n}" if i == "es"
                  else f"The engine, tested; with the agent, every entity in the material, up to round {n}")
        else:
            pr = ("El motor, probado; una primera ronda con el agente; la completa, pendiente" if i == "es"
                  else "The engine, tested; a first round with the agent; the full one, pending")
        l.append(f"| **{a['nombre']}** · {a['rol'][i]} | `{a['plugin']}` · {cs} | {pr} · "
                 f"[{'resultados' if i == 'es' else 'results'}](../../tests/{a['plugin']}/RESULTADOS.md) |")
    l.append(f"| **Rostrum** · {ROSTRUM[i]['rol']} | `criterio-server` · "
             f"{'2 comandos, para todas las familias' if i == 'es' else '2 commands, for every family'} | — |")
    return "\n".join(l)


def intake_md(ca: dict, fa: dict) -> str:
    """La estructura, como la necesita el agente instalado: el árbol, qué va en cada carpeta y quién la usa."""
    t = carpetas_md(ca, fa)
    return ("Recomendada, no obligatoria: el motor procesa la carpeta como esté, y el inventario dice qué archivo "
            "está fuera de su lugar y dónde iría (ADR 0007). " + F["intake"][1] + "\n\n" + t)


# ---------------------------------------------------------------- lo que tiene que cuadrar

def revisar(fu: dict, ca: dict, fa: dict) -> list[str]:
    err = []
    todas = [f for s in fu["secciones"] for f in s["fuentes"]] + fu["cifras"]
    ids = [f["id"] for f in todas]
    if len(ids) != len(set(ids)):
        err.append("fuentes.json: hay identificadores repetidos")
    por_id = {f["id"]: f for f in todas}
    for f in todas:
        if f["estado"] not in ("verificada", "por verificar"):
            err.append(f"{f['id']}: estado «{f['estado']}» no es verificada ni por verificar")
        if not re.fullmatch(r"C-\d\d" if f in fu["cifras"] else r"F-\d\d", f["id"]):
            err.append(f"{f['id']}: las fuentes van como F-NN y las cifras de terceros como C-NN")
    for c in fu["cifras"]:
        if not all(c[k].get(i) for k in ("valor", "cifra", "muestra") for i in ("es", "en")):
            err.append(f"{c['id']}: le falta texto en un idioma")

    agentes = {a["id"] for a in fa["agentes"]}
    numeradas = set()
    for nv in ca["niveles"]:
        nombres = [c["carpeta"] for c in nv["carpetas"]]
        if nombres != sorted(nombres):
            err.append(f"carpetas.json, {nv['id']}: las carpetas no van en el orden de su prefijo")
        for c in nv["carpetas"]:
            if not re.fullmatch(r"\d0-[a-z]+", c["carpeta"]):
                err.append(f"carpetas.json: «{c['carpeta']}» no va numerada de diez en diez")
            if not set(c["agentes"]) <= agentes:
                err.append(f"carpetas.json: «{c['carpeta']}» cita un agente que no existe")
            if not (c.get("es") and c.get("en")):
                err.append(f"carpetas.json: a «{c['carpeta']}» le falta el texto en un idioma")
            numeradas.add(c["carpeta"])
    for a in fa["agentes"]:
        if not any(a["id"] in c["agentes"] for nv in ca["niveles"] for c in nv["carpetas"]):
            err.append(f"{a['nombre']}: ninguna carpeta de la estructura es suya")
        cmds = [c["id"] for c in a["comandos"]]
        if [c["n"] for c in a["comandos"]] != list(range(len(cmds))):
            err.append(f"{a['nombre']}: los comandos no van numerados desde 0 sin saltos")
        if len(set(s["id"] for s in a["senales"])) != len(a["senales"]):
            err.append(f"{a['nombre']}: hay señales repetidas")
        for s in a["senales"]:
            if not (s.get("es") and s.get("en")):
                err.append(f"{s['id']}: le falta el texto en un idioma")
        for c in a["comandos"]:
            # El diseño en inglés publica el comando entero, así que el inglés trae lo mismo que el español.
            faltan = [k for k in c["es"] if not c["en"].get(k)]
            if faltan:
                err.append(f"{c['id']}: le falta en inglés {', '.join(faltan)}")
            texto = " ".join(list(c["es"].values()) + list(c["en"].values()))
            for tok in re.findall(r"`([^`]+)`", texto):
                cabeza = tok.split("/")[0]
                if re.match(r"\d\d-", cabeza) and cabeza not in numeradas:
                    err.append(f"{c['id']}: cita `{tok}` y esa carpeta no está en carpetas.json")
            for fid in re.findall(r"F-\d\d", texto):
                if fid not in por_id:
                    err.append(f"{c['id']}: cita {fid} y no está en fuentes.json")
                elif por_id[fid]["estado"] != "verificada":
                    err.append(f"{c['id']}: se apoya en {fid}, que está por verificar (ADR 0006, regla 1)")
    err += revisar_campos(fu)
    err += revisar_skills(fa)
    err += revisar_area(fa)
    return err


def revisar_area(fa: dict) -> list[str]:
    """El motor exige que cada agente use su propia carpeta de configuración: la de nucleo.py
    tiene que ser la `area` de familia.json."""
    texto = (P / "criterio-finance" / "scripts" / "nucleo.py").read_text(encoding="utf-8")
    m = re.search(r"^AREA = (\{.*?\})$", texto, re.S | re.M)
    motor = ast.literal_eval(m.group(1)) if m else {}
    return [f"{a['plugin']}: el motor usa .criterio/{motor.get(a['plugin'])}/ y familia.json dice .criterio/{a['area']}/"
            for a in fa["agentes"] if (P / a["plugin"]).is_dir() and motor.get(a["plugin"]) != a["area"]]


def revisar_skills(fa: dict) -> list[str]:
    """Cada skill de cada plugin está descrito en familia.json, en los dos idiomas, y nada más."""
    err = []
    en_plugins = {s for a in fa["agentes"] for s in skills_de(a["plugin"])}
    descritos = set(fa.get("skills") or {})
    for s in sorted(en_plugins - descritos):
        err.append(f"el skill {s} está en un plugin y no en los skills de familia.json")
    for s in sorted(descritos - en_plugins):
        err.append(f"familia.json describe el skill {s}, que ningún plugin trae")
    for s, t in (fa.get("skills") or {}).items():
        if not (t.get("es") and t.get("en")):
            err.append(f"el skill {s}: le falta la descripción en un idioma")
    for a in fa["agentes"]:
        if not (a.get("nunca", {}).get("es") and a.get("nunca", {}).get("en")):
            err.append(f"{a['nombre']}: le falta lo que nunca hace (nunca) en un idioma")
    if not (fa.get("instancia", {}).get("es") and fa.get("instancia", {}).get("en")):
        err.append("falta la instancia de la familia en un idioma")
    return err


# Cada cifra de comandos o de skills escrita en palabras tiene que ser una que cuenta el código:
# la del plugin en su página, la de la familia o la de uno de sus agentes en las de la familia.
# «Los dos comandos de reloj» no cuenta los comandos de nadie: es el de cada agente.
_CUENTA = re.compile(r"\b([a-záéíóúñ]+) (comandos|commands|skills)\b(?! de reloj)", re.I)


def revisar_cuentas(fa: dict) -> list[str]:
    err = []
    a_n = {i: {v: k for k, v in NUMEROS[i].items()} for i in ("es", "en")}
    familia = (sum(len(a["comandos"]) for a in fa["agentes"]), len(fa.get("skills") or {}))
    paginas = [(F["dir"] / n, i, [familia] + [cuenta(a) for a in fa["agentes"]])
               for n, i in (("README.es.md", "es"), ("README.md", "en"), ("DISENO.es.md", "es"), ("DISENO.md", "en"))]
    paginas += [(P / a["plugin"] / n, i, [cuenta(a)]) for a in fa["agentes"]
                for n, i in (("README.es.md", "es"), ("README.md", "en"))]
    for ruta, i, validas in paginas:
        if not ruta.is_file():
            continue
        for m in _CUENTA.finditer(ruta.read_text(encoding="utf-8")):
            n = a_n[i].get(m.group(1).lower())
            if n is None:
                continue
            tipo = 0 if m.group(2).lower() in ("comandos", "commands") else 1
            if n not in {v[tipo] for v in validas}:
                err.append(f"{ruta.relative_to(RAIZ)} dice «{m.group(0)}» y el código cuenta "
                           f"{' o '.join(str(v[tipo]) for v in validas)}")
    return err


def revisar_campos(fu: dict) -> list[str]:
    """Cada campo de factura que procesa el motor tiene que estar verificado en su fuente (ADR 0006, regla 2)."""
    if not F["motor"] or not F["motor"].is_file() or not F["lectores"]:
        return []
    import importlib.util
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(f"motor_{CLAVE[0]}", F["motor"])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    por_id = {f["id"]: f for s in fu["secciones"] for f in s["fuentes"]}
    err = []
    for constante, ids in F["lectores"].items():
        campos = {c["id"]: c for i in ids for c in (por_id.get(i) or {}).get("campos", [])}
        for k in getattr(mod, constante, {}):
            if k not in campos:
                err.append(f"{F['motor'].name} usa el campo {k} y no está en {' ni '.join(ids)}")
            elif campos[k]["estado"] != "verificado":
                err.append(f"{F['motor'].name} usa el campo {k}, que está por verificar en {' o '.join(ids)}")
    return err


def nombres_json(fa: dict) -> str:
    """El nombre en palabras de cada señal y de cada comando de la familia, para que el motor los
    escriba así en sus reportes: un reporte que se abre fuera del portal también se entiende."""
    d = {"generado": f"por scripts/familias.py desde families/criterio-{CLAVE[0]}/familia.json; {AVISO}",
         "senales": {x["id"]: x["es"] for a in fa["agentes"] for x in a.get("senales") or []},
         "comandos": {c["id"]: c["es"]["etiqueta"] for a in fa["agentes"] for c in a["comandos"]}}
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n"


def estructura_json(ca: dict) -> str:
    """Lo que el motor necesita de la estructura para decir qué está fuera de su lugar."""
    d = {"generado": f"por scripts/familias.py desde families/criterio-{CLAVE[0]}/carpetas.json; no se edita a mano",
         "niveles": [{"id": n["id"], "ruta": n.get("ruta"), "profundidad": n.get("profundidad", 1),
                      "etiqueta": "" if not n.get("ruta") else n["carpeta"],
                      "carpetas": [{"carpeta": c["carpeta"], "patrones": c.get("patrones", [])} for c in n["carpetas"]]}
                     for n in ca["niveles"]]}
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n"


def una(clave: str, check: bool) -> tuple[list[str], int, int]:
    F.clear()
    F.update(config(FAMILIAS[clave]))
    CLAVE[0] = clave
    fu, ca, fa = cargar("fuentes.json"), cargar("carpetas.json"), cargar("familia.json")
    hecha = construida(fa)
    errores = revisar(fu, ca, fa) + revisar_cuentas(fa)
    salidas: list[tuple[Path, str]] = [(F["dir"] / "FUENTES.es.md", fuentes_md(fu))]
    # El diseño, en los dos idiomas: las mismas tablas, de las mismas fuentes.
    for nombre_d, i in (("DISENO.es.md", "es"), ("DISENO.md", "en")):
        diseno = F["dir"] / nombre_d
        if not diseno.is_file():
            continue
        d = diseno.read_text(encoding="utf-8")
        for nombre, contenido in (("agentes", agentes_md(fa, i)), ("senales", senales_md(fa, i)),
                                  ("cifras", cifras_diseno(fu, i))):
            d = poner(d, nombre, contenido, diseno)
        for a in fa["agentes"]:
            d = poner(d, f"comandos-{a['id']}", comandos_md(a, i), diseno)
        salidas.append((diseno, d))
    # La página de la familia, con la forma de la de la PMO: lo que sale de las fuentes y de los
    # plugins —quién responde de qué, la estructura, la configuración, los skills, el estado— no
    # se escribe a mano.
    for nombre_r, i in (("README.es.md", "es"), ("README.md", "en")):
        pagina = F["dir"] / nombre_r
        if not pagina.is_file():
            if not hecha:
                continue
            errores.append(f"falta families/criterio-{CLAVE[0]}/{nombre_r}, la página de la familia")
            continue
        t = pagina.read_text(encoding="utf-8")
        for nombre, contenido in (("familia-agentes", familia_agentes(fa, i)), ("carpetas", carpetas_md(ca, fa, i)),
                                  ("configuracion", configuracion(fa, i)), ("skills-familia", skills_familia(fa, i)),
                                  ("estado", estado_familia(fa, i))):
            t = poner(t, nombre, contenido, pagina)
        salidas.append((pagina, t))
    for a in fa["agentes"]:
        base = P / a["plugin"]
        for nombre, i in (("README.es.md", "es"), ("README.md", "en")):
            ruta = base / nombre
            if not ruta.is_file():
                continue
            t = poner(ruta.read_text(encoding="utf-8"), "comandos", comandos_readme(a, i), ruta)
            t = poner(t, "skills", skills_readme(a, fa, i), ruta)
            if a["id"] == F["cifras_en"]:
                t = poner(t, "cifras", cifras_readme(fu, i), ruta)
            salidas.append((ruta, t))
    intake = F["intake"][0] if F["intake"] else None
    if intake and intake.is_file():
        salidas.append((intake, poner(intake.read_text(encoding="utf-8"), "intake", intake_md(ca, fa), intake)))
    for p in F["estructuras"]:
        ruta = P / p / "scripts" / "estructura.json"
        if ruta.parent.is_dir():
            salidas.append((ruta, estructura_json(ca)))
            salidas.append((ruta.with_name("nombres.json"), nombres_json(fa)))
    for ruta, nuevo in salidas:
        actual = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
        if nuevo == actual:
            continue
        if check:
            errores.append(f"{ruta.relative_to(RAIZ)}: no es lo que sale de las fuentes; corre scripts/familias.py")
        else:
            ruta.write_text(nuevo, encoding="utf-8")
            print(f"  {ruta.relative_to(RAIZ)}")
    return [f"{clave.upper()} · {e}" for e in errores], sum(len(a["comandos"]) for a in fa["agentes"]), len(salidas)


# ---------------------------------------------------------------- los agentes, para Rostrum

SERVIDOR = {"id": "rostrum", "nombre": "Rostrum", "plugin": "criterio-server", "area": "rostrum",
            "rol": {"es": "El portal", "en": "The portal"}, "titulo": "el portal",
            "grupos": [{"titulo": "El portal", "linea": "El mapa de las familias y el servidor que las publica",
                        "comandos": [{"id": "server-setup", "etiqueta": "El mapa de las familias"},
                                     {"id": "server-start", "etiqueta": "Levantar el portal"}]}]}


# Las palabras que la impresora no dice: los agentes no «leen», procesan, calculan y preparan.
PROHIBIDAS = ("leen ", "gratis", "free ", "100 %", "100%", "certificad", "certified")


def revisar_impresora(sigla: str, fa: dict) -> list[str]:
    """La hoja de la impresora del portal: en los dos idiomas, cada línea de un agente de la
    familia o de Rostrum, cada robot con su papel, y sin las palabras que no se usan."""
    err, imp = [], fa.get("impresora")
    if not imp:
        return [f"{sigla}: falta la impresora (impresora en familia.json)"]
    propios = {a["id"] for a in fa["agentes"]}
    bots = imp.get("bots") or []
    if set(bots) - propios - {"rostrum"} or not propios <= set(bots):
        err.append(f"{sigla}: los robots de la impresora no son los agentes de la familia y Rostrum")
    for i in ("es", "en"):
        t = imp.get(i) or {}
        for k in ("eyebrow", "titulo", "sub", "ficha", "fichaNota", "roles", "nota", "guion"):
            if not t.get(k):
                err.append(f"{sigla}.impresora.{i}: falta {k}")
        if set(t.get("roles") or {}) != set(bots):
            err.append(f"{sigla}.impresora.{i}: cada robot lleva su papel, y solo ellos")
        quienes = [x.get("quien") for x in t.get("guion") or [] if x.get("quien")]
        if set(quienes) - set(bots) - {"ficha"} or set(bots) - set(quienes):
            err.append(f"{sigla}.impresora.{i}: la hoja habla de cada robot, y solo de ellos")
        todo = json.dumps(t, ensure_ascii=False).lower()
        for w in PROHIBIDAS:
            if w in todo:
                err.append(f"{sigla}.impresora.{i}: dice «{w.strip()}»")
    if len((imp.get("es") or {}).get("guion") or []) != len((imp.get("en") or {}).get("guion") or []):
        err.append(f"{sigla}.impresora: la hoja no tiene las mismas líneas en los dos idiomas")
    return err


def _raiz():
    """raiz.py de criterio-server, el mismo que copia cada plugin."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("raiz", P / "criterio-server" / "scripts" / "raiz.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def agentes_json() -> tuple[str, list[str]]:
    """Los agentes de las familias construidas, en su orden. Una en diseño todavía no tiene plugin."""
    err, familias, agentes = [], [], []
    hechas = [fa for fa in todas() if construida(fa)]
    for fa in hechas:
        sigla = fa["sigla"]
        familias.append({"sigla": sigla, "nombre": fa["nombre"], "estado": fa["estado"],
                         "agentes": [a["area"] for a in fa["agentes"]]})
        for a in fa["agentes"]:
            if "grupos" in a:
                grupos = a["grupos"]
            else:
                por_n = sorted(a["comandos"], key=lambda c: c["n"])
                ritmo = [por_n[0], por_n[-1]]
                grupos = [{"titulo": "Arranque y ritmo", "linea": "Instalar y saber qué toca hoy",
                           "comandos": [{"id": c["id"], "etiqueta": c["es"]["etiqueta"]} for c in ritmo]},
                          {"titulo": a["rol"]["es"], "linea": a["hace"]["es"],
                           "comandos": [{"id": c["id"], "etiqueta": c["es"]["etiqueta"]} for c in por_n[1:-1]]}]
            # El setup y la marca de su carpeta raíz son de raiz.py (ADR 0011): aquí solo se copian,
            # para que Rostrum y el portal digan cómo entra cada agente al mapa sin escribirlo a mano.
            dest = _raiz().DESTINO.get(a["plugin"]) or {}
            agentes.append({"id": a["id"], "nombre": a["nombre"], "plugin": a["plugin"], "area": a["area"],
                            "ambitos": a.get("ambitos") or [], "familia": sigla, "rol": a["rol"], "titulo": a.get("titulo") or a["rol"]["es"].lower(),
                            "setup": dest.get("setup"), "marca": dest.get("marca"), "grupos": grupos})
    for a in agentes + [SERVIDOR]:
        existentes = {x.stem for x in (P / a["plugin"] / "commands").glob("*.md")}
        en_grupos = [c["id"] for g in a["grupos"] for c in g["comandos"]]
        if len(en_grupos) != len(set(en_grupos)):
            err.append(f"{a['nombre']}: un comando está en dos grupos")
        for x in sorted(existentes - set(en_grupos)):
            err.append(f"{a['plugin']}:{x} no está en ningún grupo de {a['nombre']}")
        for x in sorted(set(en_grupos) - existentes):
            err.append(f"{a['nombre']}: el grupo nombra {x}, que no existe en {a['plugin']}")
    for fa in hechas:
        err += revisar_impresora(fa["sigla"], fa)
    areas = [a["area"] for a in agentes]
    if len(areas) != len(set(areas)):
        err.append("dos agentes con la misma área")
    # El nombre de cada señal, para que Rostrum la diga en palabras y no en código.
    senales = {}
    for fa in hechas:
        for a in fa["agentes"]:
            senales.update({x["id"]: x["es"] for x in a.get("senales") or []})
    d = {"generado": f"por scripts/familias.py desde families/*/familia.json; {AVISO}",
         "familias": familias, "agentes": agentes, "servidor": SERVIDOR,
         "senales": dict(sorted(senales.items()))}
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n", err


def revisar_preguntas() -> list[str]:
    """Las preguntas frecuentes de cada familia: el portal las publica en los dos idiomas, así que
    los dos tienen que traer las mismas secciones y las mismas preguntas, en el mismo orden."""
    err = []
    for d in sorted((RAIZ / "families").glob("criterio-*")):
        es, en = d / "PREGUNTAS.es.md", d / "PREGUNTAS.md"
        if not es.is_file() and not en.is_file():
            continue
        if not (es.is_file() and en.is_file()):
            err.append(f"{d.name}: las preguntas frecuentes están en un solo idioma")
            continue
        forma = [[ln.startswith("## ") for ln in f.read_text(encoding="utf-8").splitlines() if ln.startswith(("## ", "### "))]
                 for f in (es, en)]
        if forma[0] != forma[1]:
            err.append(f"{d.name}: PREGUNTAS.es.md y PREGUNTAS.md no traen las mismas secciones y preguntas")
        for f in (es, en):
            texto = f.read_text(encoding="utf-8").lower()
            # «certificado» aquí es un documento (el de la contraparte), no una promesa de calidad.
            for x in (p for p in PROHIBIDAS if not p.startswith("certif")):
                if x in texto:
                    err.append(f"{d.name}/{f.name}: dice «{x.strip()}»")
    return err


def familias_servidor(reg: dict, i: str) -> str:
    """Cada agente de cada familia: su setup, dónde deja su configuración y con qué marca su
    carpeta raíz. Es lo que `server-setup` encuentra para armar el mapa."""
    cab = ("| Familia | Agente | Su setup | Deja su configuración en | Marca su carpeta raíz con |\n|---|---|---|---|---|"
           if i == "es" else
           "| Family | Agent | Its setup | Leaves its configuration in | Marks its root folder with |\n|---|---|---|---|---|")
    filas = [cab]
    nombre = {f["sigla"]: f["nombre"][i] for f in reg["familias"]}
    for a in reg["agentes"]:
        donde = f"`.criterio/{a['area']}/`" if a["area"] == "portafolio" else f"`.criterio/{a['area']}/<{'instancia' if i == 'es' else 'instance'}>/`"
        filas.append(f"| **Criterio {a['familia'].upper()}** · {celda(nombre[a['familia']])} | {a['nombre']} | "
                     f"`{a['setup']}` | {donde} | `{a['marca']}` |")
    return "\n".join(filas)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    errores, resumen = [], []
    for clave in FAMILIAS:
        e, n, archivos = una(clave, args.check)
        errores += e
        if n:
            resumen.append(f"{clave.upper()} {n} comandos y {archivos} archivos")
    contenido, e_ag = agentes_json()
    errores += [f"AGENTES · {e}" for e in e_ag]
    errores += [f"PREGUNTAS · {e}" for e in revisar_preguntas()]
    destino = P / "criterio-server" / "scripts" / "agentes.json"
    if destino.parent.is_dir():
        actual = destino.read_text(encoding="utf-8") if destino.exists() else ""
        if actual != contenido:
            if args.check:
                errores.append(f"{destino.relative_to(RAIZ)}: no es lo que sale de las familias; corre scripts/familias.py")
            else:
                destino.write_text(contenido, encoding="utf-8")
                print(f"  {destino.relative_to(RAIZ)}")
    # En el README de Rostrum, cómo entra cada familia al mapa: sale de las mismas familias.
    reg = json.loads(contenido)
    CLAVE[0] = "servidor"
    for nombre, i in (("README.es.md", "es"), ("README.md", "en")):
        ruta = P / "criterio-server" / nombre
        if not ruta.is_file():
            continue
        actual = ruta.read_text(encoding="utf-8")
        nuevo = poner(actual, "familias", familias_servidor(reg, i), ruta)
        if nuevo != actual:
            if args.check:
                errores.append(f"{ruta.relative_to(RAIZ)}: no es lo que sale de las familias; corre scripts/familias.py")
            else:
                ruta.write_text(nuevo, encoding="utf-8")
                print(f"  {ruta.relative_to(RAIZ)}")
    for e in errores:
        print(f"  ✗ {e}")
    if args.check and not errores:
        print(f"  las familias cuadran: {' · '.join(resumen)}, cada carpeta y cada fuente en su lugar")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
