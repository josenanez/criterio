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
           17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte", 21: "veintiún", 22: "veintidós",
           23: "veintitrés", 24: "veinticuatro", 25: "veinticinco", 26: "veintiséis", 27: "veintisiete",
           28: "veintiocho", 29: "veintinueve", 30: "treinta"},
    "en": {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
           10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
           17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty-one", 22: "twenty-two",
           23: "twenty-three", 24: "twenty-four", 25: "twenty-five", 26: "twenty-six", 27: "twenty-seven",
           28: "twenty-eight", 29: "twenty-nine", 30: "thirty"},
}


def palabra(n: int, i: str) -> str:
    return NUMEROS[i][n]


def skills_de(plugin: str) -> list[str]:
    base = P / plugin / "skills"
    return sorted(d.name for d in base.iterdir() if (d / "SKILL.md").is_file()) if base.is_dir() else []


def cuenta(a: dict) -> tuple[int, int]:
    """Los comandos del agente, con su entrada, y sus skills."""
    return len(a["comandos"]) + 1, len(skills_de(a["plugin"]))


def comandos_readme(a: dict, i: str) -> str:
    """La tabla de comandos de la página del agente, con la forma de las de la familia PMO: el
    comando con su prefijo y lo que entrega. De aquí la toma también el manual de los comandos."""
    n = len(a["comandos"]) + 1
    if i == "es":
        l = [f"### Los {palabra(n, i)} comandos", "",
             f"> Se escriben con el prefijo del plugin: `/{a['plugin']}:` y autocompletar hace el resto. Es la única "
             "forma que resuelve en una sesión de Claude Code.", "", "| Comando | Qué hace |", "|---|---|"]
    else:
        l = [f"### The {palabra(n, i)} commands", "",
             f"> They are typed with the plugin prefix: `/{a['plugin']}:` and autocomplete does the rest. It is the "
             "only form that resolves in a Claude Code session.", "", "| Command | What it does |", "|---|---|"]
    filas = [f"| `/{a['plugin']}:{c['id']}` | {celda(c[i]['entrega'])} |" for c in a["comandos"]]
    filas.insert(1, f"| `/{a['plugin']}:{a['id']}` | {ENTRADA[i][1].format(n=a['nombre'])} |")
    return "\n".join(l + filas)


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
    n_srv = len(list((P / "criterio-server" / "commands").glob("*.md")))
    dos = f"{n_srv} comandos, uno para todas las familias" if i == "es" else f"{n_srv} commands, one for every family"
    l.append(f"| **Rostrum** · {r['rol']} | {r['hace']} | {r['nunca']} | [criterio-server]({_readme('criterio-server', i)}) · "
             f"{dos} | [{res}](../../tests/criterio-server/RESULTADOS.md) |")
    return "\n".join(l)


def _mayus(t: str) -> str:
    return t[:1].upper() + t[1:]


def configuracion(fa: dict, i: str) -> str:
    """Dónde se ve cada agente, qué le hace falta configurado y cada cuánto corre: sale de sus
    comandos: el primero, el setup, y el de su reloj."""
    ag = fa["agentes"]
    # El del reloj es el `-wake`, no el último: desde la decisión 0025, el último es share-findings.
    reloj = {a["id"]: next(c for c in a["comandos"] if c["id"].endswith("-wake")) for a in ag}
    fila = lambda k, xs: f"| **{k}** | " + " | ".join(xs) + " |"
    # La carpeta de cada instancia: la entidad, salvo que la familia diga otra (la EA, el ejecutivo).
    ent = (fa.get("carpeta_instancia") or {"es": "entidad", "en": "entity"})[i]
    if i == "es":
        l = ["| | " + " | ".join(a["nombre"] for a in ag) + " |", "|---|" + "---|" * len(ag),
             fila("Se instala", [f"`{a['plugin']}`" for a in ag]),
             fila("Instancias", [fa["instancia"][i] for a in ag]),
             fila("Se configura con", [f"`/{a['plugin']}:{a['comandos'][0]['id']}`" for a in ag]),
             fila("Cuánto tarda eso", ["Quince minutos" for a in ag]),
             fila("Qué le tienes que decir", [celda(_mayus(a["comandos"][0][i]["entrada"].split("Preguntas: ", 1)[-1])) for a in ag]),
             fila("Dónde queda", [f"`.criterio/{a['area']}/<{ent}>/config.json`, escrito por el comando" for a in ag]),
             fila("El que se le pone a un reloj", [f"`/{a['plugin']}:{reloj[a['id']]['id']}`" for a in ag]),
             fila("Qué toca cada día", [celda(reloj[a["id"]][i]["proceso"]) for a in ag]),
             fila("Qué lo despierta además del reloj", ["Una pregunta que alguien dejó en Rostrum" for a in ag])]
    else:
        l = ["| | " + " | ".join(a["nombre"] for a in ag) + " |", "|---|" + "---|" * len(ag),
             fila("Installs as", [f"`{a['plugin']}`" for a in ag]),
             fila("Instances", [fa["instancia"][i] for a in ag]),
             fila("Configured with", [f"`/{a['plugin']}:{a['comandos'][0]['id']}`" for a in ag]),
             fila("How long that takes", ["Fifteen minutes" for a in ag]),
             fila("What you have to tell it", [celda(_mayus(a["comandos"][0][i]["entrada"].split("Questions: ", 1)[-1])) for a in ag]),
             fila("Where it lands", [f"`.criterio/{a['area']}/<{ent}>/config.json`, written by the command" for a in ag]),
             fila("The one you put on a clock", [f"`/{a['plugin']}:{reloj[a['id']]['id']}`" for a in ag]),
             fila("What it does each day", [celda(reloj[a["id"]][i]["proceso"]) for a in ag]),
             fila("What wakes it besides the clock", ["A question somebody left in Rostrum" for a in ag])]
    return "\n".join(l)


