#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La ronda con el agente de la familia CFO: Clara y Tomás corren sus comandos sobre el material
de una entidad, y lo que escribieron se califica contra la clave que no vieron.

    python3 tests/criterio-cfo/ronda.py armar <carpeta> --entidad banca
    python3 tests/criterio-cfo/ronda.py correr <carpeta> --tope 5000000 [--solo 1 2]
    python3 tests/criterio-cfo/ronda.py calificar <carpeta>

**El tope es obligatorio.** Antes de cada comando se suma lo que gastaron los anteriores; si
llegó al tope, la ronda para ahí y lo dice. Un comando ya empezado no se corta: el tope se puede
pasar por lo que gaste el último.

**Qué queda de cada comando**, en `<carpeta>/salidas/`: lo que imprimió, cuánto tardó, cuántos
tokens usó y qué archivos cambió, igual que en las rondas de la PMO (`tests/ronda.py`).

**Qué se califica.** Las señales que el motor dejó en `resultados.json` a partir de la
configuración y de la ficha que escribió el agente, contra las esperadas de la clave: una de más
cuenta igual que una de menos. Y la extracción: lo que el agente llevó a la ficha contra lo que
la clave dice que traen los documentos escritos. `evaluar.py` prueba el motor con la extracción
correcta; esto prueba la extracción.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
MATERIAL = AQUI / "material"
FAMILIA = json.loads((RAIZ / "families" / "criterio-cfo" / "familia.json").read_text(encoding="utf-8"))
DE = {a["id"]: {x["id"] for x in a["senales"]} for a in FAMILIA["agentes"]}
ORDEN = [(a["id"], a["plugin"], c["id"]) for a in FAMILIA["agentes"] for c in sorted(a["comandos"], key=lambda c: c["n"])]
NOTA = ("(Sesión de prueba sin interfaz: nadie va a responder preguntas. La fecha de esta prueba es {hoy}: "
        "pásala al motor con `--today {hoy}` en cada llamada que la acepte. Términos: José Francisco Ñáñez "
        "acepta los términos vigentes de esta versión para esta prueba, fecha {hoy}; cuando el agente los "
        "muestre, regístralo con ese nombre. En cada otra pregunta toma la respuesta sugerida a partir de "
        "los documentos, dila en una línea y sigue. Si un comando pide algo que no existe, dilo y termina; "
        "no lo inventes.)")


