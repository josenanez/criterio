#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La calidad de cada familia: laboratorio o estable, calculada desde la evidencia de sus rondas.

    python3 scripts/calidad.py              la etiqueta de cada familia y lo que la sostiene
    python3 scripts/calidad.py --selftest   la regla sobre casos conocidos, y la numeración
    python3 scripts/calidad.py --json       la etiqueta de cada familia como datos, para el portal

**La regla (decisión 0020).** Una versión es **estable** si su evidencia con los agentes —cada entidad
del material con su corrida más reciente, sea de la ronda que sea— cumple las tres condiciones; si
no, es de **laboratorio**:

1. el piso del margen del 95 % (Wilson) de la cobertura de las señales sembradas es de 95 % o más;
2. el piso del margen del 95 % de los datos extraídos es de 95 % o más;
3. ninguna entidad de control levantó una señal: una sola es laboratorio, sea cual sea el margen.

En la familia PMO, cada agente cuenta por separado: la precisión y la cobertura de Vera, los
compromisos de Samuel y la cobertura de Alba, y los proyectos de control sin alertas, con la
corrida más reciente de cada industria, como en las demás familias (decisión 0021). Una familia con una entidad que nunca corrió con los
agentes es de laboratorio: no hay con qué sostener otra cosa.

El piso exige muestra: sin fallas, un 95 % pide al menos 73 casos (`casos_minimos`). Una familia que
no falla y no llega es de laboratorio por tamaño, no por error, y la salida es sembrar más señales
por entidad. Este archivo no decide nada que no salga de `tests/evidencias/`: lo leen
`scripts/registro.py`, que anota la etiqueta en cada liberación, y `scripts/hoja.py`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

UMBRAL = 95.0


def casos_minimos(umbral: float = UMBRAL, fallas: int = 0) -> int:
    """Cuántos casos necesita una métrica para que su piso alcance el umbral con esas fallas."""
    import analisis as A
    n = fallas + 1
    while (A.wilson(n - fallas, n) or (0.0, 0.0))[0] < umbral:
        n += 1
    return n


def _pmo() -> dict:
    """Las cifras de la PMO con la misma regla que las demás familias (decisiones 0020 y 0021): cada
    industria con su corrida más reciente, sea de la ronda que sea. Una ronda que agrega industrias
    no obliga a repetir las que ya pasaron; cada agente cuenta por separado."""
    import analisis as A
    R, U, *_ = A.calcular()
    ultima = {}
    for r in R:
        for e, x in r["por_industria"].items():
            ultima[e] = (r["n"], r["version"], x)
    xs = [x for _, _, x in ultima.values()]
    s = lambda f: sum(f(x) or 0 for x in xs)  # noqa: E731
    vtp, vfp, vfn = s(lambda x: x["vera"]["aciertos"]), s(lambda x: x["vera"]["falsos_positivos"]), s(lambda x: x["vera"]["falsos_negativos"])
    sok, stot = s(lambda x: x["samuel"]["correctos"]), s(lambda x: x["samuel"]["total"])
    atp, aesp = s(lambda x: x["alba"]["aciertos"]), s(lambda x: x["alba"]["esperados"])
    ctrl, limpios = s(lambda x: x["vera"].get("controles")), s(lambda x: x["vera"].get("controles_limpios"))
    w = lambda k, n: A.wilson(k, n)[0] if n else 0.0  # noqa: E731
    pisos = {"Vera · precisión": w(vtp, vtp + vfp), "Vera · cobertura": w(vtp, vtp + vfn),
             "Samuel · compromisos": w(sok, stot), "Alba · cobertura": w(atp, aesp)}
    rondas = sorted({n for n, _, _ in ultima.values()})
    return {"ronda": max(rondas), "rondas": rondas, "version_medida": U["version"], "pisos": pisos,
            "controles_con_senal": ctrl - limpios, "completa": True,
            "casos": {"señales": vtp + vfn, "datos": stot + aesp}, "industrias": len(ultima)}


def _familia(sigla: str) -> dict | None:
    import analisis_familias as AF
    import ronda_familia as RF
    if not (RAIZ / "tests" / "evidencias" / "familias" / sigla).is_dir():
        return None
    C, _, ENT = AF.cargar(sigla)
    if not C:
        return None
    # Todas las herramientas, no una sola ronda: cada entidad del material con su corrida más
    # reciente, sea de la ronda que sea. Un país que entra con su propia ronda no obliga a repetir
    # los que ya pasaron, y la muestra es la del material entero, no la de la última ronda.
    ultima: dict = {}
    for c in sorted(C, key=lambda c: c["ronda"]):
        ultima[RF._material(sigla, c["carpeta"])] = c
    faltan = sorted({RF._material(sigla, e) for e in ENT} - set(ultima))
    rondas = sorted({c["ronda"] for c in ultima.values()})
    if faltan:
        return {"ronda": max(rondas), "rondas": rondas, "version_medida": None, "pisos": {}, "controles_con_senal": None,
                "completa": False, "faltan": faltan}
    t = AF.suma(list(ultima.values()))
    import analisis as A
    pisos = {"Señales · cobertura": A.wilson(t["acertadas"], t["esperadas"])[0] if t["esperadas"] else 0.0,
             "Datos extraídos": A.wilson(t["bien"], t["campos"])[0] if t["campos"] else 0.0}
    return {"ronda": max(rondas), "rondas": rondas, "version_medida": None, "pisos": pisos,
            "controles_con_senal": t["controles"] - t["limpios"], "completa": True,
            "casos": {"señales": t["esperadas"], "datos": t["campos"]}}


