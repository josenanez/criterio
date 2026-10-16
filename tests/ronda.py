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
import os
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
        "Ñáñez acepta los términos vigentes de esta versión para esta prueba, fecha {hoy}; cuando el "
        "agente los muestre, regístralo con ese nombre. En cada otra pregunta toma la "
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

    fechado = lambda p: any(not c.get("cumplido") and c["fechas"] and all(isinstance(x, str) and x[:4].isdigit()
                                                                          for x in c["fechas"]) for c in p["compromisos"])
    sam = max(pry, key=lambda p: (fechado(p), len(p["compromisos"]), sum(len(c["fechas"]) for c in p["compromisos"]),
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

    # Samuel: seis comités de historia y las notas de hoy. La clave de Vera para ese
    # proyecto se recalcula con las mismas reglas del simulador sobre los compromisos que
    # quedaron escritos, para que los dos agentes se califiquen contra el mismo material.
    sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
    import simulador
    car_sam = docs / "proyectos" / sam["carpeta"]
    comps = historia_samuel(car_sam, sam, hoy, simulador.NOMBRES, f"{a.entorno}-{a.ronda}-samuel")
    notas = escribir_notas(car_sam, sam, comps, hoy)
    _w(clave / "notas.json", {"proyecto": sam["codigo"], "compromisos": clave_samuel(comps),
                              "riesgo": "el proveedor podría no llegar con el equipo completo"})
    sam_mod = dict(sam, compromisos=comps, ultimo_escrito=hoy.isoformat())
    esp_ronda = dict(esp)
    esp_ronda["esperado"] = {k: list(v) for k, v in senales.items()}
    esp_ronda["esperado"][sam["codigo"]] = simulador.esperado_proyecto(sam_mod, hoy)
    _w(clave / "esperado-ronda.json", esp_ronda)
    efecto = {"resumen": f"{len(comps)} compromisos en {SEMANAS_SAM} comités y las notas de hoy; "
                         f"{sum(c['cumplido'] for c in comps)} cerrados con acta, "
                         f"{sum(bool(c.get('reclamado')) for c in comps)} dichos sin acta"}
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


# La muestra de Samuel. Con tres compromisos por industria su cifra salía de doce casos y
# el margen era de cuarenta puntos (ronda 2): ni subir ni bajar significaba nada. Un
# proyecto real llega a su sexta semana con decenas de compromisos dichos en comité,
# unos reprogramados, otros cerrados con acta y otros «ya lo entregué» sin nada que lo
# pruebe. Eso es lo que se escribe aquí, y la clave sale de lo que quedó escrito.
VERBOS_SAM = ("Entregar el punto", "Enviar el documento", "Cerrar la prueba", "Revisar el anexo",
              "Validar el ambiente", "Aprobar el diseño", "Actualizar la matriz", "Confirmar la fecha")
SEMANAS_SAM, NUEVOS_SAM = 6, 4


def historia_samuel(carpeta: Path, p: dict, hoy: dt.date, nombres: list, semilla: str) -> list:
    """Seis comités semanales del proyecto de Samuel, con sus compromisos de punta a punta.
    Reemplaza la minuta del simulador —que solo mostraba la última foto— por la historia:
    cada fecha nueva queda en la minuta de la semana en que se dijo."""
    import random
    rnd = random.Random(semilla)
    reun, seg = carpeta / "30-reuniones", carpeta / "20-seguimiento"
    reun.mkdir(parents=True, exist_ok=True)
    seg.mkdir(parents=True, exist_ok=True)
    for f in reun.glob("*comite-semanal*"):
        f.unlink()
    iso = lambda d: d.isoformat()
    comps, n = [], 0
    for w in range(SEMANAS_SAM):
        fr = hoy - dt.timedelta(days=7 * (SEMANAS_SAM - w))
        cerrados, dichos = [], []
        for c in [c for c in comps if not c["cumplido"] and not c.get("reclamado")]:
            u = rnd.random()
            fechada = c["fechas"][-1] is not None
            if c.get("terco") or (0.20 <= u < 0.50):
                if fechada:                       # otra fecha: una reprogramación más
                    base = max(dt.date.fromisoformat(c["fechas"][-1]), fr)
                    c["fechas"].append(iso(base + dt.timedelta(days=rnd.randint(7, 21))))
                else:                             # «por definir» que se fecha: no se reprograma
                    c["fechas"].append(iso(fr + dt.timedelta(days=rnd.randint(7, 21))))
            elif u < 0.12 and fechada:
                c["cumplido"] = True
                cerrados.append(c)
                (seg / f"{iso(fr)}-acta-recibo-{c['n']}.md").write_text(
                    f"# Acta de recibo · {c['que']}\n\n**Proyecto:** {p['codigo']} · {p['nombre']}\n"
                    f"**Fecha de recibo:** {iso(fr)}\n**Recibido por:** {p['gerente']}\n\n"
                    f"Se recibe a satisfacción: **{c['que']}**, compromiso de {c['quien']}.\n",
                    encoding="utf-8")
            elif u < 0.20:
                c["reclamado"] = True             # lo dice, y no hay acta: sigue abierto
                dichos.append(c)
        for k in range(NUEVOS_SAM):
            n += 1
            sin_fecha = rnd.random() < 0.15
            comps.append({"n": n, "quien": rnd.choice(nombres), "que": f"{VERBOS_SAM[n % len(VERBOS_SAM)]} {n}",
                          "fechas": [None if sin_fecha else iso(fr + dt.timedelta(days=rnd.randint(3, 28)))],
                          "cumplido": False, "dicho": iso(fr), "terco": w == 0 and k < 2})
        abiertos = [c for c in comps if not c["cumplido"] and not c.get("reclamado")]
        filas = "\n".join(f"| {c['quien']} | {c['que']} | {c['fechas'][-1] or 'por definir'} |" for c in abiertos)
        partes = [f"# {p.get('comite') or 'Comité de seguimiento'} · {p['nombre']}", "",
                  f"**Fecha:** {iso(fr)}",
                  f"**Asistentes:** {', '.join(sorted({p['gerente'], *(c['quien'] for c in abiertos)}))}", "",
                  "## Compromisos abiertos", "", "| Responsable | Compromiso | Para |", "|---|---|---|", filas]
        if cerrados:
            partes += ["", "## Cerrados en esta reunión", ""] + [
                f"- {c['que']} ({c['quien']}): recibido, acta de recibo del {iso(fr)}." for c in cerrados]
        if dichos:
            partes += ["", "## Lo que se dijo", ""] + [
                f"- {c['quien']} dice que ya entregó «{c['que'].lower()}». No se presentó acta." for c in dichos]
        (reun / f"{iso(fr)}-comite-semanal.md").write_text("\n".join(partes) + "\n", encoding="utf-8")
    return comps


def escribir_notas(carpeta: Path, p: dict, comps: list, hoy: dt.date) -> Path:
    """Las notas crudas de la reunión de hoy, como las toma alguien en el cuaderno: sin
    tabla, con las fechas dichas como se dicen. Reprograma el compromiso que más se ha
    movido, deja uno sin fecha y uno nuevo, y un riesgo que nadie registra."""
    iso = lambda d: d.isoformat()
    abiertos = [c for c in comps if not c["cumplido"] and not c.get("reclamado") and c["fechas"][-1]]
    c1 = max(abiertos, key=lambda c: len([x for x in c["fechas"] if x]), default=None)
    otro, tercero = "Laura Vélez", "Óscar Ramírez"
    asistentes = sorted({p["gerente"], *(c["quien"] for c in abiertos)})
    lineas = [f"notas reunión {p['nombre'].lower()} — {iso(hoy)}",
              f"estuvieron: {', '.join(sorted(set(asistentes) | {otro, tercero}))}", ""]
    if c1:
        nueva = max(dt.date.fromisoformat(c1["fechas"][-1]), hoy) + dt.timedelta(days=14)
        c1["fechas"].append(iso(nueva))
        lineas.append(f"- {c1['quien']} dice que lo de «{c1['que'].lower()}» no alcanzó, "
                      f"se compromete para el {nueva.strftime('%d/%m/%Y')}")
    lineas.append(f"- {otro} queda de mandar el ajuste del presupuesto la otra semana")
    comps.append({"quien": otro, "que": "Mandar el ajuste del presupuesto", "fechas": [None],
                  "cumplido": False, "dicho": iso(hoy)})
    f3 = hoy + dt.timedelta(days=10)
    lineas.append(f"- {tercero}: revisión con el proveedor, queda para el {iso(f3)}")
    comps.append({"quien": tercero, "que": "Revisión con el proveedor", "fechas": [iso(f3)],
                  "cumplido": False, "dicho": iso(hoy)})
    lineas += ["- se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase,"
               " nadie lo anotó como riesgo", "- próxima reunión en dos semanas", ""]
    ruta = carpeta / f"{iso(hoy)}-notas-reunion.txt"
    ruta.write_text("\n".join(lineas), encoding="utf-8")
    return ruta


def clave_samuel(comps: list) -> list:
    """Lo que Samuel debe dejar en su ficha por cada compromiso: la fecha vigente, cuántas
    veces se reprogramó —fechas a la vista menos la primera; «por definir» no cuenta— y si
    está cumplido, que solo lo está con acta."""
    return [{"quien": c["quien"], "que": c["que"], "fecha": c["fechas"][-1] or "no_declarada",
             "reprogramaciones": max(len([x for x in c["fechas"] if x]) - 1, 0),
             "estado": "cumplido" if c["cumplido"] else "abierto"} for c in comps]


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
                "inicio": dt.datetime.fromtimestamp(t0, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
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


def servidor_instalado(espacio: Path) -> Path:
    """El servidor.py de la versión que la sesión tenía instalada —la que aceptó en sus
    términos—, no el del árbol del repositorio. Si no está en la caché, el del repositorio."""
    try:
        cfg = _j(espacio / ".criterio" / "portafolio" / "config.json")
        version = (cfg.get("terms_accepted") or {}).get("family_version")
    except (OSError, json.JSONDecodeError):
        version = None
    cache = Path.home() / ".claude" / "plugins" / "cache"
    for f in sorted(cache.glob(f"*/criterio-portfolio/{version}/scripts/servidor.py")) if version else []:
        return f
    return RAIZ / "plugins" / "criterio-portfolio" / "scripts" / "servidor.py"


# Lo que no debe llegar a quien lee un informe: palabras del esquema, rutas de la ficha,
# nombres de señal en snake_case y restos de un programa.
CRUDO_ROSTRUM = re.compile(
    r"\b(?:identity|declared|plan|money|vendors|raid|changes|commitments|pm_record|activity|meta)"
    r"(?:\[\d+\])?\.[a-z_]+|\b(?:not_found|no_declarada|unknown|undefined|NaN|None|null)\b"
    r"|Traceback|\[object|No aplica|\b[a-z]+_[a-z_]+\b")


def probar_servidor(espacio: Path, puerto: int = 8799) -> dict:
    """Rostrum de punta a punta. Lo levanta este script, no el agente —un servidor en
    primer plano dentro de una sesión sin interfaz no termina—, con la versión instalada,
    y recorre cada enlace interno desde la portada: que cada página responda, que ninguna
    ruta, palabra del esquema o nombre de señal llegue al informe, que una petición se
    guarde y que no escriba fichas. Las páginas de corrida muestran lo que el agente dijo
    tal cual; lo crudo de ellas se cuenta aparte, como voz del agente."""
    import html as _html
    import urllib.error
    import urllib.parse
    espacio = espacio.resolve()       # el servidor corre con cwd en el espacio
    cfg = _j(espacio / ".criterio" / "portafolio" / "config.json")
    estado = espacio / cfg["paths"]["state"]
    informe = espacio / cfg["paths"].get("reports", "reportes")
    script = servidor_instalado(espacio)
    antes = manifiesto(estado / "records") if (estado / "records").is_dir() else {}
    buzon = estado / "peticiones"
    previas = set(buzon.glob("*")) if buzon.is_dir() else set()
    log = espacio.parent / "rostrum.log"
    p = subprocess.Popen([sys.executable, str(script), "--informe", str(informe), "--estado", str(estado),
                          "--config", str(espacio / ".criterio" / "portafolio" / "config.json"),
                          "--evidencia", str(espacio / ".criterio" / "corridas"), "--puerto", str(puerto)],
                         cwd=espacio, stdout=subprocess.DEVNULL, stderr=log.open("w"))
    base = f"http://127.0.0.1:{puerto}"
    vistas, cola, malas, crudo, voz, paginas, peticion = {}, ["/"], {}, [], 0, 0, None
    def visible(s):
        s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
        s = re.sub(r"(?is)<span class=\"cita\">.*?</span>", " ", s)   # la cita es una ruta de archivo
        return _html.unescape(re.sub(r"(?s)<[^>]+>", " ", s))
    try:
        time.sleep(3)
        while cola and len(vistas) < 900:
            ruta = cola.pop(0)
            if ruta in vistas:
                continue
            try:
                with urllib.request.urlopen(base + ruta, timeout=15) as r:
                    cod, cuerpo = r.status, r.read().decode("utf-8", "replace")
                    tipo, final = r.headers.get("Content-Type", ""), urllib.parse.urlparse(r.url).path
            except urllib.error.HTTPError as e:
                cod, cuerpo, tipo, final = e.code, "", "", ruta
            except Exception as e:  # noqa: BLE001
                cod, cuerpo, tipo, final = str(e)[:60], "", "", ruta
            vistas[ruta] = cod
            if cod != 200:
                malas[ruta] = cod
                continue
            if "html" not in tipo:
                continue
            paginas += 1
            if ruta.startswith("/corrida/"):
                # Lo que el agente le dijo a la persona, tal cual; lo que marcó como código
                # (un comando, un campo) se muestra como código y no cuenta.
                voz += len(CRUDO_ROSTRUM.findall(visible(re.sub(r"(?s)<code>.*?</code>", " ", cuerpo))))
            else:
                crudo += [f"{ruta}: {m.group(0)}" for m in CRUDO_ROSTRUM.finditer(visible(cuerpo))]
            for href in re.findall(r'href="([^"#]+)', cuerpo):
                u = urllib.parse.urlparse(urllib.parse.urljoin(base + final, _html.unescape(href)))
                if u.netloc == f"127.0.0.1:{puerto}":
                    # Como un navegador: un espacio o una tilde en el enlace viajan codificados.
                    k = urllib.parse.quote(u.path, safe="/%:@") + (f"?{u.query}" if u.query else "")
                    if k not in vistas and k not in cola:
                        cola.append(k)
        n0 = json.loads(urllib.request.urlopen(base + "/estado.json", timeout=10).read())["peticiones_abiertas"]
        datos = urllib.parse.urlencode({"asunto": "explicar", "texto": "Prueba del arnés: ¿de dónde sale el verde?"})
        urllib.request.urlopen(urllib.request.Request(base + "/peticion", data=datos.encode()), timeout=10)
        n1 = json.loads(urllib.request.urlopen(base + "/estado.json", timeout=10).read())["peticiones_abiertas"]
        peticion = n1 == n0 + 1
        pantalla = revisar_pantalla(base, [r for r, c in vistas.items() if c == 200 and not r.endswith(".json")])
    except Exception as e:  # noqa: BLE001
        malas["(arnés)"] = str(e)[:80]
        pantalla = None
    finally:
        p.terminate()
        for f in (set(buzon.glob("*")) if buzon.is_dir() else set()) - previas:
            f.unlink()          # la petición de prueba no se queda en el buzón del agente
    despues = manifiesto(estado / "records") if (estado / "records").is_dir() else {}
    # La cifra de Rostrum: comprobaciones que pasan sobre las que se hacen. Una por ruta
    # que debe responder, una por página del informe que no debe mostrar nada crudo, una
    # por página y ancho de pantalla, la petición y las fichas.
    paginas_informe = [r for r, c in vistas.items() if c == 200 and not r.startswith("/corrida/")
                       and not r.endswith(".json")]
    con_crudo = {x.split(": ", 1)[0] for x in crudo}
    total = len(vistas) + len(paginas_informe) + 2
    pasan = (len(vistas) - len(malas)) + (len(paginas_informe) - len(con_crudo)) \
        + bool(peticion) + (antes == despues)
    if pantalla is not None:
        n = len([r for r, c in vistas.items() if c == 200 and not r.endswith(".json")])
        total += 2 * n
        pasan += 2 * n - sum(len(v) for v in pantalla.values())
    return {"servidor": str(script.relative_to(Path.home())) if Path.home() in script.parents else "repositorio",
            "rutas": len(vistas), "paginas": paginas, "malas": malas, "crudo": sorted(set(crudo))[:40],
            "crudo_total": len(crudo), "voz_del_agente": voz, "peticion": peticion,
            "fichas_intactas": antes == despues, "pantalla": pantalla,
            "comprobaciones": {"total": total, "pasan": pasan}}


def revisar_pantalla(base: str, rutas: list):
    """Cada página en un teléfono y en un escritorio, con `tests/pantalla.mjs`. Sin Node o
    sin Playwright devuelve None: la prueba dice que no se hizo, no que pasó."""
    import tempfile
    if not shutil.which("node"):
        return None
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(rutas, f)
    entorno = dict(os.environ)
    if os.environ.get("PLAYWRIGHT_NODE_PATH"):
        entorno["NODE_PATH"] = os.environ["PLAYWRIGHT_NODE_PATH"]
    r = subprocess.run(["node", str(RAIZ / "tests" / "pantalla.mjs"), base, f.name],
                       capture_output=True, text=True, timeout=1800, env=entorno)
    Path(f.name).unlink()
    if r.returncode:
        return None
    fuera = json.loads(r.stdout.strip().splitlines()[-1])
    return {"390": fuera.get("390", []), "1280": fuera.get("1280", [])}


# ── revisar: los contratos ────────────────────────────────────────────────

# Lo que escribe el propio plugin en cada comando: el rastro de la corrida y la marca de
# la sesión en curso que dejan sus ganchos. No es una escritura del comando.
# Y la aceptación de los términos: cualquier comando la pide si la versión instalada cambió.
SIEMPRE = ("corridas", "corrida-en-curso", "cache", ".criterio/corridas", ".criterio/en-curso", "salida-",
           ".criterio/terminos/")


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
    """Una cita puede ir desde la raíz de documentos o desde la carpeta del proyecto: se
    da por buena si algún documento termina en esa ruta."""
    docs = espacio / "documentos"
    todos = [str(f.relative_to(docs)) for f in docs.rglob("*") if f.is_file()]
    rotas = []
    def recorrer(n):
        if isinstance(n, dict):
            s = n.get("source")
            if isinstance(s, str) and s and not s.startswith(("http", "script", "compute")):
                s2 = s.split("#")[0].split(":")[0].strip()
                if not any(t == s2 or t.endswith("/" + s2) for t in todos):
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
        # Lo que el contrato dice que escribe y no escribió. Va como aviso y no como falla:
        # un barrido sin documentos nuevos no tiene por qué tocar fichas. Se revisa a mano.
        MARCAS = (("config.json", "config.json"), ("records", "/records/"), ("snapshots", "/snapshots/"),
                  ("cadencia", "cadencia"), ("requirements", "/requirements/"), ("producto.json", "producto.json"),
                  ("ficha-pm.json", "ficha-pm.json"), ("30-reuniones", "30-reuniones/"),
                  ("<informes>", "reportes/"), ("<publicados>", "public"))
        avisos = []
        for item in escribe:
            if any(w in item for w in ("solo", "(init)", " si ")):
                continue
            marca = next((m for k, m in MARCAS if k in item), None)
            if marca and not any(marca in c for c in cambios):
                avisos.append(f"no escribió {item}")
        problemas = []
        if r["error"]:
            problemas.append(f"no terminó ({r['estado']})")
        if fuera:
            problemas.append(f"escribió fuera de su contrato: {fuera[:4]}")
        if borro_docs:
            problemas.append(f"borró documentos: {borro_docs[:4]}")
        if rotas:
            problemas.append(f"{len(rotas)} citas a documentos que no existen: {rotas[:3]}")
        s = r.get("servidor")
        if r["comando"] == "portfolio-server" and (carpeta / "rostrum.json").is_file():
            s = _j(carpeta / "rostrum.json")      # la prueba completa, corrida aparte sobre la carpeta
        if s and "rutas" in s and isinstance(s["rutas"], dict):     # la prueba de antes de la ronda 3
            s = {"malas": {k: v for k, v in s["rutas"].items() if v != 200}, "crudo": [], "peticion": True,
                 "fichas_intactas": s["fichas_intactas"]}
        if s:
            if s["malas"]:
                problemas.append(f"rutas de Rostrum que no responden: {s['malas']}")
            if s["crudo"]:
                problemas.append(f"Rostrum muestra {s.get('crudo_total', len(s['crudo']))} rutas, palabras del esquema "
                                 f"o claves de señal: {s['crudo'][:3]}")
            for ancho, rutas_ in (s.get("pantalla") or {}).items():
                if rutas_:
                    problemas.append(f"Rostrum se sale de la pantalla a {ancho} px en {len(rutas_)} páginas: {rutas_[:3]}")
            if s["peticion"] is False:
                problemas.append("Rostrum no guardó la petición")
            if not s["fichas_intactas"]:
                problemas.append("Rostrum modificó fichas")
        filas.append({"n": r["n"], "agente": r["agente"], "comando": r["comando"], "termino": not r["error"],
                      "contrato": not problemas, "problemas": problemas, "avisos": avisos, "segundos": r["segundos"],
                      "tokens": r["tokens"]})
    fugas = auditar_fugas(carpeta)
    completos = sum(1 for x in filas if x["termino"])
    cumplen = sum(1 for x in filas if x["contrato"])
    resumen = {"comandos": len(ORDEN), "corridos": len(filas), "completos": completos,
               "contratos_cumplidos": cumplen, "corrida_completa": completos == len(ORDEN),
               "fugas": fugas,
               "segundos": sum(x["segundos"] for x in filas), "tokens": sum(x["tokens"] for x in filas),
               "filas": filas}
    _w(carpeta / "revision.json", resumen)
    for x in filas:
        print(f"{x['n']:02d} {x['comando']:22} {'terminó' if x['termino'] else 'FALLÓ  '} "
              f"{'contrato ok' if x['contrato'] else 'CONTRATO'} {'; '.join(x['problemas'])[:150]}"
              + (f"  · aviso: {'; '.join(x['avisos'])[:120]}" if x["avisos"] else ""))
    print(f"\nauditoría de fugas: {len(fugas)} lecturas de la clave" + "".join(f"\n  {x}" for x in fugas[:5]))
    print(f"\n{completos}/{len(ORDEN)} terminaron · {cumplen}/{len(ORDEN)} cumplen su contrato · "
          f"{resumen['segundos'] // 60} min · {resumen['tokens'] / 1e6:.1f} M tokens")
    return 0


def auditar_fugas(carpeta: Path) -> list:
    """Que ningún agente haya leído la clave. Recorre lo que Claude Code registra de cada
    sesión —cada herramienta que llamó y con qué— desde que empezó la corrida, y señala
    cualquier lectura de la clave o del material del simulador. Una calificación con una
    fuga no vale, y se repite la industria."""
    espacio = (carpeta / "espacio").resolve()
    proyectos = Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(espacio))
    primero = min((_j(f).get("inicio", "") for f in (carpeta / "salidas").glob("[0-9][0-9]-*.json")), default="")
    patron = re.compile(r"(cat|Read|head|less|open|json\.load)[^\n]{0,200}(/clave/|esperado(-ronda)?\.json|"
                        r"organizacion\.json|notas\.json|LO-QUE-HAY|bitacora-dia)")
    fugas = []
    for f in proyectos.glob("*.jsonl"):
        for linea in f.read_text(encoding="utf-8", errors="replace").splitlines():
            if "tool_use" not in linea:
                continue
            try:
                r = json.loads(linea)
            except json.JSONDecodeError:
                continue
            if r.get("type") != "assistant" or r.get("timestamp", "") < primero:
                continue
            for c in r["message"].get("content", []):
                if c.get("type") == "tool_use":
                    txt = c.get("name", "") + " " + json.dumps(c.get("input"), ensure_ascii=False)
                    if patron.search(txt):
                        fugas.append(f"{r['timestamp']} {txt[:160]}")
    return fugas


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
    # Cada agente, en la carpeta de estado que dice su configuración.
    def estado_de(rel: str, defecto: str) -> Path:
        f = espacio / ".criterio" / rel / "config.json"
        return espacio / (_j(f).get("paths", {}).get("state", defecto) if f.is_file() else defecto)
    estado_vera = estado_de("portafolio", "estado")
    ficha_sam = estado_de(f"proyecto/{obj['pry_sam']}", "estado") / "records" / f"{obj['pry_sam']}.json"
    sam = ficha_sam if ficha_sam.is_file() else None
    comps = (_j(sam).get("commitments") or []) if sam else []
    v = lambda x: (x.get("value") if isinstance(x, dict) else x) or ""
    correctos, detalle = 0, []
    def es_el(x, c):
        """La misma persona y el mismo compromiso: el número que lo distingue, o la última
        palabra cuando no lleva número. Tolera que el agente lo redacte a su manera."""
        if not v(x.get("who")) or v(x.get("who")).split()[0] != c["quien"].split()[0]:
            return False
        num = re.findall(r"\d+", c["que"])
        que = v(x.get("what")).lower()
        return bool(re.search(rf"\b{num[-1]}\b", que)) if num else c["que"].lower().split()[-1] in que
    for c in notas["compromisos"]:
        m = next((x for x in comps if es_el(x, c)), None)
        cumplido = bool(m) and v(m.get("state")) == "met"
        ok = bool(m) and (v(m.get("due_date")) == c["fecha"] or (c["fecha"] == "no_declarada" and v(m.get("due_date")) in ("", "no_declarada"))) \
            and len(m.get("reschedules") or []) == c["reprogramaciones"] \
            and cumplido == (c.get("estado") == "cumplido")
        correctos += ok
        detalle.append({"quien": c["quien"], "esperado": c, "ok": ok,
                        "encontrado": {"fecha": v(m.get("due_date")), "reprogramaciones": len(m.get("reschedules") or []),
                                       "estado": v(m.get("state"))} if m else None})
    # Alba: las señales de su producto
    cfg_prd = espacio / ".criterio" / "producto" / obj["prd"] / "config.json"
    prd_obt = {}
    if cfg_prd.is_file():
        rutas = _j(cfg_prd).get("paths", {})
        r, _ = fiabilidad.correr(fiabilidad.PRODUCT, "compute", "--state", espacio / rutas.get("state", "estado"),
                                 "--fichas", estado_vera / "records", "--today", hoy)
        if r.returncode == 0:
            prd_obt = {obj["prd"]: [x["signal"] for x in (json.loads(r.stdout).get("alerts") or [])]}
        else:
            print("Alba · compute falló:", r.stderr.strip()[:200])
    cal = fiabilidad.calificar({obj["prd"]: clave["esperado"].get(obj["prd"], [])}, prd_obt)
    t = fiabilidad.totales(cal)
    salida = {"samuel": {"compromisos": len(notas["compromisos"]), "correctos": correctos, "detalle": detalle},
              "alba": {"producto": obj["prd"], **t, "errores": cal["por_caso"]}}
    _w(carpeta / "calificacion-samuel-alba.json", salida)
    print(f"Samuel · compromisos del proyecto: {correctos} de {len(notas['compromisos'])}")
    for d in detalle:
        print(f"   {'OK' if d['ok'] else '  '} {d['quien']}: esperado {d['esperado']['fecha']} "
              f"({d['esperado']['reprogramaciones']}) · encontrado {d['encontrado']}")
    print(f"Alba · {obj['prd']}: {t}")
    return 0


# ── publicar: la evidencia de una industria al repositorio ────────────────

def rostrum(a) -> int:
    """La prueba completa de Rostrum sobre una carpeta ya corrida: deja `rostrum.json`,
    que `revisar` usa para el comando del servidor y `publicar` lleva a la evidencia."""
    carpeta = Path(a.carpeta).expanduser()
    r = probar_servidor(carpeta / "espacio", a.puerto)
    _w(carpeta / "rostrum.json", r)
    print(f"Rostrum · {r['servidor']} · {r['rutas']} rutas, {r['paginas']} páginas · "
          f"{len(r['malas'])} sin responder {r['malas'] or ''} · {r['crudo_total']} crudas en el informe · "
          f"{r['voz_del_agente']} en la voz del agente · petición {'ok' if r['peticion'] else 'FALLA'} · "
          f"fichas {'intactas' if r['fichas_intactas'] else 'MODIFICADAS'} · pantalla "
          f"{'no revisada (sin Node o Playwright)' if r['pantalla'] is None else {k: len(v) for k, v in r['pantalla'].items()}}"
          f" · {r['comprobaciones']['pasan']} de {r['comprobaciones']['total']} comprobaciones")
    for x in r["crudo"][:12]:
        print("   ", x)
    return 0


def publicar(a) -> int:
    """Copia a `tests/evidencias/rondas/<ronda>/<entorno>/` lo que hace falta para auditar
    una industria sin volver a correrla: lo que mostró cada comando, la revisión de
    contratos, la calificación, la clave, y en dos paquetes la carpeta que leyó el agente y
    lo que escribió."""
    import tarfile
    carpeta = Path(a.carpeta).expanduser()
    obj = _j(carpeta / "clave" / "objetivos.json")
    destino = RAIZ / "tests" / "evidencias" / "rondas" / f"ronda-{obj['ronda']}" / obj["entorno"]
    if destino.exists():
        shutil.rmtree(destino)
    (destino / "clave").mkdir(parents=True)
    shutil.copytree(carpeta / "salidas", destino / "salidas")
    for f in ("revision.json", "revision.txt", "calificacion-samuel-alba.json", "rostrum.json"):
        if (carpeta / f).is_file():
            shutil.copy2(carpeta / f, destino / f)
    for f in ("esperado-ronda.json", "notas.json", "objetivos.json", "organizacion.json"):
        shutil.copy2(carpeta / "clave" / f, destino / "clave" / f)
    espacio = carpeta / "espacio"
    with tarfile.open(destino / "documentos.tgz", "w:gz") as t:
        t.add(espacio / "documentos", arcname="documentos")
    with tarfile.open(destino / "estado-del-agente.tgz", "w:gz") as t:
        for d in ("estado", "estado-producto", ".criterio", "reportes"):
            if (espacio / d).exists():
                t.add(espacio / d, arcname=d)
    rev = _j(carpeta / "revision.json")
    (destino / "LEEME.md").write_text(
        f"# Ronda {obj['ronda']} · {obj['entorno']}\n\n"
        f"Corte {obj['hoy']}. {rev['completos']} de {rev['comandos']} comandos terminaron, "
        f"{rev['contratos_cumplidos']} cumplieron su contrato, {len(rev.get('fugas') or [])} lecturas de la clave.\n\n"
        "- `salidas/NN-comando.md`: lo que el comando le mostró a la persona, tal cual.\n"
        "- `salidas/NN-comando.json`: cuánto tardó, cuántos tokens usó y qué archivos cambió.\n"
        "- `revision.json`: el contrato de cada comando y la auditoría de que ningún agente leyó la clave.\n"
        "- `calificacion-samuel-alba.json`: los compromisos de Samuel y las alertas del producto de Alba.\n"
        "- `rostrum.json`: Rostrum recorrido entero —cada página que enlaza, si responde, si muestra rutas "
        "o claves del esquema, si guarda una petición y si deja las fichas intactas—, con la versión instalada.\n"
        "- `clave/`: lo que el agente nunca vio.\n"
        "- `documentos.tgz`: la carpeta que leyó el agente. `estado-del-agente.tgz`: lo que escribió.\n\n"
        "La calificación de Vera está en `tests/evidencias/calificaciones.json` y los defectos en "
        "`tests/evidencias/defectos.json`.\n", encoding="utf-8")
    print(f"publicado en {destino.relative_to(RAIZ)}")
    return 0


# ── el resumen de una ronda, para el portal ───────────────────────────────

def _documentos(tgz: Path) -> dict:
    """Los documentos que la industria le dio a los agentes, por formato: el material que
    procesaron, contado del archivo publicado y no tecleado."""
    import tarfile
    from collections import Counter
    if not tgz.is_file():
        return {"total": 0, "por_formato": {}}
    with tarfile.open(tgz) as t:
        fmt = Counter(Path(m.name).suffix.lower().lstrip(".") or "otro" for m in t.getmembers() if m.isfile())
    return {"total": sum(fmt.values()), "por_formato": dict(fmt.most_common())}


def resumen(a) -> int:
    """Lo que un cliente necesita saber de una ronda, calculado de la evidencia y no
    tecleado: los comandos que terminaron y cumplieron su contrato, y las primeras corridas
    de Vera juntas, con un intervalo que remuestrea proyectos de todas las industrias."""
    import banco
    base = RAIZ / "tests" / "evidencias" / "rondas" / a.ronda
    filas = [f for f in banco.leer() if f.get("material") == a.ronda and f["tipo"] == "primera"
             and f["agente"] == "vera"]
    industrias = []
    for d in sorted(x for x in base.iterdir() if x.is_dir()):
        rev = _j(d / "revision.json") if (d / "revision.json").is_file() else {}
        sa = _j(d / "calificacion-samuel-alba.json") if (d / "calificacion-samuel-alba.json").is_file() else {}
        v = next((f for f in filas if f["entorno"] == d.name), None)
        # Rostrum: la prueba completa que dejó `rostrum` o la del comando del servidor.
        ro = _j(d / "rostrum.json") if (d / "rostrum.json").is_file() else \
            (_j(d / "salidas" / "34-portfolio-server.json").get("servidor") or {}) \
            if (d / "salidas" / "34-portfolio-server.json").is_file() else {}
        industrias.append({
            "entorno": d.name, "comandos": rev.get("comandos"), "completos": rev.get("completos"),
            "contratos": rev.get("contratos_cumplidos"), "fugas": len(rev.get("fugas") or []),
            "minutos": round((rev.get("segundos") or 0) / 60), "tokens": rev.get("tokens"),
            "documentos": _documentos(d / "documentos.tgz"),
            "proyectos": v.get("proyectos") if v else None,
            "vera": {k: v[k] for k in ("id", "aciertos", "falsos_positivos", "falsos_negativos", "precision",
                                       "cobertura", "ic_precision", "ic_cobertura", "controles",
                                       "controles_limpios", "version")} if v else None,
            "samuel": {"correctos": sa["samuel"]["correctos"], "total": sa["samuel"]["compromisos"]} if sa else None,
            "alba": {"aciertos": sa["alba"]["aciertos"], "esperados": sa["alba"]["aciertos"] + sa["alba"]["falsos_negativos"],
                     "reportados": sa["alba"]["aciertos"] + sa["alba"]["falsos_positivos"]} if sa else None,
            "rostrum": {"pasan": ro["comprobaciones"]["pasan"], "total": ro["comprobaciones"]["total"],
                        "pantalla": ro.get("pantalla") is not None} if ro.get("comprobaciones") else None,
        })
    casos = {}
    senales = {}
    for f in filas:
        for c, n in (f.get("por_caso") or {}).items():
            casos[f"{f['entorno']}/{c}"] = {"aciertos": n[0], "falsos_positivos": ["x"] * n[1], "falsos_negativos": ["x"] * n[2]}
        for k, x in (f.get("por_senal") or {}).items():
            t = senales.setdefault(k, {"aciertos": 0, "falsos_positivos": 0, "falsos_negativos": 0})
            for kk in t:
                t[kk] += x[kk]
    ac = sum(f["aciertos"] for f in filas)
    fp = sum(f["falsos_positivos"] for f in filas)
    fn = sum(f["falsos_negativos"] for f in filas)
    out = {"ronda": a.ronda, "fecha": dt.date.today().isoformat(), "industrias": industrias,
           "vera": {"aciertos": ac, "falsos_positivos": fp, "falsos_negativos": fn, "proyectos": len(casos),
                    "ic_precision": banco.ancho(banco.wilson(ac, ac + fp), banco.bootstrap(casos, "precision")),
                    "ic_cobertura": banco.ancho(banco.wilson(ac, ac + fn), banco.bootstrap(casos, "cobertura")),
                    "controles": sum(f["controles"] for f in filas),
                    "controles_limpios": sum(f["controles_limpios"] for f in filas)},
           "senales": [{"senal": k, **v} for k, v in sorted(senales.items(), key=lambda kv: -sum(kv[1].values()))]}
    _w(base / "resumen.json", out)
    print(json.dumps(out["vera"], ensure_ascii=False))
    for i in industrias:
        print(f"  {i['entorno']:13} {i['completos']}/{i['comandos']} completos · {i['contratos']} contratos · "
              f"{i['fugas']} fugas · {i['minutos']} min")
    return 0


# ── defectos ──────────────────────────────────────────────────────────────

ORIGENES = ("agente", "codigo", "instrucciones", "material", "clave", "arnes")


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
    s = sub.add_parser("rostrum")
    s.add_argument("carpeta")
    s.add_argument("--puerto", type=int, default=8799)
    s = sub.add_parser("publicar")
    s.add_argument("carpeta")
    s = sub.add_parser("resumen")
    s.add_argument("ronda")
    sub.add_parser("verificar")
    a = ap.parse_args()
    sys.exit({"armar": armar, "correr": correr, "revisar": revisar, "calificar": calificar,
              "publicar": publicar, "rostrum": rostrum, "resumen": resumen, "defecto": defecto, "verificar": verificar}[a.accion](a))
