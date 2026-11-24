#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CAE: lo que calcula el código para Prudencia, Justo y Remedios.

    python3 auditoria.py <acción> [opciones]       python3 auditoria.py --help

Prudencia (criterio-audit-plan) procesa el plan de auditoría: cada riesgo alto de la matriz contra
los trabajos del plan, cada unidad del universo auditable contra su ciclo, la edad de la evaluación de
riesgos, las áreas que el plan tiene que considerar, cada cambio contra el acta que lo aprueba, cada
trabajo contra sus fechas, las horas contra la capacidad del equipo, el requisito temático vigente y la
evaluación externa de calidad. Justo (criterio-audit-work), los trabajos: el programa y su aprobación,
cada hallazgo con sus elementos y su papel, cada paso con su papel, cada papel con su revisión, el
informe contra los papeles, la prioridad contra la metodología y la objetividad de cada asignación.
Remedios (criterio-remediation), el seguimiento: cada plan de acción con su responsable, su fecha y su
evidencia, las reprogramaciones, los cierres, los hallazgos que vuelven, los riesgos aceptados y los
hallazgos externos. Los tres comparten este motor, que vive en criterio-audit-plan y se copia a los
otros dos con scripts/sincronizar.py, y el núcleo común de las familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —el universo, la matriz de
riesgos, el plan, el equipo, el programa y el índice de papeles de cada trabajo, el registro de
hallazgos y el de riesgos aceptados— las procesa el código. Lo que solo trae un documento escrito
—las actas del comité, cada hallazgo de los papeles y del informe, las evidencias y las explicaciones
de atraso, los hallazgos de un informe externo— lo extrae el agente a su ficha, con la cita, y el
código lo cruza.

**La opinión es del auditor** (decisión 0033): el motor no concluye sobre el control interno, no
cambia la prioridad de un hallazgo y no cierra nada. **Los ciclos, los plazos, la escala de prioridad
y el apetito de riesgo los fija la organización**, en su metodología; lo que viene de fuera es la
estructura de las Normas Globales de Auditoría Interna de The IIA (2024) —se citan su número y su
título, nunca su texto— y las fechas de vigencia de sus requisitos temáticos.

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
from nucleo import (  # noqa: E402
    _csv, _hoy, _xlsx, alerta, escribir_json, fecha, filas_de, iso, leer_json, marco_reporte, norm, numero,
    ordenar, registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"
SUB = {"prudencia": "plan", "justo": "trabajos", "remedios": "seguimiento"}
NOMBRE = {"prudencia": "Prudencia", "justo": "Justo", "remedios": "Remedios"}
NORMAS = "Normas Globales de Auditoría Interna (The IIA, 2024)"

# Los requisitos temáticos de The IIA y el día desde el que rigen (F-02, verificado el 2026-11-24):
# obligatorios para un trabajo de aseguramiento sobre su tema que empieza desde esa fecha.
REQUISITOS_TEMATICOS = {
    "ciberseguridad": {"nombre": "Ciberseguridad", "desde": dt.date(2026, 2, 5), "temas": ("ciberseguridad", "cybersecurity", "seguridad_de_la_informacion")},
    "terceros": {"nombre": "Terceros", "desde": dt.date(2026, 9, 15), "temas": ("terceros", "third_party", "third_parties", "proveedores")},
    "comportamiento": {"nombre": "Comportamiento Organizacional", "desde": dt.date(2026, 12, 15), "temas": ("comportamiento_organizacional", "organizational_behavior", "cultura")},
    "resiliencia": {"nombre": "Resiliencia Organizacional", "desde": dt.date(2027, 4, 30), "temas": ("resiliencia", "resilience", "continuidad")},
    "anticorrupcion": {"nombre": "Anticorrupción", "desde": dt.date(2027, 11, 23), "temas": ("anticorrupcion", "anti_corruption", "soborno")},
}
# Lo que la norma 9.4 pide que el plan considere, con las palabras con que un plan lo nombra.
AREAS_94 = {
    "ti": {"nombre": "el gobierno de TI", "temas": ("ti", "gobierno_de_ti", "tecnologia", "it", "it_governance", "ciberseguridad", "cybersecurity")},
    "fraude": {"nombre": "el riesgo de fraude", "temas": ("fraude", "fraud", "antifraude")},
    "cumplimiento": {"nombre": "los programas de cumplimiento y ética", "temas": ("cumplimiento", "etica", "compliance", "ethics", "sarlaft", "lavado")},
}
EXTERNA_ANIOS = 5          # norma 8.4: al menos una vez cada cinco años
EVALUACION_DIAS = 365      # norma 9.4: la evaluación de riesgos, al menos una vez al año
OBJETIVIDAD_DIAS = 365     # norma 2.2: lo que tuvo a su cargo en los doce meses anteriores

CANCELADO = ("cancelado", "cancelada", "cancelled", "canceled", "anulado")
TERMINADO = ("terminado", "terminada", "cerrado", "cerrada", "finalizado", "emitido", "completed", "closed", "done")
EN_CURSO = ("en_curso", "en_ejecucion", "ejecucion", "in_progress", "fieldwork", "campo")
CERRADO = ("cerrado", "cerrada", "closed", "implementado", "implementada", "resuelto")
SI = ("si", "sí", "x", "yes", "true", "1", "s")


def _si(v) -> bool:
    return norm(v) in SI


def _lista(v) -> list[str]:
    return [x.strip() for x in re.split(r"[;,/|]", str(v or "")) if x.strip()]


def _temas(v) -> set[str]:
    return {norm(x) for x in _lista(v)}


# ================================================================ las tablas

class Hoja:
    """Una tabla con sus columnas canónicas, por su cabecera o por el mapeo de la configuración, y la
    fila de origen de cada dato para citarla."""

    def __init__(self, ruta: Path, requeridas: list[str], opcionales: list[str], alias: dict, columnas: dict | None = None):
        self.ruta, self.faltan, self.filas, self.mapa = ruta, [], [], {}
        filas = filas_de(ruta)
        fijas = {k: norm(v) for k, v in (columnas or {}).items() if v}
        cand = {c: ([fijas[c]] if c in fijas else [norm(x) for x in alias.get(c, [c])]) for c in list(requeridas) + list(opcionales)}
        if not filas:
            self.faltan = list(requeridas)
            return
        inicio = 0
        for i, f in enumerate(filas[:15]):
            if any(set(cand[c]) & {norm(x) for x in f} for c in requeridas):
                inicio = i
                break
        cab = [norm(x) for x in filas[inicio]]
        for campo, cs in cand.items():
            for c in cs:
                if c in cab and cab.index(c) not in self.mapa.values():
                    self.mapa[campo] = cab.index(c)
                    break
        self.faltan = [c for c in requeridas if c not in self.mapa]
        if self.faltan:
            return
        for k, f in enumerate(filas[inicio + 1:], start=inicio + 2):
            if not any(str(x).strip() for x in f):
                continue
            d = {c: (str(f[i]).strip() if i < len(f) and f[i] is not None else "") for c, i in self.mapa.items()}
            if not all(d.get(c) for c in requeridas):
                continue
            d["_fila"] = k
            self.filas.append(d)

    def cita(self, x: dict, docs: Path) -> dict:
        return {"archivo": rel(self.ruta, docs), "fila": x.get("_fila")}


def hallar(carpeta: Path, *patrones: str) -> list[Path]:
    """Las tablas de una carpeta cuyo nombre lleva alguno de los patrones."""
    if not carpeta.is_dir():
        return []
    return sorted(p for p in carpeta.rglob("*") if p.is_file() and p.suffix.lower() in (".csv", ".xlsx")
                  and not p.name.startswith((".", "~$")) and any(x in norm(p.stem) for x in patrones))


def leer_tabla(docs: Path, carpeta: str, patrones: tuple, requeridas: list, opcionales: list, alias: dict,
               cfg: dict, no_proc: list, que: str, ruta: Path | None = None) -> Hoja | None:
    rutas = [ruta] if ruta else hallar(docs / carpeta, *patrones)
    if not rutas:
        return None
    t = Hoja(rutas[-1], requeridas, opcionales, alias, (cfg.get("columns") or {}).get(que))
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"{que}: no trae una columna reconocible para {', '.join(t.faltan)}; "
                                                                f"di cuál es en la configuración (columns.{que})"})
        return None
    return t


