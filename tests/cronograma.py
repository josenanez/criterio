#!/usr/bin/env python3
"""El Gantt y la curva de avance de Rostrum, sobre las fichas que escribieron los agentes en la
corrida más reciente de cada industria. Sin tokens: no corre ningún agente.

    python3 tests/cronograma.py            # prueba y escribe tests/evidencias/cronograma.json
    python3 tests/cronograma.py --revisar  # falla si el json no está al día o tiene fallas

Por cada industria abre lo que la ronda publicó (`estado-del-agente.tgz`), calcula el portafolio
con el motor que se instala (`portafolio.compute`) y dibuja cada proyecto con el informe de
Rostrum (`informe.gantt`, `informe.curva`, `informe.tabla_hitos`). Comprueba que el dibujo dice
lo que el motor calculó, ni más ni menos:

- cada línea base aprobada con fechas es una barra, y el plan vigente otra;
- cada hito tiene su rombo de línea base y su rombo vigente, con su nombre y su estado en palabras;
- ninguna marca cae fuera del área del dibujo;
- la tabla de hitos tiene una fila por hito;
- las tres curvas suben de a un hito, sin pasar de 100 %, y llegan a 100 % cuando todos los hitos
  tienen fecha;
- la curva de cumplidos solo cuenta hitos cumplidos con evidencia hasta el día de corte;
- el avance declarado aparece como punto cuando cae dentro del cronograma;
- un proyecto sin fechas no dibuja nada inventado.

La pantalla —que la página no se desborde a 1280, 768, 390 y 320 px— la prueba `ronda.py rostrum`
en cada ronda.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import tarfile
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SRV = RAIZ / "plugins" / "criterio-server" / "scripts"
sys.path.insert(0, str(SRV))
import informe  # noqa: E402
import portafolio  # noqa: E402

SALIDA = RAIZ / "tests" / "evidencias" / "cronograma.json"
RONDAS = RAIZ / "tests" / "evidencias" / "rondas"


def ultimas() -> dict[str, Path]:
    """La corrida más reciente de cada industria (decisiones 0020 y 0021)."""
    out: dict[str, Path] = {}
    for d in sorted((x for x in RONDAS.glob("ronda-*") if x.is_dir()), key=lambda x: int(x.name.split("-")[-1])):
        for e in d.iterdir():
            if (e / "estado-del-agente.tgz").is_file():
                out[e.name] = e
    return out


def _svg(html: str, rol: str) -> str:
    m = re.search(rf'aria-label="{rol}"><svg viewBox="0 0 (\d+) (\d+)"(.*?)</svg>', html, re.S)
    return m.group(0) if m else ""


def _xs(svg: str) -> list[float]:
    xs = [float(x) for x in re.findall(r'\b(?:x|x1|x2|cx)="(-?[0-9.]+)"', svg)]
    for pts in re.findall(r'points="([^"]+)"', svg):
        xs += [float(p.split(",")[0]) for p in pts.split()]
    return xs


def proyecto(p: dict, hoy: dt.date) -> list[str]:
    """Las fallas del dibujo de un proyecto; vacía si dice lo que el motor calculó."""
    s = p.get("schedule") or {}
    fallas: list[str] = []
    g, c = informe.gantt(s), informe.curva(s, {"pct": (p.get("declared") or {}).get("progress_pct"),
                                                 "date": (p.get("declared") or {}).get("as_of")})
    dom = informe._dominio(s)
    if not dom:
        if "vacio" not in g:
            fallas.append("sin fechas dibuja un Gantt")
        return fallas
    svg = _svg(g, "Gantt de línea base contra vigente")
    if not svg:
        return ["con fechas no dibuja el Gantt"]
    ancho = informe.ANCHO_GRAFICO
    barras = len(re.findall(r"<rect ", svg))
    esperadas = sum(1 for b in s.get("baselines") or [] if b.get("start") and b.get("end")) + bool(s.get("start") and s.get("end"))
    if barras != esperadas:
        fallas.append(f"{barras} barras y el motor da {esperadas}")
    hitos = s.get("milestones") or []
    rombos = len(re.findall(r"<polygon ", svg))
    esperados = sum(bool(h.get("baseline")) + bool(h.get("current")) for h in hitos)
    if rombos != esperados:
        fallas.append(f"{rombos} rombos y el motor da {esperados}")
    for h in hitos:
        nombre = informe.e(informe._recorta(h.get("name") or "Hito sin nombre", 30))
        if f">{nombre}</text>" not in svg:
            fallas.append(f"el hito «{h.get('name')}» no tiene su nombre")
        palabra = informe.ESTADO_HITO.get(h.get("status"), ("—",))[0]
        if h.get("current") and f"vigente {h['current']} · {palabra}" not in svg:
            fallas.append(f"el hito «{h.get('name')}» no dice su estado en palabras")
    fuera = [x for x in _xs(svg) if not 0 <= x <= ancho]
    if fuera:
        fallas.append(f"{len(fuera)} marcas fuera del dibujo")
    if hitos and informe.tabla_hitos(s).count("<tr>") != len(hitos) + 1:
        fallas.append("la tabla de hitos no trae una fila por hito")

    cur = s.get("curve")
    if hitos:
        if not cur:
            return fallas + ["con hitos no hay curva"]
        svgc = _svg(c, "Curva de avance por hitos")
        if not svgc:
            return fallas + ["con hitos no dibuja la curva"]
        n = cur["milestones"]
        for k in ("baseline", "current", "met"):
            pcts = [x["pct"] for x in cur[k]]
            fechas = [x["date"] for x in cur[k]]
            if fechas != sorted(fechas) or pcts != sorted(pcts) or any(not 0 < v <= 100 for v in pcts):
                fallas.append(f"la curva {k} no sube de a un hito")
        for k, campo in (("baseline", "baseline"), ("current", "current")):
            if all(h.get(campo) for h in hitos) and (not cur[k] or cur[k][-1]["pct"] != 100):
                fallas.append(f"la curva {k} no llega a 100 % con todos los hitos fechados")
        cumplidos = [h for h in hitos if h["status"] == "met" and h["evidence"] and h["current"]
                     and h["current"] <= hoy.isoformat()]
        if len(cur["met"]) != len(cumplidos):
            fallas.append(f"la curva de cumplidos cuenta {len(cur['met'])} y hay {len(cumplidos)} con evidencia")
        if len(re.findall(r"<circle ", svgc)) != len(cur["met"]):
            fallas.append("un punto de cumplido sin dibujar")
        dec = p.get("declared") or {}
        f = informe._f(dec.get("as_of"))
        if dec.get("progress_pct") is not None and f and dom[0] <= f <= dom[1] and "Avance declarado" not in svgc:
            fallas.append("el avance declarado no aparece")
        fuera = [x for x in _xs(svgc) if not 0 <= x <= ancho]
        if fuera:
            fallas.append(f"{len(fuera)} marcas de la curva fuera del dibujo")
    return fallas


def industria(nombre: str, carpeta: Path) -> dict:
    obj = json.loads((carpeta / "clave" / "objetivos.json").read_text(encoding="utf-8"))
    hoy = dt.date.fromisoformat(obj["hoy"])
    with tempfile.TemporaryDirectory() as t:
        with tarfile.open(carpeta / "estado-del-agente.tgz") as tar:
            miembros = [m for m in tar.getmembers() if m.name.startswith(("estado/records/", ".criterio/portafolio/"))
                        and m.isfile() and ".." not in m.name]
            tar.extractall(t, members=miembros, **({"filter": "data"} if hasattr(tarfile, "data_filter") else {}))
        cfg = Path(t) / ".criterio" / "portafolio" / "config.json"
        th = portafolio.load_thresholds(cfg if cfg.is_file() else None)
        r = portafolio.compute(Path(t) / "estado", hoy, th)
    proyectos = []
    for p in r["projects"]:
        s = p.get("schedule") or {}
        proyectos.append({"codigo": p["code"], "dibuja": bool(informe._dominio(s)),
                          "lineas_base": len(s.get("baselines") or []), "hitos": len(s.get("milestones") or []),
                          "fallas": proyecto(p, hoy)})
    return {"industria": nombre, "ronda": obj["ronda"], "corte": obj["hoy"],
            "proyectos": len(proyectos), "con_gantt": sum(p["dibuja"] for p in proyectos),
            "lineas_base": sum(p["lineas_base"] for p in proyectos), "hitos": sum(p["hitos"] for p in proyectos),
            "con_fallas": [p for p in proyectos if p["fallas"]], "detalle": proyectos}


def correr() -> dict:
    filas = [industria(n, c) for n, c in sorted(ultimas().items())]
    return {"nota": "Escrito por tests/cronograma.py: el Gantt y la curva de Rostrum sobre las fichas de la corrida "
                    "más reciente de cada industria. No se edita a mano.",
            "industrias": len(filas), "proyectos": sum(f["proyectos"] for f in filas),
            "con_gantt": sum(f["con_gantt"] for f in filas), "lineas_base": sum(f["lineas_base"] for f in filas),
            "hitos": sum(f["hitos"] for f in filas), "fallas": sum(len(p["fallas"]) for f in filas for p in f["con_fallas"]),
            "por_industria": filas}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true")
    a = ap.parse_args()
    r = correr()
    texto = json.dumps(r, ensure_ascii=False, indent=2) + "\n"
    if a.revisar:
        if not SALIDA.is_file() or SALIDA.read_text(encoding="utf-8") != texto:
            print("tests/evidencias/cronograma.json no está al día: python3 tests/cronograma.py")
            return 1
    else:
        SALIDA.write_text(texto, encoding="utf-8")
    for f in r["por_industria"]:
        print(f"  {f['industria']:<20} ronda {f['ronda']:>2} · {f['proyectos']} proyectos · {f['con_gantt']} con Gantt · "
              f"{f['lineas_base']} líneas base · {f['hitos']} hitos · {sum(len(p['fallas']) for p in f['con_fallas'])} fallas")
        for p in f["con_fallas"]:
            print(f"      {p['codigo']}: {'; '.join(p['fallas'])}")
    print(f"  {r['industrias']} industrias · {r['proyectos']} proyectos · {r['con_gantt']} con Gantt · {r['hitos']} hitos · {r['fallas']} fallas")
    return 1 if r["fallas"] else 0


if __name__ == "__main__":
    sys.exit(main())
