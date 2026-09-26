#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Criterio Product — la aritmética del registro de requerimiento.

El modelo extrae; esto calcula. Leer en una entrevista que alguien pidió algo es leer.
Contar cuántos requerimientos aceptados no tienen evidencia de demanda, cuántos días
lleva uno sin decidirse, y si lo que el negocio declara coincide con lo que la métrica
mide, es aritmética — y la aritmética va aquí, donde es determinista y se puede probar.

    python3 producto.py init      --state <dir>
    python3 producto.py config    --config <archivo>
    python3 producto.py compute   --state <dir> [--config <archivo>] [--fichas <dir>]
                                  [--today YYYY-MM-DD]
    python3 producto.py snapshot  --state <dir> [--today YYYY-MM-DD]
    python3 producto.py diff      --state <dir> [--against <snapshot.json>]
    python3 producto.py selftest

Solo librería estándar.

Por qué este script existe aparte de `pmo.py`: la espina de la ficha de un proyecto es
`plan` + `baseline` + `money`, y en definición de producto **ninguno de los tres
existe**. Un requerimiento no tiene línea base ni presupuesto: tiene evidencia de
demanda, criterios de aceptación, y un proyecto que lo ejecuta o no lo ejecuta.

Lo que sí comparte es el contrato de dato: **todo campo es un valor o
`{value, source, source_date, state}`**, y eso se importa de `pmo.py`, que es la copia
que este plugin lleva. Se importa y no se reescribe: dos definiciones del mismo campo
que se separan es la deuda que este proyecto no acepta.

El estado vive así:

    <estado>/
      producto.json              la definición, y las afirmaciones que hace
      requirements/REQ-xxx.json  un registro por requerimiento
      metrics/<nombre>.json      la serie medida, con su fuente
      snapshots/

Nada aquí decide qué reportar: reporta lo que cruzó un umbral. Qué significa cada señal
está en el skill `product-health`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

# El contrato de campo es el de la familia. Se importa de la copia que este plugin
# lleva —mismo directorio—, nunca de la ruta del otro plugin: un plugin instalado
# tiene que correr solo.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pmo import as_date, as_number, pct, source_of, state_of, value  # noqa: E402

DEFAULT_THRESHOLDS = {
    # Días que un requerimiento puede llevar propuesto sin que nadie lo decida. Pasado
    # eso no es un pendiente: es una decisión que no se está tomando.
    "undecided_days": 60,
    # Días que un supuesto puede llevar declarado sin verificarse. Un supuesto que
    # nadie verifica no es un supuesto: es un riesgo sin registrar.
    "assumption_unverified_days": 30,
    # Meses tras los cuales la evidencia de demanda envejece. Una entrevista de hace
    # dos años no sostiene una definición de hoy, y esto es lo primero que se olvida.
    "evidence_stale_months": 12,
    # Diferencia porcentual entre lo que el negocio declara y lo que la métrica mide,
    # a partir de la cual hay contradicción y no imprecisión.
    "claim_gap_pct": 20,
}

# El vocabulario de estado de un requerimiento, en los dos idiomas en que puede venir
# escrito. El orden no es severidad: solo permite preguntar «¿ya se decidió?».
ESTADOS = {
    "propuesto": "propuesto", "proposed": "propuesto",
    "aceptado": "aceptado", "accepted": "aceptado",
    "descartado": "descartado", "discarded": "descartado", "rejected": "descartado",
    "en_construccion": "en_construccion", "building": "en_construccion",
    "en construcción": "en_construccion",
    "entregado": "entregado", "delivered": "entregado",
}

# Los estados en que alguien ya decidió que esto se hace. Son los que exigen evidencia,
# criterio de aceptación y un proyecto que lo ejecute.
DECIDIDOS = ("aceptado", "en_construccion", "entregado")

# Las señales. Cada una tiene su nombre en castellano y su umbral —si lo tiene— en el
# skill `product-health`, y `tests/coherencia.py` falla si alguna no está ahí.
SENALES = (
    "requirement_without_owner",
    "requirement_without_acceptance",
    "requirement_accepted_without_evidence",
    "requirement_undecided",
    "requirement_untraced",
    "trace_not_confirmed",
    "decision_without_source",
    "assumption_unverified",
    "evidence_stale",
    "claim_vs_metric",
)


# ---------------------------------------------------------------- helpers

def estado_de(req: dict) -> str:
    """El estado normalizado. Lo que no está en el vocabulario se devuelve como
    `desconocido`: inventarle un estado a un requerimiento es peor que no tenerlo."""
    crudo = str(value(req.get("state")) or "").strip().lower()
    return ESTADOS.get(crudo, "desconocido")