def calidad(sigla: str) -> dict:
    """La etiqueta de la familia, la ronda que la sostiene y por qué."""
    sys.path.insert(0, str(RAIZ / "tests"))
    m = _pmo() if sigla == "pmo" else _familia(sigla)
    if m is None:
        return {"etiqueta": "laboratorio", "ronda": None, "pisos": {}, "motivo": ["sin ronda con los agentes"], "umbral": UMBRAL}
    motivo = []
    if not m["completa"]:
        motivo.append(f"{len(m.get('faltan') or [])} entidad(es) del material sin ninguna corrida con los agentes")
    for k, v in m["pisos"].items():
        if v < UMBRAL:
            motivo.append(f"{k}: piso de {v:.1f} %, por debajo del {UMBRAL:.0f} %")
    if m["controles_con_senal"]:
        motivo.append(f"{m['controles_con_senal']} entidad(es) de control con una señal")
    return {"etiqueta": "estable" if not motivo else "laboratorio", "ronda": m["ronda"], "rondas": m.get("rondas") or [m["ronda"]],
            "casos": m.get("casos"), "version_medida": m.get("version_medida"),
            "pisos": {k: round(v, 1) for k, v in m["pisos"].items()}, "motivo": motivo, "umbral": UMBRAL,
            "casos_minimos": casos_minimos()}


def siglas() -> list[str]:
    fams = [json.loads(f.read_text(encoding="utf-8")) for f in (RAIZ / "families").glob("criterio-*/familia.json")]
    return [fa["sigla"] for fa in sorted(fams, key=lambda fa: fa["orden"])]


def selftest() -> int:
    """La regla, sobre casos que se conocen: cuánta muestra pide el piso y qué versión puede seguir a cuál."""
    import registro as R
    fallas = []

    def ok(que, real, esperado):
        print(f"  {'ok' if real == esperado else 'FALLA'}  {que}")
        if real != esperado:
            fallas.append(que)
    ok("un piso del 95 % pide 73 casos sin fallas", casos_minimos(), 73)
    ok("y 110 con una falla", casos_minimos(fallas=1), 110)
    ok("de la 0.12.1, la que pasó la 0.9, se sube a la 1.0.0", R.sigue("0.12.1", "1.0.0"), None)
    ok("y no a la 0.13.0", R.sigue("0.12.1", "0.13.0") is not None, True)
    ok("una corrección no cuenta entre las diez", R.sigue("0.12.1", "0.12.2"), None)
    ok("de la 1.8 a la 1.9", R.sigue("1.8.0", "1.9.0"), None)
    ok("después de la 1.9 viene la 2.0", (R.sigue("1.9.0", "1.10.0") is not None, R.sigue("1.9.3", "2.0.0")), (True, None))
    ok("no se salta a la 1.0 antes de la 0.9", R.sigue("0.3.0", "1.0.0") is not None, True)
    ok("una familia lanzada y estable abre la 1.0 desde cualquier 0.y (decisión 0021)", R.sigue("0.2.0", "1.0.0", abre=True), None)
    ok("y sin lanzar sigue su década", R.sigue("0.2.0", "1.0.0") is not None, True)
    ok("abrir la 1.0 no salta a la 2.0", R.sigue("1.3.0", "2.0.0", abre=True) is not None, True)
    ok("una familia nueva empieza en una 0.y.0", (R.sigue(None, "0.1.0"), R.sigue(None, "1.0.0") is not None), (None, True))
    for s in siglas():
        c = calidad(s)
        ok(f"{s.upper()}: la etiqueta es una de las dos y dice por qué si no es estable",
           c["etiqueta"] in ("estable", "laboratorio") and (c["etiqueta"] == "estable") == (not c["motivo"]), True)
    print(f"\n{'OK' if not fallas else str(len(fallas)) + ' FALLAS'}")
    return 1 if fallas else 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    if "--json" in sys.argv:
        # Para quien la publica —el portal—: la misma etiqueta, sin recalcularla allá.
        print(json.dumps({s: calidad(s) for s in siglas()}, ensure_ascii=False, indent=1))
        return 0
    for s in siglas():
        c = calidad(s)
        pisos = " · ".join(f"{k} {v:.1f} %" for k, v in c["pisos"].items()) or "—"
        casos = f" · {c['casos']['señales']} señales, {c['casos']['datos']} datos" if c.get("casos") else ""
        print(f"  {s.upper():4} {c['etiqueta']:11} rondas {', '.join(map(str, c['rondas'])) if c['ronda'] else '—'} · {pisos}{casos}")
        for m in c["motivo"]:
            print(f"       {m}")
    print(f"\n  Un piso del {UMBRAL:.0f} % pide al menos {casos_minimos()} casos sin fallas, {casos_minimos(fallas=1)} con una.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
