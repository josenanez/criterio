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

Por qué este script existe aparte de `portafolio.py`: la espina de la ficha de un proyecto es
`plan` + `baseline` + `money`, y en definición de producto **ninguno de los tres
existe**. Un requerimiento no tiene línea base ni presupuesto: tiene evidencia de
demanda, criterios de aceptación, y un proyecto que lo ejecuta o no lo ejecuta.

Lo que sí comparte es el contrato de dato: **todo campo es un valor o
`{value, source, source_date, state}`**, y eso se importa de `portafolio.py`, que es la copia
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
from portafolio import (as_date, as_number, _cada, pct, proximo_comite,  # noqa: E402
                 source_of, state_of, value, plan, sellar, load_execution)

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
    # No sale de `compute`: sale de cruzar este producto contra los que otros
    # publicaron. Vive en la misma lista porque es una señal como las demás, y
    # `product-health` tiene que explicarla igual.
    "product_overlap",
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


def _normalizar(texto) -> str:
    """Para comparar segmentos escritos por dos personas distintas. No resuelve
    sinónimos y no lo pretende: quita mayúsculas, tildes y puntuación, y ahí se detiene.
    Lo que dos redacciones distintas del mismo segmento significan lo decide el modelo."""
    import unicodedata
    crudo = unicodedata.normalize("NFKD", str(texto or "").lower())
    limpio = "".join(c for c in crudo if not unicodedata.combining(c))
    return " ".join("".join(c if c.isalnum() else " " for c in limpio).split())


def ficha_producto(state: Path, today: dt.date, th: dict) -> dict:
    """Lo que un producto publica para que los demás lo lean.

    Es la misma mecánica con la que el gerente de proyecto publica su ficha: **no hay
    almacenamiento compartido y no hay consistencia distribuida.** Cada producto deja un
    documento, y los demás lo leen como leen cualquier otro.

    Lleva lo mínimo para poder cruzar y nada más: quién lo publica, a quién dice servir,
    qué métricas afirma, y qué proyectos ejecutan sus requerimientos. Lo demás —las
    entrevistas, los supuestos, el registro completo— es del producto y no se publica.
    """
    datos = compute(state, today, th)
    return {
        "code": datos["product"]["code"],
        "name": datos["product"]["name"],
        "manager": datos["product"]["manager"],
        "as_of": datos["as_of"],
        "who": datos["definition"]["who"],
        "claims": [{"metric": c["metric"], "declared": c["declared"],
                    "source": c["source"], "source_date": c["source_date"]}
                   for c in datos["definition"]["claims"]],
        "projects": sorted({r["project"] for r in datos["requirements"] if r.get("project")}),
        "requirements": [{"id": r["id"], "title": r["title"], "state": r["state"],
                          "project": r.get("project")} for r in datos["requirements"]],
    }


