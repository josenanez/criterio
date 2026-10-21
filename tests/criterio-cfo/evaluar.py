#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CFO contra la clave del material.

    python3 tests/criterio-cfo/evaluar.py                  los dos agentes
    python3 tests/criterio-cfo/evaluar.py --agente clara   solo las señales de Clara, o de Tomás

Para cada entidad de `material/`: arma la configuración que dejaría el setup, escribe en la
ficha lo que el agente tendría que extraer de los documentos escritos —está en la clave—, corre
el motor de Clara y el de Tomás, y compara cada señal, por su nombre y su clave, contra las
esperadas. **Una señal de más falla igual que una de menos**, y en las entidades de control
cualquier señal es una falla.

Comprueba además la aritmética que no depende de ninguna señal: que en cada cuenta bancaria la
diferencia sin explicar sea cero, que el balance cuadre donde no se sembró el descuadre y que
cada factura cruce con su registro o tenga su señal.

Esto prueba el motor con la extracción correcta. La extracción misma —que el agente lea el acta
y la registre bien— la prueba la ronda con el agente, sobre el mismo material.
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-finance" / "scripts"))
import finanzas as F  # noqa: E402

MATERIAL = AQUI / "material"


def evaluar(carpeta: Path) -> dict:
    clave = json.loads((carpeta / "clave.json").read_text(encoding="utf-8"))
    hoy = dt.date.fromisoformat(clave["hoy"])
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        docs = carpeta / clave["config"]["clara"]["paths"]["documents"]
        cfg_c = dict(clave["config"]["clara"], _docs=docs, _estado=estado)
        tomas_cfg = json.loads(json.dumps(clave["config"]["tomas"]))
        tomas_cfg["budget"]["pmo_records"] = str(carpeta / tomas_cfg["budget"]["pmo_records"])
        cfg_t = dict(tomas_cfg, _docs=docs, _estado=estado)
        F.escribir_json(estado / "cierre" / cfg_c["period"] / "ficha.json", clave["extraccion"]["cierre"])
        F.escribir_json(estado / "presupuesto" / cfg_t["budget"]["year"] / "ficha.json", clave["extraccion"]["presupuesto"])
        rc = F.clara(cfg_c, cfg_c["period"], hoy)
        rt = F.tomas(cfg_t, cfg_t["budget"]["year"], cfg_t["budget"]["cut"], hoy)
    obtenido = {(a["signal"], a["key"]) for a in rc["alertas"] + rt["alertas"]}
    esperado = {(x["signal"], x["key"]) for x in clave["esperado"]}
    aritmetica = []
    for c in rc["partes"]["bank-reconcile"]["cuentas"]:
        if abs(c["diferencia_sin_explicar"]) > 0.005:
            aritmetica.append(f"{c['cuenta']}: diferencia sin explicar {c['diferencia_sin_explicar']}")
    if "balance_descuadrado" not in clave["siembra"] and abs(rc["partes"]["ledger-check"].get("diferencia") or 0) > 0.005:
        aritmetica.append(f"el balance no cuadra: {rc['partes']['ledger-check']['diferencia']}")
    fi = rc["partes"]["einvoice-check"]
    sin_cruce = fi["facturas"] - fi["cruzadas"] - len(fi["solo_identidad"]) - sum(1 for a in rc["alertas"] if a["signal"] == "einvoice_not_recorded")
    if sin_cruce:
        aritmetica.append(f"{sin_cruce} facturas sin cruce ni señal")
    no_proc = rc["partes"]["einvoice-check"]["no_procesado"] + [x for p in rc["partes"].values() for x in p.get("no_procesado", []) if "factura" not in x["motivo"]] + rt.get("no_procesado", [])
    return {"entidad": clave["entidad"], "pais": clave["pais"], "control": not clave["siembra"],
            "esperado": esperado, "obtenido": obtenido, "aritmetica": aritmetica, "issues": rc["record_issues"] + rt["record_issues"],
            "no_procesado": [x for x in no_proc if "para revisar" not in x["motivo"]]}


# Qué señales son de cada agente: las de su lista en el diseño.
FAMILIA = json.loads((RAIZ / "families" / "criterio-cfo" / "familia.json").read_text(encoding="utf-8"))
DE = {a["id"]: {x["id"] for x in a["senales"]} for a in FAMILIA["agentes"]}


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--agente", choices=sorted(DE))
    agente = ap.parse_args().agente
    suyas = DE[agente] if agente else set().union(*DE.values())
    if not MATERIAL.is_dir():
        print("  falta el material: corre tests/criterio-cfo/generar.py")
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
        if agente == "tomas":
            r["aritmetica"] = []
        bien = not de_mas and not faltan and not r["aritmetica"] and not r["issues"] and not r["no_procesado"]
        fallas += not bien
        etiqueta = "control" if r["control"] else f"{len(r['esperado'])} esperadas"
        print(f"  {'ok  ' if bien else 'FALLA'} {carpeta.name:13} {r['pais']}  {etiqueta:13} · {len(ok_)} levantadas · {len(de_mas)} de más · {len(faltan)} sin levantar")
        for s, k in sorted(de_mas):
            print(f"         de más        {s}  {k}")
        for s, k in sorted(faltan):
            print(f"         sin levantar  {s}  {k}")
        for x in r["aritmetica"] + r["issues"]:
            print(f"         {x}")
        for x in r["no_procesado"]:
            print(f"         no procesado  {x['archivo']}: {x['motivo']}")
    print()
    for s, (a, b, c) in sorted(por_senal.items()):
        print(f"  {s:34} {a} levantadas · {b} de más · {c} sin levantar")
    cubiertas = {s for s, v in por_senal.items() if v[0]}
    from_code = set(F.SEVERIDAD) & suyas
    sin_sembrar = sorted(from_code - cubiertas)
    print(f"\n  {tp} levantadas, {fp} de más y {fn} sin levantar · {len(cubiertas)} de {len(from_code)} señales sembradas al menos una vez")
    if sin_sembrar:
        print(f"  FALLA  señales que el material no siembra: {', '.join(sin_sembrar)}")
        fallas += 1
    print(f"\n{'OK' if not fallas else str(fallas) + ' FALLAS'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
