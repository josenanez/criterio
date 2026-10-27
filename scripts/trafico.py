#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cuántos instalan o actualizan Criterio, medido igual cada vez.

    python3 scripts/trafico.py              lee GitHub con `gh`, suma al histórico y lo resume
    python3 scripts/trafico.py --selftest   la cuenta, sobre datos fijos

GitHub guarda el tráfico de clonación solo 14 días, así que el histórico se acumula aquí, en
`.pruebas/trafico.csv`, que no se versiona: un día ya guardado se reemplaza con el dato más nuevo.

**El punto de medición.** Cada instalación y cada actualización del marketplace clona el
repositorio; también lo clona la validación de GitHub Actions en cada push a `main`. La cuenta es:

    clonadores únicos de la ventana − pushes a main en esa misma ventana

Los pushes salen del reflog de `origin/main` de este equipo, uno por cada «update by push». Es una
cota baja: si un runner de la validación no cuenta como clonador único, la cifra real es mayor. Y
no son personas: una misma persona que actualiza desde otra red cuenta otra vez. La referencia
acordada para compararla es 210.

Necesita `gh` con sesión: el tráfico de un repositorio solo lo ve quien puede escribir en él.
"""
from __future__ import annotations

import csv
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REPO = "josenanez/criterio"
HISTORICO = RAIZ / ".pruebas" / "trafico.csv"
REFERENCIA = 210
CAMPOS = ["dia", "clonaciones", "clonadores_unicos", "pushes", "visitas", "visitantes_unicos"]


def gh(ruta: str) -> dict:
    return json.loads(subprocess.run(["gh", "api", f"repos/{REPO}/{ruta}"], check=True,
                                     capture_output=True, text=True).stdout)


def pushes_por_dia() -> Counter:
    """Un push a main por cada «update by push» del reflog de origin/main, por día."""
    salida = subprocess.run(["git", "-C", str(RAIZ), "reflog", "show", "--date=format:%Y-%m-%d",
                             "refs/remotes/origin/main"], capture_output=True, text=True).stdout
    dias = Counter()
    for linea in salida.splitlines():
        if "update by push" in linea and "@{" in linea:
            dias[linea.split("@{", 1)[1].split("}", 1)[0]] += 1
    return dias


def filas(clones: dict, visitas: dict, pushes: Counter) -> list[dict]:
    vis = {v["timestamp"][:10]: v for v in visitas.get("views", [])}
    out = []
    for c in clones.get("clones", []):
        d = c["timestamp"][:10]
        out.append({"dia": d, "clonaciones": c["count"], "clonadores_unicos": c["uniques"], "pushes": pushes.get(d, 0),
                    "visitas": vis.get(d, {}).get("count", 0), "visitantes_unicos": vis.get(d, {}).get("uniques", 0)})
    return out


def ventana(clones: dict, nuevas: list[dict]) -> dict:
    unicos, pushes = clones.get("uniques", 0), sum(f["pushes"] for f in nuevas)
    return {"desde": nuevas[0]["dia"] if nuevas else None, "hasta": nuevas[-1]["dia"] if nuevas else None,
            "clonaciones": clones.get("count", 0), "clonadores_unicos": unicos, "pushes": pushes,
            "estimado": max(0, unicos - pushes)}


def guardar(nuevas: list[dict]) -> list[dict]:
    previas = {}
    if HISTORICO.is_file():
        with HISTORICO.open(encoding="utf-8") as fh:
            previas = {r["dia"]: r for r in csv.DictReader(fh)}
    for f in nuevas:
        previas[f["dia"]] = {k: str(v) for k, v in f.items()}
    todas = [previas[d] for d in sorted(previas)]
    HISTORICO.parent.mkdir(parents=True, exist_ok=True)
    with HISTORICO.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(todas)
    return todas


def resumen(v: dict) -> str:
    cambio = (v["estimado"] - REFERENCIA) / REFERENCIA * 100
    return (f"Ventana {v['desde']} a {v['hasta']}: {v['clonaciones']} clonaciones, {v['clonadores_unicos']} clonadores "
            f"únicos y {v['pushes']} pushes a main.\n"
            f"Instalaciones o actualizaciones, cota baja: {v['estimado']} ({cambio:+.0f} % frente a la referencia de {REFERENCIA}).")


def selftest() -> int:
    clones = {"count": 30, "uniques": 12, "clones": [{"timestamp": "2026-10-20T00:00:00Z", "count": 20, "uniques": 8},
                                                     {"timestamp": "2026-10-21T00:00:00Z", "count": 10, "uniques": 6}]}
    visitas = {"views": [{"timestamp": "2026-10-21T00:00:00Z", "count": 3, "uniques": 1}]}
    f = filas(clones, visitas, Counter({"2026-10-20": 3, "2026-10-19": 9}))
    v = ventana(clones, f)
    casos = [("cada día con su clonación, sus pushes y sus visitas", [(x["dia"], x["pushes"], x["visitas"]) for x in f],
              [("2026-10-20", 3, 0), ("2026-10-21", 0, 3)]),
             ("los pushes fuera de la ventana no se restan", v["pushes"], 3),
             ("la cota baja: únicos de la ventana menos sus pushes", v["estimado"], 9)]
    fallas = 0
    for nombre, obtenido, esperado in casos:
        ok = obtenido == esperado
        fallas += not ok
        print(f"  {'ok' if ok else 'FALLA'}  {nombre}" + ("" if ok else f": {obtenido!r} en lugar de {esperado!r}"))
    print("\nOK" if not fallas else f"\n{fallas} FALLAS")
    return 1 if fallas else 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    clones, visitas = gh("traffic/clones"), gh("traffic/views")
    nuevas = filas(clones, visitas, pushes_por_dia())
    guardar(nuevas)
    print(resumen(ventana(clones, nuevas)))
    print(f"Histórico en {HISTORICO.relative_to(RAIZ)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