def solapamiento(state: Path, otros: Path | None, today: dt.date, th: dict) -> dict:
    """Dónde este producto y otro se pisan.

    Canibalización es una palabra grande para tres preguntas que se pueden responder con
    aritmética sobre lo que cada producto publicó:

    - **¿Dos productos afirman la misma métrica?** Entonces los dos casos de negocio
      están contando las mismas transacciones, y la suma que vio el comité no existe.
      Es el hallazgo más caro de los tres y el que nadie busca.
    - **¿El mismo proyecto ejecuta requerimientos de dos productos?** Entonces uno de los
      dos registros está mirando mal, o el proyecto está construyendo para dos dueños.
    - **¿Dos productos dicen servir al mismo segmento?** No es un defecto por sí solo
      —una organización puede tener dos productos para el mismo cliente a propósito—,
      pero es la pregunta que alguien tiene que haber respondido.

    Lo que **no** se calcula, porque no es aritmética: si dos requerimientos escritos con
    palabras distintas son el mismo. Eso lo lee el modelo, con las dos listas a la vista.
    """
    mio = ficha_producto(state, today, th)
    vecinos = []
    if otros and otros.is_dir():
        for f in sorted(otros.glob("*.json")):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if d.get("code") and d["code"] != mio["code"]:
                d["_file"] = f.name
                vecinos.append(d)

    metricas, proyectos, segmentos, alertas = [], [], [], []
    mis_metricas = {c["metric"]: c for c in mio["claims"] if c.get("metric")}
    mis_proyectos = set(mio["projects"])
    mi_segmento = _normalizar(mio["who"])

    for otro in vecinos:
        for c in otro.get("claims") or []:
            nombre = c.get("metric")
            if nombre and nombre in mis_metricas:
                fila = {"metric": nombre, "with": otro["code"],
                        "mine": mis_metricas[nombre]["declared"],
                        "mine_source": mis_metricas[nombre]["source"],
                        "theirs": c.get("declared"), "theirs_source": c.get("source"),
                        "file": otro["_file"]}
                metricas.append(fila)
                alertas.append({"signal": "product_overlap", "id": nombre,
                                "detail": {**fila, "kind": "metric"}})

        suyos = set(otro.get("projects") or [])
        for p in sorted(mis_proyectos & suyos):
            mios = [r["id"] for r in mio["requirements"] if r.get("project") == p]
            de_el = [r["id"] for r in otro.get("requirements") or []
                     if r.get("project") == p]
            fila = {"project": p, "with": otro["code"], "mine": mios, "theirs": de_el,
                    "file": otro["_file"]}
            proyectos.append(fila)
            alertas.append({"signal": "product_overlap", "id": p,
                            "detail": {**fila, "kind": "project"}})

        if mi_segmento and _normalizar(otro.get("who")) == mi_segmento:
            fila = {"who": mio["who"], "with": otro["code"], "file": otro["_file"]}
            segmentos.append(fila)
            alertas.append({"signal": "product_overlap", "id": otro["code"],
                            "detail": {**fila, "kind": "segment"}})

    return {
        "as_of": today.isoformat(),
        "product": mio["code"],
        "read": [o["code"] for o in vecinos],
        "shared_metrics": metricas,
        "shared_projects": proyectos,
        "same_segment": segmentos,
        "alerts": alertas,
        "totals": {"others": len(vecinos), "metrics": len(metricas),
                   "projects": len(proyectos), "segments": len(segmentos)},
        "note": ("Si dos requerimientos escritos con palabras distintas son el mismo no "
                 "se calcula aquí: eso se lee, con las dos listas a la vista."
                 if vecinos else
                 "No hay ningún otro producto publicado a la vista. Sin eso, "
                 "canibalización no es una pregunta que se pueda responder."),
    }


# ------------------------------------------------------------- la cadencia

# Las tres señales que aparecen **sin que nadie haga nada**: el calendario se mueve y el
# hallazgo nace solo. Es lo propio de un registro de producto, y la razón por la que este
# agente tiene que despertarse en vez de esperar a que lo llamen — nadie va a abrir una
# sesión para preguntar si un supuesto de marzo ya lleva demasiado tiempo sin verificarse.
SENALES_DE_TIEMPO = ("requirement_undecided", "assumption_unverified", "evidence_stale")


# Lo único que `due` lee de la constancia. Ver la nota equivalente en portafolio.py:
# un valor fuera de esta lista se guardaba igual, no lo leía nadie, y el agente creía
# haber dejado constancia mientras `due` seguía diciendo que tocaba.
CONSTANCIAS = ("review", "report", "crossed")


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


