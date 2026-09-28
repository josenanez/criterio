# -*- coding: utf-8 -*-
"""Qué señales dispara el material, y cuáles no las ha disparado nunca.

    python3 tests/sintetico/cobertura.py

Una señal con selftest no está probada: está *especificada*. Lo que la prueba es que
algún documento la haga saltar. Y eso no se veía por ninguna parte — había ocho señales
de portafolio que ningún corpus había disparado jamás, y las diecisiete puertas estaban
en verde.

Esta puerta las cuenta. No falla por una señal sin disparar: **falla si aparece una que
no esté declarada abajo con su razón.** La lista obliga a decidir en vez de dejar pasar,
que es la misma regla que ya gobierna los nombres pendientes de `coherencia.py`.

El material es el corpus de los tres agentes. La organización sintética de
`organizacion.py` no entra: se genera con fecha relativa al día, así que no puede ser
la base de una puerta que tiene que dar lo mismo siempre.
"""
import json
import re
import subprocess
import sys
import shutil
import tempfile
from pathlib import Path

RAIZ = Path(__file__).parent.parent.parent
PORTFOLIO = RAIZ / "plugins" / "criterio-portfolio" / "scripts" / "portafolio.py"
PRODUCT = RAIZ / "plugins" / "criterio-product" / "scripts" / "producto.py"

OK, FALLA, NOTA = "OK   ", "FALLA", "nota "
fallas = []

# Señales que el material no dispara, y por qué. Una señal que no esté aquí y tampoco
# dispare hace fallar la puerta: hay que decidir si se le construye material o si se
# declara, pero no se puede ignorar.
SIN_MATERIAL = {
    # Las cinco que el corpus de los tres agentes no contiene. Todas disparan sobre la
    # organización sintética de `organizacion.py`, así que no son señales muertas: es
    # material que al corpus le falta, y el sitio donde está escrito que le falta.
    "change_without_baseline": ("el corpus no trae un cambio autorizado sin línea base "
                                "nueva · la organización demo sí, en PRY-109"),
    "milestone_met_without_evidence": ("el corpus no trae un hito declarado cerrado sin "
                                       "acta · la demo sí, en cinco proyectos"),
    "pm_vs_pmo": ("el corpus no trae una ficha publicada por el gerente junto a la de "
                  "la PMO · la demo sí, en PRY-107"),
    "vendor_invoiced_without_delivery": ("el corpus no trae una factura contra un "
                                         "contrato sin nada recibido · la demo sí, en "
                                         "PRY-106"),
    "product_overlap": ("no sale de `compute` sino de cruzar dos productos publicados, "
                        "y esta puerta solo corre `compute`"),
}



def senales(script: Path) -> list:
    codigo = script.read_text(encoding="utf-8")
    inv = re.search(r"SENALES = \((.*?)\n\)", codigo, re.S)
    if inv:
        return [s for s in re.findall(r'"([a-z_]+)"', inv.group(1))]
    return sorted(set(re.findall(r'alert\("([a-z_]+)"', codigo)))


def disparadas(script: Path, estado: Path, extra=()) -> set:
    r = subprocess.run([sys.executable, str(script), "compute", "--state", str(estado),
                        *extra], capture_output=True, text=True)
    if r.returncode:
        return set()
    d = json.loads(r.stdout)
    proyectos = d.get("projects")
    if proyectos is not None:
        return {a["signal"] for p in proyectos for a in (p.get("alerts") or [])}
    return {a["signal"] for a in (d.get("alerts") or [])}


def decir(marca, texto):
    print(f"  {marca}  {texto}")
    if marca == FALLA:
        fallas.append(texto)


print(__doc__.strip().splitlines()[0])

# ── portafolio ───────────────────────────────────────────────────────────
print("\nLas señales de portafolio que el material dispara")
todas = senales(PORTFOLIO)
# `expected/fichas` es la extracción de referencia; el cálculo espera un estado con
# `records/`. Se arma uno temporal, que además garantiza que la puerta no escriba en
# el material de pruebas.
vistas = set()
for plugin in ("criterio-portfolio", "criterio-project"):
    fichas = RAIZ / "tests" / plugin / "expected" / "fichas"
    if not fichas.is_dir():
        continue
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        shutil.copytree(fichas, estado / "records")
        vistas |= disparadas(PORTFOLIO, estado)
faltan = [s for s in todas if s not in vistas]
decir(OK if vistas else FALLA, f"{len(vistas)} de {len(todas)} disparan sobre el corpus")

# ── producto ─────────────────────────────────────────────────────────────
print("\nLas señales de producto que el material dispara")
todas_p = senales(PRODUCT)
vistas_p = set()
reg = RAIZ / "tests" / "criterio-product" / "expected" / "registros"
if reg.is_dir():
    for d in sorted(x for x in reg.iterdir() if x.is_dir()):
        vistas_p |= disparadas(PRODUCT, d)
faltan_p = [s for s in todas_p if s not in vistas_p]
decir(OK if vistas_p else FALLA,
      f"{len(vistas_p)} de {len(todas_p)} disparan sobre el corpus")

# ── la lista obliga a decidir ────────────────────────────────────────────
print("\nCada señal que no dispara, declarada con su razón")
sin_declarar = [s for s in faltan + faltan_p if s not in SIN_MATERIAL]
sobran = [s for s in SIN_MATERIAL if s not in faltan + faltan_p]
for s in faltan + faltan_p:
    if s in SIN_MATERIAL:
        decir(NOTA, f"`{s}` · {SIN_MATERIAL[s]}")
if sin_declarar:
    for s in sin_declarar:
        decir(FALLA, f"`{s}` no dispara sobre ningún material y no está declarada. "
                     f"Constrúyele material, o decláralo en SIN_MATERIAL con su razón")
else:
    decir(OK, "ninguna señal sin disparar se quedó sin declarar")
if sobran:
    for s in sobran:
        decir(NOTA, f"`{s}` ya dispara y sigue declarada como sin material · "
                    f"quitarla de SIN_MATERIAL")

print(f"\n{'cobertura declarada' if not fallas else f'{len(fallas)} FALLAS'}")
sys.exit(1 if fallas else 0)
