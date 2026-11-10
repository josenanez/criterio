#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las descargas de Criterio, día por día, sin perder ninguno, y las estrellas y los forks de cada día.

    python3 scripts/descargas.py capturar --csv descargas.csv     lee el tráfico de GitHub y lo suma al historial
    python3 scripts/descargas.py resumen --csv descargas.csv      el acumulado, los últimos siete días y cada mes
    python3 scripts/descargas.py cifra --csv descargas.csv        la cifra de siempre, en una línea
    python3 scripts/descargas.py insignia --csv descargas.csv --dir .   la insignia del README, en los dos idiomas y los dos temas
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
corrige al día siguiente; un día que salió de la ventana de GitHub ya no cambia. Por eso el promedio
y las barras de la insignia cuentan solo los días completos: hasta ayer.

**La insignia del README** sale de aquí y de nada más: el promedio diario y las barras de los últimos
veintiocho días, sin acumulados ni fechas. El flujo diario la escribe en la rama `descargas`, junto al
CSV, y los README la toman de ahí.

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
import html
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
    # Una celda vacía es un dato que no se leyó, no un cero: el tráfico de un día sin token, las
    # estrellas de un día sin captura.
    return None if v in (None, "") else int(v)


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
        fila = out.setdefault(hoy, dict({k: None for k in TRAFICO}, fecha=hoy))
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
    """El acumulado del historial, su promedio por día con tráfico leído, los últimos siete días
    completos con su récord y la suma de cada mes. Los
    únicos de GitHub son por día: sumarlos cuenta dos veces a quien volvió otro día, así que el
    resumen dice clonaciones, no personas."""
    siete = {(hoy - dt.timedelta(days=k)).isoformat() for k in range(1, 8)}
    c = lambda v, k="clonaciones": v.get(k) or 0
    meses: dict[str, int] = {}
    for f, v in filas.items():
        meses[f[:7]] = meses.get(f[:7], 0) + c(v)
    ultimo = next((v for v in reversed(filas.values()) if v.get("estrellas") is not None), None)
    # El día en curso llega incompleto: el promedio cuenta hasta ayer.
    leidos = {f: v for f, v in filas.items() if v.get("clonaciones") is not None and f < hoy.isoformat()}
    semana = [(f, v["clonaciones"]) for f, v in leidos.items() if f in siete]
    record = max(semana, key=lambda x: (x[1], x[0]), default=None)
    return {"desde": next(iter(filas), None), "hasta": max(leidos, default=None), "dias": len(filas),
            "clonaciones": sum(c(v) for v in filas.values()),
            "dias_con_trafico": len(leidos),
            "promedio_diario": round(sum(c(v) for v in leidos.values()) / len(leidos), 1) if leidos else 0,
            "record_7_dias": {"fecha": record[0], "clonaciones": record[1]} if record else None,
            "dias_sin_trafico": sorted(f for f, v in filas.items() if v.get("clonaciones") is None),
            "estrellas": ultimo and ultimo["estrellas"], "forks": ultimo and ultimo["forks"],
            "estrellas_y_forks_al": ultimo and ultimo["fecha"],
            "visitas": sum(c(v, "visitas") for v in filas.values()),
            "ultimos_7_dias": sum(c(v) for f, v in filas.items() if f in siete),
            "por_mes": meses}


def cifra(r: dict) -> str:
    """La cifra que se da siempre, igual cada vez: el acumulado, el promedio por día con tráfico leído y
    el récord de los últimos siete días completos. Son clonaciones, no personas."""
    rec = r["record_7_dias"]
    fmt = lambda n, d=0: f"{n:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", ".")
    return (f"Descargas al {r['hasta']}: {fmt(r['clonaciones'])} acumuladas · {fmt(r['promedio_diario'], 1)} por día en "
            f"promedio ({r['dias_con_trafico']} días) · récord de la última semana: "
            + (f"{fmt(rec['clonaciones'])}, el {rec['fecha']}" if rec else "sin tráfico leído"))


