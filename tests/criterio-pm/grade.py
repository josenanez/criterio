# -*- coding: utf-8 -*-
"""Califica el cálculo de criterio-pm contra las respuestas escritas a mano.

    python3 tests/criterio-pm/grade.py              la aritmética
    python3 tests/criterio-pm/grade.py --fichas <d> la extracción, campo por campo

El primer modo toma las fichas de referencia, corre `compute` sobre ellas y verifica
que cada hallazgo plantado aparezca y que **no aparezca ninguno más**. El segundo
compara una extracción real contra la de referencia.

Las respuestas viven en `expected/hallazgos.json` y **se escribieron leyendo las
minutas**, no calculándolas. Si salieran de las mismas fórmulas que el código, esto
no probaría nada.

El control negativo es la mitad del valor de esta prueba: **PRY-102 tiene reuniones
y compromisos y no produce ni un hallazgo.** Un agente que encuentra algo ahí es un
generador de ruido, y eso no se detecta mirando solo los casos que sí fallan.
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
PMO = RAIZ.parent.parent / "plugins" / "criterio-pm" / "scripts" / "pmo.py"

OK, FALLA = "OK ", "FALLA"
fallas = 0


def decir(marca, texto, extra=""):
    global fallas
    if marca == FALLA:
        fallas += 1
    print(f"   {marca} {texto:52} {extra}")


def comprobar(que, real, esperado):
    if real == esperado:
        decir(OK, que, real if isinstance(real, str) else f"{real}")
    else:
        decir(FALLA, que, f"{real!r} en vez de {esperado!r}")


def correr_compute(fichas: Path, hoy: str) -> dict:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "records").mkdir()
    for f in sorted(fichas.glob("*.json")):
        shutil.copy(f, tmp / "records" / f.name)
    r = subprocess.run([sys.executable, str(PMO), "compute", "--state", str(tmp),
                        "--today", hoy], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr)
        raise SystemExit("compute falló")
    return json.loads(r.stdout)


def calificar_aritmetica(fichas: Path) -> None:
    esperado = json.loads((EXPECTED / "hallazgos.json").read_text(encoding="utf-8"))
    hoy = esperado["as_of"]
    real = correr_compute(fichas, hoy)
    por_codigo = {p["code"]: p for p in real["projects"]}

    for codigo in sorted(k for k in esperado if k.startswith("PRY-")):
        e = esperado[codigo]
        print(f"\n{codigo} · {e['_porque']}")
        p = por_codigo.get(codigo)
        if p is None:
            decir(FALLA, "el proyecto no aparece en compute")
            continue

        comprobar("compromisos vencidos", len(p["commitments_overdue"]),
                  e["commitments_overdue"])
        comprobar("compromisos sin fecha", len(p["commitments_undated"]),
                  e["commitments_undated"])
        comprobar("compromisos reprogramados", len(p["commitments_rescheduled"]),
                  e["commitments_rescheduled"])
        if e.get("reschedule_times"):
            comprobar("veces que se reprogramó",
                      p["commitments_rescheduled"][0]["times"], e["reschedule_times"])
        comprobar("hitos vencidos sin evidencia", len(p["milestones_overdue"]),
                  e["milestones_overdue"])
        comprobar("días en silencio", p["days_silent"], e["days_silent"])
        comprobar("lo que declara el gerente",
                  (p.get("declared") or {}).get("status"), e["declared"])

        # La declaración contra la evidencia, en los dos sentidos. Un agente que
        # contradice siempre es tan inútil como uno que nunca contradice.
        contradicho = any(a["signal"] == "declared_vs_evidence" for a in p["alerts"])
        comprobar("la evidencia contradice lo declarado", contradicho,
                  e["declared_vs_evidence"])

        # Riesgos dichos y nunca registrados: están en la ficha, no en compute.
        ficha = json.loads((fichas / f"{codigo}.json").read_text(encoding="utf-8"))
        sin_registrar = sum(
            1 for r in (ficha.get("raid") or {}).get("risks") or []
            if (r.get("formally_registered") or {}).get("value") is False)
        comprobar("riesgos dichos y no registrados", sin_registrar,
                  e["risks_not_registered"])

        # El conjunto exacto, no «al menos estas». Una señal de más es un falso
        # positivo, y en un control negativo es el defecto que importa.
        comprobar("el conjunto exacto de señales",
                  sorted({a["signal"] for a in p["alerts"]}), sorted(e["signals"]))


def calificar_fichas(reales: Path) -> None:
    """Compara una extracción real contra la de referencia, campo por campo."""
    ref = EXPECTED / "fichas"
    for f in sorted(ref.glob("*.json")):
        otra = reales / f.name
        print(f"\n{f.stem}")
        if not otra.exists():
            decir(FALLA, "no se extrajo esta ficha")
            continue
        a = json.loads(f.read_text(encoding="utf-8"))
        b = json.loads(otra.read_text(encoding="utf-8"))
        comparar(a, b, "")


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
            if k == "meta":
                continue
            comparar(v, (b or {}).get(k), f"{ruta}.{k}".lstrip("."))
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            decir(FALLA, ruta, f"{len(b) if isinstance(b, list) else '—'} elementos "
                               f"en vez de {len(a)}")
            return
        for i, v in enumerate(a):
            comparar(v, b[i], f"{ruta}[{i}]")


def main() -> int:
    ap = argparse.ArgumentParser(description="Califica criterio-pm.")
    ap.add_argument("--fichas", type=Path, default=None,
                    help="carpeta con una extracción real, para calificarla")
    args = ap.parse_args()

    if args.fichas:
        print("Extracción, campo por campo")
        calificar_fichas(args.fichas)
    else:
        print("Aritmética sobre las fichas de referencia")
        calificar_aritmetica(EXPECTED / "fichas")
        print("\n   El control negativo es la mitad del valor de esta prueba: PRY-102")
        print("   tiene reuniones y compromisos y no produce ni un hallazgo. Un agente")
        print("   que encuentra algo ahí es un generador de ruido.")

    print()
    if fallas:
        print(f"{fallas} falla(s)")
        return 1
    print("sin errores")
    return 0


if __name__ == "__main__":
    sys.exit(main())