def due(config: Path, state: Path, today: dt.date, th: dict | None = None) -> dict:
    """Qué toca hoy, según la cadencia que la persona declaró.

    Esto es lo que convierte esto en un agente y no en un comando: no espera a que lo
    llamen. La decisión de si hoy toca algo es aritmética de fechas, así que vive aquí y
    no en el criterio del modelo.

    La cadencia de un producto no es la de un proyecto. No hay reunión semanal contra la
    que medir: hay una revisión del registro, un comité de producto cuando lo haya, y
    **lo que cruzó un umbral desde la corrida anterior**, que es lo único que aparece sin
    que nadie haga nada.
    """
    cfg = json.loads(config.read_text(encoding="utf-8")) if config and config.exists() else {}
    ciclo = cfg.get("cycle", {}) or {}
    th = th or load_thresholds(config)

    registro_f = state / "cadencia.json"
    registro = json.loads(registro_f.read_text(encoding="utf-8")) if registro_f.exists() else {}
    toca, detalle = [], {}

    def ultima(clave):
        return as_date(registro.get(clave))

    # 1 · la revisión del registro contra la carpeta
    dias_rev = _cada(ciclo.get("review"))
    if dias_rev:
        u = ultima("review")
        detalle["review"] = {"every_days": dias_rev, "last": registro.get("review")}
        if u is None or (today - u).days >= dias_rev:
            toca.append("review")

    # 2 · el comité de producto, con su anticipación. La aritmética es la misma que la
    # del comité de proyectos, así que se importa en vez de reescribirse.
    fecha, paso = proximo_comite(ciclo, today)
    anticipacion = int(ciclo.get("report_lead_days") or 0)
    if fecha:
        entrega = fecha - dt.timedelta(days=anticipacion)
        detalle["committee"] = {"next": fecha.isoformat(),
                                "days_away": (fecha - today).days,
                                "report_on": entrega.isoformat(),
                                "every_days": paso or None}
        u = ultima("report")
        if today >= entrega and (u is None or u < entrega):
            toca.append("report")

    # 3 · lo que cruzó un umbral desde la corrida anterior. No es cadencia: es lo que el
    # paso del tiempo produjo solo. Se compara contra el último corte guardado, y si no
    # hay corte anterior no se reporta nada — la primera corrida no «descubre» cosas que
    # llevaban ahí desde siempre, las revisa.
    carpeta = state / "snapshots"
    previos = sorted(carpeta.glob("*.json")) if carpeta.is_dir() else []
    if previos:
        antes = json.loads(previos[-1].read_text(encoding="utf-8"))
        vistas = {(a["signal"], a.get("id")) for a in antes.get("alerts", [])}
        ahora = compute(state, today, th)
        nuevas = [a for a in ahora["alerts"]
                  if a["signal"] in SENALES_DE_TIEMPO and (a["signal"], a.get("id")) not in vistas]
        if nuevas:
            detalle["crossed"] = {"since": previos[-1].stem, "count": len(nuevas),
                                  "signals": sorted({a["signal"] for a in nuevas})}
            toca.append("crossed")

    proximos = []
    if dias_rev:
        u = ultima("review")
        proximos.append((u or today) + dt.timedelta(days=dias_rev))
    if fecha:
        proximos.append(fecha - dt.timedelta(days=anticipacion))
    futuros = [p for p in proximos if p > today]

    return {"today": today.isoformat(), "due": toca, "quiet": not toca,
            "detail": detalle,
            "next_wake": min(futuros).isoformat() if futuros else None}


# ----------------------------------------------------------- estado en disco

def corrida_inicio(state: Path) -> dict:
    """Marca el arranque, para que el tiempo lo mida la corrida y no lo estime nadie."""
    import time
    (state / "corrida-en-curso.json").write_text(
        json.dumps({"desde": time.time()}), encoding="utf-8")
    return {"marcado": True}


