#!/usr/bin/env python3
"""Lo que cuesta cada comando en las pruebas, para que Rostrum lo muestre al lado del consumo real.

    python3 scripts/consumo_pruebas.py            escribe plugins/criterio-server/scripts/consumo-pruebas.json
    python3 scripts/consumo_pruebas.py --check    falla si el archivo no es lo que sale de la evidencia

Sale de cada corrida publicada: `tests/evidencias/familias/<sigla>/ronda-N/<carpeta>/salidas/*.json`
y, en la PMO, `tests/evidencias/rondas/ronda-N/<industria>/salidas/*.json`. Cuenta solo la primera
corrida de cada comando, no las que se repitieron después de corregir un defecto (`repetidas/`).
Los tokens son los que informa Claude Code: entrada, escritura y lectura de caché, y salida.
"""
import argparse
import json
import statistics as st
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "plugins" / "criterio-server" / "scripts" / "consumo-pruebas.json"
REGISTRO = RAIZ / "plugins" / "criterio-server" / "scripts" / "agentes.json"


def corridas() -> list[tuple[str, dict]]:
    """(ronda, salida) de cada comando corrido en una ronda publicada; la salida lleva su carpeta."""
    ev = RAIZ / "tests" / "evidencias"
    rutas = sorted(ev.glob("familias/*/ronda-*/*/salidas/*.json")) + sorted(ev.glob("rondas/ronda-*/*/salidas/*.json"))
    return [(p.parent.parent.parent.name, {**json.loads(p.read_text(encoding="utf-8")), "_carpeta": p.parent.parent.name})
            for p in rutas]


def _material(familia: str, carpeta: str) -> str:
    """La entidad del material de una carpeta: `bc-mx-eficiencia` es una corrida más sobre `bc-mx`."""
    m = RAIZ / "tests" / f"criterio-{familia}" / "material"
    ents = [d.name for d in m.iterdir() if d.is_dir()] if m.is_dir() else []
    return max((e for e in ents if carpeta == e or carpeta.startswith(e + "-")), key=len, default=carpeta)


def indicador(familia: str, entradas: list) -> dict | None:
    """El indicador de eficiencia de un agente (decisión 0032): su última pasada —la corrida más reciente
    con más comandos—, en tokens, costo y segundos, con el modelo de la sesión, que es el del setup; lo
    que costó su reloj si ese día no le tocaba nada (dos o tres pasos: el camino corto); y el cambio
    contra la pasada anterior sobre la misma entidad y con el mismo modelo de sesión, en los comandos
    que corrieron en las dos."""
    if not entradas:
        return None
    def num(r):
        return int(r.split("-")[1])
    def sesion(cs):
        setup = next((v for c, v in cs.items() if c.endswith("-setup")), None)
        modelos = [v["modelo"] for v in cs.values() if v.get("modelo")]
        return (setup or {}).get("modelo") or (max(set(modelos), key=modelos.count) if modelos else None)
    ult = max(entradas, key=lambda e: (num(e["ronda"]), len(e["comandos"])))
    cs = ult["comandos"]
    def suma(d, k):
        v = [x.get(k) for x in d.values() if x.get(k) is not None]
        return round(sum(v), 4) if v else None   # la PMO no guarda el costo de sus corridas
    out = {"ronda": ult["ronda"], "carpeta": ult["carpeta"], "material": _material(familia, ult["carpeta"]),
           "modelo_sesion": sesion(cs), "comandos": len(cs),
           "tokens": suma(cs, "tokens"), "costo_usd": suma(cs, "costo_usd"), "segundos": suma(cs, "segundos")}
    reloj = next(((c, v) for c, v in cs.items() if c.endswith("-wake") and v["turnos"] <= 3), None)
    out["sin_pendientes"] = {"comando": reloj[0], "tokens": reloj[1]["tokens"], "segundos": reloj[1]["segundos"]} if reloj else None
    previas = [e for e in entradas if num(e["ronda"]) < num(ult["ronda"]) and _material(familia, e["carpeta"]) == out["material"]
               and sesion(e["comandos"]) == out["modelo_sesion"]]
    out["contra"] = None
    if previas:
        ant = max(previas, key=lambda e: (num(e["ronda"]), len(e["comandos"])))
        comunes = sorted(set(ant["comandos"]) & set(cs))
        a_ = {c: ant["comandos"][c] for c in comunes}
        b_ = {c: cs[c] for c in comunes}
        out["contra"] = {"ronda": ant["ronda"], "comandos": len(comunes),
                         "tokens": [suma(a_, "tokens"), suma(b_, "tokens")],
                         "costo_usd": [suma(a_, "costo_usd"), suma(b_, "costo_usd")],
                         "segundos": [suma(a_, "segundos"), suma(b_, "segundos")]}
    return out


