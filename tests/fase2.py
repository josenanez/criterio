#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 2: cada agente sobre un corpus pequeño con casos sembrados, un comando a la vez.

    python3 tests/fase2.py armar vera        arma .pruebas/vera-mini desde corp-demo
    python3 tests/fase2.py calificar vera    califica el estado de Vera contra la clave

El corpus grande (51 proyectos, 350 documentos) sirve para las cifras de venta y cuesta
25 minutos por barrido. Para depurar sirve uno pequeño: los proyectos de corp-demo que,
juntos, cubren cada señal de la clave, más el control negativo. Un comando que falla
aquí falla en dos minutos y se sabe en qué proyecto.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import fiabilidad  # noqa: E402

FUENTE = RAIZ / ".pruebas" / "corp-demo"
MINI = {"vera": RAIZ / ".pruebas" / "vera-mini", "samuel": RAIZ / ".pruebas" / "samuel-mini"}


def _senales(lista) -> list:
    return [x["signal"] if isinstance(x, dict) else x for x in lista]


def elegir(esperado: dict, controles: list) -> list:
    """Los proyectos que cubren todas las señales de la clave, de a uno, más los controles."""
    filas = {k: set(_senales(v)) for k, v in esperado.items() if k.startswith("PRY")}
    falta, elegidos = set().union(*filas.values()), []
    while falta:
        k = max(sorted(filas), key=lambda c: len(filas[c] & falta))
        if not filas[k] & falta:
            break
        elegidos.append(k)
        falta -= filas[k]
    return sorted(set(elegidos) | {c for c in controles if c.startswith("PRY")})