def meses(desde: dt.date, hasta: dt.date) -> int:
    """Meses completos entre dos fechas. Aritmética de calendario, no días / 30."""
    return (hasta.year - desde.year) * 12 + (hasta.month - desde.month) - (hasta.day < desde.day)


def fecha_mas_nueva(items) -> tuple[dt.date | None, dict | None]:
    """La evidencia más reciente y de dónde salió. La más nueva es la que decide si el
    conjunto está viejo: una entrevista de hace tres años no envejece a la de ayer."""
    mejor, cual = None, None
    for it in items or []:
        f = as_date(it.get("source_date")) or as_date(it.get("date"))
        if f and (mejor is None or f > mejor):
            mejor, cual = f, it
    return mejor, cual


def ultimo_medido(serie) -> tuple[dt.date | None, float | None]:
    fecha, valor = None, None
    for punto in serie or []:
        f = as_date(punto.get("date"))
        v = as_number(punto.get("value"))
        if f and v is not None and (fecha is None or f > fecha):
            fecha, valor = f, v
    return fecha, valor


# ---------------------------------------------------------- un requerimiento

def compute_requirement(req: dict, today: dt.date, th: dict) -> dict:
    ident = value(req.get("id")) or "?"
    estado = estado_de(req)
    out = {"id": ident, "title": value(req.get("title")), "state": estado,
           "owner": value(req.get("owner")), "alerts": []}

    def alert(kind, detail):
        out["alerts"].append({"signal": kind, "id": ident, "detail": detail})

    # --- el doliente -----------------------------------------------------
    # Un requerimiento sin doliente es decoración, igual que un riesgo sin doliente. Y
    # un área no es un doliente: «producto lo revisa» no compromete a nadie. Quién
    # decide si eso es persona o área es el modelo, con el skill; aquí se compara.
    dueno = req.get("owner")
    quien = value(dueno)
    clase = (dueno or {}).get("kind") if isinstance(dueno, dict) else None
    if not quien or state_of(dueno) == "not_found":
        alert("requirement_without_owner", {"owner": None})
    elif clase == "area":
        alert("requirement_without_owner", {"owner": quien, "kind": "area"})
    out["owner_kind"] = clase

    # --- los criterios de aceptación -------------------------------------
    # Sin criterio de aceptación nadie puede decir que esto quedó hecho, y la
    # discusión se da al final, cuando ya está construido.
    criterios = [c for c in (req.get("acceptance") or []) if value(c)]
    out["acceptance"] = len(criterios)
    if estado in DECIDIDOS and not criterios:
        alert("requirement_without_acceptance", {"state": estado})

    # --- la evidencia de demanda -----------------------------------------
    # La tesis de Criterio, un paso antes: en un proyecto se contrasta el estado
    # declarado contra la evidencia documental; en un producto, la definición contra
    # la evidencia de demanda. Un requerimiento aceptado sin una sola cita de alguien
    # que lo pidió es una definición que se sostiene sola.
    evidencia = [e for e in (req.get("evidence") or []) if value(e)]
    out["evidence"] = len(evidencia)
    if estado in DECIDIDOS and not evidencia:
        alert("requirement_accepted_without_evidence", {"state": estado})
    else:
        nueva, cual = fecha_mas_nueva(evidencia)
        out["evidence_newest"] = nueva.isoformat() if nueva else None
        if nueva and meses(nueva, today) >= th["evidence_stale_months"]:
            alert("evidence_stale", {"months": meses(nueva, today),
                                     "newest": nueva.isoformat(),
                                     "source": value(cual) if cual else None})

    # --- lo que nadie decide ---------------------------------------------
    dicho = as_date(req.get("stated_on"))
    out["days_since_stated"] = (today - dicho).days if dicho else None
    if estado == "propuesto" and dicho:
        dias = (today - dicho).days
        if dias >= th["undecided_days"]:
            alert("requirement_undecided", {"days": dias, "stated_on": dicho.isoformat()})

    # --- la decisión, y de qué documento salió ---------------------------
    decision = req.get("decision") or {}
    out["decided_on"] = value(decision.get("on"))
    if estado in DECIDIDOS or estado == "descartado":
        fuente = source_of(decision.get("what")) or value(decision.get("source"))
        if not fuente:
            alert("decision_without_source", {"state": estado,
                                              "who": value(decision.get("who"))})

    # --- la traza al proyecto que lo ejecuta -----------------------------
    # Lo que se decidió construir y nadie está construyendo. Es el hallazgo que un
    # gerente de producto descubre en el comité, seis meses después.
    traza = req.get("traces") or {}
    proyecto = value(traza.get("project"))
    out["project"] = proyecto
    if estado in ("aceptado", "en_construccion") and not proyecto:
        alert("requirement_untraced", {"state": estado})

    # --- los supuestos ---------------------------------------------------
    sin_verificar = []
    for s in req.get("assumptions") or []:
        if value(s.get("verified")) in (True, "true", "sí", "si", "yes"):
            continue
        desde = as_date(s.get("stated_on")) or dicho
        dias = (today - desde).days if desde else None
        if dias is None or dias >= th["assumption_unverified_days"]:
            sin_verificar.append({"what": value(s), "days": dias})
    out["assumptions_unverified"] = sin_verificar
    for s in sin_verificar:
        alert("assumption_unverified", s)

    return out