def skills_familia(fa: dict, i: str) -> str:
    todos = sorted(fa["skills"])
    ag = fa["agentes"]
    compartidos = [s for s in todos if sum(s in skills_de(a["plugin"]) for a in ag) > 1]
    n = palabra(len(todos), i).capitalize()
    if len(ag) == 1:
        l = [f"{n} skills, todos de {ag[0]['nombre']}." if i == "es" else f"{n} skills, all of them {ag[0]['nombre']}'s.", ""]
    elif i == "es":
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


def hay_rondas(sigla: str) -> bool:
    base = RAIZ / "tests" / "evidencias" / "familias" / sigla
    return base.is_dir() and any(base.glob("ronda-*"))


def estado_familia(fa: dict, i: str) -> str:
    if i == "es":
        l = ["| Agente | Se instala | Su prueba |", "|---|---|---|"]
    else:
        l = ["| Agent | Installs as | Its test |", "|---|---|---|"]
    for a in fa["agentes"]:
        nc, ns = cuenta(a)
        cs = f"{nc} comandos, {ns} skills" if i == "es" else f"{nc} commands, {ns} skills"
        n = ronda_completa(fa["sigla"])
        if not hay_rondas(fa["sigla"]):
            pr = ("El motor, probado; la ronda con el agente, pendiente" if i == "es"
                  else "The engine, tested; the round with the agent, pending")
        elif n:
            # Lo que el material llama entidad —en la EA, una oficina— y el artículo del agente, de familia.json.
            mat = (fa.get("unidad") or {"es": "entidades", "en": "entities"})[i]
            art = "la" if a.get("ella") else "el"
            pr = (f"El motor, probado; con {art} agente, todas las {mat} del material, hasta la ronda {n}" if i == "es"
                  else f"The engine, tested; with the agent, every {mat[:-1] if mat.endswith('s') else mat} in the material, up to round {n}")
        else:
            pr = ("El motor, probado; una primera ronda con el agente; la completa, pendiente" if i == "es"
                  else "The engine, tested; a first round with the agent; the full one, pending")
        l.append(f"| **{a['nombre']}** · {a['rol'][i]} | `{a['plugin']}` · {cs} | {pr} · "
                 f"[{'resultados' if i == 'es' else 'results'}](../../tests/{a['plugin']}/RESULTADOS.md) |")
    l.append(f"| **Rostrum** · {ROSTRUM[i]['rol']} | `criterio-server` · "
             f"{len(list((P / 'criterio-server' / 'commands').glob('*.md')))} "
             f"{'comandos, para todas las familias' if i == 'es' else 'commands, for every family'} | — |")
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
_CUENTA = re.compile(r"\b([a-záéíóúñ]+(?:-[a-z]+)?) (comandos|commands|skills)\b(?! de reloj)", re.I)


def revisar_cuentas(fa: dict) -> list[str]:
    err = []
    a_n = {i: {v: k for k, v in NUMEROS[i].items()} for i in ("es", "en")}
    familia = (sum(cuenta(a)[0] for a in fa["agentes"]), len(fa.get("skills") or {}))
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
    return [f"{clave.upper()} · {e}" for e in errores], sum(cuenta(a)[0] for a in fa["agentes"]), len(salidas)


# ---------------------------------------------------------------- la entrada de cada agente

# Cada agente tiene un comando con su nombre —/criterio-finance:clara— que recibe lo que la persona
# necesita en sus palabras y corre el comando que lo resuelve (decisión 0027). No tiene texto propio:
# su tabla sale de los grupos del agente y de la descripción de cada comando, así que un comando que
# cambia de descripción cambia aquí, y --check rompe si alguien lo editó a mano.
ENTRADA = {"es": ("Pídeselo a {n}", "Lo que necesites, en tus palabras: {n} elige el comando que lo resuelve y lo corre"),
           "en": ("Ask {n}", "Whatever you need, in your own words: {n} picks the command that does it and runs it")}


