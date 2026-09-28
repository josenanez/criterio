# -*- coding: utf-8 -*-
"""La corrida diaria: cuánto tarda, qué acierta, y qué se inventa.

    python3 tests/sintetico/fiabilidad.py <carpeta de la demo>

Lo que había hasta ahora contaba **puertas y comprobaciones**, que dice si el código
corre. No dice si el agente acierta. Para decidir qué mejorar hace falta otra cosa:

    aciertos            un hallazgo esperado que apareció
    falsos positivos    uno que apareció y nadie esperaba — el que quema la confianza
    falsos negativos    uno que se esperaba y no apareció
    precisión           de lo que reportó, cuánto era cierto
    cobertura           de lo que había, cuánto encontró

Y por señal, no solo en total: el promedio esconde justo lo que hay que arreglar.

**El falso positivo pesa más que el falso negativo**, y el informe lo dice así. Un
hallazgo que no era cierto hace que la siguiente lista no se lea; uno que faltó hace
que se lea una lista incompleta. La segunda es mala, la primera es terminal.

Escribe `informes/AAAA-MM-DD.md` para leer y `informes/AAAA-MM-DD.json` para acumular.
"""
import json
import os
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).parent.parent.parent
PORTFOLIO = RAIZ / "plugins" / "criterio-portfolio" / "scripts" / "portafolio.py"
PRODUCT = RAIZ / "plugins" / "criterio-product" / "scripts" / "producto.py"
EXTRACTOR = RAIZ / "tests" / "sintetico" / "extractor.py"


def correr(*args, **kw):
    t0 = time.perf_counter()
    r = subprocess.run([sys.executable, *[str(a) for a in args]],
                       capture_output=True, text=True, **kw)
    return r, round((time.perf_counter() - t0) * 1000)


def documentos(carpeta: Path) -> dict:
    """Cuántos archivos, de qué formato y cuánto pesan."""
    por_formato, total, bytes_ = Counter(), 0, 0
    for f in carpeta.rglob("*"):
        if f.is_file():
            por_formato[f.suffix.lower() or "(sin extensión)"] += 1
            total += 1
            bytes_ += f.stat().st_size
    return {"total": total, "bytes": bytes_, "por_formato": dict(por_formato)}


def hallazgos_portafolio(estado: Path) -> tuple:
    r, ms = correr(PORTFOLIO, "compute", "--state", estado)
    if r.returncode:
        return {}, ms, r.stderr.strip()[:300]
    d = json.loads(r.stdout)
    return ({p["code"]: [a["signal"] for a in (p.get("alerts") or [])]
             for p in d.get("projects", [])}, ms, None)


def hallazgos_producto(base: Path, fichas: Path) -> tuple:
    salida, total_ms, error = {}, 0, None
    if not base.is_dir():
        return salida, 0, "no hay registros de producto"
    for d in sorted(x for x in base.iterdir() if x.is_dir()):
        r, ms = correr(PRODUCT, "compute", "--state", d, "--fichas", fichas)
        total_ms += ms
        if r.returncode:
            error = r.stderr.strip()[:200]
            continue
        salida[d.name] = [a["signal"] for a in (json.loads(r.stdout).get("alerts") or [])]
    return salida, total_ms, error


def calificar(esperado: dict, obtenido: dict) -> dict:
    """Aciertos, falsos positivos y falsos negativos, por caso y por señal."""
    por_senal, por_caso = {}, {}
    for caso in sorted(set(esperado) | set(obtenido)):
        esp, obt = Counter(esperado.get(caso, [])), Counter(obtenido.get(caso, []))
        acierto = esp & obt                       # intersección de multiconjuntos
        falta = esp - obt
        sobra = obt - esp
        por_caso[caso] = {"esperado": sum(esp.values()), "obtenido": sum(obt.values()),
                          "aciertos": sum(acierto.values()),
                          "falsos_negativos": sorted(falta.elements()),
                          "falsos_positivos": sorted(sobra.elements())}
        for s in set(esp) | set(obt):
            fila = por_senal.setdefault(s, {"aciertos": 0, "fp": 0, "fn": 0, "casos": []})
            fila["aciertos"] += acierto[s]
            fila["fp"] += sobra[s]
            fila["fn"] += falta[s]
            if sobra[s] or falta[s]:
                fila["casos"].append(caso)
    for s, f in por_senal.items():
        emitidos = f["aciertos"] + f["fp"]
        habia = f["aciertos"] + f["fn"]
        f["precision"] = round(100 * f["aciertos"] / emitidos, 1) if emitidos else None
        f["cobertura"] = round(100 * f["aciertos"] / habia, 1) if habia else None
    return {"por_caso": por_caso, "por_senal": por_senal}


