#!/usr/bin/env python3
"""El consumo de tokens de cada familia y de cada agente, desde las sesiones de Claude Code.

    python3 consumo.py medir --raiz <carpeta de trabajo>      el consumo, en JSON
    python3 consumo.py --selftest

Claude Code guarda cada sesión en `~/.claude/projects/<carpeta>/<sesión>.jsonl` (o bajo
`CLAUDE_CONFIG_DIR`), con el uso de cada respuesta: los tokens de entrada, los que escribió y
leyó de la caché y los de salida. De esas líneas se toman solo cuatro cosas —el uso, el
identificador de la respuesta, la fecha y la carpeta donde corrió—, más el nombre del comando
que la persona pidió. **El texto de la conversación no se guarda ni se muestra.** Solo cuentan
las sesiones que corrieron dentro de la carpeta de trabajo.

Cómo se atribuye: una sesión se cuenta al último comando de Criterio que se pidió en ella,
hasta el siguiente. Lo que la persona escribe después en sus palabras («ahora concilia el
banco») sigue siendo de ese agente; otro comando, de Criterio o no, cambia la cuenta. Los
subagentes cuentan con la sesión que los lanzó. Una respuesta se cuenta una sola vez aunque
Claude Code la escriba en varias líneas.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import mapa  # noqa: E402

COMANDO = re.compile(r"<command-name>/?([a-z0-9-]+):([a-z0-9-]+)</command-name>")
COMANDO_SUELTO = re.compile(r"^\s*/([a-z0-9-]+):([a-z0-9-]+)")
OTRO_COMANDO = re.compile(r"<command-name>/?[^<]+</command-name>")
CAMPOS = (("entrada", "input_tokens"), ("cache_escritura", "cache_creation_input_tokens"),
          ("cache_lectura", "cache_read_input_tokens"), ("salida", "output_tokens"))


def carpeta_sesiones() -> Path:
    base = os.environ.get("CLAUDE_CONFIG_DIR")
    return (Path(base) if base else Path.home() / ".claude") / "projects"


def codificar(p: Path) -> str:
    """Cómo nombra Claude Code la carpeta de las sesiones de un directorio: cada carácter que no es
    letra ni dígito pasa a guion (`/x/.pruebas/y` → `-x--pruebas-y`)."""
    return re.sub(r"[^A-Za-z0-9]", "-", str(p))


def quien(registro: dict) -> dict:
    """Del plugin al agente: (familia, agente). El plugin de la familia y Rostrum cuentan aparte."""
    d = {a["plugin"]: (a["familia"], a["id"]) for a in registro["agentes"]}
    for f in registro["familias"]:
        d.setdefault(f"criterio-{f['sigla']}", (f["sigla"], "familia"))
    d.setdefault("criterio-server", ("rostrum", "rostrum"))
    return d


def _vacio() -> dict:
    return {"corridas": 0, **{k: 0 for k, _ in CAMPOS}, "total": 0}


def _sumar(a: dict, u: dict) -> None:
    for k, campo in CAMPOS:
        n = int(u.get(campo) or 0)
        a[k] += n
        a["total"] += n


def medir(raiz: Path, base: Path | None = None, registro: dict | None = None) -> dict:
    raiz = raiz.resolve()
    base = base or carpeta_sesiones()
    plugins = quien(registro or mapa.registro())
    pref = codificar(raiz)
    carpetas = [d for d in (base.iterdir() if base.is_dir() else [])
                if d.is_dir() and (d.name == pref or d.name.startswith(pref + "-"))]
    # Las líneas de cada sesión, con sus subagentes, en orden: lo que cuenta un subagente depende
    # del comando que estaba corriendo cuando se lanzó.
    sesiones: dict[str, list] = {}
    for d in carpetas:
        for f in d.rglob("*.jsonl"):
            with open(f, encoding="utf-8", errors="replace") as fh:
                for linea in fh:
                    if '"usage"' not in linea and "command-name" not in linea and '"type":"user"' not in linea:
                        continue
                    try:
                        x = json.loads(linea)
                    except ValueError:
                        continue
                    cwd = x.get("cwd")
                    if not cwd or not (Path(cwd) == raiz or raiz in Path(cwd).parents):
                        continue
                    sesiones.setdefault(x.get("sessionId") or f.stem, []).append(x)
    out = {"agentes": {}, "fuera": _vacio(), "por_dia": {}, "sesiones": 0, "desde": None, "hasta": None}
    vistos = set()
    for sid, lineas in sesiones.items():
        lineas.sort(key=lambda x: x.get("timestamp") or "")
        actual = None
        usada = False
        for x in lineas:
            m = x.get("message") or {}
            if x.get("type") == "user" and not x.get("isMeta"):
                c = m.get("content")
                texto = c if isinstance(c, str) else ""
                hit = COMANDO.search(texto) or COMANDO_SUELTO.match(texto)
                if hit and hit.group(1) in plugins:
                    fam, ag = plugins[hit.group(1)]
                    actual = (fam, ag, hit.group(2))
                    reg = out["agentes"].setdefault(ag, {"familia": fam, "comandos": {}})
                    reg["comandos"].setdefault(hit.group(2), _vacio())["corridas"] += 1
                elif hit or OTRO_COMANDO.search(texto):
                    actual = None
            elif x.get("type") == "assistant" and m.get("usage"):
                clave = (sid, m.get("id") or x.get("uuid"))
                if clave in vistos:
                    continue
                vistos.add(clave)
                usada = True
                if actual:
                    fam, ag, cmd = actual
                    destino = out["agentes"].setdefault(ag, {"familia": fam, "comandos": {}})["comandos"].setdefault(cmd, _vacio())
                else:
                    destino = out["fuera"]
                _sumar(destino, m["usage"])
                if actual:
                    dia = (x.get("timestamp") or "")[:10]
                    if dia:
                        out["por_dia"][dia] = out["por_dia"].get(dia, 0) + sum(int(m["usage"].get(c) or 0) for _, c in CAMPOS)
                        out["desde"] = min(out["desde"] or dia, dia)
                        out["hasta"] = max(out["hasta"] or dia, dia)
        out["sesiones"] += usada
    for a in out["agentes"].values():
        a["total"] = _vacio()
        for c in a["comandos"].values():
            for k in a["total"]:
                a["total"][k] += c[k]
    return out


def por_familia(medido: dict) -> dict:
    fam = {}
    for a in medido["agentes"].values():
        t = fam.setdefault(a["familia"], _vacio())
        for k in t:
            t[k] += a["total"][k]
    return fam


def pruebas() -> dict:
    """Lo que cuesta cada comando en las rondas de prueba (lo escribe scripts/consumo_pruebas.py)."""
    f = AQUI / "consumo-pruebas.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.is_file() else {"agentes": {}}


def selftest() -> int:
    import tempfile
    fallas = []

    def ok(que, real, esperado):
        if real != esperado:
            fallas.append(que)
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}' + ("" if real == esperado else f": {real!r} ≠ {esperado!r}"))

    reg = {"agentes": [{"plugin": "criterio-finance", "familia": "cfo", "id": "clara"}],
           "familias": [{"sigla": "cfo"}]}
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        raiz = t / "org.trabajo"
        (raiz / "finanzas").mkdir(parents=True)
        base = t / "projects"
        ses = base / codificar(raiz)
        ses.mkdir(parents=True)
        otra = base / codificar(t / "otra")
        otra.mkdir()

        def u(i, o, c=0):
            return {"input_tokens": i, "output_tokens": o, "cache_read_input_tokens": c, "cache_creation_input_tokens": 0}
        lineas = [
            {"type": "user", "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:00:00Z",
             "message": {"content": "<command-name>/criterio-finance:close-scan</command-name><command-args>secreto del cliente</command-args>"}},
            {"type": "user", "isMeta": True, "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:00:00Z",
             "message": {"content": "<command-name>/clear</command-name>"}},
            {"type": "assistant", "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:00:05Z",
             "message": {"id": "m1", "usage": u(10, 5, 100)}},
            {"type": "assistant", "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:00:05Z",
             "message": {"id": "m1", "usage": u(10, 5, 100)}},
            {"type": "user", "sessionId": "s1", "cwd": str(raiz / "finanzas"), "timestamp": "2026-11-10T10:01:00Z",
             "message": {"content": "ahora concilia el banco"}},
            {"type": "assistant", "sessionId": "s1", "cwd": str(raiz / "finanzas"), "timestamp": "2026-11-10T10:01:05Z",
             "message": {"id": "m2", "usage": u(1, 2)}},
            {"type": "user", "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:02:00Z",
             "message": {"content": "<command-name>/clear</command-name>"}},
            {"type": "assistant", "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:02:05Z",
             "message": {"id": "m3", "usage": u(7, 0)}},
        ]
        (ses / "s1.jsonl").write_text("\n".join(json.dumps(x) for x in lineas) + "\n", encoding="utf-8")
        sub = ses / "s1" / "subagents"
        sub.mkdir(parents=True)
        (sub / "agent-1.jsonl").write_text(json.dumps(
            {"type": "assistant", "isSidechain": True, "sessionId": "s1", "cwd": str(raiz), "timestamp": "2026-11-10T10:00:30Z",
             "message": {"id": "m9", "usage": u(3, 3)}}) + "\n", encoding="utf-8")
        (otra / "s2.jsonl").write_text(json.dumps(
            {"type": "assistant", "sessionId": "s2", "cwd": str(t / "otra"), "timestamp": "2026-11-10T10:00:00Z",
             "message": {"id": "x", "usage": u(999, 999)}}) + "\n", encoding="utf-8")
        m = medir(raiz, base, reg)
        c = m["agentes"]["clara"]["comandos"]["close-scan"]
        ok("el comando y lo que siguió en palabras cuentan para su agente; la respuesta repetida, una vez",
           (c["corridas"], c["entrada"], c["salida"], c["cache_lectura"]), (1, 14, 10, 100))
        ok("el subagente cuenta con el comando que lo lanzó", c["total"], 124)
        ok("otro comando corta la cuenta: lo que sigue va fuera de Criterio", m["fuera"]["total"], 7)
        ok("otra carpeta no entra", m["sesiones"], 1)
        ok("por familia", por_familia(m)["cfo"]["total"], 124)
        ok("y lo que se guarda no lleva el texto de la conversación", "secreto" in json.dumps(m), False)
        ok("la carpeta de las sesiones se nombra como Claude Code", codificar(Path("/x/.pruebas/y")), "-x--pruebas-y")
    print()
    print(f"{len(fallas)} falla(s)" if fallas else "todo pasa")
    return 1 if fallas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="El consumo de tokens de cada familia y cada agente.")
    ap.add_argument("accion", nargs="?", choices=["medir"])
    ap.add_argument("--raiz", type=Path, default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.accion == "medir":
        print(json.dumps(medir((a.raiz or Path.cwd()).expanduser()), ensure_ascii=False, indent=1))
        return 0
    ap.error("medir o --selftest")
    return 2


if __name__ == "__main__":
    sys.exit(main())
