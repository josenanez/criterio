#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El diseño de la familia CFO, escrito desde sus tres fuentes.

    python3 scripts/cfo.py           escribe FUENTES.es.md, las tablas de DISENO.es.md y las cifras
                                     de los README de criterio-finance
    python3 scripts/cfo.py --check   falla si alguna copia no sale de las fuentes, o si las fuentes
                                     no cuadran entre sí

Las fuentes son tres, en families/criterio-cfo/, y cada cosa tiene una sola:
  fuentes.json    las fuentes técnicas, normativas y las cifras de terceros, con su estado
  carpetas.json   la estructura de carpetas recomendada (ADR 0007)
  familia.json    los agentes, sus comandos con entrada, proceso y reporte, y sus señales

El portal publica las mismas tres con scripts/criterio-cfo.mjs. Lo que comprueba además de las
copias: que cada carpeta citada por un comando exista en la estructura, que cada fuente citada
por un comando esté verificada (ADR 0006, regla 1) y que la numeración vaya de diez en diez.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CFO = RAIZ / "families" / "criterio-cfo"
DISENO = CFO / "DISENO.es.md"
FUENTES_MD = CFO / "FUENTES.es.md"
README_FINANCE = [(RAIZ / "plugins" / "criterio-finance" / "README.es.md", "es"),
                  (RAIZ / "plugins" / "criterio-finance" / "README.md", "en")]
AVISO = "generado por scripts/cfo.py; no se edita a mano"


def cargar(nombre: str) -> dict:
    return json.loads((CFO / nombre).read_text(encoding="utf-8"))


def marcas(nombre: str) -> tuple[str, str]:
    return f"<!-- cfo:{nombre} · {AVISO} -->", f"<!-- /cfo:{nombre} -->"


def poner(texto: str, nombre: str, contenido: str, ruta: Path) -> str:
    ini, fin = marcas(nombre)
    if ini not in texto or fin not in texto:
        raise SystemExit(f"{ruta.relative_to(RAIZ)}: faltan las marcas de «{nombre}»")
    a = texto.index(ini)
    b = texto.index(fin, a) + len(fin)
    return texto[:a] + f"{ini}\n{contenido}\n{fin}" + texto[b:]


def celda(s: str) -> str:
    return s.replace("|", "\\|")


# ---------------------------------------------------------------- las fuentes

def estado(f: dict) -> str:
    e = "Verificada" if f["estado"] == "verificada" else "Por verificar"
    return f"{e}: {f['nota']}" if f.get("nota") else e


def fuentes_md(fu: dict) -> str:
    l = ["# criterio-cfo · las fuentes", "",
         f"<!-- {AVISO}, desde fuentes.json -->", "",
         "Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la",
         "fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el",
         "material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en",
         "[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/cfo.py`.", "",
         "**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se",
         "conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre",
         "ella hasta verificarla ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 1).", ""]
    for s in fu["secciones"]:
        l += [f"## {s['titulo']}", "",
              "| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |", "|---|---|---|---|---|---|---|"]
        for f in s["fuentes"]:
            enl = " · ".join(f"[{t}]({u})" for t, u in f["enlaces"])
            l.append(f"| {f['id']} | {celda(f['fuente'])} | {celda(f['version'])} | {enl} | {f['consultada']} "
                     f"| {celda(estado(f))} | {celda(f['uso'])} |")
        l.append("")
    l += ["## Cifras de terceros", "",
          "| Id | Cifra | Fuente | Año | Muestra | Estado |", "|---|---|---|---|---|---|"]
    for c in fu["cifras"]:
        l.append(f"| {c['id']} | **{c['valor']['es']}** {celda(c['cifra']['es'])} | [{celda(c['fuente'])}]({c['enlace']}) "
                 f"| {c['anio']} | {celda(c['muestra']['es'])} | {celda(estado(c))} |")
    l += ["", "## Cómo se agrega una fuente", "",
          "1. Se agrega en `fuentes.json` con el siguiente identificador libre —F-01 a F-09 para fuentes",
          "   técnicas y normativas, desde F-10 para cifras de terceros— y la fila entera: versión, enlace",
          "   al emisor, fecha de consulta, estado y uso. Después se corre `python3 scripts/cfo.py`.",
          "2. Mientras diga «por verificar», nada se construye sobre ella: la puerta falla si un comando",
          "   la cita.",
          "3. Cuando una fuente cambia de versión, se agrega la nueva fila y la anterior se marca como",
          "   reemplazada, sin borrarla: el material de prueba generado con ella sigue citándola.", ""]
    return "\n".join(l)


def cifras_diseno(fu: dict) -> str:
    ver = [c for c in fu["cifras"] if c["estado"] == "verificada"]
    pend = [c for c in fu["cifras"] if c["estado"] != "verificada"]
    ids = ", ".join(f"{c['id']} ({c['fuente'].split(',')[0]})" for c in ver)
    t = (f"Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). "
         f"Verificadas: {ids}.")
    if pend:
        t += " Por verificar, y fuera de cualquier publicación hasta verificarse: " + ", ".join(c["id"] for c in pend) + "."
    return t


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