def descripcion(plugin: str, comando: str) -> str:
    texto = (P / plugin / "commands" / f"{comando}.md").read_text(encoding="utf-8")
    m = re.search(r"^description:\s*(.+)$", texto.split("\n---", 1)[0], re.M)
    return m.group(1).strip().strip('"') if m else ""


def entrada_md(a: dict, familia: list[dict]) -> str:
    """El comando de entrada del agente, desde sus grupos (los de agentes.json) y sus pares."""
    n, pl = a["nombre"], a["plugin"]
    filas = [f"| {celda(g['titulo'])} · {celda(c['etiqueta'])} | `/{pl}:{c['id']}` | {celda(descripcion(pl, c['id']))} |"
             for g in a["grupos"] for c in g["comandos"] if c["id"] != a["id"]]
    pares = [f"| {x['nombre']} · {x['titulo']} | `/{x['plugin']}:{x['id']}` |" for x in familia if x is not a]
    l = ["---",
         f"description: Pídeselo a {n} ({a['rol']['es']}) en tus palabras — dice qué comando lo resuelve y lo corre",
         'argument-hint: "[lo que necesitas, en tus palabras] o vacío"',
         "allowed-tools: Skill, Read, Glob",
         "---",
         f"<!-- generado desde families/criterio-{a['familia']}/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->",
         "",
         f"# /{a['id']} — {ENTRADA['es'][0].format(n=n)}",
         "",
         f"Quien trabaja con {n} no tiene que saber cómo se llama cada comando: dice lo que necesita y este",
         "comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace",
         "el comando elegido, con su motor y sus reglas.",
         "",
         "## Flujo",
         "",
         f"**1. Sin argumento**, muestra en una pantalla lo que {n} sabe hacer —los grupos de la tabla de abajo,",
         "con sus etiquetas y sin nombres de comando— y pregunta qué necesita la persona.",
         "",
         "**2. Con argumento, elige de la tabla el comando que lo resuelve.** Antes de elegir, busca en la",
         "tabla **todos** los que encajan, no solo el primero:",
         "",
         "- **Dos o más posibles:** pregunta cuál, con sus etiquetas, y no corras nada. Un pedido general",
         "  —«revisa», «qué pasa con», «cómo va»— que no nombra lo que distingue a dos comandos es de dos",
         "  posibles aunque uno parezca más probable. No adivines: correr el equivocado cuesta más que una",
         "  pregunta.",
         "- **Pero si el pedido nombra lo que distingue a uno** —«el embudo», «el banco», «las facturas»,",
         "  la palabra de su etiqueta—, es ese, aunque otro toque el mismo tema: no preguntes.",
         "- **Uno solo:** di en una línea cuál vas a correr y por qué —«Esto es *<etiqueta>*: corro",
         "  `/<comando>`»— y córrelo con la herramienta que corre los comandos, pasándole como argumento lo que",
         "  del pedido le sirva. Si no puedes invocarlo, dile a la persona exactamente qué escribir.",
         f"- **Es de otro agente de la familia:** dilo en una línea y da su entrada, de la segunda tabla.",
         "- **Ninguno:** dilo en una línea. No improvises el trabajo con lo que hay en la conversación.",
         "",
         "**Un comando a la vez, sin subagentes en paralelo.**",
         "",
         "**3. Lo que el pedido no dice no se inventa.** Si el comando necesita un dato que el pedido no trae —un",
         "periodo, un proyecto, una ruta—, lo pide el propio comando.",
         "",
         "**4. Si el comando elegido responde que falta la configuración**, ofrece",
         f"`{a['setup']}` y no corras nada más.",
         "",
         f"## Lo que {n} sabe hacer",
         "",
         "| Para | Comando | Qué hace |",
         "|---|---|---|",
         *filas]
    if pares:
        l += ["", "## Los otros agentes de la familia", "", "| Agente | Su entrada |", "|---|---|", *pares]
    return "\n".join(l) + "\n"


def con_entrada(a: dict, grupos: list[dict]) -> list[dict]:
    """Los grupos del agente con su entrada en el primero, justo después de la instalación."""
    grupos = [dict(g, comandos=list(g["comandos"])) for g in grupos]
    grupos[0]["comandos"].insert(1, {"id": a["id"], "etiqueta": ENTRADA["es"][0].format(n=a["nombre"])})
    return grupos


# ---------------------------------------------------------------- la familia de una vez y su reloj

