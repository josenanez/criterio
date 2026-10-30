#!/usr/bin/env python3
"""Criterio — compartir hallazgos, siempre preguntando (decisión 0025).

    python3 compartir.py resumen [--raiz <carpeta>]   el resumen sin datos, en Markdown
    python3 compartir.py enlace  [--raiz <carpeta>]   el enlace a la plantilla de hallazgo, con el resumen
    python3 compartir.py --selftest

El resumen sale del rastro local que escribe el arnés (`.criterio/corridas/<área>/corridas.json`,
ver rastro.py), y solo de una lista cerrada de campos que no vienen de los documentos: el plugin y
su versión, cada comando con cuántas veces corrió y su duración mediana, y cada señal por su código
con cuántas veces salió. No lleva el argumento de ningún comando, ni notas, ni nombres, ni rutas,
ni cifras de una ficha. Lo arma este código; el modelo de lenguaje (LLM) no lo redacta.

Este script no envía nada. `enlace` imprime una dirección de la plantilla de hallazgo del
repositorio con los campos ya escritos; la persona la abre, la completa con sus palabras y decide
si la publica.
"""
from __future__ import annotations

import json
import os
import re
import statistics
import sys
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = "https://github.com/josenanez/criterio"
CODIGO = re.compile(r"^[a-z][a-z0-9_]{2,60}$")      # un código de señal o un comando, nada más
COMANDO = re.compile(r"^[a-z][a-z0-9-]{1,40}$")


