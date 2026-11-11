#!/usr/bin/env python3
"""El montaje de una toma: de su línea de tiempo (linea.json) y del guion salen las anclas —tiempo de la
toma → tiempo del video— y los capítulos. La toma no se edita: se acelera, se sostiene y se corta entre
anclas.

    python3 uso/montaje.py <toma> <guion.json>      escribe <toma>/montaje.json

Reglas, iguales para cada video de uso:
- Lo que escribe la persona va a 1,4×.
- Lo que hace el agente se comprime a una quinta parte, entre 1 y 5 segundos.
- Lo que el agente deja en pantalla se sostiene para leerlo (3,5 s, o lo que diga el guion).
- La espera entre una respuesta y la siguiente entrada se corta.
"""
import bisect, json, sys
from pathlib import Path

toma = Path(sys.argv[1])
L = json.loads((toma / "linea.json").read_text(encoding="utf-8"))
G = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
C, E = L["cambios"], L["entradas"]
anclas = [(G["desde"], 0.0)]


def a(cast, dur):
    """Avanza hasta `cast` en `dur` segundos de video."""
    anclas.append((cast, anclas[-1][1] + max(dur, 0.04)))


def sostener(seg):
    anclas.append((anclas[-1][0], anclas[-1][1] + seg))


inicios = [e["enviado"] - 0.06 * len(e["texto"]) - 0.8 for e in E]
for i, e in enumerate(E):
    ini = max(inicios[i], anclas[-1][0])
    a(ini, 0.15)                                   # el corte de la espera
    a(e["enviado"], (e["enviado"] - ini) / 1.4)     # la persona escribe
    o = G["entradas"].get(str(i), {})
    if "anclas" in o:                              # un tramo montado a mano
        for cast, dur, sost in o["anclas"]:
            a(cast, dur)
            if sost:
                sostener(sost)
        continue
    sig = inicios[i + 1] if i + 1 < len(E) else G["hasta"]
    R = C[bisect.bisect_left(C, sig - 0.3) - 1]
    R = max(R, e["enviado"])
    a(R, o.get("dur", min(max((R - e["enviado"]) / 5, 1.0), 5.0)))
    sostener(o.get("sostener", 3.5))

capitulos = [{**c, "video": None} for c in G["capitulos"]]
# El tiempo de video de cada capítulo: el primero de la toma que lo alcanza.
for c in capitulos:
    for (c0, v0), (c1, v1) in zip(anclas, anclas[1:]):
        if c0 <= c["desde"] <= c1 and c1 > c0:
            c["video"] = round(v0 + (c["desde"] - c0) / (c1 - c0) * (v1 - v0), 3)
            break
        if c["desde"] < c0:
            c["video"] = round(v0, 3)
            break
(toma / "montaje.json").write_text(json.dumps({"anclas": anclas, "capitulos": capitulos, "duracion": anclas[-1][1]}, ensure_ascii=False), encoding="utf-8")
print(f"{len(anclas)} anclas · {anclas[-1][1]:.1f} s de toma montada")
for c in capitulos:
    print(f"  {c['video']:7.1f} s  {c['titulo'][:40]} · {c['texto'][:50]}")