# ---------------------------------------------------------------- la insignia del README

DIAS_BARRAS = 28
TEMAS = {
    "claro": {"fondo": "#f5f4ef", "borde": "#d8d5cd", "cifra": "#111111", "oro": "#8a6327", "apagado": "#6b675f", "texto": "#3f4450"},
    "oscuro": {"fondo": "#050505", "borde": "#2b2b28", "cifra": "#f5f4ef", "oro": "#d5a84b", "apagado": "#8a867e", "texto": "#c9c6bd"},
}
TEXTOS = {
    "es": {"eyebrow": "DESCARGAS DIARIAS", "k": "en promedio, desde el lanzamiento",
           "pie": f"Clonaciones del repositorio · las barras, los últimos {DIAS_BARRAS} días · se actualiza a diario",
           "alt": "Criterio: {n} descargas diarias en promedio, desde el lanzamiento"},
    "en": {"eyebrow": "DAILY DOWNLOADS", "k": "on average, since launch",
           "pie": f"Repository clones · the bars, the last {DIAS_BARRAS} days · updated daily",
           "alt": "Criterio: {n} downloads a day on average, since launch"},
}
FUENTE = "'Inter Tight', Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def barras(filas: dict[str, dict], hoy: dt.date) -> list[int | None]:
    """Las clonaciones de los últimos días completos, del más viejo a ayer; un día sin tráfico leído
    queda sin barra."""
    return [(filas.get((hoy - dt.timedelta(days=k)).isoformat()) or {}).get("clonaciones") for k in range(DIAS_BARRAS, 0, -1)]


def insignia(r: dict, serie: list[int | None], idioma: str, tema: str) -> str:
    """La insignia: el promedio diario, grande, y las barras de cada día. Sin acumulados ni fechas."""
    c, x = TEMAS[tema], TEXTOS[idioma]
    n = f"{round(r['promedio_diario']):,}".replace(",", "." if idioma == "es" else ",")
    W, H = 520, 156
    x0, x1, y0, y1 = 228, 496, 30, 112
    paso = (x1 - x0) / len(serie)
    ancho, radio = paso * 0.68, 2.0
    tope = max([v for v in serie if v] or [1])
    marcas = []
    for i, v in enumerate(serie):
        if not v:
            continue
        a = max((y1 - y0) * v / tope, radio * 2)
        bx, by = x0 + i * paso + (paso - ancho) / 2, y1 - a
        marcas.append(f'<path d="M{bx:.1f},{y1}V{by + radio:.1f}Q{bx:.1f},{by:.1f} {bx + radio:.1f},{by:.1f}'
                      f'H{bx + ancho - radio:.1f}Q{bx + ancho:.1f},{by:.1f} {bx + ancho:.1f},{by + radio:.1f}V{y1}Z"/>')
    alt = html.escape(x["alt"].format(n=n))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{alt}">'
            f'<title>{alt}</title>'
            f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="{c["fondo"]}" stroke="{c["borde"]}"/>'
            f'<g font-family="{FUENTE}">'
            f'<text x="24" y="38" font-size="11" font-weight="600" letter-spacing="1.6" fill="{c["oro"]}">{x["eyebrow"]}</text>'
            f'<text x="22" y="92" font-size="56" font-weight="600" letter-spacing="-2" fill="{c["cifra"]}">{n}</text>'
            f'<text x="24" y="112" font-size="12.5" fill="{c["texto"]}">{html.escape(x["k"])}</text>'
            f'<text x="24" y="138" font-size="11" fill="{c["apagado"]}">{html.escape(x["pie"])}</text>'
            f'</g>'
            f'<line x1="{x0}" y1="{y1 + .5}" x2="{x1}" y2="{y1 + .5}" stroke="{c["borde"]}"/>'
            f'<g fill="{c["oro"]}">{"".join(marcas)}</g>'
            f'</svg>\n')


