# -*- coding: utf-8 -*-
"""Extractor de referencia: de los documentos a las fichas, sin modelo.

    python3 tests/sintetico/extractor.py <carpeta de la organización>

**Qué es y qué no es.** El agente extrae con un modelo, que lee documentos de formas
que nadie previó. Esto no hace eso: recorre documentos cuya estructura se conoce y los
convierte en fichas de forma determinística. No prueba la extracción del modelo, y no
pretende hacerlo.

Lo que sí contesta, y es la pregunta que va antes: **¿los documentos contienen lo que la
ficha necesita, y la aritmética encuentra sobre ellos lo que se plantó?** Sin esto, para
probar el cálculo a escala habría que escribir dieciocho fichas a mano cada vez que el
material cambie.

Es también la vara contra la que se puede medir después la extracción del modelo: la
misma carpeta, las dos fichas, campo por campo.
"""
import csv
import datetime as dt
import io
import json
import re
import shutil
import sys
from pathlib import Path

HOY = dt.date.today()


# ── utilidades de lectura ────────────────────────────────────────────────

def campo(valor, fuente, fecha):
    return {"value": valor, "source": fuente, "source_date": fecha, "state": "found"}


def vacio():
    return {"value": None, "state": "not_found"}


def negrita(texto: str, etiqueta: str):
    """`**Etiqueta:** valor` → valor."""
    m = re.search(rf"\*\*{re.escape(etiqueta)}:\*\*\s*(.+)", texto)
    return m.group(1).strip() if m else None


def fecha_de(nombre: str):
    return nombre[:10] if nombre[:4].isdigit() else None


def plata(s: str):
    return int(re.sub(r"[^\d]", "", s)) if s and re.search(r"\d", s) else None


def seccion(texto: str, titulo: str) -> str:
    """El cuerpo de `## titulo`, hasta el siguiente encabezado del mismo nivel."""
    m = re.search(rf"^## {re.escape(titulo)}\s*$(.*?)(?=^## |\Z)", texto,
                  re.M | re.S)
    return m.group(1).strip() if m else ""


def vinetas(bloque: str):
    return [l[2:].strip() for l in bloque.splitlines() if l.startswith("- ")]


def filas(texto: str, cabecera: str):
    """Las filas de la tabla markdown cuya cabecera contiene `cabecera`.

    La cabecera se reconoce **una sola vez**. Una fila de datos puede repetir la
    palabra de la columna —«| REQ-1000 | Requerimiento de conciliación | …»— y si se
    siguiera buscando cabecera, esa fila se descartaría por parecer un encabezado.
    Es el defecto que dejó la extracción de requerimientos en cero sin fallar.
    """
    out, dentro = [], False
    for l in texto.splitlines():
        if not dentro and l.startswith("|") and cabecera in l:
            dentro = True
            continue
        if dentro:
            if not l.startswith("|"):
                break
            celdas = [c.strip() for c in l.strip("|").split("|")]
            if all(set(c) <= {"-", ":"} for c in celdas):
                continue
            out.append(celdas)
    return out


