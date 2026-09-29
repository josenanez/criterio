#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-portfolio/scripts/portafolio.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
"""Criterio PMO — the arithmetic layer.

The model extracts; this computes. Reading a date off a page is reading.
Subtracting days, projecting variance and adding committed against executed is
arithmetic, and arithmetic belongs here, where it is deterministic and testable.

Usage:
    python3 portafolio.py init     --state <dir>
    python3 portafolio.py config   --config <file>
    python3 portafolio.py due      --state <dir> --config <file>
    python3 portafolio.py ran      --state <dir> --what sweep
    python3 portafolio.py index    --state <dir> --docs <dir>
    python3 portafolio.py compute  --state <dir> [--config <file>] [--today YYYY-MM-DD]
    python3 portafolio.py snapshot --state <dir> [--today YYYY-MM-DD]
    python3 portafolio.py diff     --state <dir> [--against <snapshot.json>]
    python3 portafolio.py selftest

Standard library only.

Records live in <state>/records/<code>.json and follow the shape documented in
../skills/project-record/references/schema.yaml. Every field is either a plain
value or an object {value, source, source_date, state}; this script reads the
value and never invents one.

Output is JSON on stdout. Nothing here decides what to report — it reports what
crossed a threshold. What a number means is in the skills.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

DEFAULT_THRESHOLDS = {
    "silent_days": 15,
    "variance_time_pct": 10,
    # Puntos de diferencia entre el avance que el gerente declara y el que sostiene su
    # propio cronograma. Por debajo es redondeo; por encima, los dos documentos no
    # pueden ser ciertos a la vez.
    "progress_vs_plan_points": 25,
    # Hitos mínimos para que la fracción pueda contradecir un porcentaje. Con uno solo, el
    # plan únicamente sostiene 0% o 100%, así que cualquier cifra intermedia dispararía:
    # sería un falso positivo garantizado en todo proyecto con pocos hitos.
    "progress_vs_plan_min_milestones": 3,
    "variance_cost_pct": 10,
    "committed_pct": 90,
    "stale_field_months": 12,
    "declaration_stale_days": 30,
    "rebaseline_tolerance_days": 0,
    "reschedules_to_flag": 3,
}

# Lo que se puede leer como texto sin instalar nada. Para el resto, el hash de bytes
# es lo único disponible, y un reguardado se ve como un cambio: se declara así en la
# salida en vez de fingir precisión.
TEXTO_PLANO = (".md", ".txt", ".csv", ".tsv", ".json", ".yaml", ".yml", ".html", ".xml")
IGNORAR = (".DS_Store", "Thumbs.db")

# Declared status, as the manager reports it. The rank only orders the
# vocabulary so the code can ask "is this light green". It is not a severity
# score and nothing else is computed from it.
STATUS_RANK = {
    "verde": 0, "green": 0,
    "amarillo": 1, "yellow": 1, "amber": 1, "en riesgo": 1, "at risk": 1,
    "rojo": 2, "red": 2,
}

# Los roles de gobierno. Cuando uno de estos campos queda en conflicto, el hallazgo no
# es un defecto de la ficha: es un cambio de gobierno. Nadie reexpide el acta de
# constitución porque se fue el patrocinador — aparece en un correo o en una minuta —, y
# un proyecto con tres patrocinadores en dieciocho meses explica más que cualquier
# análisis de causa raíz. Por eso se reporta aparte de `contradiction`.
GOVERNANCE_FIELDS = ("identity.sponsor", "identity.manager", "identity.committee")

# Los campos que el agente del proyecto y el del portafolio tienen **los dos** por qué
# leer. Contrastar todo produciría una avalancha de diferencias de alcance —el agente
# del proyecto lee minutas semana a semana y el de portafolio no— y nadie volvería a
# abrir el informe. Son los que envejecen peor y los que una PMO usa para decidir.
CAMPOS_CONTRASTADOS = (
    "identity.sponsor", "identity.manager", "identity.committee", "identity.product",
    "plan.end_date", "money.approved", "declared.status", "declared.as_of",
)

# The signals a status light is supposed to account for. `contradiction` is
# deliberately out: it is a defect of the record, not of the project, and
# mixing the two weakens the finding.
# `milestone_met_without_evidence` pertenece a esta lista por la misma razón que
# `milestone_overdue`: un hito cuya fecha pasó y que nadie probó es evidencia contra el
# verde, y que alguien lo haya declarado cumplido no lo explica — lo empeora. Salió de
# `milestone_overdue` al partirse en dos señales, y partir una señal sin traerla aquí
# debilitó en silencio el contraste contra la declaración.
EVIDENCE_SIGNALS = (
    "silent", "variance_time", "variance_cost", "milestone_overdue",
    "milestone_met_without_evidence", "progress_vs_plan",
    "commitment_overdue", "commitment_rescheduled", "budget_committed",
    "vendor_deliverable_late", "vendor_invoiced_without_delivery",
    "vendor_invoiced_over_accepted", "rebaseline_unauthorized", "governance_change",
)


# ---------------------------------------------------------------- helpers

def value(field):
    """A field is either a bare value or {value, source, source_date, state}."""
    if isinstance(field, dict) and "value" in field:
        return field["value"]
    return field


def state_of(field) -> str:
    if isinstance(field, dict):
        return field.get("state", "found")
    return "found"


def source_of(field):
    if isinstance(field, dict):
        return field.get("source")
    return None


def as_date(raw):
    raw = value(raw)
    if not raw:
        return None
    try:
        return dt.date.fromisoformat(str(raw)[:10])
    except ValueError:
        return None


def as_number(raw):
    raw = value(raw)
    if raw in (None, ""):
        return None
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def hash_bytes(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for trozo in iter(lambda: f.read(65536), b""):
            h.update(trozo)
    return h.hexdigest()


def hash_texto(ruta: Path):
    """Hash del texto extraído, o None si el formato no se puede leer sin dependencias.

    Existe por una razón económica: un Word reguardado o un Excel que recalcula al
    abrirlo cambian el hash de bytes sin cambiar una palabra, y cada falso positivo
    cuesta una relectura del documento, que es el único paso caro del sistema.
    """
    if ruta.suffix.lower() not in TEXTO_PLANO:
        return None
    try:
        texto = ruta.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    return hashlib.sha256(" ".join(texto.split()).encode("utf-8")).hexdigest()


def as_days(raw):
    """Days out of a field that may be a number or text like "30 días".

    Weeks convert exactly. Months do not: a month is not a fixed number of
    days, so it returns None and the caller reports the field as unreadable
    instead of guessing.
    """
    raw = value(raw)
    if raw in (None, ""):
        return None
    if isinstance(raw, bool):
        return None
    if isinstance(raw, (int, float)):
        return int(raw)
    text = str(raw).lower()
    m = re.search(r"-?\d+", text)
    if not m:
        return None
    n = int(m.group())
    if "sem" in text or "week" in text:
        return n * 7
    if "mes" in text or "month" in text or "año" in text or "year" in text:
        return None
    return n


def pct(part, whole):
    if part is None or not whole:
        return None
    return round(part / whole * 100, 1)


def walk_fields(node, path=""):
    """Yield (path, field) for every {value,...} object in the record.

    `state` is optional here, exactly as it is for value() and state_of().
    Requiring it made every field written without one invisible: it dropped out
    of the run-to-run diff, out of conflict detection and out of the staleness
    check, without a word. A record that loses change detection because a key
    was omitted is the silent skip this plugin exists to refuse.
    """
    if isinstance(node, dict):
        if "value" in node:
            yield path, node
            return
        for k, v in node.items():
            yield from walk_fields(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_fields(v, f"{path}[{i}]")


# ---------------------------------------------------------------- compute

def compute_record(rec: dict, today: dt.date, th: dict) -> dict:
    ident = rec.get("identity", {}) or {}
    code = value(ident.get("code")) or "?"
    out = {"code": code, "name": value(ident.get("name")),
           "product": value(ident.get("product")),
           "authority": value(ident.get("authority")),
           "alerts": []}

    def alert(kind, detail):
        out["alerts"].append({"signal": kind, "detail": detail})

    # --- silence -------------------------------------------------------
    activity = rec.get("activity", {}) or {}
    last_doc = as_date(activity.get("last_document_date"))
    out["days_silent"] = (today - last_doc).days if last_doc else None
    if out["days_silent"] is not None and out["days_silent"] >= th["silent_days"]:
        alert("silent", {"days": out["days_silent"], "since": last_doc.isoformat()})

    # --- schedule ------------------------------------------------------
    plan = rec.get("plan", {}) or {}
    baselines = plan.get("baseline") or []
    current_end = as_date(plan.get("end_date"))
    original_end = as_date(baselines[0].get("end_date")) if baselines else None
    approved_end = as_date(baselines[-1].get("end_date")) if baselines else None

    out["replans"] = max(len(baselines) - 1, 0)
    out["end_date"] = current_end.isoformat() if current_end else None
    out["slip_vs_original_days"] = (current_end - original_end).days if current_end and original_end else None
    out["slip_vs_current_days"] = (current_end - approved_end).days if current_end and approved_end else None
    out["has_baseline"] = bool(baselines)

    start = as_date(plan.get("start_date"))
    if out["slip_vs_original_days"] and start and original_end and original_end > start:
        span = (original_end - start).days
        out["slip_vs_original_pct"] = pct(out["slip_vs_original_days"], span)
        if out["slip_vs_original_pct"] >= th["variance_time_pct"]:
            alert("variance_time", {"days": out["slip_vs_original_days"],
                                    "pct": out["slip_vs_original_pct"],
                                    "against": "original"})
    else:
        out["slip_vs_original_pct"] = None

    # --- milestones ----------------------------------------------------
    # Dos formas de que un hito vencido no tenga prueba, y son señales distintas
    # porque piden acciones distintas.
    #
    # El vencido y abierto lo ve cualquiera que mire el cronograma. El vencido y
    # marcado «cerrado» sin un documento que lo sustente no lo ve nadie, y es el caso
    # común: quien cierra un hito lo marca cerrado, y ahí se acaba el rastro. Es
    # exactamente lo que el README promete —«el hito cuya fecha pasó y no hay un solo
    # documento que pruebe que se cumplió»— y durante un tiempo el código no lo hizo.
    overdue, sin_prueba = [], []
    for m in plan.get("milestones") or []:
        due = as_date(m.get("current_date")) or as_date(m.get("baseline_date"))
        st = value(m.get("state"))
        evidence = value(m.get("evidence"))
        if not (due and due < today) or evidence:
            continue
        fila = {"name": value(m.get("name")), "due": due.isoformat(),
                "days": (today - due).days}
        (sin_prueba if st == "met" else overdue).append(fila)
    out["milestones_overdue"] = overdue
    out["milestones_met_without_evidence"] = sin_prueba

    # --- el avance declarado contra el cronograma del mismo proyecto ----
    # `contradiction` es el mismo campo dicho distinto en dos documentos. Esto es otra
    # cosa: dos campos distintos cuya combinación no puede ser cierta. Un proyecto con
    # los cinco hitos marcados cerrados —incluida la salida a producción— declarando 28%
    # de avance no tiene un dato desactualizado: tiene dos documentos que se desmienten.
    #
    # Salió de correr el agente sobre cincuenta proyectos: encontró los ocho casos y los
    # puso en una sección inventada, porque con la definición anterior de `contradiction`
    # no cabían en ninguna. El informe decía «sin contradicciones» y listaba ocho. Es
    # aritmética, así que le corresponde al código y no a la lectura.
    hitos = plan.get("milestones") or []
    # `pct` ya es una función en este módulo; el avance declarado va con su propio nombre.
    avance = as_number(declarado_pct(rec))
    if len(hitos) >= th["progress_vs_plan_min_milestones"] and avance is not None:
        cerrados = sum(1 for m in hitos if value(m.get("state")) == "met")
        sostiene = round(100 * cerrados / len(hitos))
        brecha = sostiene - avance
        out["progress_vs_plan"] = {"declared_pct": avance, "plan_supports_pct": sostiene,
                                   "milestones_met": cerrados, "milestones": len(hitos),
                                   "gap_points": brecha}
        if abs(brecha) >= th["progress_vs_plan_points"]:
            alert("progress_vs_plan", dict(out["progress_vs_plan"],
                                           direction="behind" if brecha > 0 else "ahead"))
    for m in overdue:
        alert("milestone_overdue", m)
    for m in sin_prueba:
        alert("milestone_met_without_evidence", dict(m, declared_state="met"))

    # --- money ---------------------------------------------------------
    money = rec.get("money", {}) or {}
    approved = as_number(money.get("approved"))
    committed = as_number(money.get("committed"))
    executed = as_number(money.get("executed"))
    projection = as_number(money.get("projection"))

    out["money"] = {
        "currency": value(money.get("currency")),
        "approved": approved, "committed": committed,
        "executed": executed, "projection": projection,
        "available_real": round(approved - committed, 2) if approved is not None and committed is not None else None,
        "pct_executed": pct(executed, approved),
        "pct_committed": pct(committed, approved),
    }
    if out["money"]["pct_committed"] is not None and out["money"]["pct_committed"] >= th["committed_pct"]:
        alert("budget_committed", {"pct": out["money"]["pct_committed"],
                                   "available_real": out["money"]["available_real"]})
    if projection is not None and approved:
        over = round((projection - approved) / approved * 100, 1)
        out["money"]["projection_over_pct"] = over
        if over >= th["variance_cost_pct"]:
            alert("variance_cost", {"pct": over, "projection": projection, "approved": approved})

    # --- commitments ---------------------------------------------------
    late, sin_fecha, reprogramados = [], [], []
    for c in rec.get("commitments") or []:
        due = as_date(c.get("due_date"))
        st = value(c.get("state"))
        quien = value(c.get("who"))
        que = value(c.get("what"))
        fuente = source_of(c.get("what")) or value(c.get("source"))
        if due is None:
            # El skill registra un compromiso sin fecha como `no_declarada`. No puede
            # estar vencido, y por eso mismo desaparecía del informe. Un compromiso
            # que nadie fechó es un hallazgo, no un vacío.
            sin_fecha.append({"who": quien, "what": que, "source": fuente})
        elif due < today and st in (None, "open", "unknown"):
            late.append({"who": quien, "what": que, "due": due.isoformat(),
                         "days": (today - due).days, "source": fuente})
        veces = len(c.get("reschedules") or [])
        if veces >= th["reschedules_to_flag"]:
            reprogramados.append({"who": quien, "what": que, "times": veces,
                                  "dates": [value(r.get("due_date"))
                                            for r in c.get("reschedules") or []]})
    out["commitments_overdue"] = late
    out["commitments_undated"] = sin_fecha
    out["commitments_rescheduled"] = reprogramados
    for c in late:
        alert("commitment_overdue", c)
    for c in sin_fecha:
        alert("commitment_undated", c)
    for c in reprogramados:
        # Reprogramado tres veces no es un problema de seguimiento: es un bloqueo
        # que nadie ha nombrado, y es información distinta de tres vencidos.
        alert("commitment_rescheduled", c)

    # --- vendors -------------------------------------------------------
    # The schema has carried vendor deliverables since 0.1 and nothing read
    # them. Crossing what was promised against what has evidence of receipt,
    # and both against what was invoiced, is comparison and subtraction.
    vendors = []
    for v in rec.get("vendors") or []:
        entregables = v.get("deliverables") or []
        vencidos, sin_evidencia, aceptados = [], [], 0
        for dv in entregables:
            due = as_date(dv.get("due_date"))
            st = value(dv.get("state")) or "unknown"
            ev = value(dv.get("evidence"))
            if st in ("delivered", "accepted"):
                aceptados += 1
                if not ev:
                    sin_evidencia.append({"what": value(dv.get("name")), "state": st})
            elif due and due < today:
                vencidos.append({"what": value(dv.get("name")), "due": due.isoformat(),
                                 "days": (today - due).days, "state": st})
        facturado = as_number(v.get("invoiced"))
        # Monto aceptado: solo suma lo que tiene monto declarado. Sin esto, una
        # factura contra un entregable que nunca empezó pasa desapercibida mientras
        # haya otros aceptados — el límite que destapó la corrida sintética.
        montos = [as_number(dv.get("amount")) for dv in entregables]
        con_monto = [m for m in montos if m is not None]
        monto_aceptado = sum(
            m for dv, m in zip(entregables, montos)
            if m is not None and (value(dv.get("state")) or "") in ("delivered", "accepted"))
        fila = {
            "name": value(v.get("name")),
            "contract_ref": value(v.get("contract_ref")),
            "deliverables": len(entregables),
            "accepted": aceptados,
            "late": vencidos,
            "accepted_without_evidence": sin_evidencia,
            "invoiced": facturado,
            "amount_accepted": round(monto_aceptado, 2) if con_monto else None,
            "amounts_declared": len(con_monto),
        }
        vendors.append(fila)
        for d in vencidos:
            alert("vendor_deliverable_late", dict(d, vendor=fila["name"]))
        for d in sin_evidencia:
            alert("vendor_accepted_without_evidence", dict(d, vendor=fila["name"]))
        if facturado and entregables and aceptados == 0:
            alert("vendor_invoiced_without_delivery",
                  {"vendor": fila["name"], "invoiced": facturado,
                   "deliverables": len(entregables)})
        elif facturado and con_monto and facturado > monto_aceptado:
            alert("vendor_invoiced_over_accepted",
                  {"vendor": fila["name"], "invoiced": facturado,
                   "accepted_amount": round(monto_aceptado, 2),
                   "difference": round(facturado - monto_aceptado, 2),
                   "amounts_declared": f"{len(con_monto)} de {len(entregables)}"})
    out["vendors"] = vendors

    # --- changes against the baseline ----------------------------------
    # An append-only baseline keeps the history. It does not by itself prove
    # the replanning stayed inside what the committee approved, and that is a
    # subtraction: days the baseline moved, minus days the approved changes
    # authorised. No document authorising the difference is a finding, not an
    # accusation — the agent says what the documents show.
    cambios = rec.get("changes") or []
    autorizados, ilegibles, sin_linea_base = 0, [], []
    for ch in cambios:
        if (value(ch.get("decision")) or "unknown").lower() != "approved":
            continue
        dias = as_days(ch.get("time_impact"))
        if dias is None:
            if value(ch.get("time_impact")) not in (None, ""):
                ilegibles.append({"ref": value(ch.get("ref")),
                                  "time_impact": value(ch.get("time_impact"))})
            continue
        autorizados += dias
        pedido = as_date(ch.get("requested_on"))
        posterior = [b for b in baselines[1:]
                     if pedido and as_date(b.get("approved_on"))
                     and as_date(b.get("approved_on")) >= pedido]
        if dias and not posterior:
            sin_linea_base.append({"ref": value(ch.get("ref")), "days": dias})

    movido = (approved_end - original_end).days if approved_end and original_end else None
    out["changes"] = {
        "total": len(cambios),
        "approved_time_days": autorizados,
        "baseline_moved_days": movido,
        "unauthorized_days": (movido - autorizados) if movido is not None else None,
        "time_impact_unreadable": ilegibles,
        "approved_without_new_baseline": sin_linea_base,
    }
    sin_autorizar = out["changes"]["unauthorized_days"]
    if sin_autorizar is not None and sin_autorizar > th["rebaseline_tolerance_days"]:
        alert("rebaseline_unauthorized", {"days": sin_autorizar, "moved": movido,
                                          "authorized": autorizados,
                                          "changes_seen": len(cambios)})
    for c in sin_linea_base:
        alert("change_without_baseline", c)

    # --- record quality -------------------------------------------------
    conflicts, missing, stale = [], [], []
    for path, field in walk_fields(rec):
        st = field.get("state")
        if st == "ambiguous":
            conflicts.append({"field": path, "value": field.get("value"),
                              "source": field.get("source"),
                              "conflict": field.get("conflict")})
        elif st == "not_found":
            missing.append(path)
        d = as_date(field.get("source_date"))
        if d:
            months = (today.year - d.year) * 12 + (today.month - d.month)
            if months >= th["stale_field_months"]:
                stale.append({"field": path, "source_date": d.isoformat(), "months": months})
    gobierno = [c for c in conflicts if c["field"] in GOVERNANCE_FIELDS]
    conflicts = [c for c in conflicts if c["field"] not in GOVERNANCE_FIELDS]
    out["conflicts"] = conflicts
    out["governance_changes"] = gobierno
    out["fields_missing"] = missing
    out["fields_stale"] = stale

    # De dónde viene cada dato. Un campo marcado `declaration` es la afirmación de
    # alguien traída de otra herramienta; no es evidencia documental, y contarlo como
    # tal es lo que rompería la comparación el día que se conecte un PPM.
    procedencia = {"evidence": 0, "declaration": 0, "unmarked": 0}
    for _, field in walk_fields(rec):
        if field.get("value") is None:
            continue
        procedencia[field.get("source_kind") or "unmarked"] = \
            procedencia.get(field.get("source_kind") or "unmarked", 0) + 1
    out["sources"] = procedencia
    for c in conflicts:
        alert("contradiction", c)
    for c in gobierno:
        alert("governance_change", c)

    # --- declaration against evidence ----------------------------------
    # The thesis of the plugin, and until now the one thing it did not
    # compute: what the manager asserts in one column, what the documents
    # support in the other. No severity scale is invented here. The signals
    # above are listed as they came out, and the light is only called out when
    # it is green and there is something it does not account for.
    declared = rec.get("declared", {}) or {}
    dicho = value(declared.get("status"))
    clave = str(dicho).strip().lower() if dicho else None
    rango = STATUS_RANK.get(clave)
    dicho_el = as_date(declared.get("as_of"))
    sin_explicar = sorted({a["signal"] for a in out["alerts"]
                           if a["signal"] in EVIDENCE_SIGNALS})

    out["declared"] = {
        "status": dicho,
        "understood": rango is not None,
        "progress_pct": as_number(declared.get("progress_pct")),
        "as_of": dicho_el.isoformat() if dicho_el else None,
        "age_days": (today - dicho_el).days if dicho_el else None,
        "source": source_of(declared.get("status")) or value(declared.get("source")),
        "unaccounted_signals": sin_explicar,
    }

    if rango == 0 and sin_explicar:
        alert("declared_vs_evidence", {"declared": dicho,
                                       "as_of": out["declared"]["as_of"],
                                       "source": out["declared"]["source"],
                                       "signals": sin_explicar})

    edad = out["declared"]["age_days"]
    if edad is not None and edad >= th["declaration_stale_days"]:
        alert("declaration_stale", {"days": edad, "as_of": out["declared"]["as_of"]})

    # --- la ficha del gerente contra la lectura del portafolio ----------
    # Séptima invariante: dos agentes leen los mismos documentos y escriben dos
    # fichas que nunca se fusionan. Lo que era un conflicto de escritura es aquí
    # la señal, y aquí solo hay aritmética sobre dos registros que ya existen.
    for d in contrastar(rec, rec.get("pm_record"), today):
        alert("pm_vs_pmo", d)

    return out


def declarado_pct(rec):
    """El avance que el gerente declara, esté el campo donde esté en la ficha."""
    d = rec.get("declared") or {}
    return value(d.get("progress_pct"))


def campo_en(rec, ruta):
    """Baja por una ficha siguiendo «identity.sponsor» y devuelve el campo entero."""
    nodo = rec
    for parte in ruta.split("."):
        if not isinstance(nodo, dict):
            return None
        nodo = nodo.get(parte)
    return nodo


def contrastar(pmo_rec: dict, pm_rec, today: dt.date) -> list:
    """Dónde el gerente y la PMO no leyeron lo mismo.

    **Solo es hallazgo cuando los dos citan y no coinciden**, porque entonces uno de
    los dos vio un documento que el otro no vio, y la señal puede decir cuál y de qué
    fecha. Las otras tres formas de diferir no son hallazgo, y distinguirlas es lo que
    hace que esto sirva:

    - El gerente lo tiene y la PMO no: **diferencia de profundidad.** Un compromiso
      dicho en una reunión no está al alcance de un barrido de portafolio.
    - La PMO lo tiene y el gerente no: sí es hallazgo — la PMO leyó un documento del
      proyecto que el gerente no está viendo.
    - Coinciden: el caso normal, y no se reporta. Un agente que celebra las
      coincidencias es ruido.
    """
    if not isinstance(pm_rec, dict):
        return []
    fuera = []
    for ruta in CAMPOS_CONTRASTADOS:
        a, b = campo_en(pmo_rec, ruta), campo_en(pm_rec, ruta)
        va, vb = value(a), value(b)
        if vb is None and va is None:
            continue
        if vb is None:
            continue                       # profundidad al revés: la PMO vio más
        if va is None:
            fuera.append({"field": ruta, "only": "pm", "pm": vb,
                          "pm_source": source_of(b), "pm_date": source_of_date(b)})
            continue
        if str(va).strip() == str(vb).strip():
            continue
        fa, fb = source_of_date(a), source_of_date(b)
        fuera.append({
            "field": ruta,
            "pmo": va, "pmo_source": source_of(a), "pmo_date": fa,
            "pm": vb, "pm_source": source_of(b), "pm_date": fb,
            # Cuál de los dos cita el documento más reciente. Es lo que convierte el
            # hallazgo en accionable: no «no coinciden», sino «el gerente cita la
            # minuta del 11 y la PMO el acta de enero».
            "newer": ("pm" if fa and fb and fb > fa else
                      "pmo" if fa and fb and fa > fb else None),
        })
    return fuera


def source_of_date(field):
    if isinstance(field, dict):
        return field.get("source_date")
    return None


def _pruebas_contraste():
    """Las cuatro formas de diferir, y solo dos son hallazgo."""
    def c(v, fuente, fecha):
        return {"value": v, "source": fuente, "source_date": fecha, "state": "found"}

    hoy = dt.date(2026, 11, 20)
    pmo = {"identity": {"sponsor": c("María Restrepo", "00-gobierno/acta.md", "2026-01-12"),
                        "manager": c("Daniel Ospina", "00-gobierno/acta.md", "2026-01-12"),
                        "product": {"value": None, "state": "not_found"}},
           "plan": {"end_date": c("2027-02-27", "10-plan/crono.csv", "2026-08-10")}}
    pm = {"identity": {"sponsor": c("Sandra Gil", "30-reuniones/2026-09-11.md", "2026-09-11"),
                       "manager": c("Daniel Ospina", "00-gobierno/acta.md", "2026-01-12"),
                       "product": c("Pagos QR", "00-gobierno/acta.md", "2026-01-12")},
          "plan": {"end_date": c("2027-02-27", "10-plan/crono.csv", "2026-08-10")}}

    d = contrastar(pmo, pm, hoy)
    por_campo = {x["field"]: x for x in d}
    solo_pm = por_campo.get("identity.product", {})
    patro = por_campo.get("identity.sponsor", {})

    # Lo que el gerente tiene y la PMO no, al revés: profundidad, no hallazgo.
    hondo = contrastar({"identity": {"sponsor": c("X", "a.md", "2026-01-01")}},
                       {"identity": {}}, hoy)

    # una cadencia que nadie lee tiene que fallar, no guardarse en silencio
    import tempfile as _tf
    with _tf.TemporaryDirectory() as _d:
        _e = Path(_d)
        try:
            ran(_e, "scan", dt.date(2026, 9, 28))
            _rechaza = False
        except ValueError:
            _rechaza = True
        _acepta = ran(_e, "sweep", dt.date(2026, 9, 28)).get("sweep") == "2026-09-28"

    return [
        ("cadencia · un `--what` que nadie lee se rechaza", _rechaza, True),
        ("cadencia · uno que `due` sí lee se guarda", _acepta, True),
        ("contraste · solo lo que difiere", sorted(por_campo),
         ["identity.product", "identity.sponsor"]),
        ("contraste · coincidir no es hallazgo", "identity.manager" in por_campo, False),
        ("contraste · quién cita lo más nuevo", patro.get("newer"), "pm"),
        ("contraste · lleva las dos citas",
         bool(patro.get("pmo_source") and patro.get("pm_source")), True),
        ("contraste · lo que solo tiene el PM", solo_pm.get("only"), "pm"),
        ("contraste · profundidad al revés no es hallazgo", hondo, []),
        ("contraste · sin ficha del PM no hay señal", contrastar(pmo, None, hoy), []),
    ]


def compute(state: Path, today: dt.date, th: dict) -> dict:
    records = {}
    for f in sorted((state / "records").glob("*.json")):
        records[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    projects = [compute_record(r, today, th) for r in records.values()]

    # dependencies that point at a project whose end date moved
    ends = {p["code"]: p.get("end_date") for p in projects}
    for code, rec in records.items():
        deps = (rec.get("raid") or {}).get("dependencies") or []
        me = next((p for p in projects if p["code"] == value(rec.get("identity", {}).get("code"))), None)
        if me is None:
            continue
        broken = []
        for d in deps:
            on = value(d.get("on_project"))
            if on and on in ends:
                broken.append({"on": on, "their_end": ends[on],
                               "confirmed": bool(value(d.get("confirmed")))})
        me["dependencies"] = broken

    # La PMO no vigila proyectos sueltos: vigila los proyectos que tienen producto.
    # Un producto vive varios proyectos y sobrevive a todos ellos.
    productos = {}
    for pr in projects:
        nombre = pr.get("product")
        if not nombre:
            continue
        g = productos.setdefault(nombre, {"product": nombre, "projects": [],
                                          "alerts": 0, "signals": set()})
        g["projects"].append(pr["code"])
        g["alerts"] += len(pr["alerts"])
        g["signals"].update(a["signal"] for a in pr["alerts"])
    por_producto = [dict(g, signals=sorted(g["signals"]))
                    for g in sorted(productos.values(), key=lambda x: x["product"])]

    return {
        "as_of": today.isoformat(),
        "thresholds": th,
        "projects": projects,
        "products": por_producto,
        "totals": {
            "projects": len(projects),
            "with_alerts": sum(1 for p in projects if p["alerts"]),
            "alerts": sum(len(p["alerts"]) for p in projects),
            "no_baseline": sum(1 for p in projects if not p["has_baseline"]),
            # the number a committee should be handed first: how many of the
            # projects reporting green have evidence their light ignores
            "green_contradicted": sum(
                1 for p in projects
                if any(a["signal"] == "declared_vs_evidence" for a in p["alerts"])
            ),
            "products": len(por_producto),
            "no_authority": sum(1 for p in projects if not p.get("authority")),
        },
    }


def _grafo(records: dict) -> dict:
    """Quién depende de quién, por código de proyecto.

    En la ficha, `raid.dependencies[].on_project` dice *«yo dependo de ese»*. Para
    propagar un cambio hace falta la flecha contraria: quién queda alcanzado si ese se
    mueve. Se invierte una vez y se recorre.
    """
    de = {}
    for rec in records.values():
        mio = value((rec.get("identity") or {}).get("code"))
        if not mio:
            continue
        for d in (rec.get("raid") or {}).get("dependencies") or []:
            otro = value(d.get("on_project"))
            if not otro:
                continue
            de.setdefault(otro, []).append({
                "code": mio,
                "what": value(d.get("what")),
                "needed_by": value(d.get("needed_by")),
                "confirmed": bool(value(d.get("confirmed"))),
                "source": source_of(d.get("what")) or value(d.get("source")),
            })
    return de


def impacto(state: Path, codigo: str, dias: int, today: dt.date) -> dict:
    """A quién alcanza mover un proyecto, y quién no puede sostener su fecha.

    Esto es lo que antes estaba solo en prosa: *«mira las dependencias»*. Mirarlas es
    aritmética sobre dos campos que la ficha ya tiene, así que se calcula aquí.

    Lo que **sí** se puede afirmar con lo que hay escrito:

    - **A quién alcanza**, directa o indirectamente, y por qué camino.
    - **Quién no puede sostener su fecha**: un proyecto que depende del que se movió y
      cierra antes de la fecha nueva tiene un problema que todavía no sabe que tiene.
    - **Qué dependencia nunca se confirmó** con el otro lado. Una dependencia declarada
      y no acordada es la que se descubre el día que se incumple.

    Lo que **no** se puede afirmar, y por eso no se inventa: cuántos días se mueve cada
    uno. Eso necesita holgura por actividad, y una ficha de portafolio no la tiene. Decir
    «se mueve 21 días» sin holgura es un número con aspecto de cálculo.
    """
    records = {}
    for f in sorted((state / "records").glob("*.json")):
        records[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    por_codigo = {}
    for rec in records.values():
        ident = rec.get("identity") or {}
        c = value(ident.get("code"))
        if c:
            por_codigo[c] = rec

    if codigo not in por_codigo:
        return {"project": codigo, "found": False,
                "note": "no hay ficha de ese proyecto en el estado"}

    rec = por_codigo[codigo]
    fin = as_date((rec.get("plan") or {}).get("end_date"))
    nueva = fin + dt.timedelta(days=dias) if fin and dias else fin

    de = _grafo(records)
    alcanzados, vistos = [], {codigo}
    # Anchura, no profundidad: el camino más corto hasta cada proyecto es el que
    # explica mejor por qué quedó alcanzado. Y el conjunto `vistos` es lo que impide
    # que un ciclo de dependencias —que existen— deje esto girando.
    cola = [(codigo, [codigo])]
    while cola:
        actual, camino = cola.pop(0)
        for hijo in de.get(actual, []):
            c = hijo["code"]
            if c in vistos:
                continue
            vistos.add(c)
            otro = por_codigo.get(c) or {}
            su_fin = as_date((otro.get("plan") or {}).get("end_date"))
            fila = {
                "code": c,
                "manager": value((otro.get("identity") or {}).get("manager")),
                "end_date": su_fin.isoformat() if su_fin else None,
                "depends_on": actual,
                "path": camino + [c],
                "hops": len(camino),
                "what": hijo["what"],
                "needed_by": hijo["needed_by"],
                "confirmed": hijo["confirmed"],
                "source": hijo["source"],
                # el hallazgo: cierra antes de que esté lo que espera
                "cannot_hold_date": bool(nueva and su_fin and su_fin <= nueva),
            }
            if fila["cannot_hold_date"]:
                fila["days_short"] = (nueva - su_fin).days
            alcanzados.append(fila)
            cola.append((c, camino + [c]))

    alcanzados.sort(key=lambda x: (not x["cannot_hold_date"], x["hops"], x["code"]))

    # Los hitos del proyecto que se mueve. Sin una red de actividades no se puede saber
    # cuánto se mueve cada uno, así que no se dice: lo que sí se puede afirmar es **por
    # cuáles pasa el cambio** — los que siguen abiertos y caen entre hoy y la fecha
    # nueva son los que tienen que absorberlo, y son los que hay que volver a fechar.
    hitos = []
    for m in (rec.get("plan") or {}).get("milestones") or []:
        cuando = as_date(m.get("current_date")) or as_date(m.get("baseline_date"))
        if not cuando or value(m.get("state")) == "met" or value(m.get("evidence")):
            continue
        if nueva and today <= cuando <= nueva:
            hitos.append({"name": value(m.get("name")), "date": cuando.isoformat(),
                          "days_away": (cuando - today).days})
    hitos.sort(key=lambda x: x["date"])
    return {
        "project": codigo,
        "found": True,
        "manager": value((rec.get("identity") or {}).get("manager")),
        "end_date": fin.isoformat() if fin else None,
        "moves_days": dias,
        "new_end": nueva.isoformat() if nueva else None,
        "reached": alcanzados,
        "milestones_reached": hitos,
        "totals": {
            "reached": len(alcanzados),
            "milestones_reached": len(hitos),
            "direct": sum(1 for a in alcanzados if a["hops"] == 1),
            "indirect": sum(1 for a in alcanzados if a["hops"] > 1),
            "cannot_hold_date": sum(1 for a in alcanzados if a["cannot_hold_date"]),
            "unconfirmed": sum(1 for a in alcanzados if not a["confirmed"]),
            "managers": sorted({a["manager"] for a in alcanzados if a["manager"]}),
        },
        "note": ("Cuántos días se mueve cada uno no sale de aquí: eso necesita holgura "
                 "por actividad, y la ficha de portafolio no la tiene. Los hitos que "
                 "salen son por los que pasa el cambio, no los que se movieron."),
    }


# ---------------------------------------------------------------- cadencia

CADENCIAS = {"daily": 1, "weekly": 7, "biweekly": 14, "fortnightly": 14,
             "monthly": 30, "quarterly": 91}


def _cada(nombre) -> int:
    return CADENCIAS.get(str(nombre or "").lower().strip(), 0)


def proximo_comite(cfg_cycle: dict, today: dt.date):
    """La próxima fecha de comité, rodando hacia adelante desde la declarada.

    La organización declara una fecha y una cadencia. Si la fecha ya pasó —porque
    nadie volvió a tocar la configuración, que es lo normal— se avanza en pasos de
    la cadencia hasta alcanzar hoy. Preguntar por una fecha vencida no sirve de nada.
    """
    base = as_date(cfg_cycle.get("committee_next"))
    paso = _cada(cfg_cycle.get("committee"))
    if not base:
        return None, paso
    if paso <= 0:
        return (base if base >= today else None), paso
    while base < today:
        base += dt.timedelta(days=paso)
    return base, paso


def due(config: Path, state: Path, today: dt.date) -> dict:
    """Qué toca hoy, según la cadencia que la persona declaró.

    Esto es lo que convierte esto en un agente y no en un comando: no espera a que
    lo llamen. La decisión de si hoy toca algo es aritmética de fechas, así que vive
    aquí y no en el criterio del modelo.

    El registro de la última corrida vive en <estado>/cadencia.json. Sin él, "mensual"
    no se puede calcular: no hay contra qué contar.
    """
    cfg = json.loads(config.read_text(encoding="utf-8")) if config and config.exists() else {}
    ciclo = cfg.get("cycle", {}) or {}
    confirmacion = cfg.get("confirmation", {}) or {}

    registro_f = state / "cadencia.json"
    registro = json.loads(registro_f.read_text(encoding="utf-8")) if registro_f.exists() else {}

    def ultima(clave):
        return as_date(registro.get(clave))

    def vencido(clave, dias):
        if dias <= 0:
            return False
        u = ultima(clave)
        return True if u is None else (today - u).days >= dias

    toca, detalle = [], {}

    # 1 · el barrido: mirar qué cambió en la carpeta. Barato y a diario si se quiso.
    if ciclo.get("daily_sweep"):
        if vencido("sweep", 1):
            toca.append("sweep")
        detalle["sweep"] = {"every_days": 1, "last": registro.get("sweep")}

    # 2 · el informe de comité, con su anticipación
    fecha, paso = proximo_comite(ciclo, today)
    anticipacion = int(ciclo.get("report_lead_days") or 0)
    if fecha:
        entrega = fecha - dt.timedelta(days=anticipacion)
        detalle["committee"] = {
            "next": fecha.isoformat(),
            "days_away": (fecha - today).days,
            "report_on": entrega.isoformat(),
            "every_days": paso or None,
        }
        # se entrega el día que toca, y también si ese día ya pasó sin entregarse
        u = ultima("report")
        pendiente = today >= entrega and (u is None or u < entrega)
        if pendiente:
            toca.append("report")

    # 3 · la confirmación periódica de los campos que envejecen peor
    dias_conf = _cada(confirmacion.get("every"))
    if dias_conf:
        detalle["confirmation"] = {"every_days": dias_conf, "last": registro.get("confirmation"),
                                   "fields_per_run": confirmacion.get("fields_per_run")}
        if vencido("confirmation", dias_conf):
            toca.append("confirmation")

    # 4 · las peticiones que dejó alguien en el servidor
    # No es cadencia: es una bandeja. Pero entra por aquí porque `due` es lo único
    # que el agente mira al despertar, y una cola que nadie lee es peor que no
    # tenerla — alguien preguntó y se quedó esperando.
    abiertas = peticiones_abiertas(state)
    if abiertas:
        detalle["requests"] = {"open": len(abiertas),
                               "oldest": abiertas[0].get("recibida"),
                               "subjects": sorted({r.get("asunto") for r in abiertas})}
        toca.append("requests")

    # cuándo hay que volver a mirar, si hoy no toca nada
    proximos = []
    if ciclo.get("daily_sweep"):
        u = ultima("sweep")
        proximos.append(today + dt.timedelta(days=1) if u is None else u + dt.timedelta(days=1))
    if fecha:
        proximos.append(fecha - dt.timedelta(days=anticipacion))
    if dias_conf:
        u = ultima("confirmation")
        proximos.append((u or today) + dt.timedelta(days=dias_conf))
    futuros = [p for p in proximos if p > today]

    return {
        "today": today.isoformat(),
        "due": toca,
        "quiet": not toca,
        "detail": detalle,
        "next_wake": min(futuros).isoformat() if futuros else None,
    }


def peticiones_abiertas(state: Path) -> list:
    """Las peticiones que el servidor dejó y nadie ha respondido, de la más vieja
    a la más nueva. El agente no las escribe: solo las lee y las marca."""
    carpeta = state / "peticiones"
    if not carpeta.is_dir():
        return []
    salida = []
    for f in sorted(carpeta.glob("*.json")):
        try:
            r = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if not r.get("respondida"):
            r["_file"] = str(f)
            salida.append(r)
    return salida


def responder_peticion(state: Path, ident: str, today: dt.date) -> dict:
    """Marca una petición como respondida. Lo único que el agente le escribe."""
    f = state / "peticiones" / f"{ident}.json"
    if not f.exists():
        raise SystemExit(f"no existe la petición {ident}")
    r = json.loads(f.read_text(encoding="utf-8"))
    r["respondida"] = today.isoformat()
    f.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
    return r


# Lo único que `due` lee de la constancia. Un valor fuera de esta lista se escribía
# igual y no lo leía nadie: el agente creía haber dejado constancia, `due` seguía
# diciendo que tocaba, y el error era silencioso — exactamente lo que el docstring de
# `ran` dice que no puede pasar.
CONSTANCIAS = ("sweep", "report", "confirmation")


def ran(state: Path, que: str, today: dt.date) -> dict:
    """Deja constancia de que algo se corrió hoy. Sin esto, `due` repite para siempre."""
    if que not in CONSTANCIAS:
        raise ValueError(f"cadencia desconocida: {que!r}. "
                         f"Las que `due` lee son {', '.join(CONSTANCIAS)}")
    f = state / "cadencia.json"
    registro = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    registro[que] = today.isoformat()
    f.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    return registro


# ---------------------------------------------------------------- index


def index(docs: Path, state: Path) -> dict:
    """Qué cambió en la carpeta, y qué citas dejaron de resolver.

    Es la regla que controla el costo de todo el sistema: sin esto, cada corrida
    vuelve a leer documentos que no cambiaron. Dos etapas — el hash de bytes decide
    si vale la pena extraer, el hash del texto decide si vale la pena releer — y una
    tercera verificación que no es de costo sino de integridad: toda cita de toda
    ficha tiene que seguir apuntando a un archivo que existe. Una cita que dejó de
    resolver es un hallazgo; en un diseño cuyo valor es la cita, es el peor de los
    huecos silenciosos.
    """
    fichas = {}
    for f in sorted((state / "records").glob("*.json")):
        fichas[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    # lo que cada ficha dice haber leído, y qué proyectos toca cada documento
    visto, de_quien = {}, {}
    for codigo, rec in fichas.items():
        for d in ((rec.get("meta") or {}).get("documents_seen") or []):
            ruta = value(d.get("path"))
            if not ruta:
                continue
            visto[ruta] = d
            de_quien.setdefault(ruta, []).append(codigo)

    nuevos, cambiados, solo_bytes, sin_cambio = [], [], [], 0
    en_disco = {}
    for ruta in sorted(docs.rglob("*")):
        if not ruta.is_file() or ruta.name in IGNORAR or ruta.name.startswith("."):
            continue
        rel = str(ruta.relative_to(docs))
        hb = hash_bytes(ruta)
        en_disco[rel] = hb
        antes = visto.get(rel)
        if antes is None:
            nuevos.append({"path": rel, "hash": hb})
            continue
        if value(antes.get("hash")) == hb:
            sin_cambio += 1
            continue
        ht, ht_antes = hash_texto(ruta), value(antes.get("text_hash"))
        fila = {"path": rel, "projects": de_quien.get(rel, []), "hash": hb}
        if ht and ht_antes and ht == ht_antes:
            solo_bytes.append(fila)          # reguardado: no hay que releer
        else:
            cambiados.append(fila)

    # lo que la ficha dice haber leído y ya no está: borrado, o renombrado si otro
    # archivo nuevo tiene exactamente el mismo contenido
    por_hash_nuevo = {n["hash"]: n["path"] for n in nuevos}
    borrados, renombrados = [], []
    for ruta, d in sorted(visto.items()):
        if ruta in en_disco:
            continue
        hb = value(d.get("hash"))
        destino = por_hash_nuevo.get(hb)
        fila = {"path": ruta, "projects": de_quien.get(ruta, [])}
        if destino:
            renombrados.append(dict(fila, now=destino))
        else:
            borrados.append(fila)
    movidos = {r["now"] for r in renombrados}
    nuevos = [n for n in nuevos if n["path"] not in movidos]

    # integridad de las citas: todo `source` tiene que resolver
    rotas = []
    for codigo, rec in fichas.items():
        for ruta_campo, campo in walk_fields(rec):
            fuente = campo.get("source")
            if fuente and fuente not in en_disco:
                rotas.append({"project": codigo, "field": ruta_campo, "source": fuente})

    tocados = sorted({c for f in cambiados for c in f["projects"]}
                     | {c for f in renombrados for c in f["projects"]}
                     | {c for f in borrados for c in f["projects"]})

    return {
        "documents": len(en_disco),
        "unchanged": sin_cambio,
        "new": nuevos,
        "changed": cambiados,
        "resaved_only": solo_bytes,
        "renamed": renombrados,
        "deleted": borrados,
        "source_missing": rotas,
        "projects_to_recompute": tocados,
        "to_read": len(nuevos) + len(cambiados),
    }


# ---------------------------------------------------------------- init / config


REQUIRED_CONFIG = ["role", "paths", "cycle", "report", "terms_accepted"]
ROLES = ("pmo", "pm")


def init(state: Path) -> dict:
    """Create the state tree. Deterministic, so the model never has to."""
    created = []
    for sub in ("records", "snapshots", "reports"):
        d = state / sub
        if not d.exists():
            d.mkdir(parents=True)
            created.append(str(d))
    return {"state": str(state), "created": created,
            "already_there": not created}


def corrida_inicio(state: Path) -> dict:
    """Marca el arranque, para que el tiempo lo mida la corrida y no lo estime nadie.

    Un tiempo que el operador escribe a mano no es una medición: es un recuerdo. Y la
    promesa publicada de la instalación son quince minutos.
    """
    import time
    f = state / "corrida-en-curso.json"
    f.write_text(json.dumps({"desde": time.time()}), encoding="utf-8")
    return {"marcado": True}


def corrida(state: Path, que: str, today: dt.date, docs: Path = None,
            informe=None, nota=None, salida: Path = None) -> dict:
    """Deja el registro de una corrida: qué se corrió, sobre qué, y qué encontró.

    `cadencia.json` guarda una fecha por tipo, que es lo que `due` necesita y nada más.
    Esto es otra cosa: **la corrida como algo que se puede compartir.** Cuántos proyectos,
    cuántos hallazgos y de qué señal, cuánto tardó, y dónde quedó el informe — para que
    mañana se pueda comparar y para que alguien que no estuvo pueda abrirlo.

    Estaba escrito en prosa en `portfolio-scan.md` —«registra en registro.log qué leyó,
    qué movió y qué omitió»— y en una corrida sobre cincuenta proyectos el archivo quedó
    vacío. Una instrucción en prosa se salta; un comando que hay que correr, no. Por eso es
    aritmética y no una indicación.
    """
    import time
    from collections import Counter

    # El tiempo y los documentos los mide la corrida. Si el operador los teclea, lo que se
    # mide es su transcripción —el mismo defecto que este repositorio le encontró a un
    # informe que reescribió una cifra ya calculada— y la prueba queda viciada.
    # La marca se consume reescribiéndola, no borrándola: el estado de un agente puede
    # vivir en una carpeta compartida donde no se permite borrar, y que la corrida falle
    # por eso sería un defecto del agente, no del recurso.
    segundos = None
    marca = state / "corrida-en-curso.json"
    if marca.exists():
        try:
            d = json.loads(marca.read_text())
            if not d.get("consumida"):
                segundos = round(time.time() - d["desde"])
        except (json.JSONDecodeError, KeyError, TypeError):
            segundos = None
        try:
            marca.write_text(json.dumps({"consumida": True}), encoding="utf-8")
        except OSError:
            pass

    documentos = relectura = None
    if docs and docs.is_dir():
        idx = index(docs, state)
        documentos = idx.get("documents")
        # Lo que de verdad hubo que releer, que es la cifra que gobierna el costo del
        # sistema: sin ella, «leí ciento ochenta y seis documentos» no dice nada.
        relectura = {"sin_cambio": idx.get("unchanged"), "releidos": idx.get("to_read")}

    fichas = sorted((state / "records").glob("*.json"))
    senales, por_caso = Counter(), {}
    for f in fichas:
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        r = compute_record(rec, today, DEFAULT_THRESHOLDS)
        suyas = [a["signal"] for a in r.get("alerts") or []]
        senales.update(suyas)
        # Por caso y no solo el total: sin esto no se puede reconstruir después desde
        # cuándo un proyecto viene arrastrando una señal, y ese es el dato que un comité
        # necesita. Una corrida que pase sin guardarlo lo pierde para siempre.
        codigo = value((rec.get("identity") or {}).get("code")) or f.stem
        por_caso[codigo] = sorted(suyas)

    entrada = {"que": que, "fecha": today.isoformat(), "proyectos": len(fichas),
               "documentos": documentos, "segundos": segundos,
               "relectura": relectura,
               "medido": {"segundos": segundos is not None,
                          "documentos": documentos is not None},
               "hallazgos": sum(senales.values()),
               "por_senal": dict(senales.most_common()), "por_caso": por_caso,
               "informe": str(informe) if informe else None, "nota": nota}

    f = state / "corridas.json"
    previas = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    # Cada corrida tiene identidad propia. Dos corridas del mismo comando el mismo día
    # eran un solo archivo que se pisaba: la segunda borraba a la primera, y borrar una
    # corrida es borrar historia. El ordinal las separa.
    n = 1 + sum(1 for x in previas if x.get("fecha") == today.isoformat() and x.get("que") == que)
    entrada["id"] = f"{today.isoformat()}-{que}-{n}"
    # Lo que el comando produjo, entero. Sin esto la corrida guarda cifras y lo que el
    # agente dijo se queda en una conversación que se cierra, que es justo lo que no se
    # puede auditar. Se copia tal cual: lo que el comando produjo se copia, no se reescribe.
    texto_salida = None
    if salida is not None and Path(salida).is_file():
        texto_salida = Path(salida).read_text(encoding="utf-8", errors="replace").strip()
    entrada["salida"] = bool(texto_salida)
    previas.append(entrada)
    f.write_text(json.dumps(previas, ensure_ascii=False, indent=2) + "\n",
                 encoding="utf-8")

    # Y la versión legible, que es la que se comparte con quien no abre un JSON.
    d = state / "corridas"
    d.mkdir(parents=True, exist_ok=True)
    lineas = [f"# Corrida del {today.isoformat()} · {que}", "",
              f"{len(fichas)} proyectos"
              + (f" · {documentos} documentos" if documentos else "")
              + (f", {relectura['releidos']} releídos y {relectura['sin_cambio']} sin cambio"
                 if relectura and relectura.get("releidos") is not None else "")
              + (f" · {segundos} s" if segundos else "")
              + f" · {sum(senales.values())} hallazgos", ""]
    if segundos is None:
        lineas += ["> El tiempo no se midió: faltó `corrida-inicio` al arrancar. Un "
                   "tiempo escrito a mano es un recuerdo, no una medición.", ""]
    if senales:
        lineas += ["| Señal | Hallazgos |", "|---|---:|"]
        lineas += [f"| `{s}` | {n} |" for s, n in senales.most_common()]
        lineas.append("")
    if informe:
        lineas += [f"El informe quedó en `{informe}`.", ""]
    if nota:
        lineas += [nota, ""]
    anterior = previas[-2] if len(previas) > 1 else None
    if anterior:
        d_h = sum(senales.values()) - (anterior.get("hallazgos") or 0)
        lineas += [f"Contra la corrida del {anterior['fecha']}: "
                   f"{d_h:+d} hallazgos.", ""]
    else:
        lineas += ["Primera corrida: no hay una anterior contra la cual comparar.", ""]
    if texto_salida:
        lineas += ["## Lo que produjo", "", texto_salida, ""]
    else:
        lineas += ["## Lo que produjo", "",
                   "> El comando no entregó su resultado (`--salida`): la corrida registra "
                   "las cifras, pero lo que dijo se quedó en la conversación.", ""]
    (d / f"{entrada['id']}.md").write_text("\n".join(lineas), encoding="utf-8")
    (d / f"{entrada['id']}.html").write_text(
        pagina_corrida(f"Corrida · {entrada['id']}", "\n".join(lineas), today.isoformat()),
        encoding="utf-8")
    return entrada



# ------------------------------------------------------------ la corrida como página
# Cada corrida deja un HTML al lado de su markdown. Es la evidencia que se puede abrir sin
# servidor, mandar por correo o archivar; Rostrum sirve el mismo archivo con el árbol
# encima. Los colores son los del informe, declarados aquí porque los tres agentes
# comparten este módulo y solo Vera lleva `informe.py`.
_PALETA = {"crema": "#f5f4ef", "panel": "#efeee8", "tinta": "#111111", "cuerpo": "#3f4450",
           "apagado": "#6b675f", "oro": "#8a6327", "filete": "#c9c6bd"}


def _e(x) -> str:
    import html as _html
    return _html.escape(str(x), quote=True)


def md_a_html(md: str) -> str:
    """Markdown a HTML, lo justo para lo que una corrida escribe: títulos, párrafos,
    listas, tablas, citas y código. No es un procesador de Markdown y no pretende serlo."""
    out, parrafo, lista, tabla, codigo = [], [], None, [], False
    def cierra():
        nonlocal parrafo, lista, tabla
        if parrafo:
            out.append('<p>' + inl(' '.join(parrafo)) + '</p>'); parrafo = []
        if lista:
            out.append(f'</{lista}>'); lista = None
        if tabla:
            filas = [f for f in tabla if not set(f.replace('|', '').strip()) <= set('-: ')]
            if filas:
                celdas = lambda f: [c.strip() for c in f.strip().strip('|').split('|')]
                out.append('<table><thead><tr>' + ''.join(f'<th>{inl(c)}</th>' for c in celdas(filas[0]))
                           + '</tr></thead><tbody>'
                           + ''.join('<tr>' + ''.join(f'<td>{inl(c)}</td>' for c in celdas(f)) + '</tr>'
                                     for f in filas[1:]) + '</tbody></table>')
            tabla = []
    def inl(t):
        t = _e(t)
        t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
        t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
        t = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', t)
        return t
    for linea in md.splitlines():
        if linea.startswith('```'):
            cierra()
            out.append('<pre>' if not codigo else '</pre>'); codigo = not codigo; continue
        if codigo:
            out.append(_e(linea)); continue
        l = linea.rstrip()
        if not l.strip():
            cierra(); continue
        if l.lstrip().startswith('|'):
            if parrafo or lista: cierra()
            tabla.append(l); continue
        m = re.match(r'^(#{1,6})\s+(.*)', l)
        if m:
            cierra(); n = min(len(m.group(1)) + 1, 6)
            out.append(f'<h{n}>{inl(m.group(2))}</h{n}>'); continue
        if l.startswith('>'):
            cierra(); out.append(f'<blockquote>{inl(l.lstrip("> "))}</blockquote>'); continue
        m = re.match(r'^\s*([-*]|\d+\.)\s+(.*)', l)
        if m:
            if parrafo or tabla: cierra()
            tipo = 'ol' if m.group(1)[0].isdigit() else 'ul'
            if lista != tipo:
                if lista: out.append(f'</{lista}>')
                out.append(f'<{tipo}>'); lista = tipo
            out.append(f'<li>{inl(m.group(2))}</li>'); continue
        if lista or tabla: cierra()
        parrafo.append(l.strip())
    cierra()
    if codigo: out.append('</pre>')
    return '\n'.join(out)



def pagina_corrida(titulo: str, md: str, hoy: str) -> str:
    """El HTML de una corrida, autocontenido, en la paleta del informe."""
    p = _PALETA
    css = (f"body{{margin:0;background:{p['crema']};color:{p['cuerpo']};font:16px/1.6 -apple-system,"
           f"Segoe UI,Helvetica,Arial,sans-serif}}.hoja{{max-width:900px;margin:0 auto;padding:38px 24px}}"
           f"h1,h2,h3{{color:{p['tinta']};letter-spacing:-.02em;line-height:1.15}}h1{{font-size:1.9rem}}"
           f"h2{{font-size:1.25rem;margin-top:2em}}.nav a{{color:{p['oro']};text-decoration:none}}"
           f"table{{border-collapse:collapse;width:100%;margin:1em 0;font-size:.95rem}}"
           f"th,td{{text-align:left;padding:.45em .6em;border-bottom:1px solid {p['filete']}}}"
           f"th{{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:{p['apagado']}}}"
           f"code{{background:{p['panel']};padding:.1em .35em;border-radius:3px;font-size:.9em}}"
           f"pre{{background:{p['panel']};padding:1em;overflow:auto}}"
           f"blockquote{{margin:1em 0;padding:.2em 1em;border-left:3px solid {p['oro']};color:{p['apagado']}}}"
           f".pie{{margin-top:3em;padding-top:1em;border-top:1px solid {p['filete']};font-size:.85rem;"
           f"color:{p['apagado']}}}")
    return (f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex,nofollow"><title>{_e(titulo)}</title>'
            f'<style>{css}</style></head><body><div class="hoja">'
            f'<div class="nav"><a href="/corridas">← Historia de las corridas</a></div>'
            f'<div class="bloque">{md_a_html(md)}</div>'
            f'<div class="pie">Esta corrida se escribió sola al terminar el comando, el {_e(hoy)}; '
            f'nada de esto se redactó después. Es la historia de lo que el agente leyó en los '
            f'documentos, no de lo que pasó ni un juicio sobre nadie.</div></div></body></html>\n')


def estados_de(state: Path) -> list:
    """Los estados de los tres agentes bajo una misma raíz, con quién es cada uno.

    Rostrum es **uno** para los tres. El gerente de proyecto y el de producto no tienen
    servidor aparte: publican su estado y el mismo portal lo sirve. Un portal por agente
    obligaría a un patrocinador a saber a cuál entrar, y eso ya no es transparencia.

    La convención es la carpeta: el estado del portafolio es la raíz, y al lado viven
    `<estado>-productos/<código>` y `<estado>-proyectos/<código>`. Lo que no esté, no está —
    no se inventa una ruta.
    """
    out = [("portafolio", None, state)]
    for sufijo, quien in (("-productos", "producto"), ("-proyectos", "proyecto")):
        hermano = state.parent / (state.name + sufijo)
        if hermano.is_dir():
            for d in sorted(x for x in hermano.iterdir() if x.is_dir()):
                out.append((quien, d.name, d))

    # La primera corrida real de los tres agentes a la vez dejó los estados en otro
    # sitio: Samuel en `<estado>/<código>/` y Alba en `<estado>/productos/<código>/`, que
    # es donde sus `setup` los ponen por defecto. Un portal que solo mirara a los hermanos
    # los habría dado por inexistentes, y eso no es «lo que no esté, no está»: es no
    # buscar. Un estado se reconoce por lo que contiene, no por dónde quedó.
    propios = {"records", "snapshots", "reports", "corridas", "peticiones", "metrics",
               "requirements"}
    ya = {d for _, _, d in out}

    def es_estado(d: Path) -> bool:
        return (d / "corridas.json").is_file() or (d / "config.json").is_file() \
            or (d / "producto.json").is_file()

    cola = sorted(x for x in state.iterdir() if x.is_dir() and x.name not in propios)
    while cola:
        x = cola.pop(0)
        if x.name == "productos":
            cola += sorted(y for y in x.iterdir() if y.is_dir())
            continue
        if x in ya or not es_estado(x):
            continue
        quien = "producto" if (x / "producto.json").is_file() else "proyecto"
        out.append((quien, x.name, x))
        ya.add(x)
    return out


def historia(state: Path, todos: bool = False) -> dict:
    """La historia de las corridas. Con `todos`, la de los tres agentes junta."""
    if todos:
        return historia_junta(state)
    return _historia_de(state)


def historia_junta(state: Path) -> dict:
    """Las corridas de los tres agentes en una sola línea de tiempo.

    Un director de PMO, un gerente o un patrocinador entra a un sitio y ve todo lo que
    corrió sobre el portafolio, sobre un proyecto y sobre un producto. Cada corrida dice
    de quién es; sin eso, una lista mezclada no se puede leer.
    """
    corridas, casos, instantaneas = [], {}, []
    for quien, cual, d in estados_de(state):
        h = _historia_de(d)
        for c in h["corridas"]:
            corridas.append(dict(c, agente=quien, sobre=cual))
        for codigo, senales in h["casos"].items():
            destino = casos.setdefault(codigo, {})
            for s, x in senales.items():
                # Un mismo caso puede aparecer en dos estados —el proyecto lo ve su
                # gerente y el portafolio lo ve entero—. Se queda la racha más larga, que
                # es la que un comité necesita: el problema no empieza de nuevo porque lo
                # mire otro.
                if s not in destino or x["seguidas"] > destino[s]["seguidas"]:
                    destino[s] = dict(x, agente=quien)
        instantaneas += h["instantaneas"]
    corridas.sort(key=lambda c: (c.get("fecha") or "", c.get("agente") or ""))
    return {"corridas": corridas, "casos": casos, "total": len(corridas),
            "desde": corridas[0]["fecha"] if corridas else None,
            "hasta": corridas[-1]["fecha"] if corridas else None,
            "instantaneas": sorted(set(instantaneas)),
            "agentes": sorted({c["agente"] for c in corridas})}


def _historia_de(state: Path) -> dict:
    """La historia de las corridas: qué se corrió, qué encontró, y desde cuándo.

    Una organización real produce documentos todos los días, y ese rastro **es** la
    memoria del proyecto. Borrarlo es borrar la historia: sin él no se puede presentar un
    avance, ni entender dónde está un proyecto, ni sostener ante un comité que algo lleva
    meses sin resolverse. Así que aquí no se poda nada — y no hace falta: una instantánea
    de cincuenta proyectos pesa 112 KB, y tres años de corridas semanales caben en 17 MB.
    Lo que no se guarda es el informe renderizado, que pesa siete veces más y se vuelve a
    producir cuando alguien lo pide.

    De cada caso sale lo único que un comité necesita saber de una señal: **desde cuándo**
    la arrastra y **en cuántas corridas seguidas** apareció. Una señal que sonó una vez es
    ruido; una que lleva cinco cortes es una decisión que nadie tomó. Y cuando deja de
    sonar queda la fecha en que se resolvió, que también es historia.
    """
    f = state / "corridas.json"
    corridas = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    corridas.sort(key=lambda c: (c.get("fecha") or "", c.get("que") or ""))

    casos = {}
    for i, c in enumerate(corridas):
        for codigo, senales in (c.get("por_caso") or {}).items():
            d = casos.setdefault(codigo, {})
            for s in senales:
                e = d.setdefault(s, {"primera": c["fecha"], "ultima": None,
                                     "corridas": 0, "seguidas": 0, "_i": None})
                e["ultima"] = c["fecha"]
                e["corridas"] += 1
                e["seguidas"] = (e["seguidas"] + 1 if e["_i"] == i - 1 else 1)
                e["_i"] = i
                e.pop("resuelta_en", None)
            for s, e in d.items():
                if s not in senales and e["_i"] == i - 1:
                    e["resuelta_en"] = c["fecha"]
    for d in casos.values():
        for e in d.values():
            e.pop("_i", None)

    return {
        "corridas": [{k: v for k, v in c.items() if k != "por_caso"} for c in corridas],
        "casos": casos, "total": len(corridas),
        "desde": corridas[0]["fecha"] if corridas else None,
        "hasta": corridas[-1]["fecha"] if corridas else None,
        "instantaneas": sorted(x.stem for x in (state / "snapshots").glob("*.json")),
    }


def check_config(config: Path) -> dict:
    """Validate a configuration and return the effective settings."""
    problems = []
    if not config.exists():
        return {"ok": False, "problems": [f"{config} does not exist — run the setup command"]}
    try:
        cfg = json.loads(config.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {"ok": False, "problems": [f"invalid JSON: {e}"]}

    for key in REQUIRED_CONFIG:
        if key not in cfg:
            problems.append(f"missing section '{key}'")

    role = cfg.get("role")
    if role and role not in ROLES:
        problems.append(f"role '{role}' is not valid (pmo | pm)")

    paths = cfg.get("paths", {})
    for key in ("documents", "state"):
        if not paths.get(key):
            problems.append(f"paths.{key} is not set")
        elif not Path(paths[key]).expanduser().exists():
            problems.append(f"paths.{key} points at something that does not exist: {paths[key]}")

    accepted = cfg.get("terms_accepted") or {}
    if not accepted.get("version") or not accepted.get("date"):
        problems.append("terms_accepted has no version or no date — the gate is not satisfied")

    th = dict(DEFAULT_THRESHOLDS)
    th.update(cfg.get("thresholds", {}))
    unknown = set(cfg.get("thresholds", {})) - set(DEFAULT_THRESHOLDS)
    for u in sorted(unknown):
        problems.append(f"unknown threshold '{u}'")

    return {"ok": not problems, "problems": problems, "role": role,
            "effective_thresholds": th,
            "paths": {k: str(Path(v).expanduser()) for k, v in paths.items() if v}}


# ---------------------------------------------------------------- snapshot / diff

def flatten(rec: dict) -> dict:
    return {path: field.get("value") for path, field in walk_fields(rec)}


def snapshot(state: Path, today: dt.date) -> Path:
    snaps = state / "snapshots"
    snaps.mkdir(parents=True, exist_ok=True)
    data = {}
    for f in sorted((state / "records").glob("*.json")):
        data[f.stem] = flatten(json.loads(f.read_text(encoding="utf-8")))
    out = snaps / f"{today.isoformat()}.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def diff(state: Path, against: Path | None) -> dict:
    snaps = sorted((state / "snapshots").glob("*.json"))
    previous = against or (snaps[-1] if snaps else None)
    if previous is None:
        return {"baseline_run": True, "note": "no previous snapshot: this is the starting point"}

    old = json.loads(Path(previous).read_text(encoding="utf-8"))
    new = {f.stem: flatten(json.loads(f.read_text(encoding="utf-8")))
           for f in sorted((state / "records").glob("*.json"))}

    changed = []
    for code in sorted(set(old) | set(new)):
        if code not in old:
            changed.append({"project": code, "change": "new"})
            continue
        if code not in new:
            changed.append({"project": code, "change": "gone"})
            continue
        for field in sorted(set(old[code]) | set(new[code])):
            before, after = old[code].get(field), new[code].get(field)
            if before != after:
                changed.append({"project": code, "field": field,
                                "before": before, "after": after})
    return {"against": str(previous), "changes": changed, "count": len(changed)}


# ---------------------------------------------------------------- selftest

def _selftest_corrida():
    """Que la corrida quede registrada y sepa compararse con la anterior.

    Es lo que permite compartir una corrida: sin registro, el informe queda en una
    carpeta que hay que recordar y la del mes siguiente no tiene contra qué medirse.
    """
    import tempfile
    hoy = dt.date(2026, 9, 28)
    with tempfile.TemporaryDirectory() as tmp:
        estado = Path(tmp) / "estado"
        init(estado)
        ficha = {"identity": {"code": {"value": "PRY-Z"}},
                 "declared": {"status": {"value": "verde"}, "progress_pct": {"value": 90},
                              "as_of": {"value": "2026-09-27"}},
                 "plan": {"milestones": [
                     {"name": {"value": "Diseño"}, "current_date": {"value": "2025-01-10"},
                      "state": {"value": "met"}},
                     {"name": {"value": "Piloto"}, "current_date": {"value": "2025-06-10"},
                      "state": {"value": "open"}},
                     {"name": {"value": "Salida"}, "current_date": {"value": "2025-09-10"},
                      "state": {"value": "open"}}]},
                 "activity": {"last_document_date": {"value": "2026-09-27"}}}
        (estado / "records" / "PRY-Z.json").write_text(
            json.dumps(ficha, ensure_ascii=False), encoding="utf-8")

        corrida_inicio(estado)
        una = corrida(estado, "sweep", hoy, nota="la primera")
        legible = (estado / "corridas" / "2026-09-28-sweep-1.md").read_text(encoding="utf-8")
        dos = corrida(estado, "report", hoy, informe=Path("x/informe"))
        todas = json.loads((estado / "corridas.json").read_text(encoding="utf-8"))
        segundo = (estado / "corridas" / "2026-09-28-report-1.md").read_text(encoding="utf-8")
        (Path(tmp) / "salida.md").write_text("# Diagnóstico\n\nLa carpeta no permite saber "
                                             "el presupuesto.", encoding="utf-8")
        corrida(estado, "health-check", hoy, salida=Path(tmp) / "salida.md")
        tercero = (estado / "corridas" / "2026-09-28-health-check-1.md").read_text(encoding="utf-8")
        return [
            ("corrida · cuenta los proyectos del estado", una["proyectos"], 1),
            ("corrida · cuenta los hallazgos por señal",
             una["por_senal"].get("milestone_overdue"), 2),
            ("corrida · el avance declarado contra el plan también",
             "progress_vs_plan" in una["por_senal"], True),
            ("corrida · deja la versión legible", "| Señal | Hallazgos |" in legible, True),
            ("corrida · y dice que no hay anterior",
             "no hay una anterior" in legible, True),
            ("corrida · acumula, no reemplaza", len(todas), 2),
            ("corrida · cada una tiene identidad propia", [x["id"] for x in todas],
             ["2026-09-28-sweep-1", "2026-09-28-report-1"]),
            ("corrida · sin salida entregada, la página lo dice",
             "no entregó su resultado" in legible, True),
            ("corrida · deja también el HTML, abrible sin servidor",
             (estado / "corridas" / "2026-09-28-health-check-1.html").is_file()
             and "no permite saber el presupuesto" in
             (estado / "corridas" / "2026-09-28-health-check-1.html").read_text(encoding="utf-8"), True),
            ("corrida · con salida, la copia entera",
             "no permite saber el presupuesto" in tercero
             and "no entregó su resultado" not in tercero, True),
            ("corrida · mide el tiempo ella misma", una["medido"]["segundos"], True),
            ("corrida · y la segunda ya no tiene marca que leer",
             dos["medido"]["segundos"], False),
            ("corrida · lo dice cuando no lo pudo medir",
             "no se midió" in segundo, True),
            ("corrida · guarda dónde quedó el informe", dos["informe"], "x/informe"),
            ("corrida · y compara con la anterior",
             "Contra la corrida del 2026-09-28" in segundo, True),
        ]


def selftest() -> int:
    today = dt.date(2026, 9, 19)
    rec = {
        "identity": {"code": {"value": "PRY-001", "source": "a.md", "source_date": "2026-01-10", "state": "found"},
                     "name": {"value": "Originación", "source": "a.md", "source_date": "2026-01-10", "state": "found"},
                     "sponsor": {"value": "M. Restrepo", "source": "a.md", "source_date": "2024-06-01", "state": "found"}},
        "plan": {
            "start_date": {"value": "2026-01-01", "source": "p.md", "source_date": "2026-01-01", "state": "found"},
            "end_date": {"value": "2026-12-31", "source": "p3.md", "source_date": "2026-08-01", "state": "found"},
            "baseline": [
                {"version": 1, "approved_on": "2026-01-01", "end_date": "2026-09-30",
                 "reason": "inicial"},
                {"version": 2, "approved_on": "2026-08-01", "end_date": "2026-11-30",
                 "reason": "atraso proveedor"},
            ],
            "milestones": [
                {"name": {"value": "Hito 1"}, "current_date": {"value": "2026-08-15"},
                 "state": {"value": "pending"}, "evidence": {"value": None}},
                {"name": {"value": "Hito 2"}, "current_date": {"value": "2026-07-01"},
                 "state": {"value": "met"}, "evidence": {"value": "acta.md"}},
            ],
        },
        # `approved` viene importado de la herramienta de portafolio: es una
        # declaración, no evidencia documental, y se marca como tal
        "money": {"currency": {"value": "COP"},
                  "approved": {"value": 1000, "source_kind": "declaration"},
                  "committed": {"value": 950}, "executed": {"value": 400},
                  "projection": {"value": 1200}},
        "commitments": [
            {"who": {"value": "Carlos"}, "what": {"value": "Propuesta"},
             "due_date": {"value": "2026-09-05"}, "state": {"value": "open"},
             "source": {"value": "min.md"},
             # prometido tres veces con fecha nueva cada vez: un bloqueo, no tres vencidos
             "reschedules": [{"due_date": "2026-08-07"}, {"due_date": "2026-08-21"},
                             {"due_date": "2026-09-05"}]},
            # sin fecha: no puede estar vencido, y hasta ahora tampoco se contaba
            {"who": {"value": "Diana"}, "what": {"value": "Revisar el alcance"},
             "due_date": {"value": "no_declarada"}, "state": {"value": "open"},
             "source": {"value": "min.md"}},
        ],
        "activity": {"last_document_date": {"value": "2026-08-20"}},
        "raid": {"dependencies": [{"on_project": {"value": "PRY-002"}, "confirmed": {"value": False}}]},
        # el comité autorizó 30 días; la línea base se movió 61
        "changes": [
            {"ref": {"value": "CC-01"}, "requested_on": {"value": "2026-07-15"},
             "time_impact": {"value": "30 días"}, "decision": {"value": "approved"}},
            {"ref": {"value": "CC-02"}, "requested_on": {"value": "2026-07-20"},
             "time_impact": {"value": "2 meses"}, "decision": {"value": "approved"}},
        ],
        "vendors": [
            {"name": {"value": "Proveedor A"}, "contract_ref": {"value": "OC-77"},
             "invoiced": {"value": 500},
             "deliverables": [
                 {"name": {"value": "Módulo 1"}, "due_date": {"value": "2026-08-01"},
                  "amount": {"value": 300}, "state": {"value": "pending"},
                  "evidence": {"value": None}},
                 {"name": {"value": "Módulo 2"}, "due_date": {"value": "2026-09-01"},
                  "amount": {"value": 150}, "state": {"value": "accepted"},
                  "evidence": {"value": None}},
             ]},
            {"name": {"value": "Proveedor B"}, "invoiced": {"value": 200},
             "deliverables": [
                 {"name": {"value": "Soporte"}, "due_date": {"value": "2026-12-01"},
                  "state": {"value": "pending"}, "evidence": {"value": None}},
             ]},
        ],
        "declared": {"status": {"value": "verde", "source": "informe.md"},
                     "progress_pct": {"value": 65},
                     "as_of": {"value": "2026-08-10"}},
    }
    r = compute_record(rec, today, DEFAULT_THRESHOLDS)
    kinds = sorted({a["signal"] for a in r["alerts"]})

    checks = [
        ("replanificaciones", r["replans"], 1),
        ("atraso vs original (días)", r["slip_vs_original_days"], 92),
        ("atraso vs vigente (días)", r["slip_vs_current_days"], 31),
        ("días en silencio", r["days_silent"], 30),
        ("hitos vencidos", len(r["milestones_overdue"]), 1),
        ("compromisos vencidos", len(r["commitments_overdue"]), 1),
        ("disponible real", r["money"]["available_real"], 50.0),
        ("% comprometido", r["money"]["pct_committed"], 95.0),
        ("% ejecutado", r["money"]["pct_executed"], 40.0),
        ("proyección sobre aprobado %", r["money"]["projection_over_pct"], 20.0),
        ("campos vencidos", len(r["fields_stale"]), 1),
        # compromisos
        ("compromisos sin fecha", len(r["commitments_undated"]), 1),
        ("compromisos reprogramados", len(r["commitments_rescheduled"]), 1),
        ("veces que se reprogramó", r["commitments_rescheduled"][0]["times"], 3),
        # procedencia del dato
        ("campos marcados como declaración", r["sources"]["declaration"], 1),
        # proveedores
        ("monto aceptado del proveedor", r["vendors"][0]["amount_accepted"], 150.0),
        ("entregables con monto", r["vendors"][0]["amounts_declared"], 2),
        ("entregables vencidos", len(r["vendors"][0]["late"]), 1),
        ("aceptados sin evidencia", len(r["vendors"][0]["accepted_without_evidence"]), 1),
        ("facturado sin entrega", r["vendors"][1]["invoiced"], 200.0),
        # cambios contra línea base
        ("la línea base se movió (días)", r["changes"]["baseline_moved_days"], 61),
        ("días autorizados por el comité", r["changes"]["approved_time_days"], 30),
        ("días sin autorización", r["changes"]["unauthorized_days"], 31),
        ("impactos de tiempo ilegibles", len(r["changes"]["time_impact_unreadable"]), 1),
        # declaración contra evidencia
        ("la declaración se entendió", r["declared"]["understood"], True),
        ("antigüedad de la declaración", r["declared"]["age_days"], 40),
        ("señales que el verde no explica", len(r["declared"]["unaccounted_signals"]), 11),
        # lo que ve el diff: un campo sin `state` tiene que contarse igual
        ("campo con state visible al diff", "declared.status" in flatten(rec), True),
        ("campo sin state visible al diff", "money.approved" in flatten(rec), True),
        ("señales", kinds, ["budget_committed", "commitment_overdue",
                            "commitment_rescheduled", "commitment_undated",
                            "declaration_stale", "declared_vs_evidence",
                            "milestone_overdue", "rebaseline_unauthorized",
                            "silent", "variance_cost", "variance_time",
                            "vendor_accepted_without_evidence",
                            "vendor_deliverable_late", "vendor_invoiced_over_accepted",
                            "vendor_invoiced_without_delivery"]),
    ]
    checks += _selftest_cadencia()
    checks += _selftest_corrida()

    ok = True
    for label, got, want in checks:
        good = got == want
        ok &= good
        print(f"  {'OK ' if good else 'FALLA'} {label:32} {got!r}{'' if good else f'  esperado {want!r}'}")
    print("\nselftest:", "sin errores" if ok else "CON ERRORES")
    return 0 if ok else 1


def _pruebas_impacto():
    """A quién alcanza mover un proyecto, y quién no puede sostener su fecha."""
    import shutil
    import tempfile

    def c(v, fuente="acta.md", fecha="2026-01-12"):
        return {"value": v, "source": fuente, "source_date": fecha, "state": "found"}

    def ficha(codigo, gerente, fin, depende_de=(), confirmada=True, hitos=()):
        return {
            "identity": {"code": c(codigo), "name": c(f"Proyecto {codigo}"),
                         "manager": c(gerente)},
            "plan": {"end_date": c(fin),
                     "milestones": [{"name": c(n), "current_date": c(f),
                                     "state": c(e)} for n, f, e in hitos]},
            "raid": {"dependencies": [
                {"on_project": c(x), "what": c("la interfaz"),
                 "confirmed": c(confirmada)} for x in depende_de]},
        }

    hoy = dt.date(2026, 11, 20)
    tmp = Path(tempfile.mkdtemp())
    (tmp / "records").mkdir()

    # A se mueve. B depende de A y cierra después; C depende de B y cierra ANTES de la
    # fecha nueva de A, así que no puede sostener su fecha y nadie se lo ha dicho.
    # D no depende de nadie: el control negativo del grafo.
    # E depende de A con la dependencia sin confirmar.
    fichas = [
        ficha("PRY-A", "Ana", "2027-01-15", hitos=[
            ("Certificación", "2026-12-10", "open"),      # entre hoy y la fecha nueva
            ("Piloto", "2027-03-01", "open"),             # también
            ("Cierre contable", "2027-06-30", "open"),    # después: no lo toca
            ("Diseño", "2026-12-01", "met")]),            # cumplido: no cuenta
        ficha("PRY-B", "Beto", "2027-06-30", ["PRY-A"]),
        ficha("PRY-C", "Caro", "2027-02-01", ["PRY-B"]),
        ficha("PRY-D", "Dani", "2027-09-01"),
        ficha("PRY-E", "Eva", "2027-08-01", ["PRY-A"], confirmada=False),
    ]
    for f in fichas:
        codigo = value(f["identity"]["code"])
        (tmp / "records" / f"{codigo}.json").write_text(
            json.dumps(f, ensure_ascii=False), encoding="utf-8")

    r = impacto(tmp, "PRY-A", 60, hoy)
    por = {x["code"]: x for x in r["reached"]}
    ciclo_ok = True
    try:
        # un ciclo de dependencias existe en la vida real y no puede dejar esto girando
        (tmp / "records" / "PRY-F.json").write_text(json.dumps(
            ficha("PRY-F", "Fede", "2027-05-01", ["PRY-G"]), ensure_ascii=False),
            encoding="utf-8")
        (tmp / "records" / "PRY-G.json").write_text(json.dumps(
            ficha("PRY-G", "Gabi", "2027-05-01", ["PRY-F"]), ensure_ascii=False),
            encoding="utf-8")
        impacto(tmp, "PRY-F", 10, hoy)
    except RecursionError:
        ciclo_ok = False

    sin_ficha = impacto(tmp, "PRY-Z", 10, hoy)
    shutil.rmtree(tmp)

    return [
        ("impacto · la fecha nueva es aritmética, no estimación",
         r["new_end"], "2027-03-16"),
        ("impacto · alcanza al que depende directo", "PRY-B" in por, True),
        ("impacto · y al que depende de ese", "PRY-C" in por, True),
        ("impacto · el que no depende de nadie no se toca", "PRY-D" in por, False),
        ("impacto · dice por qué camino quedó alcanzado",
         por["PRY-C"]["path"], ["PRY-A", "PRY-B", "PRY-C"]),
        ("impacto · directos e indirectos se cuentan aparte",
         (r["totals"]["direct"], r["totals"]["indirect"]), (2, 1)),
        ("impacto · el que cierra antes de la fecha nueva no la puede sostener",
         por["PRY-C"]["cannot_hold_date"], True),
        ("impacto · y dice por cuántos días", por["PRY-C"]["days_short"], 43),
        ("impacto · el que cierra después sí la sostiene",
         por["PRY-B"]["cannot_hold_date"], False),
        ("impacto · la dependencia declarada y no acordada se marca",
         por["PRY-E"]["confirmed"], False),
        ("impacto · y se cuenta, porque es la que se descubre incumplida",
         r["totals"]["unconfirmed"], 1),
        ("impacto · trae el gerente de cada uno, que es a quien hay que llamar",
         r["totals"]["managers"], ["Beto", "Caro", "Eva"]),
        ("impacto · lo que no puede sostener su fecha va primero",
         r["reached"][0]["code"], "PRY-C"),
        ("impacto · los hitos por los que pasa el cambio",
         [h["name"] for h in r["milestones_reached"]], ["Certificación", "Piloto"]),
        ("impacto · el hito cumplido no cuenta, y el de después tampoco",
         r["totals"]["milestones_reached"], 2),
        ("impacto · un ciclo de dependencias no lo deja girando", ciclo_ok, True),
        ("impacto · sin ficha de ese proyecto, lo dice", sin_ficha["found"], False),
    ]


def _selftest_cadencia():
    """La cadencia: qué toca hoy, y que deje de tocar cuando ya se corrió.

    Corre sobre un directorio temporal porque necesita escribir el registro de la
    última corrida. Sin ese registro, «mensual» no se puede calcular.
    """
    import shutil
    import tempfile
    tmp = Path(tempfile.mkdtemp())
    (tmp / "records").mkdir()
    cfg = tmp / "config.json"
    # el comité se declaró en agosto y nadie volvió a tocar la configuración,
    # que es exactamente lo que pasa en la vida real
    cfg.write_text(json.dumps({
        "cycle": {"committee": "biweekly", "committee_next": "2026-08-06",
                  "report_lead_days": 2, "daily_sweep": True},
        "confirmation": {"every": "monthly", "fields_per_run": 5},
    }), encoding="utf-8")

    hoy = dt.date(2026, 9, 30)
    d1 = due(cfg, tmp, hoy)
    for que in ("sweep", "report", "confirmation"):
        ran(tmp, que, hoy)
    d2 = due(cfg, tmp, hoy)
    d3 = due(cfg, tmp, dt.date(2026, 10, 13))

    vacio = tmp / "vacio.json"
    vacio.write_text(json.dumps({"cycle": {}, "confirmation": {}}), encoding="utf-8")
    d4 = due(vacio, tmp, hoy)

    # La cola del servidor. Una petición que nadie lee es peor que no tenerla:
    # alguien preguntó y se quedó esperando. Por eso rompe el silencio.
    (tmp / "peticiones").mkdir(exist_ok=True)
    (tmp / "peticiones" / "p1.json").write_text(json.dumps(
        {"id": "p1", "recibida": "2026-09-29T10:00:00+00:00", "asunto": "explicar",
         "texto": "¿de dónde sale el verde?", "respondida": None}), encoding="utf-8")
    (tmp / "peticiones" / "p0.json").write_text(json.dumps(
        {"id": "p0", "recibida": "2026-09-20T10:00:00+00:00", "asunto": "revisar",
         "texto": "ya contestada", "respondida": "2026-09-21"}), encoding="utf-8")
    d5 = due(vacio, tmp, hoy)
    responder_peticion(tmp, "p1", hoy)
    d6 = due(vacio, tmp, hoy)

    salida = [
        ("cadencia · toca hoy", sorted(d1["due"]), ["confirmation", "report", "sweep"]),
        ("cadencia · el comité rueda", d1["detail"]["committee"]["next"], "2026-10-01"),
        ("cadencia · el informe se anticipa", d1["detail"]["committee"]["report_on"], "2026-09-29"),
        ("cadencia · ya corrido, se calla", d2["quiet"], True),
        ("cadencia · y dice cuándo vuelve", d2["next_wake"], "2026-10-01"),
        ("cadencia · dos semanas después", sorted(d3["due"]), ["report", "sweep"]),
        ("cadencia · sin configurar, nada", d4["due"], []),
        ("cadencia · sin configurar, sin cita", d4["next_wake"], None),
        ("cola · una petición abierta rompe el silencio", d5["due"], ["requests"]),
        ("cola · dice cuántas y desde cuándo", d5["detail"]["requests"]["open"], 1),
        ("cola · la respondida no cuenta", [r["id"] for r in peticiones_abiertas(tmp)], []),
        ("cola · respondida, vuelve a callarse", d6["quiet"], True),
    ] + _pruebas_contraste() + _pruebas_impacto() + [
    ]
    shutil.rmtree(tmp)
    return salida


# ---------------------------------------------------------------- cli

def load_thresholds(config: Path | None) -> dict:
    th = dict(DEFAULT_THRESHOLDS)
    if config and config.exists():
        cfg = json.loads(config.read_text(encoding="utf-8"))
        th.update(cfg.get("thresholds", {}))
    return th


def main() -> int:
    ap = argparse.ArgumentParser(description="Criterio PMO — arithmetic over project records.")
    ap.add_argument("action", choices=["init", "config", "due", "ran", "corrida",
                                       "corrida-inicio", "index", "compute", "snapshot",
                                       "diff", "requests", "answered", "impact",
                                       "historia", "selftest"])
    ap.add_argument("--state", type=Path, help="state directory holding records/ and snapshots/")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--docs", type=Path, default=None,
                    help="carpeta de documentación, para `index`")
    ap.add_argument("--what", default=None,
                    help="qué se corrió: sweep | report | confirmation | requests, para `ran`")
    ap.add_argument("--informe", type=Path, default=None,
                    help="dónde quedó el informe, para `corrida`")
    ap.add_argument("--salida", type=Path, default=None,
                    help="archivo con el resultado completo del comando, para `corrida`")
    ap.add_argument("--nota", default=None,
                    help="qué se movió, qué se omitió, qué hay que mirar, para `corrida`")
    ap.add_argument("--id", default=None,
                    help="identificador de la petición, para `answered`")
    ap.add_argument("--code", default=None,
                    help="código del proyecto que se mueve, para `impact`")
    ap.add_argument("--days", type=int, default=0,
                    help="días que se mueve, para `impact`")
    ap.add_argument("--against", type=Path, default=None)
    ap.add_argument("--today", default=None)
    args = ap.parse_args()

    if args.action == "selftest":
        return selftest()

    if args.action == "config":
        if not args.config:
            ap.error("--config is required")
        result = check_config(args.config)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["ok"] else 1

    if args.action == "init":
        if not args.state:
            ap.error("--state is required")
        print(json.dumps(init(args.state), ensure_ascii=False, indent=2))
        return 0

    if not args.state:
        ap.error("--state is required")
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    if args.action == "due":
        print(json.dumps(due(args.config, args.state, today), ensure_ascii=False, indent=2))
    elif args.action == "ran":
        if not args.what:
            ap.error("--what es obligatorio para ran")
        print(json.dumps(ran(args.state, args.what, today), ensure_ascii=False, indent=2))
    elif args.action == "historia":
        print(json.dumps(historia(args.state, todos=True), ensure_ascii=False, indent=2))
    elif args.action == "corrida-inicio":
        print(json.dumps(corrida_inicio(args.state), ensure_ascii=False))
    elif args.action == "corrida":
        if not args.what:
            ap.error("--what es obligatorio para corrida: sweep | report | confirmation")
        print(json.dumps(corrida(args.state, args.what, today, args.docs,
                                 args.informe, args.nota, args.salida),
                         ensure_ascii=False, indent=2))
    elif args.action == "impact":
        if not args.code:
            ap.error("--code es obligatorio para impact")
        print(json.dumps(impacto(args.state, args.code, args.days, today),
                         ensure_ascii=False, indent=2))
    elif args.action == "requests":
        print(json.dumps(peticiones_abiertas(args.state), ensure_ascii=False, indent=2))
    elif args.action == "answered":
        if not args.id:
            ap.error("--id es obligatorio para answered")
        print(json.dumps(responder_peticion(args.state, args.id, today),
                         ensure_ascii=False, indent=2))
    elif args.action == "index":
        if not args.docs:
            ap.error("--docs es obligatorio para index")
        print(json.dumps(index(args.docs, args.state), ensure_ascii=False, indent=2))
    elif args.action == "compute":
        print(json.dumps(compute(args.state, today, load_thresholds(args.config)),
                         ensure_ascii=False, indent=2))
    elif args.action == "snapshot":
        print(json.dumps({"written": str(snapshot(args.state, today))}, ensure_ascii=False))
    elif args.action == "diff":
        print(json.dumps(diff(args.state, args.against), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
