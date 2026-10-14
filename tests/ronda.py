#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Una ronda de pruebas: los tres agentes, sus 37 comandos, en orden, en una industria.

    python3 tests/ronda.py armar <entorno> <carpeta> --ronda 1
    python3 tests/ronda.py correr <carpeta>            # necesita `claude` (Claude Code)
    python3 tests/ronda.py revisar <carpeta>           # contratos, sin modelo
    python3 tests/ronda.py calificar <carpeta> --version 0.3.6 --tipo primera
    python3 tests/ronda.py defecto ...                 # registra un defecto y su corrección
    python3 tests/ronda.py verificar                   # puerta

**La regla.** Una corrida es una industria completa: los 37 comandos uno tras otro, sobre
la misma carpeta, sin saltarse ninguno. Si uno falla, la corrida sigue y el fallo queda
escrito; la corrida cuenta como completa solo si terminaron los 37. Cada ronda sortea
hechos nuevos (`--ronda`), así que la versión que se prueba no los ha visto.

**El orden es el del trabajo real.** Alba define el producto; Samuel ejecuta un proyecto
y publica su ficha; Vera mira el portafolio entero y levanta el servidor; y al final
Alba cruza su producto con lo que los proyectos dicen.

**Qué queda de cada comando**, en `<carpeta>/salidas/`: lo que imprimió, cuánto tardó,
cuántos tokens usó y qué archivos cambió. Con eso `revisar` comprueba el contrato de cada
comando —escribió lo que debe y nada más, y cada cita de una ficha apunta a un documento
que existe— y `calificar` mide contra la clave lo que tiene clave.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
sys.path.insert(0, str(RAIZ / "tests"))
import fiabilidad  # noqa: E402

PLUGIN = {"vera": "criterio-portfolio", "samuel": "criterio-project", "alba": "criterio-product"}
DEFECTOS = RAIZ / "tests" / "evidencias" / "defectos.json"
NOTA = ("(Sesión de prueba sin interfaz: nadie va a responder preguntas. Términos: José Francisco "
        "Ñáñez acepta TERMS.md para esta prueba, fecha {hoy}. En cada otra pregunta toma la "
        "respuesta sugerida, dila en una línea y sigue. Si un comando pide algo que no existe, "
        "dilo y termina; no lo inventes.)")


# ── los 37, en orden ──────────────────────────────────────────────────────
# (agente, comando, argumento). El argumento se arma con los objetivos que `armar` elige
# desde la clave: {prd} producto de Alba, {prd_otro} el segundo, {req} un requerimiento
# aceptado, {pry_sam} el proyecto de Samuel, {notas} sus notas crudas, y uno por comando
# de Vera.
ORDEN = [
    ("alba", "product-setup", "documentos/productos/{prd_carpeta}"),
    ("alba", "product-discovery", ""),
    ("alba", "product-requirements", ""),
    ("alba", "product-definition", ""),
    ("alba", "product-business-case", ""),
    ("alba", "product-spec", ""),
    ("alba", "product-charter", "{req}"),
    ("alba", "product-publish", ""),
    ("samuel", "pm-setup", "documentos/proyectos/{sam_carpeta}"),
    ("samuel", "pm-minutes", "{notas}"),
    ("samuel", "pm-commitments", ""),
    ("samuel", "pm-agenda", ""),
    ("samuel", "pm-report", ""),
    ("samuel", "pm-plan", ""),
    ("samuel", "pm-escalate", ""),
    ("samuel", "pm-publish", "confirmar"),
    ("samuel", "pm-wake", ""),
    ("vera", "portfolio-setup", "documentos/proyectos"),
    ("vera", "portfolio-scan", ""),
    ("vera", "document-index", ""),
    ("vera", "status-report", "{status}"),
    ("vera", "health-check", "{health}"),
    ("vera", "budget-tracking", "{budget}"),
    ("vera", "vendor-tracking", "{vendor}"),
    ("vera", "change-control", "{change} mover la salida a producción 30 días"),
    ("vera", "project-history", "{history}"),
    ("vera", "raid-log", "portafolio"),
    ("vera", "project-charter", "{charter} revisar"),
    ("vera", "project-closure", "{closure}"),
    ("vera", "steering-pack", ""),
    ("vera", "product-view", "{producto_vista}"),
    ("vera", "portfolio-report", "html"),
    ("vera", "portfolio-wake", ""),
    ("vera", "portfolio-server", "rato"),
    ("alba", "product-trace", ""),
    ("alba", "product-overlap", "{prd_otro}"),
    ("alba", "product-wake", ""),
]


