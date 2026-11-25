#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CDO: lo que calcula el código para Custodia y Ariadna.

    python3 datos.py <acción> [opciones]       python3 datos.py --help

Custodia (criterio-data-governance) procesa el gobierno de los datos: cada conjunto del catálogo contra
su dueño y su clasificación, cada política contra su fecha de revisión, lo que se conserva contra el
plazo de la política, cada término de los informes contra el glosario de negocio y cada conjunto con
datos personales contra el registro de bases de la organización. Ariadna (criterio-data-quality), la
calidad y el linaje: cada cifra de un informe de dirección contra su fuente, su corte y su linaje, y
cada regla de calidad contra su umbral y su corrida. Las dos comparten este motor, que vive en
criterio-data-governance y se copia al otro con scripts/sincronizar.py, y el núcleo común de las
familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —el catálogo, el registro de
bases de datos personales, el glosario, el linaje, las cifras de la fuente, las reglas de calidad, sus
resultados y los datos críticos— las procesa el código. Lo que solo trae un documento escrito —las
políticas con su fecha de revisión, los plazos de conservación, los términos y las cifras de cada
informe— lo extrae el agente a su ficha, con la cita, y el código lo cruza.

**Nunca se conecta a una base ni a un sistema, y nunca procesa un dato personal** (decisión 0034):
procesa exportaciones, y de una base con datos personales solo sus metadatos. **Las tolerancias, los
umbrales y los plazos los fija la organización**, en su política de datos: el código calcula y la
persona decide.

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
    _hoy, _xlsx, alerta, escribir_json, fecha, filas_de, iso, leer_json, marco_reporte, norm, numero, ordenar,
    registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"
SUB = {"custodia": "gobierno", "ariadna": "calidad"}
NOMBRE = {"custodia": "Custodia", "ariadna": "Ariadna"}
SI = ("si", "sí", "x", "yes", "true", "1", "s")


def _si(v) -> bool:
    return norm(v) in SI


def _lista(v) -> list[str]:
    return [x.strip() for x in re.split(r"[;,/|]", str(v or "")) if x.strip()]


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
    "catalogo": {"conjunto": ["conjunto", "conjunto_de_datos", "dataset", "id", "codigo", "tabla", "asset"],
                 "nombre": ["nombre", "descripcion", "name", "description"],
                 "dueno": ["dueno", "dueno_de_negocio", "propietario", "responsable", "owner", "data_owner", "business_owner"],
                 "clasificacion": ["clasificacion", "confidencialidad", "nivel_de_clasificacion", "classification", "sensitivity"],
                 "tipo": ["tipo", "tipo_de_dato", "categoria", "type", "category"],
                 "personales": ["datos_personales", "personales", "contiene_datos_personales", "pii", "personal_data"],
                 "antiguo": ["dato_mas_antiguo", "registro_mas_antiguo", "desde", "fecha_mas_antigua", "oldest_record"],
                 "sistema": ["sistema", "sistema_de_origen", "fuente", "system", "source_system"]},
    "registro": {"conjunto": ["conjunto", "conjunto_de_datos", "base", "base_de_datos", "dataset"],
                 "numero": ["numero_de_registro", "registro", "radicado", "registration_number"],
                 "fecha": ["fecha_de_registro", "fecha", "registered_on"]},
    "glosario": {"termino": ["termino", "indicador", "concepto", "term"],
                 "definicion": ["definicion", "descripcion", "definition"],
                 "dueno": ["dueno", "responsable", "owner"]},
    "linaje": {"indicador": ["indicador", "cifra", "metrica", "indicator", "metric"],
               "paso": ["paso", "orden", "step"],
               "sistema": ["sistema_de_origen", "sistema", "origen", "source_system", "system"],
               "conjunto": ["conjunto", "conjunto_de_datos", "tabla", "dataset"]},
    "fuente": {"indicador": ["indicador", "cifra", "metrica", "indicator", "metric"],
               "corte": ["corte", "fecha_de_corte", "periodo", "cutoff", "as_of"],
               "valor": ["valor", "cifra_fuente", "value"]},
    "reglas": {"regla": ["regla", "id", "codigo", "rule", "rule_id"],
               "dato": ["dato", "campo", "elemento", "data_element", "field"],
               "umbral": ["umbral", "minimo", "meta", "threshold"]},
    "resultados": {"regla": ["regla", "id_regla", "rule", "rule_id"],
                   "periodo": ["periodo", "mes", "corte", "period"],
                   "resultado": ["resultado", "porcentaje", "cumplimiento", "score", "result"]},
    "criticos": {"dato": ["dato", "dato_critico", "elemento", "campo", "critical_data_element", "data_element"],
                 "dueno": ["dueno", "responsable", "owner"]},
}
REQ = {"catalogo": ["conjunto"], "registro": ["conjunto"], "glosario": ["termino"], "linaje": ["indicador"],
       "fuente": ["indicador", "corte", "valor"], "reglas": ["regla", "dato"], "resultados": ["regla", "resultado"], "criticos": ["dato"]}
