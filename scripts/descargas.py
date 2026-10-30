#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las descargas de Criterio, día por día, sin perder ninguno.

    python3 scripts/descargas.py capturar --csv descargas.csv     lee el tráfico de GitHub y lo suma al historial
    python3 scripts/descargas.py resumen --csv descargas.csv      el acumulado, los últimos siete días y cada mes
    python3 scripts/descargas.py selftest

**GitHub guarda solo los últimos catorce días.** La cifra que muestra la pestaña de tráfico —las
clonaciones, que es como `claude plugin marketplace add` trae el repositorio, y las visitas— es la
suma de esa ventana, no un acumulado: cuando un día sale de la ventana, la cifra baja aunque nadie
haya dejado de descargar. Este script guarda cada día con su cifra en un CSV y suma el historial
completo. Corre a diario (`.github/workflows/descargas.yml`); con eso, ningún día se pierde.

**Cada día se guarda una sola vez, con su última lectura.** El día en curso llega incompleto y se
corrige al día siguiente; un día que salió de la ventana de GitHub ya no cambia.

El token de lectura es de quien administra el repositorio, en la variable `TRAFFIC_TOKEN` (en
GitHub, un secreto del repositorio con permiso de lectura de administración). Sin token, usa la
sesión de `gh` si existe. Este script nunca lo escribe en ningún archivo.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

REPO = "josenanez/criterio"
CAMPOS = ["fecha", "clonaciones", "clonadores_unicos", "visitas", "visitantes_unicos", "capturado"]


