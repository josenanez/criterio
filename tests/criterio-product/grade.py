# -*- coding: utf-8 -*-
"""Califica el cálculo de criterio-product contra las respuestas escritas a mano.

    python3 tests/criterio-product/grade.py                 la aritmética
    python3 tests/criterio-product/grade.py --registros <d>  la extracción, campo por campo

El primer modo toma los registros de referencia, corre `compute` sobre ellos con las fichas
de proyecto a la vista, y verifica que cada hallazgo plantado aparezca y que **no aparezca
ninguno más**. El segundo compara una extracción real contra la de referencia.

Las respuestas viven en `expected/hallazgos.json` y **se escribieron leyendo los
documentos**, no calculándolas.

El control negativo es la mitad del valor de esta prueba: **PRD-NOMINA tiene definición,
entrevistas, métricas y tres requerimientos, y no produce ni un hallazgo.** Un agente que
encuentra algo ahí es un generador de ruido, y eso no se detecta mirando solo los casos que
sí fallan.
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).parent
EXPECTED = RAIZ / "expected"
PRODUCTO = (RAIZ.parent.parent / "plugins" / "criterio-product" / "scripts" / "producto.py")

OK, FALLA = "OK ", "FALLA"
fallas = 0


def decir(marca, texto, extra=""):
    global fallas
    if marca == FALLA:
        fallas += 1
    print(f"   {marca} {texto:54} {extra}")


def comprobar(que, real, esperado):
    if real == esperado:
        decir(OK, que, real if isinstance(real, str) else f"{real}")
    else:
        decir(FALLA, que, f"{real!r} en vez de {esperado!r}")


def correr_compute(registros: Path, hoy: str) -> dict:
    """Se copia a un temporal para que la corrida no escriba nada en el material."""
    tmp = Path(tempfile.mkdtemp())
    shutil.copytree(registros, tmp / "estado")
    r = subprocess.run([sys.executable, str(PRODUCTO), "compute",
                        "--state", str(tmp / "estado"),
                        "--fichas", str(EXPECTED / "fichas"),
                        "--today", hoy], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr)
        raise SystemExit("compute falló")
    return json.loads(r.stdout)


def calificar_aritmetica() -> None:
    esperado = json.loads((EXPECTED / "hallazgos.json").read_text(encoding="utf-8"))
    hoy = esperado["as_of"]

    for codigo in sorted(k for k in esperado if k.startswith("PRD-")):
        e = esperado[codigo]
        print(f"\n{codigo} · {e['_porque']}")
        real = correr_compute(EXPECTED / "registros" / codigo, hoy)

        comprobar("el producto que salió", real["product"]["code"], codigo)
        t = real["totals"]
        comprobar("requerimientos", t["requirements"], e["requirements"])
        comprobar("por estado", t["by_state"], e["by_state"])
        comprobar("decididos", t["decided"], e["decided"])
        comprobar("decididos con evidencia", t["with_evidence"], e["with_evidence"])
        comprobar("decididos con proyecto", t["traced"], e["traced"])
        comprobar("% con evidencia", t["with_evidence_pct"], e["with_evidence_pct"])
        comprobar("% con proyecto", t["traced_pct"], e["traced_pct"])
        comprobar("campos de la definición sin dato", real["unknown"], e["unknown"])

        # El conteo por señal, no «al menos estas»: una señal de más es un falso positivo,
        # y en un control negativo es el defecto que importa.
        comprobar("el conteo de cada señal", real["by_signal"], e["por_senal"])
        comprobar("el conjunto exacto de señales",
                  sorted({a["signal"] for a in real["alerts"]}), sorted(e["signals"]))

        # Y las cifras concretas de los hallazgos que se leyeron a mano en los documentos.
        if "claim_gap_pct" in e:
            a = next(x for x in real["alerts"] if x["signal"] == "claim_vs_metric")
            comprobar("la diferencia entre lo declarado y lo medido",
                      a["detail"]["gap_pct"], e["claim_gap_pct"])
            comprobar("y la señal trae las dos fuentes",
                      bool(a["detail"]["declared_source"] and a["detail"]["measured_source"]),
                      True)
            comprobar("y las dos fechas",
                      bool(a["detail"]["declared_date"] and a["detail"]["measured_on"]), True)
        if "trace_says" in e:
            a = next(x for x in real["alerts"] if x["signal"] == "trace_not_confirmed")
            comprobar("qué producto dice la ficha del otro proyecto",
                      a["detail"].get("says"), e["trace_says"])
        if "evidence_stale_months" in e:
            a = next(x for x in real["alerts"] if x["signal"] == "evidence_stale")
            comprobar("meses de la evidencia más nueva", a["detail"]["months"],
                      e["evidence_stale_months"])
        if "undecided_days" in e:
            a = next(x for x in real["alerts"] if x["signal"] == "requirement_undecided")
            comprobar("días propuesto sin decidirse", a["detail"]["days"],
                      e["undecided_days"])


def correr_overlap(registros: Path, hoy: str) -> dict:
    tmp = Path(tempfile.mkdtemp())
    shutil.copytree(registros, tmp / "estado")
    r = subprocess.run([sys.executable, str(PRODUCTO), "overlap",
                        "--state", str(tmp / "estado"),
                        "--otros", str(EXPECTED / "publicados"),
                        "--today", hoy], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr)
        raise SystemExit("overlap falló")
    return json.loads(r.stdout)


def calificar_solapamiento() -> None:
    """Dónde este producto y los que otros publicaron se pisan.

    El caso no es de laboratorio: **PRD-QR aceptó el cobro recurrente, no le puso
    proyecto, y otro producto lo está construyendo.** Y los dos casos de negocio
    afirman la misma métrica, así que la suma que vio el comité no existe.

    El control negativo va en la misma carpeta: PRD-NOMINA está publicado y no se pisa
    con nada. Un agente que encuentra solapamiento ahí está generando ruido, y eso solo
    se detecta teniendo publicado algo que no se pisa.
    """
    esperado = json.loads((EXPECTED / "hallazgos.json").read_text(encoding="utf-8"))
    hoy = esperado["as_of"]
    e = esperado["solapamiento"]

    print(f"\n{e['producto']} contra lo publicado · {e['_porque']}")
    r = correr_overlap(EXPECTED / "registros" / e["producto"], hoy)

    comprobar("lee todo lo publicado menos lo propio", sorted(r["read"]), sorted(e["lee"]))
    comprobar("métricas que dos casos de negocio cuentan", r["totals"]["metrics"],
              e["metricas"])
    if r["shared_metrics"]:
        m = r["shared_metrics"][0]
        comprobar("cuál métrica", m["metric"], e["metrica"])
        comprobar("mi cifra", m["mine"], e["mi_cifra"])
        comprobar("la suya", m["theirs"], e["su_cifra"])
        comprobar("y las dos fuentes, que es lo que permite ir a ver",
                  bool(m["mine_source"] and m["theirs_source"]), True)
    comprobar("proyectos con dos dueños", r["totals"]["projects"], e["proyectos"])
    if r["shared_projects"]:
        pr = r["shared_projects"][0]
        comprobar("cuál proyecto", pr["project"], e["proyecto"])
        comprobar("qué pongo yo ahí", pr["mine"], e["mis_req"])
        comprobar("qué pone el otro", pr["theirs"], e["sus_req"])
    comprobar("mismo segmento, escrito por otra persona", r["totals"]["segments"],
              e["segmentos"])
    comprobar("el conteo exacto de señales", len(r["alerts"]), e["senales"])
    comprobar("y ninguna contra el producto que no se pisa con nada",
              [a for a in r["alerts"] if a["detail"]["with"] == e["no_se_pisa_con"]], [])

    print(f"\n   Control negativo · {e['negativo']} contra los mismos publicados")
    n = correr_overlap(EXPECTED / "registros" / e["negativo"], hoy)
    comprobar("no encuentra nada", n["alerts"], [])
    comprobar("y sí leyó lo que había, menos él mismo", n["totals"]["others"],
              e["negativo_lee"])


def calificar_registros(reales: Path) -> None:
    """Compara una extracción real contra la de referencia, campo por campo.

    Nunca se ha corrido sobre una extracción de verdad, y eso está dicho en EVIDENCIA.md:
    el corpus siembra los registros, así que la cadena documento → modelo → registro no se
    ha ejercitado. Este modo existe para el día en que se ejercite.
    """
    for base in sorted((EXPECTED / "registros").iterdir()):
        for ref in sorted((base / "requirements").glob("*.json")):
            otra = reales / base.name / "requirements" / ref.name
            print(f"\n{base.name}/{ref.stem}")
            if not otra.exists():
                decir(FALLA, "no se extrajo este registro")
                continue
            comparar(json.loads(ref.read_text(encoding="utf-8")),
                     json.loads(otra.read_text(encoding="utf-8")), "")


def comparar(a, b, ruta):
    if isinstance(a, dict) and "value" in a:
        va, vb = a.get("value"), (b or {}).get("value")
        if va != vb:
            decir(FALLA, ruta, f"{vb!r} en vez de {va!r}")
        elif a.get("state") != (b or {}).get("state"):
            decir(FALLA, f"{ruta} · estado", f"{(b or {}).get('state')!r}")
        else:
            decir(OK, ruta, "")
        return
    if isinstance(a, dict):
        for k, v in a.items():
            comparar(v, (b or {}).get(k), f"{ruta}.{k}".lstrip("."))
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            decir(FALLA, ruta, f"{len(b) if isinstance(b, list) else '—'} elementos "
                               f"en vez de {len(a)}")
            return
        for i, v in enumerate(a):
            comparar(v, b[i], f"{ruta}[{i}]")


def main() -> int:
    ap = argparse.ArgumentParser(description="Califica criterio-product.")
    ap.add_argument("--registros", type=Path, default=None,
                    help="carpeta con una extracción real, para calificarla")
    args = ap.parse_args()

    if args.registros:
        print("Extracción, campo por campo")
        calificar_registros(args.registros)
    else:
        print("Aritmética sobre los registros de referencia")
        calificar_aritmetica()
        print("\n" + "=" * 72)
        print("Dónde dos productos se pisan")
        calificar_solapamiento()
        print("\n   El control negativo es la mitad del valor de esta prueba: PRD-NOMINA")
        print("   tiene definición, entrevistas, métricas y tres requerimientos, y no")
        print("   produce ni un hallazgo. Un agente que encuentra algo ahí es ruido.")

    print()
    if fallas:
        print(f"{fallas} falla(s)")
        return 1
    print("sin errores")
    return 0


if __name__ == "__main__":
    sys.exit(main())
