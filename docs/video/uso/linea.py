#!/usr/bin/env python3
"""La línea de tiempo de una toma: cuándo cambia la conversación y cuándo se escribe y se envía cada
entrada del guion. La lee el montaje.

    python3 uso/linea.py <toma> <guion.json>      escribe <toma>/linea.json

Las entradas son las del guion («escrito»), en el orden en que se escribieron. Una entrada está escrita
cuando la caja de entrada de Claude Code la muestra completa, y enviada cuando la caja la deja: así no
confunde la sugerencia gris que Claude Code a veces propone con lo que escribió la persona.
"""
import json, sys
from pathlib import Path

import pyte

toma, guion = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
ev = [json.loads(l) for l in (toma / "toma.cast").read_text(encoding="utf-8").splitlines()[1:] if l.strip()]
E = guion["escrito"]
sc = pyte.Screen(120, 36)
st = pyte.ByteStream(sc)
prev, cambios, out, k, fase, lleno = None, [], [], 0, "espera", None
for t, _, d in ev:
    st.feed(d.encode())
    disp = sc.display
    # La caja de entrada: entre las dos últimas líneas horizontales; arriba, la conversación.
    hs = [i for i, l in enumerate(disp) if l.startswith("────")]
    caja = "".join(l.strip() for l in disp[hs[-2] + 1:hs[-1]]).replace("\xa0", " ") if len(hs) >= 2 else ""
    cuerpo = "\n".join(disp[:hs[-2]] if len(hs) >= 2 else disp)
    if cuerpo != prev:
        cambios.append(t)
        prev = cuerpo
    if k < len(E):
        e = E[k]
        if fase == "espera" and caja.replace(" ", "") == ("❯" + e).replace(" ", ""):
            lleno, fase = t, "lleno"
        elif fase == "lleno" and caja.replace(" ", "") != ("❯" + e).replace(" ", ""):
            out.append({"texto": e, "lleno": lleno, "enviado": t})
            k, fase = k + 1, "espera"
if k < len(E):
    raise SystemExit(f"La toma no tiene la entrada {k}: «{E[k]}»")
(toma / "linea.json").write_text(json.dumps({"cambios": cambios, "entradas": out}, ensure_ascii=False), encoding="utf-8")
for i, x in enumerate(out):
    print(f"{i:3} {x['enviado']:8.1f}  {x['texto'][:70]}")
