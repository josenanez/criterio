#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El soporte de cada rol: el marco de trabajo que lo define y lo que le cuesta hoy a una organización.

    python3 scripts/soporte.py           escribe las FUENTES.es.md que solo esta puerta escribe (la PMO)
    python3 scripts/soporte.py --check   falla si una familia no tiene su soporte

Cada familia, en families/criterio-<familia>/:

- cada agente de familia.json nombra en `marco` la fuente que define su rol;
- esa fuente está en fuentes.json, en la sección `rol`, y está verificada;
- fuentes.json trae al menos tres cifras de terceros verificadas, con su fuente, año y muestra.

Las fuentes de la CFO y la CLO las escribe scripts/familias.py; la de la PMO, esta puerta, con el
mismo formato. Ninguna cifra se teclea aquí.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import familias as FAM  # noqa: E402

MINIMO_CIFRAS = 3
# Las familias cuyas FUENTES.es.md no escribe familias.py.
PROPIAS = {"pmo": "0005-scope-pmo-only.md"}


def revisar(dir_: Path) -> list[str]:
    err = []
    fu_p, fa_p = dir_ / "fuentes.json", dir_ / "familia.json"
    if not fu_p.is_file():
        return [f"{dir_.name}: no tiene fuentes.json con el soporte de sus roles"]
    fu, fa = json.loads(fu_p.read_text(encoding="utf-8")), json.loads(fa_p.read_text(encoding="utf-8"))
    rol = next((s for s in fu["secciones"] if s["id"] == "rol"), None)
    if rol is None:
        err.append(f"{dir_.name}: fuentes.json no tiene la sección «rol»")
    del_rol = {f["id"]: f for f in (rol or {}).get("fuentes", [])}
    todas = {f["id"]: f for s in fu["secciones"] for f in s["fuentes"]}
    for a in fa["agentes"]:
        marco = a.get("marco") or []
        if not marco:
            err.append(f"{dir_.name}: {a['nombre']} no nombra el marco de su rol")
        for m in marco:
            f = todas.get(m)
            if f is None:
                err.append(f"{dir_.name}: {a['nombre']} cita {m}, que no está en fuentes.json")
            elif f["estado"] != "verificada":
                err.append(f"{dir_.name}: el marco de {a['nombre']} ({m}) está por verificar")
            elif m not in del_rol and not any(m in (x.get("uso") or "") for x in del_rol.values()):
                # el marco puede vivir en otra sección —la ISO 37301 de Constanza está en los marcos de
                # referencia—, pero la sección «rol» lo nombra en su uso
                err.append(f"{dir_.name}: el marco de {a['nombre']} ({m}) no está en la sección «rol» ni lo nombra")
    ver = [c for c in fu["cifras"] if c["estado"] == "verificada"]
    if len(ver) < MINIMO_CIFRAS:
        err.append(f"{dir_.name}: {len(ver)} cifras de costo verificadas; el mínimo es {MINIMO_CIFRAS}")
    for c in ver:
        for k in ("fuente", "anio", "enlace"):
            if not c.get(k):
                err.append(f"{dir_.name}: {c['id']} no trae {k}")
        if not (c.get("muestra") or {}).get("es"):
            err.append(f"{dir_.name}: {c['id']} no trae su muestra")
    return err


def fuentes_md(sigla: str) -> str:
    """La FUENTES.es.md de una familia que no pasa por familias.py, con el mismo formato."""
    FAM.F.clear()
    FAM.F.update({"adr": PROPIAS[sigla], "dir": RAIZ / "families" / f"criterio-{sigla}"})
    FAM.CLAVE[0] = sigla
    fu = json.loads((RAIZ / "families" / f"criterio-{sigla}" / "fuentes.json").read_text(encoding="utf-8"))
    return FAM.fuentes_md(fu) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    err = []
    familias = sorted(d for d in (RAIZ / "families").iterdir() if (d / "familia.json").is_file())
    for d in familias:
        err += revisar(d)
    for sigla in PROPIAS:
        ruta = RAIZ / "families" / f"criterio-{sigla}" / "FUENTES.es.md"
        texto = fuentes_md(sigla)
        if a.check:
            if not ruta.is_file() or ruta.read_text(encoding="utf-8") != texto:
                err.append(f"{ruta.relative_to(RAIZ)} no es la que sale de fuentes.json: corre python3 scripts/soporte.py")
        elif not ruta.is_file() or ruta.read_text(encoding="utf-8") != texto:
            ruta.write_text(texto, encoding="utf-8")
            print(f"  {ruta.relative_to(RAIZ)}")
    for e in err:
        print(f"  ✗ {e}")
    if not err:
        print(f"  cada rol de las {len(familias)} familias tiene su marco verificado y cada familia, al menos {MINIMO_CIFRAS} cifras de costo verificadas")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