def agrupar(raiz: Path, prefijo: str) -> dict:
    """Los archivos de cada caso, venga la carpeta como venga.

    Una carpeta por caso es la forma ordenada, y es la que este material usa casi
    siempre. Pero el agente promete funcionar con lo que haya, así que el extractor de
    referencia no puede depender de ella: agrupa por el código —que está en la carpeta o
    en el nombre del archivo— y cuando no encuentra ninguno, cae a la primera carpeta.
    """
    import re as _re
    grupos = {}
    for f in sorted(raiz.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(raiz)
        m = _re.search(rf"{prefijo}-[A-Z0-9]+", str(rel))
        clave = m.group(0) if m else rel.parts[0]
        grupos.setdefault(clave, []).append(f)
    return grupos


# ── proyectos ────────────────────────────────────────────────────────────

def ficha_proyecto(docs: list, raiz: Path) -> dict:
    docs = sorted(docs)
    rel = {p: str(p.relative_to(raiz)) for p in docs}

    acta = next((p for p in docs if "acta-constitucion" in p.name), None)
    crono = sorted(p for p in docs if "cronograma" in p.name)
    inf = next((p for p in docs if "informe-avance" in p.name
                or "nota-avance" in p.name), None)
    # Por el nombre y no por la carpeta: una minuta sigue siendo una minuta esté en
    # `30-reuniones`, en «Reuniones/Comité semanal» o suelta con las demás.
    minutas = sorted(p for p in docs
                     if any(x in p.name for x in ("comite", "reunion", "seguimiento",
                                                  "minuta")))
    recibos = [p for p in docs if "acta-recibo" in p.name]
    contratos = [p for p in docs if p.name.count("contrato")]
    facturas = [p for p in docs if "factura" in p.name]
    cambios = [p for p in docs if "solicitud-cambio" in p.name]

    if not acta:
        return None
    ta, fa = acta.read_text(encoding="utf-8"), fecha_de(acta.name)
    ra = rel[acta]

    def de_acta(etiqueta):
        v = negrita(ta, etiqueta)
        return campo(v, ra, fa) if v and v != "No aplica" else vacio()

    fechas = filas(ta, "Fecha")
    inicio = next((f[1] for f in fechas if f[0].lower().startswith("inicio")), None)
    cierre = next((f[1] for f in fechas if f[0].lower().startswith("cierre")), None)
    mpres = re.search(r"\*\*([\d.]+)\s*COP\*\*", ta)

    ficha = {
        "schema_version": "0.1",
        "identity": {
            "code": de_acta("Código"),
            "name": campo(ta.splitlines()[0].split("·", 1)[-1].strip(), ra, fa),
            "business_area": de_acta("Área dueña"),
            # «PRD-NOMINA · Nómina empresarial» → el código, que es con lo que la
            # traza del producto se confirma. El nombre solo no sirve: dos productos
            # pueden llamarse parecido y el código es único.
            "product": (lambda c: campo(c["value"].split("·")[0].strip(), c["source"],
                                        c["source_date"]) if c.get("value") else c)(
                de_acta("Producto asociado")),
            "sponsor": de_acta("Patrocinador"),
            "manager": de_acta("Gerente de proyecto"),
            "committee": de_acta("Comité"),
            # Ningún documento de esta organización delega autoridad. No se rellena
            # con lo razonable: se declara que no está dicho en ninguna parte.
            "authority": vacio(),
        },
        "declared": {"status": vacio(), "progress_pct": vacio(), "as_of": vacio()},
        "plan": {
            "start_date": campo(inicio, ra, fa) if inicio else vacio(),
            "end_date": campo(cierre, ra, fa) if cierre else vacio(),
            "baseline": [], "milestones": [],
        },
        "money": {"currency": campo("COP", ra, fa),
                  "approved": campo(plata(mpres.group(1)), ra, fa) if mpres else vacio(),
                  "committed": vacio(), "executed": vacio(), "projection": vacio()},
        "commitments": [], "activity": {}, "raid": {"dependencies": []},
    }

    # ── dependencias declaradas: «PRY-109 · Motor de decisión…»
    for d in vinetas(seccion(ta, "Dependencias declaradas")):
        m = re.match(r"(PRY-\d+)\s*·\s*(.+)", d)
        if m:
            ficha["raid"]["dependencies"].append({
                "on_project": campo(m.group(1), ra, fa),
                "what": campo(m.group(2).strip(), ra, fa),
                "confirmed": vacio()})

    # ── el estado declarado y el dinero salen del informe, que lo escribe el gerente
    if inf:
        ti, fi = inf.read_text(encoding="utf-8"), fecha_de(inf.name)
        ri = rel[inf]
        est = seccion(ti, "Estado declarado")
        me = re.search(r"\*\*(\w+)\*\*", est)
        mp = re.search(r"\*\*(\d+)%\*\*", est)
        corte = negrita(ti, "Fecha de corte") or fi
        if me:
            ficha["declared"]["status"] = campo(me.group(1).lower(), ri, corte)
        if mp:
            ficha["declared"]["progress_pct"] = campo(int(mp.group(1)), ri, corte)
        ficha["declared"]["as_of"] = campo(corte, ri, corte)
        for fila in filas(ti, "COP"):
            clave = {"Aprobado": "approved", "Comprometido": "committed",
                     "Ejecutado": "executed",
                     "Proyección al cierre": "projection"}.get(fila[0])
            if clave and plata(fila[1]):
                ficha["money"][clave] = campo(plata(fila[1]), ri, corte)

    # ── los hitos, y qué recibo los sustenta
    recibidos = {}
    for r in recibos:
        tr = r.read_text(encoding="utf-8")
        nombre = tr.splitlines()[0].split("·", 1)[-1].strip()
        recibidos[nombre.lower()] = (rel[r], negrita(tr, "Fecha de recibo"))
    def recibo_de(nombre: str):
        """El acta de recibo de un hito, si existe.

        Por contención y no por igualdad: el cronograma dice «Carga de archivo» y el
        acta dice «Carga de archivo de nómina». Un modelo lo empata leyendo; un parser
        necesita que se lo digan, y esta es la regla más cercana que hay sin inventar.
        """
        n = nombre.lower()
        for titulo, dato in recibidos.items():
            if n in titulo or titulo in n:
                return dato
        return None

    for c in crono:
        rc, fc = rel[c], fecha_de(c.name)
        lector = csv.DictReader(io.StringIO(c.read_text(encoding="utf-8")))
        hitos = []
        for fila in lector:
            nombre = fila["hito"]
            ev = recibo_de(nombre)
            cerrado = fila["estado"] == "cerrado"
            hitos.append({
                "name": campo(nombre, rc, fc),
                "baseline_date": campo(fila["fecha_linea_base"], rc, fc),
                "current_date": campo(fila["fecha_vigente"], rc, fc),
                "state": campo("met" if (cerrado or ev) else "open",
                               ev[0] if ev else rc, ev[1] if ev else fc),
                "evidence": campo(ev[0], ev[0], ev[1]) if ev else vacio()})
        ficha["plan"]["milestones"] = hitos
        if hitos:
            # La fecha de cierre del plan es la del cronograma vigente; la del acta es
            # el compromiso original, y la diferencia entre las dos es la desviación.
            ficha["plan"]["end_date"] = hitos[-1]["current_date"]
        ficha["plan"]["baseline"].append({
            "version": len(ficha["plan"]["baseline"]) + 1, "approved_on": fc,
            "start_date": inicio, "end_date": hitos[-1]["current_date"]["value"]
            if hitos else cierre,
            "reason": "línea base inicial" if not ficha["plan"]["baseline"]
            else "replanificación", "source": rc})

    # ── compromisos: el mismo doliente y lo mismo con fecha nueva es uno reprogramado
    vistos = {}
    for m in minutas:
        tm = m.read_text(encoding="utf-8")
        fm = negrita(tm, "Fecha") or fecha_de(m.name)
        rm = rel[m]
        for fila in filas(tm, "Responsable"):
            quien, que, para = fila[0], fila[1], fila[2]
            clave = (quien, que)
            fecha_ok = re.match(r"\d{4}-\d{2}-\d{2}", para)
            entrada = vistos.get(clave)
            if entrada is None:
                entrada = {"who": campo(quien, rm, fm), "what": campo(que, rm, fm),
                           "due_date": campo(para, rm, fm) if fecha_ok else vacio(),
                           "stated_on": campo(fm, rm, fm),
                           "state": campo("open", rm, fm), "reschedules": []}
                vistos[clave] = entrada
                ficha["commitments"].append(entrada)
            else:
                entrada["due_date"] = campo(para, rm, fm) if fecha_ok else vacio()
                entrada["stated_on"] = campo(fm, rm, fm)
                for k in ("who", "what", "state"):
                    entrada[k]["source"], entrada[k]["source_date"] = rm, fm
            if fecha_ok:
                entrada["reschedules"].append({"due_date": para, "source": rm})
    for c in ficha["commitments"]:
        if len(c["reschedules"]) < 2:
            c.pop("reschedules")

    # ── proveedores: contrato contra recibo contra factura
    if contratos:
        tc = contratos[0].read_text(encoding="utf-8")
        rc2 = rel[contratos[0]]
        fc2 = fecha_de(contratos[0].name)
        entregables = []
        for fila in filas(tc, "Entregable"):
            ev = recibo_de(fila[0])
            # El contrato declara el estado; el acta de recibo es la evidencia. Son
            # dos cosas distintas y el cruce entre ellas es media aritmética de
            # proveedores: «recibido» sin acta que lo sustente es un hallazgo.
            declarado = (fila[3] if len(fila) > 3 else "").strip().lower()
            estado = {"recibido": "accepted", "entregado": "delivered"}.get(
                declarado, "pending")
            entregables.append({
                "name": campo(fila[0], rc2, fc2),
                "due_date": campo(fila[1], rc2, fc2),
                "amount": campo(plata(fila[2]), rc2, fc2),
                "state": campo(estado, rc2, fc2),
                "evidence": campo(ev[0], ev[0], ev[1]) if ev else vacio()})
        total, detalle = 0, []
        for fx in facturas:
            tf = fx.read_text(encoding="utf-8")
            monto = plata(negrita(tf, "Valor") or "")
            total += monto or 0
            detalle.append({
                "concept": campo(negrita(tf, "Concepto"), rel[fx], fecha_de(fx.name)),
                "amount": campo(monto, rel[fx], fecha_de(fx.name))})
        ficha["vendors"] = [{"name": campo(negrita(tc, "Proveedor"), rc2, fc2),
                             "contract_ref": campo(
                                 tc.splitlines()[0].split("·")[0].split()[-1], rc2, fc2),
                             "deliverables": entregables,
                             "invoiced": campo(total, rc2, fc2) if detalle else vacio(),
                             "invoices": detalle}]

    # ── control de cambios sin línea base nueva
    if cambios:
        ficha["changes"] = []
        for ch in cambios:
            tch = ch.read_text(encoding="utf-8")
            aut = seccion(tch, "Autorización")
            import re as _re
            m_dias = _re.search(r"\|\s*Tiempo\s*\|\s*([+-]?\d+)\s*días", tch)
            aprobado = "Pendiente" not in aut
            ficha["changes"].append({
                "ref": campo(tch.splitlines()[0].split()[-1], rel[ch],
                             fecha_de(ch.name)),
                "decision": campo("approved" if aprobado else "pending",
                                  rel[ch], fecha_de(ch.name)),
                "time_impact": campo(int(m_dias.group(1)) if m_dias else None,
                                     rel[ch], fecha_de(ch.name)),
                "requested_on": campo(negrita(tch, "Fecha") or fecha_de(ch.name),
                                      rel[ch], fecha_de(ch.name))})

    # ── la ficha que el gerente publicó, si está
    # No se fusiona con la de Vera: se guarda al lado, y el cálculo compara las dos.
    publicada = next((p for p in docs if p.name.endswith("ficha-proyecto.json")), None)
    if publicada:
        ficha["pm_record"] = json.loads(publicada.read_text(encoding="utf-8"))

    # ── actividad
    todos = [(fecha_de(p.name), rel[p]) for p in docs if fecha_de(p.name)]
    if todos:
        f, r = max(todos)
        ficha["activity"]["last_document_date"] = campo(f, r, f)
    reuniones = [(fecha_de(p.name), rel[p]) for p in minutas if fecha_de(p.name)]
    if reuniones:
        f, r = max(reuniones)
        ficha["activity"]["last_meeting_date"] = campo(f, r, f)

    ficha["meta"] = {"record_updated": HOY.isoformat(),
                     "documents_seen": [{"path": rel[p]} for p in docs]}
    return ficha


# ── productos ────────────────────────────────────────────────────────────

def registro_producto(docs: list, raiz: Path) -> tuple:
    docs = sorted(docs)
    rel = {p: str(p.relative_to(raiz)) for p in docs}
    defin = next((p for p in docs if "definicion-producto" in p.name), None)
    caso = next((p for p in docs if "caso-de-negocio" in p.name), None)
    entre = next((p for p in docs if "entrevistas" in p.name), None)
    tab = next((p for p in docs if "tablero" in p.name), None)
    com = next((p for p in docs if "comite-producto" in p.name), None)
    if not defin:
        return None, [], []

    td, fd, rd = defin.read_text(encoding="utf-8"), fecha_de(defin.name), rel[defin]
    proyectos = [v.split("·")[0].strip() for v in
                 vinetas(seccion(td, "Proyectos que lo construyen"))
                 if v.startswith("PRY")]

    prod = {
        "identity": {
            "code": negrita(td, "Código"),
            "name": {"value": td.splitlines()[0].split("·", 1)[-1].strip(),
                     "source": rd, "source_date": fd},
            "manager": {"value": negrita(td, "Gerente de producto"), "source": rd,
                        "source_date": fd},
            "authority": {"value": None, "state": "not_found"},
        },
        "definition": {
            "problem": {"value": seccion(td, "El problema"), "source": rd,
                        "source_date": fd},
            "who": {"value": negrita(td, "Segmento"), "source": rd, "source_date": fd},
            "success": {"value": None, "state": "not_found"},
            "claims": [], "assumptions": [],
        },
        "activity": {"last_document_date": max(
            (fecha_de(p.name) for p in docs if fecha_de(p.name)), default=None)},
    }
    for s in vinetas(seccion(td, "Supuestos")):
        m = re.match(r"\*\*(.+?)\*\*\s*·\s*declarado el (\d{4}-\d{2}-\d{2})", s)
        if m:
            # Si el documento no dice nada sobre la verificación, queda sin verificar:
            # es lo que el documento dice, y no se rellena con lo razonable.
            prod["definition"]["assumptions"].append(
                {"value": m.group(1), "verified": "verificado" in s.lower()
                 and "sin verificar" not in s.lower(),
                 "stated_on": m.group(2), "source": rd})
    if caso:
        tc, fc, rc = caso.read_text(encoding="utf-8"), fecha_de(caso.name), rel[caso]
        for fila in filas(tc, "Métrica"):
            prod["definition"]["claims"].append(
                {"metric": fila[0], "declared": plata(fila[1]), "source": rc,
                 "source_date": fc})

    metricas = []
    if tab:
        tt, ft, rt = tab.read_text(encoding="utf-8"), fecha_de(tab.name), rel[tab]
        for fila in filas(tt, "Métrica"):
            metricas.append({"metric": fila[0], "source": rt,
                             "definition": f"serie del tablero de producto",
                             "series": [{"date": fila[2], "value": plata(fila[1])}]})

    reqs = []
    if com:
        tm, fm, rm = com.read_text(encoding="utf-8"), fecha_de(com.name), rel[com]
        evidencias = []
        if entre:
            te, fe, re_ = entre.read_text(encoding="utf-8"), fecha_de(entre.name), rel[entre]
            for m in re.finditer(r"^### (.+?) · (\d{4}-\d{2}-\d{2})", te, re.M):
                evidencias.append({"value": m.group(1), "source": re_,
                                   "source_date": m.group(2)})
        for fila in filas(tm, "Requerimiento"):
            rid, titulo, doliente, criterio, quien_pidio, estado, desde = fila[:7]
            # La traza es del requerimiento, no del producto. Heredarle al requerimiento
            # el primer proyecto de la definición hacía que `requirement_untraced` no
            # pudiera sonar nunca en un producto que declarara algún proyecto: el
            # hallazgo es justamente el requerimiento decidido que ningún proyecto
            # recogió, y ese se pierde entre los que sí.
            traza = fila[7].strip() if len(fila) > 7 else ""
            if traza in ("—", "", "-"):
                traza = None
            sin_doliente = doliente.lower().startswith("sin ")
            reqs.append({
                "id": rid, "product": prod["identity"]["code"],
                "title": {"value": titulo, "source": rm, "source_date": fm},
                "state": {"aceptado": "accepted", "propuesto": "proposed"}.get(
                    estado, estado),
                "stated_on": desde,
                "owner": ({"value": None, "state": "not_found"} if sin_doliente
                          else {"value": doliente, "kind": "person", "source": rm}),
                "need": {"value": titulo, "source": rm, "source_date": fm},
                # Un requerimiento sin criterio queda con la lista vacía, que es lo
                # que dice el documento. No se rellena con lo razonable.
                "acceptance": ([] if criterio in ("—", "", None)
                               else [{"value": criterio, "source": rm}]),
                # Solo la evidencia que el comité cita para ESE requerimiento. Un
                # aceptado sin nadie que lo haya pedido es una definición que se
                # sostiene sola, y ese es el hallazgo.
                "evidence": [e for e in evidencias
                             if quien_pidio not in ("—", "", None)
                             and e["value"].startswith(quien_pidio.split(",")[0])],
                "decision": {"what": {"value": titulo, "source": rm},
                             "who": "Comité de producto", "on": fm},
                "traces": {"project": traza, "deliverables": []},
            })
    return prod, reqs, metricas


# ── ejecución ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base = Path(sys.argv[1]).expanduser()
    proy_raiz = base / "documentos" / "proyectos"
    prod_raiz = base / "documentos" / "productos"

    # La extracción se rehace completa, no se acumula. Un registro que sobrevive a una
    # corrida anterior —un requerimiento que ya no está en ningún documento— sigue
    # produciendo hallazgos, y en cinco días eso infla la cuenta sin que nada falle.
    # Es el defecto que metió un `REQ-1542` fantasma en la primera calificación.
    for viejo in (base / "estado" / "records", base / "estado-productos"):
        if viejo.exists():
            shutil.rmtree(viejo)

    destino = base / "estado" / "records"
    destino.mkdir(parents=True, exist_ok=True)
    n = 0
    for clave, archivos in sorted(agrupar(proy_raiz, "PRY").items()):
        ficha = ficha_proyecto(archivos, proy_raiz)
        if not ficha:
            print(f"  SIN ACTA  {clave}")
            continue
        codigo = ficha["identity"]["code"]["value"]
        (destino / f"{codigo}.json").write_text(
            json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
    print(f"proyectos  {n} fichas  →  estado/records/")

    m = 0
    for clave, archivos in sorted(agrupar(prod_raiz, "PRD").items()):
        prod, reqs, metricas = registro_producto(archivos, prod_raiz)
        if not prod:
            continue
        codigo = prod["identity"]["code"]
        d = base / "estado-productos" / codigo
        (d / "requirements").mkdir(parents=True, exist_ok=True)
        (d / "metrics").mkdir(parents=True, exist_ok=True)
        (d / "producto.json").write_text(
            json.dumps(prod, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for r in reqs:
            (d / "requirements" / f"{r['id']}.json").write_text(
                json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for x in metricas:
            (d / "metrics" / f"{x['metric']}.json").write_text(
                json.dumps(x, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        m += 1
    print(f"productos  {m} registros  →  estado-productos/<código>/")