def totales(cal: dict) -> dict:
    a = sum(c["aciertos"] for c in cal["por_caso"].values())
    fp = sum(len(c["falsos_positivos"]) for c in cal["por_caso"].values())
    fn = sum(len(c["falsos_negativos"]) for c in cal["por_caso"].values())
    return {"aciertos": a, "falsos_positivos": fp, "falsos_negativos": fn,
            "precision": round(100 * a / (a + fp), 1) if a + fp else None,
            "cobertura": round(100 * a / (a + fn), 1) if a + fn else None}


def pagina(d: dict) -> str:
    t = d["totales"]
    p = [f"# Corrida del {d['fecha']}", "",
         f"Organización sintética de {d['casos']['proyectos']} proyectos y "
         f"{d['casos']['productos']} productos, escrita con la disposición "
         f"**{d['disposicion']}**. Commit `{d['commit']}`.", "",
         "## Fiabilidad", "",
         "| | |", "|---|---:|",
         f"| Hallazgos esperados | {t['aciertos'] + t['falsos_negativos']} |",
         f"| **Aciertos** | **{t['aciertos']}** |",
         f"| Falsos positivos · *reportó algo que no era* | {t['falsos_positivos']} |",
         f"| Falsos negativos · *no vio algo que estaba* | {t['falsos_negativos']} |",
         f"| **Precisión** · de lo que reportó, cuánto era cierto | "
         f"**{t['precision']}%** |" if t["precision"] is not None else "| Precisión | — |",
         f"| **Cobertura** · de lo que había, cuánto encontró | "
         f"**{t['cobertura']}%** |" if t["cobertura"] is not None else "| Cobertura | — |",
         ""]

    ctrl = d["controles"]
    malos = [c for c, n in ctrl.items() if n]
    p += ["## Controles negativos", "",
          "Dos casos con documentos, reuniones y requerimientos que **no deben producir "
          "ni un hallazgo**. Un agente que encuentra algo ahí es un generador de ruido, "
          "y eso cuenta tanto como no encontrar lo que sí está.", ""]
    for c, n in sorted(ctrl.items()):
        p.append(f"- **{c}** · {'✗ ' + str(n) + ' hallazgos' if n else '✓ cero hallazgos'}")
    p.append("")

    p += ["## Tiempo", "", "| Etapa | Tiempo |", "|---|---:|"]
    for etapa, ms in d["tiempos"].items():
        p.append(f"| {etapa} | {ms / 1000:.2f} s |")
    doc = d["documentos"]
    ms_total = sum(d["tiempos"].values())
    p += [f"| **Total** | **{ms_total / 1000:.2f} s** |", "",
          f"**{doc['total']} documentos · {doc['bytes'] / 1024:.0f} KB · "
          f"{ms_total / max(doc['total'], 1):.0f} ms por documento.**", "",
          "| Formato | Archivos |", "|---|---:|"]
    for ext, n in sorted(doc["por_formato"].items(), key=lambda x: -x[1]):
        p.append(f"| `{ext}` | {n} |")
    p.append("")

    problemas = {s: f for s, f in d["calificacion"]["por_senal"].items()
                 if f["fp"] or f["fn"]}
    p += ["## Por señal", ""]
    if not problemas:
        p += ["Ninguna señal falló: todas las esperadas aparecieron y ninguna apareció "
              "de más.", ""]
    else:
        p += ["Solo las que fallaron. El promedio esconde justo lo que hay que arreglar.",
              "", "| Señal | Aciertos | Falsos + | Falsos − | Precisión | Cobertura | Dónde |",
              "|---|---:|---:|---:|---:|---:|---|"]
        for s, f in sorted(problemas.items(), key=lambda x: (-x[1]["fp"], -x[1]["fn"])):
            p.append(f"| `{s}` | {f['aciertos']} | {f['fp']} | {f['fn']} | "
                     f"{f['precision'] if f['precision'] is not None else '—'}% | "
                     f"{f['cobertura'] if f['cobertura'] is not None else '—'}% | "
                     f"{', '.join(f['casos'][:4])} |")
        p.append("")

    fallos = {c: v for c, v in d["calificacion"]["por_caso"].items()
              if v["falsos_positivos"] or v["falsos_negativos"]}
    if fallos:
        p += ["## Qué revisar", "",
              "En orden: primero lo que el agente **se inventó**, porque un hallazgo "
              "falso hace que la siguiente lista no se lea; después lo que **no vio**.",
              ""]
        for c, v in sorted(fallos.items()):
            if v["falsos_positivos"]:
                p.append(f"- **{c}** reportó de más: "
                         f"{', '.join('`' + x + '`' for x in v['falsos_positivos'])}")
        for c, v in sorted(fallos.items()):
            if v["falsos_negativos"]:
                p.append(f"- **{c}** no vio: "
                         f"{', '.join('`' + x + '`' for x in v['falsos_negativos'])}")
        p.append("")

    if d.get("errores"):
        p += ["## Errores de ejecución", ""]
        for e in d["errores"]:
            p.append(f"- {e}")
        p.append("")

    p += ["---", "",
          "**Qué no mide esta corrida.** La extracción la hace "
          "`tests/sintetico/extractor.py`, que lee documentos de estructura conocida sin "
          "modelo: lo que se mide aquí es la aritmética sobre una ficha bien construida, "
          "no la lectura de documentos reales. Y el material es sintético.", ""]
    return "\n".join(p)