# ------------------------------------------------------------ la definición

def compute_definition(prod: dict, metricas: dict, today: dt.date, th: dict) -> dict:
    definicion = prod.get("definition", {}) or {}
    out = {"problem": value(definicion.get("problem")),
           "who": value(definicion.get("who")),
           "success": value(definicion.get("success")),
           "claims": [], "assumptions_unverified": [], "alerts": []}

    def alert(kind, detail):
        out["alerts"].append({"signal": kind, "detail": detail})

    # Los supuestos de la definición, no los de un requerimiento suelto. Son los que
    # sostienen el producto entero, y son los que nadie vuelve a mirar.
    for s in definicion.get("assumptions") or prod.get("assumptions") or []:
        if value(s.get("verified")) in (True, "true", "sí", "si", "yes"):
            continue
        desde = as_date(s.get("stated_on"))
        dias = (today - desde).days if desde else None
        if dias is None or dias >= th["assumption_unverified_days"]:
            item = {"what": value(s), "days": dias}
            out["assumptions_unverified"].append(item)
            alert("assumption_unverified", item)

    # Lo que el negocio declara contra lo que la métrica mide. Las dos con su fuente y
    # su fecha: «el negocio y los datos no coinciden» no le permite a nadie hacer nada,
    # y «el caso de negocio de marzo dice 250.000 y la serie de septiembre mide
    # 180.000» sí.
    for c in definicion.get("claims") or []:
        nombre = value(c.get("metric"))
        declarado = as_number(c.get("declared"))
        fila = {"metric": nombre, "declared": declarado,
                "source": source_of(c.get("declared")) or value(c.get("source")),
                "source_date": value(c.get("source_date")),
                "measured": None, "measured_on": None, "gap_pct": None}
        serie = (metricas.get(nombre) or {}).get("series")
        fecha, medido = ultimo_medido(serie)
        if declarado is not None and medido is not None and declarado:
            fila["measured"], fila["measured_on"] = medido, fecha.isoformat() if fecha else None
            fila["measured_source"] = (metricas.get(nombre) or {}).get("source")
            fila["gap_pct"] = round(abs(medido - declarado) / abs(declarado) * 100, 1)
            if fila["gap_pct"] >= th["claim_gap_pct"]:
                alert("claim_vs_metric", {
                    "metric": nombre, "declared": declarado, "measured": medido,
                    "gap_pct": fila["gap_pct"],
                    "direction": "declarado por encima" if declarado > medido else "declarado por debajo",
                    "declared_source": fila["source"], "declared_date": fila["source_date"],
                    "measured_source": fila["measured_source"], "measured_on": fila["measured_on"]})
        out["claims"].append(fila)

    return out


# ---------------------------------------------------------- las trazas reales

