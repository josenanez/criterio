#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-portfolio/scripts/raiz.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
"""Criterio — la carpeta raíz de cada agente: encontrarla y marcarla.

    python3 raiz.py buscar --plugin <plugin> [--desde <carpeta>]
    python3 raiz.py marcar --plugin <plugin> --carpeta <raíz> --entidad "<nombre>" --por "<nombre>"
    python3 raiz.py leer   --plugin <plugin> --carpeta <raíz>
    python3 raiz.py --selftest

Quien instala un agente casi nunca sabe cuál de sus carpetas es «la carpeta de documentos», y
escribir una ruta a mano es donde más se equivoca. Así que el setup no la pide: **la busca**.
Recorre la carpeta de trabajo hacia abajo y propone las candidatas numeradas, cada una con la
evidencia de por qué parece ser —«tiene `00-referencia/` y tres periodos»—, y la persona elige
un número.

Una vez elegida, y **solo si la persona lo autoriza**, la carpeta queda marcada con un archivo de
texto visible, `_CRITERIO_<QUÉ>.txt`. El guion bajo lo pone primero en la carpeta; el texto dice de
qué agentes es, de qué entidad o caso y que no se mueva. Es lo único que un agente deja dentro de
los documentos de la organización (ADR 0011, que modifica la 0007): ningún inventario lo cuenta
como documento, y borrarlo no pierde nada, solo la marca. La próxima búsqueda la encuentra
primero, con certeza.

La fuente vive en criterio-portfolio y `scripts/sincronizar.py` la copia a todos los plugins.
Librería estándar, sin dependencias.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREFIJO = "_CRITERIO_"

# Qué busca cada plugin y cómo marca lo que encuentra. `busca`: «raiz» es la carpeta que contiene
# la estructura —la del portafolio, la de una entidad—; «caso», una carpeta de un proyecto o de un
# producto. El nivel es el de `estructura.json` cuyas carpetas la identifican.
DESTINO = {
    "criterio-portfolio": {"familia": "pmo", "busca": "raiz", "marca": "_CRITERIO_PORTAFOLIO.txt",
                           "que": "la carpeta del portafolio de proyectos", "agentes": "Vera",
                           "setup": "/criterio-portfolio:portfolio-setup"},
    "criterio-project": {"familia": "pmo", "busca": "caso", "nivel": "proyecto", "marca": "_CRITERIO_PROYECTO.txt",
                         "que": "la carpeta de un proyecto", "agentes": "Samuel",
                         "setup": "/criterio-project:pm-setup"},
    "criterio-product": {"familia": "pmo", "busca": "caso", "nivel": "producto", "marca": "_CRITERIO_PRODUCTO.txt",
                         "que": "la carpeta de un producto", "agentes": "Alba",
                         "setup": "/criterio-product:product-setup"},
    "criterio-finance": {"familia": "cfo", "busca": "raiz", "marca": "_CRITERIO_FINANZAS.txt",
                         "que": "la carpeta de finanzas de una entidad", "agentes": "Clara y Tomás",
                         "setup": "/criterio-finance:finance-setup"},
    "criterio-budget": {"familia": "cfo", "busca": "raiz", "marca": "_CRITERIO_FINANZAS.txt",
                        "que": "la carpeta de finanzas de una entidad", "agentes": "Clara y Tomás",
                        "setup": "/criterio-budget:budget-setup"},
    "criterio-legal": {"familia": "clo", "busca": "raiz", "marca": "_CRITERIO_LEGAL.txt",
                       "que": "la carpeta legal de una entidad", "agentes": "Fidel y Constanza",
                       "setup": "/criterio-legal:legal-setup"},
    "criterio-compliance": {"familia": "clo", "busca": "raiz", "marca": "_CRITERIO_LEGAL.txt",
                            "que": "la carpeta legal de una entidad", "agentes": "Fidel y Constanza",
                            "setup": "/criterio-compliance:compliance-setup"},
}
# Lo que no se recorre: lo que no es de la organización, y el estado de los agentes.
SALTAR = {".git", "node_modules", ".criterio", "__pycache__", ".venv", ".next", "Library", "Applications"}
TOPE = 6
CANDIDATAS = 10


def es_marcador(nombre: str) -> bool:
    """El archivo que marca una raíz. Ningún inventario lo cuenta como documento."""
    return nombre.startswith(PREFIJO) and nombre.endswith(".txt")


def plugin_propio() -> str:
    try:
        return json.loads((AQUI.parent / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["name"]
    except (OSError, json.JSONDecodeError, KeyError):
        return ""


def estructura() -> dict:
    try:
        return json.loads((AQUI / "estructura.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"niveles": []}


def leer(carpeta: Path, plugin: str) -> dict | None:
    """La marca de una carpeta, si la tiene: de qué familia, de qué entidad o caso y quién la puso."""
    f = carpeta / DESTINO[plugin]["marca"]
    if not f.is_file():
        return None
    try:
        texto = f.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r"^criterio: (.+)$", texto, re.M)
    datos = dict(x.split("=", 1) for x in (m.group(1).split("; ") if m else []) if "=" in x)
    return {"archivo": f.name, "familia": datos.get("familia"), "entidad": datos.get("entidad"),
            "marcada": datos.get("fecha"), "por": datos.get("por")}


def _hijos(d: Path) -> list[Path]:
    try:
        return sorted(x for x in d.iterdir() if x.is_dir() and not x.name.startswith(".") and x.name not in SALTAR)
    except OSError:
        return []


def _puntaje_raiz(d: Path, est: dict) -> tuple[int, list[str]]:
    """Cuánto se parece una carpeta a la raíz de la estructura recomendada, y por qué."""
    hijos = _hijos(d)
    nombres = {h.name for h in hijos}
    puntos, evidencia = 0, []
    for nv in est.get("niveles", []):
        if not nv.get("ruta"):
            propias = [c["carpeta"] for c in nv.get("carpetas", []) if c["carpeta"] in nombres]
            if propias:
                puntos += 2 * len(propias)
                evidencia.append("tiene " + ", ".join(f"{c}/" for c in propias))
            continue
        rx = re.compile(nv["ruta"] + "$")
        prof = nv.get("profundidad", 1)
        if prof == 1:
            inst = [h for h in hijos if rx.match(h.name)]
        else:
            inst = [n for h in hijos for n in _hijos(h) if rx.match(f"{h.name}/{n.name}")]
        conocidas = {c["carpeta"] for c in nv.get("carpetas", [])}
        con_estructura = [i for i in inst if conocidas & {x.name for x in _hijos(i)}]
        if con_estructura:
            # Una carpeta que contiene casos con su estructura ya es candidata, aunque sea uno solo.
            puntos += min(len(con_estructura), 5) + 2
            ejemplos = ", ".join(i.name for i in con_estructura[:3]) + ("…" if len(con_estructura) > 3 else "")
            n = len(con_estructura)
            evidencia.append(f"{n} {nv['id']}{'s' if n > 1 else ''} ({ejemplos})")
    return puntos, evidencia


def _puntaje_caso(d: Path, est: dict, nivel: str) -> tuple[int, list[str]]:
    """Cuánto se parece una carpeta a la de un proyecto o un producto."""
    nv = next((n for n in est.get("niveles", []) if n["id"] == nivel), None)
    if nv is None or not re.match(nv["ruta"] + "$", d.name):
        return 0, []
    conocidas = [c["carpeta"] for c in nv.get("carpetas", [])]
    propias = [c for c in conocidas if (d / c).is_dir()]
    if len(propias) < 2:
        return 0, []
    return 2 * len(propias), [f"se llama como un {nivel} y tiene " + ", ".join(f"{c}/" for c in propias)]


def buscar(desde: Path, plugin: str) -> dict:
    """Las carpetas que pueden ser la raíz de este agente, de la más probable a la menos: primero
    las marcadas, después por la evidencia de su estructura."""
    dest = DESTINO[plugin]
    est = estructura()
    desde = desde.expanduser()
    vistas, candidatas = 0, []
    pila = [(desde, 0)]
    while pila:
        d, nivel = pila.pop()
        vistas += 1
        marca = leer(d, plugin)
        if dest["busca"] == "raiz":
            puntos, evidencia = _puntaje_raiz(d, est)
        else:
            puntos, evidencia = _puntaje_caso(d, est, dest["nivel"])
        if marca or puntos >= 3:
            if marca:
                evidencia.insert(0, f"marcada con {marca['archivo']}" + (f": {marca['entidad']}" if marca.get("entidad") else ""))
            try:
                rel = d.resolve().relative_to(desde.resolve()).as_posix() or "."
            except ValueError:
                rel = str(d)
            candidatas.append({"carpeta": rel, "ruta": str(d.resolve()), "marcada": bool(marca), "marca": marca,
                               "puntaje": puntos, "evidencia": evidencia})
        if nivel < TOPE:
            for h in reversed(_hijos(d)):
                if not h.name.startswith("estado-"):
                    pila.append((h, nivel + 1))
    candidatas.sort(key=lambda c: (not c["marcada"], -c["puntaje"], c["carpeta"]))
    for i, c in enumerate(candidatas[:CANDIDATAS], 1):
        c["n"] = i
    return {"desde": str(desde), "busca": dest["que"], "marca": dest["marca"], "carpetas_vistas": vistas,
            "candidatas": candidatas[:CANDIDATAS], "hay_mas": max(0, len(candidatas) - CANDIDATAS),
            "si_no_esta": "Si la carpeta no está en la lista, conéctala a la sesión y vuelve a buscar, "
                          f"o di su ruta. Después, {dest['setup']}."}


def marcar(carpeta: Path, plugin: str, entidad: str | None, por: str | None, hoy: dt.date | None = None) -> dict:
    """Deja la marca visible en la raíz. Solo se corre con el sí de la persona: es lo único que un
    agente escribe dentro de los documentos (ADR 0011)."""
    dest = DESTINO[plugin]
    carpeta = carpeta.expanduser()
    if not carpeta.is_dir():
        return {"ok": False, "motivo": f"{carpeta} no es una carpeta"}
    partes = carpeta.resolve().parts
    if ".criterio" in partes or any(p.startswith("estado-") for p in partes):
        return {"ok": False, "motivo": "esa es una carpeta de estado de un agente, no de documentos"}
    hoy = hoy or dt.date.today()
    familia = {"pmo": "PMO", "cfo": "CFO", "clo": "CLO"}[dest["familia"]]
    texto = f"""CRITERIO · {dest['que'].upper()}