def _j(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def _w(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def manifiesto(raiz: Path) -> dict:
    return {str(f.relative_to(raiz)): hashlib.sha1(f.read_bytes()).hexdigest()[:12]
            for f in raiz.rglob("*") if f.is_file() and ".claude" not in f.parts and ".git" not in f.parts}


def armar(a) -> int:
    """El espacio del agente es el material de la entidad sin su clave; la clave queda afuera."""
    origen = MATERIAL / a.entidad
    if not (origen / "clave.json").is_file():
        print(f"no hay material para «{a.entidad}»: corre tests/criterio-cfo/generar.py")
        return 1
    carpeta = Path(a.carpeta).expanduser()
    espacio = carpeta / "espacio"
    if espacio.exists():
        print(f"{espacio} ya existe; usa otra carpeta")
        return 1
    shutil.copytree(origen, espacio, ignore=shutil.ignore_patterns("clave.json"))
    shutil.copy2(origen / "clave.json", carpeta / "clave.json")
    print(f"armado: {a.entidad} en {espacio}")
    return 0


def instalar(espacio: Path) -> None:
    if (espacio / ".claude" / "settings.json").is_file():
        return
    subprocess.run(["git", "init", "-q"], cwd=espacio)
    for p in sorted({p for _, p, _ in ORDEN}):
        subprocess.run(["claude", "plugin", "install", f"{p}@criterio", "--scope", "project"],
                       cwd=espacio, capture_output=True)


def correr(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio, sal = carpeta / "espacio", carpeta / "salidas"
    clave = _j(carpeta / "clave.json")
    sal.mkdir(exist_ok=True)
    instalar(espacio)
    docs = clave["config"]["clara"]["paths"]["documents"]
    gastado = sum(_j(f).get("tokens") or 0 for f in sal.glob("*.json"))
    for n, (agente, plugin, cmd) in enumerate(ORDEN, start=1):
        base = sal / f"{n:02d}-{cmd}"
        if base.with_suffix(".json").is_file() or (a.solo and n not in a.solo):
            continue
        if gastado >= a.tope:
            print(f"tope alcanzado: {gastado / 1e6:.2f} M de {a.tope / 1e6:.2f} M tokens; la ronda para antes de {cmd}")
            return 2
        arg = docs if cmd.endswith("-setup") else ""
        prompt = f"/{plugin}:{cmd} {arg}".strip() + "\n\n" + NOTA.format(hoy=clave["hoy"])
        antes, t0 = manifiesto(espacio), time.time()
        try:
            r = subprocess.run(["claude", "-p", prompt, "--permission-mode", "bypassPermissions",
                                "--output-format", "json"], cwd=espacio, capture_output=True,
                               text=True, timeout=a.limite)
            salida = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"subtype": "error", "result": r.stdout + r.stderr}
        except subprocess.TimeoutExpired:
            salida = {"subtype": "timeout", "result": f"no terminó en {a.limite} s"}
        despues, u = manifiesto(espacio), salida.get("usage") or {}
        fila = {"n": n, "agente": agente, "comando": cmd, "argumento": arg,
                "inicio": dt.datetime.fromtimestamp(t0, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
                "estado": salida.get("subtype"), "error": bool(salida.get("is_error")) or salida.get("subtype") != "success",
                "segundos": round(time.time() - t0), "turnos": salida.get("num_turns"),
                "tokens": sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens",
                                                       "cache_read_input_tokens", "output_tokens")),
                "tokens_salida": u.get("output_tokens"), "costo_usd": salida.get("total_cost_usd"),
                "modelo": next(iter(salida.get("modelUsage") or {}), None),
                "cambios": {"nuevos": sorted(set(despues) - set(antes)),
                            "modificados": sorted(k for k in set(antes) & set(despues) if antes[k] != despues[k]),
                            "borrados": sorted(set(antes) - set(despues))}}
        _w(base.with_suffix(".json"), fila)
        base.with_suffix(".md").write_text(f"# /{plugin}:{cmd} {arg}\n\n" + (salida.get("result") or ""), encoding="utf-8")
        gastado += fila["tokens"]
        print(f"{n:02d} {cmd:22} {fila['estado']:8} {fila['segundos']:4d} s {fila['tokens'] // 1000:6d} k "
              f"(acumulado {gastado / 1e6:.2f} M) +{len(fila['cambios']['nuevos'])} ~{len(fila['cambios']['modificados'])}",
              flush=True)
    return 0


def _norma(x):
    """3000000.0 y 3000000 son la misma cifra."""
    if isinstance(x, float) and x.is_integer():
        return int(x)
    if isinstance(x, dict):
        return {k: _norma(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_norma(v) for v in x]
    return x


def _igual(esperado, obtenido) -> bool:
    """Igual campo por campo, con una tolerancia: un texto del agente que contiene el de la clave
    —el mismo compromiso, dicho con más detalle— cuenta como bien. La diferencia se reporta igual."""
    esperado, obtenido = _norma(esperado), _norma(obtenido)
    if isinstance(esperado, str) and isinstance(obtenido, str):
        return esperado.strip().lower() in obtenido.strip().lower()
    if isinstance(esperado, dict) and isinstance(obtenido, dict):
        return all(_igual(v, obtenido.get(k)) for k, v in esperado.items())
    if isinstance(esperado, list) and isinstance(obtenido, list):
        return len(esperado) == len(obtenido) and all(_igual(a, b) for a, b in zip(esperado, obtenido))
    return esperado == obtenido


def _plano(x, pre=""):
    """Un dict anidado como pares ruta → valor, para comparar la ficha campo por campo."""
    if isinstance(x, dict):
        for k, v in x.items():
            yield from _plano(v, f"{pre}.{k}" if pre else k)
    else:
        yield pre, x


def calificar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio, clave = carpeta / "espacio", _j(carpeta / "clave.json")
    obtenido, fichas = set(), {}
    for rol, sub in (("clara", "cierre"), ("tomas", "presupuesto")):
        for f in sorted(espacio.rglob(f"{sub}/*/resultados.json")):
            obtenido |= {(x["signal"], x["key"]) for x in _j(f).get("alertas") or [] if x["signal"] in DE[rol]}
        fichas[sub] = [_j(f) for f in sorted(espacio.rglob(f"{sub}/*/ficha.json"))]
    corridos = {_j(f)["agente"] for f in (carpeta / "salidas").glob("*.json")}
    esperado = {(x["signal"], x["key"]) for x in clave["esperado"]
                if any(x["signal"] in DE[r] for r in corridos)}
    ok, sobran, faltan = obtenido & esperado, obtenido - esperado, esperado - obtenido
    extraccion = []
    de_quien = {"cierre": "clara", "presupuesto": "tomas"}
    for sub, ref in (clave.get("extraccion") or {}).items():
        if de_quien.get(sub) not in corridos:
            continue
        hecho = dict(_plano(fichas.get(sub)[-1])) if fichas.get(sub) else {}
        for ruta, valor in _plano(ref):
            extraccion.append({"ficha": sub, "campo": ruta, "esperado": valor, "obtenido": hecho.get(ruta),
                               "bien": _igual(valor, hecho.get(ruta))})
    tokens = sum(_j(f).get("tokens") or 0 for f in (carpeta / "salidas").glob("*.json"))
    res = {"entidad": clave["entidad"], "agentes": sorted(corridos), "tokens": tokens,
           "senales": {"esperadas": len(esperado), "acertadas": len(ok), "de_mas": sorted(map(list, sobran)),
                       "faltantes": sorted(map(list, faltan))},
           "extraccion": {"campos": len(extraccion), "bien": sum(x["bien"] for x in extraccion),
                          "mal": [x for x in extraccion if not x["bien"]]}}
    _w(carpeta / "calificacion.json", res)
    print(f"{clave['entidad']} · {', '.join(res['agentes'])} · {tokens / 1e6:.2f} M tokens")
    print(f"  señales: {len(ok)} de {len(esperado)} esperadas, {len(sobran)} de más, {len(faltan)} faltantes")
    print(f"  extracción: {res['extraccion']['bien']} de {res['extraccion']['campos']} campos bien")
    return 0 if not sobran and not faltan and not res["extraccion"]["mal"] else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="accion", required=True)
    s = sp.add_parser("armar")
    s.add_argument("carpeta")
    s.add_argument("--entidad", required=True, choices=sorted(d.name for d in MATERIAL.iterdir() if d.is_dir()))
    s = sp.add_parser("correr")
    s.add_argument("carpeta")
    s.add_argument("--tope", type=int, required=True, help="tokens; la ronda para antes del comando que lo pase")
    s.add_argument("--limite", type=int, default=900, help="segundos por comando")
    s.add_argument("--solo", type=int, nargs="*")
    s = sp.add_parser("calificar")
    s.add_argument("carpeta")
    a = ap.parse_args()
    return {"armar": armar, "correr": correr, "calificar": calificar}[a.accion](a)


if __name__ == "__main__":
    sys.exit(main())