# El plugin de cada familia, criterio-<sigla>, no tiene agentes propios (decisión 0026): su setup y
# sus páginas salen de aquí, de los mismos agentes que publica Rostrum. Y el reloj (decisión 0028):
# lo que toca hoy, en una tarea programada que el setup ofrece al final y crea solo con un sí.
RELOJ = {"cron": "0 7 * * 1-5", "dice": "los días hábiles a las 7:00"}
# La versión de Claude Code desde la que instalar un plugin instala sus `dependencies`: probada con la
# 2.1.109, que instala solo el plugin de la familia, y con la 2.1.110, que instala sus agentes.
MIN_CLAUDE = "2.1.110"


def frente(plugin: str, comando: str) -> dict:
    texto = (P / plugin / "commands" / f"{comando}.md").read_text(encoding="utf-8")
    return {k.strip(): v.strip().strip('"') for k, _, v in
            (l.partition(":") for l in texto.split("\n---", 1)[0].splitlines()[1:]) if _}


def wake_de(a: dict) -> str:
    return next(c["id"] for g in a["grupos"] for c in g["comandos"] if c["id"].endswith("-wake"))


def y_es(xs: list[str]) -> str:
    return ", ".join(xs[:-1]) + " y " + xs[-1] if len(xs) > 1 else xs[0]


def reloj_md(agentes: list[dict], nombre: str, familia: bool) -> str:
    """El paso del reloj: una tarea programada para los agentes dados, con un sí explícito."""
    wakes = [f"/{a['plugin']}:{wake_de(a)}" for a in agentes]
    # Samuel y Alba son una instancia por proyecto y por producto: su reloj corre una vez por cada uno.
    dest = _raiz().DESTINO
    pasos = [w + (f" una vez por cada {dest[a['plugin']]['nivel']} configurado, con su código"
                  if dest.get(a["plugin"], {}).get("busca") == "caso" else "")
             for a, w in zip(agentes, wakes)]
    quien = y_es([a["nombre"] for a in agentes])
    herramientas = ["Skill"]
    for a in agentes:
        for h in frente(a["plugin"], wake_de(a)).get("allowed-tools", "").split(", "):
            if h and h not in herramientas:
                herramientas.append(h)
    instruccion = (f"En esta carpeta, corre {'en orden ' if len(pasos) > 1 else ''}{y_es(pasos)}. Solo procesa y escribe en el estado de "
                   "Criterio; no envíes nada. Si un paso necesita un permiso que no tienes, detente y déjalo dicho.")
    cron = (f'{RELOJ["cron"]} cd "<carpeta raíz>" && "<ruta de claude>" -p "{instruccion}" '
            f'--allowedTools "{",".join(herramientas)}" >> ".criterio/reloj/{nombre}.log" 2>&1')
    l = []
    if familia:
        l += [f"**6. El reloj, una tarea para la familia** ([decisión 0028](../../../docs/decisions/0028-el-setup-ofrece-el-reloj.md)).",
              "Solo con los agentes que quedaron configurados; los saltados no entran. Pregunta:"]
    else:
        l += ["## El reloj: lo que toca hoy, sin que nadie se acuerde", "",
              "**Si este setup corre dentro del de su familia, aquí no se ofrece nada:** la familia ofrece al final",
              "una sola tarea para todos sus agentes ([decisión 0028](../../../docs/decisions/0028-el-setup-ofrece-el-reloj.md)).",
              f"Si corre solo, pregunta:"]
    l += ["",
          f"> ¿Quieres que {quien} {'revisen' if len(agentes) > 1 else 'revise'} solo lo que toca cada día? Te propongo una tarea programada",
          f"> {RELOJ['dice']}: {'cada uno decide' if len(agentes) > 1 else 'decide'} según su frecuencia si le toca algo y, si no, se calla.",
          "> Solo procesa y escribe en el estado de Criterio; no envía nada.",
          "",
          "**Solo con un sí explícito**, y a la hora que la persona confirme o cambie. Según dónde corres:",
          "",
          "- **Si tienes una herramienta para crear tareas programadas** —en Cowork, la de las tareas",
          "  programadas de la app—, créala para la carpeta raíz, con la hora confirmada y esta instrucción:",
          f"  «{instruccion}»",
          "- **Si no** —Claude Code en una terminal—, usa el programador del equipo. Busca la ruta de Claude",
          "  con `which claude`, crea `.criterio/reloj/` en la carpeta raíz, muestra la línea completa y, con",
          "  un sí, agrégala a `crontab`. El equipo tiene que estar encendido a esa hora.",
          "",
          "  ```",
          f"  {cron}",
          "  ```",
          "",
          "**Después de cada versión nueva, la tarea se detiene** hasta que alguien acepte los términos de esa",
          "versión en una sesión con la persona presente: una aceptación por versión, nunca desatendida. Dilo",
          "al crearla.",
          "",
          f"**Si la persona dice que no**, di en una línea cómo se corre a mano: {y_es([f'`{w}`' for w in wakes])}.",
          ("Y en la tabla del final, una fila más: la tarea, con su hora y dónde quedó, o «sin reloj»." if familia else
           "Y en la salida, en «Cuándo vuelvo», di si quedó la tarea, a qué hora y dónde, o «sin reloj».")]
    return "\n".join(l)