Esta es {dest['que']} que procesa{'n' if ' y ' in dest['agentes'] else ''} {dest['agentes']} (familia {familia} de Criterio).
{'Entidad o caso: ' + entidad if entidad else ''}
Marcada el {hoy.isoformat()}{' por ' + por if por else ''}.

No muevas ni cambies el nombre de esta carpeta. Si lo haces, el agente deja de encontrarla y hay que
correr otra vez {dest['setup']}.

Este archivo no es un documento: ningún agente lo procesa ni lo cuenta. Se puede borrar sin perder
nada; solo se pierde la marca que deja reconocer la carpeta a primera vista.

criterio: familia={dest['familia']}; plugin={plugin}; entidad={entidad or ''}; fecha={hoy.isoformat()}; por={por or ''}
"""
    f = carpeta / dest["marca"]
    previa = leer(carpeta, plugin)
    f.write_text(texto, encoding="utf-8")
    return {"ok": True, "archivo": f.name, "carpeta": str(carpeta), "reemplazo": bool(previa),
            "antes": previa}


def selftest() -> int:
    import tempfile
    fallas = []

    def ok(que, real, esperado):
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}')
        if real != esperado:
            fallas.append(f"{que}: {real!r} en vez de {esperado!r}")

    est_cfo = {"niveles": [
        {"id": "entidad", "ruta": None, "carpetas": [{"carpeta": "00-referencia"}]},
        {"id": "periodo", "ruta": r"\d{4}-\d{2}", "profundidad": 1, "carpetas": [{"carpeta": "10-contabilidad"}, {"carpeta": "20-bancos"}]}]}
    global estructura
    original = estructura
    estructura = lambda: est_cfo  # noqa: E731
    try:
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            ent = t / "Documentos" / "Contabilidad 2026" / "900123456 Entidad de Ejemplo"
            for d in ("00-referencia", "2026-08/10-contabilidad", "2026-09/10-contabilidad", "2026-09/20-bancos"):
                (ent / d).mkdir(parents=True)
            (t / "Documentos" / "Fotos" / "2026-09").mkdir(parents=True)        # se parece, pero no es
            (t / "estado-finanzas" / "900123456" / "2026-09" / "10-contabilidad").mkdir(parents=True)
            (t / ".criterio" / "finanzas" / "00-referencia").mkdir(parents=True)
            r = buscar(t, "criterio-finance")
            ok("encuentra la carpeta de la entidad aunque esté tres niveles abajo y tenga espacios",
               [c["carpeta"] for c in r["candidatas"]], ["Documentos/Contabilidad 2026/900123456 Entidad de Ejemplo"])
            ok("y dice por qué: la carpeta de referencia y los periodos",
               r["candidatas"][0]["evidencia"], ["tiene 00-referencia/", "2 periodos (2026-08, 2026-09)"])
            ok("no propone el estado del agente ni una carpeta de fotos con nombre de periodo",
               any("estado" in c["carpeta"] or "Fotos" in c["carpeta"] for c in r["candidatas"]), False)
            m = marcar(ent, "criterio-finance", "Entidad de Ejemplo (900123456)", "Ana Gil", dt.date(2026, 10, 21))
            f = ent / "_CRITERIO_FINANZAS.txt"
            # El guion bajo: el Finder y el Explorador ponen la puntuación antes que números y letras.
            ok("la marca es un archivo de texto visible, que empieza por guion bajo para salir primero",
               (m["ok"], f.is_file(), f.name.startswith("_") and f.suffix == ".txt"), (True, True, True))
            ok("dice de quién es, en palabras", "Clara y Tomás" in f.read_text(encoding="utf-8")
               and "No muevas" in f.read_text(encoding="utf-8"), True)
            otra = t / "Respaldo" / "900123456 copia"
            for d in ("00-referencia", "2026-09/10-contabilidad"):
                (otra / d).mkdir(parents=True)
            r = buscar(t, "criterio-finance")
            ok("con una copia parecida al lado, la marcada va primero y con certeza",
               (r["candidatas"][0]["carpeta"], r["candidatas"][0]["marcada"], r["candidatas"][0]["n"]),
               ("Documentos/Contabilidad 2026/900123456 Entidad de Ejemplo", True, 1))
            ok("y se lee de qué entidad es", leer(ent, "criterio-finance")["entidad"], "Entidad de Ejemplo (900123456)")
            ok("un marcador no se pone en el estado de un agente",
               marcar(t / "estado-finanzas" / "900123456", "criterio-finance", None, None)["ok"], False)
            ok("el marcador se reconoce como tal", (es_marcador("_CRITERIO_FINANZAS.txt"), es_marcador("acta.txt")), (True, False))
            estructura = lambda: {"niveles": [  # noqa: E731
                {"id": "proyecto", "ruta": r"[A-Z]{2,5}-\d{2,}[^/]*", "profundidad": 1,
                 "carpetas": [{"carpeta": "00-gobierno"}, {"carpeta": "10-plan"}, {"carpeta": "30-reuniones"}]}]}
            pry = t / "PMO" / "PRY-101 Originación digital"
            for d in ("00-gobierno", "30-reuniones"):
                (pry / d).mkdir(parents=True)
            (t / "PMO" / "PRY-102 Sin carpetas").mkdir(parents=True)
            r = buscar(t, "criterio-project")
            ok("Samuel encuentra la carpeta de un proyecto por su nombre y lo que tiene adentro",
               [c["carpeta"] for c in r["candidatas"]], ["PMO/PRY-101 Originación digital"])
            r = buscar(t, "criterio-portfolio")
            ok("y Vera, la carpeta que contiene los proyectos", [c["carpeta"] for c in r["candidatas"]][:1], ["PMO"])
    finally:
        estructura = original
    print()
    if fallas:
        print(f"{len(fallas)} falla(s)")
        return 1
    print("todo pasa")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="La carpeta raíz de cada agente: buscarla y marcarla.")
    ap.add_argument("action", choices=["buscar", "marcar", "leer"], nargs="?")
    ap.add_argument("--plugin", default=None, help="por defecto, el plugin donde está este archivo")
    ap.add_argument("--desde", type=Path, default=None)
    ap.add_argument("--carpeta", type=Path, default=None)
    ap.add_argument("--entidad", default=None)
    ap.add_argument("--por", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    plugin = a.plugin or plugin_propio()
    if plugin not in DESTINO:
        ap.error(f"{plugin or 'este plugin'} no tiene carpeta raíz de documentos")
    if a.action == "buscar":
        print(json.dumps(buscar(a.desde or Path.cwd(), plugin), ensure_ascii=False, indent=2))
    elif a.action == "marcar":
        if not a.carpeta:
            ap.error("--carpeta es la raíz que la persona eligió")
        r = marcar(a.carpeta, plugin, a.entidad, a.por)
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 0 if r["ok"] else 1
    elif a.action == "leer":
        print(json.dumps(leer(a.carpeta or Path.cwd(), plugin), ensure_ascii=False, indent=2))
    else:
        ap.error("buscar, marcar o leer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