if __name__ == "__main__":
    base = Path(sys.argv[1] if len(sys.argv) > 1 else "~/Projects/pmo-demo").expanduser()
    import datetime as dt
    hoy = dt.date.today().isoformat()
    errores, tiempos = [], {}

    clave = json.loads((base / "esperado.json").read_text(encoding="utf-8"))
    esperado = clave["esperado"]

    # ── extracción
    r, tiempos["Extracción · documentos a ficha"] = correr(EXTRACTOR, base)
    if r.returncode:
        errores.append(f"extractor: {r.stderr.strip()[:200]}")

    # ── cálculo
    pf, ms1, err1 = hallazgos_portafolio(base / "estado")
    tiempos["Cálculo · portafolio"] = ms1
    if err1:
        errores.append(f"portafolio compute: {err1}")
    pd_, ms2, err2 = hallazgos_producto(base / "estado-productos", base / "estado" / "records")
    tiempos["Cálculo · productos"] = ms2
    if err2:
        errores.append(f"producto compute: {err2}")

    obtenido = {**pf, **pd_}
    cal = calificar(esperado, obtenido)
    git = subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "--short", "HEAD"],
                         capture_output=True, text=True).stdout.strip() or "?"

    informe = {
        "fecha": hoy, "dia": clave.get("dia"), "commit": git,
        "disposicion": clave.get("disposicion", "?"),
        "casos": {"proyectos": len(pf), "productos": len(pd_)},
        "documentos": documentos(base / "documentos"),
        "tiempos": tiempos, "totales": totales(cal), "calificacion": cal,
        "controles": {c: len(obtenido.get(c, [])) for c in clave.get("controles", [])},
        "errores": errores,
    }

    # El nombre lleva el día de la simulación y no solo la fecha. Dos corridas de la
    # misma jornada —el día 3 y el día 4 ensayados de seguido— se sobreescribían, y el
    # resumen de cinco días se quedaba en uno sin que nada fallara.
    dia = informe["dia"]
    nombre = f"dia-{dia}-{hoy}" if dia else hoy
    salida = RAIZ / "tests" / "informes"
    salida.mkdir(parents=True, exist_ok=True)
    (salida / f"{nombre}.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (salida / f"{nombre}.md").write_text(pagina(informe) + "\n", encoding="utf-8")

    t = informe["totales"]
    print(f"{hoy} · disposición {informe['disposicion']} · "
          f"{informe['documentos']['total']} documentos")
    print(f"  aciertos {t['aciertos']} · falsos+ {t['falsos_positivos']} · "
          f"falsos− {t['falsos_negativos']} · "
          f"precisión {t['precision']}% · cobertura {t['cobertura']}%")
    for c, n in sorted(informe["controles"].items()):
        print(f"  control {c}: {'cero hallazgos' if not n else str(n) + ' HALLAZGOS'}")
    print(f"  → tests/informes/{nombre}.md")
    # Falla si un control negativo produjo algo o si hubo un error de ejecución: las
    # dos cosas invalidan la corrida entera, no solo una señal.
    sys.exit(1 if errores or any(informe["controles"].values()) else 0)
