#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-changes/scripts/tecnologia.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
# -*- coding: utf-8 -*-
"""El motor de la familia CTO: lo que calcula el código para Fausto y Domingo.

    python3 tecnologia.py <acción> [opciones]       python3 tecnologia.py --help

Fausto (criterio-changes) procesa los cambios y el servicio: cada cambio en producción contra su
aprobación y su revisión, cada despliegue contra su cambio, cada incidente mayor contra su problema y su
causa, y cada servicio contra el nivel acordado en el catálogo. Domingo (criterio-assets), los activos y
los proveedores: cada activo contra su dueño y el soporte de su fabricante, cada licencia contra su uso,
cada proveedor contra su nivel de servicio y la factura de la nube contra su presupuesto. Los dos
comparten este motor, que vive en criterio-changes y se copia al otro con scripts/sincronizar.py, y el
núcleo común de las familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —el catálogo de servicios, los
cambios, los despliegues, los incidentes, los problemas, la disponibilidad, el inventario, las licencias, el
cumplimiento y las facturas de los proveedores, y la factura y el presupuesto de la nube— las procesa el
código. Lo que solo trae un documento escrito —cada aprobación y cada revisión de un cambio en un acta,
cada excepción aprobada sobre un activo y cada nivel de servicio de un contrato con su crédito— lo extrae el
agente a su ficha, con la cita, y el código lo cruza.

**Nunca aprueba un cambio, decide una arquitectura ni elige un proveedor; nunca se conecta a una
herramienta, a la nube ni a un servidor, y nunca procesa la seguridad**, que es de la familia CISO
(decisión 0037). **Los plazos, los niveles y los umbrales los fija la organización**, en su política: el
código calcula y la persona decide.

Librería estándar, sin dependencias.
"""
from __future__ import annotations

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
SUB = {"fausto": "cambios", "domingo": "activos"}
NOMBRE = {"fausto": "Fausto", "domingo": "Domingo"}
SI = ("si", "sí", "x", "yes", "true", "1", "s", "sim")
# La norma de la nube de cada país, en una entidad de ese país (fuentes.json de la familia).
REGULADOR = {"CO": "F-10"}
EMERGENCIA = ("emergencia", "emergency", "urgente", "emergencial")
ESTANDAR = ("estandar", "standard", "preaprobado", "pre_aprobado", "padrao")
FALLIDO = ("fallido", "fallo", "revertido", "failed", "rolled_back", "rollback", "falhou", "revertida", "fallida")
PRODUCCION = ("produccion", "production", "prod", "producao")
MAYOR = ("p1", "1", "critica", "critico", "mayor", "major", "critical")


def _si(v) -> bool:
    return norm(v) in SI


def _es(v, lista) -> bool:
    return norm(v) in lista


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
    "catalogo": {"servicio": ["servicio", "id_servicio", "codigo", "service", "service_id", "servico"],
                 "nombre": ["nombre", "descripcion", "name", "nome"],
                 "nivel": ["disponibilidad_acordada", "nivel_de_disponibilidad", "disponibilidad_objetivo", "objetivo", "sla", "target_availability",
                           "availability_target", "disponibilidade_acordada"],
                 "dueno": ["dueno", "responsable", "owner", "responsavel"]},
    "cambios": {"cambio": ["cambio", "id_cambio", "numero", "change", "change_id", "number", "mudanca"],
                "tipo": ["tipo", "tipo_de_cambio", "type", "change_type", "tipo_de_mudanca"],
                "implementado": ["fecha_de_implementacion", "implementado", "implementado_el", "implemented", "implemented_on", "end_date", "data_de_implementacao"],
                "resultado": ["resultado", "estado_de_cierre", "close_code", "outcome", "result"],
                "servicio": ["servicio", "service", "ci", "servico"],
                "descripcion": ["descripcion", "resumen", "short_description", "description", "descricao"]},
    "despliegues": {"despliegue": ["despliegue", "id_despliegue", "deployment", "deployment_id", "release", "implantacao"],
                    "fecha": ["fecha", "fecha_de_despliegue", "date", "deployed_on", "data"],
                    "ambiente": ["ambiente", "entorno", "environment", "env"],
                    "cambio": ["cambio", "id_cambio", "change", "change_id", "mudanca"],
                    "sistema": ["sistema", "aplicacion", "system", "application", "app"]},
    "incidentes": {"incidente": ["incidente", "id_incidente", "numero", "incident", "incident_id", "number"],
                   "prioridad": ["prioridad", "priority", "prioridade", "severidad", "severity"],
                   "mayor": ["incidente_mayor", "mayor", "major_incident", "major"],
                   "servicio": ["servicio", "service", "servico"],
                   "resuelto": ["fecha_de_solucion", "resuelto", "resuelto_el", "resolved", "resolved_at", "data_de_resolucao"]},
    "problemas": {"problema": ["problema", "id_problema", "problem", "problem_id"],
                  "incidente": ["incidente", "incidentes", "incidente_relacionado", "incident", "related_incident", "incidents"],
                  "causa": ["causa", "causa_raiz", "root_cause", "cause", "causa_raiz_identificada"],
                  "registrado": ["fecha_de_registro", "registrado", "abierto", "opened", "opened_at", "data_de_registro"]},
    "disponibilidad": {"servicio": ["servicio", "service", "servico"],
                       "periodo": ["periodo", "mes", "period", "month"],
                       "valor": ["disponibilidad", "disponibilidad_medida", "valor", "availability", "value", "disponibilidade"]},
    "inventario": {"activo": ["activo", "id_activo", "codigo", "asset", "asset_id", "ci", "ativo"],
                   "nombre": ["nombre", "descripcion", "name", "nome"],
                   "dueno": ["dueno", "responsable", "owner", "responsavel"],
                   "ambiente": ["ambiente", "entorno", "environment", "env"],
                   "fin_soporte": ["fin_de_soporte", "fin_soporte", "end_of_support", "eos", "fim_do_suporte"]},
    "licencias": {"software": ["software", "producto", "product", "programa"],
                  "compradas": ["licencias_compradas", "compradas", "purchased", "entitlements", "licencas_compradas"],
                  "en_uso": ["licencias_en_uso", "en_uso", "instaladas", "asignadas", "in_use", "installed", "assigned", "em_uso"]},
    "cumplimiento": {"proveedor": ["proveedor", "vendor", "fornecedor"],
                     "metrica": ["metrica", "indicador", "metric", "kpi"],
                     "periodo": ["periodo", "mes", "period", "month"],
                     "valor": ["valor", "medido", "resultado", "value", "measured"]},
    "facturas": {"factura": ["factura", "numero_de_factura", "invoice", "invoice_number", "nota_fiscal"],
                 "proveedor": ["proveedor", "vendor", "fornecedor"],
                 "periodo": ["periodo", "mes", "period", "month"],
                 "valor": ["valor", "total", "monto", "amount"],
                 "credito": ["credito", "credito_por_nivel_de_servicio", "nota_credito", "credit", "service_credit", "desconto"]},
    "nube": {"cuenta": ["cuenta", "cuenta_de_nube", "suscripcion", "proyecto", "account", "subscription", "project", "conta"],
             "periodo": ["periodo", "mes", "period", "month"],
             "costo": ["costo", "valor", "cost", "amount", "custo"],
             "servicio": ["servicio", "service", "servico"]},
    "presupuesto_nube": {"cuenta": ["cuenta", "cuenta_de_nube", "suscripcion", "proyecto", "account", "subscription", "project", "conta"],
                         "periodo": ["periodo", "mes", "period", "month"],
                         "presupuesto": ["presupuesto", "budget", "orcamento"]},
}
REQ = {"catalogo": ["servicio"], "cambios": ["cambio"], "despliegues": ["despliegue"], "incidentes": ["incidente"], "problemas": ["problema"],
       "disponibilidad": ["servicio", "valor"], "inventario": ["activo"], "licencias": ["software", "compradas"], "cumplimiento": ["proveedor", "valor"],
       "facturas": ["factura", "proveedor"], "nube": ["cuenta", "costo"], "presupuesto_nube": ["cuenta", "presupuesto"]}
