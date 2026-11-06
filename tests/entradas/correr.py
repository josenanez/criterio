#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La prueba de las entradas: cada agente, pedido en palabras, contra Claude Code real.

    python3 tests/entradas/correr.py --carpeta ~/Projects/criterio-prueba
    python3 tests/entradas/correr.py --carpeta ~/Projects/criterio-prueba --solo clara
    python3 tests/entradas/correr.py --resumen tests/entradas/resultados.json

La entrada de cada agente (decisión 0027) elige el comando que resuelve el pedido. Esa elección la
hace el modelo de lenguaje (LLM), así que no se prueba en verificar.py: se prueba aquí, con los
plugins instalados y Claude Code en modo no interactivo (`claude -p`), un pedido a la vez.

**Solo se mide la elección, no el trabajo.** Apenas la entrada invoca el comando que eligió, la
corrida se detiene: lo que haría ese comando lo prueban las rondas de cada familia. Así cada pedido
cuesta un turno del modelo, no una corrida completa. Las herramientas que escriben o ejecutan quedan
bloqueadas (`--disallowedTools`), por si algo llegara más lejos.

Lo que cuenta como acierto, según lo que pide `pedidos.json`:

    comando    invocó ese comando
    pregunta   no invocó nada y terminó preguntando
    entrada    no invocó nada y dio la entrada del otro agente
    ninguno    no invocó nada y no hizo el trabajo por su cuenta
    menu       no invocó nada y mostró lo que sabe hacer

Escribe `resultados.json` y `RESULTADOS.md` junto a este archivo, con el acierto y su intervalo del
95 %, como las rondas. Usa la librería estándar y el `claude` del equipo.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
COMANDO = re.compile(r"(criterio-[a-z]+):([a-z][a-z-]*)")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if not n:
        return 0.0, 0.0
    p = k / n
    c = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    centro = (p + z * z / (2 * n)) / (1 + z * z / n)
    return max(0.0, centro - c), min(1.0, centro + c)


def correr(claude: str, carpeta: Path, p: dict, timeout: int) -> dict:
    """Un pedido: lo que invocó, lo que dijo al final y cuánto tardó."""
    propio = f"{p['plugin']}:{p['agente']}"
    cmd = [claude, "-p", p["pedido"], "--output-format", "stream-json", "--verbose",
           "--allowedTools", "Skill", "Read", "Glob",
           "--disallowedTools", "Bash", "Write", "Edit", "NotebookEdit", "WebFetch", "WebSearch"]
    inicio = time.time()
    proc = subprocess.Popen(cmd, cwd=carpeta, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    invocado, texto, error = None, [], None
    try:
        for linea in proc.stdout:
            if time.time() - inicio > timeout:
                error = f"más de {timeout} s"
                break
            try:
                ev = json.loads(linea)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "assistant":
                for parte in (ev.get("message") or {}).get("content") or []:
                    if parte.get("type") == "text":
                        texto.append(parte.get("text") or "")
                    elif parte.get("type") == "tool_use" and parte.get("name") in ("Skill", "SlashCommand"):
                        m = COMANDO.search(json.dumps(parte.get("input") or {}, ensure_ascii=False))
                        if m and m.group(0) != propio:
                            invocado = m.group(0)
            elif ev.get("type") == "result":
                if ev.get("result"):
                    texto.append(ev["result"])
                if ev.get("is_error"):
                    error = ev.get("result") or "error"
            if invocado:
                break
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()
    if not invocado and not texto and proc.returncode not in (0, None, -15):
        error = error or (proc.stderr.read() if proc.stderr else "")[:400] or f"salió con {proc.returncode}"
    return {"invocado": invocado, "texto": "\n".join(texto).strip()[-1500:], "segundos": round(time.time() - inicio, 1),
            "error": error}


def calificar(p: dict, r: dict) -> tuple[bool, str]:
    e, inv, t = p["espera"], r["invocado"], r["texto"]
    if r["error"] and not inv and not t:
        return False, f"no corrió: {r['error']}"
    if "comando" in e:
        return inv == e["comando"], f"invocó {inv}" if inv else "no invocó nada"
    if inv:
        return False, f"invocó {inv}"
    if "pregunta" in e:
        return "?" in t[-400:], "preguntó" if "?" in t[-400:] else "no preguntó"
    if "entrada" in e:
        ok = f"/{e['entrada']}" in t or e["entrada"] in t
        return ok, f"dio la entrada {e['entrada']}" if ok else "no dio la entrada del otro agente"
    if "menu" in e:
        return len(t) > 80, "mostró lo que sabe hacer" if len(t) > 80 else "no mostró nada"
    return True, "no hizo el trabajo por su cuenta"


def coma(x: float) -> str:
    return f"{x:.1f}".replace(".", ",")


def escribir(filas: list[dict], destino: Path) -> None:
    k, n = sum(f["ok"] for f in filas), len(filas)
    lo, hi = wilson(k, n)
    d = {"fecha": dt.date.today().isoformat(), "aciertos": k, "pedidos": n,
         "intervalo_95": [round(lo * 100, 1), round(hi * 100, 1)], "filas": filas}
    (destino / "resultados.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    l = ["# La prueba de las entradas · resultados", "",
         f"Corrida del {d['fecha']} con Claude Code en modo no interactivo: **{k} de {n} pedidos** eligieron bien "
         f"({coma(100 * k / n if n else 0)} %; intervalo del 95 %: {coma(d['intervalo_95'][0])} a {coma(d['intervalo_95'][1])} %). "
         "Se mide la elección del comando, no su trabajo: eso lo prueban las rondas de cada familia.", "",
         "| # | Pedido | Lo esperado | Lo que hizo | |", "|---|---|---|---|---|"]
    for f in filas:
        l.append(f"| {f['id']} | `{f['pedido']}` | {f['como']} | {f['resultado']} | {'✅' if f['ok'] else '❌'} |")
    (destino / "RESULTADOS.md").write_text("\n".join(l) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="La prueba de las entradas, contra Claude Code real.")
    ap.add_argument("--carpeta", type=Path, default=Path.cwd(), help="donde se abre Claude; por defecto, aquí")
    ap.add_argument("--solo", default=None, help="un agente: clara, fidel…")
    ap.add_argument("--claude", default="claude")
    ap.add_argument("--timeout", type=int, default=180)
    a = ap.parse_args()
    pedidos = json.loads((AQUI / "pedidos.json").read_text(encoding="utf-8"))["pedidos"]
    if a.solo:
        pedidos = [p for p in pedidos if p["agente"] == a.solo]
    filas = []
    for p in pedidos:
        r = correr(a.claude, a.carpeta.expanduser(), p, a.timeout)
        ok, que = calificar(p, r)
        filas.append({"id": p["id"], "pedido": p["pedido"], "como": p["como"], "ok": ok, "resultado": que,
                      "segundos": r["segundos"], "texto": r["texto"]})
        print(f"  {'✅' if ok else '❌'} {p['id']:4} {p['pedido'][:70]:70} → {que} ({r['segundos']} s)", flush=True)
    escribir(filas, AQUI)
    k = sum(f["ok"] for f in filas)
    print(f"\n  {k} de {len(filas)} · RESULTADOS.md y resultados.json en {AQUI}")
    return 0 if k == len(filas) else 1


if __name__ == "__main__":
    sys.exit(main())