PATRONES = {"catalogo": ("catalogo", "catalog"), "registro": ("registro_de_bases", "registro_bases", "bases_personales", "rnbd"),
            "glosario": ("glosario", "glossary"), "linaje": ("linaje", "lineage"), "fuente": ("cifras_fuente", "valores_fuente", "source_figures"),
            "reglas": ("reglas_calidad", "reglas_de_calidad", "quality_rules"), "resultados": ("resultados_calidad", "resultados_de_calidad", "quality_results"),
            "criticos": ("datos_criticos", "critical_data")}
CARPETA = {"catalogo": "10-catalogo", "registro": "10-catalogo", "glosario": "00-referencia", "linaje": "30-calidad", "fuente": "30-calidad",
           "reglas": "30-calidad", "resultados": "30-calidad", "criticos": "30-calidad"}


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

DEFECTOS = {"report": {"language": "es"}, "methodology": {"tolerance_pct": 0.5}}
SEVERIDAD = {
    "figure_differs_from_source": 1, "personal_data_unregistered": 1, "figure_without_source": 1,
    "dataset_without_owner": 2, "retention_exceeded": 2, "cutoff_mismatch": 2, "lineage_broken": 2, "quality_rule_below_threshold": 2,
    "quality_rule_not_run": 2, "critical_data_without_rule": 2,
    "dataset_without_classification": 3, "policy_review_overdue": 3, "term_not_in_glossary": 3,
}
N.SEVERIDAD.update(SEVERIDAD)


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
    if not re.fullmatch(r"\d{4}-\d{2}", str(cfg.get("period") or "")):
        p.append("period vacío: el periodo que se evalúa, AAAA-MM")
    if rol == "ariadna" and numero(metodologia(cfg).get("tolerance_pct")) is None:
        p.append("methodology.tolerance_pct vacío: la diferencia, en porcentaje, que la política de datos tolera entre una cifra y su fuente")
    return p


def _ficha(cfg: dict, rol: str, periodo: str) -> dict:
    return leer_json(cfg["_estado"] / SUB[rol] / periodo / "ficha.json", {}) or {}


def _archivo(src) -> str:
    return str(src or "").split(",")[0].strip()


def _cita(src) -> dict | None:
    return {"archivo": _archivo(src)} if src else None


def _informe(src) -> str:
    """El identificador de un informe en una clave: el nombre de su archivo, sin extensión."""
    return norm(Path(_archivo(src)).stem)


def _sin_ficha(docs: Path, carpeta: str, citadas: set, aviso: str) -> list[str]:
    """Los documentos escritos de una carpeta que la ficha no cita: se le dice a quien la escribe."""
    out = []
    citadas = {_archivo(s) for s in citadas}
    base = docs / carpeta
    for p in sorted(x for x in base.rglob("*") if x.is_file() and not x.name.startswith(".")) if base.is_dir() else []:
        if p.suffix.lower() in (".csv", ".xlsx"):
            continue
        if rel(p, docs) not in citadas:
            out.append(f"{rel(p, docs)} no está en la ficha: {aviso}")
    return out