def insignias(filas: dict[str, dict], hoy: dt.date, carpeta: Path) -> list[Path]:
    """Las cuatro: español e inglés, en tema claro y oscuro. El README elige el tema con <picture>."""
    r, serie = resumen(filas, hoy), barras(filas, hoy)
    carpeta.mkdir(parents=True, exist_ok=True)
    out = []
    for idioma in TEXTOS:
        for tema in TEMAS:
            p = carpeta / f"descargas-{idioma}-{tema}.svg"
            p.write_text(insignia(r, serie, idioma, tema), encoding="utf-8")
            out.append(p)
    return out


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
    ok("el promedio, sobre los días con tráfico leído", resumen(h, dt.date(2026, 10, 31))["promedio_diario"], 63.3)
    ok("el récord de la semana, con su fecha", resumen(h, dt.date(2026, 10, 31))["record_7_dias"], {"fecha": "2026-10-29", "clonaciones": 80})
    ok("la cifra, en una línea", cifra(resumen(h, dt.date(2026, 10, 31))),
       "Descargas al 2026-10-30: 190 acumuladas · 63,3 por día en promedio (3 días) · récord de la última semana: 80, el 2026-10-29")
    h = fusionar(h, {}, "2026-10-31", {"estrellas": 3, "forks": 1})
    ok("las estrellas y los forks van al día de la captura", (h["2026-10-31"]["estrellas"], h["2026-10-31"]["forks"]), (3, 1))
    ok("un día sin captura queda sin estrellas", h["2026-10-30"]["estrellas"], None)
    ok("un día que solo tiene estrellas no inventa un tráfico de cero", h["2026-10-31"]["clonaciones"], None)
    ok("y el resumen lo dice como un día sin tráfico", resumen(h, dt.date(2026, 11, 1))["dias_sin_trafico"], ["2026-10-31"])
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
    hi = fusionar({}, por_dia({"clones": [{"timestamp": "2026-11-08T00:00:00Z", "count": 90, "uniques": 9},
                                          {"timestamp": "2026-11-09T00:00:00Z", "count": 70, "uniques": 7},
                                          {"timestamp": "2026-11-10T00:00:00Z", "count": 3, "uniques": 1}]}, {"views": []}), "2026-11-10")
    ri = resumen(hi, dt.date(2026, 11, 10))
    ok("el promedio no cuenta el día en curso, que llega incompleto", ri["promedio_diario"], 80.0)
    ok("las barras terminan ayer y un día sin tráfico no tiene barra", (barras(hi, dt.date(2026, 11, 10))[-2:], barras(hi, dt.date(2026, 11, 10))[0]), ([90, 70], None))
    import xml.etree.ElementTree as ET
    svg = insignia(ri, barras(hi, dt.date(2026, 11, 10)), "es", "oscuro")
    ok("la insignia es un SVG válido", ET.fromstring(svg).tag, "{http://www.w3.org/2000/svg}svg")
    ok("la insignia dice el promedio, con dos barras", (">80<" in svg, svg.count("<path")), (True, 2))
    ok("y no dice el acumulado ni fechas", ("163" in svg, "2026" in svg), (False, False))
    print("\n" + ("OK" if not fallas else f"{len(fallas)} FALLAS"))
    return 1 if fallas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Las descargas de Criterio, día por día.")
    ap.add_argument("accion", choices=["capturar", "resumen", "cifra", "insignia", "selftest"])
    ap.add_argument("--csv", type=Path, default=Path("descargas.csv"))
    ap.add_argument("--dir", type=Path, default=Path("."), help="dónde escribe `insignia` sus cuatro SVG")
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
    if a.accion == "cifra":
        print(cifra(resumen(filas, hoy)))
        return 0
    if a.accion == "insignia":
        for p in insignias(filas, hoy, a.dir):
            print(p)
        return 0
    print(json.dumps(resumen(filas, hoy), ensure_ascii=False, indent=2))
    if a.accion == "capturar":
        # En el registro del flujo diario, la cifra de siempre debajo del detalle. `resumen` da solo el
        # JSON, que lee el video de Criterio (docs/video/grabar.mjs).
        print(cifra(resumen(filas, hoy)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
