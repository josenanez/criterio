#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-portfolio/scripts/texto.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
"""Criterio PMO — el documento a texto.

Convierte la documentación del portafolio a Markdown para que el modelo la lea y
para que el hash del texto sea estable. **No extrae campos**: eso lo hace el modelo
con el skill project-record. Aquí solo se saca el texto de adentro del archivo.

    python3 texto.py --docs <carpeta> --cache <carpeta>
    python3 texto.py --docs <carpeta> --cache <carpeta> --solo PRY-014
    python3 texto.py --selftest

Librería estándar, sin dependencias. Eso es posible porque `.docx`, `.xlsx` y
`.pptx` son archivos ZIP con XML adentro, y `zipfile` y `xml.etree` vienen con
Python. El cronograma de Microsoft Project guardado como XML también es XML, y se
procesa como cronograma: tareas, hitos, líneas base, predecesoras y recursos. El PDF
necesita `pdftotext`, y el `.mpp` binario de Project necesita Java con MPXJ; sin eso,
se declara cómo guardarlo para que se procese.

La conversión es un CACHÉ, no la fuente. La cita de una ficha apunta siempre al
documento original, porque es lo que una persona abre para verificar. El Markdown
existe para leer barato y para comparar corridas.

Salida: `<cache>/<misma ruta>.md` y `<cache>/manifest.json`, que declara por cada
archivo qué convertidor se usó o por qué no se pudo. **Nada se salta en silencio.**
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

IGNORAR = (".DS_Store", "Thumbs.db")
NATIVO = (".md", ".txt", ".csv", ".tsv", ".json", ".yaml", ".yml")


def limpiar(texto: str) -> str:
    texto = texto.replace(" ", " ")
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def hash_texto(texto: str) -> str:
    return hashlib.sha256(" ".join(texto.split()).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- convertidores

def de_nativo(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8", errors="replace")


def de_docx(ruta: Path) -> str:
    """Un .docx es un ZIP. El texto vive en word/document.xml, por párrafo."""
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with zipfile.ZipFile(ruta) as z:
        xml = z.read("word/document.xml")
    raiz = ET.fromstring(xml)
    lineas = []
    for p in raiz.iter(f"{W}p"):
        trozos = [t.text or "" for t in p.iter(f"{W}t")]
        linea = "".join(trozos).strip()
        # una fila de tabla se reconoce por el ancestro; sin recorrer ancestros,
        # basta con conservar el orden del documento: una tabla sale como líneas
        if linea:
            lineas.append(linea)
    return "\n\n".join(lineas)


def de_xlsx(ruta: Path) -> str:
    """Un .xlsx es un ZIP. Las cadenas están compartidas y las celdas referencian.

    Para una celda con fórmula se toma el valor en caché, que es el último
    calculado. Si ese valor cambia, el texto cambia — y está bien que cambie: el
    número es distinto. Lo que NO cambia el texto es un reguardado que solo mueve
    metadatos del ZIP, y ese es el caso que ahorra la relectura.
    """
    S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    with zipfile.ZipFile(ruta) as z:
        nombres = z.namelist()
        compartidas = []
        if "xl/sharedStrings.xml" in nombres:
            raiz = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in raiz.iter(f"{S}si"):
                compartidas.append("".join(t.text or "" for t in si.iter(f"{S}t")))

        titulos = {}
        if "xl/workbook.xml" in nombres:
            raiz = ET.fromstring(z.read("xl/workbook.xml"))
            for i, hoja in enumerate(raiz.iter(f"{S}sheet"), start=1):
                titulos[f"sheet{i}.xml"] = hoja.get("name", f"Hoja {i}")

        salida = []
        hojas = sorted(n for n in nombres
                       if n.startswith("xl/worksheets/sheet") and n.endswith(".xml"))
        for hoja in hojas:
            raiz = ET.fromstring(z.read(hoja))
            nombre = titulos.get(hoja.rsplit("/", 1)[-1], hoja)
            filas = []
            for fila in raiz.iter(f"{S}row"):
                celdas = []
                for c in fila.iter(f"{S}c"):
                    v = c.find(f"{S}v")
                    isx = c.find(f"{S}is")
                    if c.get("t") == "s" and v is not None and v.text is not None:
                        idx = int(v.text)
                        celdas.append(compartidas[idx] if idx < len(compartidas) else "")
                    elif isx is not None:
                        celdas.append("".join(t.text or "" for t in isx.iter(f"{S}t")))
                    elif v is not None:
                        celdas.append(v.text or "")
                    else:
                        celdas.append("")
                if any(x.strip() for x in celdas):
                    filas.append(" | ".join(x.strip() for x in celdas))
            if filas:
                salida.append(f"## {nombre}\n\n" + "\n".join(filas))
        return "\n\n".join(salida)


def de_pptx(ruta: Path) -> str:
    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    with zipfile.ZipFile(ruta) as z:
        laminas = sorted(n for n in z.namelist()
                         if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
        salida = []
        for i, lamina in enumerate(laminas, start=1):
            raiz = ET.fromstring(z.read(lamina))
            textos = [t.text.strip() for t in raiz.iter(f"{A}t") if t.text and t.text.strip()]
            if textos:
                salida.append(f"## Lámina {i}\n\n" + "\n\n".join(textos))
        return "\n\n".join(salida)


def de_marcado(ruta: Path) -> str:
    bruto = ruta.read_text(encoding="utf-8", errors="replace")
    bruto = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", bruto, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", bruto)


def de_eml(ruta: Path) -> str:
    """Un correo .eml se lee con la librería estándar. El .msg de Outlook no."""
    from email import policy
    from email.parser import BytesParser
    with ruta.open("rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)
    cabeza = [f"**De:** {msg.get('From','')}", f"**Para:** {msg.get('To','')}",
              f"**Fecha:** {msg.get('Date','')}", f"**Asunto:** {msg.get('Subject','')}"]
    cuerpo = ""
    if msg.is_multipart():
        for parte in msg.walk():
            if parte.get_content_type() == "text/plain":
                cuerpo = parte.get_content()
                break
        else:
            for parte in msg.walk():
                if parte.get_content_type() == "text/html":
                    cuerpo = re.sub(r"<[^>]+>", " ", parte.get_content())
                    break
    else:
        cuerpo = msg.get_content()
    return "\n".join(cabeza) + "\n\n" + (cuerpo or "")


def de_pdf(ruta: Path):
    """El PDF es el único formato que necesita algo de afuera.

    Se intenta `pdftotext`, de poppler, que es lo que hay instalado en la mayoría
    de los equipos y en cualquier imagen de Linux. Si no está, se declara — y si
    el PDF es un escaneo sin capa de texto, `pdftotext` devuelve vacío y eso
    tambien se declara: no hay OCR aquí, y un documento que no se pudo leer es un
    hallazgo de la carpeta, no un dato faltante inventado.
    """
    if not shutil.which("pdftotext"):
        return None, "pdftotext no está instalado (poppler). Sin él no se lee el PDF."
    try:
        r = subprocess.run(["pdftotext", "-layout", str(ruta), "-"],
                           capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, f"pdftotext falló: {e}"
    if r.returncode != 0:
        return None, f"pdftotext terminó en {r.returncode}"
    if len(r.stdout.strip()) < 20:
        return None, ("el PDF no tiene capa de texto: es un escaneo. Necesita OCR, "
                      "o que una persona lo transcriba.")
    return r.stdout, None


# ---------------------------------------------------------------- Microsoft Project

NS_PROJECT = "http://schemas.microsoft.com/project"
TIPOS_DEPENDENCIA = {"0": "FF", "1": "FS", "2": "SF", "3": "SS"}


def es_project(ruta: Path) -> bool:
    """El XML que guarda Microsoft Project (MSPDI): su raíz es `<Project>` en el espacio
    de nombres de Project. Cualquier otro XML se procesa como marcado."""
    try:
        with ruta.open("rb") as f:
            cabeza = f.read(4096).decode("utf-8", errors="replace")
    except OSError:
        return False
    return NS_PROJECT in cabeza and "<Project" in cabeza


def _fecha(v):
    return v[:10] if v and re.match(r"\d{4}-\d{2}-\d{2}", v) else None


def _dias(duracion, minutos_dia: int):
    """`PT40H0M0S` → días de trabajo, con los minutos por día del propio proyecto."""
    m = re.match(r"PT(\d+)H(\d+)M", duracion or "")
    if not m:
        return None
    return round((int(m.group(1)) * 60 + int(m.group(2))) / minutos_dia, 2)


def proyecto_mspdi(ruta: Path) -> dict:
    """El cronograma de un XML de Project, con sus campos y sin interpretar: lo que el
    archivo dice. La tarea de UID 0 es el resumen del proyecto y no se cuenta."""
    raiz = ET.parse(ruta).getroot()
    ns = {"p": NS_PROJECT}

    def t(el, tag):
        x = el.find(f"p:{tag}", ns)
        return x.text.strip() if x is not None and x.text else None

    minutos_dia = int(t(raiz, "MinutesPerDay") or 480)
    recursos = {t(r, "UID"): t(r, "Name") for r in raiz.findall("p:Resources/p:Resource", ns)}
    asignados = {}
    for a in raiz.findall("p:Assignments/p:Assignment", ns):
        nombre = recursos.get(t(a, "ResourceUID"))
        if nombre:
            asignados.setdefault(t(a, "TaskUID"), []).append(nombre)
    tareas = []
    for x in raiz.findall("p:Tasks/p:Task", ns):
        uid = t(x, "UID")
        if uid in (None, "0") or t(x, "IsNull") == "1":
            continue
        bases = {}
        for b in x.findall("p:Baseline", ns):
            bases[int(t(b, "Number") or 0)] = {"start": _fecha(t(b, "Start")), "finish": _fecha(t(b, "Finish"))}
        preds = [{"uid": t(l, "PredecessorUID"), "type": TIPOS_DEPENDENCIA.get(t(l, "Type") or "1", "FS"),
                  "lag_days": round(int(t(l, "LinkLag") or 0) / 10 / minutos_dia, 2)}
                 for l in x.findall("p:PredecessorLink", ns)]
        tareas.append({"uid": uid, "id": t(x, "ID"), "wbs": t(x, "WBS") or t(x, "OutlineNumber"),
                       "name": t(x, "Name") or "", "level": int(t(x, "OutlineLevel") or 1),
                       "summary": t(x, "Summary") == "1", "milestone": t(x, "Milestone") == "1",
                       "start": _fecha(t(x, "Start")), "finish": _fecha(t(x, "Finish")),
                       "duration_days": _dias(t(x, "Duration"), minutos_dia),
                       "percent": int(float(t(x, "PercentComplete") or 0)),
                       "actual_finish": _fecha(t(x, "ActualFinish")), "baselines": bases,
                       "predecessors": preds, "resources": asignados.get(uid, [])})
    return {"name": t(raiz, "Title") or t(raiz, "Name"), "start": _fecha(t(raiz, "StartDate")),
            "finish": _fecha(t(raiz, "FinishDate")), "status_date": _fecha(t(raiz, "StatusDate")),
            "tasks": tareas}


def hitos_project(cr: dict) -> list:
    """Las filas del cronograma con las mismas columnas que el CSV y el Excel —hito, fecha
    de línea base, fecha vigente, estado—, para que el motor las procese igual. Son los
    hitos del archivo; si no marca ninguno, las tareas que no son resumen."""
    filas = [x for x in cr["tasks"] if x["milestone"]] or [x for x in cr["tasks"] if not x["summary"]]
    return [{"hito": x["name"], "fecha_linea_base": (x["baselines"].get(0) or {}).get("finish") or x["finish"],
             "fecha_vigente": x["finish"],
             "estado": "cerrado" if x["percent"] >= 100 else ("en curso" if x["percent"] > 0 else "pendiente")}
            for x in filas if x["finish"]]


def de_project(ruta: Path) -> str:
    cr = proyecto_mspdi(ruta)
    por_uid = {x["uid"]: x["id"] or x["uid"] for x in cr["tasks"]}
    lineas = [f"# Cronograma · Microsoft Project · {cr['name'] or ruta.stem}", "",
              f"**Inicio:** {cr['start'] or '—'} · **Fin:** {cr['finish'] or '—'} · "
              f"**Fecha de estado:** {cr['status_date'] or '—'}", "", "## Tareas", "",
              "| ID | EDT | Tarea | Inicio | Fin | Línea base: fin | Avance | Tipo | Predecesoras | Recursos |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for x in cr["tasks"]:
        tipo = "hito" if x["milestone"] else ("resumen" if x["summary"] else "tarea")
        preds = ", ".join(f"{por_uid.get(p['uid'], p['uid'])}{p['type']}"
                          + (f"{'+' if p['lag_days'] > 0 else ''}{p['lag_days']:g}d" if p["lag_days"] else "")
                          for p in x["predecessors"])
        base = (x["baselines"].get(0) or {}).get("finish") or "—"
        lineas.append(f"| {x['id'] or ''} | {x['wbs'] or ''} | {'· ' * (x['level'] - 1)}{x['name']} | {x['start'] or '—'} | "
                      f"{x['finish'] or '—'} | {base} | {x['percent']}% | {tipo} | {preds or '—'} | {', '.join(x['resources']) or '—'} |")
    hitos = hitos_project(cr)
    if hitos:
        lineas += ["", "## Hitos", "", "| Hito | Línea base | Vigente | Estado |", "|---|---|---|---|"]
        lineas += [f"| {h['hito']} | {h['fecha_linea_base']} | {h['fecha_vigente']} | {h['estado']} |" for h in hitos]
    return "\n".join(lineas)


def de_xml(ruta: Path):
    """Un XML de Project es un cronograma; cualquier otro XML, marcado."""
    return ("project", de_project(ruta)) if es_project(ruta) else ("marcado", de_marcado(ruta))


def de_mpp(ruta: Path):
    """El `.mpp` es binario y propietario. Se procesa solo si el equipo tiene Java y MPXJ
    —`CRITERIO_MPXJ` con el classpath de sus .jar—, que lo pasa a XML de Project. Sin eso
    se declara, con la forma de guardarlo para que sí se procese."""
    import os
    import tempfile
    cp = os.environ.get("CRITERIO_MPXJ")
    if not cp or not shutil.which("java"):
        return None, ("Microsoft Project (.mpp). Guárdalo como XML de Project (Archivo → Guardar como → "
                      "XML) y se procesa como cronograma, o configura Java con MPXJ en CRITERIO_MPXJ.")
    with tempfile.TemporaryDirectory() as tmp:
        destino = Path(tmp) / (ruta.stem + ".xml")
        try:
            r = subprocess.run(["java", "-cp", cp, "net.sf.mpxj.sample.MpxjConvert", str(ruta), str(destino)],
                               capture_output=True, text=True, timeout=180)
        except (OSError, subprocess.TimeoutExpired) as e:
            return None, f"MPXJ falló: {e}"
        if r.returncode != 0 or not destino.exists():
            return None, f"MPXJ no pudo convertir el .mpp (código {r.returncode})"
        return de_project(destino), None


CONVERTIDORES = {
    ".docx": ("docx", de_docx), ".xlsx": ("xlsx", de_xlsx), ".pptx": ("pptx", de_pptx),
    ".html": ("marcado", de_marcado), ".htm": ("marcado", de_marcado),
    ".eml": ("eml", de_eml),
}

SIN_SOPORTE = {
    ".msg": "formato propietario de Outlook. Guárdalo como .eml y se lee.",
    ".doc": "Word anterior a 2007. Guárdalo como .docx y se lee.",
    ".xls": "Excel anterior a 2007. Guárdalo como .xlsx y se lee.",
    ".zip": "un contenedor: descomprímelo en la carpeta.",
}


# ---------------------------------------------------------------- correr

def convertir(docs: Path, cache: Path, solo: str | None = None) -> dict:
    cache.mkdir(parents=True, exist_ok=True)
    manifiesto, formatos = [], {}

    for ruta in sorted(docs.rglob("*")):
        if not ruta.is_file() or ruta.name in IGNORAR or ruta.name.startswith("."):
            continue
        rel = ruta.relative_to(docs)
        if solo and solo not in str(rel):
            continue
        ext = ruta.suffix.lower()
        formatos[ext] = formatos.get(ext, 0) + 1
        fila = {"path": str(rel), "format": ext}

        try:
            if ext in NATIVO:
                fila["converter"], texto, razon = "nativo", de_nativo(ruta), None
            elif ext == ".pdf":
                fila["converter"] = "pdftotext"
                texto, razon = de_pdf(ruta)
            elif ext == ".xml":
                fila["converter"], texto = de_xml(ruta)
                razon = None
            elif ext == ".mpp":
                fila["converter"] = "mpxj"
                texto, razon = de_mpp(ruta)
            elif ext in CONVERTIDORES:
                nombre, fn = CONVERTIDORES[ext]
                fila["converter"], texto, razon = nombre, fn(ruta), None
            elif ext in SIN_SOPORTE:
                fila["converter"], texto, razon = None, None, SIN_SOPORTE[ext]
            else:
                fila["converter"], texto, razon = None, None, f"formato {ext} no reconocido"
        except Exception as e:                                  # noqa: BLE001
            texto, razon = None, f"{type(e).__name__}: {e}"

        if texto is None or not texto.strip():
            fila.update(ok=False, reason=razon or "el convertidor no devolvió texto")
        else:
            texto = limpiar(texto)
            destino = cache / rel.with_suffix(rel.suffix + ".md")
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(
                f"<!-- origen: {rel} · convertidor: {fila['converter']} -->\n"
                f"<!-- Esto es un caché. La cita de una ficha apunta al original. -->\n\n"
                f"{texto}\n", encoding="utf-8")
            fila.update(ok=True, chars=len(texto), text_hash=hash_texto(texto),
                        cached=str(destino.relative_to(cache)))
        manifiesto.append(fila)

    ok = [f for f in manifiesto if f["ok"]]
    resumen = {
        "documents": len(manifiesto),
        "converted": len(ok),
        "unreadable": len(manifiesto) - len(ok),
        "formats": dict(sorted(formatos.items())),
        "pdftotext": bool(shutil.which("pdftotext")),
        "files": manifiesto,
    }
    (cache / "manifest.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    return resumen


def selftest() -> int:
    """Construye un .docx, un .xlsx, un .pptx y un XML de Project mínimos y los vuelve a leer."""
    import tempfile
    tmp = Path(tempfile.mkdtemp())
    docs = tmp / "docs"
    docs.mkdir()

    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    doc = (f'<?xml version="1.0"?><w:document xmlns:w="{W}"><w:body>'
           '<w:p><w:r><w:t>Patrocinador: María Restrepo</w:t></w:r></w:p>'
           '<w:p><w:r><w:t>Cierre: 2026-11-30</w:t></w:r></w:p>'
           '</w:body></w:document>')
    with zipfile.ZipFile(docs / "acta.docx", "w") as z:
        z.writestr("word/document.xml", doc)

    S = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    with zipfile.ZipFile(docs / "presupuesto.xlsx", "w") as z:
        z.writestr("xl/sharedStrings.xml",
                   f'<?xml version="1.0"?><sst xmlns="{S}">'
                   '<si><t>Aprobado</t></si><si><t>Comprometido</t></si></sst>')
        z.writestr("xl/workbook.xml",
                   f'<?xml version="1.0"?><workbook xmlns="{S}"><sheets>'
                   '<sheet name="Presupuesto" sheetId="1"/></sheets></workbook>')
        z.writestr("xl/worksheets/sheet1.xml",
                   f'<?xml version="1.0"?><worksheet xmlns="{S}"><sheetData>'
                   '<row><c t="s"><v>0</v></c><c t="s"><v>1</v></c></row>'
                   '<row><c><v>1850000000</v></c><c><v>1762000000</v></c></row>'
                   '</sheetData></worksheet>')

    A = "http://schemas.openxmlformats.org/drawingml/2006/main"
    with zipfile.ZipFile(docs / "comite.pptx", "w") as z:
        z.writestr("ppt/slides/slide1.xml",
                   f'<?xml version="1.0"?><sld xmlns:a="{A}"><a:t>Decisión: ampliar '
                   'el alcance</a:t></sld>')

    (docs / "minuta.md").write_text("# Minuta\n\nCarlos se compromete al viernes.\n",
                                    encoding="utf-8")
    (docs / "reporte.msg").write_bytes(b"binario de outlook")

    # El XML que guarda Microsoft Project: un resumen, dos tareas y un hito con línea base,
    # predecesora, avance y un recurso asignado.
    (docs / "cronograma.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><Project xmlns="{NS_PROJECT}"><Title>Core de depósitos</Title>'
        '<StartDate>2026-01-12T08:00:00</StartDate><FinishDate>2026-09-30T17:00:00</FinishDate>'
        '<StatusDate>2026-06-01T17:00:00</StatusDate><MinutesPerDay>480</MinutesPerDay><Tasks>'
        '<Task><UID>0</UID><ID>0</ID><Name>Core de depósitos</Name><Summary>1</Summary></Task>'
        '<Task><UID>1</UID><ID>1</ID><Name>Diseño</Name><WBS>1</WBS><OutlineLevel>1</OutlineLevel>'
        '<Start>2026-01-12T08:00:00</Start><Finish>2026-03-06T17:00:00</Finish><Duration>PT320H0M0S</Duration>'
        '<PercentComplete>100</PercentComplete><Baseline><Number>0</Number><Finish>2026-02-27T17:00:00</Finish></Baseline></Task>'
        '<Task><UID>2</UID><ID>2</ID><Name>Migración</Name><WBS>2</WBS><OutlineLevel>1</OutlineLevel>'
        '<Start>2026-03-09T08:00:00</Start><Finish>2026-08-28T17:00:00</Finish><PercentComplete>40</PercentComplete>'
        '<PredecessorLink><PredecessorUID>1</PredecessorUID><Type>1</Type><LinkLag>9600</LinkLag></PredecessorLink></Task>'
        '<Task><UID>3</UID><ID>3</ID><Name>Salida en vivo</Name><WBS>3</WBS><OutlineLevel>1</OutlineLevel><Milestone>1</Milestone>'
        '<Start>2026-09-30T17:00:00</Start><Finish>2026-09-30T17:00:00</Finish><PercentComplete>0</PercentComplete>'
        '<Baseline><Number>0</Number><Finish>2026-07-31T17:00:00</Finish></Baseline>'
        '<PredecessorLink><PredecessorUID>2</PredecessorUID><Type>1</Type></PredecessorLink></Task>'
        '</Tasks><Resources><Resource><UID>1</UID><Name>Laura Gómez</Name></Resource></Resources>'
        '<Assignments><Assignment><TaskUID>2</TaskUID><ResourceUID>1</ResourceUID></Assignment></Assignments></Project>',
        encoding="utf-8")
    (docs / "otro.xml").write_text('<?xml version="1.0"?><nota><p>Texto de una nota</p></nota>', encoding="utf-8")
    (docs / "plan.mpp").write_bytes(b"binario de project")

    r = convertir(docs, tmp / "cache")
    por_ruta = {f["path"]: f for f in r["files"]}
    leer = lambda p: (tmp / "cache" / por_ruta[p]["cached"]).read_text(encoding="utf-8")

    pruebas = [
        ("documentos vistos", r["documents"], 8),
        ("convertidos", r["converted"], 6),
        ("ilegibles declarados", r["unreadable"], 2),
        ("project · se reconoce", por_ruta["cronograma.xml"]["converter"], "project"),
        ("project · la tarea, su fin y su avance", "| 2 | 2 | Migración | 2026-03-09 | 2026-08-28 | — | 40% |" in leer("cronograma.xml"), True),
        ("project · predecesora con desfase", "1FS+2d" in leer("cronograma.xml"), True),
        ("project · recurso asignado", "Laura Gómez" in leer("cronograma.xml"), True),
        ("project · el hito contra su línea base", "| Salida en vivo | 2026-07-31 | 2026-09-30 | pendiente |" in leer("cronograma.xml"), True),
        ("project · el resumen no es tarea", "| 0 |" in leer("cronograma.xml"), False),
        ("xml común · sigue como marcado", por_ruta["otro.xml"]["converter"], "marcado"),
        ("mpp · sin MPXJ se declara", por_ruta["plan.mpp"]["ok"], False),
        ("mpp · dice cómo guardarlo", "XML de Project" in por_ruta["plan.mpp"]["reason"], True),
        ("docx · patrocinador", "María Restrepo" in leer("acta.docx"), True),
        ("docx · dos párrafos", "2026-11-30" in leer("acta.docx"), True),
        ("xlsx · nombre de la hoja", "Presupuesto" in leer("presupuesto.xlsx"), True),
        ("xlsx · cadena compartida", "Comprometido" in leer("presupuesto.xlsx"), True),
        ("xlsx · valor numérico", "1850000000" in leer("presupuesto.xlsx"), True),
        ("pptx · texto de la lámina", "ampliar el alcance" in leer("comite.pptx"), True),
        ("md · pasa nativo", por_ruta["minuta.md"]["converter"], "nativo"),
        ("msg · se declara", por_ruta["reporte.msg"]["ok"], False),
        ("msg · con la razón", "Outlook" in por_ruta["reporte.msg"]["reason"], True),
        ("caché · <estado>/cache/texto", cache_valido(Path("estado/cache/texto")), True),
        ("caché · rechaza <estado>/texto", cache_valido(Path("estado/texto")), False),
    ]
    ok = True
    for etiqueta, tiene, quiere in pruebas:
        bien = tiene == quiere
        ok &= bien
        print(f"  {'OK ' if bien else 'FALLA'} {etiqueta:34} {tiene!r}"
              f"{'' if bien else f'  esperado {quiere!r}'}")
    shutil.rmtree(tmp)
    print("\nselftest:", "sin errores" if ok else "CON ERRORES")
    return 0 if ok else 1


def cache_valido(cache: Path) -> bool:
    """El caché tiene un solo lugar, `<estado>/cache/texto/`. Un barrido de la ronda 6 lo
    dejó en `<estado>/texto/`, fuera de lo que declara su contrato, aunque el skill lo
    dice: la regla está ahora en el script, que es donde no se olvida."""
    return tuple(Path(cache).parts[-2:]) == ("cache", "texto")


def main() -> int:
    ap = argparse.ArgumentParser(description="Criterio PMO — el documento a texto.")
    ap.add_argument("--docs", type=Path)
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--solo", default=None, help="convertir solo lo que contenga esto")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.docs or not args.cache:
        ap.error("--docs y --cache son obligatorios")
    if not cache_valido(args.cache):
        ap.error(f"el caché va en <estado>/cache/texto, no en {args.cache}: "
                 "es el único sitio que declara el contrato del comando")

    r = convertir(args.docs, args.cache, args.solo)
    print(json.dumps({k: v for k, v in r.items() if k != "files"},
                     ensure_ascii=False, indent=2))
    for f in r["files"]:
        if not f["ok"]:
            print(f"  no se pudo leer · {f['path']} · {f['reason']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
