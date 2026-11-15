#!/usr/bin/env python3
"""La transcripción de un video de uso, para quien no lo ve: lo que dice la pantalla, en orden y con su minuto.

    python3 uso/transcribir.py <toma> <guion.json>     escribe transcripciones/criterio-<familia>-uso-<idioma>.txt

Sale de lo mismo que el video —el guion, el montaje (montaje.json) y la línea de tiempo de la toma
(linea.json)—, así que dice lo mismo: la portada, cada capítulo con su texto, cada entrada que escribe la
persona en Claude Code, en el segundo del video en que se envía, y el cierre. Lo que el agente responde en
la terminal lo cuentan los capítulos, que citan solo cifras que están en pantalla en ese momento.
Los tiempos son los de render.mjs: la portada dura INTRO segundos y el cierre, CIERRE.
"""
import json
import sys
from pathlib import Path

INTRO, CIERRE = 5, 7   # los de render.mjs

toma, guion = Path(sys.argv[1]), Path(sys.argv[2])
G = json.loads(guion.read_text(encoding="utf-8"))
M = json.loads((toma / "montaje.json").read_text(encoding="utf-8"))
L = json.loads((toma / "linea.json").read_text(encoding="utf-8"))
A = M["anclas"]


def video(cast: float) -> float:
    """El segundo del video en que se ve el segundo `cast` de la toma: el primero que lo alcanza."""
    for (c0, v0), (c1, v1) in zip(A, A[1:]):
        if c0 <= cast <= c1 and c1 > c0:
            return INTRO + v0 + (cast - c0) / (c1 - c0) * (v1 - v0)
    return INTRO + A[-1][1]


def minuto(s: float) -> str:
    return f"{int(s // 60)}:{int(s % 60):02d}"


lineas = [(0.0, f"{G['eyebrow']}"), (0.0, f"{G['intro']['titulo']} {G['intro']['sub']}"),
          (0.0, " · ".join(G["intro"]["nombres"])), (0.0, G["intro"]["texto"])]
ev = [(c["video"] + INTRO, f"{c['n']} · {c['titulo']}. {c['texto']}") for c in M["capitulos"]]
ev += [(video(e["enviado"]), f"Se escribe en Claude Code: {e['texto']}") for e in L["entradas"]]
lineas += sorted(ev, key=lambda x: x[0])
fin = INTRO + M["duracion"]
c = G["cierre"]
lineas += [(fin, c["titulo"]), (fin, c["comando"]), (fin, c["url"]), (fin, c["licencia"]), (fin, c["aviso"])]
vistos, salida = set(), []
for s, t in lineas:
    if t not in vistos:
        vistos.add(t)
        salida.append(f"{minuto(s)}  {t}")
destino = Path(__file__).resolve().parent.parent / "transcripciones" / f"criterio-{G['familia']}-uso-{G['idioma']}.txt"
destino.write_text("\n".join(salida) + "\n", encoding="utf-8")
print(f"{destino.name} · {len(salida)} líneas · {minuto(fin + CIERRE)}")