def _meses_atras(d: dt.date, n: float) -> dt.date:
    m = d.year * 12 + d.month - 1 - int(n)
    return dt.date(m // 12, m % 12 + 1, min(d.day, 28))


# ================================================================ Custodia · el gobierno

def custodia(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "custodia", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    cat, reg, glo = (tabla(cfg, q, no_proc) for q in ("catalogo", "registro", "glosario"))
    if cat is None and not any(x["motivo"].startswith("catalogo") for x in no_proc):
        no_proc.append({"archivo": "10-catalogo", "motivo": "no está la exportación del catálogo de datos: sin ella no se calcula el gobierno de los conjuntos"})
    politicas, plazos, terminos = ficha.get("policies") or [], ficha.get("retention") or [], ficha.get("report_terms") or []
    citadas = {str(x.get("source")) for x in politicas + plazos + terminos} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, "00-referencia", citadas, "es una política o un documento de referencia; corre governance-scan")
    problemas += _sin_ficha(docs, "20-informes", citadas, "es un informe con términos que el glosario tiene que definir; corre governance-scan")
    for x in politicas:
        if not (x.get("name") and x.get("source")):
            problemas.append(f"una política de la ficha no trae nombre o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    filas = cat.filas if cat else []
    conjuntos = []
    # 1 y 2 · Cada conjunto con su dueño y su clasificación.
    for x in filas:
        cid, cita = x["conjunto"], cat.cita(x, docs)
        nom = f"{cid} · {x.get('nombre') or ''}".strip(" ·")
        conjuntos.append({"conjunto": cid, "nombre": x.get("nombre"), "dueno": x.get("dueno"), "clasificacion": x.get("clasificacion"),
                          "tipo": x.get("tipo"), "personales": _si(x.get("personales")), "antiguo": iso(fecha(x.get("antiguo")))})
        if not x.get("dueno"):
            al.append(alerta("dataset_without_owner", f"{nom}: el catálogo no le asigna un dueño de negocio", cita, clave=f"dueno:{cid}"))
        if not x.get("clasificacion"):
            al.append(alerta("dataset_without_classification", f"{nom}: el catálogo no trae su clasificación de confidencialidad", cita,
                             responsable=x.get("dueno") or None, clave=f"clasificacion:{cid}"))
    # 3 · Cada política contra su fecha de revisión.
    revisiones = []
    for x in politicas:
        prox = fecha(x.get("next_review"))
        revisiones.append({"politica": x.get("name"), "aprobada": iso(fecha(x.get("approved"))), "revision": iso(prox), "fuente": _archivo(x.get("source"))})
        if prox and prox < hoy:
            al.append(alerta("policy_review_overdue", f"{x.get('name')}: su revisión tocaba el {iso(prox)} y no hay una versión posterior", _cita(x.get("source")),
                             dias=(hoy - prox).days, clave=f"politica:{norm(x.get('name'))}"))
        elif not prox:
            no_proc.append({"archivo": _archivo(x.get("source")) or "ficha", "motivo": f"{x.get('name')}: la ficha no trae su fecha de revisión"})
    # 4 · Lo que se conserva contra el plazo de la política.
    meses = {norm(x.get("type")): numero(x.get("months")) for x in plazos if numero(x.get("months")) is not None}
    fuente_plazo = {norm(x.get("type")): x.get("source") for x in plazos}
    conservacion = []
    for x in filas:
        tipo, antiguo = norm(x.get("tipo")), fecha(x.get("antiguo"))
        if not tipo or tipo not in meses or not antiguo:
            continue
        limite = _meses_atras(hoy, meses[tipo])
        conservacion.append({"conjunto": x["conjunto"], "tipo": x.get("tipo"), "meses": meses[tipo], "antiguo": iso(antiguo), "limite": iso(limite)})
        if antiguo < limite:
            al.append(alerta("retention_exceeded", f"{x['conjunto']} · {x.get('nombre') or ''}: conserva registros desde el {iso(antiguo)}, y la política fija "
                             f"{int(meses[tipo])} meses para «{x.get('tipo')}»: todo lo anterior al {iso(limite)} pasó su plazo",
                             [cat.cita(x, docs)] + ([_cita(fuente_plazo[tipo])] if fuente_plazo.get(tipo) else []),
                             responsable=x.get("dueno") or None, dias=(limite - antiguo).days, clave=f"conservacion:{x['conjunto']}"))
    # 5 · Cada término de los informes contra el glosario.
    glosario = {norm(x["termino"]) for x in (glo.filas if glo else [])}
    if terminos and glo is None:
        no_proc.append({"archivo": "00-referencia", "motivo": "no está el glosario de negocio: sin él no se sabe qué término de los informes está definido"})
    vistos = set()
    lista_terminos = []
    for x in terminos:
        t = norm(x.get("term"))
        if not t or t in vistos:
            continue
        vistos.add(t)
        definido = t in glosario
        lista_terminos.append({"termino": x.get("term"), "informe": _archivo(x.get("source")), "definido": definido})
        if glo is not None and not definido:
            al.append(alerta("term_not_in_glossary", f"«{x.get('term')}»: el informe lo usa y el glosario de negocio no lo define", _cita(x.get("source")),
                             clave=f"termino:{t}"))
    # 6 · Cada conjunto con datos personales contra el registro de bases de la organización.
    registrados = {norm(x["conjunto"]) for x in (reg.filas if reg else [])}
    personales = []
    for x in filas:
        if not _si(x.get("personales")):
            continue
        dentro = norm(x["conjunto"]) in registrados
        personales.append({"conjunto": x["conjunto"], "nombre": x.get("nombre"), "registrado": dentro})
        if reg is None:
            continue
        if not dentro:
            al.append(alerta("personal_data_unregistered", f"{x['conjunto']} · {x.get('nombre') or ''}: el catálogo dice que tiene datos personales y no está en el "
                             f"registro de bases de datos personales de la organización", [cat.cita(x, docs), {"archivo": rel(reg.ruta, docs)}],
                             responsable=x.get("dueno") or None, clave=f"personales:{x['conjunto']}"))
    if personales and reg is None:
        no_proc.append({"archivo": "10-catalogo", "motivo": "no está el registro de bases de datos personales de la organización: sin él no se sabe qué base con datos personales falta"})
    partes = {
        "governance-scan": {"conjuntos": len(conjuntos), "politicas": len(politicas), "terminos": len(lista_terminos), "personales": len(personales), "fuentes": ["F-01"]},
        "catalog-check": {"conjuntos": conjuntos, "fuentes": ["F-01"]},
        "retention-check": {"politicas": revisiones, "conservacion": conservacion, "fuentes": ["F-01"]},
        "glossary-check": {"terminos": lista_terminos, "personales": personales, "fuentes": ["F-01"]},
    }
    vence = sorted(({"fecha": r["revision"], "que": f"{r['politica']} · revisión", "caso": r["politica"], "estado": "pendiente", "comando": "retention-check"}
                    for r in revisiones if r["revision"] and 0 <= (fecha(r["revision"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "custodia", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": vence}


# ================================================================ Ariadna · la calidad y el linaje

def _iguales(a: float, b: float, tol_pct: float) -> bool:
    base = max(abs(a), abs(b))
    return base == 0 or abs(a - b) <= base * tol_pct / 100


def ariadna(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    N._PAIS[0] = N.pais_de(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "ariadna", periodo)
    al: list[dict] = []
    no_proc: list[dict] = []
    tol = numero(metodologia(cfg).get("tolerance_pct"))
    tol = 0.0 if tol is None else tol
    lin, fue, reglas, res, crit = (tabla(cfg, q, no_proc) for q in ("linaje", "fuente", "reglas", "resultados", "criticos"))
    cifras = ficha.get("figures") or []
    citadas = {str(x.get("source")) for x in cifras} | {str(s) for s in ficha.get("reviewed") or []}
    problemas = _sin_ficha(docs, "20-informes", citadas, "es un informe con cifras; corre lineage-scan")
    for x in cifras:
        if not (x.get("indicator") and x.get("source")) or numero(x.get("value")) is None:
            problemas.append(f"una cifra de la ficha no trae indicador, valor o cita: {json.dumps(x, ensure_ascii=False)[:160]}")
    pasos = {}
    for x in lin.filas if lin else []:
        pasos.setdefault(norm(x["indicador"]), []).append(x)
    valores = {}
    for x in fue.filas if fue else []:
        v, c = numero(x.get("valor")), fecha(x.get("corte"))
        if v is not None and c:
            valores.setdefault(norm(x["indicador"]), []).append((c, v, x))
    if cifras and lin is None and fue is None:
        no_proc.append({"archivo": "30-calidad", "motivo": "no están el linaje ni las cifras de la fuente: sin ellos no se contrasta ninguna cifra"})
    # 1, 2 y 3 · Cada cifra del informe contra su fuente, su corte y su linaje.
    revisadas = []
    for x in cifras:
        ind, v, corte = norm(x.get("indicator")), numero(x.get("value")), fecha(x.get("cutoff"))
        if not ind or v is None:
            continue
        inf = _informe(x.get("source"))
        nom = f"«{x.get('indicator')}» del informe {_archivo(x.get('source'))}"
        tiene = ind in pasos or ind in valores
        en_corte = next(((c, w, y) for c, w, y in valores.get(ind, []) if c == corte), None)
        otro = next(((c, w, y) for c, w, y in valores.get(ind, []) if c != corte and _iguales(v, w, tol)), None)
        estado = "coincide"
        if not tiene:
            estado = "sin fuente"
            al.append(alerta("figure_without_source", f"{nom}: {v:,.0f} no tiene fuente en el linaje ni en las cifras de la fuente exportadas", _cita(x.get("source")),
                             monto=v, clave=f"fuente:{inf}:{ind}"))
        elif en_corte and _iguales(v, en_corte[1], tol):
            estado = "coincide"
        elif otro:
            estado = "otro corte"
            al.append(alerta("cutoff_mismatch", f"{nom}: el informe declara el corte {iso(corte) or 'sin fecha'}, y su cifra, {v:,.0f}, es la de la fuente al {iso(otro[0])}",
                             [_cita(x.get("source")), fue.cita(otro[2], docs)], monto=v, clave=f"corte:{inf}:{ind}"))
        elif en_corte:
            estado = "distinta"
            dif = v - en_corte[1]
            al.append(alerta("figure_differs_from_source", f"{nom}: el informe trae {v:,.0f} y la fuente {en_corte[1]:,.0f} al mismo corte, {iso(corte)}: "
                             f"una diferencia de {dif:,.0f}, más allá de la tolerancia del {tol:g} %", [_cita(x.get("source")), fue.cita(en_corte[2], docs)],
                             monto=abs(dif), clave=f"cifra:{inf}:{ind}"))
        else:
            estado = "sin cifra al corte"
            no_proc.append({"archivo": _archivo(x.get("source")), "motivo": f"«{x.get('indicator')}»: las cifras de la fuente no traen su valor al corte {iso(corte) or 'sin fecha'}"})
        revisadas.append({"informe": _archivo(x.get("source")), "indicador": x.get("indicator"), "valor": v, "corte": iso(corte),
                          "fuente": en_corte[1] if en_corte else None, "estado": estado})
    # 4 · Cada paso del linaje con su sistema de origen.
    linaje = []
    for ind, ps in sorted(pasos.items()):
        rotos = [p for p in ps if not p.get("sistema")]
        linaje.append({"indicador": ps[0]["indicador"], "pasos": len(ps), "rotos": [p.get("paso") or str(p["_fila"]) for p in rotos]})
        for p in rotos:
            al.append(alerta("lineage_broken", f"«{p['indicador']}»: el paso {p.get('paso') or '(sin número)'} del linaje no tiene su sistema de origen", lin.cita(p, docs),
                             clave=f"linaje:{ind}:{norm(p.get('paso') or p['_fila'])}"))
    # 5, 6 y 7 · Cada regla de calidad contra su umbral y su corrida, y cada dato crítico con su regla.
    criticos = {norm(x["dato"]): x for x in (crit.filas if crit else [])}
    resultado = {}
    for x in res.filas if res else []:
        if not x.get("periodo") or str(x.get("periodo"))[:7] == periodo:
            resultado[norm(x["regla"])] = x
    lista_reglas = []
    for x in reglas.filas if reglas else []:
        rid = x["regla"]
        r = resultado.get(norm(rid))
        valor, umbral = numero(r.get("resultado")) if r else None, numero(x.get("umbral"))
        critico = norm(x.get("dato")) in criticos
        lista_reglas.append({"regla": rid, "dato": x.get("dato"), "critico": critico, "umbral": umbral, "resultado": valor})
        if r is None:
            if critico:
                al.append(alerta("quality_rule_not_run", f"{rid} sobre {x.get('dato')}, un dato crítico: no tiene resultado en el periodo {periodo}", reglas.cita(x, docs),
                                 responsable=criticos[norm(x.get("dato"))].get("dueno") or None, clave=f"corrida:{rid}"))
            continue
        if valor is not None and umbral is not None and valor < umbral:
            al.append(alerta("quality_rule_below_threshold", f"{rid} sobre {x.get('dato')}: dio {valor:g} en el periodo y su umbral es {umbral:g}",
                             [reglas.cita(x, docs), res.cita(r, docs)], clave=f"umbral:{rid}"))
    con_regla = {norm(x.get("dato")) for x in (reglas.filas if reglas else [])}
    sin_regla = []
    for k, x in criticos.items():
        if reglas is not None and k not in con_regla:
            sin_regla.append(x["dato"])
            al.append(alerta("critical_data_without_rule", f"{x['dato']}: está marcado como dato crítico y ninguna regla de calidad lo mide", crit.cita(x, docs),
                             responsable=x.get("dueno") or None, clave=f"critico:{k}"))
    fuentes = ["F-01", "F-03"] + (["F-02"] if any(a["signal"] in ("figure_differs_from_source", "cutoff_mismatch", "figure_without_source") for a in al) else [])
    partes = {
        "lineage-scan": {"cifras": len(revisadas), "indicadores": len(linaje), "reglas": len(lista_reglas), "fuentes": fuentes},
        "figure-check": {"cifras": revisadas, "tolerancia": tol, "fuentes": ["F-01", "F-02"]},
        "lineage-check": {"linaje": linaje, "fuentes": ["F-01"]},
        "rule-check": {"reglas": lista_reglas, "sin_regla": sin_regla, "fuentes": ["F-01", "F-03"]},
    }
    return {"agente": "ariadna", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy), "partes": partes,
            "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas, "preguntas": ficha.get("questions") or [], "vence": []}


# ================================================================ el reporte

SENALES_DE = {
    "catalog-check": {"dataset_without_owner", "dataset_without_classification"},
    "retention-check": {"policy_review_overdue", "retention_exceeded"},
    "glossary-check": {"term_not_in_glossary", "personal_data_unregistered"},
    "figure-check": {"figure_without_source", "figure_differs_from_source", "cutoff_mismatch"},
    "lineage-check": {"lineage_broken"},
    "rule-check": {"quality_rule_below_threshold", "quality_rule_not_run", "critical_data_without_rule"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-cdo")


def _sn(b) -> str:
    return "sí" if b else "no"


def _n(v) -> str:
    return "—" if v is None else f"{v:,.0f}"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "governance-scan":
        l += [f"**Conjuntos en el catálogo:** {p['conjuntos']} · **Con datos personales:** {p['personales']} · **Políticas en la ficha:** {p['politicas']} · "
              f"**Términos de los informes:** {p['terminos']}.", ""]
    elif comando == "catalog-check":
        l += ["| Conjunto | Dueño | Clasificación | Tipo | Datos personales |", "|---|---|---|---|---|"]
        l += [f"| {x['conjunto']} · {x['nombre'] or ''} | {x['dueno'] or '—'} | {x['clasificacion'] or '—'} | {x['tipo'] or '—'} | {_sn(x['personales'])} |" for x in p["conjuntos"]]
        l += ["", "El dueño y la clasificación los asigna el área: aquí se dice cuál falta.", ""]
    elif comando == "retention-check":
        l += ["| Política | Aprobada | Revisión | Documento |", "|---|---|---|---|"]
        l += [f"| {x['politica']} | {x['aprobada'] or '—'} | {x['revision'] or '—'} | `{x['fuente']}` |" for x in p["politicas"]]
        if p["conservacion"]:
            l += ["", "| Conjunto | Tipo | Plazo | Registro más antiguo | Lo que vence antes del |", "|---|---|---|---|---|"]
            l += [f"| {x['conjunto']} | {x['tipo']} | {int(x['meses'])} meses | {x['antiguo']} | {x['limite']} |" for x in p["conservacion"]]
        l += ["", "Qué se borra o se archiva lo decide el dueño del dato con la política: aquí se dice qué pasó su plazo.", ""]
    elif comando == "glossary-check":
        if p["terminos"]:
            l += ["| Término | Informe | En el glosario |", "|---|---|---|"] + [f"| {x['termino']} | `{x['informe']}` | {_sn(x['definido'])} |" for x in p["terminos"]]
            l.append("")
        if p["personales"]:
            l += ["| Conjunto con datos personales | En el registro de bases |", "|---|---|"] + [f"| {x['conjunto']} · {x['nombre'] or ''} | {_sn(x['registrado'])} |" for x in p["personales"]]
            l.append("")
        l += ["Lo que exige la ley de cada país sobre el registro de bases de datos personales lo confirma el área: aquí se compara el catálogo con el registro de la organización.", ""]
    elif comando == "lineage-scan":
        l += [f"**Cifras de los informes en la ficha:** {p['cifras']} · **Indicadores con linaje:** {p['indicadores']} · **Reglas de calidad:** {p['reglas']}.", ""]
    elif comando == "figure-check":
        l += [f"**Tolerancia de la política de datos:** {p['tolerancia']:g} %.", "", "| Informe | Indicador | Corte | En el informe | En la fuente | Estado |", "|---|---|---|---|---|---|"]
        l += [f"| `{x['informe']}` | {x['indicador']} | {x['corte'] or '—'} | {_n(x['valor'])} | {_n(x['fuente'])} | {x['estado']} |" for x in p["cifras"]]
        l += ["", "Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.", ""]
    elif comando == "lineage-check":
        l += ["| Indicador | Pasos | Pasos sin sistema de origen |", "|---|---|---|"]
        l += [f"| {x['indicador']} | {x['pasos']} | {', '.join(x['rotos']) or '—'} |" for x in p["linaje"]]
        l.append("")
    elif comando == "rule-check":
        l += ["| Regla | Dato | Crítico | Umbral | Resultado del periodo |", "|---|---|---|---|---|"]
        g = lambda v, vacio: vacio if v is None else format(v, "g")  # noqa: E731
        l += [f"| {x['regla']} | {x['dato'] or '—'} | {_sn(x['critico'])} | {g(x['umbral'], '—')} | {g(x['resultado'], 'sin corrida')} |" for x in p["reglas"]]
        if p["sin_regla"]:
            l += ["", "**Datos críticos sin regla:** " + ", ".join(p["sin_regla"]) + "."]
        l += ["", "Los umbrales los fija la política de datos de la organización.", ""]
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
    scan = {"custodia": "governance-scan", "ariadna": "lineage-scan"}[rol]
    carpetas = {"custodia": ("10-catalogo", "20-informes"), "ariadna": ("20-informes", "30-calidad")}[rol]
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


AGENTE = {"custodia": custodia, "ariadna": ariadna}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-data-quality": "ariadna"}.get(N.plugin(AQUI)["name"], "custodia")


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
    ap = N.argumentos("El motor de Custodia y Ariadna.")
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
    ok("la tolerancia: dentro y fuera", [_iguales(1000, 1004, 0.5), _iguales(1000, 1010, 0.5), _iguales(0, 0, 0)], [True, False, True])
    ok("los meses hacia atrás", [iso(_meses_atras(hoy, 60)), iso(_meses_atras(dt.date(2026, 1, 31), 1))], ["2021-11-25", "2025-12-28"])
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "datos" / "e1", t / "estado" / "e1"
        _x(docs / "10-catalogo" / "catalogo_datos.xlsx", [
            ["Conjunto", "Nombre", "Dueño", "Clasificación", "Tipo", "Datos personales", "Dato más antiguo", "Sistema"],
            ["DS-01", "Clientes", "Gerencia comercial", "Confidencial", "Clientes", "Sí", "2015-03-01", "CRM"],
            ["DS-02", "Cartera", "", "Restringida", "Transaccional", "No", "2019-01-01", "Core"],
            ["DS-03", "Proveedores", "Compras", "", "Proveedores", "Sí", "2024-01-01", "ERP"],
            ["DS-04", "Empleados", "Gestión humana", "Confidencial", "Empleados", "Sí", "2023-01-01", "Nómina"]])
        _x(docs / "10-catalogo" / "registro_de_bases_personales.xlsx", [["Conjunto", "Número de registro", "Fecha de registro"],
                                                                         ["DS-01", "RNBD-1", "2020-05-01"], ["DS-04", "RNBD-2", "2023-02-01"]])
        _x(docs / "00-referencia" / "glosario.xlsx", [["Término", "Definición", "Dueño"], ["Cartera vencida", "Saldo con más de 30 días de mora", "Riesgo"]])
        for f in ("00-referencia/politica_de_datos.pdf", "00-referencia/politica_de_conservacion.pdf", "20-informes/informe_junta_2026-10.pdf"):
            (docs / f).parent.mkdir(parents=True, exist_ok=True)
            (docs / f).write_text("doc", encoding="utf-8")
        escribir_json(est / "gobierno" / "2026-11" / "ficha.json", {
            "policies": [{"name": "Política de datos", "approved": "2023-06-01", "next_review": "2025-06-01", "source": "00-referencia/politica_de_datos.pdf"},
                         {"name": "Política de conservación", "approved": "2025-08-01", "next_review": "2027-08-01", "source": "00-referencia/politica_de_conservacion.pdf"}],
            "retention": [{"type": "Clientes", "months": 120, "source": "00-referencia/politica_de_conservacion.pdf"},
                          {"type": "Transaccional", "months": 120, "source": "00-referencia/politica_de_conservacion.pdf"}],
            "report_terms": [{"term": "Cartera vencida", "source": "20-informes/informe_junta_2026-10.pdf"},
                             {"term": "Margen financiero", "source": "20-informes/informe_junta_2026-10.pdf"}]})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-11", "_docs": docs, "_estado": est,
               "methodology": {"tolerance_pct": 0.5}}
        ok("la configuración de Custodia pasa", revisar_config(cfg, "custodia"), [])
        r = custodia(cfg, "2026-11", hoy)
        ok("Custodia: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("dataset_without_classification", "clasificacion:DS-03"), ("dataset_without_owner", "dueno:DS-02"),
            ("personal_data_unregistered", "personales:DS-03"), ("policy_review_overdue", "politica:politica_de_datos"),
            ("retention_exceeded", "conservacion:DS-01"), ("term_not_in_glossary", "termino:margen_financiero")])
        ok("Custodia: la ficha cita sus documentos", r["record_issues"], [])

        _x(docs / "30-calidad" / "linaje.xlsx", [["Indicador", "Paso", "Sistema de origen", "Conjunto"],
                                                 ["Cartera vencida", "1", "Core", "DS-02"], ["Cartera vencida", "2", "Bodega", "DM-01"],
                                                 ["Clientes activos", "1", "CRM", "DS-01"], ["Clientes activos", "2", "", "DM-02"],
                                                 ["Margen financiero", "1", "ERP", "DS-09"]])
        _x(docs / "30-calidad" / "cifras_fuente.xlsx", [["Indicador", "Corte", "Valor"],
                                                        ["Cartera vencida", "2026-10-31", "1250000000"], ["Cartera vencida", "2026-09-30", "1180000000"],
                                                        ["Clientes activos", "2026-10-31", "84200"], ["Margen financiero", "2026-10-31", "3400000000"],
                                                        ["Margen financiero", "2026-09-30", "3150000000"]])
        _x(docs / "30-calidad" / "reglas_calidad.xlsx", [["Regla", "Dato", "Umbral"], ["RQ-01", "Cliente.documento", "99"], ["RQ-02", "Crédito.saldo", "98"],
                                                        ["RQ-03", "Crédito.fecha_desembolso", "97"]])
        _x(docs / "30-calidad" / "resultados_calidad.xlsx", [["Regla", "Periodo", "Resultado"], ["RQ-01", "2026-11", "99.6"], ["RQ-02", "2026-11", "96.1"]])
        _x(docs / "30-calidad" / "datos_criticos.xlsx", [["Dato", "Dueño"], ["Cliente.documento", "Comercial"], ["Crédito.fecha_desembolso", "Crédito"],
                                                        ["Crédito.calificación", "Riesgo"]])
        escribir_json(est / "calidad" / "2026-11" / "ficha.json", {"figures": [
            {"indicator": "Cartera vencida", "value": 1180000000, "cutoff": "2026-10-31", "source": "20-informes/informe_junta_2026-10.pdf, p. 2"},
            {"indicator": "Clientes activos", "value": 84200, "cutoff": "2026-10-31", "source": "20-informes/informe_junta_2026-10.pdf, p. 3"},
            {"indicator": "Margen financiero", "value": 3520000000, "cutoff": "2026-10-31", "source": "20-informes/informe_junta_2026-10.pdf, p. 3"},
            {"indicator": "Índice de solvencia", "value": 14, "cutoff": "2026-10-31", "source": "20-informes/informe_junta_2026-10.pdf, p. 4"}]})
        ok("la configuración de Ariadna pasa", revisar_config(cfg, "ariadna"), [])
        r = ariadna(cfg, "2026-11", hoy)
        ok("Ariadna: las señales donde se sembraron, y ninguna de más", sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("critical_data_without_rule", "critico:credito_calificacion"), ("cutoff_mismatch", "corte:informe_junta_2026_10:cartera_vencida"),
            ("figure_differs_from_source", "cifra:informe_junta_2026_10:margen_financiero"),
            ("figure_without_source", "fuente:informe_junta_2026_10:indice_de_solvencia"), ("lineage_broken", "linaje:clientes_activos:2"),
            ("quality_rule_below_threshold", "umbral:RQ-02"), ("quality_rule_not_run", "corrida:RQ-03")])
        ok("Ariadna: la ficha cita sus documentos", r["record_issues"], [])
        md = reporte(r, "figure-check", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        sin_tol = dict(cfg, methodology={})
        ok("la configuración de Ariadna pide la tolerancia", any("tolerance_pct" in x for x in revisar_config(sin_tol, "ariadna")), True)
    print(f"\n{'Todo bien' if not fallas else str(len(fallas)) + ' fallas'}.")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