def _med(v: list) -> float | None:
    v = [x for x in v if x is not None]
    return round(st.median(v), 4) if v else None


def resumen() -> dict:
    agentes = {a["id"]: a for a in json.loads(REGISTRO.read_text(encoding="utf-8"))["agentes"]}
    por, extra, rondas = {}, {}, {}
    for ronda, x in corridas():
        a, c, t = x.get("agente"), x.get("comando"), x.get("tokens")
        if a not in agentes or not c or not t:
            continue
        por.setdefault(a, {}).setdefault(c, []).append((t, x.get("tokens_salida") or 0, x.get("turnos") or 0))
        extra.setdefault(a, {}).setdefault(c, []).append((x.get("segundos"), x.get("costo_usd"), x.get("modelo")))
        # La evolución: por ronda y por carpeta, lo de cada comando, para ver qué cambió de una versión a otra.
        rondas.setdefault(a, {}).setdefault((ronda, x["_carpeta"]), {})[c] = {
            "tokens": t, "turnos": x.get("turnos") or 0, "segundos": x.get("segundos"), "costo_usd": x.get("costo_usd"),
            "modelo": x.get("modelo")}
    salida = {"nota": "Generado por scripts/consumo_pruebas.py desde las corridas publicadas en tests/evidencias; no se edita a mano.",
              "agentes": {}}
    for a in sorted(por, key=lambda k: (agentes[k]["familia"], k)):
        cmds = {}
        for c, v in sorted(por[a].items()):
            ex = extra[a][c]
            cmds[c] = {"corridas": len(v), "mediana": round(st.median(t for t, _, _ in v)),
                       "maximo": max(t for t, _, _ in v), "mediana_salida": round(st.median(s for _, s, _ in v)),
                       "mediana_turnos": round(st.median(n for _, _, n in v)),
                       "mediana_segundos": _med([s for s, _, _ in ex]), "mediana_costo_usd": _med([u for _, u, _ in ex]),
                       "modelo": ex[-1][2]}
        evol = [{"ronda": r_, "carpeta": ca, "comandos": dict(sorted(cs.items()))}
                for (r_, ca), cs in sorted(rondas[a].items(), key=lambda kv: (int(kv[0][0].split("-")[1]), kv[0][1]))]
        fam = agentes[a]["familia"]
        salida["agentes"][a] = {"familia": fam, "comandos": cmds, "pasada": sum(x["mediana"] for x in cmds.values()),
                                "indicador": indicador(fam, evol)}
    return salida


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    texto = json.dumps(resumen(), ensure_ascii=False, indent=1) + "\n"
    if ap.parse_args().check:
        if not SALIDA.is_file() or SALIDA.read_text(encoding="utf-8") != texto:
            print(f"{SALIDA.relative_to(RAIZ)} no es lo que sale de la evidencia: corre scripts/consumo_pruebas.py")
            return 1
        print("el consumo de las pruebas coincide con la evidencia")
        return 0
    SALIDA.write_text(texto, encoding="utf-8")
    d = json.loads(texto)["agentes"]
    print(f"{SALIDA.relative_to(RAIZ)} · {len(d)} agentes · {sum(len(x['comandos']) for x in d.values())} comandos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