def confirmar_trazas(filas: list, producto: str, fichas: Path | None) -> list:
    """Cruza cada traza contra la ficha del proyecto que dice ejecutarla.

    Alba no le cree a su propio registro: el registro dice «REQ-014 lo ejecuta
    PRY-101», y la ficha de PRY-101 dice qué producto ejecuta. Si no coinciden, alguien
    está mirando un proyecto que no es el suyo, y eso no se descubre solo.
    """
    encontradas = {}
    if fichas and fichas.is_dir():
        for f in sorted(fichas.glob("*.json")):
            try:
                rec = json.loads(f.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            ident = rec.get("identity", {}) or {}
            codigo = value(ident.get("code"))
            if codigo:
                encontradas[codigo] = {"product": value(ident.get("product")),
                                       "source": str(f.name)}
    nuevas = []
    for fila in filas:
        proyecto = fila.get("project")
        if not proyecto:
            continue
        ficha = encontradas.get(proyecto)
        if ficha is None:
            detalle = {"project": proyecto, "why": "no hay ficha de ese proyecto"}
        elif not ficha["product"]:
            detalle = {"project": proyecto, "why": "la ficha del proyecto no dice qué producto ejecuta",
                       "source": ficha["source"]}
        elif ficha["product"] != producto:
            detalle = {"project": proyecto, "why": "la ficha del proyecto dice otro producto",
                       "says": ficha["product"], "source": ficha["source"]}
        else:
            fila["trace_confirmed"] = True
            continue
        fila["trace_confirmed"] = False
        alerta = {"signal": "trace_not_confirmed", "id": fila["id"], "detail": detalle}
        fila["alerts"].append(alerta)
        nuevas.append(alerta)
    return nuevas


# ------------------------------------------------------------------ compute

def compute(state: Path, today: dt.date, th: dict, fichas: Path | None = None) -> dict:
    prod_path = state / "producto.json"
    prod = json.loads(prod_path.read_text(encoding="utf-8")) if prod_path.exists() else {}
    ident = prod.get("identity", {}) or {}
    codigo = value(ident.get("code")) or "?"

    metricas = {}
    for m in sorted((state / "metrics").glob("*.json")) if (state / "metrics").is_dir() else []:
        try:
            dato = json.loads(m.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        metricas[value(dato.get("metric")) or m.stem] = dato

    filas, alertas = [], []
    carpeta = state / "requirements"
    for f in sorted(carpeta.glob("*.json")) if carpeta.is_dir() else []:
        fila = compute_requirement(json.loads(f.read_text(encoding="utf-8")), today, th)
        filas.append(fila)
        alertas.extend(fila["alerts"])

    alertas.extend(confirmar_trazas(filas, codigo, fichas))

    definicion = compute_definition(prod, metricas, today, th)
    alertas.extend(definicion["alerts"])

    por_estado = {}
    for fila in filas:
        por_estado[fila["state"]] = por_estado.get(fila["state"], 0) + 1
    decididos = [f for f in filas if f["state"] in DECIDIDOS]
    con_evidencia = [f for f in decididos if f["evidence"]]
    trazados = [f for f in decididos if f.get("project")]

    por_senal = {}
    for a in alertas:
        por_senal[a["signal"]] = por_senal.get(a["signal"], 0) + 1

    # Los campos de la definición que no están dichos en ninguna parte. Un producto sin
    # criterio de éxito declarado no se puede cerrar: el cierre se juzga contra él,
    # meses después, y no haberlo escrito es la razón por la que nadie cierra nada.
    sin_dato = [nombre for nombre, campo in
                (("problem", definicion["problem"]), ("who", definicion["who"]),
                 ("success", definicion["success"]),
                 ("authority", value(ident.get("authority"))))
                if not campo]

    return {
        "as_of": today.isoformat(),
        "product": {"code": codigo, "name": value(ident.get("name")),
                    "manager": value(ident.get("manager")),
                    "authority": value(ident.get("authority"))},
        "totals": {
            "requirements": len(filas),
            "by_state": por_estado,
            "decided": len(decididos),
            "with_evidence": len(con_evidencia),
            "traced": len(trazados),
            "with_evidence_pct": pct(len(con_evidencia), len(decididos)),
            "traced_pct": pct(len(trazados), len(decididos)),
        },
        "definition": definicion,
        "requirements": filas,
        "alerts": alertas,
        "by_signal": por_senal,
        "unknown": sin_dato,
    }


# ----------------------------------------------------------- estado en disco

def init(state: Path) -> dict:
    for sub in ("requirements", "metrics", "snapshots"):
        (state / sub).mkdir(parents=True, exist_ok=True)
    prod = state / "producto.json"
    if not prod.exists():
        prod.write_text(json.dumps({
            "identity": {"code": None, "name": None, "manager": None, "authority": None},
            "definition": {"problem": None, "who": None, "success": None,
                           "claims": [], "assumptions": []},
            "activity": {"last_document_date": None},
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"state": str(state), "created": True}


def snapshot(state: Path, today: dt.date) -> Path:
    destino = state / "snapshots" / f"{today.isoformat()}.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    datos = compute(state, today, DEFAULT_THRESHOLDS)
    destino.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    return destino


def diff(state: Path, against: Path | None) -> dict:
    """Qué cambió desde la corrida anterior. Es el eje de cualquier informe útil: lo
    que sigue igual y está bien no es noticia, y lo que sigue igual y está mal lleva
    los días que lleva."""
    carpeta = state / "snapshots"
    previos = sorted(carpeta.glob("*.json")) if carpeta.is_dir() else []
    base = against or (previos[-1] if previos else None)
    if base is None:
        return {"against": None, "note": "no hay corrida anterior con la que comparar"}
    antes = json.loads(Path(base).read_text(encoding="utf-8"))
    ahora = compute(state, dt.date.today(), DEFAULT_THRESHOLDS)

    def clave(a):
        return (a["signal"], a.get("id"), json.dumps(a.get("detail"), sort_keys=True))

    antes_set = {clave(a) for a in antes.get("alerts", [])}
    ahora_set = {clave(a) for a in ahora.get("alerts", [])}
    ids_antes = {r["id"] for r in antes.get("requirements", [])}
    ids_ahora = {r["id"] for r in ahora.get("requirements", [])}
    estados_antes = {r["id"]: r["state"] for r in antes.get("requirements", [])}
    return {
        "against": str(base),
        "new_alerts": [a for a in ahora.get("alerts", []) if clave(a) not in antes_set],
        "closed_alerts": [a for a in antes.get("alerts", []) if clave(a) not in ahora_set],
        "new_requirements": sorted(ids_ahora - ids_antes),
        "gone_requirements": sorted(ids_antes - ids_ahora),
        "state_changed": [{"id": r["id"], "from": estados_antes[r["id"]], "to": r["state"]}
                          for r in ahora.get("requirements", [])
                          if r["id"] in estados_antes and estados_antes[r["id"]] != r["state"]],
    }


def check_config(config: Path) -> dict:
    """Lo mínimo que este agente necesita para no adivinar. Falta algo, se dice cuál:
    un agente que arranca con la configuración a medias produce un informe a medias y
    nadie sabe por qué."""
    if not config.exists():
        return {"ok": False, "missing": ["el archivo entero"], "path": str(config)}
    try:
        cfg = json.loads(config.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {"ok": False, "error": f"JSON inválido: {e}", "path": str(config)}
    faltan = [c for c in ("product", "paths", "terms_accepted") if c not in cfg]
    rutas = cfg.get("paths", {}) or {}
    faltan += [f"paths.{c}" for c in ("documents", "state") if c not in rutas]
    return {"ok": not faltan, "missing": faltan, "path": str(config),
            "thresholds": {**DEFAULT_THRESHOLDS, **(cfg.get("thresholds") or {})}}


def load_thresholds(config: Path | None) -> dict:
    th = dict(DEFAULT_THRESHOLDS)
    if config and config.exists():
        try:
            th.update(json.loads(config.read_text(encoding="utf-8")).get("thresholds") or {})
        except json.JSONDecodeError:
            pass
    return th


# ----------------------------------------------------------------- selftest

def selftest() -> int:
    import tempfile

    fallas = []

    def ok(condicion, que):
        if not condicion:
            fallas.append(que)
        print(f"  {'ok  ' if condicion else 'FALLA'} {que}")

    hoy = dt.date(2026, 11, 20)
    th = DEFAULT_THRESHOLDS

    print("\nEl estado de un requerimiento")
    ok(estado_de({"state": "Accepted"}) == "aceptado", "el estado se normaliza entre idiomas")
    ok(estado_de({"state": "en construcción"}) == "en_construccion", "y entre grafías")
    ok(estado_de({"state": "priorizado"}) == "desconocido",
       "un estado que no está en el vocabulario no se inventa")
    ok(estado_de({}) == "desconocido", "sin estado, desconocido")

    print("\nAritmética de calendario")
    ok(meses(dt.date(2025, 11, 21), hoy) == 11, "once meses no son doce")
    ok(meses(dt.date(2025, 11, 20), hoy) == 12, "el día exacto sí cumple")
    ok(meses(dt.date(2026, 11, 1), hoy) == 0, "el mismo mes es cero")

    print("\nEl doliente")
    r = compute_requirement({"id": "R1", "state": "aceptado"}, hoy, th)
    ok(any(a["signal"] == "requirement_without_owner" for a in r["alerts"]),
       "sin doliente, señal")
    r = compute_requirement({"id": "R2", "state": "aceptado",
                             "owner": {"value": "Producto", "kind": "area"}}, hoy, th)
    ok(any(a["signal"] == "requirement_without_owner" for a in r["alerts"]),
       "un área no es un doliente")
    r = compute_requirement({"id": "R3", "state": "aceptado",
                             "owner": {"value": "Marcela Ruiz", "kind": "person"}}, hoy, th)
    ok(not any(a["signal"] == "requirement_without_owner" for a in r["alerts"]),
       "una persona sí")

    print("\nCriterio de aceptación y evidencia")
    r = compute_requirement({"id": "R4", "state": "aceptado"}, hoy, th)
    ok(any(a["signal"] == "requirement_without_acceptance" for a in r["alerts"]),
       "aceptado sin criterio de aceptación, señal")
    r = compute_requirement({"id": "R5", "state": "propuesto"}, hoy, th)
    ok(not any(a["signal"] == "requirement_without_acceptance" for a in r["alerts"]),
       "propuesto sin criterio todavía no: nadie dijo que se hace")
    ok(not any(a["signal"] == "requirement_accepted_without_evidence" for a in r["alerts"]),
       "y tampoco se le exige evidencia de demanda")
    r = compute_requirement({"id": "R6", "state": "aceptado",
                             "acceptance": [{"value": "la transacción se confirma en 3 s"}]},
                            hoy, th)
    ok(any(a["signal"] == "requirement_accepted_without_evidence" for a in r["alerts"]),
       "aceptado sin una sola cita de quien lo pidió, señal")

    print("\nLa evidencia envejece")
    r = compute_requirement({"id": "R7", "state": "aceptado",
                             "acceptance": [{"value": "x"}],
                             "evidence": [{"value": "entrevista con 8 comercios",
                                           "source_date": "2025-06-10"},
                                          {"value": "ticket 4471", "source_date": "2024-01-08"}]},
                            hoy, th)
    ok(r["evidence_newest"] == "2025-06-10", "la más nueva es la que cuenta")
    ok(any(a["signal"] == "evidence_stale" for a in r["alerts"]),
       "diecisiete meses es evidencia vieja")
    r = compute_requirement({"id": "R8", "state": "aceptado", "acceptance": [{"value": "x"}],
                             "evidence": [{"value": "entrevista", "source_date": "2026-09-01"}]},
                            hoy, th)
    ok(not any(a["signal"] == "evidence_stale" for a in r["alerts"]),
       "dos meses no lo es")

    print("\nLo que nadie decide")
    r = compute_requirement({"id": "R9", "state": "propuesto", "stated_on": "2026-05-02"}, hoy, th)
    ok(any(a["signal"] == "requirement_undecided" for a in r["alerts"]),
       "propuesto hace seis meses es una decisión que no se toma")
    r = compute_requirement({"id": "R10", "state": "propuesto", "stated_on": "2026-11-01"}, hoy, th)
    ok(not any(a["signal"] == "requirement_undecided" for a in r["alerts"]),
       "diecinueve días todavía no")
    r = compute_requirement({"id": "R11", "state": "aceptado", "acceptance": [{"value": "x"}],
                             "evidence": [{"value": "e", "source_date": "2026-09-01"}],
                             "stated_on": "2026-01-02"}, hoy, th)
    ok(not any(a["signal"] == "requirement_undecided" for a in r["alerts"]),
       "lo ya decidido no lleva días sin decidirse, por viejo que sea")

    print("\nLa decisión y su documento")
    r = compute_requirement({"id": "R12", "state": "descartado",
                             "decision": {"what": "no se hace", "who": "Marcela"}}, hoy, th)
    ok(any(a["signal"] == "decision_without_source" for a in r["alerts"]),
       "una decisión sin documento que la respalde, señal")
    r = compute_requirement({"id": "R13", "state": "descartado",
                             "decision": {"what": {"value": "no se hace",
                                                   "source": "comite-2026-10-08.md"}}}, hoy, th)
    ok(not any(a["signal"] == "decision_without_source" for a in r["alerts"]),
       "con cita, no")

    print("\nLo decidido que nadie está construyendo")
    r = compute_requirement({"id": "R14", "state": "aceptado", "acceptance": [{"value": "x"}],
                             "evidence": [{"value": "e", "source_date": "2026-09-01"}]}, hoy, th)
    ok(any(a["signal"] == "requirement_untraced" for a in r["alerts"]),
       "aceptado y sin proyecto que lo ejecute, señal")
    r = compute_requirement({"id": "R15", "state": "entregado", "acceptance": [{"value": "x"}],
                             "evidence": [{"value": "e", "source_date": "2026-09-01"}]}, hoy, th)
    ok(not any(a["signal"] == "requirement_untraced" for a in r["alerts"]),
       "entregado sin traza es historia, no hallazgo")

    print("\nSupuestos sin verificar")
    r = compute_requirement({"id": "R16", "state": "propuesto", "stated_on": "2026-11-18",
                             "assumptions": [{"value": "el comercio tiene datos",
                                              "verified": False, "stated_on": "2026-01-10"},
                                             {"value": "el switch responde en 2 s",
                                              "verified": True, "stated_on": "2026-01-10"}]},
                            hoy, th)
    ok(len(r["assumptions_unverified"]) == 1, "solo cuenta el que nadie verificó")

    print("\nLa definición contra la métrica")
    prod = {"identity": {"code": "PRD-QR", "name": "Pagos QR", "authority": "Comité de producto"},
            "definition": {"problem": "p", "who": "q", "success": "s",
                           "claims": [{"metric": "tx_mensuales", "declared": 250000,
                                       "source": "caso-negocio-2026-03.md",
                                       "source_date": "2026-03-04"},
                                      {"metric": "comercios_activos", "declared": 1200,
                                       "source": "caso-negocio-2026-03.md",
                                       "source_date": "2026-03-04"}]}}
    metricas = {"tx_mensuales": {"metric": "tx_mensuales", "source": "tablero-transaccional",
                                 "series": [{"date": "2026-08-01", "value": 150000},
                                            {"date": "2026-09-01", "value": 180000}]},
                "comercios_activos": {"metric": "comercios_activos", "source": "crm",
                                      "series": [{"date": "2026-09-01", "value": 1150}]}}
    d = compute_definition(prod, metricas, hoy, th)
    tx = next(c for c in d["claims"] if c["metric"] == "tx_mensuales")
    ok(tx["measured"] == 180000, "se compara contra el punto más reciente de la serie")
    ok(tx["gap_pct"] == 28.0, "la diferencia es 28%")
    ok(any(a["signal"] == "claim_vs_metric" for a in d["alerts"]), "28% es contradicción")
    alerta = next(a for a in d["alerts"] if a["signal"] == "claim_vs_metric")
    ok(alerta["detail"]["declared_source"] and alerta["detail"]["measured_source"],
       "y la señal lleva las dos fuentes, que es lo que la hace servir")
    ok(alerta["detail"]["measured_on"] == "2026-09-01", "y las dos fechas")
    ca = next(c for c in d["claims"] if c["metric"] == "comercios_activos")
    ok(ca["gap_pct"] == 4.2 and not any(a["detail"].get("metric") == "comercios_activos"
                                        for a in d["alerts"]),
       "4,2% es imprecisión, no contradicción")

    print("\nLa traza contra la ficha del proyecto")
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        fichas = Path(tmp) / "fichas"
        init(estado)
        fichas.mkdir()
        (estado / "producto.json").write_text(json.dumps(prod, ensure_ascii=False),
                                              encoding="utf-8")
        (estado / "metrics" / "tx.json").write_text(
            json.dumps(metricas["tx_mensuales"], ensure_ascii=False), encoding="utf-8")
        base = {"state": "aceptado", "acceptance": [{"value": "x"}],
                "evidence": [{"value": "e", "source_date": "2026-09-01"}],
                "owner": {"value": "Marcela Ruiz", "kind": "person"},
                "decision": {"what": {"value": "se hace", "source": "comite.md"}}}
        for ident, proyecto in (("REQ-001", "PRY-101"), ("REQ-002", "PRY-777"),
                                ("REQ-003", "PRY-102")):
            (estado / "requirements" / f"{ident}.json").write_text(
                json.dumps({**base, "id": ident, "traces": {"project": proyecto}},
                           ensure_ascii=False), encoding="utf-8")
        (fichas / "PRY-101.json").write_text(json.dumps(
            {"identity": {"code": "PRY-101", "product": "PRD-QR"}}, ensure_ascii=False),
            encoding="utf-8")
        (fichas / "PRY-102.json").write_text(json.dumps(
            {"identity": {"code": "PRY-102", "product": "PRD-PROVEEDORES"}}, ensure_ascii=False),
            encoding="utf-8")

        r = compute(estado, hoy, th, fichas)
        por = {f["id"]: f for f in r["requirements"]}
        ok(por["REQ-001"].get("trace_confirmed") is True,
           "la ficha del proyecto nombra este producto: traza confirmada")
        ok(por["REQ-002"].get("trace_confirmed") is False,
           "un proyecto sin ficha no confirma nada")
        ok(any(a["signal"] == "trace_not_confirmed" and a["id"] == "REQ-003"
               for a in r["alerts"]),
           "y una ficha que dice otro producto es el hallazgo que nadie encuentra solo")
        dicho = next(a for a in r["alerts"]
                     if a["signal"] == "trace_not_confirmed" and a["id"] == "REQ-003")
        ok(dicho["detail"].get("says") == "PRD-PROVEEDORES",
           "la señal dice qué producto dice la otra ficha")
        ok(r["totals"]["traced"] == 3 and r["totals"]["with_evidence_pct"] == 100.0,
           "los totales salen de los registros, no de una cuenta a mano")
        ok(r["unknown"] == [], "la definición de la prueba no tiene huecos")

        print("\nSin fichas a la vista")
        r2 = compute(estado, hoy, th, None)
        ok(all(f.get("trace_confirmed") is False for f in r2["requirements"]),
           "sin la carpeta de fichas, ninguna traza se da por confirmada")

        print("\nQué cambió desde la corrida anterior")
        snapshot(estado, hoy)
        (estado / "requirements" / "REQ-004.json").write_text(
            json.dumps({**base, "id": "REQ-004", "state": "propuesto",
                        "stated_on": "2026-01-05"}, ensure_ascii=False), encoding="utf-8")
        (estado / "requirements" / "REQ-001.json").write_text(
            json.dumps({**base, "id": "REQ-001", "state": "entregado",
                        "traces": {"project": "PRY-101"}}, ensure_ascii=False), encoding="utf-8")
        d2 = diff(estado, None)
        ok("REQ-004" in d2["new_requirements"], "un requerimiento nuevo aparece")
        ok(any(c["id"] == "REQ-001" and c["to"] == "entregado" for c in d2["state_changed"]),
           "y un cambio de estado se ve con el de antes y el de ahora")

        print("\nLa configuración")
        cfg = Path(tmp) / "config.json"
        cfg.write_text(json.dumps({"product": "PRD-QR"}), encoding="utf-8")
        res = check_config(cfg)
        ok(not res["ok"] and "paths" in res["missing"], "dice qué falta, no solo que falta")
        cfg.write_text(json.dumps({"product": "PRD-QR", "terms_accepted": {"version": "1.0"},
                                   "paths": {"documents": "d", "state": "e"},
                                   "thresholds": {"undecided_days": 30}}), encoding="utf-8")
        res = check_config(cfg)
        ok(res["ok"] and res["thresholds"]["undecided_days"] == 30,
           "y un umbral de la organización pisa el de por defecto")

    print("\nEl inventario de señales")
    # Se leen los dos sitios donde nace una señal: el atajo `alert(...)` de cada
    # bloque, y el diccionario que `confirmar_trazas` arma a mano porque su alerta
    # cuelga de dos listas a la vez. Una señal nueva que no entre en SENALES rompe
    # aquí, y una declarada que nadie emite también.
    import re as _re
    fuente = Path(__file__).read_text(encoding="utf-8")
    emitidas = set(_re.findall(r'alert\("([a-z_]+)"', fuente))
    emitidas |= set(_re.findall(r'"signal": "([a-z_]+)"', fuente))
    ok(emitidas == set(SENALES),
       f"las {len(SENALES)} señales declaradas son las que se emiten")
    ok(all(s in fuente.split("SENALES = (")[1].split(")")[0] for s in emitidas),
       "y ninguna se emite sin estar declarada arriba")

    print(f"\n{'todo en verde' if not fallas else f'{len(fallas)} FALLAS'}")
    return 0 if not fallas else 1


# --------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Criterio Product — aritmética sobre el registro de requerimiento.")
    ap.add_argument("action", choices=["init", "config", "compute", "snapshot", "diff",
                                       "selftest"])
    ap.add_argument("--state", type=Path)
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--fichas", type=Path, default=None,
                    help="carpeta con las fichas de los proyectos, para confirmar las trazas")
    ap.add_argument("--against", type=Path, default=None)
    ap.add_argument("--today", default=None)
    args = ap.parse_args()

    if args.action == "selftest":
        return selftest()

    if args.action == "config":
        if not args.config:
            ap.error("--config es obligatorio")
        res = check_config(args.config)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res["ok"] else 1

    if not args.state:
        ap.error("--state es obligatorio")
    if args.action == "init":
        print(json.dumps(init(args.state), ensure_ascii=False, indent=2))
        return 0

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    if args.action == "compute":
        print(json.dumps(compute(args.state, today, load_thresholds(args.config), args.fichas),
                         ensure_ascii=False, indent=2))
    elif args.action == "snapshot":
        print(json.dumps({"written": str(snapshot(args.state, today))}, ensure_ascii=False))
    elif args.action == "diff":
        print(json.dumps(diff(args.state, args.against), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
