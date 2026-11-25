#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CRO: lo que calcula el código para Severo y Casandra.

    python3 riesgos.py <acción> [opciones]       python3 riesgos.py --help

Severo (criterio-risk-appetite) procesa el apetito por riesgo: cada exposición que reportan las áreas
contra su límite, cada límite contra su dueño y su fecha de revisión, cada reporte contra el plazo del
marco, cada riesgo alto o crítico de la matriz contra su límite o su indicador, y la declaración de
apetito contra la revisión de la junta. Casandra (criterio-risk-events), los indicadores y los eventos:
cada indicador clave de riesgo contra sus umbrales y su acción, y cada evento de pérdida contra su causa,
su monto, su proceso, su plazo de registro, su repetición y su riesgo en la matriz. Los dos comparten
este motor, que vive en criterio-risk-appetite y se copia al otro con scripts/sincronizar.py, y el
núcleo común de las familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —la matriz de riesgos, los
límites, los indicadores con sus umbrales, la exposición de cada periodo, los planes de acción, los
valores y las acciones de los indicadores, y la base de eventos de pérdida— las procesa el código. Lo que
solo trae un documento escrito —la fecha en que la junta revisó la declaración de apetito, los excesos
que aprobó el comité y las acciones sobre un indicador que quedaron en un acta— lo extrae el agente a su
ficha, con la cita, y el código lo cruza.

**Nunca fija ni cambia un límite, nunca aprueba un exceso ni acepta un riesgo, y nunca calcula capital,
valor en riesgo ni pérdida esperada** (decisión 0035): procesa las cifras que reportan las áreas y los
modelos de la organización. **El apetito, los límites, los umbrales y los plazos los fija la
organización** en su marco de apetito: el código calcula y la persona decide.

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import calendar
import datetime as dt
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
from nucleo import (  # noqa: E402
    _hoy, _xlsx, alerta, escribir_json, fecha, filas_de, iso, leer_json, marco_reporte, norm, numero, ordenar,
    registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"
SUB = {"severo": "apetito", "casandra": "eventos"}
NOMBRE = {"severo": "Severo", "casandra": "Casandra"}
ALTOS = {"alto", "alta", "critico", "critica", "extremo", "extrema", "muy_alto", "muy_alta", "high", "critical", "very_high", "extreme"}
MINIMO = {"minimo", "min", "minimum", "piso", "floor", "menor"}
# La norma de cada país sobre el apetito y la gestión integral de riesgos, en las entidades vigiladas
# (fuentes.json de la familia): solo se cita la del país de la entidad.
REGULADOR = {"CO": "F-10", "PE": "F-11", "BR": "F-12"}


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


ALIAS = {
    "matriz": {"riesgo": ["riesgo", "id_riesgo", "codigo", "id", "risk_id", "risk", "risco"],
               "nombre": ["nombre", "descripcion", "nombre_del_riesgo", "name", "description", "nome"],
               "calificacion": ["calificacion", "nivel", "riesgo_residual", "nivel_residual", "severidad", "rating", "residual_rating", "level", "classificacao", "nivel_de_risco"],
               "proceso": ["proceso", "area", "process", "processo"],
               "dueno": ["dueno", "responsable", "propietario", "owner", "responsavel"]},
    "limites": {"limite": ["limite", "id_limite", "codigo", "id", "limit_id", "limit"],
                "valor": ["valor_del_limite", "valor_limite", "nivel_del_limite", "maximo", "limit_value", "valor_do_limite", "valor", "value"],
                "riesgo": ["riesgo", "id_riesgo", "risk_id", "risk", "risco"],
                "metrica": ["metrica", "indicador", "medida", "metric"],
                "sentido": ["sentido", "tipo", "tipo_de_limite", "direction", "type"],
                "dueno": ["dueno", "responsable", "propietario", "owner", "responsavel"],
                "revision": ["proxima_revision", "fecha_de_revision", "revision", "next_review", "review_date", "proxima_revisao", "data_de_revisao"],
                "unidad": ["unidad", "unit", "unidade"]},
    "indicadores": {"indicador": ["indicador", "id_indicador", "kri", "codigo", "id", "indicator"],
                    "nombre": ["nombre", "descripcion", "name", "description", "nome"],
                    "riesgo": ["riesgo", "id_riesgo", "risk_id", "risk", "risco"],
                    "alerta": ["umbral_de_alerta", "umbral_alerta", "alerta", "amber", "warning_threshold", "limiar_de_alerta"],
                    "limite": ["umbral_de_limite", "umbral_limite", "limite", "red", "limit_threshold", "limiar_de_limite"],
                    "sentido": ["sentido", "direccion", "direction"],
                    "dueno": ["dueno", "responsable", "owner", "responsavel"]},
    "exposicion": {"limite": ["limite", "id_limite", "codigo", "limit_id", "limit"],
                   "valor": ["exposicion", "valor", "valor_reportado", "exposure", "value", "exposicao"],
                   "periodo": ["periodo", "corte", "mes", "period", "as_of"],
                   "reporte": ["fecha_de_reporte", "fecha_reporte", "reportado_el", "reported_on", "report_date", "data_do_reporte", "data_de_reporte"],
                   "area": ["area", "reporta", "unidad", "business_unit"]},
    "planes": {"limite": ["limite", "id_limite", "limit_id", "limit"],
               "plan": ["plan", "plan_de_accion", "accion", "action_plan", "action", "plano_de_acao", "plano", "acao"],
               "responsable": ["responsable", "dueno", "owner", "responsavel"],
               "fecha": ["fecha_compromiso", "fecha", "vence", "due_date", "data_compromisso", "prazo"]},
    "valores": {"indicador": ["indicador", "id_indicador", "kri", "indicator"],
                "valor": ["valor", "resultado", "value"],
                "periodo": ["periodo", "mes", "corte", "period"]},
    "acciones": {"indicador": ["indicador", "id_indicador", "kri", "indicator"],
                 "accion": ["accion", "plan", "action", "acao"],
                 "periodo": ["periodo", "mes", "period"],
                 "responsable": ["responsable", "dueno", "owner", "responsavel"]},
    "eventos": {"evento": ["evento", "id_evento", "codigo", "id", "event_id", "event"],
                "ocurrencia": ["fecha_de_ocurrencia", "fecha_ocurrencia", "ocurrencia", "occurrence_date", "data_de_ocorrencia"],
                "descubrimiento": ["fecha_de_descubrimiento", "fecha_descubrimiento", "descubrimiento", "discovery_date", "data_de_descoberta"],
                "registro": ["fecha_de_registro", "fecha_registro", "registro", "registered_on", "registration_date", "data_de_registro"],
                "proceso": ["proceso", "area", "process", "processo"],
                "tipo": ["tipo", "tipo_de_evento", "clase", "categoria", "event_type", "type"],
                "causa": ["causa", "causa_raiz", "cause", "root_cause"],
                "monto": ["monto", "perdida", "monto_de_perdida", "perdida_bruta", "gross_loss", "amount", "loss", "valor_da_perda", "perda"],
                "riesgo": ["riesgo", "id_riesgo", "riesgo_asociado", "risk_id", "risk", "risco"]},
}
REQ = {"matriz": ["riesgo"], "limites": ["limite", "valor"], "indicadores": ["indicador"], "exposicion": ["limite", "valor"],
       "planes": ["limite"], "valores": ["indicador", "valor"], "acciones": ["indicador"], "eventos": ["evento"]}
PATRONES = {"matriz": ("matriz", "risk_register", "mapa_de_riesgos"), "limites": ("limites", "limits"),
            "indicadores": ("indicadores", "kri", "key_risk_indicators"), "exposicion": ("exposicion", "exposure", "exposicao"),
            "planes": ("planes", "action_plans", "planos"), "valores": ("valores", "kri_values"), "acciones": ("acciones", "kri_actions", "acoes"),
            "eventos": ("eventos", "loss_events", "perdidas")}
CARPETA = {"matriz": "00-marco", "limites": "00-marco", "indicadores": "00-marco", "exposicion": "10-exposicion", "planes": "10-exposicion",
           "valores": "20-indicadores", "acciones": "20-indicadores", "eventos": "30-eventos"}
# Los documentos escritos que van a la ficha: la declaración y las políticas del marco, y las actas.
ESCRITOS = ("00-marco", "40-actas")


def tabla(cfg: dict, que: str, no_proc: list, periodo: str | None = None) -> Hoja | None:
    """La tabla de `que`. Si hay varias, la del periodo —por su nombre— o la más reciente."""
    docs = cfg["_docs"]
    rutas = hallar(docs / CARPETA[que], *PATRONES[que])
    if not rutas:
        return None
    if periodo:
        del_periodo = [r for r in rutas if norm(periodo) in norm(r.stem)]
        rutas = del_periodo or rutas
    t = Hoja(rutas[-1], REQ[que], [c for c in ALIAS[que] if c not in REQ[que]], ALIAS[que], (cfg.get("columns") or {}).get(que))
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"{que}: no trae una columna reconocible para {', '.join(t.faltan)}; "
                                                                f"di cuál es en la configuración (columns.{que})"})
        return None
    return t