PMO_INSTANCIAS = """
**En la PMO, Samuel y Alba son una instancia por proyecto y por producto.** Después de Vera, pregunta
una sola vez por cuáles proyectos y cuáles productos quiere la persona configurar ahora, con la lista
que encontró Vera, y corre el setup de Samuel o de Alba una vez por cada uno. «Ninguno por ahora» es
una respuesta válida: se configuran después, cuando se necesiten.
"""


def familia_setup_md(sigla: str, agentes: list[dict]) -> str:
    S = sigla.upper()
    nombres = [a["nombre"] for a in agentes]
    lineas = "\n".join(f"{i}. **{a['nombre']}** — `{a['setup']}`" for i, a in enumerate(agentes, 1))
    return f"""---
description: Configura la familia {S} de una vez — {y_es(nombres)} — en una sola conversación, con lo común preguntado una sola vez
argument-hint: "[ruta de la carpeta] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-{sigla}/familia.json por scripts/familias.py; no se edita a mano -->

# /{sigla}-setup — La familia {S}, de una vez

Instalar `criterio-{sigla}` instaló a {y_es([f"{a['nombre']} (`{a['plugin']}`)" for a in agentes])}, y a Rostrum
(`criterio-server`). Este comando los deja listos en una sola conversación: lo que comparten se
pregunta una vez, y cada agente pregunta solo lo suyo.

**Este comando no escribe ninguna configuración.** La de cada agente la escribe su propio setup,
con su motor y sus validaciones. Aquí solo se ordena el recorrido.

## Flujo

**0. Preséntate, en una línea.**

> Vamos a dejar lista la familia {S}: {"; ".join(f"{a['nombre']}, {a['titulo']}" for a in agentes)}. Lo que comparten te lo pregunto una sola vez.

**1. Corre el setup de cada agente, en este orden**, uno después del otro y en esta misma conversación:

{lineas}

Invócalos tú, con la herramienta que corre los comandos. Si no puedes invocar un comando, dile a la
persona exactamente cuál escribir y espera a que termine. Si el argumento trae una ruta, pásasela
al primero.

**Si el setup de un agente no existe, el agente no está instalado**: casi siempre es un Claude Code
anterior a la {MIN_CLAUDE}, que instala el plugin de la familia sin sus agentes. Dilo en una línea, con
las dos salidas —actualizar con `claude update`, fuera de Claude, o instalar ese agente con
`/plugin install <su plugin>@criterio`— y sigue con el siguiente.
{PMO_INSTANCIAS if sigla == "pmo" else ""}
**2. Lo que ya se respondió no se vuelve a preguntar.** El primer setup encuentra la carpeta, la
entidad y dónde guardar el estado. Antes de cada setup siguiente, di en una línea lo que ya quedó
fijado: ese setup lo toma de la conversación y solo pide confirmarlo.

**3. Los términos los muestra cada setup.** No los resumas, no los agrupes y no los aceptes por la
persona: cada agente pide su propio sí.

**4. Si la persona no quiere uno de los agentes, sáltalo.** Cada agente funciona solo. Dilo en una
línea y sigue con el siguiente.

**5. Al final, la familia en una tabla:** una fila por agente —configurado o saltado— con el primer
resultado que mostró su setup, en sus palabras. Y el siguiente paso, en una línea: para verlo fuera de
la conversación, `/criterio-server:server-setup` publica lo de la familia en Rostrum.

{reloj_md(agentes, sigla, True)}
"""