def agentes_md(fa: dict) -> str:
    l = ["| Rol | Agente | Plugin | Qué hace |", "|---|---|---|---|"]
    for a in fa["agentes"]:
        l.append(f"| {a['rol']['es']} | **{a['nombre']}** — {a['origen']['es']} | `{a['plugin']}` | {a['hace']['es']} |")
    return "\n".join(l)


def senales_md(fa: dict) -> str:
    l = []
    for a in fa["agentes"]:
        l += [f"**{a['nombre']} · {a['rol']['es']}**", "", "| Señal | Se levanta cuando |", "|---|---|"]
        l += [f"| `{s['id']}` | {celda(s['es'])} |" for s in a["senales"]]
        l.append("")
    return "\n".join(l).rstrip()


def comandos_md(a: dict) -> str:
    l = ["| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |", "|---|---|---|---|---|"]
    for c in a["comandos"]:
        e = c["es"]
        l.append(f"| {c['n']} | `{c['id']}` | {celda(e['entrada'])} | {celda(e['proceso'])} | {celda(e['reporte'])} |")
    return "\n".join(l)


def carpetas_md(ca: dict, fa: dict) -> str:
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
    l = [ca["raiz"]["es"], "", "```", *arbol, "```", ""]
    for n in niveles:
        l += [f"**`{n['carpeta']}`** · {n['es']}", "", "| Carpeta | Qué va | Agente |", "|---|---|---|"]
        for c in n["carpetas"]:
            l.append(f"| `{c['carpeta']}/` | {celda(c['es'])} | {', '.join(nombres[x] for x in c['agentes'])} |")
        l.append("")
    l.append(f"**`{ca['estado']['carpeta']}`** · {ca['estado']['es']}.")
    return "\n".join(l)


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
        n = int(f["id"][2:])
        if (f in fu["cifras"]) != (n >= 10):
            err.append(f"{f['id']}: F-01 a F-09 son fuentes y desde F-10 son cifras")
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
    niveles = {nv["carpeta"].rstrip("/") for nv in ca["niveles"]}
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
            if not c["en"].get("entrega"):
                err.append(f"{c['id']}: le falta la entrega en inglés")
            texto = " ".join(c["es"].values())
            for tok in re.findall(r"`([^`]+)`", texto):
                cabeza = tok.split("/")[0]
                if re.match(r"\d\d-", cabeza) and cabeza not in numeradas:
                    err.append(f"{c['id']}: cita `{tok}` y esa carpeta no está en carpetas.json")
                if cabeza.startswith("presupuesto-") and cabeza not in niveles:
                    err.append(f"{c['id']}: cita `{tok}` y ese nivel no está en carpetas.json")
            for fid in re.findall(r"F-\d\d", texto):
                if fid not in por_id:
                    err.append(f"{c['id']}: cita {fid} y no está en fuentes.json")
                elif por_id[fid]["estado"] != "verificada":
                    err.append(f"{c['id']}: se apoya en {fid}, que está por verificar (ADR 0006, regla 1)")
    return err


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    fu, ca, fa = cargar("fuentes.json"), cargar("carpetas.json"), cargar("familia.json")
    errores = revisar(fu, ca, fa)

    salidas: list[tuple[Path, str]] = [(FUENTES_MD, fuentes_md(fu))]
    d = DISENO.read_text(encoding="utf-8")
    for nombre, contenido in (("agentes", agentes_md(fa)), ("carpetas", carpetas_md(ca, fa)),
                              ("senales", senales_md(fa)), ("cifras", cifras_diseno(fu))):
        d = poner(d, nombre, contenido, DISENO)
    for a in fa["agentes"]:
        d = poner(d, f"comandos-{a['id']}", comandos_md(a), DISENO)
    salidas.append((DISENO, d))
    for ruta, i in README_FINANCE:
        salidas.append((ruta, poner(ruta.read_text(encoding="utf-8"), "cifras", cifras_readme(fu, i), ruta)))

    for ruta, nuevo in salidas:
        actual = ruta.read_text(encoding="utf-8") if ruta.exists() else ""
        if nuevo == actual:
            continue
        if args.check:
            errores.append(f"{ruta.relative_to(RAIZ)}: no es lo que sale de las fuentes; corre scripts/cfo.py")
        else:
            ruta.write_text(nuevo, encoding="utf-8")
            print(f"  {ruta.relative_to(RAIZ)}")
    for e in errores:
        print(f"  ✗ {e}")
    if args.check and not errores:
        n = sum(len(a["comandos"]) for a in fa["agentes"])
        print(f"  la familia CFO cuadra: {n} comandos, {len(salidas)} archivos, cada carpeta y cada fuente en su lugar")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
