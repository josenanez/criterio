#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CSO contra la clave del material.

    python3 tests/criterio-cso/evaluar.py                     los dos agentes
    python3 tests/criterio-cso/evaluar.py --agente augusto    solo las señales de Augusto, o de Valeria

Para cada entidad de `material/`: arma la configuración que dejaría el setup, escribe la ficha del
periodo de Augusto y la de Valeria con lo que el agente tendría que extraer de los documentos
escritos —está en la clave—, corre el motor de los dos y compara cada señal, por su nombre y su
clave, contra las esperadas. **Una señal de más falla igual que una de menos**, y en las entidades
de control cualquier señal es una falla.

Comprueba además lo que no depende de ninguna señal: que cada exportación se procese en su formato
sin columnas de más ni de menos, que en los controles cada venta ganada tenga su contrato y su
factura y que el respaldo del pronóstico sostenga lo comprometido, y que ninguna ficha ni ningún
resultado guarde un dato de contacto de un cliente.

Esto prueba el motor con la extracción correcta. La extracción misma —que el agente lea la
propuesta, el acta o la cotización y los registre bien— la prueba la ronda con los agentes, sobre
el mismo material.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-sales" / "scripts"))
import ventas as V  # noqa: E402

MATERIAL = AQUI / "material"
FORMATO = {"salesforce-api": "salesforce", "salesforce-informe": "salesforce", "hubspot-csv": "hubspot", "hubspot-xlsx": "hubspot",
           "generico-csv": "generico", "generico-xlsx": "generico"}


def evaluar(carpeta: Path) -> dict:
    clave = json.loads((carpeta / "clave.json").read_text(encoding="utf-8"))
    hoy, periodo = dt.date.fromisoformat(clave["hoy"]), clave["periodo"]
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        V.escribir_json(estado / "comercial" / periodo / "ficha.json", clave["extraccion"]["comercial"])
        V.escribir_json(estado / "ingresos" / periodo / "ficha.json", clave["extraccion"]["ingresos"])
        cfg_a = json.loads(json.dumps(clave["config"]["augusto"]))
        cfg_v = json.loads(json.dumps(clave["config"]["valeria"]))
        docs = carpeta / cfg_a["paths"]["documents"]
        for c in (cfg_a, cfg_v):
            c.update(_docs=docs, _estado=estado, _raiz=carpeta)
        ra = V.augusto(cfg_a, periodo, hoy)
        rv = V.valeria(cfg_v, periodo, hoy)
        resultados = json.dumps([ra, rv], ensure_ascii=False, default=str)
    control = not clave["siembra"]
    revisar = []
    formatos = {x["formato"] for x in ra["partes"]["pipeline-scan"]["exportaciones"]}
    if formatos != {FORMATO[clave["crm"]]} or len(ra["partes"]["pipeline-scan"]["exportaciones"]) != 3:
        revisar.append(f"las exportaciones se procesaron como {sorted(formatos)}, y el CRM es {clave['crm']}")
    if "@" in resultados:
        revisar.append("un resultado guarda un correo: los datos de contacto de los clientes no entran")
    if control:
        f = ra["partes"]["forecast-check"]
        if f["comprometido"] is None or f["comprometido"] > f["respaldo"] * 1.1:
            revisar.append(f"el respaldo del pronóstico ({f['respaldo']}) no sostiene lo comprometido ({f['comprometido']})")
        for g in rv["partes"]["won-to-invoice"]["ganadas"]:
            if not g["contrato"] or not g["factura"]:
                revisar.append(f"{g['id']}: ganada sin contrato o sin factura en el control")
        if any(not q["dentro"] for q in rv["partes"]["discount-check"]["cotizaciones"]):
            revisar.append("un descuento fuera de la política en el control")
    return {"entidad": clave["entidad"], "pais": clave["pais"], "crm": clave["crm"], "control": control,
            "esperado": {(x["signal"], x["key"]) for x in clave["esperado"]},
            "obtenido": {(a["signal"], a["key"]) for a in ra["alertas"] + rv["alertas"]},
            "revisar": revisar, "issues": ra["record_issues"] + rv["record_issues"],
            "no_procesado": ra["no_procesado"] + rv["no_procesado"]}


# Qué señales son de cada agente: las de su lista en el diseño.
FAMILIA = json.loads((RAIZ / "families" / "criterio-cso" / "familia.json").read_text(encoding="utf-8"))
DE = {a["id"]: {x["id"] for x in a["senales"]} for a in FAMILIA["agentes"]}


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--agente", choices=sorted(DE))
    agente = ap.parse_args().agente
    suyas = DE[agente] if agente else set().union(*DE.values())
    if not MATERIAL.is_dir():
        print("  falta el material: corre tests/criterio-cso/generar.py")
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
        print(f"  {'ok  ' if bien else 'FALLA'} {carpeta.name:15} {r['pais']}  {r['crm']:19} {etiqueta:13} · {len(ok_)} levantadas · {len(de_mas)} de más · {len(faltan)} sin levantar")
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
    del_codigo = set(V.SEVERIDAD) & suyas
    sin_sembrar = sorted(del_codigo - cubiertas)
    print(f"\n  {tp} levantadas, {fp} de más y {fn} sin levantar · {len(cubiertas)} de {len(del_codigo)} señales sembradas al menos una vez")
    if sin_sembrar:
        print(f"  FALLA  señales que el material no siembra: {', '.join(sin_sembrar)}")
        fallas += 1
    print(f"\n{'OK' if not fallas else str(fallas) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