def familia_readme(fa: dict, agentes: list[dict], i: str) -> str:
    s, S = fa["sigla"], fa["sigla"].upper()
    multi = len(agentes) > 1
    setup = f"/criterio-{s}:{s}-setup" if multi else agentes[0]["setup"]
    adr = "../../docs/decisions/0026-una-familia-se-instala-de-una-vez.md"
    if i == "es":
        filas = "\n".join(f"| **{a['nombre']}** | {a['titulo']} | `{a['plugin']}` | `{a['setup']}` |" for a in agentes)
        despues = (f"Después, un solo comando los configura a todos en la misma conversación:\n\n```\n{setup}\n```\n\n"
                   "Corre el setup de cada agente en orden y pregunta una sola vez lo que comparten —la carpeta, la entidad y dónde\n"
                   "se guarda el estado—. Los términos los muestra cada agente, y cada uno pide su propio sí. Al final ofrece una\n"
                   "tarea programada para lo que toca cada día, y la crea solo con un sí.\n\n"
                   f"| Comando | Qué hace |\n|---|---|\n| `{setup}` | Configura la familia de una vez: corre el setup de cada agente en orden, con lo común preguntado una sola vez |\n"
                   if multi else f"Después, su setup:\n\n```\n{setup}\n```\n")
        return f"""# Criterio {S} · {fa['nombre']['es']} · la familia completa

[English](README.md) · `criterio-{s}` · Apache 2.0

**Instala la familia {S} de una vez.** Este plugin no tiene agentes propios: trae como
dependencias a los de la familia y a Rostrum, el portal de todas las familias
([ADR 0026]({adr})).

| Agente | De qué responde | Plugin | Su setup |
|---|---|---|---|
{filas}
| **Rostrum** | el portal de todas las familias | `criterio-server` | `/criterio-server:server-setup` |

## Instalación

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-{s}@criterio
```

Necesita Claude Code {MIN_CLAUDE} o posterior: antes, se instala solo este plugin, sin sus agentes, y no
avisa. Si algo falla, [la instalación paso a paso](../../docs/instalacion.es.md).

{despues}
**El primer resultado** lo da el setup de cada agente, sobre tus propios documentos, antes de terminar.

**Lo que nunca hace.** No escribe ninguna configuración: la de cada agente la escribe su propio
setup. No acepta los términos por nadie: cada agente los muestra y pide su propio sí. Y no agrega
nada a lo que cada agente hace o se niega a hacer: lo que cada uno nunca hace está en su página.

**¿Solo necesitas un agente?** Instálalo solo, con su plugin: la familia no hace falta. Todo lo de
cada agente —qué hace, qué no hace, sus comandos y sus pruebas— está en su página y en la
[familia {S}](../../families/criterio-{s}/README.es.md).
"""
    filas = "\n".join(f"| **{a['nombre']}** | `{a['plugin']}` | `{a['setup']}` |" for a in agentes)
    despues = (f"Then one command sets them all up in the same conversation:\n\n```\n{setup}\n```\n\n"
               "It runs each agent's setup in order and asks only once what they share —the folder, the entity and where\n"
               "the state is kept—. Each agent shows its own terms and asks for its own yes. At the end it offers a scheduled\n"
               "task for what is due each day, and creates it only with a yes.\n\n"
               f"| Command | What it does |\n|---|---|\n| `{setup}` | Sets the family up at once: runs each agent's setup in order, asking only once what they share |\n"
               if multi else f"Then its setup:\n\n```\n{setup}\n```\n")
    return f"""# Criterio {S} · {fa['nombre']['en']} · the whole family

[Español](README.es.md) · `criterio-{s}` · Apache 2.0

**Install the {S} family at once.** This plugin has no agents of its own: it brings the
family's agents and Rostrum, the portal for every family, as dependencies
([ADR 0026]({adr})).

| Agent | Plugin | Its setup |
|---|---|---|
{filas}
| **Rostrum** | `criterio-server` | `/criterio-server:server-setup` |

## Install

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-{s}@criterio
```

It needs Claude Code {MIN_CLAUDE} or later: before it, only this plugin installs, without its agents,
and it says nothing. If something fails, [the installation step by step](../../docs/instalacion.md).

{despues}
**The first result** comes from each agent's setup, on your own documents, before it finishes.

**What it never does.** It writes no configuration: each agent's own setup writes its own. It
accepts the terms for nobody: each agent shows them and asks for its own yes. And it adds nothing
to what each agent does or refuses to do: what each one never does is on its page.

**Only need one agent?** Install it on its own, with its plugin: the family is not needed. Everything
about each agent —what it does, what it does not, its commands and its tests— is on its page and in
the [{S} family](../../families/criterio-{s}/README.md).
"""


def poner_reloj(texto: str, contenido: str, ruta: Path) -> str:
    """El bloque del reloj en el setup de un agente: antes de registrar la corrida, que va al final."""
    pre, fin = "<!-- reloj · ", "<!-- /reloj -->"
    bloque = f"{pre}generado por scripts/familias.py; no se edita a mano -->\n{contenido}\n{fin}\n\n"
    if pre in texto:
        a = texto.index(pre)
        b = texto.index(fin, a) + len(fin)
        b = b + 2 if texto[b:b + 2] == "\n\n" else b
        return texto[:a] + bloque + texto[b:]
    ancla = "## Deja la corrida registrada"
    if ancla not in texto:
        raise SystemExit(f"{ruta.relative_to(RAIZ)}: falta «{ancla}», donde va el reloj")
    a = texto.index(ancla)
    return texto[:a] + bloque + texto[a:]


# ---------------------------------------------------------------- los agentes, para Rostrum

