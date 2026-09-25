#!/usr/bin/env python3
"""Criterio PMO — the arithmetic layer.

The model extracts; this computes. Reading a date off a page is reading.
Subtracting days, projecting variance and adding committed against executed is
arithmetic, and arithmetic belongs here, where it is deterministic and testable.

Usage:
    python3 pmo.py init     --state <dir>
    python3 pmo.py config   --config <file>
    python3 pmo.py index    --state <dir> --docs <dir>
    python3 pmo.py compute  --state <dir> [--config <file>] [--today YYYY-MM-DD]
    python3 pmo.py snapshot --state <dir> [--today YYYY-MM-DD]
    python3 pmo.py diff     --state <dir> [--against <snapshot.json>]
    python3 pmo.py selftest

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

# The signals a status light is supposed to account for. `contradiction` is
# deliberately out: it is a defect of the record, not of the project, and
# mixing the two weakens the finding.
EVIDENCE_SIGNALS = (
    "silent", "variance_time", "variance_cost", "milestone_overdue",
    "commitment_overdue", "commitment_rescheduled", "budget_committed",
    "vendor_deliverable_late", "vendor_invoiced_without_delivery",
    "vendor_invoiced_over_accepted", "rebaseline_unauthorized",
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
    overdue = []
    for m in plan.get("milestones") or []:
        due = as_date(m.get("current_date")) or as_date(m.get("baseline_date"))
        st = value(m.get("state"))
        evidence = value(m.get("evidence"))
        if due and due < today and st != "met" and not evidence:
            overdue.append({"name": value(m.get("name")), "due": due.isoformat(),
                            "days": (today - due).days})
    out["milestones_overdue"] = overdue
    for m in overdue:
        alert("milestone_overdue", m)

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
    out["conflicts"] = conflicts
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

    return out


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
    log = state / "registro.log"
    if not log.exists():
        log.write_text("", encoding="utf-8")
        created.append(str(log))
    return {"state": str(state), "created": created,
            "already_there": not created}


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
    ok = True
    for label, got, want in checks:
        good = got == want
        ok &= good
        print(f"  {'OK ' if good else 'FALLA'} {label:32} {got!r}{'' if good else f'  esperado {want!r}'}")
    print("\nselftest:", "sin errores" if ok else "CON ERRORES")
    return 0 if ok else 1


# ---------------------------------------------------------------- cli

def load_thresholds(config: Path | None) -> dict:
    th = dict(DEFAULT_THRESHOLDS)
    if config and config.exists():
        cfg = json.loads(config.read_text(encoding="utf-8"))
        th.update(cfg.get("thresholds", {}))
    return th


def main() -> int:
    ap = argparse.ArgumentParser(description="Criterio PMO — arithmetic over project records.")
    ap.add_argument("action", choices=["init", "config", "index", "compute",
                                       "snapshot", "diff", "selftest"])
    ap.add_argument("--state", type=Path, help="state directory holding records/ and snapshots/")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--docs", type=Path, default=None,
                    help="carpeta de documentación, para `index`")
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

    if args.action == "index":
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
