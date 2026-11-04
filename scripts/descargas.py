#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las descargas de Criterio, día por día, sin perder ninguno, y las estrellas y los forks de cada día.

    python3 scripts/descargas.py capturar --csv descargas.csv     lee el tráfico de GitHub y lo suma al historial
    python3 scripts/descargas.py resumen --csv descargas.csv      el acumulado, los últimos siete días y cada mes
    python3 scripts/descargas.py selftest

**GitHub guarda solo los últimos catorce días.** La cifra que muestra la pestaña de tráfico —las
clonaciones, que es como `claude plugin marketplace add` trae el repositorio, y las visitas— es la
suma de esa ventana, no un acumulado: cuando un día sale de la ventana, la cifra baja aunque nadie
haya dejado de descargar. Este script guarda cada día con su cifra en un CSV y suma el historial
completo. Corre a diario (`.github/workflows/descargas.yml`); con eso, ningún día se pierde.

**Las estrellas y los forks son un acumulado, no una ventana.** GitHub dice cuántos hay hoy, no
cuántos hubo ayer: cada captura anota en la fila del día en que corre el número de ese momento. Un
día sin captura queda sin ese dato; no se rellena.

**Cada día se guarda una sola vez, con su última lectura.** El día en curso llega incompleto y se
corrige al día siguiente; un día que salió de la ventana de GitHub ya no cambia.

El tráfico pide el token de quien administra el repositorio, en la variable `TRAFFIC_TOKEN` (en
GitHub, un secreto del repositorio con permiso de lectura de administración). Las estrellas y los
forks son públicos: bastan `GITHUB_TOKEN`, el del flujo, o ningún token. Sin `TRAFFIC_TOKEN`, usa la
sesión de `gh` si existe; si tampoco, guarda las estrellas y los forks y avisa que el tráfico no se
leyó. Este script nunca escribe un token en ningún archivo.
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
import urllib.error
import urllib.request
from pathlib import Path

REPO = "josenanez/criterio"
CAMPOS = ["fecha", "clonaciones", "clonadores_unicos", "visitas", "visitantes_unicos", "estrellas", "forks", "capturado"]
TRAFICO = ("clonaciones", "clonadores_unicos", "visitas", "visitantes_unicos")
# Las estrellas y los forks de un día sin captura quedan vacíos: no hay de dónde saberlos.
ACUMULADOS = ("estrellas", "forks")


class SinAcceso(Exception):
    """No hay cómo leer esa ruta de la API: falta el token o no alcanza su permiso."""