ALIAS = {
    "universo": {"unidad": ["unidad", "unidad_auditable", "id", "codigo", "auditable_unit", "unit"],
                 "nombre": ["nombre", "descripcion", "proceso", "name"],
                 "nivel": ["nivel", "riesgo", "nivel_de_riesgo", "calificacion", "risk_level", "rating"],
                 "ultimo": ["ultimo_trabajo", "ultima_auditoria", "fecha_ultima_auditoria", "last_audit", "last_engagement"]},
    "matriz": {"riesgo": ["riesgo", "id_riesgo", "id", "codigo", "risk_id", "risk"],
               "descripcion": ["descripcion", "nombre", "description"],
               "calificacion": ["calificacion", "nivel", "riesgo_residual", "residual", "rating", "level"],
               "unidad": ["unidad", "unidad_auditable", "proceso", "unit", "process"]},
    "plan": {"trabajo": ["trabajo", "codigo", "id", "id_trabajo", "engagement", "engagement_id"],
             "nombre": ["nombre", "titulo", "descripcion", "name", "title"],
             "unidad": ["unidad", "unidad_auditable", "proceso", "unit"],
             "riesgos": ["riesgos", "riesgos_cubiertos", "risks"],
             "tipo": ["tipo", "tipo_de_trabajo", "type"],
             "temas": ["tema", "temas", "area", "topic", "topics"],
             "inicio": ["inicio", "fecha_inicio", "start", "start_date"],
             "cierre": ["cierre", "fecha_cierre", "fin", "end", "end_date"],
             "estado": ["estado", "status"],
             "horas": ["horas", "horas_planeadas", "hours", "budget_hours"],
             "requisito": ["requisito_tematico", "requisitos_tematicos", "topical_requirement"],
             "cambio": ["cambio", "modificacion", "change"]},
    "equipo": {"auditor": ["auditor", "nombre", "persona", "id", "name"],
               "horas": ["horas_disponibles", "horas", "capacidad", "available_hours", "hours"]},
    "cargos": {"auditor": ["auditor", "nombre", "persona", "name"],
               "unidad": ["unidad", "actividad", "area", "proceso", "unit"],
               "desde": ["desde", "inicio", "from", "start"],
               "hasta": ["hasta", "fin", "to", "end"]},
    "asignaciones": {"trabajo": ["trabajo", "codigo", "engagement"],
                     "auditor": ["auditor", "nombre", "persona", "name"],
                     "unidad": ["unidad", "actividad_auditada", "unit"],
                     "inicio": ["inicio", "fecha", "fecha_inicio", "start"],
                     "tipo": ["tipo", "type"]},
    "programa": {"paso": ["paso", "procedimiento", "id", "step"],
                 "objetivo": ["objetivo", "descripcion", "objective"],
                 "papel": ["papel", "papel_de_trabajo", "referencia", "pt", "workpaper"],
                 "no_aplica": ["no_aplica", "razon_no_aplica", "justificacion", "not_applicable"]},
    "papeles": {"papel": ["papel", "referencia", "pt", "id", "workpaper"],
                "paso": ["paso", "procedimiento", "step"],
                "fecha": ["fecha", "fecha_preparacion", "preparado_el", "date", "prepared_on"],
                "revisado_por": ["revisado_por", "revisor", "reviewed_by"],
                "fecha_revision": ["fecha_revision", "revisado_el", "reviewed_on"],
                "aprobado_por": ["aprobado_por", "aprobo", "approved_by"],
                "fecha_aprobacion": ["fecha_aprobacion", "aprobado_el", "approved_on"]},
    "hallazgos": {"hallazgo": ["hallazgo", "id", "codigo", "finding", "finding_id"],
                  "trabajo": ["trabajo", "engagement"],
                  "origen": ["origen", "fuente", "source"],
                  "proceso": ["proceso", "unidad", "process", "unit"],
                  "condicion": ["condicion", "titulo", "descripcion", "condition", "title"],
                  "prioridad": ["prioridad", "calificacion", "priority", "rating"],
                  "comunicado": ["comunicado", "fecha_comunicado", "fecha_informe", "reported_on"],
                  "plan": ["plan", "plan_de_accion", "action_plan"],
                  "responsable": ["responsable", "dueno", "owner"],
                  "fecha": ["fecha_compromiso", "fecha_limite", "vence", "due_date"],
                  "reprogramaciones": ["reprogramaciones", "cambios_de_fecha", "reschedules"],
                  "estado": ["estado", "status"],
                  "cierre": ["fecha_cierre", "cerrado_el", "closed_on"],
                  "validado_por": ["validado_por", "validacion", "validated_by"],
                  "referencia": ["referencia_externa", "referencia", "external_ref"]},
    "aceptados": {"riesgo": ["riesgo", "id", "codigo", "risk"],
                  "descripcion": ["descripcion", "nombre", "description"],
                  "fecha": ["fecha", "fecha_aceptacion", "accepted_on"],
                  "encima": ["por_encima_del_apetito", "encima_apetito", "excede_apetito", "above_appetite"],
                  "discutido": ["discutido_alta_direccion", "alta_direccion", "discussed_senior_management"],
                  "resuelto": ["resuelto", "resolved"],
                  "consejo": ["escalado_consejo", "consejo", "junta", "escalated_board"]},
}
REQ = {
    "universo": ["unidad"], "matriz": ["riesgo", "calificacion"], "plan": ["trabajo"], "equipo": ["auditor", "horas"],
    "cargos": ["auditor", "unidad"], "asignaciones": ["trabajo", "auditor"], "programa": ["paso"], "papeles": ["papel"],
    "hallazgos": ["hallazgo"], "aceptados": ["riesgo"],
}
PATRONES = {
    "universo": ("universo", "universe"), "matriz": ("matriz", "risk_matrix", "riesgos_de"), "plan": ("plan_anual", "plan_de_auditoria", "plan"),
    "equipo": ("equipo", "team"), "cargos": ("cargos", "historia"), "asignaciones": ("asignaciones", "assignments"),
    "programa": ("programa", "program"), "papeles": ("indice", "papeles", "workpapers"),
    "hallazgos": ("registro_hallazgos", "hallazgos", "findings"), "aceptados": ("riesgos_aceptados", "accepted"),
}
CARPETA = {"universo": "10-plan", "matriz": "10-plan", "plan": "10-plan", "equipo": "00-referencia", "cargos": "00-referencia",
           "asignaciones": "20-trabajos", "hallazgos": "30-seguimiento", "aceptados": "30-seguimiento"}


def tabla(cfg: dict, que: str, no_proc: list, ruta: Path | None = None) -> Hoja | None:
    docs = cfg["_docs"]
    if que == "plan" and not ruta:
        # El plan no es la matriz ni el universo, aunque lleven «plan» en otra parte del nombre.
        rutas = [p for p in hallar(docs / "10-plan", *PATRONES["plan"]) if not any(x in norm(p.stem) for x in PATRONES["matriz"] + PATRONES["universo"])]
        ruta = rutas[-1] if rutas else None
        if not ruta:
            return None
    if que == "equipo" and not ruta:
        rutas = [p for p in hallar(docs / "00-referencia", *PATRONES["equipo"]) if not any(x in norm(p.stem) for x in PATRONES["cargos"])]
        ruta = rutas[-1] if rutas else None
        if not ruta:
            return None
    return leer_tabla(docs, CARPETA.get(que, ""), PATRONES[que], REQ[que], [c for c in ALIAS[que] if c not in REQ[que]], ALIAS[que],
                      cfg, no_proc, que, ruta)


# ================================================================ la configuración

DEFECTOS = {"report": {"language": "es"}, "methodology": {"max_reschedules": 2}}
SEVERIDAD = {
    "high_risk_not_covered": 1, "risk_accepted_not_escalated": 1, "closure_without_evidence": 1, "report_differs_from_workpapers": 1,
    "auditable_unit_overdue": 2, "plan_change_unapproved": 2, "action_plan_overdue": 2, "finding_element_missing": 2,
    "finding_without_workpaper": 2, "auditor_reviews_own_work": 2, "external_finding_untracked": 2, "finding_repeated": 2,
    "topical_requirement_missing": 2, "action_plan_missing": 2, "work_program_not_approved": 2,
    "risk_assessment_outdated": 3, "plan_area_not_considered": 3, "engagement_behind_schedule": 3, "plan_hours_exceed_capacity": 3,
    "external_assessment_overdue": 3, "procedure_not_executed": 3, "workpaper_not_reviewed": 3, "rating_inconsistent": 3,
    "due_date_extended_repeatedly": 3,
}
N.SEVERIDAD.update(SEVERIDAD)


def metodologia(cfg: dict) -> dict:
    return cfg.get("methodology") or {}


def ciclos(cfg: dict) -> dict[str, float]:
    """Los meses del ciclo de rotación de cada nivel de riesgo, como los fija la metodología."""
    return {norm(k): numero(v) for k, v in (metodologia(cfg).get("cycles_months") or {}).items() if numero(v)}


def altos(cfg: dict) -> set[str]:
    return {norm(x) for x in metodologia(cfg).get("high_ratings") or []}


def escala(cfg: dict) -> list[tuple[str, float]]:
    """La escala de prioridad: cada nivel con el puntaje mínimo de impacto por probabilidad, de mayor a menor."""
    niveles = (metodologia(cfg).get("priority") or {}).get("levels") or []
    out = [(norm(n), numero(m)) for n, m in niveles if numero(m) is not None]
    return sorted(out, key=lambda x: -x[1])


def prioridad_de(cfg: dict, impacto, probabilidad) -> str | None:
    i, p = numero(impacto), numero(probabilidad)
    if i is None or p is None or not escala(cfg):
        return None
    puntaje = i * p
    for nivel, minimo in escala(cfg):
        if puntaje >= minimo:
            return nivel
    return None


