#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 2: cada agente sobre un corpus pequeño con casos sembrados, un comando a la vez.

    python3 tests/fase2.py armar vera        arma .pruebas/vera-mini desde corp-demo
    python3 tests/fase2.py calificar vera    califica el estado de Vera contra la clave

El corpus grande (51 proyectos, 350 documentos) sirve para las cifras de venta y cuesta
25 minutos por barrido. Para depurar sirve uno pequeño: los proyectos de corp-demo que,
juntos, cubren cada señal de la clave, más el control negativo. Un comando que falla
aquí falla en dos minutos y se sabe en qué proyecto.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import fiabilidad  # noqa: E402

FUENTE = RAIZ / ".pruebas" / "corp-demo"
MINI = {"vera": RAIZ / ".pruebas" / "vera-mini"}


def _senales(lista) -> list:
    return [x["signal"] if isinstance(x, dict) else x for x in lista]


def elegir(esperado: dict, controles: list) -> list:
    """Los proyectos que cubren todas las señales de la clave, de a uno, más los controles."""
    filas = {k: set(_senales(v)) for k, v in esperado.items() if k.startswith("PRY")}
    falta, elegidos = set().union(*filas.values()), []
    while falta:
        k = max(sorted(filas), key=lambda c: len(filas[c] & falta))
        if not filas[k] & falta:
            break
        elegidos.append(k)
        falta -= filas[k]
    return sorted(set(elegidos) | {c for c in controles if c.startswith("PRY")})


def armar_vera() -> None:
    clave = json.loads((FUENTE / "esperado.json").read_text(encoding="utf-8"))
    codigos = elegir(clave["esperado"], clave.get("controles", []))
    destino = MINI["vera"]
    docs = destino / "documentos" / "proyectos"
    if destino.exists():
        sys.exit(f"{destino} ya existe; no se reescribe una prueba en curso")
    docs.mkdir(parents=True)
    origen = FUENTE / "documentos" / "proyectos"
    for c in codigos:
        carpeta = next(d for d in origen.iterdir() if d.name.startswith(c + "-"))
        shutil.copytree(carpeta, docs / carpeta.name)
    (destino / "estado").mkdir()
    (destino / "reportes").mkdir()
    sub = {k: v for k, v in clave["esperado"].items() if k in codigos}
    (destino / "esperado.json").write_text(json.dumps(
        {"hoy": clave["hoy"], "controles": [c for c in clave.get("controles", []) if c in codigos],
         "esperado": sub, "de": "corp-demo"}, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(1 for _ in docs.rglob("*") if _.is_file())
    print(f"{len(codigos)} proyectos, {n} documentos: {', '.join(codigos)}")
    for c in codigos:
        print(f"  {c}: {', '.join(sorted(set(_senales(sub[c])))) or 'control: ninguna señal'}")


def calificar_vera() -> int:
    destino = MINI["vera"]
    clave = json.loads((destino / "esperado.json").read_text(encoding="utf-8"))
    esperado = {k: _senales(v) for k, v in clave["esperado"].items()}
    obtenido, _, error = fiabilidad.hallazgos_portafolio(destino / "estado", clave["hoy"])
    if error:
        print("no se pudo calcular:", error)
        return 1
    cal = fiabilidad.calificar(esperado, obtenido)
    t = fiabilidad.totales(cal)
    print(json.dumps(t, ensure_ascii=False))
    for caso, r in sorted(cal["por_caso"].items()):
        marca = "OK" if not r["falsos_negativos"] and not r["falsos_positivos"] else "  "
        print(f"{marca} {caso}: {r['aciertos']}/{r['esperado']}"
              + (f"  faltan {r['falsos_negativos']}" if r["falsos_negativos"] else "")
              + (f"  sobran {r['falsos_positivos']}" if r["falsos_positivos"] else ""))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in MINI or sys.argv[1] not in ("armar", "calificar"):
        sys.exit(__doc__)
    sys.exit({"armar": {"vera": armar_vera}, "calificar": {"vera": calificar_vera}}[sys.argv[1]][sys.argv[2]]() or 0)