PATRONES = {"catalogo": ("catalogo_de_servicios", "catalogo_servicios", "service_catalog", "catalogo_de_servicos"),
            "cambios": ("cambios", "changes", "mudancas"),
            "despliegues": ("despliegues", "deployments", "implantacoes"),
            "incidentes": ("incidentes", "incidents"),
            "problemas": ("problemas", "problems"),
            "disponibilidad": ("disponibilidad", "availability", "disponibilidade"),
            "inventario": ("inventario", "inventory", "cmdb"),
            "licencias": ("licencias", "licenses", "licences", "licencas"),
            "cumplimiento": ("cumplimiento", "sla", "compliance"),
            "facturas": ("facturas", "invoices", "notas_fiscais"),
            "nube": ("factura_de_la_nube", "factura_nube", "costos_nube", "cloud_bill", "billing"),
            "presupuesto_nube": ("presupuesto_de_la_nube", "presupuesto_nube", "cloud_budget")}
CARPETA = {"catalogo": "00-politica", "cambios": "10-cambios", "despliegues": "10-cambios", "incidentes": "20-servicio", "problemas": "20-servicio",
           "disponibilidad": "20-servicio", "inventario": "30-activos", "licencias": "30-activos", "cumplimiento": "40-proveedores",
           "facturas": "40-proveedores", "nube": "50-nube", "presupuesto_nube": "50-nube"}
# Dos patrones que se pisan: «cambios» no es la factura ni el presupuesto, y la factura de la nube no es la del proveedor.
EXCLUYE = {"cambios": ("despliegues",), "facturas": ("nube",), "nube": ("presupuesto",)}


def tabla(cfg: dict, que: str, no_proc: list) -> Hoja | None:
    docs = cfg["_docs"]
    rutas = [r for r in hallar(docs / CARPETA[que], *PATRONES[que]) if not any(x in norm(r.stem) for x in EXCLUYE.get(que, ()))]
    if not rutas:
        return None
    t = Hoja(rutas[-1], REQ[que], [c for c in ALIAS[que] if c not in REQ[que]], ALIAS[que], (cfg.get("columns") or {}).get(que))
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"{que}: no trae una columna reconocible para {', '.join(t.faltan)}; "
                                                                f"di cuál es en la configuración (columns.{que})"})
        return None
    return t


# ================================================================ la configuración