SERVIDOR = {"id": "rostrum", "nombre": "Rostrum", "plugin": "criterio-server", "area": "rostrum",
            "rol": {"es": "El portal", "en": "The portal"}, "titulo": "el portal",
            "origen": {"es": "del latín *rostrum*, la tribuna del foro romano: sostiene lo que ya está escrito, donde otros puedan leerlo",
                       "en": "from the Latin *rostrum*, the speakers’ platform of the Roman forum: it holds up what is already written, where others can read it"},
            "grupos": [{"titulo": "El portal", "linea": "El mapa de las familias y el servidor que las publica",
                        "comandos": [{"id": "server-setup", "etiqueta": "El mapa de las familias"},
                                     {"id": "server-start", "etiqueta": "Levantar el portal"},
                                     {"id": "server-demo", "etiqueta": "La demostración"}]}]}


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
                # Como en la PMO: arranque y ritmo (el setup y el reloj), el oficio, y compartir.
                por_n = sorted(a["comandos"], key=lambda c: c["n"])
                et = lambda c: {"id": c["id"], "etiqueta": c["es"]["etiqueta"]}
                ritmo = [por_n[0]] + [c for c in por_n if c["id"].endswith("-wake")]
                compartir = [c for c in por_n if c["id"] == "share-findings"]
                oficio = [c for c in por_n if c not in ritmo and c not in compartir]
                grupos = [{"titulo": "Arranque y ritmo", "linea": "Instalar y saber qué toca hoy",
                           "comandos": [et(c) for c in ritmo]},
                          {"titulo": a["rol"]["es"], "linea": a["hace"]["es"], "comandos": [et(c) for c in oficio]}]
                if compartir:
                    grupos.append({"titulo": "Compartir", "linea": "Un resumen sin datos de lo que corrió, solo si dices que sí",
                                   "comandos": [et(c) for c in compartir]})
            # El setup y la marca de su carpeta raíz son de raiz.py (ADR 0011): aquí solo se copian,
            # para que Rostrum y el portal digan cómo entra cada agente al mapa sin escribirlo a mano.
            dest = _raiz().DESTINO.get(a["plugin"]) or {}
            agentes.append({"id": a["id"], "nombre": a["nombre"], "plugin": a["plugin"], "area": a["area"],
                            "ambitos": a.get("ambitos") or [], "familia": sigla, "rol": a["rol"], "titulo": a.get("titulo") or a["rol"]["es"].lower(),
                            "origen": a.get("origen"),
                            # Lo que no se publica en Rostrum salvo que la configuración lo diga (ADR 0019): el
                            # comando, la clave de la configuración que lo abre y las señales que no se muestran.
                            "privados": {c["id"]: c["privado"] for c in a.get("comandos") or [] if c.get("privado")},
                            "setup": dest.get("setup"), "marca": dest.get("marca"), "grupos": con_entrada(a, grupos)})
    for a in agentes + [SERVIDOR]:
        if not all((a.get("origen") or {}).get(i) for i in ("es", "en")):
            err.append(f"{a['nombre']}: falta de dónde viene su nombre (origen, en los dos idiomas)")
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


def nombre_md(a: dict, i: str) -> str:
    """De dónde viene el nombre del agente, en su README: sale de su familia.json (o, para
    Rostrum, de SERVIDOR), que es la misma fuente de la página de su familia y del portal."""
    return (f"**El nombre.** {a['nombre']}, {a['origen']['es']}." if i == "es"
            else f"**The name.** {a['nombre']}, {a['origen']['en']}.")


def nombres_readme(check: bool) -> list[str]:
    """El bloque «El nombre» del README de cada agente de cada familia, y del de Rostrum."""
    err = []
    CLAVE[0] = "agente"
    for a in [x for fa in todas() if construida(fa) for x in fa["agentes"]] + [SERVIDOR]:
        if not all((a.get("origen") or {}).get(i) for i in ("es", "en")):
            continue
        for nombre, i in (("README.es.md", "es"), ("README.md", "en")):
            ruta = P / a["plugin"] / nombre
            if not ruta.is_file():
                continue
            actual = ruta.read_text(encoding="utf-8")
            nuevo = poner(actual, "nombre", nombre_md(a, i), ruta)
            if nuevo != actual:
                if check:
                    err.append(f"{ruta.relative_to(RAIZ)}: el nombre no es el de su familia.json; corre scripts/familias.py")
                else:
                    ruta.write_text(nuevo, encoding="utf-8")
                    print(f"  {ruta.relative_to(RAIZ)}")
    return err