def _del_periodo(x: dict, periodo: str) -> bool:
    """Una fila sin periodo es del periodo de su archivo; una con periodo, solo si es el que se evalúa."""
    p = str(x.get("periodo") or "").strip()
    if not p:
        return True
    d = fecha(p)
    return (iso(d)[:7] if d else p[:7]) == periodo


# ================================================================ la configuración

DEFECTOS = {"report": {"language": "es"}, "methodology": {"report_days": 10, "statement_review_months": 12,
                                                           "registration_days": 30, "repeat_window_months": 12}}
SEVERIDAD = {
    "limit_breached_without_plan": 1, "kri_alert_without_action": 1, "risk_without_limit": 1,
    "appetite_statement_outdated": 2, "exposure_report_late": 2, "limit_without_owner": 2, "loss_event_repeated": 2,
    "loss_event_registered_late": 2, "loss_event_risk_unmapped": 2, "kri_not_reported": 2,
    "limit_review_overdue": 3, "loss_event_incomplete": 3,
}
N.SEVERIDAD.update(SEVERIDAD)
PARAMETROS = {
    "severo": (("report_days", "los días después del cierre del periodo que el marco da a las áreas para reportar su exposición"),
               ("statement_review_months", "cada cuántos meses la junta revisa la declaración de apetito, según el marco")),
    "casandra": (("registration_days", "los días que la política da para registrar un evento desde que se descubre"),
                 ("repeat_window_months", "la ventana, en meses, en que dos eventos del mismo tipo en el mismo proceso cuentan como repetidos")),
}