DEFECTOS = {"report": {"language": "es"}, "methodology": {"emergency_review_days": 5, "problem_days": 10, "unused_license_pct": 15, "cloud_tolerance_pct": 5}}
SEVERIDAD = {
    "change_without_approval": 1, "deployment_without_change": 1, "asset_out_of_support": 1, "license_shortfall": 1,
    "emergency_change_without_review": 2, "failed_change_without_review": 2, "major_incident_without_problem": 2, "service_below_level": 2,
    "vendor_breach_without_credit": 2, "cloud_over_budget": 2,
    "asset_without_owner": 3, "license_unused": 3,
}
N.SEVERIDAD.update(SEVERIDAD)
PARAMETROS = {
    "fausto": (("emergency_review_days", "los días que da la política para revisar un cambio de emergencia después de implementarlo"),
               ("problem_days", "los días que da la política para registrar el problema de un incidente mayor, con su causa, después de resolverlo")),
    "domingo": (("unused_license_pct", "el porcentaje de licencias pagadas sin uso que la política tolera"),
                ("cloud_tolerance_pct", "el porcentaje que la política tolera por encima del presupuesto de cada cuenta de la nube")),
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
        p.append("period vacío: el periodo que se evalúa, AAAA-MM")
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


def _ficha(cfg: dict, rol: str, periodo: str) -> dict:
    return leer_json(cfg["_estado"] / SUB[rol] / periodo / "ficha.json", {}) or {}


def _archivo(src) -> str:
    return str(src or "").split(",")[0].strip()


def _cita(src) -> dict | None:
    return {"archivo": _archivo(src)} if src else None


def _stem(src) -> str:
    return norm(Path(_archivo(src)).stem)


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


def _num(v: float | None) -> str:
    return "—" if v is None else f"{v:,.2f}".rstrip("0").rstrip(".")


def _iguales(a: float, b: float, tol_pct: float) -> bool:
    base = max(abs(a), abs(b))
    return base == 0 or abs(a - b) <= base * tol_pct / 100




def _del_periodo(x: dict, periodo: str) -> bool:
    """Una fila de un periodo: su columna de periodo, o, sin ella, cualquiera."""
    p = str(x.get("periodo") or "").strip()
    return not p or p[:7] == periodo


# ================================================================ Fausto · los cambios y el servicio

def fausto(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    met = metodologia(cfg)
    dias_rev = numero(met.get("emergency_review_days")) or 0
    dias_pro = numero(met.get("problem_days")) or 0
    ficha = _ficha(cfg, "fausto", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    cat, cam, des, inc, pro, dis = (tabla(cfg, q, no_proc) for q in ("catalogo", "cambios", "despliegues", "incidentes", "problemas", "disponibilidad"))
    aprob, revis = ficha.get("approvals") or [], ficha.get("reviews") or []
    citadas = {str(x.get("source")) for x in aprob + revis} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, ("10-cambios",), citadas, "es un acta del comité de cambios: sus aprobaciones y revisiones van a la ficha; corre changes-scan")
    for x in aprob:
        if not (x.get("change") and x.get("source")) or not fecha(x.get("date")):
            problemas.append(f"una aprobación de la ficha no trae cambio, fecha o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    for x in revis:
        if not (x.get("change") and x.get("source")) or not fecha(x.get("date")):
            problemas.append(f"una revisión de la ficha no trae cambio, fecha o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    if cam is None and not any(x["motivo"].startswith("cambios") for x in no_proc):
        no_proc.append({"archivo": "10-cambios", "motivo": "no está la exportación de cambios: sin ella no se sabe qué cambio llegó a producción"})
    aprobado = {}
    for x in aprob:
        if x.get("change") and fecha(x.get("date")):
            k = norm(x["change"])
            aprobado[k] = min(aprobado.get(k, fecha(x["date"])), fecha(x["date"]))
    revisado = {}
    for x in revis:
        if x.get("change") and fecha(x.get("date")):
            k = norm(x["change"])
            revisado[k] = min(revisado.get(k, fecha(x["date"])), fecha(x["date"]))
    # 1, 2 y 3 · Cada cambio con su aprobación y, el de emergencia y el fallido, con su revisión.
    cambios = []
    for x in cam.filas if cam else []:
        cid, cita, k = x["cambio"], cam.cita(x, docs), norm(x["cambio"])
        impl = fecha(x.get("implementado"))
        emerg, estd, fall = _es(x.get("tipo"), EMERGENCIA), _es(x.get("tipo"), ESTANDAR), _es(x.get("resultado"), FALLIDO)
        apr, rev = aprobado.get(k), revisado.get(k)
        cambios.append({"cambio": cid, "tipo": x.get("tipo") or None, "implementado": iso(impl), "resultado": x.get("resultado") or None,
                        "aprobado": iso(apr), "revisado": iso(rev), "servicio": x.get("servicio") or None})
        if not impl or impl > hoy:
            continue
        nom = f"{cid}" + (f" · {x.get('descripcion')}" if x.get("descripcion") else "")
        if not emerg and not estd and (not apr or apr > impl):
            al.append(alerta("change_without_approval", f"{nom}: se implementó el {iso(impl)} "
                             + (f"y el comité lo aprobó el {iso(apr)}, después" if apr else "sin una aprobación en las actas del comité de cambios"),
                             cita, dias=(apr - impl).days if apr else None, clave=f"aprobacion:{cid}"))
        if emerg:
            plazo = impl + dt.timedelta(days=int(dias_rev))
            if plazo < hoy and (not rev or rev > plazo):
                al.append(alerta("emergency_change_without_review", f"{nom}: cambio de emergencia implementado el {iso(impl)}; la política da {int(dias_rev)} días "
                                 "para su revisión posterior " + (f"y se revisó el {iso(rev)}, tarde" if rev else "y no tiene revisión en las actas"),
                                 cita, dias=(hoy - plazo).days, clave=f"emergencia:{cid}"))
        if fall and not rev:
            al.append(alerta("failed_change_without_review", f"{nom}: terminó como «{x.get('resultado')}» el {iso(impl)} y no tiene revisión posterior en las actas",
                             cita, clave=f"fallido:{cid}"))
    # 4 · Cada despliegue en producción con su cambio.
    conocidos = {norm(x["cambio"]) for x in (cam.filas if cam else [])}
    despliegues = []
    for x in des.filas if des else []:
        if x.get("ambiente") and not _es(x.get("ambiente"), PRODUCCION):
            continue
        did, cita = x["despliegue"], des.cita(x, docs)
        ok = bool(x.get("cambio")) and norm(x["cambio"]) in conocidos
        despliegues.append({"despliegue": did, "fecha": iso(fecha(x.get("fecha"))), "sistema": x.get("sistema") or None, "cambio": x.get("cambio") or None, "con_cambio": ok})
        if cam is not None and not ok:
            al.append(alerta("deployment_without_change", f"{did}" + (f" · {x.get('sistema')}" if x.get("sistema") else "") + f": desplegado en producción el {iso(fecha(x.get('fecha')))} "
                             + (f"con el cambio {x['cambio']}, que no está en la exportación de cambios" if x.get("cambio") else "sin un cambio que lo autorice"),
                             cita, clave=f"despliegue:{did}"))
    # 5 · Cada incidente mayor con su problema y su causa.
    por_incidente = {}
    for x in pro.filas if pro else []:
        for i in str(x.get("incidente") or "").replace(";", ",").split(","):
            if i.strip():
                por_incidente.setdefault(norm(i), []).append(x)
    mayores = []
    for x in inc.filas if inc else []:
        if not (_si(x.get("mayor")) or (not x.get("mayor") and _es(x.get("prioridad"), MAYOR))):
            continue
        iid, cita, res = x["incidente"], inc.cita(x, docs), fecha(x.get("resuelto"))
        ps = por_incidente.get(norm(iid), [])
        con_causa = [p for p in ps if p.get("causa")]
        mayores.append({"incidente": iid, "servicio": x.get("servicio") or None, "resuelto": iso(res), "problema": ps[0]["problema"] if ps else None,
                        "causa": bool(con_causa)})
        if res and res + dt.timedelta(days=int(dias_pro)) < hoy and not con_causa:
            al.append(alerta("major_incident_without_problem", f"{iid}" + (f" · {x.get('servicio')}" if x.get("servicio") else "") + f": incidente mayor resuelto el {iso(res)}; "
                             + (f"su problema, {ps[0]['problema']}, no tiene causa" if ps else "no tiene un registro de problema") + f", y la política da {int(dias_pro)} días",
                             [cita] + ([pro.cita(ps[0], docs)] if ps else []), dias=(hoy - res).days - int(dias_pro), clave=f"problema:{iid}"))
    if mayores and pro is None and not any(x["motivo"].startswith("problemas") for x in no_proc):
        no_proc.append({"archivo": "20-servicio", "motivo": "no está la exportación de problemas: sin ella no se sabe si un incidente mayor tiene su causa"})
    # 6 · Cada servicio contra su nivel acordado.
    niveles = {norm(x["servicio"]): x for x in (cat.filas if cat else [])}
    servicios = []
    for x in dis.filas if dis else []:
        if not _del_periodo(x, periodo):
            continue
        s, v = x["servicio"], numero(x.get("valor"))
        c = niveles.get(norm(s))
        obj = numero(c.get("nivel")) if c else None
        servicios.append({"servicio": s, "nombre": c.get("nombre") if c else None, "nivel": obj, "medido": v})
        if obj is not None and v is not None and v < obj:
            al.append(alerta("service_below_level", f"{s}" + (f" · {c.get('nombre')}" if c and c.get("nombre") else "") + f": dio {_num(v)} % de disponibilidad en {periodo} "
                             f"y el catálogo acuerda {_num(obj)} %", [dis.cita(x, docs), cat.cita(c, docs)], clave=f"nivel:{s}"))
    if dis is not None and cat is None:
        no_proc.append({"archivo": "00-politica", "motivo": "no está el catálogo de servicios: sin él no se sabe el nivel acordado de ningún servicio"})
    partes = {
        "changes-scan": {"cambios": len(cambios), "despliegues": len(despliegues), "incidentes_mayores": len(mayores), "servicios": len(servicios),
                         "aprobaciones": len(aprob), "revisiones": len(revis), "fuentes": ["F-01"]},
        "change-check": {"cambios": cambios, "despliegues": despliegues, "dias_revision": dias_rev, "fuentes": ["F-01"]},
        "incident-check": {"incidentes": mayores, "dias_problema": dias_pro, "fuentes": ["F-01"]},
        "service-check": {"servicios": servicios, "fuentes": ["F-01"]},
    }
    return {"agente": "fausto", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": []}


# ================================================================ Domingo · los activos y los proveedores

def domingo(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    met = metodologia(cfg)
    umbral = numero(met.get("unused_license_pct")) or 0.0
    tol = numero(met.get("cloud_tolerance_pct")) or 0.0
    ficha = _ficha(cfg, "domingo", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    inv, lic, cum, fac, nub, pre = (tabla(cfg, q, no_proc) for q in ("inventario", "licencias", "cumplimiento", "facturas", "nube", "presupuesto_nube"))
    excep, niveles = ficha.get("exceptions") or [], ficha.get("service_levels") or []
    citadas = {str(x.get("source")) for x in excep + niveles} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, ("30-activos",), citadas, "es un acta del comité de arquitectura: sus excepciones van a la ficha; corre assets-scan")
    problemas += _sin_ficha(docs, ("40-proveedores",), citadas, "es un contrato: su nivel de servicio y su crédito van a la ficha; corre assets-scan")
    for x in excep:
        if not (x.get("asset") and x.get("source")):
            problemas.append(f"una excepción de la ficha no trae activo o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    for x in niveles:
        if not (x.get("vendor") and x.get("metric") and x.get("source")) or numero(x.get("target")) is None:
            problemas.append(f"un nivel de servicio de la ficha no trae proveedor, métrica, nivel o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    if inv is None and not any(x["motivo"].startswith("inventario") for x in no_proc):
        no_proc.append({"archivo": "30-activos", "motivo": "no está el inventario de activos: sin él no se sabe qué activo tiene dueño ni soporte"})
    # 1 y 2 · Cada activo con su dueño y, el de producción, con su soporte o su excepción.
    hasta = {}
    for x in excep:
        if x.get("asset"):
            k = norm(x["asset"])
            h = fecha(x.get("until"))
            hasta[k] = max(hasta.get(k) or h, h) if h else hasta.get(k)
            hasta.setdefault(k, None)
    activos = []
    for x in inv.filas if inv else []:
        aid, cita, k = x["activo"], inv.cita(x, docs), norm(x["activo"])
        fin = fecha(x.get("fin_soporte"))
        prod = _es(x.get("ambiente"), PRODUCCION)
        h = hasta.get(k)
        cubierto = k in hasta and (h is None or h >= hoy)
        activos.append({"activo": aid, "nombre": x.get("nombre") or None, "dueno": x.get("dueno") or None, "ambiente": x.get("ambiente") or None,
                        "fin_soporte": iso(fin), "excepcion": iso(h) if k in hasta else None})
        nom = f"{aid}" + (f" · {x.get('nombre')}" if x.get("nombre") else "")
        if not x.get("dueno"):
            al.append(alerta("asset_without_owner", f"{nom}: el inventario no le asigna un dueño", cita, clave=f"dueno:{aid}"))
        if prod and fin and fin < hoy and not cubierto:
            al.append(alerta("asset_out_of_support", f"{nom}: corre en producción y su fabricante terminó el soporte el {iso(fin)}"
                             + (f"; su excepción venció el {iso(h)}" if k in hasta and h else "; no tiene una excepción aprobada"),
                             cita, dias=(hoy - fin).days, clave=f"soporte:{aid}"))
    # 3 y 4 · Cada licencia contra su uso.
    licencias = []
    for x in lic.filas if lic else []:
        sw, cita = x["software"], lic.cita(x, docs)
        c, u = numero(x.get("compradas")), numero(x.get("en_uso"))
        if c is None or u is None:
            continue
        sobra = (c - u) / c * 100 if c else 0.0
        licencias.append({"software": sw, "compradas": c, "en_uso": u, "sobra_pct": round(sobra, 1)})
        if u > c:
            al.append(alerta("license_shortfall", f"{sw}: {_num(u)} en uso y {_num(c)} compradas", cita, monto=u - c, clave=f"faltante:{norm(sw)}"))
        elif sobra > umbral:
            al.append(alerta("license_unused", f"{sw}: {_num(c - u)} de {_num(c)} licencias pagadas sin uso, el {_num(round(sobra, 1))} %; la política tolera un {umbral:g} %",
                             cita, monto=c - u, clave=f"sobrante:{norm(sw)}"))
    # 5 · Cada proveedor contra su nivel de servicio y, si incumplió, su crédito en la factura.
    medido = {}
    for x in cum.filas if cum else []:
        if _del_periodo(x, periodo):
            medido[(norm(x["proveedor"]), norm(x.get("metrica")))] = x
    facturas = {}
    for x in fac.filas if fac else []:
        if _del_periodo(x, periodo):
            facturas.setdefault(norm(x["proveedor"]), []).append(x)
    proveedores = []
    for x in niveles:
        prov, met_, obj = x.get("vendor"), x.get("metric"), numero(x.get("target"))
        if not prov or obj is None:
            continue
        r = medido.get((norm(prov), norm(met_)))
        v = numero(r.get("valor")) if r else None
        fs = facturas.get(norm(prov), [])
        credito = sum(numero(f.get("credito")) or 0 for f in fs)
        incumple = v is not None and v < obj
        proveedores.append({"proveedor": prov, "metrica": met_, "nivel": obj, "medido": v, "credito_pct": numero(x.get("credit_pct")),
                            "facturado": sum(numero(f.get("valor")) or 0 for f in fs), "credito": credito, "incumple": incumple})
        if cum is not None and r is None:
            no_proc.append({"archivo": rel(cum.ruta, docs), "motivo": f"{prov} · {met_}: el cumplimiento no trae su valor de {periodo}"})
        if incumple and fs and credito <= 0:
            al.append(alerta("vendor_breach_without_credit", f"{prov} · {met_}: dio {_num(v)} en {periodo} y el contrato pacta {_num(obj)}"
                             + (f", con un crédito del {_num(numero(x.get('credit_pct')))} %" if numero(x.get("credit_pct")) else "")
                             + f"; su factura {', '.join(f['factura'] for f in fs)} no trae el crédito",
                             [_cita(x.get("source")), cum.cita(r, docs)] + [fac.cita(f, docs) for f in fs], monto=sum(numero(f.get("valor")) or 0 for f in fs),
                             clave=f"credito:{norm(prov)}"))
    # 6 · Cada cuenta de la nube contra su presupuesto.
    gasto = {}
    for x in nub.filas if nub else []:
        if _del_periodo(x, periodo):
            k = norm(x["cuenta"])
            gasto.setdefault(k, [x["cuenta"], 0.0, x])
            gasto[k][1] += numero(x.get("costo")) or 0.0
    presup = {norm(x["cuenta"]): x for x in (pre.filas if pre else []) if _del_periodo(x, periodo)}
    if gasto and pre is None:
        no_proc.append({"archivo": "50-nube", "motivo": "no está el presupuesto de la nube: sin él no se sabe qué cuenta se pasó"})
    nube = []
    for k, (cuenta, g, x0) in sorted(gasto.items()):
        p = presup.get(k)
        b = numero(p.get("presupuesto")) if p else None
        nube.append({"cuenta": cuenta, "facturado": g, "presupuesto": b})
        if b is not None and g > b * (1 + tol / 100):
            al.append(alerta("cloud_over_budget", f"{cuenta}: la nube facturó {_num(g)} en {periodo} y el presupuesto es {_num(b)}; la política tolera un {tol:g} % más",
                             [nub.cita(x0, docs), pre.cita(p, docs)], monto=g - b, clave=f"nube:{cuenta}"))
    marco = ["F-02"] + ([REGULADOR[_pais(cfg)]] if _pais(cfg) in REGULADOR and niveles else [])
    partes = {
        "assets-scan": {"activos": len(activos), "licencias": len(licencias), "proveedores": len(proveedores), "cuentas": len(nube),
                        "excepciones": len(excep), "fuentes": marco},
        "asset-check": {"activos": activos, "fuentes": ["F-02"]},
        "license-check": {"licencias": licencias, "umbral": umbral, "fuentes": ["F-02"]},
        "vendor-check": {"proveedores": proveedores, "fuentes": marco},
        "cloud-check": {"cuentas": nube, "tolerancia": tol, "fuentes": ["F-02"]},
    }
    vence = sorted(({"fecha": a["fin_soporte"], "que": f"{a['activo']} · fin de soporte", "caso": a["activo"], "estado": "pendiente", "comando": "asset-check"}
                    for a in activos if a["fin_soporte"] and 0 <= (fecha(a["fin_soporte"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "domingo", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ el reporte

SENALES_DE = {
    "change-check": {"change_without_approval", "emergency_change_without_review", "failed_change_without_review", "deployment_without_change"},
    "incident-check": {"major_incident_without_problem"},
    "service-check": {"service_below_level"},
    "asset-check": {"asset_without_owner", "asset_out_of_support"},
    "license-check": {"license_shortfall", "license_unused"},
    "vendor-check": {"vendor_breach_without_credit"},
    "cloud-check": {"cloud_over_budget"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-cto")


def _sn(b) -> str:
    return "sí" if b else "no"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "changes-scan":
        l += [f"**Cambios en la exportación:** {p['cambios']} · **Despliegues en producción:** {p['despliegues']} · **Incidentes mayores:** {p['incidentes_mayores']} · "
              f"**Servicios medidos:** {p['servicios']} · **Aprobaciones y revisiones en la ficha:** {p['aprobaciones']} y {p['revisiones']}.", ""]
    elif comando == "change-check":
        l += [f"**Días de la política para revisar un cambio de emergencia:** {p['dias_revision']:g}.", "",
              "| Cambio | Tipo | Implementado | Resultado | Aprobado | Revisado |", "|---|---|---|---|---|---|"]
        l += [f"| {x['cambio']} | {x['tipo'] or '—'} | {x['implementado'] or '—'} | {x['resultado'] or '—'} | {x['aprobado'] or '—'} | {x['revisado'] or '—'} |"
              for x in p["cambios"]]
        if p["despliegues"]:
            l += ["", "| Despliegue | Fecha | Sistema | Cambio | En la exportación |", "|---|---|---|---|---|"]
            l += [f"| {x['despliegue']} | {x['fecha'] or '—'} | {x['sistema'] or '—'} | {x['cambio'] or '—'} | {_sn(x['con_cambio'])} |" for x in p["despliegues"]]
        l += ["", "Si un cambio se aprueba lo decide el comité de cambios: aquí se dice cuál llegó a producción sin su aprobación o sin su revisión.", ""]
    elif comando == "incident-check":
        l += [f"**Días de la política para registrar el problema de un incidente mayor:** {p['dias_problema']:g}.", "",
              "| Incidente mayor | Servicio | Resuelto | Problema | Con causa |", "|---|---|---|---|---|"]
        l += [f"| {x['incidente']} | {x['servicio'] or '—'} | {x['resuelto'] or '—'} | {x['problema'] or '—'} | {_sn(x['causa'])} |" for x in p["incidentes"]]
        l.append("")
    elif comando == "service-check":
        l += ["| Servicio | Nivel acordado | Disponibilidad del periodo |", "|---|---|---|"]
        l += [f"| {x['servicio']}{' · ' + x['nombre'] if x['nombre'] else ''} | {_num(x['nivel'])} % | {_num(x['medido'])} % |" for x in p["servicios"]]
        l += ["", "El nivel lo acuerda el área con el negocio, en el catálogo: aquí se dice qué servicio no lo cumplió.", ""]
    elif comando == "assets-scan":
        l += [f"**Activos en el inventario:** {p['activos']} · **Software con licencias:** {p['licencias']} · **Proveedores con nivel en la ficha:** {p['proveedores']} · "
              f"**Cuentas de la nube:** {p['cuentas']} · **Excepciones en la ficha:** {p['excepciones']}.", ""]
    elif comando == "asset-check":
        l += ["| Activo | Dueño | Ambiente | Fin de soporte | Excepción hasta |", "|---|---|---|---|---|"]
        l += [f"| {x['activo']}{' · ' + x['nombre'] if x['nombre'] else ''} | {x['dueno'] or '—'} | {x['ambiente'] or '—'} | {x['fin_soporte'] or '—'} | {x['excepcion'] or '—'} |"
              for x in p["activos"]]
        l += ["", "Si un activo se renueva, se retira o se exceptúa lo decide el comité de arquitectura: aquí se dice cuál corre sin dueño o sin soporte.", ""]
    elif comando == "license-check":
        l += [f"**Licencias sin uso que tolera la política:** {p['umbral']:g} %.", "", "| Software | Compradas | En uso | Sin uso |", "|---|---|---|---|"]
        l += [f"| {x['software']} | {_num(x['compradas'])} | {_num(x['en_uso'])} | {_num(x['sobra_pct'])} % |" for x in p["licencias"]]
        l.append("")
    elif comando == "vendor-check":
        l += ["| Proveedor | Métrica | Nivel del contrato | Medido | Crédito pactado | Facturado | Crédito en la factura |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['proveedor']} | {x['metrica'] or '—'} | {_num(x['nivel'])} | {_num(x['medido'])} | {_num(x['credito_pct'])} % | {_num(x['facturado'])} | {_num(x['credito'])} |"
              for x in p["proveedores"]]
        l += ["", "Qué dice el contrato lo interpreta legal: aquí se dice qué incumplimiento se facturó completo.", ""]
    elif comando == "cloud-check":
        l += [f"**Tolerancia de la política sobre el presupuesto de cada cuenta:** {p['tolerancia']:g} %.", "", "| Cuenta | Facturado | Presupuesto |", "|---|---|---|"]
        l += [f"| {x['cuenta']} | {_num(x['facturado'])} | {_num(x['presupuesto'])} |" for x in p["cuentas"]]
        l.append("")
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
    scan = {"fausto": "changes-scan", "domingo": "assets-scan"}[rol]
    carpetas = {"fausto": ("10-cambios", "20-servicio"), "domingo": ("30-activos", "40-proveedores", "50-nube")}[rol]
    u = ultima(scan)
    if not u or (hoy - u).days >= 7 or any(nueva(c, u) for c in carpetas) or nueva("00-politica", u):
        toca.append(scan)
        motivo.append("documentos nuevos o la revisión semanal")
    r = AGENTE[rol](cfg, periodo, hoy)
    for cmd, senales in SENALES_DE.items():
        if cmd in r["partes"] and any(a["signal"] in senales for a in r["alertas"]) and ultima(cmd) != hoy:
            toca.append(cmd)
            motivo.append(f"{sum(1 for a in r['alertas'] if a['signal'] in senales)} señales abiertas en {N.nombre_comando(cmd).lower()}")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


AGENTE = {"fausto": fausto, "domingo": domingo}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-assets": "domingo"}.get(N.plugin(AQUI)["name"], "fausto")


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
    ap = N.argumentos("El motor de Fausto y Domingo.")
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

    def _doc(docs: Path, f: str) -> None:
        (docs / f).parent.mkdir(parents=True, exist_ok=True)
        (docs / f).write_text("doc", encoding="utf-8")

    hoy = dt.date(2026, 11, 25)
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "tecnologia" / "e1", t / "estado" / "e1"
        for f in ("10-cambios/acta_comite_de_cambios_2026-10.pdf", "30-activos/acta_comite_de_arquitectura_2026-10.pdf", "40-proveedores/contrato_nube.pdf"):
            _doc(docs, f)
        _x(docs / "00-politica" / "catalogo_de_servicios.xlsx", [["Servicio", "Nombre", "Disponibilidad acordada"], ["S-01", "Banca en línea", "99.9"], ["S-02", "Pagos", "99.5"]])
        _x(docs / "10-cambios" / "cambios.xlsx", [
            ["Cambio", "Tipo", "Fecha de implementación", "Resultado", "Servicio"],
            ["CHG-01", "Normal", "2026-10-05", "Exitoso", "S-01"], ["CHG-02", "Normal", "2026-10-08", "Exitoso", "S-01"],
            ["CHG-03", "Emergencia", "2026-10-10", "Exitoso", "S-02"], ["CHG-04", "Normal", "2026-10-12", "Revertido", "S-02"],
            ["CHG-05", "Estándar", "2026-10-15", "Exitoso", "S-01"]])
        _x(docs / "10-cambios" / "despliegues.xlsx", [["Despliegue", "Fecha", "Ambiente", "Cambio", "Sistema"],
            ["D-01", "2026-10-05", "Producción", "CHG-01", "Core"], ["D-02", "2026-10-20", "Producción", "", "App"], ["D-03", "2026-10-21", "Pruebas", "", "App"]])
        _x(docs / "20-servicio" / "incidentes.xlsx", [["Incidente", "Prioridad", "Incidente mayor", "Servicio", "Fecha de solución"],
            ["INC-01", "P1", "Sí", "S-01", "2026-10-02"], ["INC-02", "P1", "Sí", "S-02", "2026-10-09"], ["INC-03", "P3", "No", "S-02", "2026-10-11"]])
        _x(docs / "20-servicio" / "problemas.xlsx", [["Problema", "Incidente", "Causa", "Fecha de registro"], ["PRB-01", "INC-01", "Certificado vencido", "2026-10-05"]])
        _x(docs / "20-servicio" / "disponibilidad_2026-10.xlsx", [["Servicio", "Periodo", "Disponibilidad"], ["S-01", "2026-10", "99.95"], ["S-02", "2026-10", "99.1"]])
        escribir_json(est / "cambios" / "2026-10" / "ficha.json", {
            "approvals": [{"change": "CHG-01", "date": "2026-10-01", "authority": "Comité de cambios", "source": "10-cambios/acta_comite_de_cambios_2026-10.pdf"},
                          {"change": "CHG-02", "date": "2026-10-09", "authority": "Comité de cambios", "source": "10-cambios/acta_comite_de_cambios_2026-10.pdf"},
                          {"change": "CHG-04", "date": "2026-10-10", "authority": "Comité de cambios", "source": "10-cambios/acta_comite_de_cambios_2026-10.pdf"}],
            "reviews": []})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-10", "_docs": docs, "_estado": est,
               "methodology": {"emergency_review_days": 5, "problem_days": 10, "unused_license_pct": 15, "cloud_tolerance_pct": 5}}
        ok("la configuración de Fausto pasa", revisar_config(cfg, "fausto"), [])
        r = fausto(cfg, "2026-10", hoy)
        ok("Fausto: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("change_without_approval", "aprobacion:CHG-02"), ("deployment_without_change", "despliegue:D-02"),
            ("emergency_change_without_review", "emergencia:CHG-03"), ("failed_change_without_review", "fallido:CHG-04"),
            ("major_incident_without_problem", "problema:INC-02"), ("service_below_level", "nivel:S-02")])
        ok("Fausto: la ficha cita sus documentos", r["record_issues"], [])
        _x(docs / "30-activos" / "inventario_de_activos.xlsx", [["Activo", "Nombre", "Dueño", "Ambiente", "Fin de soporte"],
            ["A-01", "Servidor del core", "Infraestructura", "Producción", "2025-12-31"], ["A-02", "Base de datos", "", "Producción", "2028-06-30"],
            ["A-03", "Servidor de reportes", "Infraestructura", "Producción", "2026-03-31"], ["A-04", "Laboratorio", "Infraestructura", "Pruebas", "2024-01-01"]])
        _x(docs / "30-activos" / "licencias.xlsx", [["Software", "Licencias compradas", "Licencias en uso"], ["Ofimática", "500", "520"], ["Diseño", "50", "30"], ["Correo", "500", "480"]])
        _x(docs / "40-proveedores" / "cumplimiento_sla_2026-10.xlsx", [["Proveedor", "Métrica", "Periodo", "Valor"], ["Nube Uno", "Disponibilidad", "2026-10", "99.7"]])
        _x(docs / "40-proveedores" / "facturas_proveedores_2026-10.xlsx", [["Factura", "Proveedor", "Periodo", "Valor", "Crédito"], ["FV-01", "Nube Uno", "2026-10", "40000000", "0"]])
        _x(docs / "50-nube" / "factura_de_la_nube_2026-10.xlsx", [["Cuenta", "Periodo", "Servicio", "Costo"], ["Producción", "2026-10", "Cómputo", "70000000"],
            ["Producción", "2026-10", "Almacenamiento", "20000000"], ["Desarrollo", "2026-10", "Cómputo", "9000000"]])
        _x(docs / "50-nube" / "presupuesto_de_la_nube.xlsx", [["Cuenta", "Periodo", "Presupuesto"], ["Producción", "2026-10", "80000000"], ["Desarrollo", "2026-10", "10000000"]])
        escribir_json(est / "activos" / "2026-10" / "ficha.json", {
            "exceptions": [{"asset": "A-03", "until": "2027-03-31", "source": "30-activos/acta_comite_de_arquitectura_2026-10.pdf"}],
            "service_levels": [{"vendor": "Nube Uno", "metric": "Disponibilidad", "target": 99.95, "credit_pct": 10, "source": "40-proveedores/contrato_nube.pdf"}]})
        ok("la configuración de Domingo pasa", revisar_config(cfg, "domingo"), [])
        r = domingo(cfg, "2026-10", hoy)
        ok("Domingo: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("asset_out_of_support", "soporte:A-01"), ("asset_without_owner", "dueno:A-02"), ("cloud_over_budget", "nube:Producción"),
            ("license_shortfall", "faltante:ofimatica"), ("license_unused", "sobrante:diseno"), ("vendor_breach_without_credit", "credito:nube_uno")])
        ok("Domingo: la ficha cita sus documentos", r["record_issues"], [])
        md = reporte(r, "asset-check", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        ok("la configuración de Domingo pide sus umbrales", sum("methodology." in x for x in revisar_config(dict(cfg, methodology={}), "domingo")), 2)
    print(f"\n{'Todo bien' if not fallas else str(len(fallas)) + ' fallas'}.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