def _j(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def _w(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ── armar ─────────────────────────────────────────────────────────────────

def armar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    r = subprocess.run([sys.executable, str(RAIZ / "tests" / "banco.py"), "armar", a.entorno,
                        str(carpeta), "--ronda", str(a.ronda), "--semanas", str(a.semanas),
                        "--disposicion", "referencia", "--proyectos", str(a.proyectos),
                        "--productos", str(a.productos)], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    clave, docs = carpeta / "clave", carpeta / "espacio" / "documentos"
    org, esp = _j(clave / "organizacion.json"), _j(clave / "esperado.json")
    hoy = dt.date.fromisoformat(esp["hoy"])
    controles = set(esp.get("controles", []))
    pry = [p for p in org["proyectos"] if p["codigo"] not in controles]
    prd = [x for x in org["productos"] if x["codigo"] not in controles]
    senales = {k: [s["signal"] if isinstance(s, dict) else s for s in v] for k, v in esp["esperado"].items()}

    def con(s, excluir=()):
        cands = [p for p in pry if s in senales.get(p["codigo"], []) and p["codigo"] not in excluir]
        return max(cands, key=lambda p: len(senales.get(p["codigo"], [])), default=None)

    sam = max(pry, key=lambda p: (len(p["compromisos"]), sum(len(c["fechas"]) for c in p["compromisos"]),
                                  len(senales.get(p["codigo"], []))))
    alba = max(prd, key=lambda x: len(senales.get(x["codigo"], [])))
    otro = max((x for x in prd if x["codigo"] != alba["codigo"]),
               key=lambda x: len(senales.get(x["codigo"], [])))
    status = con("silent") or con("milestone_overdue") or con("declared_vs_evidence") or pry[0]
    health = (con("progress_vs_plan", {status["codigo"]}) or
              con("milestone_met_without_evidence", {status["codigo"]}) or pry[1])
    vendor = next((p for p in pry if any(s.startswith("vendor_") for s in senales.get(p["codigo"], []))), None)
    budget = con("budget_committed") or con("variance_cost")
    historia = max(pry, key=lambda p: (p["lineas_base"], len(p["cambios"]), len(p["hitos"])))
    cambio = max(pry, key=lambda p: (len(p["hitos"]), p["codigo"] != sam["codigo"]))
    cierre = max(pry, key=lambda p: sum(1 for h in p["hitos"] if h["cerrado"]) / max(len(p["hitos"]), 1))
    acta = min(pry, key=lambda p: len(senales.get(p["codigo"], [])))
    vista = max({p["producto"] for p in pry if p.get("producto")} or {""},
                key=lambda n: sum(1 for p in pry if p.get("producto") == n))
    reqs = [r for r in alba["requerimientos"] if r["estado"] in ("aceptado", "en_construccion")]

    notas, efecto = escribir_notas(docs / "proyectos" / sam["carpeta"], sam, hoy)
    esp_ronda = dict(esp)
    esp_ronda["esperado"] = {k: list(v) for k, v in senales.items()}
    fila = esp_ronda["esperado"].setdefault(sam["codigo"], [])
    for s in efecto["agrega"]:
        fila.append(s)
    for s in efecto["quita"]:
        if s in fila:
            fila.remove(s)
    _w(clave / "esperado-ronda.json", esp_ronda)
    obj = {
        "entorno": org.get("sector"), "ronda": a.ronda, "hoy": esp["hoy"],
        "prd": alba["codigo"], "prd_carpeta": alba["carpeta"], "prd_otro": otro["codigo"],
        "req": reqs[0]["id"] if reqs else "", "pry_sam": sam["codigo"], "sam_carpeta": sam["carpeta"],
        "notas": str(notas.relative_to(carpeta / "espacio")),
        "status": status["codigo"], "health": health["codigo"],
        "budget": budget["codigo"] if budget else "portafolio",
        "vendor": vendor["codigo"] if vendor else status["codigo"],
        "change": cambio["codigo"], "history": historia["codigo"], "charter": acta["codigo"],
        "closure": cierre["codigo"], "producto_vista": vista,
    }
    _w(clave / "objetivos.json", obj)
    print(f"{org.get('sector')} · ronda {a.ronda} · corte {esp['hoy']}")
    for k, v in obj.items():
        print(f"  {k:15} {v}")
    print(f"  notas de Samuel: {efecto['resumen']}")
    return 0


def escribir_notas(carpeta: Path, p: dict, hoy: dt.date) -> tuple:
    """Las notas crudas de la última reunión del proyecto de Samuel, como las toma alguien
    en el cuaderno: sin tabla, con las fechas dichas como se dicen. Tres compromisos con
    respuesta conocida y un riesgo dicho que nadie registra."""
    abiertos = [c for c in p["compromisos"] if not c.get("cumplido")]
    c1 = max(abiertos, key=lambda c: len(c["fechas"]), default=None)
    fecha = hoy - dt.timedelta(days=1)
    nueva = hoy + dt.timedelta(days=14)
    asistentes = sorted({p["gerente"], *(c["quien"] for c in p["compromisos"])})
    otro, tercero = "Laura Vélez", "Óscar Ramírez"
    lineas = [f"notas reunión {p['nombre'].lower()} — {fecha.isoformat()}",
              f"estuvieron: {', '.join(asistentes + [otro, tercero])}", ""]
    clave, agrega, quita = [], [], []
    if c1:
        lineas.append(f"- {c1['quien']} dice que lo de «{c1['que'].lower()}» no alcanzó, "
                      f"se compromete para el {nueva.strftime('%d/%m/%Y')}")
        repro = len(c1["fechas"])            # con la nueva, tantas reprogramaciones como fechas tenía
        clave.append({"quien": c1["quien"], "que": c1["que"], "fecha": nueva.isoformat(),
                      "reprogramaciones": repro})
        if dt.date.fromisoformat(c1["fechas"][-1]) < hoy:
            quita.append("commitment_overdue")
        if repro >= 3 > repro - 1:
            agrega.append("commitment_rescheduled")
    lineas.append(f"- {otro} queda de mandar el ajuste del presupuesto la otra semana")
    clave.append({"quien": otro, "que": "ajuste del presupuesto", "fecha": "no_declarada", "reprogramaciones": 0})
    agrega.append("commitment_undated")
    f3 = hoy + dt.timedelta(days=10)
    lineas.append(f"- {tercero}: revisión con el proveedor, queda para el {f3.isoformat()}")
    clave.append({"quien": tercero, "que": "revisión con el proveedor", "fecha": f3.isoformat(), "reprogramaciones": 0})
    lineas += ["- se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase,"
               " nadie lo anotó como riesgo", "- próxima reunión en dos semanas", ""]
    ruta = carpeta / f"{fecha.isoformat()}-notas-reunion.txt"
    ruta.write_text("\n".join(lineas), encoding="utf-8")
    _w(carpeta.parents[2] / "clave" / "notas.json", {"proyecto": p["codigo"], "compromisos": clave,
                                                     "riesgo": "el proveedor podría no llegar con el equipo completo"})
    return ruta, {"agrega": agrega, "quita": quita,
                  "resumen": f"{len(clave)} compromisos; clave {agrega} / sin {quita}"}


# ── correr ────────────────────────────────────────────────────────────────

def manifiesto(raiz: Path) -> dict:
    out = {}
    for f in raiz.rglob("*"):
        if f.is_file() and ".claude" not in f.parts and ".git" not in f.parts:
            out[str(f.relative_to(raiz))] = hashlib.sha1(f.read_bytes()).hexdigest()[:12]
    return out


def instalar(espacio: Path) -> None:
    if (espacio / ".claude" / "settings.json").is_file():
        return
    subprocess.run(["git", "init", "-q"], cwd=espacio)
    for p in PLUGIN.values():
        subprocess.run(["claude", "plugin", "install", f"{p}@criterio", "--scope", "project"],
                       cwd=espacio, capture_output=True)


def correr(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio, sal = carpeta / "espacio", carpeta / "salidas"
    obj = _j(carpeta / "clave" / "objetivos.json")
    sal.mkdir(exist_ok=True)
    instalar(espacio)
    for n, (agente, cmd, arg) in enumerate(ORDEN, start=1):
        base = sal / f"{n:02d}-{cmd}"
        if base.with_suffix(".json").is_file() and not a.repetir:
            continue
        if a.solo and n not in a.solo:
            continue
        antes = manifiesto(espacio)
        prompt = f"/{PLUGIN[agente]}:{cmd} {arg.format(**obj)}".strip() + "\n\n" + NOTA.format(hoy=obj["hoy"])
        t0 = time.time()
        try:
            r = subprocess.run(["claude", "-p", prompt, "--permission-mode", "bypassPermissions",
                                "--output-format", "json"], cwd=espacio, capture_output=True,
                               text=True, timeout=a.limite)
            salida = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"subtype": "error", "result": r.stdout + r.stderr}
        except subprocess.TimeoutExpired:
            salida = {"subtype": "timeout", "result": f"no terminó en {a.limite} s"}
        despues = manifiesto(espacio)
        u = salida.get("usage") or {}
        fila = {"n": n, "agente": agente, "comando": cmd, "argumento": arg.format(**obj),
                "estado": salida.get("subtype"), "error": bool(salida.get("is_error")) or salida.get("subtype") != "success",
                "segundos": round(time.time() - t0), "turnos": salida.get("num_turns"),
                "tokens": sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens",
                                                       "cache_read_input_tokens", "output_tokens")),
                "tokens_salida": u.get("output_tokens"),
                "modelo": next(iter(salida.get("modelUsage") or {}), None),
                "cambios": {"nuevos": sorted(set(despues) - set(antes)),
                            "modificados": sorted(k for k in set(antes) & set(despues) if antes[k] != despues[k]),
                            "borrados": sorted(set(antes) - set(despues))}}
        if cmd == "portfolio-server":
            fila["servidor"] = probar_servidor(espacio)
        _w(base.with_suffix(".json"), fila)
        base.with_suffix(".md").write_text(f"# /{PLUGIN[agente]}:{cmd} {fila['argumento']}\n\n"
                                           + (salida.get("result") or ""), encoding="utf-8")
        print(f"{n:02d} {cmd:22} {fila['estado']:8} {fila['segundos']:4d} s {fila['tokens'] // 1000:6d} k "
              f"+{len(fila['cambios']['nuevos'])} ~{len(fila['cambios']['modificados'])}", flush=True)
    return 0


def probar_servidor(espacio: Path) -> dict:
    """Rostrum lo levanta este script, no el agente: un servidor en primer plano dentro de
    una sesión sin interfaz no termina. Se comprueba que responda y que no escriba fichas."""
    cfg = _j(espacio / ".criterio" / "portafolio" / "config.json")
    estado = espacio / cfg["paths"]["state"]
    informe = espacio / cfg["paths"].get("reports", "reportes")
    script = next(Path.home().glob(".claude/plugins/**/criterio-portfolio/scripts/servidor.py"), None) \
        or RAIZ / "plugins" / "criterio-portfolio" / "scripts" / "servidor.py"
    antes = manifiesto(estado / "records") if (estado / "records").is_dir() else {}
    p = subprocess.Popen([sys.executable, str(script), "--informe", str(informe), "--estado", str(estado),
                          "--config", str(espacio / ".criterio" / "portafolio" / "config.json"),
                          "--puerto", "8799"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    rutas = {}
    try:
        time.sleep(3)
        for ruta in ("/", "/pmo", "/decisiones", "/proyectos", "/productos", "/corridas", "/estado.json"):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:8799{ruta}", timeout=10) as resp:
                    rutas[ruta] = resp.status
            except Exception as e:  # noqa: BLE001
                rutas[ruta] = str(getattr(e, "code", e))[:60]
    finally:
        p.terminate()
    despues = manifiesto(estado / "records") if (estado / "records").is_dir() else {}
    return {"rutas": rutas, "fichas_intactas": antes == despues}


# ── revisar: los contratos ────────────────────────────────────────────────

SIEMPRE = ("corridas", "corrida-en-curso", "cache", ".criterio/corridas", "salida-")


def permitido(cambio: str, escribe: list, cmd: str) -> bool:
    if any(s in cambio for s in SIEMPRE):
        return True
    reglas = " ".join(escribe)
    if cambio.startswith("documentos/"):
        return ("ficha-pm.json" in reglas and cambio.endswith("ficha-pm.json")) or \
               ("30-reuniones" in reglas and "acta" in cambio) or \
               ("<publicados>" in reglas and "public" in cambio)
    if cambio.startswith(".criterio/") and cambio.endswith("config.json"):
        return "config.json" in reglas
    for marca, clave in (("/records/", "records"), ("/snapshots/", "snapshots"), ("cadencia", "cadencia"),
                         ("/requirements/", "requirements"), ("producto.json", "producto.json"),
                         ("reportes/", "<informes>"), ("publicados", "<publicados>")):
        if marca in cambio:
            return clave in reglas or "(init)" in reglas
    return "(init)" in reglas


def citas_rotas(espacio: Path, ficha: Path) -> list:
    docs = espacio / "documentos"
    rotas = []
    def recorrer(n):
        if isinstance(n, dict):
            s = n.get("source")
            if isinstance(s, str) and s and not s.startswith(("http", "script", "compute")):
                if not any((d / s).exists() for d in (docs, docs / "proyectos", docs / "productos", espacio)):
                    rotas.append(s)
            for v in n.values():
                recorrer(v)
        elif isinstance(n, list):
            for v in n:
                recorrer(v)
    try:
        recorrer(_j(ficha))
    except (OSError, json.JSONDecodeError):
        pass
    return rotas


def revisar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio, sal = carpeta / "espacio", carpeta / "salidas"
    contratos = {}
    for p in PLUGIN.values():
        contratos.update(_j(RAIZ / "plugins" / p / "contratos.json")["comandos"])
    filas = []
    for f in sorted(sal.glob("[0-9][0-9]-*.json")):
        r = _j(f)
        escribe = (contratos.get(r["comando"], {}).get("salida") or {}).get("escribe") or []
        cambios = r["cambios"]["nuevos"] + r["cambios"]["modificados"]
        fuera = [c for c in cambios if not permitido(c, escribe, r["comando"])]
        borro_docs = [c for c in r["cambios"]["borrados"] if c.startswith("documentos/")]
        fichas = [espacio / c for c in cambios if "/records/" in c and c.endswith(".json")]
        rotas = sorted({x for fi in fichas for x in citas_rotas(espacio, fi)})
        problemas = []
        if r["error"]:
            problemas.append(f"no terminó ({r['estado']})")
        if fuera:
            problemas.append(f"escribió fuera de su contrato: {fuera[:4]}")
        if borro_docs:
            problemas.append(f"borró documentos: {borro_docs[:4]}")
        if rotas:
            problemas.append(f"{len(rotas)} citas a documentos que no existen: {rotas[:3]}")
        if r.get("servidor"):
            malas = {k: v for k, v in r["servidor"]["rutas"].items() if v != 200}
            if malas:
                problemas.append(f"rutas de Rostrum que no responden: {malas}")
            if not r["servidor"]["fichas_intactas"]:
                problemas.append("Rostrum modificó fichas")
        filas.append({"n": r["n"], "agente": r["agente"], "comando": r["comando"], "termino": not r["error"],
                      "contrato": not problemas, "problemas": problemas, "segundos": r["segundos"],
                      "tokens": r["tokens"]})
    completos = sum(1 for x in filas if x["termino"])
    cumplen = sum(1 for x in filas if x["contrato"])
    resumen = {"comandos": len(ORDEN), "corridos": len(filas), "completos": completos,
               "contratos_cumplidos": cumplen, "corrida_completa": completos == len(ORDEN),
               "segundos": sum(x["segundos"] for x in filas), "tokens": sum(x["tokens"] for x in filas),
               "filas": filas}
    _w(carpeta / "revision.json", resumen)
    for x in filas:
        print(f"{x['n']:02d} {x['comando']:22} {'terminó' if x['termino'] else 'FALLÓ  '} "
              f"{'contrato ok' if x['contrato'] else 'CONTRATO'} {'; '.join(x['problemas'])[:150]}")
    print(f"\n{completos}/{len(ORDEN)} terminaron · {cumplen}/{len(ORDEN)} cumplen su contrato · "
          f"{resumen['segundos'] // 60} min · {resumen['tokens'] / 1e6:.1f} M tokens")
    return 0


# ── calificar: lo que tiene clave ─────────────────────────────────────────

def calificar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio = carpeta / "espacio"
    obj = _j(carpeta / "clave" / "objetivos.json")
    clave = _j(carpeta / "clave" / "esperado-ronda.json")
    hoy = clave["hoy"]
    base = ["--version", a.version, "--tipo", a.tipo, "--nota", f"ronda {obj['ronda']}"]
    # Vera: las señales del portafolio, contra la clave de la ronda (con lo que agregan las notas)
    subprocess.run([sys.executable, str(RAIZ / "tests" / "banco.py"), "calificar", str(carpeta),
                    "--agente", "vera", "--material", f"ronda-{obj['ronda']}", *base], check=False)
    # Samuel: los compromisos de las notas crudas
    notas = _j(carpeta / "clave" / "notas.json")
    fichas = list((espacio).glob(f"**/records/{obj['pry_sam']}.json"))
    sam = next((f for f in fichas if "/estado/records/" not in str(f)), fichas[0] if fichas else None)
    comps = (_j(sam).get("commitments") or []) if sam else []
    v = lambda x: (x.get("value") if isinstance(x, dict) else x) or ""
    correctos, detalle = 0, []
    for c in notas["compromisos"]:
        m = next((x for x in comps if v(x.get("who")).split()[0] == c["quien"].split()[0]
                  and c["que"].split()[0].lower() in v(x.get("what")).lower()), None)
        ok = bool(m) and (v(m.get("due_date")) == c["fecha"] or (c["fecha"] == "no_declarada" and v(m.get("due_date")) in ("", "no_declarada"))) \
            and len(m.get("reschedules") or []) == c["reprogramaciones"]
        correctos += ok
        detalle.append({"quien": c["quien"], "esperado": c, "ok": ok,
                        "encontrado": {"fecha": v(m.get("due_date")), "reprogramaciones": len(m.get("reschedules") or [])} if m else None})
    # Alba: las señales de su producto
    estado_prd = next((d for d in espacio.glob(f"**/{obj['prd']}")
                       if d.is_dir() and "documentos" not in d.relative_to(espacio).parts), None)
    prd_obt = {}
    if estado_prd and estado_prd.is_dir():
        obt, _, err = fiabilidad.hallazgos_producto(estado_prd.parent, espacio / "estado" / "records", hoy)
        prd_obt = {obj["prd"]: obt.get(obj["prd"], [])}
    cal = fiabilidad.calificar({obj["prd"]: clave["esperado"].get(obj["prd"], [])}, prd_obt)
    t = fiabilidad.totales(cal)
    salida = {"samuel": {"compromisos": len(notas["compromisos"]), "correctos": correctos, "detalle": detalle},
              "alba": {"producto": obj["prd"], **t, "errores": cal["por_caso"]}}
    _w(carpeta / "calificacion-samuel-alba.json", salida)
    print(f"Samuel · compromisos de las notas: {correctos} de {len(notas['compromisos'])}")
    for d in detalle:
        print(f"   {'OK' if d['ok'] else '  '} {d['quien']}: esperado {d['esperado']['fecha']} "
              f"({d['esperado']['reprogramaciones']}) · encontrado {d['encontrado']}")
    print(f"Alba · {obj['prd']}: {t}")
    return 0


# ── defectos ──────────────────────────────────────────────────────────────

ORIGENES = ("agente", "codigo", "material", "clave", "instrucciones")


def defecto(a) -> int:
    filas = _j(DEFECTOS) if DEFECTOS.is_file() else []
    if a.cerrar:
        f = next((x for x in filas if x["id"] == a.cerrar), None)
        if not f:
            sys.exit(f"no hay defecto {a.cerrar}")
        f["correccion"] = a.commit or f.get("correccion")
        f["verificado_en"] = a.verificado or f.get("verificado_en")
    else:
        filas.append({"id": f"D{len(filas) + 1:03d}", "fecha": dt.date.today().isoformat(),
                      "ronda": a.ronda, "entorno": a.entorno, "agente": a.agente, "comando": a.comando,
                      "que_paso": a.que, "evidencia": a.evidencia, "origen": a.origen,
                      "correccion": a.commit, "verificado_en": a.verificado})
    _w(DEFECTOS, filas)
    return verificar(None)


def verificar(_a) -> int:
    filas = _j(DEFECTOS) if DEFECTOS.is_file() else []
    malas = []
    for f in filas:
        if f["origen"] not in ORIGENES:
            malas.append(f"{f['id']}: origen «{f['origen']}»")
        if f["verificado_en"] and not f["correccion"]:
            malas.append(f"{f['id']}: verificado sin corrección")
        if f.get("evidencia") and not (RAIZ / f["evidencia"]).exists():
            malas.append(f"{f['id']}: la evidencia {f['evidencia']} no está en el repositorio")
    for m in malas:
        print("  FALLA", m)
    abiertos = sum(1 for f in filas if not f["correccion"])
    sin_verificar = sum(1 for f in filas if f["correccion"] and not f["verificado_en"])
    if not malas:
        print(f"  OK    {len(filas)} defectos · {abiertos} abiertos · {sin_verificar} corregidos sin verificar")
    return 1 if malas else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="accion", required=True)
    s = sub.add_parser("armar")
    s.add_argument("entorno")
    s.add_argument("carpeta")
    s.add_argument("--ronda", type=int, required=True)
    s.add_argument("--semanas", type=int, default=3)
    s.add_argument("--proyectos", type=int, default=12)
    s.add_argument("--productos", type=int, default=10)
    s = sub.add_parser("correr")
    s.add_argument("carpeta")
    s.add_argument("--limite", type=int, default=900, help="segundos por comando")
    s.add_argument("--repetir", action="store_true")
    s.add_argument("--solo", type=int, nargs="*")
    s = sub.add_parser("revisar")
    s.add_argument("carpeta")
    s = sub.add_parser("calificar")
    s.add_argument("carpeta")
    s.add_argument("--version", required=True)
    s.add_argument("--tipo", required=True, choices=("primera", "corregida"))
    s = sub.add_parser("defecto")
    s.add_argument("--cerrar")
    for k in ("ronda", "entorno", "agente", "comando", "que", "evidencia", "origen", "commit", "verificado"):
        s.add_argument(f"--{k}")
    sub.add_parser("verificar")
    a = ap.parse_args()
    sys.exit({"armar": armar, "correr": correr, "revisar": revisar, "calificar": calificar,
              "defecto": defecto, "verificar": verificar}[a.accion](a))