def _api(ruta: str) -> dict:
    """Una lectura de la API de GitHub: con `TRAFFIC_TOKEN` si está, si no con `gh api`."""
    token = os.environ.get("TRAFFIC_TOKEN")
    if token:
        req = urllib.request.Request(f"https://api.github.com/{ruta}", headers={
            "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    if shutil.which("gh"):
        r = subprocess.run(["gh", "api", ruta], capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            return json.loads(r.stdout)
        raise SystemExit(f"gh api {ruta}: {r.stderr.strip()}")
    raise SystemExit("sin TRAFFIC_TOKEN y sin gh: no hay cómo leer el tráfico del repositorio")


def por_dia(clones: dict, vistas: dict) -> dict[str, dict]:
    """Los días que trae GitHub, con sus cuatro cifras. La API los fecha a medianoche UTC."""
    out: dict[str, dict] = {}
    for clave, datos, total, unicos in (("c", clones, "clonaciones", "clonadores_unicos"), ("v", vistas, "visitas", "visitantes_unicos")):
        for x in datos.get("clones" if clave == "c" else "views") or []:
            d = out.setdefault(str(x["timestamp"])[:10], {"clonaciones": 0, "clonadores_unicos": 0, "visitas": 0, "visitantes_unicos": 0})
            d[total], d[unicos] = int(x.get("count") or 0), int(x.get("uniques") or 0)
    return out


def leer(csv_: Path) -> dict[str, dict]:
    if not csv_.is_file():
        return {}
    with csv_.open(encoding="utf-8", newline="") as f:
        return {r["fecha"]: {k: (int(r[k]) if k not in ("fecha", "capturado") else r[k]) for k in CAMPOS} for r in csv.DictReader(f)}


def fusionar(historial: dict[str, dict], nuevos: dict[str, dict], hoy: str) -> dict[str, dict]:
    """El historial con la lectura nueva: un día que GitHub todavía trae se reemplaza por su última
    lectura; uno que ya no trae se conserva como quedó."""
    out = {k: dict(v) for k, v in historial.items()}
    for fecha, v in nuevos.items():
        out[fecha] = dict(v, fecha=fecha, capturado=hoy)
    return dict(sorted(out.items()))


def escribir(csv_: Path, filas: dict[str, dict]) -> None:
    csv_.parent.mkdir(parents=True, exist_ok=True)
    with csv_.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for v in filas.values():
            w.writerow({k: v[k] for k in CAMPOS})


def resumen(filas: dict[str, dict], hoy: dt.date) -> dict:
    """El acumulado del historial, los últimos siete días completos y la suma de cada mes. Los
    únicos de GitHub son por día: sumarlos cuenta dos veces a quien volvió otro día, así que el
    resumen dice clonaciones, no personas."""
    siete = {(hoy - dt.timedelta(days=k)).isoformat() for k in range(1, 8)}
    meses: dict[str, int] = {}
    for f, v in filas.items():
        meses[f[:7]] = meses.get(f[:7], 0) + v["clonaciones"]
    return {"desde": next(iter(filas), None), "dias": len(filas),
            "clonaciones": sum(v["clonaciones"] for v in filas.values()),
            "visitas": sum(v["visitas"] for v in filas.values()),
            "ultimos_7_dias": sum(v["clonaciones"] for f, v in filas.items() if f in siete),
            "por_mes": meses}


def selftest() -> int:
    fallas = []

    def ok(nombre, obtenido, esperado):
        print(f"  {'ok' if obtenido == esperado else 'FALLA'}  {nombre}" + ("" if obtenido == esperado else f": {obtenido!r} en lugar de {esperado!r}"))
        if obtenido != esperado:
            fallas.append(nombre)

    c1 = {"clones": [{"timestamp": "2026-10-16T00:00:00Z", "count": 100, "uniques": 40}, {"timestamp": "2026-10-29T00:00:00Z", "count": 50, "uniques": 20}]}
    v1 = {"views": [{"timestamp": "2026-10-29T00:00:00Z", "count": 300, "uniques": 90}]}
    h = fusionar({}, por_dia(c1, v1), "2026-10-29")
    ok("la primera lectura guarda cada día que trae GitHub", (len(h), h["2026-10-29"]["visitas"]), (2, 300))
    # Al día siguiente el 16 ya salió de la ventana y el 29 llega completo.
    c2 = {"clones": [{"timestamp": "2026-10-29T00:00:00Z", "count": 80, "uniques": 30}, {"timestamp": "2026-10-30T00:00:00Z", "count": 10, "uniques": 5}]}
    h = fusionar(h, por_dia(c2, {"views": []}), "2026-10-30")
    ok("un día que salió de la ventana se conserva", h["2026-10-16"]["clonaciones"], 100)
    ok("un día que sigue en la ventana toma su última lectura", h["2026-10-29"]["clonaciones"], 80)
    ok("el acumulado suma el historial, no la ventana", resumen(h, dt.date(2026, 10, 31))["clonaciones"], 190)
    ok("los últimos siete días completos", resumen(h, dt.date(2026, 10, 31))["ultimos_7_dias"], 90)
    with tempfile.TemporaryDirectory() as t:
        p = Path(t) / "d.csv"
        escribir(p, h)
        ok("el CSV se lee como se escribió", leer(p), h)
    print("\n" + ("OK" if not fallas else f"{len(fallas)} FALLAS"))
    return 1 if fallas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Las descargas de Criterio, día por día.")
    ap.add_argument("accion", choices=["capturar", "resumen", "selftest"])
    ap.add_argument("--csv", type=Path, default=Path("descargas.csv"))
    ap.add_argument("--repo", default=REPO)
    a = ap.parse_args()
    if a.accion == "selftest":
        return selftest()
    hoy = dt.datetime.now(dt.timezone.utc).date()
    filas = leer(a.csv)
    if a.accion == "capturar":
        nuevos = por_dia(_api(f"repos/{a.repo}/traffic/clones?per=day"), _api(f"repos/{a.repo}/traffic/views?per=day"))
        filas = fusionar(filas, nuevos, hoy.isoformat())
        escribir(a.csv, filas)
        print(f"{len(nuevos)} días leídos de GitHub · {len(filas)} en el historial")
    print(json.dumps(resumen(filas, hoy), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
