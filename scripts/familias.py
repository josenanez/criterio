#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El diseño de las familias CFO y CLO, escrito desde sus tres fuentes.

    python3 scripts/familias.py           escribe FUENTES.es.md, las tablas de DISENO.es.md, los
                                          bloques de los README y del skill de documentos de cada
                                          plugin, y la estructura que usa el motor
    python3 scripts/familias.py --check   falla si alguna copia no sale de las fuentes, o si las
                                          fuentes no cuadran entre sí

Cada familia tiene tres fuentes en families/criterio-<familia>/, y cada cosa tiene una sola:
  fuentes.json    las fuentes técnicas, normativas y las cifras de terceros, con su estado
  carpetas.json   la estructura de carpetas recomendada (ADR 0007)
  familia.json    los agentes, sus comandos con entrada, proceso y reporte, y sus señales

El portal las publica con scripts/criterio-cfo.mjs y scripts/criterio-clo.mjs. Lo que comprueba
además de las copias: que cada carpeta citada por un comando exista en la estructura, que cada
fuente citada por un comando esté verificada (ADR 0006, regla 1), que cada campo que lee un motor
esté verificado en su fuente y que la numeración vaya de diez en diez.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
AVISO = "generado por scripts/familias.py; no se edita a mano"
P = RAIZ / "plugins"

# Lo que cambia de una familia a otra. Todo lo demás es igual.
FAMILIAS = {
    "cfo": {
        "dir": RAIZ / "families" / "criterio-cfo", "adr": "0006-scope-cfo.md",
        "cifras_en": "clara",
        "intake": (P / "criterio-finance" / "skills" / "finance-intake" / "SKILL.md",
                   "La contabilidad del periodo tiene un solo lugar, `10-contabilidad/`: Clara la cierra y "
                   "Tomás saca de ahí la ejecución."),
        "estructuras": ["criterio-finance", "criterio-budget"],
        "motor": P / "criterio-finance" / "scripts" / "finanzas.py",
        "lectores": {"CAMPOS_DIAN": ["F-01"], "CAMPOS_SRI": ["F-04", "F-09"]},
    },
    "clo": {
        "dir": RAIZ / "families" / "criterio-clo", "adr": "0009-scope-clo.md",
        "cifras_en": "fidel",
        "intake": (P / "criterio-legal" / "skills" / "legal-intake" / "SKILL.md",
                   "Cada contrato tiene un solo lugar, su carpeta en `contratos/`: Fidel la procesa y Constanza "
                   "toma de su ficha las obligaciones de cumplimiento."),
        "estructuras": ["criterio-legal", "criterio-compliance"],
        "motor": P / "criterio-legal" / "scripts" / "legal.py",
        "lectores": {},
    },
}
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


def comandos_readme(a: dict, i: str) -> str:
    cab = "| # | Comando | Qué entrega |" if i == "es" else "| # | Command | What it delivers |"
    l = [cab, "|---|---|---|"]
    l += [f"| {c['n']} | `/{a['plugin']}:{c['id']}` | {celda(c[i]['entrega'] if i == 'en' else c['es']['entrega'])} |" for c in a["comandos"]]
    return "\n".join(l)


def skills_readme(base: Path) -> str:
    nombres = sorted(d.name for d in (base / "skills").iterdir() if (d / "SKILL.md").is_file()) if (base / "skills").is_dir() else []
    return " · ".join(f"`{n}`" for n in nombres)


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
            if not c["en"].get("entrega"):
                err.append(f"{c['id']}: le falta la entrega en inglés")
            texto = " ".join(c["es"].values())
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
    return err


def revisar_campos(fu: dict) -> list[str]:
    """Cada campo de factura que procesa el motor tiene que estar verificado en su fuente (ADR 0006, regla 2)."""
    if not F["motor"].is_file() or not F["lectores"]:
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
    F.update(FAMILIAS[clave])
    CLAVE[0] = clave
    if not (F["dir"] / "familia.json").is_file():
        return [], 0, 0
    fu, ca, fa = cargar("fuentes.json"), cargar("carpetas.json"), cargar("familia.json")
    errores = revisar(fu, ca, fa)
    diseno = F["dir"] / "DISENO.es.md"
    salidas: list[tuple[Path, str]] = [(F["dir"] / "FUENTES.es.md", fuentes_md(fu))]
    d = diseno.read_text(encoding="utf-8")
    for nombre, contenido in (("agentes", agentes_md(fa)), ("carpetas", carpetas_md(ca, fa)),
                              ("senales", senales_md(fa)), ("cifras", cifras_diseno(fu))):
        d = poner(d, nombre, contenido, diseno)
    for a in fa["agentes"]:
        d = poner(d, f"comandos-{a['id']}", comandos_md(a), diseno)
    salidas.append((diseno, d))
    for a in fa["agentes"]:
        base = P / a["plugin"]
        for nombre, i in (("README.es.md", "es"), ("README.md", "en")):
            ruta = base / nombre
            if not ruta.is_file():
                continue
            t = poner(ruta.read_text(encoding="utf-8"), "comandos", comandos_readme(a, i), ruta)
            t = poner(t, "skills", skills_readme(base), ruta)
            if a["id"] == F["cifras_en"]:
                t = poner(t, "cifras", cifras_readme(fu, i), ruta)
            salidas.append((ruta, t))
    intake = F["intake"][0]
    if intake.is_file():
        salidas.append((intake, poner(intake.read_text(encoding="utf-8"), "intake", intake_md(ca, fa), intake)))
    for p in F["estructuras"]:
        ruta = P / p / "scripts" / "estructura.json"
        if ruta.parent.is_dir():
            salidas.append((ruta, estructura_json(ca)))
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
    for e in errores:
        print(f"  ✗ {e}")
    if args.check and not errores:
        print(f"  las familias cuadran: {' · '.join(resumen)}, cada carpeta y cada fuente en su lugar")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