def armar_vera() -> None:
    clave = json.loads((FUENTE / "esperado.json").read_text(encoding="utf-8"))
    codigos = elegir(clave["esperado"], clave.get("controles", []))
    destino = MINI["vera"]
    docs = destino / "documentos" / "proyectos"
    if destino.exists():
        sys.exit(f"{destino} ya existe; no se reescribe una prueba en curso")
    docs.mkdir(parents=True)
    origen = FUENTE / "documentos" / "proyectos"
    for c in codigos:
        carpeta = next(d for d in origen.iterdir() if d.name.startswith(c + "-"))
        shutil.copytree(carpeta, docs / carpeta.name)
    (destino / "estado").mkdir()
    (destino / "reportes").mkdir()
    sub = {k: v for k, v in clave["esperado"].items() if k in codigos}
    (destino / "esperado.json").write_text(json.dumps(
        {"hoy": clave["hoy"], "controles": [c for c in clave.get("controles", []) if c in codigos],
         "esperado": sub, "de": "corp-demo"}, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(1 for _ in docs.rglob("*") if _.is_file())
    print(f"{len(codigos)} proyectos, {n} documentos: {', '.join(codigos)}")
    for c in codigos:
        print(f"  {c}: {', '.join(sorted(set(_senales(sub[c])))) or 'control: ninguna señal'}")


def calificar_vera() -> int:
    destino = MINI["vera"]
    clave = json.loads((destino / "esperado.json").read_text(encoding="utf-8"))
    esperado = {k: _senales(v) for k, v in clave["esperado"].items()}
    obtenido, _, error = fiabilidad.hallazgos_portafolio(destino / "estado", clave["hoy"])
    if error:
        print("no se pudo calcular:", error)
        return 1
    sys.path.insert(0, str(RAIZ / "plugins" / "criterio-portfolio" / "scripts"))
    import portafolio
    repo = portafolio.huella_plugin(RAIZ / "plugins" / "criterio-portfolio")
    try:
        ultima = json.loads((destino / "estado" / "corridas.json").read_text(encoding="utf-8"))[-1]
    except (OSError, json.JSONDecodeError, IndexError):
        ultima = {}
    corrio = ultima.get("plugin") or {}
    if corrio.get("huella") != repo["huella"]:
        print(f"PLUGIN VIEJO: la corrida {ultima.get('id')} usó {corrio or 'una versión sin huella'}; "
              f"el repositorio es {repo}. Actualiza y reinstala antes de calificar.")
    else:
        print(f"plugin al día: {repo}")
    con_ficha = {f.stem for f in (destino / "estado" / "records").glob("*.json")}
    print(f"fichas escritas: {len(con_ficha)} de {len(esperado)} ({', '.join(sorted(con_ficha)) or 'ninguna'})")
    if 0 < len(con_ficha) < len(esperado):
        # un setup lee tres: se califica sobre lo que leyó, y aparte sobre el total
        parcial = fiabilidad.totales(fiabilidad.calificar(
            {k: v for k, v in esperado.items() if k in con_ficha},
            {k: v for k, v in obtenido.items() if k in con_ficha}))
        print("sobre lo leído:", json.dumps(parcial, ensure_ascii=False))
    cal = fiabilidad.calificar(esperado, obtenido)
    t = fiabilidad.totales(cal)
    print(json.dumps(t, ensure_ascii=False))
    for caso, r in sorted(cal["por_caso"].items()):
        marca = "OK" if not r["falsos_negativos"] and not r["falsos_positivos"] else "  "
        print(f"{marca} {caso}: {r['aciertos']}/{r['esperado']}"
              + (f"  faltan {r['falsos_negativos']}" if r["falsos_negativos"] else "")
              + (f"  sobran {r['falsos_positivos']}" if r["falsos_positivos"] else ""))
    return 0


# Samuel: un proyecto, PRY-200, con las notas de la reunión del 30 de septiembre sembradas
# a mano. La clave de los compromisos sale de esas notas; la de las señales, de la clave
# de corp-demo para PRY-200 más lo que las notas agregan.
SAMUEL_CLAVE = {
    "hoy": "2026-09-30",
    "senales": ["declared_vs_evidence", "variance_cost", "commitment_undated", "commitment_undated"],
    "compromisos": {
        "total": 4,
        "reprogramado": {"quien": "Paola", "fecha": "2026-10-15", "veces": 2},
        "sin_fecha": ["Andrés", "Óscar"],      # «la semana que viene» y «esta semana» no son fechas
        "con_fecha": {"Óscar": "2026-10-12"},
    },
}


def armar_samuel() -> None:
    destino = MINI["samuel"]
    if destino.exists():
        sys.exit(f"{destino} ya existe; no se reescribe una prueba en curso")
    origen = next((FUENTE / "documentos" / "proyectos").glob("PRY-200-*"))
    docs = destino / "documentos" / "proyectos"
    docs.mkdir(parents=True)
    shutil.copytree(origen, docs / origen.name, ignore=shutil.ignore_patterns("*acta-seguimiento*"))
    (destino / "estado").mkdir()
    (destino / "esperado.json").write_text(json.dumps(SAMUEL_CLAVE, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(1 for _ in docs.rglob("*") if _.is_file())
    print(f"PRY-200, {n} documentos en {docs / origen.name}")


def calificar_samuel() -> int:
    destino = MINI["samuel"]
    clave = json.loads((destino / "esperado.json").read_text(encoding="utf-8"))
    cfg = RAIZ / ".criterio" / "proyecto" / "PRY-200" / "config.json"
    estado = RAIZ / json.loads(cfg.read_text(encoding="utf-8"))["paths"]["state"] if cfg.is_file() else destino / "estado"
    print(f"configuración: {'en su sitio' if cfg.is_file() else 'NO ESTÁ en ' + str(cfg.relative_to(RAIZ))}; estado: {estado.relative_to(RAIZ)}")
    fichas = sorted((estado / "records").glob("*.json"))
    if not fichas:
        print("no hay ficha: nada que calificar")
        return 1
    rec = json.loads(fichas[0].read_text(encoding="utf-8"))
    obtenido, _, error = fiabilidad.hallazgos_portafolio(estado, clave["hoy"])
    if error:
        print("no se pudo calcular:", error)
        return 1
    cal = fiabilidad.calificar({"PRY-200": clave["senales"]}, obtenido)
    print("señales:", json.dumps(fiabilidad.totales(cal), ensure_ascii=False), cal["por_caso"].get("PRY-200"))
    cs = rec.get("commitments") or []
    k = clave["compromisos"]
    def due(c):
        v = c.get("due_date"); return (v.get("value") if isinstance(v, dict) else v) or ""
    def quien(c):
        v = c.get("who"); return (v.get("value") if isinstance(v, dict) else v) or ""
    filas = [
        ("compromisos", len(cs), k["total"]),
        ("ninguna fecha inferida (sin «~» ni fechas inventadas)",
         [quien(c) for c in cs if "~" in due(c)], []),
        ("sin fecha", sorted(q.split()[0] for q in (quien(c) for c in cs if due(c) in ("", "no_declarada"))),
         sorted(k["sin_fecha"])),
        ("Paola: uno solo, con su historial",
         [(due(c), len(c.get("reschedules") or [])) for c in cs if quien(c).startswith(k["reprogramado"]["quien"])],
         [(k["reprogramado"]["fecha"], k["reprogramado"]["veces"])]),
    ]
    for nombre, real, esperado in filas:
        print(f"{'OK' if real == esperado else '  '} {nombre}: {real}" + ("" if real == esperado else f"  esperado {esperado}"))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in MINI or sys.argv[1] not in ("armar", "calificar"):
        sys.exit(__doc__)
    sys.exit({"armar": {"vera": armar_vera, "samuel": armar_samuel},
              "calificar": {"vera": calificar_vera, "samuel": calificar_samuel}}[sys.argv[1]][sys.argv[2]]() or 0)
