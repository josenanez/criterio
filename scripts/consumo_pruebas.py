#!/usr/bin/env python3
"""Lo que cuesta cada comando en las pruebas, para que Rostrum lo muestre al lado del consumo real.

    python3 scripts/consumo_pruebas.py            escribe plugins/criterio-server/scripts/consumo-pruebas.json
    python3 scripts/consumo_pruebas.py --check    falla si el archivo no es lo que sale de la evidencia

Sale de cada corrida publicada: `tests/evidencias/familias/<sigla>/ronda-N/<carpeta>/salidas/*.json`
y, en la PMO, `tests/evidencias/rondas/ronda-N/<industria>/salidas/*.json`. Cuenta solo la primera
corrida de cada comando, no las que se repitieron después de corregir un defecto (`repetidas/`).
Los tokens son los que informa Claude Code: entrada, escritura y lectura de caché, y salida.
"""
import argparse
import json
import statistics as st
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "plugins" / "criterio-server" / "scripts" / "consumo-pruebas.json"
REGISTRO = RAIZ / "plugins" / "criterio-server" / "scripts" / "agentes.json"


def corridas() -> list[tuple[str, dict]]:
    """(ronda, salida) de cada comando corrido en una ronda publicada."""
    ev = RAIZ / "tests" / "evidencias"
    rutas = sorted(ev.glob("familias/*/ronda-*/*/salidas/*.json")) + sorted(ev.glob("rondas/ronda-*/*/salidas/*.json"))
    return [(p.parent.parent.parent.name, json.loads(p.read_text(encoding="utf-8"))) for p in rutas]


def resumen() -> dict:
    agentes = {a["id"]: a for a in json.loads(REGISTRO.read_text(encoding="utf-8"))["agentes"]}
    por = {}
    for _, x in corridas():
        a, c, t = x.get("agente"), x.get("comando"), x.get("tokens")
        if a not in agentes or not c or not t:
            continue
        por.setdefault(a, {}).setdefault(c, []).append((t, x.get("tokens_salida") or 0, x.get("turnos") or 0))
    salida = {"nota": "Generado por scripts/consumo_pruebas.py desde las corridas publicadas en tests/evidencias; no se edita a mano.",
              "agentes": {}}
    for a in sorted(por, key=lambda k: (agentes[k]["familia"], k)):
        cmds = {}
        for c, v in sorted(por[a].items()):
            cmds[c] = {"corridas": len(v), "mediana": round(st.median(t for t, _, _ in v)),
                       "maximo": max(t for t, _, _ in v), "mediana_salida": round(st.median(s for _, s, _ in v)),
                       "mediana_turnos": round(st.median(n for _, _, n in v))}
        salida["agentes"][a] = {"familia": agentes[a]["familia"], "comandos": cmds,
                                "pasada": sum(x["mediana"] for x in cmds.values())}
    return salida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    texto = json.dumps(resumen(), ensure_ascii=False, indent=1) + "\n"
    if ap.parse_args().check:
        if not SALIDA.is_file() or SALIDA.read_text(encoding="utf-8") != texto:
            print(f"{SALIDA.relative_to(RAIZ)} no es lo que sale de la evidencia: corre scripts/consumo_pruebas.py")
            return 1
        print("el consumo de las pruebas coincide con la evidencia")
        return 0
    SALIDA.write_text(texto, encoding="utf-8")
    d = json.loads(texto)["agentes"]
    print(f"{SALIDA.relative_to(RAIZ)} · {len(d)} agentes · {sum(len(x['comandos']) for x in d.values())} comandos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