def revisar_config(cfg: dict, rol: str) -> list[str]:
    p = []
    ent = cfg.get("entity") or {}
    for k in ("name", "country"):
        if not ent.get(k):
            p.append(f"entity.{k} vacío")
    p += N.revisar_pais(ent)
    for k, n in (("_docs", "documents"), ("_estado", "state")):
        if cfg.get(k) is None:
            p.append(f"paths.{n} vacío")
    if cfg.get("_docs") and not cfg["_docs"].is_dir():
        p.append(f"la carpeta de documentos {cfg['_docs']} no existe")
    if cfg.get("_docs") and cfg.get("_estado"):
        try:
            cfg["_estado"].resolve().relative_to(cfg["_docs"].resolve())
            p.append("el estado no puede vivir dentro de la carpeta de documentos: ahí lo tomaría por un documento")
        except ValueError:
            pass
    if not re.fullmatch(r"\d{4}-\d{2}", str(cfg.get("period") or "")):
        p.append("period vacío: el periodo que se evalúa, AAAA-MM")
    m = metodologia(cfg)
    if rol == "prudencia":
        if not ciclos(cfg):
            p.append("methodology.cycles_months vacío: los meses del ciclo de rotación de cada nivel de riesgo, como los fija la metodología")
        if not altos(cfg):
            p.append("methodology.high_ratings vacío: desde qué calificación de la matriz un riesgo es alto")
    if rol == "justo" and not escala(cfg):
        p.append("methodology.priority.levels vacío: cada nivel de prioridad con el puntaje mínimo de impacto por probabilidad")
    if rol == "remedios" and numero(m.get("max_reschedules")) is None:
        p.append("methodology.max_reschedules vacío: cuántas veces permite la metodología correr la fecha de un plan de acción")
    return p


def _ficha(cfg: dict, rol: str, periodo: str) -> dict:
    return leer_json(cfg["_estado"] / SUB[rol] / periodo / "ficha.json", {}) or {}


def _cita(src) -> dict | None:
    if not src:
        return None
    return {"archivo": str(src).split(",")[0].strip()}


def _sin_ficha(docs: Path, carpeta: str, citadas: set, aviso: str) -> list[str]:
    """Los documentos de una carpeta que la ficha no cita: se le dice a quien la escribe."""
    out = []
    citadas = {str(s).split(",")[0].strip() for s in citadas}
    base = docs / carpeta
    for p in sorted(x for x in base.rglob("*") if x.is_file() and not x.name.startswith(".")) if base.is_dir() else []:
        if p.suffix.lower() in (".csv", ".xlsx"):
            continue
        if rel(p, docs) not in citadas:
            out.append(f"{rel(p, docs)} no está en la ficha: {aviso}")
    return out


