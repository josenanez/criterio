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
    """Los agentes de todas las familias, en el orden de la PMO, la CFO y la CLO."""
    err, familias, agentes = [], [], []
    for sigla in ("pmo", "cfo", "clo"):
        f = RAIZ / "families" / f"criterio-{sigla}" / "familia.json"
        if not f.is_file():
            continue
        fa = json.loads(f.read_text(encoding="utf-8"))
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
    for sigla in ("pmo", "cfo", "clo"):
        f = RAIZ / "families" / f"criterio-{sigla}" / "familia.json"
        if f.is_file():
            err += revisar_impresora(sigla, json.loads(f.read_text(encoding="utf-8")))
    areas = [a["area"] for a in agentes]
    if len(areas) != len(set(areas)):
        err.append("dos agentes con la misma área")
    # El nombre de cada señal, para que Rostrum la diga en palabras y no en código.
    senales = {}
    for sigla in ("cfo", "clo"):
        f = RAIZ / "families" / f"criterio-{sigla}" / "familia.json"
        if f.is_file():
            for a in json.loads(f.read_text(encoding="utf-8"))["agentes"]:
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