def metodologia(cfg: dict) -> dict:
    return cfg.get("methodology") or {}


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
    if not _periodo_ok(cfg.get("period")):
        p.append("period vacío: el periodo que se evalúa, AAAA-MM, el último cerrado")
    for k, que in PARAMETROS.get(rol, ()):
        v = numero(metodologia(cfg).get(k))
        if v is None or v < 0:
            p.append(f"methodology.{k} vacío: {que}")
    return p


def _periodo_ok(p) -> bool:
    try:
        dt.date.fromisoformat(f"{p}-01")
        return len(str(p)) == 7
    except (TypeError, ValueError):
        return False


def _fin(periodo: str) -> dt.date:
    a, m = int(periodo[:4]), int(periodo[5:7])
    return dt.date(a, m, calendar.monthrange(a, m)[1])


def _meses_atras(d: dt.date, n: float) -> dt.date:
    m = d.year * 12 + d.month - 1 - int(n)
    return dt.date(m // 12, m % 12 + 1, min(d.day, 28))


def _ficha(cfg: dict, rol: str, periodo: str) -> dict:
    return leer_json(cfg["_estado"] / SUB[rol] / periodo / "ficha.json", {}) or {}


def _archivo(src) -> str:
    return str(src or "").split(",")[0].strip()


def _cita(src) -> dict | None:
    return {"archivo": _archivo(src)} if src else None


def _sin_ficha(docs: Path, carpetas: tuple, citadas: set, aviso: str) -> list[str]:
    """Los documentos escritos de unas carpetas que la ficha no cita: se le dice a quien la escribe."""
    out = []
    citadas = {_archivo(s) for s in citadas}
    for carpeta in carpetas:
        base = docs / carpeta
        for p in sorted(x for x in base.rglob("*") if x.is_file() and not x.name.startswith(".")) if base.is_dir() else []:
            if p.suffix.lower() in (".csv", ".xlsx"):
                continue
            if rel(p, docs) not in citadas:
                out.append(f"{rel(p, docs)} no está en la ficha: {aviso}")
    return out


def _pais(cfg: dict) -> str:
    return str((cfg.get("entity") or {}).get("country") or "").upper()


def _alto(calificacion) -> bool:
    return norm(calificacion) in ALTOS


def _num(v: float | None) -> str:
    return "—" if v is None else f"{v:,.2f}".rstrip("0").rstrip(".")


# ================================================================ Severo · el apetito

def severo(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    met = metodologia(cfg)
    dias_reporte = int(numero(met.get("report_days")) or 0)
    meses_decl = numero(met.get("statement_review_months"))
    ficha = _ficha(cfg, "severo", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    mat, lim, kri = (tabla(cfg, q, no_proc) for q in ("matriz", "limites", "indicadores"))
    exp, pla = tabla(cfg, "exposicion", no_proc, periodo), tabla(cfg, "planes", no_proc)
    if lim is None and not any(x["motivo"].startswith("limites") for x in no_proc):
        no_proc.append({"archivo": "00-marco", "motivo": "no está la tabla de límites del marco de apetito: sin ella no se contrasta ninguna exposición"})
    decl = ficha.get("statement") or {}
    aprob = ficha.get("approvals") or []
    citadas = {str(decl.get("source"))} | {str(x.get("source")) for x in aprob} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, ESCRITOS, citadas, "es parte del marco o un acta del comité o de la junta; corre appetite-scan")
    if not decl.get("source"):
        problemas.append("la ficha no trae la declaración de apetito con la fecha de su última revisión por la junta y su cita")
    for x in aprob:
        if not (x.get("limit") and x.get("source")):
            problemas.append(f"una aprobación de la ficha no trae el límite o la cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    fin = _fin(periodo)
    plazo = fin + dt.timedelta(days=dias_reporte)
    exposiciones = {}
    for x in exp.filas if exp else []:
        if _del_periodo(x, periodo):
            exposiciones[norm(x["limite"])] = x
    planes = {norm(x["limite"]): x for x in (pla.filas if pla else [])}
    aprobados = {}
    for x in aprob:
        hasta = fecha(x.get("until"))
        if x.get("limit") and (not hasta or hasta >= hoy):
            aprobados[norm(x["limit"])] = x
    filas = lim.filas if lim else []
    if filas and exp is None:
        no_proc.append({"archivo": "10-exposicion", "motivo": f"no está la exposición de {periodo}: sin ella no se sabe qué límite está excedido"})
    limites = []
    for x in filas:
        lid, cita = x["limite"], lim.cita(x, docs)
        nom = f"{lid} · {x.get('metrica') or ''}".strip(" ·")
        valor, minimo = numero(x.get("valor")), norm(x.get("sentido")) in MINIMO
        e = exposiciones.get(norm(lid))
        v = numero(e.get("valor")) if e else None
        rep = fecha(e.get("reporte")) if e else None
        excedido = v is not None and valor is not None and (v < valor if minimo else v > valor)
        cubierto = "plan" if norm(lid) in planes else ("aprobado" if norm(lid) in aprobados else None)
        rev = fecha(x.get("revision"))
        limites.append({"limite": lid, "metrica": x.get("metrica"), "riesgo": x.get("riesgo"), "valor": valor, "sentido": "mínimo" if minimo else "máximo",
                        "unidad": x.get("unidad"), "dueno": x.get("dueno"), "revision": iso(rev), "exposicion": v, "reporte": iso(rep),
                        "area": e.get("area") if e else None, "excedido": excedido, "cubierto": cubierto})
        # 1 · La exposición contra su límite, y el exceso con su plan o su aprobación.
        if excedido and not cubierto:
            al.append(alerta("limit_breached_without_plan", f"{nom}: la exposición de {periodo} es {_num(v)} {x.get('unidad') or ''} y el límite "
                             f"{'mínimo' if minimo else 'máximo'} es {_num(valor)}; no hay plan de acción ni aprobación del exceso",
                             [cita, exp.cita(e, docs)], monto=abs(v - valor), responsable=x.get("dueno") or None, clave=f"limite:{lid}"))
        if e is None and exp is not None:
            no_proc.append({"archivo": rel(exp.ruta, docs), "motivo": f"{nom}: ningún área reportó su exposición de {periodo}"})
        # 2 · El reporte de la exposición contra el plazo del marco.
        if e is not None and rep and rep > plazo:
            al.append(alerta("exposure_report_late", f"{nom}: {e.get('area') or 'el área'} reportó su exposición de {periodo} el {iso(rep)}, y el marco da "
                             f"{dias_reporte} días después del cierre: hasta el {iso(plazo)}", exp.cita(e, docs),
                             responsable=e.get("area") or None, dias=(rep - plazo).days, clave=f"reporte:{lid}"))
        # 3 · El límite con su dueño y su revisión.
        if not x.get("dueno"):
            al.append(alerta("limit_without_owner", f"{nom}: el límite no tiene un dueño que responda por él", cita, clave=f"dueno:{lid}"))
        if rev and rev < hoy:
            al.append(alerta("limit_review_overdue", f"{nom}: su revisión tocaba el {iso(rev)}", cita, responsable=x.get("dueno") or None,
                             dias=(hoy - rev).days, clave=f"revision:{lid}"))
    # 4 · Cada riesgo alto o crítico de la matriz con su límite o su indicador.
    con_limite = {norm(x.get("riesgo")) for x in filas if x.get("riesgo")}
    con_indicador = {norm(x.get("riesgo")) for x in (kri.filas if kri else []) if x.get("riesgo")}
    cobertura = []
    if mat is None:
        no_proc.append({"archivo": "00-marco", "motivo": "no está la matriz de riesgos: sin ella no se sabe qué riesgo alto no tiene límite ni indicador"})
    for x in mat.filas if mat else []:
        if not _alto(x.get("calificacion")):
            continue
        k = norm(x["riesgo"])
        cobertura.append({"riesgo": x["riesgo"], "nombre": x.get("nombre"), "calificacion": x.get("calificacion"),
                          "limite": k in con_limite, "indicador": k in con_indicador})
        if lim is not None and k not in con_limite and k not in con_indicador:
            al.append(alerta("risk_without_limit", f"{x['riesgo']} · {x.get('nombre') or ''}: calificado {x.get('calificacion')} en la matriz, sin límite "
                             f"en el marco ni indicador clave que lo mida", mat.cita(x, docs), responsable=x.get("dueno") or None, clave=f"riesgo:{x['riesgo']}"))
    # 5 · La declaración de apetito contra la revisión de la junta.
    revisada = fecha(decl.get("board_review"))
    vence_decl = None
    if decl.get("source"):
        if not revisada:
            no_proc.append({"archivo": _archivo(decl.get("source")), "motivo": "la ficha no trae la fecha en que la junta revisó la declaración de apetito"})
        elif meses_decl is not None:
            vence_decl = _meses_atras(revisada, -meses_decl)
            if vence_decl < hoy:
                al.append(alerta("appetite_statement_outdated", f"{decl.get('name') or 'La declaración de apetito'}: la junta la revisó el {iso(revisada)}, y el marco "
                                 f"pide revisarla cada {int(meses_decl)} meses: tocaba el {iso(vence_decl)}", _cita(decl.get("source")),
                                 dias=(hoy - vence_decl).days, clave="declaracion:"))
    excedidos = [x for x in limites if x["excedido"]]
    marco = ["F-01"] + ([REGULADOR[_pais(cfg)]] if _pais(cfg) in REGULADOR else [])
    partes = {
        "appetite-scan": {"limites": len(limites), "excedidos": len(excedidos), "reportados": sum(1 for x in limites if x["exposicion"] is not None),
                          "riesgos_altos": len(cobertura), "aprobaciones": len(aprob), "fuentes": ["F-01"]},
        "limit-check": {"limites": limites, "plazo": iso(plazo), "dias": dias_reporte, "fuentes": marco},
        "framework-check": {"limites": limites, "declaracion": {"nombre": decl.get("name"), "revisada": iso(revisada), "vence": iso(vence_decl),
                                                               "fuente": _archivo(decl.get("source"))}, "fuentes": marco},
        "coverage-check": {"riesgos": cobertura, "fuentes": ["F-01"]},
    }
    vence = sorted(({"fecha": x["revision"], "que": f"{x['limite']} · revisión", "caso": x["limite"], "estado": "pendiente", "comando": "framework-check"}
                    for x in limites if x["revision"] and 0 <= (fecha(x["revision"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "severo", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ Casandra · los indicadores y los eventos

def _en_alerta(v: float, umbral: float | None, menor: bool) -> bool:
    return umbral is not None and (v <= umbral if menor else v >= umbral)


def casandra(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    met = metodologia(cfg)
    dias_registro = int(numero(met.get("registration_days")) or 0)
    ventana = numero(met.get("repeat_window_months")) or 0
    ficha = _ficha(cfg, "casandra", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    mat, kri = (tabla(cfg, q, no_proc) for q in ("matriz", "indicadores"))
    val, acc = tabla(cfg, "valores", no_proc, periodo), tabla(cfg, "acciones", no_proc, periodo)
    eve = tabla(cfg, "eventos", no_proc)
    acciones_ficha = ficha.get("actions") or []
    citadas = {str(x.get("source")) for x in acciones_ficha} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, ("40-actas",), citadas, "es un acta: las acciones sobre un indicador que acordó van a la ficha; corre events-scan")
    for x in acciones_ficha:
        if not (x.get("indicator") and x.get("source")):
            problemas.append(f"una acción de la ficha no trae el indicador o la cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    if kri is None and not any(x["motivo"].startswith("indicadores") for x in no_proc):
        no_proc.append({"archivo": "00-marco", "motivo": "no están los indicadores clave de riesgo con sus umbrales: sin ellos no se sabe cuál está en alerta"})
    # 1 y 2 · Cada indicador con su valor del periodo, y el que está en alerta con su acción.
    valores = {}
    for x in val.filas if val else []:
        if _del_periodo(x, periodo) and numero(x.get("valor")) is not None:
            valores[norm(x["indicador"])] = x
    con_accion = {norm(x["indicador"]) for x in (acc.filas if acc else []) if _del_periodo(x, periodo)}
    con_accion |= {norm(x.get("indicator")) for x in acciones_ficha if x.get("indicator")}
    indicadores = []
    for x in kri.filas if kri else []:
        k, nom = norm(x["indicador"]), f"{x['indicador']} · {x.get('nombre') or ''}".strip(" ·")
        menor = norm(x.get("sentido")) in MINIMO
        alerta_u, limite_u = numero(x.get("alerta")), numero(x.get("limite"))
        r = valores.get(k)
        v = numero(r.get("valor")) if r else None
        zona = None
        if v is not None:
            zona = "límite" if _en_alerta(v, limite_u, menor) else ("alerta" if _en_alerta(v, alerta_u, menor) else "normal")
        indicadores.append({"indicador": x["indicador"], "nombre": x.get("nombre"), "riesgo": x.get("riesgo"), "alerta": alerta_u, "limite": limite_u,
                            "sentido": "menor es peor" if menor else "mayor es peor", "valor": v, "zona": zona, "accion": k in con_accion})
        if r is None:
            if val is not None:
                al.append(alerta("kri_not_reported", f"{nom}: no tiene valor en {periodo}", kri.cita(x, docs), responsable=x.get("dueno") or None,
                                 clave=f"reporte:{x['indicador']}"))
            continue
        if zona in ("alerta", "límite") and k not in con_accion:
            umbral = limite_u if zona == "límite" else alerta_u
            al.append(alerta("kri_alert_without_action", f"{nom}: dio {_num(v)} en {periodo}, en su zona de {zona} ({_num(umbral)}), y no hay una acción "
                             f"registrada en la tabla de acciones ni en un acta", [kri.cita(x, docs), val.cita(r, docs)],
                             responsable=x.get("dueno") or None, clave=f"alerta:{x['indicador']}"))
    if kri is not None and val is None:
        no_proc.append({"archivo": "20-indicadores", "motivo": f"no están los valores de los indicadores de {periodo}"})
    # 3 a 6 · Cada evento de pérdida contra su causa, su monto, su proceso, su plazo, su repetición y la matriz.
    riesgos = {norm(x["riesgo"]) for x in (mat.filas if mat else [])}
    if eve is not None and mat is None:
        no_proc.append({"archivo": "00-marco", "motivo": "no está la matriz de riesgos: sin ella no se sabe qué evento no corresponde a ningún riesgo"})
    eventos, grupos = [], {}
    desde = _meses_atras(hoy, ventana)
    for x in eve.filas if eve else []:
        eid, cita = x["evento"], eve.cita(x, docs)
        ocu, des, reg = fecha(x.get("ocurrencia")), fecha(x.get("descubrimiento")), fecha(x.get("registro"))
        monto = numero(x.get("monto"))
        faltan = [n for n, v in (("causa", x.get("causa")), ("monto", monto), ("proceso", x.get("proceso"))) if v in (None, "")]
        tarde = (reg - (des or ocu)).days - dias_registro if reg and (des or ocu) else None
        eventos.append({"evento": eid, "tipo": x.get("tipo"), "proceso": x.get("proceso"), "ocurrencia": iso(ocu), "registro": iso(reg),
                        "monto": monto, "riesgo": x.get("riesgo"), "faltan": faltan, "dias_tarde": tarde if tarde and tarde > 0 else 0})
        if faltan:
            al.append(alerta("loss_event_incomplete", f"{eid} · {x.get('tipo') or 'sin tipo'}: la base no trae {', '.join(faltan)}", cita,
                             monto=monto, clave=f"incompleto:{eid}"))
        if tarde is not None and tarde > 0:
            al.append(alerta("loss_event_registered_late", f"{eid} · {x.get('tipo') or 'sin tipo'}: se descubrió el {iso(des or ocu)} y se registró el {iso(reg)}; "
                             f"la política da {dias_registro} días", cita, monto=monto, dias=tarde, clave=f"tarde:{eid}"))
        if mat is not None and (not x.get("riesgo") or norm(x.get("riesgo")) not in riesgos):
            al.append(alerta("loss_event_risk_unmapped", f"{eid} · {x.get('tipo') or 'sin tipo'}: "
                             + (f"el riesgo {x.get('riesgo')} no está en la matriz" if x.get("riesgo") else "no está asociado a ningún riesgo de la matriz"),
                             [cita, {"archivo": rel(mat.ruta, docs)}], monto=monto, clave=f"sin_riesgo:{eid}"))
        if x.get("proceso") and x.get("tipo") and ocu and desde <= ocu <= hoy:
            grupos.setdefault((norm(x["proceso"]), norm(x["tipo"])), []).append((ocu, x))
    repetidos = []
    for (proc, tipo), xs in sorted(grupos.items()):
        if len(xs) < 2:
            continue
        xs.sort(key=lambda t: t[0])
        ids = [x["evento"] for _, x in xs]
        total = sum(numero(x.get("monto")) or 0 for _, x in xs)
        repetidos.append({"proceso": xs[0][1]["proceso"], "tipo": xs[0][1]["tipo"], "eventos": ids, "monto": total})
        al.append(alerta("loss_event_repeated", f"«{xs[0][1]['tipo']}» en {xs[0][1]['proceso']}: {len(xs)} eventos en los últimos {int(ventana)} meses "
                         f"({', '.join(ids)}), del {iso(xs[0][0])} al {iso(xs[-1][0])}", [eve.cita(x, docs) for _, x in xs],
                         monto=total, clave=f"repetido:{proc}:{tipo}"))
    partes = {
        "events-scan": {"indicadores": len(indicadores), "en_alerta": sum(1 for x in indicadores if x["zona"] in ("alerta", "límite")),
                        "eventos": len(eventos), "acciones_ficha": len(acciones_ficha), "fuentes": ["F-01"]},
        "kri-check": {"indicadores": indicadores, "fuentes": ["F-01"]},
        "event-check": {"eventos": eventos, "dias": dias_registro, "fuentes": ["F-01"]},
        "pattern-check": {"repetidos": repetidos, "ventana": ventana,
                          "sin_riesgo": [x["evento"] for x in eventos if mat is not None and (not x["riesgo"] or norm(x["riesgo"]) not in riesgos)],
                          "fuentes": ["F-01"]},
    }
    return {"agente": "casandra", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": []}


# ================================================================ el reporte

SENALES_DE = {
    "limit-check": {"limit_breached_without_plan", "exposure_report_late"},
    "framework-check": {"limit_without_owner", "limit_review_overdue", "appetite_statement_outdated"},
    "coverage-check": {"risk_without_limit"},
    "kri-check": {"kri_alert_without_action", "kri_not_reported"},
    "event-check": {"loss_event_incomplete", "loss_event_registered_late"},
    "pattern-check": {"loss_event_repeated", "loss_event_risk_unmapped"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-cro")


def _sn(b) -> str:
    return "sí" if b else "no"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "appetite-scan":
        l += [f"**Límites en el marco:** {p['limites']} · **Con exposición reportada:** {p['reportados']} · **Excedidos:** {p['excedidos']} · "
              f"**Riesgos altos o críticos en la matriz:** {p['riesgos_altos']} · **Excesos aprobados en las actas:** {p['aprobaciones']}.", ""]
    elif comando == "limit-check":
        l += [f"**Plazo del marco para reportar:** {p['dias']} días después del cierre, hasta el {p['plazo']}.", "",
              "| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {x['limite']} | {x['metrica'] or '—'} | {x['sentido']} {_num(x['valor'])} {x['unidad'] or ''} | {_num(x['exposicion'])} | {_sn(x['excedido'])} | "
              f"{x['cubierto'] or '—'} | {x['area'] or '—'} | {x['reporte'] or '—'} |" for x in p["limites"]]
        l += ["", "Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.", ""]
    elif comando == "framework-check":
        d = p["declaracion"]
        l += [f"**Declaración de apetito:** {d['nombre'] or '—'} · revisada por la junta el {d['revisada'] or '—'} · próxima revisión {d['vence'] or '—'}"
              + (f" · `{d['fuente']}`" if d["fuente"] else "") + ".", "",
              "| Límite | Métrica | Dueño | Próxima revisión |", "|---|---|---|---|"]
        l += [f"| {x['limite']} | {x['metrica'] or '—'} | {x['dueno'] or '—'} | {x['revision'] or '—'} |" for x in p["limites"]]
        l += ["", "Quién es el dueño de un límite y cuándo se revisa lo fija el marco: aquí se dice cuál falta o se venció.", ""]
    elif comando == "coverage-check":
        l += ["| Riesgo | Calificación | Con límite | Con indicador |", "|---|---|---|---|"]
        l += [f"| {x['riesgo']} · {x['nombre'] or ''} | {x['calificacion']} | {_sn(x['limite'])} | {_sn(x['indicador'])} |" for x in p["riesgos"]]
        l += ["", "Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.", ""]
    elif comando == "events-scan":
        l += [f"**Indicadores clave de riesgo:** {p['indicadores']} · **En alerta o en su límite:** {p['en_alerta']} · **Eventos en la base:** {p['eventos']} · "
              f"**Acciones tomadas de las actas:** {p['acciones_ficha']}.", ""]
    elif comando == "kri-check":
        l += ["| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['indicador']} · {x['nombre'] or ''} | {x['sentido']} | {_num(x['alerta'])} | {_num(x['limite'])} | {_num(x['valor'])} | {x['zona'] or 'sin valor'} | "
              f"{_sn(x['accion'])} |" for x in p["indicadores"]]
        l += ["", "Los umbrales los fija el marco de apetito de la organización.", ""]
    elif comando == "event-check":
        l += [f"**Plazo de la política para registrar un evento:** {p['dias']} días desde que se descubre.", "",
              "| Evento | Tipo | Proceso | Ocurrió | Se registró | Monto | Le falta | Días tarde |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {x['evento']} | {x['tipo'] or '—'} | {x['proceso'] or '—'} | {x['ocurrencia'] or '—'} | {x['registro'] or '—'} | {_num(x['monto'])} | "
              f"{', '.join(x['faltan']) or '—'} | {x['dias_tarde'] or '—'} |" for x in p["eventos"]]
        l.append("")
    elif comando == "pattern-check":
        if p["repetidos"]:
            l += [f"| Proceso | Tipo de evento | Eventos en {int(p['ventana'])} meses | Monto |", "|---|---|---|---|"]
            l += [f"| {x['proceso']} | {x['tipo']} | {', '.join(x['eventos'])} | {_num(x['monto'])} |" for x in p["repetidos"]]
            l.append("")
        if p["sin_riesgo"]:
            l += ["**Eventos sin un riesgo de la matriz:** " + ", ".join(p["sin_riesgo"]) + ".", ""]
        l += ["Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.", ""]
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
    scan = {"severo": "appetite-scan", "casandra": "events-scan"}[rol]
    carpetas = {"severo": ("00-marco", "10-exposicion", "40-actas"), "casandra": ("20-indicadores", "30-eventos", "40-actas")}[rol]
    u = ultima(scan)
    if not u or (hoy - u).days >= 7 or any(nueva(c, u) for c in carpetas):
        toca.append(scan)
        motivo.append("documentos nuevos o la revisión semanal")
    r = AGENTE[rol](cfg, periodo, hoy)
    for cmd, senales in SENALES_DE.items():
        if cmd in r["partes"] and any(a["signal"] in senales for a in r["alertas"]) and ultima(cmd) != hoy:
            toca.append(cmd)
            motivo.append(f"{sum(1 for a in r['alertas'] if a['signal'] in senales)} señales abiertas en {N.nombre_comando(cmd).lower()}")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


AGENTE = {"severo": severo, "casandra": casandra}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-risk-events": "casandra"}.get(N.plugin(AQUI)["name"], "severo")


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
    ap = N.argumentos("El motor de Severo y Casandra.")
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

    hoy = dt.date(2026, 11, 25)
    ok("el cierre del periodo", [iso(_fin("2026-10")), iso(_fin("2024-02"))], ["2026-10-31", "2024-02-29"])
    ok("la zona de alerta, en los dos sentidos", [_en_alerta(5, 4, False), _en_alerta(3, 4, False), _en_alerta(3, 4, True), _en_alerta(5, None, False)],
       [True, False, True, False])
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "riesgos" / "e1", t / "estado" / "e1"
        _x(docs / "00-marco" / "matriz_de_riesgos.xlsx", [
            ["Riesgo", "Nombre", "Calificación", "Proceso", "Dueño"],
            ["R-01", "Crédito de consumo", "Alto", "Crédito", "Vicepresidencia de crédito"],
            ["R-02", "Liquidez", "Crítico", "Tesorería", "Tesorería"],
            ["R-03", "Fraude externo", "Alto", "Canales", "Operaciones"],
            ["R-04", "Continuidad", "Alto", "Tecnología", "Tecnología"],
            ["R-05", "Reputación", "Medio", "Mercadeo", "Mercadeo"]])
        _x(docs / "00-marco" / "limites.xlsx", [
            ["Límite", "Riesgo", "Métrica", "Valor del límite", "Sentido", "Dueño", "Próxima revisión", "Unidad"],
            ["L-01", "R-01", "Cartera vencida de consumo", "6", "Máximo", "Vicepresidencia de crédito", "2027-03-31", "%"],
            ["L-02", "R-02", "Indicador de liquidez", "120", "Mínimo", "", "2026-06-30", "%"],
            ["L-03", "R-01", "Concentración en el mayor deudor", "10", "Máximo", "Vicepresidencia de crédito", "2027-03-31", "%"]])
        _x(docs / "00-marco" / "indicadores_clave.xlsx", [
            ["Indicador", "Nombre", "Riesgo", "Umbral de alerta", "Umbral de límite", "Sentido", "Dueño"],
            ["KRI-01", "Transacciones fraudulentas por millón", "R-03", "40", "60", "Mayor", "Operaciones"],
            ["KRI-02", "Disponibilidad de canales", "R-03", "99.5", "99", "Menor", "Tecnología"],
            ["KRI-03", "Rotación de personal clave", "R-01", "8", "12", "Mayor", "Gestión humana"]])
        _x(docs / "10-exposicion" / "exposicion_2026-10.xlsx", [
            ["Límite", "Exposición", "Periodo", "Fecha de reporte", "Área"],
            ["L-01", "6.4", "2026-10", "2026-11-06", "Crédito"], ["L-02", "131", "2026-10", "2026-11-18", "Tesorería"],
            ["L-03", "11.2", "2026-10", "2026-11-05", "Crédito"]])
        _x(docs / "10-exposicion" / "planes_de_accion.xlsx", [["Límite", "Plan", "Responsable", "Fecha compromiso"]])
        for f in ("00-marco/declaracion_de_apetito.pdf", "40-actas/acta_comite_riesgos_2026-10.pdf"):
            (docs / f).parent.mkdir(parents=True, exist_ok=True)
            (docs / f).write_text("doc", encoding="utf-8")
        escribir_json(est / "apetito" / "2026-10" / "ficha.json", {
            "statement": {"name": "Declaración de apetito por riesgo", "board_review": "2025-08-28", "source": "00-marco/declaracion_de_apetito.pdf, p. 1"},
            "approvals": [{"limit": "L-03", "until": "2027-01-31", "source": "40-actas/acta_comite_riesgos_2026-10.pdf, p. 3"}]})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-10", "_docs": docs, "_estado": est,
               "methodology": {"report_days": 10, "statement_review_months": 12, "registration_days": 30, "repeat_window_months": 12}}
        ok("la configuración de Severo pasa", revisar_config(cfg, "severo"), [])
        r = severo(cfg, "2026-10", hoy)
        ok("Severo: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("appetite_statement_outdated", "declaracion:"), ("exposure_report_late", "reporte:L-02"), ("limit_breached_without_plan", "limite:L-01"),
            ("limit_review_overdue", "revision:L-02"), ("limit_without_owner", "dueno:L-02"), ("risk_without_limit", "riesgo:R-04")])
        ok("Severo: la ficha cita sus documentos", r["record_issues"], [])

        _x(docs / "20-indicadores" / "valores_indicadores_2026-10.xlsx", [["Indicador", "Periodo", "Valor"], ["KRI-01", "2026-10", "52"], ["KRI-02", "2026-10", "99.7"]])
        _x(docs / "20-indicadores" / "acciones_indicadores.xlsx", [["Indicador", "Periodo", "Acción", "Responsable"]])
        _x(docs / "30-eventos" / "base_de_eventos.xlsx", [
            ["Evento", "Fecha de ocurrencia", "Fecha de descubrimiento", "Fecha de registro", "Proceso", "Tipo", "Causa", "Monto", "Riesgo"],
            ["EV-01", "2026-03-10", "2026-03-12", "2026-03-20", "Canales", "Fraude con tarjeta", "Clonación", "18500000", "R-03"],
            ["EV-02", "2026-08-02", "2026-08-04", "2026-10-15", "Canales", "Fraude con tarjeta", "Clonación", "22100000", "R-03"],
            ["EV-03", "2026-09-14", "2026-09-14", "2026-09-30", "Tesorería", "Error de liquidación", "", "4300000", "R-02"],
            ["EV-04", "2026-10-03", "2026-10-03", "2026-10-10", "Mercadeo", "Multa por publicidad", "Pieza sin revisión", "9800000", "R-09"],
            ["EV-05", "2024-05-01", "2024-05-02", "2024-05-10", "Crédito", "Error de desembolso", "Digitación", "1200000", "R-01"],
            ["EV-06", "2024-06-01", "2024-06-02", "2024-06-10", "Crédito", "Error de desembolso", "Digitación", "900000", "R-01"]])
        escribir_json(est / "eventos" / "2026-10" / "ficha.json", {"reviewed": ["40-actas/acta_comite_riesgos_2026-10.pdf"]})
        ok("la configuración de Casandra pasa", revisar_config(cfg, "casandra"), [])
        r = casandra(cfg, "2026-10", hoy)
        ok("Casandra: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("kri_alert_without_action", "alerta:KRI-01"), ("kri_not_reported", "reporte:KRI-03"), ("loss_event_incomplete", "incompleto:EV-03"),
            ("loss_event_registered_late", "tarde:EV-02"), ("loss_event_repeated", "repetido:canales:fraude_con_tarjeta"),
            ("loss_event_risk_unmapped", "sin_riesgo:EV-04")])
        escribir_json(est / "eventos" / "2026-10" / "ficha.json", {"actions": [
            {"indicator": "KRI-01", "action": "Bloqueo preventivo de BIN comprometidos", "source": "40-actas/acta_comite_riesgos_2026-10.pdf, p. 2"}]})
        r = casandra(cfg, "2026-10", hoy)
        ok("Casandra: la acción del acta cubre el indicador", any(a["signal"] == "kri_alert_without_action" for a in r["alertas"]), False)
        ok("Casandra: la ficha cita sus documentos", r["record_issues"], [])
        md = reporte(r, "event-check", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        sin = dict(cfg, methodology={})
        ok("la configuración pide los plazos del marco", [sum("methodology." in x for x in revisar_config(sin, r)) for r in ("severo", "casandra")], [2, 2])
    print(f"\n{'Todo bien' if not fallas else str(len(fallas)) + ' fallas'}.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
