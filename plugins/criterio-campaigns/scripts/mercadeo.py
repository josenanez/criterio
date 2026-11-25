#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-claims/scripts/mercadeo.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
# -*- coding: utf-8 -*-
"""El motor de la familia CMO: lo que calcula el código para Lucía y Próspero.

    python3 mercadeo.py <acción> [opciones]       python3 mercadeo.py --help

Lucía (criterio-claims) procesa lo que se anuncia: cada afirmación de una pieza aprobada contra su
soporte, cada comparativa contra su fuente, cada promoción contra sus condiciones publicadas, cada
pieza contra su aprobación y su identificación como publicidad, y cada base de contactos que usa una
campaña contra su autorización para mercadeo. Próspero (criterio-campaigns), lo que se invierte: cada
campaña contra su presupuesto, su meta y su fecha de fin, cada factura de pauta contra su campaña y su
orden, y cada resultado reportado contra la exportación de la plataforma. Los dos comparten este motor,
que vive en criterio-claims y se copia al otro con scripts/sincronizar.py, y el núcleo común de las
familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —el registro de piezas, el
registro de bases de contactos, el plan de mercadeo, las facturas de pauta y la exportación de la
plataforma— las procesa el código. Lo que solo trae un documento escrito —cada afirmación de una pieza
con su soporte, cada promoción con sus condiciones y cada resultado de un informe— lo extrae el agente a
su ficha, con la cita, y el código lo cruza.

**Nunca aprueba una pieza, juzga la creatividad ni dice si una afirmación es verdadera; nunca se conecta
a una plataforma, y nunca procesa los datos de una persona** (decisión 0036): de una base de contactos
solo procesa su registro. **Las tolerancias, las metas y quién aprueba cada pieza los fija la
organización**, en su política: el código calcula y la persona decide.

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
SUB = {"lucia": "piezas", "prospero": "campanas"}
NOMBRE = {"lucia": "Lucía", "prospero": "Próspero"}
SI = ("si", "sí", "x", "yes", "true", "1", "s", "sim")
# La ley del consumidor de cada país, en las piezas de una entidad de ese país (fuentes.json de la familia).
LEY = {"CO": "F-10"}


def _si(v) -> bool:
    return norm(v) in SI


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
    "piezas": {"pieza": ["pieza", "id_pieza", "codigo", "id", "piece", "piece_id", "peca"],
               "nombre": ["nombre", "titulo", "descripcion", "name", "title", "nome"],
               "canal": ["canal", "medio", "channel", "meio"],
               "publicada": ["fecha_de_publicacion", "publicada_el", "publicacion", "published_on", "data_de_publicacao"],
               "aprobada": ["fecha_de_aprobacion", "aprobada_el", "aprobacion", "approved_on", "data_de_aprovacao"],
               "aprobado_por": ["aprobado_por", "aprueba", "approved_by", "aprovado_por"],
               "pagada": ["pagada_a_influenciador", "influenciador_pagado", "patrocinada", "pagada", "paid_influencer", "sponsored", "patrocinado"],
               "identificada": ["identificada_como_publicidad", "identificada", "etiqueta_publicidad", "disclosed", "identificado"],
               "influenciador": ["influenciador", "creador", "influencer", "creator"]},
    "bases": {"base": ["base", "base_de_contactos", "id_base", "codigo", "contact_base", "base_de_contatos"],
              "registros": ["registros", "contactos", "records", "contatos"],
              "autorizacion": ["autorizacion_para_mercadeo", "autorizacion_mercadeo", "autorizacion", "consentimiento", "marketing_consent", "consent",
                               "autorizacao"],
              "fecha": ["fecha_de_autorizacion", "fecha_autorizacion", "consent_date", "data_de_autorizacao"],
              "finalidad": ["finalidad", "proposito", "purpose", "finalidade"]},
    "plan": {"campana": ["campana", "id_campana", "codigo", "id", "campaign", "campaign_id", "campanha"],
             "nombre": ["nombre", "descripcion", "name", "nome"],
             "presupuesto": ["presupuesto", "presupuesto_aprobado", "budget", "orcamento"],
             "inicio": ["inicio", "fecha_de_inicio", "fecha_inicio", "start", "start_date", "data_de_inicio"],
             "fin": ["fin", "fecha_de_fin", "fecha_fin", "end", "end_date", "data_de_fim", "fim"],
             "meta": ["meta", "objetivo", "goal", "target"],
             "indicador": ["indicador", "kpi", "metrica", "indicator", "metric"],
             "base": ["base_de_contactos", "base", "contact_base", "base_de_contatos"]},
    "facturas": {"factura": ["factura", "numero_de_factura", "id_factura", "invoice", "invoice_number", "nota_fiscal"],
                 "valor": ["valor", "total", "monto", "amount", "valor_total"],
                 "campana": ["campana", "id_campana", "campaign", "campanha"],
                 "orden": ["orden_de_compra", "orden", "oc", "purchase_order", "po", "pedido"],
                 "proveedor": ["proveedor", "medio", "agencia", "vendor", "fornecedor"],
                 "fecha": ["fecha", "fecha_de_factura", "invoice_date", "data"],
                 "servicio": ["pauta_hasta", "fecha_de_servicio", "servicio_hasta", "service_date", "flight_end", "veiculacao_ate"]},
    "plataforma": {"campana": ["campana", "id_campana", "campaign", "campaign_id", "campanha"],
                   "indicador": ["indicador", "metrica", "kpi", "metric", "indicator"],
                   "valor": ["valor", "resultado", "value", "result"],
                   "corte": ["corte", "fecha_de_corte", "hasta", "date", "as_of", "periodo"]},
}
REQ = {"piezas": ["pieza"], "bases": ["base"], "plan": ["campana"], "facturas": ["factura", "valor"], "plataforma": ["campana", "indicador", "valor"]}
PATRONES = {"piezas": ("registro_de_piezas", "registro_piezas", "piece_register", "registro_de_pecas"),
            "bases": ("bases_de_contactos", "registro_de_bases", "contact_bases", "bases_de_contatos"),
            "plan": ("plan_de_mercadeo", "plan_mercadeo", "marketing_plan", "plano_de_marketing"),
            "facturas": ("facturas", "media_invoices", "notas_fiscais"),
            "plataforma": ("plataforma", "platform")}
CARPETA = {"piezas": "10-piezas", "bases": "40-bases", "plan": "50-campanas", "facturas": "50-campanas", "plataforma": "50-campanas"}


def tabla(cfg: dict, que: str, no_proc: list) -> Hoja | None:
    docs = cfg["_docs"]
    rutas = hallar(docs / CARPETA[que], *PATRONES[que])
    if not rutas:
        return None
    t = Hoja(rutas[-1], REQ[que], [c for c in ALIAS[que] if c not in REQ[que]], ALIAS[que], (cfg.get("columns") or {}).get(que))
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"{que}: no trae una columna reconocible para {', '.join(t.faltan)}; "
                                                                f"di cuál es en la configuración (columns.{que})"})
        return None
    return t


# ================================================================ la configuración

DEFECTOS = {"report": {"language": "es"}, "methodology": {"budget_tolerance_pct": 5, "result_tolerance_pct": 2}}
SEVERIDAD = {
    "claim_without_substantiation": 1, "contact_base_without_consent": 1, "piece_published_unapproved": 1, "campaign_over_budget": 1,
    "comparative_claim_without_source": 2, "promotion_terms_missing": 2, "sponsored_content_unidentified": 2,
    "media_invoice_unmatched": 2, "result_differs_from_platform": 2, "campaign_ran_past_end": 2,
    "campaign_without_goal": 3,
}
N.SEVERIDAD.update(SEVERIDAD)
PARAMETROS = {
    "lucia": (),
    "prospero": (("budget_tolerance_pct", "el porcentaje que la política tolera por encima del presupuesto de una campaña"),
                 ("result_tolerance_pct", "la diferencia, en porcentaje, que la política tolera entre un resultado reportado y la plataforma")),
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


# ================================================================ Lucía · lo que se anuncia

def lucia(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "lucia", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    pie, bas, pla = (tabla(cfg, q, no_proc) for q in ("piezas", "bases", "plan"))
    afirmaciones, promociones = ficha.get("claims") or [], ficha.get("promotions") or []
    citadas = {str(x.get("source")) for x in afirmaciones + promociones} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, ("10-piezas",), citadas, "es una pieza: sus afirmaciones van a la ficha; corre claims-scan")
    problemas += _sin_ficha(docs, ("30-promociones",), citadas, "son las bases de una promoción: sus condiciones van a la ficha; corre claims-scan")
    for x in afirmaciones:
        if not (x.get("piece") and x.get("claim") and x.get("source")):
            problemas.append(f"una afirmación de la ficha no trae pieza, texto o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    if pie is None and not any(x["motivo"].startswith("piezas") for x in no_proc):
        no_proc.append({"archivo": "10-piezas", "motivo": "no está el registro de piezas: sin él no se sabe qué pieza se publicó ni quién la aprobó"})
    # 1 y 2 · Cada afirmación con su soporte, y cada comparativa con su fuente.
    lista_af = []
    for x in afirmaciones:
        pid, sop = x.get("piece"), _archivo(x.get("support"))
        existe = bool(sop) and (docs / sop).is_file()
        comp = bool(x.get("comparative"))
        lista_af.append({"pieza": pid, "afirmacion": x.get("claim"), "soporte": sop or None, "existe": existe, "comparativa": comp,
                         "fuente": x.get("comparative_source") or None})
        if not existe:
            al.append(alerta("claim_without_substantiation", f"{pid}: «{x.get('claim')}» "
                             + (f"cita un soporte que no está en la carpeta, `{sop}`" if sop else "no tiene un soporte en la carpeta de soportes"),
                             _cita(x.get("source")), clave=f"soporte:{pid}"))
        if comp and not x.get("comparative_source"):
            al.append(alerta("comparative_claim_without_source", f"{pid}: «{x.get('claim')}» compara con la competencia y la pieza no dice su fuente ni su fecha",
                             _cita(x.get("source")), clave=f"comparativa:{pid}"))
    # 3 · Cada promoción con su vigencia y sus condiciones.
    lista_pr = []
    for x in promociones:
        faltan = [n for n, ok in (("el inicio", fecha(x.get("start"))), ("el fin", fecha(x.get("end"))), ("las condiciones de modo y lugar", x.get("conditions")))
                  if not ok]
        lista_pr.append({"promocion": x.get("name"), "inicio": iso(fecha(x.get("start"))), "fin": iso(fecha(x.get("end"))), "condiciones": bool(x.get("conditions")),
                         "fuente": _archivo(x.get("source")), "faltan": faltan})
        if faltan:
            al.append(alerta("promotion_terms_missing", f"{x.get('name')}: sus bases no publican {', '.join(faltan)}", _cita(x.get("source")),
                             clave=f"promocion:{_stem(x.get('source'))}"))
    # 4 y 5 · Cada pieza con su aprobación, y la pagada a un influenciador con su identificación.
    lista_pz = []
    for x in pie.filas if pie else []:
        pid, cita = x["pieza"], pie.cita(x, docs)
        pub, apr = fecha(x.get("publicada")), fecha(x.get("aprobada"))
        pagada, ident = _si(x.get("pagada")), _si(x.get("identificada"))
        lista_pz.append({"pieza": pid, "nombre": x.get("nombre"), "canal": x.get("canal"), "publicada": iso(pub), "aprobada": iso(apr),
                         "aprobado_por": x.get("aprobado_por") or None, "pagada": pagada, "identificada": ident})
        if pub and (not apr or apr > pub):
            al.append(alerta("piece_published_unapproved", f"{pid} · {x.get('nombre') or ''}: se publicó el {iso(pub)} "
                             + (f"y se aprobó el {iso(apr)}, después" if apr else "sin aprobación registrada"), cita,
                             dias=(apr - pub).days if apr else None, clave=f"aprobacion:{pid}"))
        if pagada and not ident:
            al.append(alerta("sponsored_content_unidentified", f"{pid} · {x.get('nombre') or ''}: es una pieza pagada a {x.get('influenciador') or 'un influenciador'} "
                             f"y no se identifica como publicidad", cita, clave=f"patrocinada:{pid}"))
    # 6 · Cada base de contactos que usa una campaña, con su autorización para mercadeo.
    registro = {norm(x["base"]): x for x in (bas.filas if bas else [])}
    lista_bs = []
    usadas = {}
    for x in pla.filas if pla else []:
        if x.get("base"):
            usadas.setdefault(norm(x["base"]), (x["base"], x["campana"], pla.cita(x, docs)))
    if usadas and bas is None:
        no_proc.append({"archivo": "40-bases", "motivo": "no está el registro de bases de contactos: sin él no se sabe qué base tiene autorización"})
    for k, (nombre, camp, cita) in sorted(usadas.items()):
        r = registro.get(k)
        ok = bool(r) and _si(r.get("autorizacion"))
        lista_bs.append({"base": nombre, "campana": camp, "registrada": bool(r), "autorizacion": ok, "registros": numero(r.get("registros")) if r else None})
        if bas is not None and not ok:
            al.append(alerta("contact_base_without_consent", f"{nombre}: la usa la campaña {camp} y "
                             + ("el registro de bases no le da autorización para mercadeo" if r else "no está en el registro de bases de contactos"),
                             [cita] + ([bas.cita(r, docs)] if r else []), clave=f"base:{nombre}"))
    marco = ["F-01"] + ([LEY[_pais(cfg)]] if _pais(cfg) in LEY else [])
    partes = {
        "claims-scan": {"piezas": len(lista_pz), "afirmaciones": len(lista_af), "promociones": len(lista_pr), "bases": len(lista_bs), "fuentes": marco},
        "claim-check": {"afirmaciones": lista_af, "fuentes": marco},
        "promo-check": {"promociones": lista_pr, "fuentes": marco},
        "approval-check": {"piezas": lista_pz, "bases": lista_bs, "fuentes": marco},
    }
    return {"agente": "lucia", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": []}


# ================================================================ Próspero · lo que se invierte

def prospero(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    met = metodologia(cfg)
    tol_p = numero(met.get("budget_tolerance_pct")) or 0.0
    tol_r = numero(met.get("result_tolerance_pct")) or 0.0
    ficha = _ficha(cfg, "prospero", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    pla, fac, pta = (tabla(cfg, q, no_proc) for q in ("plan", "facturas", "plataforma"))
    reportados = ficha.get("reported") or []
    citadas = {str(x.get("source")) for x in reportados} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, ("50-campanas",), citadas, "es un informe de resultados: sus cifras van a la ficha; corre campaigns-scan")
    for x in reportados:
        if not (x.get("campaign") and x.get("indicator") and x.get("source")) or numero(x.get("value")) is None:
            problemas.append(f"un resultado de la ficha no trae campaña, indicador, valor o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    if pla is None and not any(x["motivo"].startswith("plan") for x in no_proc):
        no_proc.append({"archivo": "50-campanas", "motivo": "no está el plan de mercadeo: sin él no se sabe el presupuesto ni la meta de ninguna campaña"})
    plan = {norm(x["campana"]): x for x in (pla.filas if pla else [])}
    # 1 · Cada factura de pauta con su campaña y su orden.
    gasto, tarde = {}, {}
    lista_fac = []
    for x in fac.filas if fac else []:
        fid, cita, v = x["factura"], fac.cita(x, docs), numero(x.get("valor"))
        k = norm(x.get("campana"))
        enplan = bool(k) and k in plan
        lista_fac.append({"factura": fid, "campana": x.get("campana") or None, "orden": x.get("orden") or None, "proveedor": x.get("proveedor"),
                          "valor": v, "en_plan": enplan})
        if not enplan or not x.get("orden"):
            falta = []
            if not x.get("campana"):
                falta.append("no dice a qué campaña pertenece")
            elif not enplan:
                falta.append(f"su campaña, {x.get('campana')}, no está en el plan de mercadeo")
            if not x.get("orden"):
                falta.append("no tiene orden de compra")
            al.append(alerta("media_invoice_unmatched", f"{fid} · {x.get('proveedor') or ''}: " + " y ".join(falta), cita, monto=v, clave=f"factura:{fid}"))
        if enplan and v is not None:
            gasto[k] = gasto.get(k, 0.0) + v
            fin, serv = fecha(plan[k].get("fin")), fecha(x.get("servicio")) or fecha(x.get("fecha"))
            if fin and serv and serv > fin:
                tarde.setdefault(k, []).append((serv, x, v))
    # 2, 3 y 4 · Cada campaña contra su presupuesto, su meta y su fecha de fin.
    campanas = []
    for k, x in plan.items():
        cid, cita = x["campana"], pla.cita(x, docs)
        pres, g = numero(x.get("presupuesto")), gasto.get(k, 0.0)
        campanas.append({"campana": cid, "nombre": x.get("nombre"), "presupuesto": pres, "facturado": g, "inicio": iso(fecha(x.get("inicio"))),
                         "fin": iso(fecha(x.get("fin"))), "meta": x.get("meta") or None, "indicador": x.get("indicador") or None})
        if pres is not None and g > pres * (1 + tol_p / 100):
            al.append(alerta("campaign_over_budget", f"{cid} · {x.get('nombre') or ''}: la pauta facturada suma {_num(g)} y el presupuesto es {_num(pres)}; "
                             f"la política tolera un {tol_p:g} % más", cita, monto=g - pres, clave=f"presupuesto:{cid}"))
        if not x.get("meta") or not x.get("indicador"):
            al.append(alerta("campaign_without_goal", f"{cid} · {x.get('nombre') or ''}: el plan no le fija "
                             + ("meta ni indicador" if not x.get("meta") and not x.get("indicador") else ("meta" if not x.get("meta") else "indicador")),
                             cita, clave=f"meta:{cid}"))
        if k in tarde:
            ult = max(tarde[k], key=lambda t: t[0])
            al.append(alerta("campaign_ran_past_end", f"{cid} · {x.get('nombre') or ''}: terminaba el {iso(fecha(x.get('fin')))} y hay pauta facturada hasta el "
                             f"{iso(ult[0])} ({', '.join(f[1]['factura'] for f in tarde[k])})", [cita] + [fac.cita(f[1], docs) for f in tarde[k]],
                             monto=sum(f[2] or 0 for f in tarde[k]), dias=(ult[0] - fecha(x.get("fin"))).days, clave=f"fin:{cid}"))
    # 5 · Cada resultado reportado contra la exportación de la plataforma al mismo corte.
    plataforma = {}
    for x in pta.filas if pta else []:
        plataforma[(norm(x["campana"]), norm(x["indicador"]), iso(fecha(x.get("corte"))))] = x
    if reportados and pta is None:
        no_proc.append({"archivo": "50-campanas", "motivo": "no está la exportación de la plataforma: sin ella no se contrasta ningún resultado"})
    resultados = []
    for x in reportados:
        v = numero(x.get("value"))
        if v is None:
            continue
        corte = iso(fecha(x.get("cutoff")))
        r = plataforma.get((norm(x.get("campaign")), norm(x.get("indicator")), corte))
        w = numero(r.get("valor")) if r else None
        estado = "sin dato en la plataforma" if w is None else ("coincide" if _iguales(v, w, tol_r) else "distinto")
        resultados.append({"campana": x.get("campaign"), "indicador": x.get("indicator"), "corte": corte, "reportado": v, "plataforma": w, "estado": estado,
                           "fuente": _archivo(x.get("source"))})
        if pta is not None and w is None:
            no_proc.append({"archivo": rel(pta.ruta, docs), "motivo": f"{x.get('campaign')} · {x.get('indicator')}: la exportación no trae su valor al corte {corte or 'sin fecha'}"})
        elif estado == "distinto":
            al.append(alerta("result_differs_from_platform", f"{x.get('campaign')} · {x.get('indicator')}: el informe reporta {_num(v)} y la plataforma {_num(w)} "
                             f"al {corte}; la política tolera un {tol_r:g} %", [_cita(x.get("source")), pta.cita(r, docs)],
                             monto=abs(v - w), clave=f"resultado:{x.get('campaign')}:{norm(x.get('indicator'))}"))
    partes = {
        "campaigns-scan": {"campanas": len(campanas), "facturas": len(lista_fac), "resultados": len(resultados), "fuentes": ["F-02"]},
        "budget-check": {"campanas": campanas, "tolerancia": tol_p, "fuentes": ["F-02"]},
        "invoice-check": {"facturas": lista_fac, "fuentes": ["F-02"]},
        "result-check": {"resultados": resultados, "tolerancia": tol_r, "fuentes": ["F-02"]},
    }
    vence = sorted(({"fecha": c["fin"], "que": f"{c['campana']} · fin", "caso": c["campana"], "estado": "pendiente", "comando": "budget-check"}
                    for c in campanas if c["fin"] and 0 <= (fecha(c["fin"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "prospero", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ el reporte

SENALES_DE = {
    "claim-check": {"claim_without_substantiation", "comparative_claim_without_source"},
    "promo-check": {"promotion_terms_missing"},
    "approval-check": {"piece_published_unapproved", "sponsored_content_unidentified", "contact_base_without_consent"},
    "budget-check": {"campaign_over_budget", "campaign_without_goal", "campaign_ran_past_end"},
    "invoice-check": {"media_invoice_unmatched"},
    "result-check": {"result_differs_from_platform"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-cmo")


def _sn(b) -> str:
    return "sí" if b else "no"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "claims-scan":
        l += [f"**Piezas en el registro:** {p['piezas']} · **Afirmaciones en la ficha:** {p['afirmaciones']} · **Promociones:** {p['promociones']} · "
              f"**Bases de contactos en uso:** {p['bases']}.", ""]
    elif comando == "claim-check":
        l += ["| Pieza | Afirmación | Soporte | En la carpeta | Comparativa | Fuente citada |", "|---|---|---|---|---|---|"]
        l += [f"| {x['pieza']} | {x['afirmacion']} | {('`' + x['soporte'] + '`') if x['soporte'] else '—'} | {_sn(x['existe'])} | {_sn(x['comparativa'])} | "
              f"{x['fuente'] or '—'} |" for x in p["afirmaciones"]]
        l += ["", "Si el soporte basta lo decide legal: aquí se dice qué afirmación no tiene ninguno.", ""]
    elif comando == "promo-check":
        l += ["| Promoción | Inicio | Fin | Condiciones de modo y lugar | Bases |", "|---|---|---|---|---|"]
        l += [f"| {x['promocion']} | {x['inicio'] or '—'} | {x['fin'] or '—'} | {_sn(x['condiciones'])} | `{x['fuente']}` |" for x in p["promociones"]]
        l.append("")
    elif comando == "approval-check":
        l += ["| Pieza | Canal | Publicada | Aprobada | Aprobó | Pagada a un influenciador | Identificada |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['pieza']} · {x['nombre'] or ''} | {x['canal'] or '—'} | {x['publicada'] or '—'} | {x['aprobada'] or '—'} | {x['aprobado_por'] or '—'} | "
              f"{_sn(x['pagada'])} | {_sn(x['identificada']) if x['pagada'] else '—'} |" for x in p["piezas"]]
        if p["bases"]:
            l += ["", "| Base de contactos | Campaña | En el registro | Autorización para mercadeo |", "|---|---|---|---|"]
            l += [f"| {x['base']} | {x['campana']} | {_sn(x['registrada'])} | {_sn(x['autorizacion'])} |" for x in p["bases"]]
        l += ["", "Quién aprueba cada pieza lo fija la política de publicidad de la organización.", ""]
    elif comando == "campaigns-scan":
        l += [f"**Campañas en el plan:** {p['campanas']} · **Facturas de pauta:** {p['facturas']} · **Resultados reportados en la ficha:** {p['resultados']}.", ""]
    elif comando == "budget-check":
        l += [f"**Tolerancia de la política sobre el presupuesto:** {p['tolerancia']:g} %.", "",
              "| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |", "|---|---|---|---|---|---|---|"]
        l += [f"| {x['campana']} · {x['nombre'] or ''} | {_num(x['presupuesto'])} | {_num(x['facturado'])} | {x['inicio'] or '—'} | {x['fin'] or '—'} | "
              f"{x['meta'] or '—'} | {x['indicador'] or '—'} |" for x in p["campanas"]]
        l += ["", "Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.", ""]
    elif comando == "invoice-check":
        l += ["| Factura | Proveedor | Campaña | Orden de compra | Valor | En el plan |", "|---|---|---|---|---|---|"]
        l += [f"| {x['factura']} | {x['proveedor'] or '—'} | {x['campana'] or '—'} | {x['orden'] or '—'} | {_num(x['valor'])} | {_sn(x['en_plan'])} |"
              for x in p["facturas"]]
        l.append("")
    elif comando == "result-check":
        l += [f"**Tolerancia de la política entre el informe y la plataforma:** {p['tolerancia']:g} %.", "",
              "| Campaña | Indicador | Corte | Reportado | Plataforma | Estado |", "|---|---|---|---|---|---|"]
        l += [f"| {x['campana']} | {x['indicador']} | {x['corte'] or '—'} | {_num(x['reportado'])} | {_num(x['plataforma'])} | {x['estado']} |"
              for x in p["resultados"]]
        l += ["", "Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con la plataforma.", ""]
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
    scan = {"lucia": "claims-scan", "prospero": "campaigns-scan"}[rol]
    carpetas = {"lucia": ("10-piezas", "20-soportes", "30-promociones", "40-bases"), "prospero": ("50-campanas",)}[rol]
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


AGENTE = {"lucia": lucia, "prospero": prospero}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-campaigns": "prospero"}.get(N.plugin(AQUI)["name"], "lucia")


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
    ap = N.argumentos("El motor de Lucía y Próspero.")
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
    ok("la tolerancia: dentro y fuera", [_iguales(1000, 1015, 2), _iguales(1000, 1030, 2)], [True, False])
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "mercadeo" / "e1", t / "estado" / "e1"
        for f in ("10-piezas/pieza_P-01.pdf", "10-piezas/pieza_P-02.pdf", "20-soportes/estudio_rendimiento.pdf",
                  "30-promociones/bases_promocion_navidad.pdf", "30-promociones/bases_promocion_puntos.pdf"):
            _doc(docs, f)
        _x(docs / "10-piezas" / "registro_de_piezas.xlsx", [
            ["Pieza", "Nombre", "Canal", "Fecha de publicación", "Fecha de aprobación", "Aprobado por", "Pagada a influenciador", "Identificada como publicidad", "Influenciador"],
            ["P-01", "Tarjeta sin cuota", "Televisión", "2026-10-05", "2026-10-01", "Legal", "No", "", ""],
            ["P-02", "Crédito en minutos", "Redes", "2026-10-12", "2026-10-15", "Legal", "No", "", ""],
            ["P-03", "Reseña del crédito", "Instagram", "2026-10-20", "2026-10-18", "Legal", "Sí", "No", "@creadora"]])
        _x(docs / "40-bases" / "registro_de_bases_de_contactos.xlsx", [
            ["Base", "Registros", "Autorización para mercadeo", "Fecha de autorización"],
            ["B-01", "120000", "Sí", "2024-03-01"], ["B-02", "45000", "No", ""]])
        _x(docs / "50-campanas" / "plan_de_mercadeo.xlsx", [
            ["Campaña", "Nombre", "Presupuesto", "Inicio", "Fin", "Meta", "Indicador", "Base de contactos"],
            ["C-01", "Tarjeta sin cuota", "100000000", "2026-09-01", "2026-10-31", "5000 tarjetas", "Tarjetas emitidas", "B-01"],
            ["C-02", "Crédito en minutos", "50000000", "2026-09-15", "2026-10-15", "", "", "B-02"],
            ["C-03", "Navidad", "80000000", "2026-11-01", "2026-12-31", "2000 créditos", "Créditos desembolsados", "B-03"]])
        _x(docs / "50-campanas" / "facturas_de_pauta.xlsx", [
            ["Factura", "Proveedor", "Campaña", "Orden de compra", "Fecha", "Pauta hasta", "Valor"],
            ["F-101", "Canal Uno", "C-01", "OC-11", "2026-09-30", "2026-09-30", "60000000"],
            ["F-102", "Canal Uno", "C-01", "OC-11", "2026-10-31", "2026-10-31", "48000000"],
            ["F-103", "Redes SAS", "C-02", "OC-12", "2026-10-31", "2026-10-31", "20000000"],
            ["F-104", "Radio Norte", "", "", "2026-10-31", "2026-10-31", "7000000"]])
        _x(docs / "50-campanas" / "resultados_plataforma.xlsx", [
            ["Campaña", "Indicador", "Corte", "Valor"], ["C-01", "Tarjetas emitidas", "2026-10-31", "4100"], ["C-02", "Solicitudes", "2026-10-31", "9800"]])
        _doc(docs, "50-campanas/informe_de_resultados_2026-10.pdf")
        escribir_json(est / "piezas" / "2026-10" / "ficha.json", {
            "claims": [{"piece": "P-01", "claim": "La tarjeta sin cuota de manejo", "support": "20-soportes/estudio_rendimiento.pdf", "source": "10-piezas/pieza_P-01.pdf"},
                       {"piece": "P-02", "claim": "El crédito más rápido del país", "comparative": True, "support": "", "source": "10-piezas/pieza_P-02.pdf"}],
            "promotions": [{"name": "Navidad", "start": "2026-12-01", "end": "2026-12-24", "conditions": True, "source": "30-promociones/bases_promocion_navidad.pdf"},
                           {"name": "Puntos dobles", "start": "2026-11-01", "end": "", "conditions": True, "source": "30-promociones/bases_promocion_puntos.pdf"}]})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-10", "_docs": docs, "_estado": est,
               "methodology": {"budget_tolerance_pct": 5, "result_tolerance_pct": 2}}
        ok("la configuración de Lucía pasa", revisar_config(cfg, "lucia"), [])
        r = lucia(cfg, "2026-10", hoy)
        ok("Lucía: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("claim_without_substantiation", "soporte:P-02"), ("comparative_claim_without_source", "comparativa:P-02"),
            ("contact_base_without_consent", "base:B-02"), ("contact_base_without_consent", "base:B-03"),
            ("piece_published_unapproved", "aprobacion:P-02"), ("promotion_terms_missing", "promocion:bases_promocion_puntos"),
            ("sponsored_content_unidentified", "patrocinada:P-03")])
        ok("Lucía: la ficha cita sus documentos", r["record_issues"], [])
        escribir_json(est / "campanas" / "2026-10" / "ficha.json", {"reported": [
            {"campaign": "C-01", "indicator": "Tarjetas emitidas", "cutoff": "2026-10-31", "value": 4600, "source": "50-campanas/informe_de_resultados_2026-10.pdf, p. 1"},
            {"campaign": "C-02", "indicator": "Solicitudes", "cutoff": "2026-10-31", "value": 9900, "source": "50-campanas/informe_de_resultados_2026-10.pdf, p. 2"}]})
        ok("la configuración de Próspero pasa", revisar_config(cfg, "prospero"), [])
        r = prospero(cfg, "2026-10", hoy)
        ok("Próspero: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("campaign_over_budget", "presupuesto:C-01"), ("campaign_ran_past_end", "fin:C-02"), ("campaign_without_goal", "meta:C-02"),
            ("media_invoice_unmatched", "factura:F-104"), ("result_differs_from_platform", "resultado:C-01:tarjetas_emitidas")])
        ok("Próspero: la ficha cita sus documentos", r["record_issues"], [])
        md = reporte(r, "budget-check", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        ok("la configuración de Próspero pide las tolerancias", sum("methodology." in x for x in revisar_config(dict(cfg, methodology={}), "prospero")), 2)
    print(f"\n{'Todo bien' if not fallas else str(len(fallas)) + ' fallas'}.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