def _meses(d: dt.date, n: float) -> dt.date:
    m = d.month - 1 + int(n)
    return dt.date(d.year + m // 12, m % 12 + 1, min(d.day, 28))


# ================================================================ Prudencia · el plan

def prudencia(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "prudencia", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    m = metodologia(cfg)
    universo, matriz, plan, equipo = (tabla(cfg, q, no_proc) for q in ("universo", "matriz", "plan", "equipo"))
    for q, t in (("universo", universo), ("matriz", matriz), ("plan", plan)):
        if t is None and not any(x["motivo"].startswith(q) for x in no_proc):
            no_proc.append({"archivo": "10-plan", "motivo": f"no está la tabla de {q}: sin ella no se calcula lo que depende de ella"})
    aprobaciones = ficha.get("approvals") or []
    citadas = {str(a.get("source")) for a in aprobaciones} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, "10-plan", citadas, "es un acta o un documento del plan; corre plan-scan")
    for a in aprobaciones:
        if not (a.get("engagement") and a.get("change") and a.get("source")):
            problemas.append(f"una aprobación de la ficha no trae trabajo, cambio o cita: {json.dumps(a, ensure_ascii=False)[:160]}")

    activos = [x for x in (plan.filas if plan else []) if norm(x.get("estado")) not in CANCELADO]
    trabajos = []
    # 1 · Cada riesgo alto contra los trabajos del plan.
    alto = altos(cfg)
    riesgos = []
    for r in matriz.filas if matriz else []:
        cal = norm(r.get("calificacion"))
        cubre = [x["trabajo"] for x in activos if r["riesgo"] in _lista(x.get("riesgos")) or (r.get("unidad") and norm(r.get("unidad")) == norm(x.get("unidad")))]
        riesgos.append({"riesgo": r["riesgo"], "descripcion": r.get("descripcion"), "calificacion": r.get("calificacion"), "unidad": r.get("unidad"),
                        "trabajos": cubre, "alto": cal in alto})
        if cal in alto and not cubre:
            al.append(alerta("high_risk_not_covered", f"{r['riesgo']} · {r.get('descripcion') or ''}: calificado {r.get('calificacion')} en la matriz y "
                             f"ningún trabajo del plan lo cubre (norma 9.4)", matriz.cita(r, docs), clave=f"riesgo:{r['riesgo']}"))
    # 2 · Cada unidad del universo contra su ciclo.
    cic = ciclos(cfg)
    unidades = []
    for u in universo.filas if universo else []:
        meses = cic.get(norm(u.get("nivel")))
        ultimo = fecha(u.get("ultimo"))
        tope = _meses(ultimo, meses) if ultimo and meses else None
        planeada = [x["trabajo"] for x in activos if norm(x.get("unidad")) == norm(u["unidad"])]
        unidades.append({"unidad": u["unidad"], "nombre": u.get("nombre"), "nivel": u.get("nivel"), "ultimo": iso(ultimo), "ciclo": meses,
                         "tope": iso(tope), "planeada": planeada})
        if meses is None:
            if u.get("nivel"):
                no_proc.append({"archivo": rel(universo.ruta, docs), "motivo": f"{u['unidad']}: el nivel «{u.get('nivel')}» no tiene ciclo en la metodología (methodology.cycles_months)"})
            continue
        if planeada:
            continue
        if not ultimo:
            al.append(alerta("auditable_unit_overdue", f"{u['unidad']} · {u.get('nombre') or ''}: no tiene un trabajo registrado y no está en el plan; "
                             f"su ciclo es de {int(meses)} meses", universo.cita(u, docs), clave=f"unidad:{u['unidad']}"))
        elif tope < hoy:
            al.append(alerta("auditable_unit_overdue", f"{u['unidad']} · {u.get('nombre') or ''}: el último trabajo fue el {iso(ultimo)}, su ciclo de "
                             f"{int(meses)} meses venció el {iso(tope)} y no está en el plan", universo.cita(u, docs), dias=(hoy - tope).days,
                             clave=f"unidad:{u['unidad']}"))
    # 3 · La evaluación de riesgos que sostiene el plan (norma 9.4: al menos una vez al año).
    ev = fecha(m.get("risk_assessment_date"))
    if not ev:
        no_proc.append({"archivo": "configuración", "motivo": "sin la fecha de la última evaluación de riesgos (methodology.risk_assessment_date) no se sabe si tiene más de un año"})
    elif (hoy - ev).days > EVALUACION_DIAS:
        al.append(alerta("risk_assessment_outdated", f"la evaluación de riesgos que sostiene el plan es del {iso(ev)}: tiene {(hoy - ev).days} días, "
                         f"y la norma 9.4 la pide al menos una vez al año", _cita(m.get("risk_assessment_source")), dias=(hoy - ev).days - EVALUACION_DIAS,
                         clave="evaluacion_de_riesgos"))
    # 4 · Lo que el plan tiene que considerar (norma 9.4).
    temas = set().union(*[_temas(x.get("temas")) for x in activos]) if activos else set()
    razones = {norm(k): v for k, v in (ficha.get("areas_not_considered") or {}).items() if v}
    areas = []
    for k, a in AREAS_94.items():
        tiene = bool(temas & set(a["temas"]))
        areas.append({"area": a["nombre"], "considerada": tiene, "razon": razones.get(k)})
        if plan and not tiene and k not in razones:
            al.append(alerta("plan_area_not_considered", f"el plan no considera {a['nombre']} ni dice por qué (norma 9.4)",
                             {"archivo": rel(plan.ruta, docs)}, clave=f"area:{k}"))
    # 5 · Cada cambio al plan contra el acta que lo aprueba.
    aprobado = {(norm(a.get("engagement")), norm(a.get("change"))) for a in aprobaciones if a.get("approved_by")}
    cambios = []
    for x in plan.filas if plan else []:
        c = norm(x.get("cambio"))
        if not c:
            continue
        tipo = "cancela" if c.startswith("cancel") else "aplaza" if c.startswith(("aplaz", "posterg", "postpon")) else "agrega" if c.startswith(("agreg", "nuev", "add", "incl")) else c
        ok = (norm(x["trabajo"]), tipo) in aprobado
        acta = next((a for a in aprobaciones if norm(a.get("engagement")) == norm(x["trabajo"]) and norm(a.get("change")) == tipo), None)
        cambios.append({"trabajo": x["trabajo"], "cambio": tipo, "aprobado": ok, "acta": (acta or {}).get("source"), "por": (acta or {}).get("approved_by")})
        if not ok:
            al.append(alerta("plan_change_unapproved", f"{x['trabajo']} · {x.get('nombre') or ''}: el plan lo {'cancela' if tipo == 'cancela' else 'aplaza' if tipo == 'aplaza' else 'agrega'} "
                             f"y no hay un acta del órgano que aprueba el plan que lo apruebe (norma 9.4)", plan.cita(x, docs), clave=f"cambio:{x['trabajo']}"))
    # 6 · Cada trabajo contra sus fechas.
    for x in activos:
        ini, fin, est = fecha(x.get("inicio")), fecha(x.get("cierre")), norm(x.get("estado"))
        trabajos.append({"trabajo": x["trabajo"], "nombre": x.get("nombre"), "unidad": x.get("unidad"), "inicio": iso(ini), "cierre": iso(fin),
                         "estado": x.get("estado"), "horas": numero(x.get("horas")), "temas": sorted(_temas(x.get("temas")))})
        if est in TERMINADO:
            continue
        if fin and fin < hoy:
            al.append(alerta("engagement_behind_schedule", f"{x['trabajo']} · {x.get('nombre') or ''}: tenía que cerrar el {iso(fin)} y sigue {x.get('estado') or 'sin estado'}",
                             plan.cita(x, docs), dias=(hoy - fin).days, clave=f"atraso:{x['trabajo']}"))
        elif ini and ini < hoy and est not in EN_CURSO:
            al.append(alerta("engagement_behind_schedule", f"{x['trabajo']} · {x.get('nombre') or ''}: tenía que empezar el {iso(ini)} y sigue {x.get('estado') or 'sin estado'}",
                             plan.cita(x, docs), dias=(hoy - ini).days, clave=f"atraso:{x['trabajo']}"))
    # 7 · Las horas del plan contra la capacidad del equipo.
    horas_plan = sum(numero(x.get("horas")) or 0 for x in activos)
    horas_equipo = sum(numero(x.get("horas")) or 0 for x in (equipo.filas if equipo else []))
    if equipo and plan and horas_plan > horas_equipo:
        al.append(alerta("plan_hours_exceed_capacity", f"el plan suma {horas_plan:g} horas y el equipo tiene {horas_equipo:g} disponibles en el periodo: "
                         f"faltan {horas_plan - horas_equipo:g}", [{"archivo": rel(plan.ruta, docs)}, {"archivo": rel(equipo.ruta, docs)}], clave="horas"))
    elif plan and not equipo:
        no_proc.append({"archivo": "00-referencia", "motivo": "sin la tabla del equipo con sus horas disponibles no se compara la capacidad"})
    # 8 · El requisito temático vigente de cada trabajo de aseguramiento.
    for x in activos:
        if norm(x.get("tipo")).startswith(("consult", "advis", "asesor")):
            continue
        ini = fecha(x.get("inicio"))
        for k, rq in REQUISITOS_TEMATICOS.items():
            if not (_temas(x.get("temas")) & set(rq["temas"])) or not ini or ini < rq["desde"]:
                continue
            if not any(norm(rq["nombre"]) in norm(y) or k in norm(y) for y in _lista(x.get("requisito"))):
                al.append(alerta("topical_requirement_missing", f"{x['trabajo']} · {x.get('nombre') or ''}: trabajo de aseguramiento sobre {rq['nombre'].lower()} que empieza el "
                                 f"{iso(ini)}, y el requisito temático de {rq['nombre']} rige desde el {iso(rq['desde'])}; su programa no lo lleva",
                                 plan.cita(x, docs), clave=f"tematico:{x['trabajo']}:{k}"))
    # 9 · La evaluación externa de calidad (norma 8.4: al menos una vez cada cinco años).
    ext = fecha(m.get("external_assessment_date"))
    siguiente = dt.date(ext.year + EXTERNA_ANIOS, ext.month, min(ext.day, 28)) if ext else None
    if not ext:
        al.append(alerta("external_assessment_overdue", "no hay fecha de la última evaluación externa de calidad: la norma 8.4 la pide al menos una vez cada cinco años",
                         _cita(m.get("external_assessment_source")), clave="evaluacion_externa"))
    elif siguiente < hoy:
        al.append(alerta("external_assessment_overdue", f"la última evaluación externa de calidad fue el {iso(ext)}; la siguiente tocaba a más tardar el {iso(siguiente)} (norma 8.4)",
                         _cita(m.get("external_assessment_source")), dias=(hoy - siguiente).days, clave="evaluacion_externa"))

    fuentes = ["F-01"] + (["F-02"] if any(a["signal"] == "topical_requirement_missing" for a in al) else [])
    partes = {
        "plan-scan": {"trabajos": len(activos), "riesgos": len(riesgos), "unidades": len(unidades), "aprobaciones": len(aprobaciones), "fuentes": fuentes},
        "plan-coverage": {"riesgos": riesgos, "unidades": unidades, "areas": areas, "evaluacion": iso(ev), "fuentes": ["F-01"]},
        "plan-status": {"trabajos": trabajos, "cambios": cambios, "fuentes": ["F-01"]},
        "plan-capacity": {"horas_plan": horas_plan, "horas_equipo": horas_equipo if equipo else None, "trabajos": trabajos, "fuentes": fuentes},
        "quality-status": {"ultima": iso(ext), "siguiente": iso(siguiente), "fuentes": ["F-01"]},
    }
    vence = sorted(({"fecha": t["cierre"], "que": f"{t['trabajo']} · cierre del trabajo", "caso": t["trabajo"], "estado": "pendiente", "comando": "plan-status"}
                    for t in trabajos if t["cierre"] and 0 <= (fecha(t["cierre"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "prudencia", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ Justo · los trabajos

def _carpetas_trabajo(docs: Path) -> list[Path]:
    base = docs / "20-trabajos"
    return sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")) if base.is_dir() else []


def _cifras(v) -> list[float]:
    return sorted(x for x in (numero(y) for y in (v if isinstance(v, list) else _lista(v))) if x is not None)


def revisar_ficha_justo(f: dict) -> list[str]:
    p = []
    for e in f.get("engagements") or []:
        if not e.get("id"):
            p.append("un trabajo de la ficha no trae id")
        for h in (e.get("findings") or []) + (e.get("report_findings") or []):
            if not h.get("id"):
                p.append(f"{e.get('id')}: un hallazgo sin id")
            if not h.get("source"):
                p.append(f"{e.get('id')} · {h.get('id')}: sin cita")
    return p


def justo(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "justo", periodo)
    problemas = revisar_ficha_justo(ficha)
    al: list[dict] = []
    no_proc: list[dict] = []
    por_id = {norm(e.get("id")): e for e in ficha.get("engagements") or []}
    citadas = {str(e.get(k)) for e in ficha.get("engagements") or [] for k in ("program_source", "report_source")}
    citadas |= {str(h.get("source")) for e in ficha.get("engagements") or [] for h in (e.get("findings") or []) + (e.get("report_findings") or [])}
    citadas |= {str(s) for s in ficha.get("reviewed") or []}
    problemas += _sin_ficha(docs, "20-trabajos", citadas, "es un documento de un trabajo; corre work-scan")
    trabajos = []
    hallazgos = []
    for carpeta in _carpetas_trabajo(docs):
        tid = carpeta.name.split("_")[0]
        e = por_id.get(norm(tid)) or {}
        prog = tabla(cfg, "programa", no_proc, (hallar(carpeta, *PATRONES["programa"]) or [None])[-1]) if hallar(carpeta, *PATRONES["programa"]) else None
        pap = tabla(cfg, "papeles", no_proc, (hallar(carpeta, *PATRONES["papeles"]) or [None])[-1]) if hallar(carpeta, *PATRONES["papeles"]) else None
        indice = {norm(x["papel"]): x for x in (pap.filas if pap else [])}
        informe = fecha(e.get("report_date"))
        fila = {"trabajo": tid, "programa": bool(prog), "aprobado": e.get("program_approved"), "pasos": len(prog.filas) if prog else 0,
                "papeles": len(indice), "sin_papel": [], "sin_revision": [], "hallazgos": len(e.get("findings") or []), "informe": iso(informe)}
        if not e:
            problemas.append(f"20-trabajos/{carpeta.name}: el trabajo no está en la ficha; corre work-scan")
        if not prog:
            no_proc.append({"archivo": rel(carpeta, docs), "motivo": "sin programa de trabajo en Excel o CSV: no se revisan sus pasos"})
        # 1 · El programa, aprobado antes del primer papel (norma 13.6).
        primero = min((d for d in (fecha(x.get("fecha")) for x in indice.values()) if d), default=None)
        apr = fecha(e.get("program_approved"))
        if e and prog and (not apr or (primero and apr > primero)):
            cita = _cita(e.get("program_source")) or prog.cita({}, docs)
            al.append(alerta("work_program_not_approved", f"{tid}: el programa de trabajo " + (f"se aprobó el {iso(apr)}, después del primer papel ({iso(primero)})" if apr else
                             "no tiene la aprobación del responsable de auditoría") + " (norma 13.6)", cita, clave=f"programa:{tid}"))
        # 2 · Cada paso del programa con su papel (norma 12.3).
        for x in prog.filas if prog else []:
            ref = norm(x.get("papel"))
            if ref and ref in indice:
                continue
            if not ref and x.get("no_aplica"):
                continue
            fila["sin_papel"].append(x["paso"])
            al.append(alerta("procedure_not_executed", f"{tid} · paso {x['paso']} «{x.get('objetivo') or ''}»: " +
                             (f"cita el papel {x.get('papel')}, que no está en el índice" if ref else "no tiene papel ni la razón por la que no aplica") + " (norma 12.3)",
                             prog.cita(x, docs), clave=f"paso:{tid}:{x['paso']}"))
        # 3 · Cada papel con su revisión y su aprobación antes del informe (normas 12.3 y 14.6).
        for x in pap.filas if pap else []:
            rev, aprp = fecha(x.get("fecha_revision")), fecha(x.get("fecha_aprobacion"))
            falta = [] if (x.get("revisado_por") and rev) else ["la revisión del supervisor"]
            falta += [] if (x.get("aprobado_por") and aprp) else ["la aprobación del responsable de auditoría"]
            tarde = informe and ((rev and rev > informe) or (aprp and aprp > informe))
            if falta or tarde:
                fila["sin_revision"].append(x["papel"])
                al.append(alerta("workpaper_not_reviewed", f"{tid} · {x['papel']}: " + (f"no tiene {' ni '.join(falta)}" if falta else
                                 f"se revisó o aprobó después del informe del {iso(informe)}") + " (normas 12.3 y 14.6)", pap.cita(x, docs), clave=f"revision:{tid}:{x['papel']}"))
        # 4 · Cada hallazgo de los papeles: sus elementos, su papel y su prioridad (normas 14.2, 14.3 y 14.6).
        en_papeles = {norm(h.get("id")): h for h in e.get("findings") or []}
        for h in e.get("findings") or []:
            hid, cita = h.get("id"), _cita(h.get("source"))
            falta = [n for k, n in (("criteria", "el criterio"), ("condition", "la condición"), ("effect", "el efecto"), ("priority", "la prioridad")) if not h.get(k)]
            if not h.get("cause") and not h.get("cause_unknown_reason"):
                falta.append("la causa raíz ni la razón por la que no se pudo identificar")
            calc = prioridad_de(cfg, h.get("impact"), h.get("likelihood"))
            hallazgos.append({"trabajo": tid, "id": hid, "prioridad": h.get("priority"), "metodologia": calc, "falta": falta, "papeles": h.get("workpapers") or []})
            if falta:
                al.append(alerta("finding_element_missing", f"{tid} · {hid}: le falta {', '.join(falta)} (normas 14.2 y 14.3)", cita, clave=f"elementos:{tid}:{hid}"))
            refs = [norm(r) for r in h.get("workpapers") or []]
            if not refs or any(r not in indice for r in refs):
                malos = [r for r in h.get("workpapers") or [] if norm(r) not in indice]
                al.append(alerta("finding_without_workpaper", f"{tid} · {hid}: " + (f"cita {', '.join(malos)}, que no está en el índice de papeles" if refs else "no cita un papel de trabajo")
                                 + " (norma 14.6)", cita, clave=f"papel:{tid}:{hid}"))
            if calc and h.get("priority") and norm(h.get("priority")) != calc:
                al.append(alerta("rating_inconsistent", f"{tid} · {hid}: prioridad «{h.get('priority')}»; con impacto {h.get('impact')} y probabilidad {h.get('likelihood')} "
                                 f"la metodología da «{calc}» (norma 14.3)", cita, clave=f"prioridad:{tid}:{hid}"))
        # 5 · El informe contra los papeles.
        en_informe = {norm(h.get("id")): h for h in e.get("report_findings") or []}
        if e.get("report_findings") is not None:
            for k in sorted(set(en_papeles) | set(en_informe)):
                a, b = en_papeles.get(k), en_informe.get(k)
                if a and not b:
                    dif = "está en los papeles y no en el informe"
                elif b and not a:
                    dif = "está en el informe y no en los papeles"
                elif norm(a.get("priority")) != norm(b.get("priority")):
                    dif = f"el informe le da prioridad «{b.get('priority')}» y los papeles «{a.get('priority')}»"
                elif _cifras(a.get("figures")) != _cifras(b.get("figures")):
                    dif = f"el informe trae {', '.join(f'{x:,.0f}' for x in _cifras(b.get('figures'))) or 'ninguna cifra'} y los papeles {', '.join(f'{x:,.0f}' for x in _cifras(a.get('figures'))) or 'ninguna'}"
                else:
                    continue
                hid = (a or b).get("id")
                al.append(alerta("report_differs_from_workpapers", f"{tid} · {hid}: {dif}", [c for c in (_cita((b or {}).get("source")), _cita((a or {}).get("source"))) if c],
                                 clave=f"informe:{tid}:{hid}"))
        trabajos.append(fila)
    # 6 · La objetividad de cada asignación (norma 2.2).
    asig, cargos = tabla(cfg, "asignaciones", no_proc), tabla(cfg, "cargos", no_proc)
    asignaciones = []
    for x in asig.filas if asig else []:
        if norm(x.get("tipo")).startswith(("consult", "advis", "asesor")):
            continue
        ini = fecha(x.get("inicio")) or (fecha((por_id.get(norm(x["trabajo"])) or {}).get("start_date")))
        choque = None
        for c in cargos.filas if cargos else []:
            if norm(c["auditor"]) != norm(x["auditor"]) or norm(c["unidad"]) != norm(x.get("unidad")) or not ini:
                continue
            desde, hasta = fecha(c.get("desde")), fecha(c.get("hasta")) or ini
            if (not desde or desde <= ini) and (ini - hasta).days <= OBJETIVIDAD_DIAS:
                choque = (c, hasta)
                break
        asignaciones.append({"trabajo": x["trabajo"], "auditor": x["auditor"], "unidad": x.get("unidad"), "choque": bool(choque)})
        if choque:
            c, hasta = choque
            al.append(alerta("auditor_reviews_own_work", f"{x['trabajo']}: {x['auditor']} está asignado a un trabajo de aseguramiento sobre {x.get('unidad')}, que tuvo a su cargo "
                             f"hasta el {iso(hasta)}, dentro de los doce meses anteriores al {iso(ini)} (norma 2.2)", [asig.cita(x, docs), cargos.cita(c, docs)],
                             clave=f"objetividad:{x['trabajo']}:{norm(x['auditor'])}"))
    partes = {
        "work-scan": {"trabajos": len(trabajos), "hallazgos": len(hallazgos), "fuentes": ["F-01"]},
        "finding-check": {"hallazgos": hallazgos, "escala": [[n, v] for n, v in escala(cfg)], "fuentes": ["F-01"]},
        "workpaper-check": {"trabajos": trabajos, "fuentes": ["F-01"]},
        "report-check": {"trabajos": trabajos, "fuentes": ["F-01"]},
        "objectivity-check": {"asignaciones": asignaciones, "fuentes": ["F-01"]},
    }
    return {"agente": "justo", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": []}


# ================================================================ Remedios · el seguimiento

def _palabras(s) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", norm(s).replace("_", " ")) if len(w) > 3}


def remedios(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "remedios", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    reg, acep = tabla(cfg, "hallazgos", no_proc), tabla(cfg, "aceptados", no_proc)
    if reg is None and not no_proc:
        no_proc.append({"archivo": "30-seguimiento", "motivo": "no está el registro de hallazgos y planes de acción: sin él no se calcula el seguimiento"})
    evid = {}
    for x in ficha.get("evidence") or []:
        evid.setdefault(norm(x.get("finding")), []).append(x)
    expl = {}
    for x in ficha.get("delay_explanations") or []:
        expl.setdefault(norm(x.get("finding")), []).append(x)
    citadas = {str(x.get("source")) for k in ("evidence", "delay_explanations", "external_findings") for x in ficha.get(k) or []}
    citadas |= {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, "30-seguimiento", citadas, "es una evidencia, una explicación o un informe externo; corre remediation-scan")
    maximo = numero(metodologia(cfg).get("max_reschedules"))
    planes = []
    filas = reg.filas if reg else []
    for x in filas:
        hid, cita = x["hallazgo"], reg.cita(x, docs)
        nom = f"{hid} · {x.get('condicion') or ''}".strip(" ·")
        cerrado = norm(x.get("estado")) in CERRADO
        vence = fecha(x.get("fecha"))
        rep = numero(x.get("reprogramaciones")) or 0
        e = evid.get(norm(hid)) or []
        planes.append({"hallazgo": hid, "trabajo": x.get("trabajo"), "prioridad": x.get("prioridad"), "responsable": x.get("responsable"), "fecha": iso(vence),
                       "reprogramaciones": int(rep), "estado": x.get("estado"), "evidencias": len(e), "proceso": x.get("proceso")})
        # 1 · Plan, responsable y fecha (norma 15.1).
        if x.get("comunicado") and not cerrado:
            falta = [n for k, n in (("plan", "plan de acción"), ("responsable", "responsable"), ("fecha", "fecha")) if not x.get(k)]
            if falta:
                al.append(alerta("action_plan_missing", f"{nom}: comunicado el {iso(fecha(x.get('comunicado')))} y sin {', '.join(falta)} (norma 15.1)", cita,
                                 responsable=x.get("responsable") or None, clave=f"plan:{hid}"))
        # 2 · Vencido sin evidencia ni explicación (norma 15.2).
        if not cerrado and vence and vence < hoy and not e and not expl.get(norm(hid)):
            al.append(alerta("action_plan_overdue", f"{nom}: venció el {iso(vence)} sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2)",
                             cita, responsable=x.get("responsable") or None, dias=(hoy - vence).days, clave=f"vencido:{hid}"))
        # 3 · Las reprogramaciones.
        if maximo is not None and rep > maximo:
            al.append(alerta("due_date_extended_repeatedly", f"{nom}: su fecha se corrió {int(rep)} veces y la metodología permite {int(maximo)}", cita,
                             responsable=x.get("responsable") or None, clave=f"reprogramado:{hid}"))
        # 4 · El cierre, con su evidencia y su validación (norma 15.2).
        if cerrado and (not e or not x.get("validado_por")):
            falta = (["la evidencia de su implementación"] if not e else []) + (["la validación de auditoría"] if not x.get("validado_por") else [])
            al.append(alerta("closure_without_evidence", f"{nom}: cerrado{' el ' + iso(fecha(x.get('cierre'))) if fecha(x.get('cierre')) else ''} sin {' ni '.join(falta)} (norma 15.2)",
                             cita, responsable=x.get("responsable") or None, clave=f"cierre:{hid}"))
    # 5 · Los hallazgos que vuelven: la misma condición en el mismo proceso, después del cierre del anterior.
    repetidos = []
    for x in filas:
        com = fecha(x.get("comunicado"))
        if not com or not x.get("proceso"):
            continue
        for y in filas:
            if y is x or norm(y.get("estado")) not in CERRADO or norm(y.get("proceso")) != norm(x.get("proceso")):
                continue
            cy = fecha(y.get("cierre"))
            a, b = _palabras(x.get("condicion")), _palabras(y.get("condicion"))
            if cy and cy < com and a and b and len(a & b) / len(a | b) >= 0.5:
                repetidos.append({"hallazgo": x["hallazgo"], "anterior": y["hallazgo"], "proceso": x.get("proceso")})
                al.append(alerta("finding_repeated", f"{x['hallazgo']}: la misma condición que {y['hallazgo']} en {x.get('proceso')}, que se cerró el {iso(cy)}",
                                 [reg.cita(x, docs), reg.cita(y, docs)], clave=f"repetido:{x['hallazgo']}:{y['hallazgo']}"))
                break
    # 6 · Los riesgos aceptados por encima del apetito (norma 11.5).
    riesgos = []
    for x in acep.filas if acep else []:
        if not _si(x.get("encima")):
            continue
        disc, cons, res = fecha(x.get("discutido")) or _si(x.get("discutido")), fecha(x.get("consejo")) or _si(x.get("consejo")), _si(x.get("resuelto"))
        riesgos.append({"riesgo": x["riesgo"], "descripcion": x.get("descripcion"), "discutido": bool(disc), "resuelto": res, "consejo": bool(cons)})
        if not disc:
            que = "no hay constancia de que se discutiera con la alta dirección"
        elif not res and not cons:
            que = "se discutió con la alta dirección, no se resolvió y no hay constancia de que llegara al consejo"
        else:
            continue
        al.append(alerta("risk_accepted_not_escalated", f"{x['riesgo']} · {x.get('descripcion') or ''}: aceptado por encima del apetito{' el ' + iso(fecha(x.get('fecha'))) if fecha(x.get('fecha')) else ''}; {que} (norma 11.5)",
                         acep.cita(x, docs), clave=f"aceptado:{x['riesgo']}"))
    # 7 · Los hallazgos externos que no están en el registro.
    en_registro = {norm(x["hallazgo"]) for x in filas} | {norm(x.get("referencia")) for x in filas if x.get("referencia")}
    externos = []
    for x in ficha.get("external_findings") or []:
        dentro = norm(x.get("id")) in en_registro
        externos.append({"id": x.get("id"), "de": x.get("issuer"), "en_registro": dentro})
        if not dentro:
            al.append(alerta("external_finding_untracked", f"{x.get('id')} · {x.get('title') or ''}: hallazgo de {x.get('issuer') or 'un informe externo'} que no está en el registro con su plan",
                             _cita(x.get("source")), clave=f"externo:{x.get('id')}"))
    abiertos = [p for p in planes if norm(p["estado"]) not in CERRADO]
    partes = {
        "remediation-scan": {"hallazgos": len(planes), "abiertos": len(abiertos), "evidencias": sum(len(v) for v in evid.values()), "fuentes": ["F-01"]},
        "action-status": {"planes": abiertos, "maximo": maximo, "fuentes": ["F-01"]},
        "closure-check": {"cerrados": [p for p in planes if norm(p["estado"]) in CERRADO], "repetidos": repetidos, "fuentes": ["F-01"]},
        "committee-brief": {"abiertos": len(abiertos), "vencidos": sum(1 for a in al if a["signal"] == "action_plan_overdue"), "repetidos": repetidos,
                            "riesgos": riesgos, "externos": externos, "fuentes": ["F-01"]},
    }
    vence = sorted(({"fecha": p["fecha"], "que": f"{p['hallazgo']} · plan de acción", "caso": p["hallazgo"], "estado": "pendiente", "comando": "action-status"}
                    for p in abiertos if p["fecha"] and 0 <= (fecha(p["fecha"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "remedios", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ el reporte

SENALES_DE = {
    "plan-coverage": {"high_risk_not_covered", "auditable_unit_overdue", "risk_assessment_outdated", "plan_area_not_considered"},
    "plan-status": {"plan_change_unapproved", "engagement_behind_schedule"},
    "plan-capacity": {"plan_hours_exceed_capacity", "topical_requirement_missing"},
    "quality-status": {"external_assessment_overdue"},
    "finding-check": {"finding_element_missing", "rating_inconsistent"},
    "workpaper-check": {"work_program_not_approved", "procedure_not_executed", "workpaper_not_reviewed", "finding_without_workpaper"},
    "report-check": {"report_differs_from_workpapers"},
    "objectivity-check": {"auditor_reviews_own_work"},
    "action-status": {"action_plan_missing", "action_plan_overdue", "due_date_extended_repeatedly"},
    "closure-check": {"closure_without_evidence", "finding_repeated"},
    "committee-brief": {"action_plan_overdue", "finding_repeated", "risk_accepted_not_escalated", "external_finding_untracked"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-cae")


def _sn(b) -> str:
    return "sí" if b else "no"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "plan-scan":
        l += [f"**Trabajos activos en el plan:** {p['trabajos']} · **Riesgos en la matriz:** {p['riesgos']} · **Unidades del universo:** {p['unidades']} · "
              f"**Aprobaciones en la ficha:** {p['aprobaciones']}.", ""]
    elif comando == "plan-coverage":
        l += ["| Riesgo | Calificación | Unidad | Alto | Trabajos que lo cubren |", "|---|---|---|---|---|"]
        l += [f"| {x['riesgo']} · {x['descripcion'] or ''} | {x['calificacion'] or '—'} | {x['unidad'] or '—'} | {_sn(x['alto'])} | {', '.join(x['trabajos']) or '—'} |" for x in p["riesgos"]]
        l += ["", "| Unidad | Nivel | Último trabajo | Ciclo | Vence | En el plan |", "|---|---|---|---|---|---|"]
        l += [f"| {u['unidad']} · {u['nombre'] or ''} | {u['nivel'] or '—'} | {u['ultimo'] or '—'} | {str(int(u['ciclo'])) + ' meses' if u['ciclo'] else '—'} | "
              f"{u['tope'] or '—'} | {', '.join(u['planeada']) or '—'} |" for u in p["unidades"]]
        l += ["", "| Lo que el plan tiene que considerar (norma 9.4) | Considerado | Por qué no |", "|---|---|---|"]
        l += [f"| {a['area']} | {_sn(a['considerada'])} | {a['razon'] or '—'} |" for a in p["areas"]]
        l += ["", f"**Última evaluación de riesgos:** {p['evaluacion'] or '—'}.", "", "Qué se audita lo decide el responsable de auditoría con el consejo: aquí se dice qué queda sin cubrir.", ""]
    elif comando == "plan-status":
        l += ["| Trabajo | Unidad | Inicio | Cierre | Estado | Horas |", "|---|---|---|---|---|---|"]
        l += [f"| {t['trabajo']} · {t['nombre'] or ''} | {t['unidad'] or '—'} | {t['inicio'] or '—'} | {t['cierre'] or '—'} | {t['estado'] or '—'} | "
              f"{t['horas'] if t['horas'] is not None else '—'} |" for t in p["trabajos"]]
        if p["cambios"]:
            l += ["", "| Cambio | Trabajo | Aprobado | Por | Acta |", "|---|---|---|---|---|"]
            l += [f"| {c['cambio']} | {c['trabajo']} | {_sn(c['aprobado'])} | {c['por'] or '—'} | {('`' + c['acta'] + '`') if c['acta'] else '—'} |" for c in p["cambios"]]
        l.append("")
    elif comando == "plan-capacity":
        l += [f"**Horas del plan:** {p['horas_plan']:g} · **Horas disponibles del equipo:** {p['horas_equipo']:g}." if p["horas_equipo"] is not None else
              f"**Horas del plan:** {p['horas_plan']:g} · **Horas disponibles del equipo:** sin la tabla del equipo.", ""]
        l += ["| Trabajo | Temas | Horas |", "|---|---|---|"] + [f"| {t['trabajo']} · {t['nombre'] or ''} | {', '.join(t['temas']) or '—'} | {t['horas'] if t['horas'] is not None else '—'} |"
                                                         for t in p["trabajos"]]
        l += ["", "Requisitos temáticos de The IIA y desde cuándo rigen: " + "; ".join(f"{v['nombre']}, {iso(v['desde'])}" for v in REQUISITOS_TEMATICOS.values()) + ".", ""]
    elif comando == "quality-status":
        l += [f"**Última evaluación externa de calidad:** {p['ultima'] or 'sin fecha'} · **La siguiente, a más tardar:** {p['siguiente'] or '—'} (norma 8.4: al menos una vez cada cinco años).", ""]
    elif comando == "work-scan":
        l += [f"**Trabajos en `20-trabajos/`:** {p['trabajos']} · **Hallazgos en la ficha:** {p['hallazgos']}.", ""]
    elif comando == "finding-check":
        l += ["**Escala de la metodología:** " + (", ".join(f"{n} desde {v:g}" for n, v in p["escala"]) or "—") + " (impacto por probabilidad).", ""]
        l += ["| Trabajo | Hallazgo | Prioridad | La de la metodología | Le falta | Papeles |", "|---|---|---|---|---|---|"]
        l += [f"| {h['trabajo']} | {h['id']} | {h['prioridad'] or '—'} | {h['metodologia'] or '—'} | {', '.join(h['falta']) or '—'} | {', '.join(h['papeles']) or '—'} |"
              for h in p["hallazgos"]]
        l += ["", "La prioridad la pone el auditor: aquí se dice cuándo no es la que da la metodología.", ""]
    elif comando in ("workpaper-check", "report-check"):
        l += ["| Trabajo | Programa aprobado | Pasos | Papeles | Pasos sin papel | Papeles sin revisión | Hallazgos | Informe |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {t['trabajo']} | {t['aprobado'] or '—'} | {t['pasos']} | {t['papeles']} | {', '.join(t['sin_papel']) or '—'} | {', '.join(t['sin_revision']) or '—'} | "
              f"{t['hallazgos']} | {t['informe'] or '—'} |" for t in p["trabajos"]]
        l.append("")
    elif comando == "objectivity-check":
        l += ["| Trabajo | Auditor | Actividad auditada | Posible impedimento |", "|---|---|---|---|"]
        l += [f"| {a['trabajo']} | {a['auditor']} | {a['unidad'] or '—'} | {_sn(a['choque'])} |" for a in p["asignaciones"]]
        l += ["", "Un posible impedimento lo revisa y lo declara el responsable de auditoría (norma 2.3); aquí no se califica a nadie.", ""]
    elif comando == "remediation-scan":
        l += [f"**Hallazgos en el registro:** {p['hallazgos']} · **Abiertos:** {p['abiertos']} · **Evidencias en la ficha:** {p['evidencias']}.", ""]
    elif comando == "action-status":
        l += [f"**Reprogramaciones que permite la metodología:** {int(p['maximo']) if p['maximo'] is not None else '—'}.", "",
              "| Hallazgo | Trabajo | Prioridad | Responsable | Fecha | Reprogramaciones | Evidencias |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['hallazgo']} | {x['trabajo'] or '—'} | {x['prioridad'] or '—'} | {x['responsable'] or '—'} | {x['fecha'] or '—'} | {x['reprogramaciones']} | {x['evidencias']} |"
              for x in p["planes"]]
        l.append("")
    elif comando == "closure-check":
        l += ["| Hallazgo | Proceso | Estado | Evidencias |", "|---|---|---|---|"]
        l += [f"| {x['hallazgo']} | {x['proceso'] or '—'} | {x['estado'] or '—'} | {x['evidencias']} |" for x in p["cerrados"]]
        if p["repetidos"]:
            l += ["", "| Vuelve | Antes | Proceso |", "|---|---|---|"] + [f"| {x['hallazgo']} | {x['anterior']} | {x['proceso']} |" for x in p["repetidos"]]
        l += ["", "El cierre lo valida el auditor: aquí se dice cuál no tiene con qué sostenerse.", ""]
    elif comando == "committee-brief":
        l += [f"**Planes abiertos:** {p['abiertos']} · **Vencidos sin evidencia ni explicación:** {p['vencidos']} · **Hallazgos que vuelven:** {len(p['repetidos'])}.", ""]
        if p["riesgos"]:
            l += ["| Riesgo aceptado por encima del apetito | Alta dirección | Resuelto | Consejo |", "|---|---|---|---|"]
            l += [f"| {x['riesgo']} · {x['descripcion'] or ''} | {_sn(x['discutido'])} | {_sn(x['resuelto'])} | {_sn(x['consejo'])} |" for x in p["riesgos"]]
            l.append("")
        if p["externos"]:
            l += ["| Hallazgo externo | De | En el registro |", "|---|---|---|"] + [f"| {x['id']} | {x['de'] or '—'} | {_sn(x['en_registro'])} |" for x in p["externos"]]
            l.append("")
        l += ["Este es el material; lo que se concluye y se comunica al comité es del responsable de auditoría.", ""]
    return l


# ================================================================ cuándo toca qué

def despertar(cfg: dict, rol: str, hoy: dt.date) -> dict:
    corr = registro_corridas(cfg["_estado"])
    ultima = lambda que: max((fecha(c["fecha"]) for c in corr if c["comando"] == que), default=None)  # noqa: E731
    periodo = cfg.get("period")
    toca, motivo = [], []
    if not periodo:
        return {"toca": [], "motivo": ["falta el periodo en la configuración"], "hoy": iso(hoy), "callado": False}
    docs = cfg["_docs"]
    nueva = lambda carpeta, desde: [p for p in (docs / carpeta).rglob("*") if p.is_file() and (not desde or dt.date.fromtimestamp(p.stat().st_mtime) >= desde)] if (docs / carpeta).is_dir() else []  # noqa: E731
    scan = {"prudencia": "plan-scan", "justo": "work-scan", "remedios": "remediation-scan"}[rol]
    carpetas = {"prudencia": ("10-plan",), "justo": ("20-trabajos",), "remedios": ("30-seguimiento",)}[rol]
    u = ultima(scan)
    if not u or (hoy - u).days >= 7 or any(nueva(c, u) for c in carpetas) or nueva("00-referencia", u):
        toca.append(scan)
        motivo.append("documentos nuevos o la revisión semanal")
    r = AGENTE[rol](cfg, periodo, hoy)
    for cmd, senales in SENALES_DE.items():
        if cmd in r["partes"] and any(a["signal"] in senales for a in r["alertas"]) and ultima(cmd) != hoy:
            toca.append(cmd)
            motivo.append(f"{sum(1 for a in r['alertas'] if a['signal'] in senales)} señales abiertas en {N.nombre_comando(cmd).lower()}")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


AGENTE = {"prudencia": prudencia, "justo": justo, "remedios": remedios}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-audit-work": "justo", "criterio-remediation": "remedios"}.get(N.plugin(AQUI)["name"], "prudencia")


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    periodo = a.period or cfg.get("period")
    if not periodo:
        raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
    r = AGENTE[rol](cfg, periodo, hoy)
    destino = cfg["_estado"] / SUB[rol] / periodo / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Prudencia, Justo y Remedios.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir", "compute", "reporte", "despertar",
                                       "responder", "corrida", "buscar-raiz", "marcar-raiz", "arranque", "dejar-listo", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=tuple(SUB.values()),
                       revisar_config=revisar_config, calcular=calcular, reporte=reporte, despertar=despertar)


# ================================================================ la prueba del motor

def selftest() -> int:
    import tempfile
    fallas = []

    def ok(nombre, obtenido, esperado):
        if obtenido == esperado:
            print(f"  ok  {nombre}")
        else:
            fallas.append(nombre)
            print(f"  FALLA  {nombre}: {obtenido!r} en lugar de {esperado!r}")

    def _x(ruta: Path, filas: list[list]) -> None:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        _xlsx(ruta, filas)

    hoy = dt.date(2026, 11, 24)
    met = {"cycles_months": {"Crítico": 12, "Alto": 12, "Medio": 24, "Bajo": 36}, "high_ratings": ["Alto", "Crítico"],
           "risk_assessment_date": "2025-10-01", "external_assessment_date": "2021-06-30",
           "priority": {"levels": [["Alta", 15], ["Media", 8], ["Baja", 1]]}, "max_reschedules": 2}
    ok("la prioridad de la metodología", [prioridad_de({"methodology": met}, 4, 4), prioridad_de({"methodology": met}, 3, 3), prioridad_de({"methodology": met}, 2, 2)],
       ["alta", "media", "baja"])
    ok("los requisitos temáticos vigentes y su fecha (F-02)", {k: iso(v["desde"]) for k, v in REQUISITOS_TEMATICOS.items()},
       {"ciberseguridad": "2026-02-05", "terceros": "2026-09-15", "comportamiento": "2026-12-15", "resiliencia": "2027-04-30", "anticorrupcion": "2027-11-23"})
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "auditoria" / "e1", t / "estado" / "e1"
        _x(docs / "10-plan" / "universo.xlsx", [["Unidad", "Nombre", "Nivel", "Último trabajo"],
                                                   ["U-01", "Crédito", "Alto", "2025-03-10"], ["U-02", "Tesorería", "Medio", "2023-05-01"],
                                                   ["U-03", "Nómina", "Bajo", ""], ["U-04", "Tecnología", "Alto", "2025-09-01"]])
        _x(docs / "10-plan" / "matriz_riesgos.xlsx", [["Riesgo", "Descripción", "Calificación", "Unidad"],
                                                         ["R-01", "Pérdida por crédito", "Alto", "U-01"], ["R-02", "Fraude en pagos", "Crítico", "U-05"],
                                                         ["R-03", "Ciberataque", "Alto", "U-04"], ["R-04", "Error de nómina", "Bajo", "U-03"]])
        _x(docs / "10-plan" / "plan_anual.xlsx", [["Trabajo", "Nombre", "Unidad", "Riesgos", "Tipo", "Tema", "Inicio", "Cierre", "Estado", "Horas", "Requisito temático", "Cambio"],
                                                     ["TR-01", "Crédito comercial", "U-01", "R-01", "Aseguramiento", "Crédito; fraude", "2026-02-01", "2026-04-30", "Terminado", "400", "", ""],
                                                     ["TR-02", "Ciberseguridad", "U-04", "R-03", "Aseguramiento", "Ciberseguridad", "2026-10-01", "2026-12-15", "En curso", "300", "", ""],
                                                     ["TR-03", "Proveedores", "U-06", "", "Aseguramiento", "Terceros", "2026-09-20", "2026-11-10", "En curso", "250", "Terceros", ""],
                                                     ["TR-04", "Cumplimiento SARLAFT", "U-07", "", "Aseguramiento", "Cumplimiento", "2026-11-01", "2026-12-20", "Planeado", "200", "", "Agregado"],
                                                     ["TR-05", "Tesorería", "U-02", "", "Aseguramiento", "Tesorería", "2026-08-01", "2026-09-30", "Cancelado", "150", "", "Cancelado"]])
        _x(docs / "00-referencia" / "equipo.xlsx", [["Auditor", "Horas disponibles"], ["Ana", "500"], ["Luis", "500"]])
        _x(docs / "00-referencia" / "cargos_anteriores.xlsx", [["Auditor", "Unidad", "Desde", "Hasta"], ["Luis", "Tecnología", "2022-01-01", "2026-03-31"]])
        (docs / "10-plan" / "actas").mkdir(parents=True)
        (docs / "10-plan" / "actas" / "acta-2026-07.pdf").write_text("acta", encoding="utf-8")
        escribir_json(est / "plan" / "2026-11" / "ficha.json", {"approvals": [
            {"engagement": "TR-05", "change": "cancela", "approved_by": "Comité de auditoría", "date": "2026-07-15", "source": "10-plan/actas/acta-2026-07.pdf"}]})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-11", "_docs": docs, "_estado": est, "methodology": met}
        ok("la configuración de Prudencia pasa", revisar_config(cfg, "prudencia"), [])
        r = prudencia(cfg, "2026-11", hoy)
        ok("Prudencia: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("auditable_unit_overdue", "unidad:U-02"), ("auditable_unit_overdue", "unidad:U-03"),
            ("engagement_behind_schedule", "atraso:TR-03"), ("engagement_behind_schedule", "atraso:TR-04"),
            ("external_assessment_overdue", "evaluacion_externa"), ("high_risk_not_covered", "riesgo:R-02"),
            ("plan_change_unapproved", "cambio:TR-04"), ("plan_hours_exceed_capacity", "horas"),
            ("risk_assessment_outdated", "evaluacion_de_riesgos"), ("topical_requirement_missing", "tematico:TR-02:ciberseguridad")])
        ok("Prudencia: la ficha cita sus actas", r["record_issues"], [])

        tr = docs / "20-trabajos" / "TR-01_credito"
        _x(tr / "programa.xlsx", [["Paso", "Objetivo", "Papel", "No aplica"], ["P1", "Muestreo de créditos", "PT-01", ""], ["P2", "Garantías", "PT-02", ""],
                                     ["P3", "Provisiones", "", ""], ["P4", "Cartera castigada", "", "sin castigos en el periodo"]])
        _x(tr / "indice_papeles.xlsx", [["Papel", "Paso", "Fecha", "Revisado por", "Fecha revisión", "Aprobado por", "Fecha aprobación"],
                                           ["PT-01", "P1", "2026-02-10", "Ana", "2026-03-01", "Jefe", "2026-03-05"],
                                           ["PT-02", "P2", "2026-02-12", "", "", "Jefe", "2026-03-05"]])
        (tr / "informe.pdf").write_text("informe", encoding="utf-8")
        (tr / "PT-01.pdf").write_text("papel", encoding="utf-8")
        (tr / "PT-02.pdf").write_text("papel", encoding="utf-8")
        _x(docs / "20-trabajos" / "asignaciones.xlsx", [["Trabajo", "Auditor", "Unidad", "Inicio"], ["TR-01", "Ana", "Crédito", "2026-02-01"],
                                                          ["TR-02", "Luis", "Tecnología", "2026-10-01"]])
        H = lambda i, **k: {"id": i, "source": f"20-trabajos/TR-01_credito/PT-0{1 if i == 'H-01' else 2}.pdf", **k}  # noqa: E731
        escribir_json(est / "trabajos" / "2026-11" / "ficha.json", {"engagements": [{
            "id": "TR-01", "program_approved": "2026-02-15", "program_source": "20-trabajos/TR-01_credito/PT-01.pdf",
            "report_date": "2026-04-30", "report_source": "20-trabajos/TR-01_credito/informe.pdf",
            "findings": [H("H-01", criteria="Política de crédito 4.2", condition="12 créditos sin garantía", cause="", effect="Pérdida esperada", impact=4, likelihood=4,
                           priority="Media", workpapers=["PT-01"], figures=[1200000]),
                         H("H-02", criteria="Manual de garantías", condition="Avalúos vencidos", cause="Falta de control", effect="Garantía sin valor", impact=3, likelihood=3,
                           priority="Media", workpapers=["PT-09"], figures=[500000])],
            "report_findings": [{"id": "H-01", "priority": "Alta", "figures": [1200000], "source": "20-trabajos/TR-01_credito/informe.pdf"},
                                {"id": "H-02", "priority": "Media", "figures": [500000], "source": "20-trabajos/TR-01_credito/informe.pdf"}]}]})
        cfg["_docs"] = docs
        r = justo(cfg, "2026-11", hoy)
        ok("Justo: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("auditor_reviews_own_work", "objetividad:TR-02:luis"), ("finding_element_missing", "elementos:TR-01:H-01"),
            ("finding_without_workpaper", "papel:TR-01:H-02"), ("procedure_not_executed", "paso:TR-01:P3"),
            ("rating_inconsistent", "prioridad:TR-01:H-01"), ("report_differs_from_workpapers", "informe:TR-01:H-01"),
            ("work_program_not_approved", "programa:TR-01"), ("workpaper_not_reviewed", "revision:TR-01:PT-02")])

        _x(docs / "30-seguimiento" / "registro_hallazgos.xlsx", [
            ["Hallazgo", "Trabajo", "Origen", "Proceso", "Condición", "Prioridad", "Comunicado", "Plan", "Responsable", "Fecha compromiso", "Reprogramaciones", "Estado", "Fecha cierre", "Validado por", "Referencia externa"],
            ["H-10", "TR-00", "Interna", "Crédito", "Créditos desembolsados sin garantía constituida", "Alta", "2025-05-10", "Constituir garantías", "Gerente de crédito", "2025-09-30", "0", "Cerrado", "2025-09-20", "Ana", ""],
            ["H-01", "TR-01", "Interna", "Crédito", "Créditos desembolsados sin garantía constituida", "Media", "2026-05-05", "Revisar", "Gerente de crédito", "2026-08-31", "3", "Abierto", "", "", ""],
            ["H-02", "TR-01", "Interna", "Garantías", "Avalúos vencidos", "Media", "2026-05-05", "", "", "", "0", "Abierto", "", "", ""],
            ["H-11", "TR-00", "Interna", "Tesorería", "Conciliaciones sin firma", "Baja", "2025-05-10", "Firmar", "Tesorero", "2025-08-31", "0", "Cerrado", "2025-08-30", "", ""],
            ["RF-02", "", "Revisor fiscal", "Nómina", "Horas extra sin aprobación", "Media", "2026-06-01", "Aprobar", "Gestión humana", "2026-12-31", "0", "Abierto", "", "", "RF-02"]])
        _x(docs / "30-seguimiento" / "riesgos_aceptados.xlsx", [["Riesgo", "Descripción", "Fecha", "Por encima del apetito", "Discutido alta dirección", "Resuelto", "Escalado consejo"],
                                                                   ["RA-01", "Sistema sin soporte del fabricante", "2026-06-01", "Sí", "", "", ""],
                                                                   ["RA-02", "Concentración de proveedor", "2026-06-01", "Sí", "2026-06-10", "No", "2026-07-01"],
                                                                   ["RA-03", "Demora en un reporte", "2026-06-01", "No", "", "", ""]])
        (docs / "30-seguimiento" / "H-10").mkdir()
        (docs / "30-seguimiento" / "H-10" / "evidencia.pdf").write_text("ev", encoding="utf-8")
        (docs / "30-seguimiento" / "informe_revisor_2026.pdf").write_text("inf", encoding="utf-8")
        escribir_json(est / "seguimiento" / "2026-11" / "ficha.json", {
            "evidence": [{"finding": "H-10", "source": "30-seguimiento/H-10/evidencia.pdf"}],
            "external_findings": [{"id": "RF-02", "issuer": "Revisor fiscal", "title": "Horas extra", "source": "30-seguimiento/informe_revisor_2026.pdf"},
                                  {"id": "RF-03", "issuer": "Revisor fiscal", "title": "Caja menor", "source": "30-seguimiento/informe_revisor_2026.pdf"}]})
        r = remedios(cfg, "2026-11", hoy)
        ok("Remedios: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("action_plan_missing", "plan:H-02"), ("action_plan_overdue", "vencido:H-01"), ("closure_without_evidence", "cierre:H-11"),
            ("due_date_extended_repeatedly", "reprogramado:H-01"), ("external_finding_untracked", "externo:RF-03"),
            ("finding_repeated", "repetido:H-01:H-10"), ("risk_accepted_not_escalated", "aceptado:RA-01")])
        ok("Remedios: la ficha cita sus documentos", r["record_issues"], [])
        md = reporte(r, "committee-brief", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
    print(f"\n{'Todo bien' if not fallas else str(len(fallas)) + ' fallas'}.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
