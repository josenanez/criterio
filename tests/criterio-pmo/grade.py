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


def correr_index(docs: Path) -> dict:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "records").mkdir()
    for f in sorted((EXPECTED / "fichas").glob("*.json")):
        shutil.copy(f, tmp / "records" / f.name)
    salida = subprocess.run(
        [sys.executable, str(PMO), "index", "--state", str(tmp), "--docs", str(docs)],
        capture_output=True, text=True, check=True)
    shutil.rmtree(tmp)
    return json.loads(salida.stdout)


# Los cuatro casos que un índice de documentos tiene que distinguir. Si el corpus
# cambia y alguno de estos archivos ya no existe, la prueba falla en voz alta en vez
# de pasar sin probar nada.
MUTACIONES = {
    "cambiado": "PRY-001-originacion-digital/30-reuniones/2026-09-11-comite-tecnico.md",
    "reguardado": "PRY-005-debito-contactless/20-seguimiento/2026-09-26-informe-avance.md",
    "renombrado": "PRY-003-migracion-nube/20-seguimiento/2026-06-05-acta-recibo-landing-zone.md",
    "borrado": "PRY-006-sarlaft/20-seguimiento/2026-07-08-solicitud-cambio-cc-07.md",
}


def calificar_indice() -> int:
    """El índice de documentos: qué hay que releer y qué citas dejaron de resolver."""
    fallas = 0
    docs = RAIZ / "input"
    total = sum(1 for x in docs.rglob("*") if x.is_file())

    def comprobar(etiqueta, tiene, quiere):
        nonlocal fallas
        bien = tiene == quiere
        fallas += 0 if bien else 1
        print(f"   {OK if bien else FALLA} {etiqueta:38} {tiene!r}"
              f"{'' if bien else f'  esperado {quiere!r}'}")

    print("── sin cambios: no hay nada que releer")
    d = correr_index(docs)
    comprobar("documentos en disco", d["documents"], total)
    comprobar("sin cambio", d["unchanged"], total)
    comprobar("hay que releer", d["to_read"], 0)
    comprobar("citas que no resuelven", len(d["source_missing"]), 0)

    print("\n── con un cambio real, un reguardado, un renombrado y un borrado")
    tmp = Path(tempfile.mkdtemp()) / "docs"
    shutil.copytree(docs, tmp)
    for etiqueta, rel in MUTACIONES.items():
        if not (tmp / rel).exists():
            print(f"   {FALLA} el corpus ya no tiene {rel}")
            fallas += 1
    (tmp / MUTACIONES["cambiado"]).open("a", encoding="utf-8").write(
        "\nSe agrega que el proveedor pidió una prórroga adicional.\n")
    (tmp / MUTACIONES["reguardado"]).open("a", encoding="utf-8").write("\n\n   \n")
    renombrado = tmp / MUTACIONES["renombrado"]
    renombrado.rename(renombrado.with_name(renombrado.stem + "-FIRMADA.md"))
    (tmp / MUTACIONES["borrado"]).unlink()

    d = correr_index(tmp)
    comprobar("cambiados de verdad", len(d["changed"]), 1)
    comprobar("solo reguardados", len(d["resaved_only"]), 1)
    comprobar("renombrados", len(d["renamed"]), 1)
    comprobar("borrados", len(d["deleted"]), 1)
    comprobar("nuevos", len(d["new"]), 0)
    comprobar("hay que releer", d["to_read"], 1)
    comprobar("proyectos a recalcular", d["projects_to_recompute"],
              ["PRY-001", "PRY-003", "PRY-006"])
    rotas = {x["project"] for x in d["source_missing"]}
    comprobar("proyectos con citas rotas", sorted(rotas), ["PRY-003", "PRY-006"])
    shutil.rmtree(tmp.parent)

    print("\n   El reguardado es el caso que paga el diseño: cambió el hash de bytes y")
    print("   no el del texto, así que no entra en lo que hay que releer. Un Excel que")
    print("   recalcula al abrirlo hace eso todos los días.")
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
        print("\n" + "=" * 72)
        print("Índice de documentos\n")
        fallas += calificar_indice()

    print(f"\n{'sin errores' if not fallas else f'{fallas} FALLAS'}")
    sys.exit(0 if not fallas else 1)
