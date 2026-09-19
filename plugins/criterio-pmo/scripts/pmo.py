#!/usr/bin/env python3
"""Criterio PMO — the arithmetic layer.

The model extracts; this computes. Reading a date off a page is reading.
Subtracting days, projecting variance and adding committed against executed is
arithmetic, and arithmetic belongs here, where it is deterministic and testable.

Usage:
    python3 pmo.py init     --state <dir>
    python3 pmo.py config   --config <file>
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
import json
import sys
from pathlib import Path

DEFAULT_THRESHOLDS = {
    "silent_days": 15,
    "variance_time_pct": 10,
    "variance_cost_pct": 10,
    "committed_pct": 90,
    "stale_field_months": 12,
}

# Signals that always speak, with no number attached.
ALWAYS = ("milestone_overdue", "commitment_overdue", "contradiction", "governance_change")


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


def pct(part, whole):
    if part is None or not whole:
        return None
    return round(part / whole * 100, 1)


def walk_fields(node, path=""):
    """Yield (path, field) for every {value,...} object in the record."""
    if isinstance(node, dict):
        if "value" in node and "state" in node:
            yield path, node
            return
        for k, v in node.items():
            yield from walk_fields(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_fields(v, f"{path}[{i}]")


# ---------------------------------------------------------------- compute

def compute_record(rec: dict, today: dt.date, th: dict) -> dict:
    code = value(rec.get("identity", {}).get("code")) or "?"
    out = {"code": code, "name": value(rec.get("identity", {}).get("name")), "alerts": []}

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
    late = []
    for c in rec.get("commitments") or []:
        due = as_date(c.get("due_date"))
        st = value(c.get("state"))
        if due and due < today and st in (None, "open", "unknown"):
            late.append({"who": value(c.get("who")), "what": value(c.get("what")),
                         "due": due.isoformat(), "days": (today - due).days,
                         "source": source_of(c.get("what")) or value(c.get("source"))})
    out["commitments_overdue"] = late
    for c in late:
        alert("commitment_overdue", c)

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
    for c in conflicts:
        alert("contradiction", c)

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

    return {
        "as_of": today.isoformat(),
        "thresholds": th,
        "projects": projects,
        "totals": {
            "projects": len(projects),
            "with_alerts": sum(1 for p in projects if p["alerts"]),
            "alerts": sum(len(p["alerts"]) for p in projects),
            "no_baseline": sum(1 for p in projects if not p["has_baseline"]),
        },
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
                {"version": 1, "end_date": "2026-09-30", "reason": "inicial"},
                {"version": 2, "end_date": "2026-11-30", "reason": "atraso proveedor"},
            ],
            "milestones": [
                {"name": {"value": "Hito 1"}, "current_date": {"value": "2026-08-15"},
                 "state": {"value": "pending"}, "evidence": {"value": None}},
                {"name": {"value": "Hito 2"}, "current_date": {"value": "2026-07-01"},
                 "state": {"value": "met"}, "evidence": {"value": "acta.md"}},
            ],
        },
        "money": {"currency": {"value": "COP"}, "approved": {"value": 1000},
                  "committed": {"value": 950}, "executed": {"value": 400},
                  "projection": {"value": 1200}},
        "commitments": [
            {"who": {"value": "Carlos"}, "what": {"value": "Propuesta"},
             "due_date": {"value": "2026-09-05"}, "state": {"value": "open"},
             "source": {"value": "min.md"}},
        ],
        "activity": {"last_document_date": {"value": "2026-08-20"}},
        "raid": {"dependencies": [{"on_project": {"value": "PRY-002"}, "confirmed": {"value": False}}]},
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
        ("señales", kinds, ["budget_committed", "commitment_overdue",
                            "milestone_overdue", "silent", "variance_cost", "variance_time"]),
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
    ap.add_argument("action", choices=["init", "config", "compute", "snapshot", "diff", "selftest"])
    ap.add_argument("--state", type=Path, help="state directory holding records/ and snapshots/")
    ap.add_argument("--config", type=Path, default=None)
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

    if args.action == "compute":
        print(json.dumps(compute(args.state, today, load_thresholds(args.config)),
                         ensure_ascii=False, indent=2))
    elif args.action == "snapshot":
        print(json.dumps({"written": str(snapshot(args.state, today))}, ensure_ascii=False))
    elif args.action == "diff":
        print(json.dumps(diff(args.state, args.against), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
