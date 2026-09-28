# -*- coding: utf-8 -*-
"""El resumen de las corridas diarias: qué se sostiene y qué se movió.

    python3 tests/sintetico/resumen.py

Una corrida dice cómo salió ese día. Cinco dicen otra cosa: **si la fiabilidad se
sostiene cuando cambia algo que no debería importar.** Cada día el material se escribe
con una disposición distinta —ordenado, plano, revuelto, sin carpetas— y lo esperado no
cambia, así que una caída entre días no es ruido: es una dependencia que no sabíamos que
teníamos.

Lee todos los `tests/informes/*.json` y escribe `tests/informes/RESUMEN.md`.
"""
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).parent.parent.parent
INFORMES = RAIZ / "tests" / "informes"


def barra(pct, ancho=20):
    if pct is None:
        return "—"
    return "█" * max(1, round(ancho * pct / 100))


if __name__ == "__main__":
    dias = []
    for f in sorted(INFORMES.glob("*.json")):
        try:
            dias.append(json.loads(f.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    if not dias:
        sys.exit("no hay corridas todavía en tests/informes/")

    p = ["# Resumen de las corridas", "",
         f"**{len(dias)} corrida(s)**, de la del {dias[0]['fecha']} a la del "
         f"{dias[-1]['fecha']}.", "",
         "Cada día el mismo material se escribe con una disposición distinta y lo "
         "esperado no cambia. Una diferencia entre días no es ruido: es una dependencia "
         "que no sabíamos que teníamos.", "",
         "## Día a día", "",
         "| Día | Disposición | Docs | Tiempo | Aciertos | Falsos + | Falsos − | Precisión | Cobertura | Controles |",
         "|---|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for d in dias:
        t, ms = d["totales"], sum(d["tiempos"].values())
        ctrl = d.get("controles", {})
        marca = "✓" if not any(ctrl.values()) else "✗ " + ", ".join(
            c for c, n in ctrl.items() if n)
        p.append(f"| {d['fecha']} | {d['disposicion']} | {d['documentos']['total']} | "
                 f"{ms / 1000:.1f} s | {t['aciertos']} | {t['falsos_positivos']} | "
                 f"{t['falsos_negativos']} | {t['precision']}% | {t['cobertura']}% | "
                 f"{marca} |")
    p.append("")

    # ── lo que se movió entre días
    prec = [d["totales"]["precision"] for d in dias if d["totales"]["precision"] is not None]
    cob = [d["totales"]["cobertura"] for d in dias if d["totales"]["cobertura"] is not None]
    tiempos = [sum(d["tiempos"].values()) / max(d["documentos"]["total"], 1) for d in dias]
    p += ["## Qué se sostiene", "", "| | Mínimo | Máximo | Mediana |", "|---|---:|---:|---:|"]
    for nombre, serie, suf in (("Precisión", prec, "%"), ("Cobertura", cob, "%"),
                               ("ms por documento", tiempos, "")):
        if serie:
            p.append(f"| {nombre} | {min(serie):.1f}{suf} | {max(serie):.1f}{suf} | "
                     f"{statistics.median(serie):.1f}{suf} |")
    p.append("")
    if prec and min(prec) == max(prec) == 100:
        p += ["**La precisión no se movió entre disposiciones.** Con el material escrito "
              "de cuatro formas distintas, el agente reportó lo mismo: el recorrido no "
              "depende de cómo esté organizada la carpeta.", ""]
    elif prec:
        peor = min(dias, key=lambda d: d["totales"]["precision"] or 100)
        p += [f"**La precisión sí se movió**, y lo peor fue el {peor['fecha']} con la "
              f"disposición «{peor['disposicion']}». Eso es una dependencia del layout, "
              f"y es un defecto, no una variación.", ""]

    # ── la señal menos fiable del conjunto
    acum = defaultdict(lambda: Counter())
    for d in dias:
        for s, f in d["calificacion"]["por_senal"].items():
            acum[s]["aciertos"] += f["aciertos"]
            acum[s]["fp"] += f["fp"]
            acum[s]["fn"] += f["fn"]
    flojas = {s: f for s, f in acum.items() if f["fp"] or f["fn"]}
    p += ["## Qué arreglar", ""]
    if not flojas:
        p += ["Ninguna señal falló en ninguna corrida.", ""]
    else:
        p += ["En orden de prioridad: el falso positivo primero. Un hallazgo que no era "
              "cierto hace que la siguiente lista no se lea; uno que faltó hace que se "
              "lea incompleta.", "",
              "| Señal | Aciertos | Falsos + | Falsos − | Precisión |",
              "|---|---:|---:|---:|---:|"]
        for s, f in sorted(flojas.items(), key=lambda x: (-x[1]["fp"], -x[1]["fn"])):
            em = f["aciertos"] + f["fp"]
            pr = f"{100 * f['aciertos'] / em:.0f}%" if em else "—"
            p.append(f"| `{s}` | {f['aciertos']} | {f['fp']} | {f['fn']} | {pr} |")
        p.append("")

    errores = [(d["fecha"], e) for d in dias for e in d.get("errores", [])]
    if errores:
        p += ["## Errores de ejecución", ""]
        for fecha, e in errores:
            p.append(f"- **{fecha}** · {e}")
        p.append("")

    p += ["---", "",
          "Lo que estas corridas **no** miden: la extracción con modelo, documentos que "
          "no sean markdown ni CSV, y una organización real. El material es sintético y "
          "su estructura se conoce.", ""]
    (INFORMES / "RESUMEN.md").write_text("\n".join(p) + "\n", encoding="utf-8")
    print(f"{len(dias)} corridas → tests/informes/RESUMEN.md")
    if prec:
        print(f"  precisión {min(prec):.0f}–{max(prec):.0f}% · "
              f"cobertura {min(cob):.0f}–{max(cob):.0f}%")
    print(f"  señales con fallo: {', '.join(flojas) if flojas else 'ninguna'}")
