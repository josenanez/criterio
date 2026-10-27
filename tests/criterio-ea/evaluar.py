#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia EA contra la clave del material.

    python3 tests/criterio-ea/evaluar.py

Para cada oficina de `material/`: arma la configuración que dejaría el setup, escribe la ficha de
cada sesión y de cada correo con lo que la agente tendría que extraer de los documentos —está en
la clave—, corre el motor de Ofelia y compara cada señal, por su nombre y su clave, contra las
esperadas. **Una señal de más falla igual que una de menos**, y en las oficinas de control
cualquier señal es una falla.

Comprueba además las reglas de la operación real que no son señales: que la agenda vieja avise y
no dé cruces, que un borrador en `40-acta/` se diga, que la carpeta excluida no se procese y que
el informe no se publique en Rostrum por omisión.

Esto prueba el motor con la extracción correcta. La extracción misma la prueba la ronda con la
agente, sobre el mismo material.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-assistant" / "scripts"))
import asistente as A  # noqa: E402


def evaluar(carpeta: Path) -> dict:
    clave = json.loads((carpeta / "clave.json").read_text(encoding="utf-8"))
    hoy = dt.date.fromisoformat(clave["hoy"])
    cfg0 = clave["config"]["ofelia"]
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        for k, f in clave["extraccion"]["reuniones"].items():
            A.escribir_json(estado / "reuniones" / f"{k}.json", f)
        for k, f in clave["extraccion"]["correspondencia"].items():
            A.escribir_json(estado / "correspondencia" / f"{k}.json", f)
        cfg = dict(cfg0, _docs=carpeta / cfg0["paths"]["documents"], _estado=estado)
        problemas = A.revisar_config(cfg, "ofelia")
        r = A.ofelia(cfg, hoy)
    return {"clave": clave, "r": r, "problemas_config": problemas,
            "obtenido": {(a["signal"], a["key"]) for a in r["alertas"]},
            "esperado": {(x["signal"], x["key"]) for x in clave["esperado"]}}


def main() -> int:
    material = AQUI / "material"
    if not material.is_dir():
        print("no hay material: corre python3 tests/criterio-ea/generar.py")
        return 1
    fallas = 0
    por_senal: dict[str, list[int]] = {}
    total = [0, 0, 0]
    for carpeta in sorted(x for x in material.iterdir() if x.is_dir()):
        e = evaluar(carpeta)
        ok, sobran, faltan = e["obtenido"] & e["esperado"], e["obtenido"] - e["esperado"], e["esperado"] - e["obtenido"]
        for s_, _ in e["esperado"] | e["obtenido"]:
            v = por_senal.setdefault(s_, [0, 0, 0])
        for s_, _ in ok:
            por_senal[s_][0] += 1
        for s_, _ in sobran:
            por_senal[s_][1] += 1
        for s_, _ in faltan:
            por_senal[s_][2] += 1
        total = [total[0] + len(ok), total[1] + len(sobran), total[2] + len(faltan)]
        reglas = []
        siembra = set(e["clave"]["siembra"])
        r = e["r"]
        if e["problemas_config"]:
            reglas.append(f"la configuración de la clave no pasa: {e['problemas_config']}")
        if ("agenda_vieja" in siembra) != bool(r["avisos"]):
            reglas.append("la agenda vieja tiene que avisar, y solo ella")
        if ("borrador_en_acta" in siembra) != any("borrador en 40-acta" in x["motivo"] for x in r["no_procesado"]):
            reglas.append("un borrador en 40-acta/ tiene que decirse, y solo ese")
        if "carpeta_excluida" in siembra and any("personal" in (x.get("archivo") or "") for x in r["no_procesado"]):
            reglas.append("la carpeta excluida no se procesa ni se menciona como pendiente")
        if r["publica_en_rostrum"]:
            reglas.append("el informe no se publica en Rostrum por omisión")
        if r["record_issues"]:
            reglas.append(f"las fichas de la clave traen problemas: {r['record_issues']}")
        mal = bool(sobran or faltan or reglas)
        fallas += mal
        print(f"  {'FALLA' if mal else 'ok   '} {carpeta.name:13} {e['clave']['pais']}  {len(e['esperado']):2} esperadas · "
              f"{len(ok):2} levantadas · {len(sobran)} de más · {len(faltan)} sin levantar")
        for x in sorted(sobran):
            print(f"         de más        {x[0]}  {x[1]}")
        for x in sorted(faltan):
            print(f"         sin levantar  {x[0]}  {x[1]}")
        for x in reglas:
            print(f"         regla         {x}")
    print()
    for s_, (a, b, c) in sorted(por_senal.items()):
        print(f"  {s_:30} {a} levantadas · {b} de más · {c} sin levantar")
    sembradas = {s_ for s_, v in por_senal.items() if v[0] or v[2]}
    todas = set(A.SEVERIDAD)
    print(f"  {total[0]} levantadas, {total[1]} de más y {total[2]} sin levantar · {len(sembradas & todas)} de {len(todas)} señales sembradas al menos una vez")
    if todas - sembradas:
        print(f"  FALLA: sin sembrar {', '.join(sorted(todas - sembradas))}")
        fallas += 1
    print(f"\n{'OK' if not fallas else str(fallas) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    raise SystemExit(main())
