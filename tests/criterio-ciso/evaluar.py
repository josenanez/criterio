#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CISO contra la clave del material.

    python3 tests/criterio-ciso/evaluar.py                      los tres agentes
    python3 tests/criterio-ciso/evaluar.py --agente guillermo   solo las señales de uno

Para cada entidad de `material/`: arma la configuración que dejaría el setup de cada agente —con los
plazos que el agente toma de cada política y, si el escáner lo pide, su mapeo de columnas—, escribe la
ficha de Alexis y la de Amparo con lo que el agente tendría que extraer de los documentos escritos
—está en la clave—, corre el motor de los tres y compara cada señal, por su nombre y su clave, contra
las esperadas. **Una señal de más falla igual que una de menos**, y en las entidades de control
cualquier señal es una falla.

Comprueba además lo que no depende de ninguna señal: que se excluya exactamente lo que nunca se abre
—la llave, las credenciales y el respaldo—, que las tres exportaciones del escáner se procesen sin
columnas de menos, que ninguna ficha deje un documento sin citar y que ningún resultado guarde el
contenido de lo excluido.

Esto prueba el motor con la extracción correcta. La extracción misma —que el agente lea la evidencia,
el informe del incidente o la política y los registre bien— la prueba la ronda con los agentes, sobre
el mismo material.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-security" / "scripts"))
import seguridad as S  # noqa: E402

MATERIAL = AQUI / "material"
FAMILIA = json.loads((RAIZ / "families" / "criterio-ciso" / "familia.json").read_text(encoding="utf-8"))
DE = {a["id"]: {s["id"] for s in a["senales"]} for a in FAMILIA["agentes"]}
MOTOR = {"alexis": S.alexis, "guillermo": S.guillermo, "amparo": S.amparo}


def evaluar(carpeta: Path, agentes: list[str]) -> dict:
    clave = json.loads((carpeta / "clave.json").read_text(encoding="utf-8"))
    hoy, periodo = dt.date.fromisoformat(clave["hoy"]), clave["periodo"]
    revisar, obtenido, issues = [], set(), []
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        for sub, ficha in clave["extraccion"].items():
            S.escribir_json(estado / sub / periodo / "ficha.json", ficha)
        for ag in agentes:
            cfg = json.loads(json.dumps(clave["config"][ag]))
            docs = carpeta / cfg["paths"]["documents"]
            cfg.update(_docs=docs, _estado=estado, _raiz=carpeta)
            p = S.revisar_config(cfg, ag)
            if p:
                revisar.append(f"{ag}: la configuración no pasa: {'; '.join(p)}")
            r = MOTOR[ag](cfg, periodo, hoy)
            obtenido |= {(a["signal"], a["key"]) for a in r["alertas"]}
            issues += [f"{ag}: {x}" for x in r["record_issues"]]
            excl = sorted(x["archivo"] for x in r["no_procesado"] if x["motivo"].startswith("excluido"))
            if excl != sorted(clave["excluidos"]):
                revisar.append(f"{ag}: excluyó {excl} y la clave dice {sorted(clave['excluidos'])}")
            if "NO-ES-UNA-LLAVE" in json.dumps(r, ensure_ascii=False, default=str) or "no-es-una-clave" in json.dumps(r, ensure_ascii=False, default=str):
                revisar.append(f"{ag}: un resultado guarda el contenido de algo excluido")
            otros = [x for x in r["no_procesado"] if not x["motivo"].startswith("excluido")]
            if otros:
                revisar.append(f"{ag}: no procesó {otros}")
            if ag == "guillermo":
                esc = r["partes"]["vuln-scan"]["escaneos"]
                if len(esc) != 3:
                    revisar.append(f"guillermo: procesó {len(esc)} exportaciones del escáner y son 3")
                if not r["partes"]["vuln-scan"]["kev"]["entradas"]:
                    revisar.append("guillermo: no procesó el catálogo KEV")
    esperado = {(x["signal"], x["key"]) for x in clave["esperado"] if any(x["signal"] in DE[a] for a in agentes)}
    return {"entidad": clave["entidad"], "pais": clave["pais"], "escaner": clave["escaner"], "control": not clave["siembra"],
            "esperado": esperado, "obtenido": obtenido, "revisar": revisar, "issues": issues}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--agente", choices=sorted(MOTOR))
    a = ap.parse_args()
    agentes = [a.agente] if a.agente else list(MOTOR)
    if not MATERIAL.is_dir():
        print("no hay material: corre tests/criterio-ciso/generar.py")
        return 1
    fallas, total, levantadas, sembradas = 0, 0, 0, set()
    for carpeta in sorted(d for d in MATERIAL.iterdir() if d.is_dir()):
        r = evaluar(carpeta, agentes)
        faltan, sobran = r["esperado"] - r["obtenido"], r["obtenido"] - r["esperado"]
        total += len(r["esperado"])
        levantadas += len(r["esperado"] & r["obtenido"])
        sembradas |= {s for s, _ in r["esperado"]}
        mal = bool(faltan or sobran or r["revisar"] or r["issues"])
        fallas += mal
        print(f"  {'FALLA' if mal else 'ok':<5}  {carpeta.name:<15} {r['pais']}  {r['escaner']:<13} {len(r['esperado'] & r['obtenido']):>3} de {len(r['esperado']):>3}"
              + (" · control" if r["control"] else ""))
        for s, k in sorted(faltan):
            print(f"         falta  {s}  {k}")
        for s, k in sorted(sobran):
            print(f"         sobra  {s}  {k}")
        for x in r["revisar"] + r["issues"]:
            print(f"         revisar  {x}")
    todas = set().union(*(DE[x] for x in agentes))
    sin = sorted(todas - sembradas)
    print(f"\n  {levantadas} levantadas, {total - levantadas} sin levantar · {len(sembradas)} de {len(todas)} señales sembradas al menos una vez"
          + (f"; sin sembrar: {', '.join(sin)}" if sin else ""))
    if sin:
        fallas += 1
    print("\nOK" if not fallas else f"\n{fallas} FALLAS")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
