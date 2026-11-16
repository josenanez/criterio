#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CHRO contra la clave del material, y la prueba de sesgo.

    python3 tests/criterio-chro/evaluar.py                     los dos agentes
    python3 tests/criterio-chro/evaluar.py --agente candido    solo las señales de uno

Para cada entidad de `material/`: arma la configuración que dejaría el setup de cada agente, escribe la
ficha de Norma y la de Cándido con lo que el agente tendría que extraer de los documentos escritos —está
en la clave—, corre el motor de los dos y compara cada señal, por su nombre y su clave, contra las
esperadas. **Una señal de más falla igual que una de menos.** En las entidades de control solo se espera
el aviso de lo que se excluyó a un miembro de su par de sesgo.

Comprueba además lo que no depende de ninguna señal: que **cada par de la prueba de sesgo dé exactamente
lo mismo** salvo el aviso de lo que se excluyó, que la descarga del estándar se procese con todas sus
ocupaciones, que ninguna ficha deje un documento sin citar y que ningún resultado guarde el valor de un
dato protegido.

Esto prueba el motor con la extracción correcta. La extracción misma —que el agente procese el perfil y la
hoja de vida y los registre bien, sin el dato protegido— la prueba la ronda con los agentes, sobre el
mismo material.
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
sys.path.insert(0, str(RAIZ / "plugins" / "criterio-roles" / "scripts"))
import talento as T  # noqa: E402

MATERIAL = AQUI / "material"
FAMILIA = json.loads((RAIZ / "families" / "criterio-chro" / "familia.json").read_text(encoding="utf-8"))
DE = {a["id"]: {s["id"] for s in a["senales"]} for a in FAMILIA["agentes"]}
MOTOR = {"norma": T.norma, "candido": T.candido}
PROTEGIDO = ("14 de marzo de 1991", "femenino")


def sembrar(clave: dict, estado: Path) -> None:
    """Lo que los agentes extraen de los documentos, escrito en el estado: lo mismo para la prueba del
    motor y para la demostración (scripts/demo.py)."""
    for sub, ficha in clave["extraccion"].items():
        T.escribir_json(estado / sub / clave["periodo"] / "ficha.json", ficha)


def evaluar(carpeta: Path, agentes: list[str]) -> dict:
    clave = json.loads((carpeta / "clave.json").read_text(encoding="utf-8"))
    hoy, periodo = dt.date.fromisoformat(clave["hoy"]), clave["periodo"]
    revisar, obtenido, issues = [], set(), []
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        sembrar(clave, estado)
        for ag in agentes:
            cfg = json.loads(json.dumps(clave["config"][ag]))
            docs = carpeta / cfg["paths"]["documents"]
            cfg.update(_docs=docs, _estado=estado, _raiz=carpeta)
            p = T.revisar_config(cfg, ag)
            if p:
                revisar.append(f"{ag}: la configuración no pasa: {'; '.join(p)}")
            r = MOTOR[ag](cfg, periodo, hoy)
            obtenido |= {(a["signal"], a["key"]) for a in r["alertas"]}
            issues += [f"{ag}: {x}" for x in r["record_issues"]]
            if r["no_procesado"]:
                revisar.append(f"{ag}: no procesó {r['no_procesado']}")
            texto = json.dumps(r, ensure_ascii=False, default=str)
            if any(x in texto for x in PROTEGIDO):
                revisar.append(f"{ag}: un resultado guarda el valor de un dato protegido")
            if ag == "norma":
                est = T.estandar(cfg, [])
                if not est or len(est["ocupaciones"]) != clave["ocupaciones"]:
                    revisar.append("norma: el estándar no se procesó")
            if ag == "candido":
                for f in T.sesgo(r, [tuple(x) for x in clave["pares"]]):
                    revisar.append(f"sesgo: {f}")
    esperado = {(x["signal"], x["key"]) for x in clave["esperado"] if any(x["signal"] in DE[a] for a in agentes)}
    return {"entidad": clave["entidad"], "pais": clave["pais"], "estandar": clave["estandar"], "control": not clave["siembra"],
            "pares": len(clave["pares"]), "esperado": esperado, "obtenido": obtenido, "revisar": revisar, "issues": issues}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--agente", choices=sorted(MOTOR))
    a = ap.parse_args()
    agentes = [a.agente] if a.agente else list(MOTOR)
    if not MATERIAL.is_dir():
        print("no hay material: corre tests/criterio-chro/generar.py")
        return 1
    fallas, total, levantadas, sembradas, pares = 0, 0, 0, set(), 0
    for carpeta in sorted(d for d in MATERIAL.iterdir() if d.is_dir()):
        r = evaluar(carpeta, agentes)
        faltan, sobran = r["esperado"] - r["obtenido"], r["obtenido"] - r["esperado"]
        total += len(r["esperado"])
        levantadas += len(r["esperado"] & r["obtenido"])
        sembradas |= {s for s, _ in r["esperado"]}
        pares += r["pares"] if "candido" in agentes else 0
        mal = bool(faltan or sobran or r["revisar"] or r["issues"])
        fallas += mal
        print(f"  {'FALLA' if mal else 'ok':<5}  {carpeta.name:<15} {r['pais']}  {r['estandar']:<5} {len(r['esperado'] & r['obtenido']):>3} de {len(r['esperado']):>3}"
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
          + (f"; sin sembrar: {', '.join(sin)}" if sin else "") + (f" · {pares} pares de sesgo, cada uno igual" if pares and not fallas else ""))
    if sin:
        fallas += 1
    print("\nOK" if not fallas else f"\n{fallas} FALLAS")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