def _api(ruta: str, variable: str = "TRAFFIC_TOKEN") -> dict:
    """Una lectura de la API de GitHub: con el token de `variable` si está, si no con `gh api`."""
    token = os.environ.get(variable)
    if token:
        req = urllib.request.Request(f"https://api.github.com/{ruta}", headers={
            "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise SinAcceso(f"{ruta}: HTTP {e.code} con {variable}") from e
    if shutil.which("gh"):
        r = subprocess.run(["gh", "api", ruta], capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            return json.loads(r.stdout)
        raise SinAcceso(f"gh api {ruta}: {r.stderr.strip()}")
    raise SinAcceso(f"sin {variable} y sin gh: no hay cómo leer {ruta}")


def repositorio(repo: str) -> dict:
    """Las estrellas y los forks de hoy. Son públicos: el token del flujo basta, y sin ninguno
    también se leen."""
    try:
        d = _api(f"repos/{repo}", "GITHUB_TOKEN")
    except SinAcceso:
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={"Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode("utf-8"))
    return {"estrellas": int(d.get("stargazers_count") or 0), "forks": int(d.get("forks_count") or 0)}


def por_dia(clones: dict, vistas: dict) -> dict[str, dict]:
    """Los días que trae GitHub, con sus cuatro cifras. La API los fecha a medianoche UTC."""
    out: dict[str, dict] = {}
    for clave, datos, total, unicos in (("c", clones, "clonaciones", "clonadores_unicos"), ("v", vistas, "visitas", "visitantes_unicos")):
        for x in datos.get("clones" if clave == "c" else "views") or []:
            d = out.setdefault(str(x["timestamp"])[:10], {"clonaciones": 0, "clonadores_unicos": 0, "visitas": 0, "visitantes_unicos": 0})
            d[total], d[unicos] = int(x.get("count") or 0), int(x.get("uniques") or 0)
    return out


def _celda(k: str, v: str | None):
    if k in ("fecha", "capturado"):
        return v or ""
    if v in (None, ""):
        return None if k in ACUMULADOS else 0
    return int(v)


def leer(csv_: Path) -> dict[str, dict]:
    """El historial. Un CSV escrito antes de que existieran las estrellas y los forks se lee con
    esas dos columnas vacías."""
    if not csv_.is_file():
        return {}
    with csv_.open(encoding="utf-8", newline="") as f:
        return {r["fecha"]: {k: _celda(k, r.get(k)) for k in CAMPOS} for r in csv.DictReader(f)}


def fusionar(historial: dict[str, dict], nuevos: dict[str, dict], hoy: str, repo: dict | None = None) -> dict[str, dict]:
    """El historial con la lectura nueva: un día que GitHub todavía trae toma su última lectura del
    tráfico; uno que ya no trae se conserva como quedó. Las estrellas y los forks van al día de la
    captura, y los de un día anterior no se tocan."""
    out = {k: dict(v) for k, v in historial.items()}
    for fecha, v in nuevos.items():
        previo = out.get(fecha) or {}
        out[fecha] = dict({k: previo.get(k) for k in ACUMULADOS}, **v, fecha=fecha, capturado=hoy)
    if repo is not None:
        fila = out.setdefault(hoy, dict({k: 0 for k in TRAFICO}, fecha=hoy))
        fila.update(repo, capturado=hoy)
    return dict(sorted(out.items()))


def escribir(csv_: Path, filas: dict[str, dict]) -> None:
    csv_.parent.mkdir(parents=True, exist_ok=True)
    with csv_.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        for v in filas.values():
            w.writerow({k: ("" if v.get(k) is None else v[k]) for k in CAMPOS})


def resumen(filas: dict[str, dict], hoy: dt.date) -> dict:
    """El acumulado del historial, los últimos siete días completos y la suma de cada mes. Los
    únicos de GitHub son por día: sumarlos cuenta dos veces a quien volvió otro día, así que el
    resumen dice clonaciones, no personas."""
    siete = {(hoy - dt.timedelta(days=k)).isoformat() for k in range(1, 8)}
    meses: dict[str, int] = {}
    for f, v in filas.items():
        meses[f[:7]] = meses.get(f[:7], 0) + v["clonaciones"]
    ultimo = next((v for v in reversed(filas.values()) if v.get("estrellas") is not None), None)
    return {"desde": next(iter(filas), None), "dias": len(filas),
            "clonaciones": sum(v["clonaciones"] for v in filas.values()),
            "estrellas": ultimo and ultimo["estrellas"], "forks": ultimo and ultimo["forks"],
            "estrellas_y_forks_al": ultimo and ultimo["fecha"],
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
    h = fusionar(h, {}, "2026-10-31", {"estrellas": 3, "forks": 1})
    ok("las estrellas y los forks van al día de la captura", (h["2026-10-31"]["estrellas"], h["2026-10-31"]["forks"]), (3, 1))
    ok("un día sin captura queda sin estrellas", h["2026-10-30"]["estrellas"], None)
    c3 = {"clones": [{"timestamp": "2026-10-31T00:00:00Z", "count": 7, "uniques": 2}]}
    h = fusionar(h, por_dia(c3, {"views": []}), "2026-11-01", {"estrellas": 4, "forks": 1})
    ok("la lectura del tráfico de un día no borra sus estrellas", (h["2026-10-31"]["clonaciones"], h["2026-10-31"]["estrellas"]), (7, 3))
    ok("el resumen da las estrellas y los forks de la última captura",
       [resumen(h, dt.date(2026, 11, 2))[k] for k in ("estrellas", "forks", "estrellas_y_forks_al")], [4, 1, "2026-11-01"])
    with tempfile.TemporaryDirectory() as t:
        p = Path(t) / "d.csv"
        escribir(p, h)
        ok("el CSV se lee como se escribió", leer(p), h)
        viejo = Path(t) / "viejo.csv"
        viejo.write_text("fecha,clonaciones,clonadores_unicos,visitas,visitantes_unicos,capturado\n2026-10-20,5,2,9,3,2026-10-21\n", encoding="utf-8")
        ok("un historial anterior a las estrellas se lee con ellas vacías", (leer(viejo)["2026-10-20"]["clonaciones"], leer(viejo)["2026-10-20"]["forks"]), (5, None))
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
        repo = repositorio(a.repo)
        try:
            nuevos = por_dia(_api(f"repos/{a.repo}/traffic/clones?per=day"), _api(f"repos/{a.repo}/traffic/views?per=day"))
        except SinAcceso as e:
            # Sin el tráfico, el día conserva sus estrellas y sus forks; el aviso sale en el flujo.
            nuevos = {}
            print(f"::warning::El tráfico no se leyó ({e}). Falta el secreto TRAFFIC_TOKEN o su permiso de lectura de administración: "
                  "GitHub guarda solo catorce días, y cada día sin leer se pierde.")
        filas = fusionar(filas, nuevos, hoy.isoformat(), repo)
        escribir(a.csv, filas)
        print(f"{len(nuevos)} días de tráfico leídos de GitHub · {repo['estrellas']} estrellas y {repo['forks']} forks · "
              f"{len(filas)} días en el historial")
    print(json.dumps(resumen(filas, hoy), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
