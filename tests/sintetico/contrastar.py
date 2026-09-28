# -*- coding: utf-8 -*-
"""Las cifras que un informe tiene que acertar, para contrastarlas a mano.

    python3 tests/sintetico/contrastar.py .pruebas/corp-demo
    python3 tests/sintetico/contrastar.py .pruebas/corp-demo --alertas 158 --aprobado 303100000000000

`fiabilidad.py` califica lo que el **script** calcula. Esto es para la otra capa: lo que el
**modelo** escribió en el informe. Un agente puede tener la aritmética exacta y equivocarse
al transcribirla —pasó: el presupuesto aprobado salió con tres ceros de más mientras las
otras tres cifras del mismo cuadro quedaban bien— y ninguna puerta lo atrapa, porque el
script tenía razón.

Sin argumentos imprime las cifras que el informe debe acertar. Con `--alertas` y las demás,
compara lo que el informe dijo contra la clave y señala en qué se separó.
"""
import argparse
import json
from collections import Counter
from pathlib import Path


def cifras(org: Path) -> dict:
    esperado = json.loads((org / "esperado.json").read_text(encoding="utf-8"))["esperado"]
    estado = json.loads((org / "organizacion.json").read_text(encoding="utf-8"))
    pry = {k: v for k, v in esperado.items() if k.startswith("PRY")}
    prd = {k: v for k, v in esperado.items() if k.startswith("PRD")}
    p = estado["proyectos"]
    luz = Counter(x["declarado"]["estado"] for x in p)
    return {
        "dia": estado["dia"],
        "solo_modelo": json.loads(
            (org / "esperado.json").read_text(encoding="utf-8")).get("solo_modelo", {}),
        "proyectos": len(p),
        "productos": len(estado["productos"]),
        "verde": luz["verde"], "amarillo": luz["amarillo"], "rojo": luz["rojo"],
        "alertas_proyecto": sum(len(v) for v in pry.values()),
        "alertas_producto": sum(len(v) for v in prd.values()),
        "por_senal": dict(Counter(s for v in esperado.values() for s in v).most_common()),
        "aprobado": sum(x["presupuesto"] for x in p),
        "comprometido": sum(x["comprometido"] for x in p),
        "ejecutado": sum(x["ejecutado"] for x in p),
        "proyeccion": sum(x["proyeccion"] for x in p),
        "sin_cronograma": sorted(x["codigo"] for x in p
                                 if x["profundidad"] == "minima"),
    }


COMPARABLES = ("alertas", "proyectos", "verde", "amarillo", "rojo",
               "aprobado", "comprometido", "ejecutado", "proyeccion")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("organizacion", type=Path)
    for c in COMPARABLES:
        ap.add_argument(f"--{c}", type=int, default=None,
                        help="lo que el informe dijo")
    a = ap.parse_args()
    c = cifras(a.organizacion)

    print(f"Día {c['dia']} · {c['proyectos']} proyectos · {c['productos']} productos\n")
    print("Lo que el informe de portafolio tiene que acertar")
    print(f"  alertas de proyecto      {c['alertas_proyecto']}")
    print(f"  semáforo declarado       {c['verde']} verde · {c['amarillo']} amarillo · "
          f"{c['rojo']} rojo")
    print(f"  aprobado                 {c['aprobado']:,} COP")
    print(f"  comprometido             {c['comprometido']:,} COP")
    print(f"  ejecutado                {c['ejecutado']:,} COP")
    print(f"  proyección al cierre     {c['proyeccion']:,} COP")
    print(f"  sin cronograma           {len(c['sin_cronograma'])} · "
          f"{', '.join(c['sin_cronograma'])}")
    print("\n  por señal:")
    for s, n in c["por_senal"].items():
        print(f"    {s:38} {n:>4}")
    print(f"\n  alertas de producto      {c['alertas_producto']} "
          f"(reparte entre los {c['productos']} productos)")

    # ── lo que ningún script calcula
    if any(c["solo_modelo"].values()):
        print("\nSolo el modelo puede encontrar esto — el script no lo calcula")
        for senal, casos in sorted(c["solo_modelo"].items()):
            if casos:
                print(f"  {senal:24} {len(casos)} · {', '.join(casos)}")
        print("  Si el agente no los nombra, es un falso negativo del modelo, no del "
              "código.\n  Si nombra otros, hay que mirar el material antes de culparlo.")

    # ── lo que el informe dijo, contra la clave
    dichos = {k: v for k, v in vars(a).items()
              if k in COMPARABLES and v is not None}
    if not dichos:
        print("\nPasa las cifras del informe con --alertas, --aprobado, … y te digo en "
              "qué se separó.")
        raise SystemExit(0)

    llaves = {"alertas": "alertas_proyecto"}
    print("\nLo que el informe dijo")
    mal = 0
    for k, dicho in dichos.items():
        real = c[llaves.get(k, k)]
        if dicho == real:
            print(f"  ✓ {k:16} {dicho:,}")
        else:
            mal += 1
            razon = ""
            if real and dicho % real == 0 and dicho != real:
                razon = f" — {dicho // real} veces la cifra real"
            elif real and dicho and real % dicho == 0:
                razon = f" — la real es {real // dicho} veces esta"
            print(f"  ✗ {k:16} dijo {dicho:,} · es {real:,}{razon}")
    print(f"\n{'todas coinciden' if not mal else f'{mal} cifra(s) del informe no coinciden'}")
    raise SystemExit(1 if mal else 0)