def revisar_nivel_c() -> list[str]:
    """Lo que hace cada familia para quien dirige la función (`nivel_c` de su familia.json), que el
    portal publica en «Qué hace»: en los dos idiomas, y cada fuente que cita existe y está verificada."""
    errores = []
    for f in sorted((RAIZ / "families").glob("criterio-*/familia.json")):
        fam = json.loads(f.read_text(encoding="utf-8"))
        if not construida(fam):
            continue
        n = fam.get("nivel_c")
        s = f.parent.name
        if not n:
            errores.append(f"{s}: familia.json no trae `nivel_c`, lo que hace la familia para el nivel C")
            continue
        fu = f.parent / "fuentes.json"
        estado = {x["id"]: x.get("estado") for sec in json.loads(fu.read_text(encoding="utf-8"))["secciones"]
                  for x in sec.get("fuentes", []) if "id" in x} if fu.exists() else {}
        if not (n.get("para", {}).get("es") and n.get("para", {}).get("en")):
            errores.append(f"{s}: `nivel_c.para` sin los dos idiomas")
        if not n.get("con"):
            errores.append(f"{s}: `nivel_c.con` vacío: con qué trabaja la familia")
        for x in n.get("con", []):
            if len(x.get("es", [])) != 2 or len(x.get("en", [])) != 2:
                errores.append(f"{s}: `nivel_c.con` con una entrada sin título y texto en los dos idiomas")
            for i in x.get("fuentes", []):
                if estado.get(i) != "verificada":
                    errores.append(f"{s}: `nivel_c` cita {i}, que no está verificada en fuentes.json")
    return errores


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
    # La versión mínima de Claude Code se escribe en varias páginas; todas dicen la de MIN_CLAUDE.
    for pag in [RAIZ / "README.es.md", RAIZ / "README.md", *sorted((RAIZ / "families").glob("criterio-*/README*.md")),
                *sorted((RAIZ / "docs" / "decisions").glob("*.md")), RAIZ / "docs" / "instalacion.es.md", RAIZ / "docs" / "instalacion.md"]:
        for v in re.findall(r"Claude Code (\d+\.\d+\.\d+) (?:o posterior|or later)", pag.read_text(encoding="utf-8")):
            if v != MIN_CLAUDE:
                errores.append(f"{pag.relative_to(RAIZ)} pide Claude Code {v} y la mínima es la {MIN_CLAUDE}")
    errores += [f"NOMBRES · {e}" for e in nombres_readme(args.check)]
    errores += [f"NIVEL C · {e}" for e in revisar_nivel_c()]
    destino = P / "criterio-server" / "scripts" / "agentes.json"
    if destino.parent.is_dir():
        actual = destino.read_text(encoding="utf-8") if destino.exists() else ""
        if actual != contenido:
            if args.check:
                errores.append(f"{destino.relative_to(RAIZ)}: no es lo que sale de las familias; corre scripts/familias.py")
            else:
                destino.write_text(contenido, encoding="utf-8")
                print(f"  {destino.relative_to(RAIZ)}")
    reg = json.loads(contenido)
    # La entrada de cada agente, desde lo mismo que publica Rostrum.
    for a in reg["agentes"]:
        ruta = P / a["plugin"] / "commands" / f"{a['id']}.md"
        nuevo = entrada_md(a, [x for x in reg["agentes"] if x["familia"] == a["familia"]])
        actual = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
        if actual != nuevo:
            if args.check:
                errores.append(f"{ruta.relative_to(RAIZ)}: no es lo que sale de las familias; corre scripts/familias.py")
            else:
                ruta.write_text(nuevo, encoding="utf-8")
                print(f"  {ruta.relative_to(RAIZ)}")
    # La familia de una vez (decisión 0026) y el reloj de cada agente (decisión 0028).
    for fa in todas():
        if not construida(fa):
            continue
        agentes = [x for x in reg["agentes"] if x["familia"] == fa["sigla"]]
        base = P / f"criterio-{fa['sigla']}"
        salidas = []
        if base.is_dir():
            salidas += [(base / "README.es.md", familia_readme(fa, agentes, "es")),
                        (base / "README.md", familia_readme(fa, agentes, "en"))]
            if len(agentes) > 1:
                salidas.append((base / "commands" / f"{fa['sigla']}-setup.md", familia_setup_md(fa["sigla"], agentes)))
        for a in agentes:
            ruta = P / a["plugin"] / "commands" / f"{a['setup'].split(':')[1]}.md"
            salidas.append((ruta, poner_reloj(ruta.read_text(encoding="utf-8"), reloj_md([a], a["id"], False), ruta)))
        for ruta, nuevo in salidas:
            actual = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
            if actual != nuevo:
                if args.check:
                    errores.append(f"{ruta.relative_to(RAIZ)}: no es lo que sale de las familias; corre scripts/familias.py")
                else:
                    ruta.parent.mkdir(parents=True, exist_ok=True)
                    ruta.write_text(nuevo, encoding="utf-8")
                    print(f"  {ruta.relative_to(RAIZ)}")
    # En el README de Rostrum, cómo entra cada familia al mapa: sale de las mismas familias.
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