def plugin() -> dict:
    """El plugin que corre: su nombre y su versión, de su propio plugin.json."""
    raiz = Path(os.environ.get("CLAUDE_PLUGIN_ROOT") or AQUI.parent)
    try:
        return json.loads((raiz / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def familias() -> dict:
    """Plugin → la familia como la lista la plantilla de hallazgo. Lo escribe scripts/sincronizar.py
    desde cada familia.json, el mismo de donde sale la lista de la plantilla."""
    try:
        return json.loads((AQUI / "compartir.json").read_text(encoding="utf-8"))["familias"]
    except (OSError, json.JSONDecodeError, KeyError):
        return {}


def area(nombre: str) -> str | None:
    sys.path.insert(0, str(AQUI))
    from rastro import AGENTE  # noqa: E402
    return AGENTE.get(nombre)


def resumen(raiz: Path, nombre: str, version: str) -> dict:
    """El resumen, desde la lista cerrada de campos. Lo que no pasa por CODIGO o COMANDO no entra."""
    ar = area(nombre)
    f = raiz / ".criterio" / "corridas" / (ar or "_") / "corridas.json"
    try:
        corridas = json.loads(f.read_text(encoding="utf-8")) if ar and f.is_file() else []
    except json.JSONDecodeError:
        corridas = []
    comandos: dict[str, dict] = {}
    senales: dict[str, int] = {}
    for c in corridas if isinstance(corridas, list) else []:
        cmd = str(c.get("comando") or "")
        if not COMANDO.match(cmd):
            continue
        x = comandos.setdefault(cmd, {"n": 0, "seg": []})
        x["n"] += 1
        if isinstance(c.get("segundos"), (int, float)):
            x["seg"].append(int(c["segundos"]))
        for m in c.get("medidas") or []:
            for k, v in (m.get("por_senal") or {}).items():
                if CODIGO.match(str(k)) and isinstance(v, int) and v >= 0:
                    senales[k] = senales.get(k, 0) + v
    return {
        "plugin": nombre, "version": version, "familia": familias().get(nombre),
        "comandos": [{"comando": k, "corridas": v["n"], "segundos_mediana": int(statistics.median(v["seg"])) if v["seg"] else None}
                     for k, v in sorted(comandos.items())],
        "senales": [{"senal": k, "veces": v} for k, v in sorted(senales.items())],
    }


def markdown(r: dict) -> str:
    l = [f"**{r['plugin']} {r['version']}**", ""]
    if not r["comandos"]:
        return "\n".join(l + ["No hay corridas en el rastro de esta carpeta."])
    l += ["| Comando | Corridas | Duración mediana |", "|---|---:|---:|"]
    l += [f"| {c['comando']} | {c['corridas']} | {str(c['segundos_mediana']) + ' s' if c['segundos_mediana'] is not None else '—'} |"
          for c in r["comandos"]]
    if r["senales"]:
        l += ["", "| Señal | Veces |", "|---|---:|"] + [f"| `{s['senal']}` | {s['veces']} |" for s in r["senales"]]
    return "\n".join(l)


def enlace(r: dict) -> str:
    q = {"template": "hallazgo.yml", "title": f"[Hallazgo] {r['plugin']} {r['version']}",
         "comando": f"{r['plugin']} · {r['version']}", "hallazgo": markdown(r) + "\n\n(Escribe aquí, con tus palabras, qué encontró o qué no encontró.)"}
    if r.get("familia"):
        q["familia"] = r["familia"]
    return f"{REPO}/issues/new?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)


def selftest() -> int:
    import tempfile
    fallas = []

    def ok(que, obtenido, esperado):
        print(("  ok   " if obtenido == esperado else "  FALLA ") + que)
        if obtenido != esperado:
            print(f"         esperado {esperado!r}\n         obtenido {obtenido!r}")
            fallas.append(que)

    with tempfile.TemporaryDirectory() as t:
        raiz = Path(t)
        d = raiz / ".criterio" / "corridas" / "finanzas"
        d.mkdir(parents=True)
        secreto = "Banco Sintético 900123456 por 1.234.567,89"
        (d / "corridas.json").write_text(json.dumps([
            {"comando": "close-scan", "args": f"finanzas/{secreto}", "segundos": 60,
             "medidas": [{"por_senal": {"bank_unreconciled": 2, "einvoice_duplicate": 1}, "nota": secreto, "_estado": secreto}]},
            {"comando": "close-scan", "args": "", "segundos": 100, "medidas": [{"por_senal": {"bank_unreconciled": 1}}]},
            {"comando": "finance-setup", "segundos": 30, "medidas": [{"por_senal": {secreto: 9}}]},
            {"comando": "../../etc", "segundos": 1},
        ]), encoding="utf-8")
        r = resumen(raiz, "criterio-finance", "1.1.0")
        texto = json.dumps(r, ensure_ascii=False) + markdown(r) + enlace(r)
        ok("cuenta las corridas de cada comando y su duración mediana",
           [(c["comando"], c["corridas"], c["segundos_mediana"]) for c in r["comandos"]],
           [("close-scan", 2, 80), ("finance-setup", 1, 30)])
        ok("suma cada señal por su código", [(s["senal"], s["veces"]) for s in r["senales"]],
           [("bank_unreconciled", 3), ("einvoice_duplicate", 1)])
        ok("no lleva el argumento, la nota, el estado ni una llave que no sea un código",
           any(x in texto for x in ("Banco", "900123456", "1.234.567", "finanzas/")), False)
        ok("un comando que no es un nombre de comando no entra", "etc" in texto, False)
        ok("el enlace va a la plantilla de hallazgo del repositorio",
           enlace(r).startswith(f"{REPO}/issues/new?template=hallazgo.yml"), True)
        ok("sin rastro, lo dice", "No hay corridas" in markdown(resumen(raiz, "criterio-legal", "1.2.0")), True)
    print("todo pasa" if not fallas else f"{len(fallas)} fallas")
    return 0 if not fallas else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    import argparse
    ap = argparse.ArgumentParser(description="Compartir hallazgos: un resumen sin datos, que la persona ve y abre ella.")
    ap.add_argument("action", choices=["resumen", "enlace"])
    ap.add_argument("--raiz", default=os.getcwd(), help="la carpeta donde corre la sesión, la que tiene .criterio/")
    a = ap.parse_args()
    p = plugin()
    r = resumen(Path(a.raiz), p.get("name") or AQUI.parent.name, p.get("version") or "")
    print(markdown(r) if a.action == "resumen" else enlace(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
