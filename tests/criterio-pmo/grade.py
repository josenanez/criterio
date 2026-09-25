# -*- coding: utf-8 -*-
"""Califica una corrida de criterio-pmo contra las respuestas conocidas.

    python3 tests/criterio-pmo/grade.py                  la extracción de referencia
    python3 tests/criterio-pmo/grade.py --fichas <dir>    fichas producidas por un modelo

Sin argumentos califica la ARITMÉTICA: toma las fichas de `expected/fichas/`, corre
`compute` sobre ellas y verifica que cada hallazgo plantado aparezca, que no
aparezca ninguno que no esté declarado, y que los números coincidan.

Con `--fichas` califica la EXTRACCIÓN: compara campo por campo las fichas que
produjo un modelo leyendo `input/` contra las de referencia. Eso es lo que no se
puede verificar sin correr el plugin, y es la mitad que necesita una sesión real.

Un grader que solo verifica que el informe se produjo no es un grader.
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
PMO = RAIZ.parent.parent / "plugins" / "criterio-pmo" / "scripts" / "pmo.py"

OK, FALLA = "OK   ", "FALLA"


def resolver(nodo, ruta: str):
    """Resuelve "money.pct_committed" o "vendors.0.late" sobre la salida de compute."""
    for parte in ruta.split("."):
        if nodo is None:
            return None
        nodo = nodo[int(parte)] if parte.isdigit() else nodo.get(parte)
    return nodo


def correr_compute(fichas: Path, hoy: str) -> dict:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "records").mkdir()
    for f in sorted(fichas.glob("*.json")):
        shutil.copy(f, tmp / "records" / f.name)
    salida = subprocess.run(
        [sys.executable, str(PMO), "compute", "--state", str(tmp), "--today", hoy],
        capture_output=True, text=True, check=True)
    shutil.rmtree(tmp)
    return json.loads(salida.stdout)


def calificar_aritmetica(fichas: Path) -> int:
    esperado = json.loads((EXPECTED / "hallazgos.json").read_text(encoding="utf-8"))
    hoy = esperado["as_of"]
    real = correr_compute(fichas, hoy)
    por_codigo = {p["code"]: p for p in real["projects"]}

    fallas = 0
    print(f"Aritmética sobre {len(por_codigo)} proyectos · corte {hoy}\n")

    for codigo, esp in esperado["proyectos"].items():
        print(f"── {codigo} · {esp['por_que']}")
        p = por_codigo.get(codigo)
        if p is None:
            print(f"   {FALLA} el proyecto no aparece en la salida")
            fallas += 1
            continue

        vistas = sorted({a["signal"] for a in p["alerts"]})
        quiere = sorted(esp["senales"])
        if vistas == quiere:
            print(f"   {OK} señales · {', '.join(vistas) if vistas else 'ninguna'}")
        else:
            faltan = [s for s in quiere if s not in vistas]
            sobran = [s for s in vistas if s not in quiere]
            print(f"   {FALLA} señales")
            if faltan:
                print(f"         no encontradas: {', '.join(faltan)}")
            if sobran:
                print(f"         no declaradas:  {', '.join(sobran)}")
            fallas += 1

        for ruta, quiere_valor in esp.get("valores", {}).items():
            tiene = resolver(p, ruta)
            if isinstance(tiene, list):
                tiene = len(tiene)
            bien = tiene == quiere_valor
            fallas += 0 if bien else 1
            marca = OK if bien else FALLA
            extra = "" if bien else f"  esperado {quiere_valor!r}"
            print(f"   {marca} {ruta:38} {tiene!r}{extra}")
        print()

    print("── totales del portafolio")
    for clave, quiere_valor in esperado["totales"].items():
        tiene = real["totals"].get(clave)
        bien = tiene == quiere_valor
        fallas += 0 if bien else 1
        print(f"   {OK if bien else FALLA} {clave:38} {tiene!r}"
              f"{'' if bien else f'  esperado {quiere_valor!r}'}")

    return fallas


def campos_planos(nodo, ruta=""):
    """Todo campo {value,...} de una ficha, con su ruta."""
    if isinstance(nodo, dict):
        if "value" in nodo:
            yield ruta, nodo
            return
        for k, v in nodo.items():
            yield from campos_planos(v, f"{ruta}.{k}" if ruta else k)
    elif isinstance(nodo, list):
        for i, v in enumerate(nodo):
            yield from campos_planos(v, f"{ruta}[{i}]")


def calificar_extraccion(producidas: Path) -> int:
    """Compara ficha a ficha contra la referencia. Un valor distinto es una falla;
    una cita a un documento que no existe es peor, y se reporta aparte."""
    fallas = 0
    for ref in sorted((EXPECTED / "fichas").glob("*.json")):
        codigo = ref.stem
        otra = producidas / ref.name
        print(f"── {codigo}")
        if not otra.exists():
            print(f"   {FALLA} no se produjo ficha")
            fallas += 1
            continue
        a = dict(campos_planos(json.loads(ref.read_text(encoding="utf-8"))))
        b = dict(campos_planos(json.loads(otra.read_text(encoding="utf-8"))))

        for ruta, ca in a.items():
            cb = b.get(ruta)
            if cb is None:
                print(f"   {FALLA} {ruta} · no extraído")
                fallas += 1
            elif cb.get("value") != ca.get("value"):
                print(f"   {FALLA} {ruta} · {cb.get('value')!r} en vez de {ca.get('value')!r}")
                fallas += 1
            elif cb.get("state") != ca.get("state"):
                print(f"   {FALLA} {ruta} · estado {cb.get('state')} en vez de {ca.get('state')}")
                fallas += 1

        inventados = [r for r in b if r not in a]
        if inventados:
            print(f"   {FALLA} campos que la referencia no tiene: {', '.join(inventados[:6])}")
            fallas += len(inventados)

        sin_fuente = [r for r, c in b.items()
                      if c.get("value") is not None and not c.get("source")]
        if sin_fuente:
            print(f"   {FALLA} valores sin cita: {', '.join(sin_fuente[:6])}")
            fallas += len(sin_fuente)

        rotas = []
        for r, c in b.items():
            fuente = c.get("source")
            if fuente and not (RAIZ / "input").glob(f"*/{fuente}"):
                rotas.append(r)
        if rotas:
            print(f"   {FALLA} citas que no resuelven: {', '.join(rotas[:6])}")
            fallas += len(rotas)
    return fallas


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichas", type=Path, default=None,
                    help="directorio con fichas producidas por un modelo, para calificar la extracción")
    args = ap.parse_args()

    if args.fichas:
        print("Calificando EXTRACCIÓN contra la referencia\n")
        fallas = calificar_extraccion(args.fichas)
    else:
        fallas = calificar_aritmetica(EXPECTED / "fichas")

    print(f"\n{'sin errores' if not fallas else f'{fallas} FALLAS'}")
    sys.exit(0 if not fallas else 1)
