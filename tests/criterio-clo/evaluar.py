#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CLO contra la clave del material.

    python3 tests/criterio-clo/evaluar.py                     los dos agentes
    python3 tests/criterio-clo/evaluar.py --agente fidel      solo las señales de Fidel, o de Constanza

Para cada entidad de `material/`: arma la configuración que dejaría el setup, escribe la ficha
de cada contrato y la del periodo de cumplimiento con lo que el agente tendría que extraer de
los documentos escritos —está en la clave—, corre el motor de Fidel y el de Constanza, y
compara cada señal, por su nombre y su clave, contra las esperadas. **Una señal de más falla
igual que una de menos**, y en las entidades de control cualquier señal es una falla.

Comprueba además lo que no depende de ninguna señal: que en las entidades de control el estado
de cada contrato según sus fechas sea el del registro, que cada pago caiga en su contrato y que
el avance de cumplimiento con evidencia de los controles sea el que da la matriz.

Esto prueba el motor con la extracción correcta. La extracción misma —que el agente lea el
contrato, el otrosí o el acta y los registre bien— la prueba la ronda con el agente, sobre el
mismo material.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-legal" / "scripts"))
import legal as L  # noqa: E402

MATERIAL = AQUI / "material"


def evaluar(carpeta: Path) -> dict:
    clave = json.loads((carpeta / "clave.json").read_text(encoding="utf-8"))
    hoy = dt.date.fromisoformat(clave["hoy"])
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        docs = carpeta / clave["config"]["fidel"]["paths"]["documents"]
        for code, ficha in clave["extraccion"]["contratos"].items():
            L.escribir_json(estado / "contratos" / f"{code}.json", ficha)
        L.escribir_json(estado / "cumplimiento" / clave["periodo"] / "ficha.json", clave["extraccion"]["cumplimiento"])
        cfg_f = dict(clave["config"]["fidel"], _docs=docs, _estado=estado)
        cfg_c = json.loads(json.dumps(clave["config"]["constanza"]))
        cfg_c["compliance"]["contract_records"] = str(estado / "contratos")
        cfg_c.update(_docs=docs, _estado=estado)
        rf = L.fidel(cfg_f, hoy)
        rc = L.constanza(cfg_c, clave["periodo"], hoy)
    control = not (clave["siembra"]["fidel"] or clave["siembra"]["constanza"])
    revisar = []
    if control:
        for c in rf["partes"]["contract-register"]["contratos"]:
            if L.norm(c["estado_declarado"]) != L.norm(c["estado_fechas"]):
                revisar.append(f"{c['codigo']}: el registro dice {c['estado_declarado']} y las fechas, {c['estado_fechas']}")
        for c in rf["partes"]["contract-execution"]["contratos"]:
            if c["saldo"] is None or c["saldo"] < 0:
                revisar.append(f"{c['codigo']}: saldo {c['saldo']}")
        cs = rc["partes"]["compliance-status"]
        if any(o["estado"] in ("vencida", "cumplida sin evidencia") for o in cs["obligaciones"]):
            revisar.append("una obligación vencida o sin evidencia en el control")
        if not all(x["en_matriz"] for x in cs["contratos"]) or not cs["contratos"]:
            revisar.append("la obligación de cumplimiento del contrato no cruza con la matriz")
    return {"entidad": clave["entidad"], "pais": clave["pais"], "control": control,
            "esperado": {(x["signal"], x["key"]) for x in clave["esperado"]},
            "obtenido": {(a["signal"], a["key"]) for a in rf["alertas"] + rc["alertas"]},
            "revisar": revisar, "issues": rf["record_issues"] + rc["record_issues"],
            "no_procesado": rf["no_procesado"] + rc["no_procesado"]}


# Qué señales son de cada agente: las de su lista en el diseño.
FAMILIA = json.loads((RAIZ / "families" / "criterio-clo" / "familia.json").read_text(encoding="utf-8"))
DE = {a["id"]: {x["id"] for x in a["senales"]} for a in FAMILIA["agentes"]}


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--agente", choices=sorted(DE))
    agente = ap.parse_args().agente
    suyas = DE[agente] if agente else set().union(*DE.values())
    if not MATERIAL.is_dir():
        print("  falta el material: corre tests/criterio-clo/generar.py")
        return 1
    fallas = 0
    tp = fp = fn = 0
    por_senal: dict[str, list[int]] = {}
    for carpeta in sorted(d for d in MATERIAL.iterdir() if (d / "clave.json").is_file()):
        r = evaluar(carpeta)
        r["esperado"] = {x for x in r["esperado"] if x[0] in suyas}
        r["obtenido"] = {x for x in r["obtenido"] if x[0] in suyas}
        ok_ = r["obtenido"] & r["esperado"]
        de_mas = r["obtenido"] - r["esperado"]
        faltan = r["esperado"] - r["obtenido"]
        tp, fp, fn = tp + len(ok_), fp + len(de_mas), fn + len(faltan)
        for s, _ in r["esperado"] | r["obtenido"]:
            por_senal.setdefault(s, [0, 0, 0])
        for s, _ in ok_:
            por_senal[s][0] += 1
        for s, _ in de_mas:
            por_senal[s][1] += 1
        for s, _ in faltan:
            por_senal[s][2] += 1
        bien = not de_mas and not faltan and not r["revisar"] and not r["issues"] and not r["no_procesado"]
        fallas += not bien
        etiqueta = "control" if r["control"] else f"{len(r['esperado'])} esperadas"
        print(f"  {'ok  ' if bien else 'FALLA'} {carpeta.name:13} {r['pais']}  {etiqueta:13} · {len(ok_)} levantadas · {len(de_mas)} de más · {len(faltan)} sin levantar")
        for s, k in sorted(de_mas):
            print(f"         de más        {s}  {k}")
        for s, k in sorted(faltan):
            print(f"         sin levantar  {s}  {k}")
        for x in r["revisar"] + r["issues"]:
            print(f"         {x}")
        for x in r["no_procesado"]:
            print(f"         no procesado  {x['archivo']}: {x['motivo']}")
    print()
    for s, (a, b, c) in sorted(por_senal.items()):
        print(f"  {s:34} {a} levantadas · {b} de más · {c} sin levantar")
    cubiertas = {s for s, v in por_senal.items() if v[0]}
    del_codigo = set(L.SEVERIDAD) & suyas
    sin_sembrar = sorted(del_codigo - cubiertas)
    print(f"\n  {tp} levantadas, {fp} de más y {fn} sin levantar · {len(cubiertas)} de {len(del_codigo)} señales sembradas al menos una vez")
    if sin_sembrar:
        print(f"  FALLA  señales que el material no siembra: {', '.join(sin_sembrar)}")
        fallas += 1
    print(f"\n{'OK' if not fallas else str(fallas) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