def corrida(state: Path, que: str, today: dt.date, th: dict, fichas: Path = None,
            nota=None, salida: Path = None, caso: str = None) -> dict:
    """El registro de una corrida sobre este producto: qué se corrió y qué encontró.

    Es lo mismo que `portafolio.py corrida` hace para Vera, y por la misma razón: sin
    registro, lo que el agente produjo queda en una carpeta que hay que recordar, la
    corrida del mes siguiente no tiene contra qué compararse, y cualquier estadística de
    prueba tendría que teclearla una persona — que es medir su transcripción y no la
    corrida.
    """
    import time
    from collections import Counter

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

    r = compute(state, today, th, fichas)
    # `compute` ya publica el conteo por señal. Volver a contarlo a mano sería el mismo
    # error que este repositorio le encontró a un informe que reescribió una cifra.
    senales = Counter(r.get("by_signal") or {})
    if not senales:
        senales = Counter(a["signal"] for a in r.get("alerts") or [])
        for req in r.get("requirements") or []:
            senales.update(a["signal"] for a in req.get("alerts") or [])

    # Por requerimiento y no solo el total del producto: es el equivalente de `por_caso`
    # en el portafolio, y sin él no se puede saber después desde cuándo un requerimiento
    # viene sin doliente, sin criterio o sin nadie que lo esté construyendo.
    por_caso = {}
    for req in r.get("requirements") or []:
        rid = (req.get("id") or {})
        rid = rid.get("value") if isinstance(rid, dict) else rid
        por_caso[rid or "?"] = sorted(a["signal"] for a in req.get("alerts") or [])
    del_producto = sorted(a["signal"] for a in r.get("alerts") or [])
    if del_producto:
        por_caso[(r.get("product") or {}).get("code") or "producto"] = del_producto

    entrada = {"que": que, "fecha": today.isoformat(),
               "producto": (r.get("product") or {}).get("code"),
               "por_caso": por_caso,
               "requerimientos": len(r.get("requirements") or []),
               "segundos": segundos, "hallazgos": sum(senales.values()),
               "por_senal": dict(senales.most_common()),
               "medido": {"segundos": segundos is not None}, "nota": nota}

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
    # Cuándo se escribió, en segundos de reloj: es lo que permite que el rastro que
    # deja el arnés encuentre estas cifras y las incruste en la página de su corrida.
    entrada["escrita"] = time.time()
    if caso:
        entrada["caso"] = caso
    previas.append(entrada)
    f.write_text(json.dumps(previas, ensure_ascii=False, indent=2) + "\n",
                 encoding="utf-8")

    d = state / "corridas"
    d.mkdir(parents=True, exist_ok=True)
    lineas = [f"# Corrida del {today.isoformat()} · {que}", "",
              f"{entrada['producto'] or 'producto sin código'} · "
              f"{entrada['requerimientos']} requerimientos"
              + (f" · {segundos} s" if segundos else "")
              + f" · {entrada['hallazgos']} hallazgos", ""]
    if senales:
        lineas += ["| Señal | Hallazgos |", "|---|---:|"]
        lineas += [f"| `{s}` | {n} |" for s, n in senales.most_common()]
        lineas.append("")
    if segundos is None:
        lineas += ["> El tiempo no se midió: faltó `corrida-inicio` al arrancar.", ""]
    if nota:
        lineas += [nota, ""]
    anterior = previas[-2] if len(previas) > 1 else None
    lineas += ([f"Contra la corrida del {anterior['fecha']}: "
                f"{entrada['hallazgos'] - (anterior.get('hallazgos') or 0):+d} hallazgos.",
                ""] if anterior
               else ["Primera corrida: no hay una anterior contra la cual comparar.", ""])
    if texto_salida:
        lineas += ["## Lo que produjo", "", texto_salida, ""]
    else:
        lineas += ["## Lo que produjo", "",
                   "> El comando no entregó su resultado (`--salida`): la corrida registra "
                   "las cifras, pero lo que dijo se quedó en la conversación.", ""]
    (d / f"{entrada['id']}.md").write_text("\n".join(lineas), encoding="utf-8")
    import portafolio as _pf  # la página de la corrida es una sola para los tres agentes
    return entrada


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
    faltan = [c for c in ("product", "paths", "terms_accepted", "cycle") if c not in cfg]
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
                                   "cycle": {"review": "monthly", "committee": "monthly",
                                             "committee_next": "2026-12-03",
                                             "report_lead_days": 2},
                                   "thresholds": {"undecided_days": 30}}), encoding="utf-8")
        res = check_config(cfg)
        ok(res["ok"] and res["thresholds"]["undecided_days"] == 30,
           "y un umbral de la organización pisa el de por defecto")

        print("\nLa cadencia")
        d3 = due(cfg, estado, hoy)
        ok("review" in d3["due"], "sin constancia de ninguna revisión, toca revisar")
        ran(estado, "review", hoy)
        d3 = due(cfg, estado, hoy)
        ok("review" not in d3["due"], "y después de dejar constancia, ya no")
        ok(due(cfg, estado, dt.date(2026, 12, 21))["due"].count("review") == 1,
           "un mes después vuelve a tocar")
        ok(due(cfg, estado, dt.date(2026, 12, 1))["due"].count("report") == 1,
           "el informe de comité aterriza con su anticipación, no el día del comité")
        ok(due(cfg, estado, hoy)["next_wake"] is not None,
           "y si hoy no toca nada, dice cuándo vuelve")

        print("\nLo que cruzó un umbral desde la corrida anterior")
        # El corte ya guardado arriba tiene el estado de siempre. Un requerimiento nuevo
        # que nace ya vencido es exactamente el caso: nadie hizo nada y el hallazgo está.
        vacio = Path(tmp) / "limpio"
        init(vacio)
        (vacio / "producto.json").write_text(json.dumps(prod, ensure_ascii=False),
                                             encoding="utf-8")
        ok("crossed" not in due(cfg, vacio, hoy)["due"],
           "sin corte anterior, la primera corrida no «descubre» nada: revisa")
        snapshot(vacio, hoy)
        (vacio / "requirements" / "REQ-900.json").write_text(json.dumps(
            {**base, "id": "REQ-900", "state": "propuesto", "stated_on": "2026-01-05"},
            ensure_ascii=False), encoding="utf-8")
        d4 = due(cfg, vacio, hoy)
        ok("crossed" in d4["due"], "con corte anterior, lo que cruzó desde entonces sí")
        ok(d4["detail"]["crossed"]["signals"] == ["requirement_undecided"],
           "y dice qué señal fue")

    print("\nDónde dos productos se pisan")
    with tempfile.TemporaryDirectory() as tmp2:
        uno = Path(tmp2) / "uno"
        otros = Path(tmp2) / "publicados"
        init(uno)
        otros.mkdir()
        # el segmento escrito como lo escribiría una persona, para poder probar que dos
        # redacciones con distintas mayúsculas y tildes se reconocen como el mismo
        mio = {**prod, "definition": {**prod["definition"],
                                      "who": "comercios con recaudo QR y sin punto de venta integrado"}}
        (uno / "producto.json").write_text(json.dumps(mio, ensure_ascii=False),
                                           encoding="utf-8")
        base2 = {"state": "aceptado", "acceptance": [{"value": "x"}],
                 "evidence": [{"value": "e", "source_date": "2026-09-01"}],
                 "owner": {"value": "Marcela Ruiz", "kind": "person"},
                 "decision": {"what": {"value": "se hace", "source": "comite.md"}}}
        (uno / "requirements" / "REQ-010.json").write_text(json.dumps(
            {**base2, "id": "REQ-010", "traces": {"project": "PRY-101"}},
            ensure_ascii=False), encoding="utf-8")

        publicada = ficha_producto(uno, hoy, th)
        ok(publicada["code"] == "PRD-QR" and publicada["projects"] == ["PRY-101"],
           "lo que un producto publica lleva sus proyectos")
        ok("assumptions" not in publicada and "evidence" not in str(publicada.get("who")),
           "y no lleva el registro completo: lo que no hace falta para cruzar no se publica")

        vacio = solapamiento(uno, otros, hoy, th)
        ok(vacio["alerts"] == [] and vacio["totals"]["others"] == 0,
           "sin otro producto publicado, canibalización no es una pregunta")

        # el vecino: misma métrica, mismo proyecto y mismo segmento, escrito distinto
        (otros / "PRD-COBROS.json").write_text(json.dumps({
            "code": "PRD-COBROS", "name": "Cobros recurrentes", "manager": "Julián",
            "who": "Comercios con recaudo QR y SIN punto de venta integrado",
            "claims": [{"metric": "tx_mensuales", "declared": 90000,
                        "source": "caso-cobros.md", "source_date": "2026-05-02"}],
            "projects": ["PRY-101"],
            "requirements": [{"id": "REQ-501", "title": "Cobro recurrente",
                              "state": "aceptado", "project": "PRY-101"}],
        }, ensure_ascii=False), encoding="utf-8")
        # y un tercero que no se pisa con nada: el control negativo del cruce
        (otros / "PRD-TESORERIA.json").write_text(json.dumps({
            "code": "PRD-TESORERIA", "name": "Tesorería", "manager": "Ana",
            "who": "Empresas grandes con mesa de dinero",
            "claims": [{"metric": "saldos_medios", "declared": 10,
                        "source": "caso-tes.md", "source_date": "2026-05-02"}],
            "projects": ["PRY-900"], "requirements": [],
        }, ensure_ascii=False), encoding="utf-8")

        s = solapamiento(uno, otros, hoy, th)
        clases = sorted({a["detail"]["kind"] for a in s["alerts"]})
        ok(s["totals"]["others"] == 2, "lee todo lo publicado menos lo propio")
        ok(clases == ["metric", "project", "segment"], "y encuentra las tres formas de pisarse")
        m = next(x for x in s["shared_metrics"] if x["metric"] == "tx_mensuales")
        ok((m["mine"], m["theirs"]) == (250000, 90000),
           "la métrica compartida trae las dos cifras: la suma que vio el comité no existe")
        ok(m["mine_source"] and m["theirs_source"],
           "y las dos fuentes, que es lo que permite ir a ver")
        pr = s["shared_projects"][0]
        ok(pr["project"] == "PRY-101" and pr["mine"] == ["REQ-010"]
           and pr["theirs"] == ["REQ-501"],
           "el proyecto compartido dice qué requerimiento pone cada uno")
        ok(len(s["same_segment"]) == 1,
           "el mismo segmento escrito con otras mayúsculas y otras tildes es el mismo")
        ok(all(a["detail"]["with"] != "PRD-TESORERIA" for a in s["alerts"]),
           "y el producto que no se pisa con nada no produce ni una señal")

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
    ap.add_argument("action", choices=["init", "config", "due", "ran", "corrida",
                                       "corrida-inicio", "plan-lectura", "sellar", "compute",
                                       "snapshot", "diff", "publish", "overlap", "selftest"])
    ap.add_argument("--docs", type=Path, default=None,
                    help="carpeta de documentación del producto, para plan-lectura y sellar")
    ap.add_argument("--state", type=Path)
    ap.add_argument("--salida", type=Path, default=None,
                    help="archivo con el resultado completo del comando, para `corrida`")
    ap.add_argument("--caso", default=None,
                    help="código del producto sobre el que corrió, para `corrida`")
    ap.add_argument("--nota", default=None,
                    help="qué hay que mirar de esta corrida, para `corrida`")
    ap.add_argument("--config", type=Path, default=None)
    ap.add_argument("--otros", type=Path, default=None,
                    help="carpeta con las fichas de producto que otros publicaron")
    ap.add_argument("--fichas", type=Path, default=None,
                    help="carpeta con las fichas de los proyectos, para confirmar las trazas")
    ap.add_argument("--against", type=Path, default=None)
    ap.add_argument("--what", default=None,
                    help="qué se corrió: review | report | crossed, para `ran`")
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
    if args.action == "publish":
        print(json.dumps(ficha_producto(args.state, today, load_thresholds(args.config)),
                         ensure_ascii=False, indent=2))
    elif args.action == "overlap":
        print(json.dumps(solapamiento(args.state, args.otros, today,
                                      load_thresholds(args.config)),
                         ensure_ascii=False, indent=2))
    elif args.action == "due":
        print(json.dumps(due(args.config, args.state, today), ensure_ascii=False, indent=2))
    elif args.action == "ran":
        if not args.what:
            ap.error("--what es obligatorio para ran")
        print(json.dumps(ran(args.state, args.what, today), ensure_ascii=False, indent=2))
    elif args.action == "compute":
        print(json.dumps(compute(args.state, today, load_thresholds(args.config), args.fichas),
                         ensure_ascii=False, indent=2))
    elif args.action == "plan-lectura":
        if not args.docs:
            ap.error("--docs es obligatorio para plan-lectura")
        print(json.dumps(plan(args.docs, args.state, load_execution(args.config)),
                         ensure_ascii=False, indent=2))
    elif args.action == "sellar":
        if not args.docs:
            ap.error("--docs es obligatorio para sellar")
        print(json.dumps(sellar(args.docs, args.state, "producto"), ensure_ascii=False))
    elif args.action == "corrida-inicio":
        print(json.dumps(corrida_inicio(args.state), ensure_ascii=False))
    elif args.action == "corrida":
        if not args.what:
            ap.error("--what es obligatorio para corrida: review | report | crossed")
        print(json.dumps(corrida(args.state, args.what, today,
                                 load_thresholds(args.config), args.fichas, args.nota,
                                 args.salida, args.caso),
                         ensure_ascii=False, indent=2))
    elif args.action == "snapshot":
        print(json.dumps({"written": str(snapshot(args.state, today))}, ensure_ascii=False))
    elif args.action == "diff":
        print(json.dumps(diff(args.state, args.against), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
