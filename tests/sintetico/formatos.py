# -*- coding: utf-8 -*-
"""Pasa parte del material a Word, Excel y PDF, como llega en una organización real.

    python3 tests/sintetico/simulador.py <carpeta> --dia 1 --sector mineria --formatos

Hasta el 14 de octubre de 2026 todo el material era Markdown y CSV, y la página decía
«docx · xlsx · pptx · pdf · eml». Lo que no se había probado era justo lo que la gente
tiene: el acta en Word, el cronograma en Excel o en Microsoft Project y el informe en PDF.

Sin dependencias, como `texto.py`: un .docx y un .xlsx son un ZIP con XML, y un PDF de
texto se escribe a mano. Las tablas del Markdown pasan a tablas de verdad en Word, no a
líneas con barras: así llega una minuta.

**Qué se convierte se decide por el nombre del archivo**, con un hash, así que el mismo
documento queda en el mismo formato todos los días de la prueba. Los hechos no cambian
con el formato, y por eso la clave tampoco: un agente que acierta en Markdown y falla en
Word está fallando en la lectura.
"""
from __future__ import annotations

import hashlib
import os
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "plugins" / "criterio-portfolio" / "scripts"))
from terminos import pdf_de_lineas  # noqa: E402

# Qué tipo de documento va a qué formato, y en qué proporción.
REGLAS = (
    ("acta-constitucion", ".docx", 0.6), ("comite", ".docx", 0.5), ("minuta", ".docx", 0.5),
    ("informe-avance", ".pdf", 0.5), ("acta-recibo", ".pdf", 0.5), ("factura", ".pdf", 0.7),
    ("contrato", ".docx", 0.6), ("definicion-producto", ".docx", 0.5),
    ("entrevistas", ".docx", 0.4), ("cronograma-v", ".xlsx", 0.45),
)
# De los cronogramas que no pasan a Excel, esta parte se guarda desde Microsoft Project, como
# XML (desde la 0.7.0). El resto queda en CSV: los tres formatos en que llega un cronograma.
CRONOGRAMA_PROJECT = 0.6


def _fijo(nombre: str) -> zipfile.ZipInfo:
    """La entrada de un ZIP con fecha fija: sin esto, `writestr` le pone la hora de la corrida y el
    mismo material sale distinto cada minuto."""
    zi = zipfile.ZipInfo(nombre, date_time=(2026, 1, 1, 0, 0, 0))
    zi.compress_type = zipfile.ZIP_DEFLATED
    return zi


def _toca(ruta: Path, proporcion: float, sal: str = "") -> bool:
    h = int(hashlib.sha256((sal + ruta.name).encode("utf-8")).hexdigest()[:8], 16)
    return (h % 1000) / 1000 < proporcion


# ── Markdown a bloques ────────────────────────────────────────────────────

def bloques(md: str) -> list:
    """('h', nivel, texto) · ('p', texto) · ('li', texto) · ('tabla', filas)."""
    out, tabla = [], []
    for linea in md.splitlines():
        l = linea.rstrip()
        if l.startswith("|"):
            celdas = [c.strip() for c in l.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in celdas if c):
                tabla.append(celdas)
            continue
        if tabla:
            out.append(("tabla", tabla))
            tabla = []
        if not l.strip():
            continue
        m = re.match(r"(#+)\s+(.*)", l)
        if m:
            out.append(("h", len(m.group(1)), m.group(2)))
        elif re.match(r"\s*[-*]\s+", l):
            out.append(("li", re.sub(r"\s*[-*]\s+", "", l, count=1)))
        else:
            out.append(("p", l))
    if tabla:
        out.append(("tabla", tabla))
    return out


def _plano(t: str) -> str:
    return t.replace("**", "").replace("«", "«").strip()


# ── Word ──────────────────────────────────────────────────────────────────

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def _wp(texto: str, negrita=False, estilo=None) -> str:
    pr = f'<w:pPr><w:pStyle w:val="{estilo}"/></w:pPr>' if estilo else ""
    rpr = "<w:rPr><w:b/></w:rPr>" if negrita else ""
    return f'<w:p>{pr}<w:r>{rpr}<w:t xml:space="preserve">{escape(_plano(texto))}</w:t></w:r></w:p>'


def a_docx(md: str, destino: Path) -> None:
    cuerpo = []
    for b in bloques(md):
        if b[0] == "h":
            cuerpo.append(_wp(b[2], negrita=True, estilo=f"Heading{min(b[1], 3)}"))
        elif b[0] == "li":
            cuerpo.append(_wp("• " + b[1]))
        elif b[0] == "p":
            cuerpo.append(_wp(b[1]))
        else:
            filas = "".join("<w:tr>" + "".join(f"<w:tc>{_wp(c)}</w:tc>" for c in fila) + "</w:tr>"
                            for fila in b[1])
            cuerpo.append(f"<w:tbl>{filas}</w:tbl>")
    doc = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {W}>'
           f'<w:body>{"".join(cuerpo)}</w:body></w:document>')
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(_fijo("[Content_Types].xml"),
                   '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
        z.writestr(_fijo("_rels/.rels"),
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
        z.writestr(_fijo("word/document.xml"), doc)


# ── Excel ─────────────────────────────────────────────────────────────────

def _col(i: int) -> str:
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def a_xlsx(csv_texto: str, destino: Path, hoja: str = "Cronograma") -> None:
    import csv
    filas = list(csv.reader(csv_texto.splitlines()))
    xml_filas = []
    for r, fila in enumerate(filas, start=1):
        celdas = "".join(f'<c r="{_col(c)}{r}" t="inlineStr"><is><t>{escape(v)}</t></is></c>'
                         for c, v in enumerate(fila))
        xml_filas.append(f'<row r="{r}">{celdas}</row>')
    S = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"'
    R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(_fijo("[Content_Types].xml"),
                   '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr(_fijo("_rels/.rels"),
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr(_fijo("xl/workbook.xml"),
                   f'<?xml version="1.0" encoding="UTF-8"?><workbook {S} {R}><sheets>'
                   f'<sheet name="{escape(hoja)}" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr(_fijo("xl/_rels/workbook.xml.rels"),
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr(_fijo("xl/worksheets/sheet1.xml"),
                   f'<?xml version="1.0" encoding="UTF-8"?><worksheet {S}><sheetData>'
                   f'{"".join(xml_filas)}</sheetData></worksheet>')


# ── XML de Microsoft Project ─────────────────────────────────────────────

def a_mspdi(csv_texto: str, destino: Path, titulo: str = "Cronograma") -> None:
    """El cronograma guardado desde Microsoft Project (MSPDI): cada hito del CSV con su fecha
    vigente, su línea base guardada en el propio archivo, su avance y la predecesora de
    fin a comienzo con el hito anterior. Los mismos hechos que el CSV, en el formato de
    Project."""
    import csv
    filas = [r for r in csv.DictReader(csv_texto.strip().splitlines()) if r.get("hito")]
    avance = {"cerrado": 100, "en curso": 50}
    tareas = []
    for i, r in enumerate(filas, start=1):
        fin, base = r.get("fecha_vigente") or r.get("fecha_linea_base"), r.get("fecha_linea_base") or r.get("fecha_vigente")
        pred = (f"<PredecessorLink><PredecessorUID>{i - 1}</PredecessorUID><Type>1</Type></PredecessorLink>" if i > 1 else "")
        tareas.append(f"<Task><UID>{i}</UID><ID>{i}</ID><Name>{escape(r['hito'])}</Name><WBS>{i}</WBS>"
                      f"<OutlineLevel>1</OutlineLevel><Milestone>1</Milestone><Start>{fin}T17:00:00</Start>"
                      f"<Finish>{fin}T17:00:00</Finish><Duration>PT0H0M0S</Duration>"
                      f"<PercentComplete>{avance.get((r.get('estado') or '').strip(), 0)}</PercentComplete>"
                      f"<Baseline><Number>0</Number><Finish>{base}T17:00:00</Finish></Baseline>{pred}</Task>")
    destino.write_text(
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<Project xmlns="http://schemas.microsoft.com/project"><Title>{escape(titulo)}</Title>'
        f'<MinutesPerDay>480</MinutesPerDay><Tasks><Task><UID>0</UID><ID>0</ID><Name>{escape(titulo)}</Name>'
        f'<Summary>1</Summary></Task>{"".join(tareas)}</Tasks></Project>', encoding="utf-8")


# ── PDF ───────────────────────────────────────────────────────────────────

def _envolver(t: str, ancho: int = 92) -> list:
    out, linea = [], ""
    for p in t.split():
        if len(linea) + len(p) + 1 > ancho and linea:
            out.append(linea)
            linea = p
        else:
            linea = (linea + " " + p).strip()
    return out + ([linea] if linea else [])


def a_pdf(md: str, destino: Path) -> None:
    """Un PDF con capa de texto, Helvetica, en tantas páginas como haga falta."""
    lineas = []
    for b in bloques(md):
        if b[0] == "h":
            lineas += [("", 11), (_plano(b[2]), 14 if b[1] == 1 else 12)]
        elif b[0] == "tabla":
            for fila in b[1]:
                lineas += [(x, 10) for x in _envolver("   ".join(_plano(c) for c in fila))]
        else:
            pre = "- " if b[0] == "li" else ""
            lineas += [(x, 10) for x in _envolver(pre + _plano(b[1]))]
    # El PDF lo escribe el plugin, que también lo usa para el comprobante de los términos:
    # una sola implementación, que la puerta de formatos ejercita con el material.
    pdf_de_lineas(lineas, destino)


# ── la pasada ─────────────────────────────────────────────────────────────

def convertir(raiz: Path) -> dict:
    """Recorre `raiz/documentos` y reemplaza los elegidos por su versión en otro formato.
    Devuelve cuántos de cada uno, para la bitácora."""
    cuenta = {}
    for f in sorted((raiz / "documentos").rglob("*")):
        if not f.is_file() or f.suffix not in (".md", ".csv"):
            continue
        if ("cronograma-v" in f.name and f.suffix == ".csv" and not _toca(f, dict((c, x) for c, _, x in REGLAS)["cronograma-v"])
                and _toca(f, CRONOGRAMA_PROJECT, sal="project")):
            nuevo = f.with_suffix(".xml")
            a_mspdi(f.read_text(encoding="utf-8"), nuevo)
            st = f.stat()
            os.utime(nuevo, (st.st_atime, st.st_mtime))
            f.unlink()
            cuenta[".xml"] = cuenta.get(".xml", 0) + 1
            continue
        for clave, ext, prop in REGLAS:
            if clave in f.name and _toca(f, prop):
                if ext == ".xlsx" and f.suffix != ".csv":
                    break
                if ext != ".xlsx" and f.suffix != ".md":
                    break
                nuevo = f.with_suffix(ext)
                texto = f.read_text(encoding="utf-8")
                {".docx": a_docx, ".pdf": a_pdf, ".xlsx": a_xlsx}[ext](texto, nuevo)
                st = f.stat()          # la fecha del archivo es parte del material
                os.utime(nuevo, (st.st_atime, st.st_mtime))
                f.unlink()
                cuenta[ext] = cuenta.get(ext, 0) + 1
                break
    return cuenta


def selftest() -> list:
    import tempfile
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "plugins" / "criterio-portfolio" / "scripts"))
    import texto
    md = ("# Minuta · Comité\n\n**Fecha:** 2026-10-02\n\n## Compromisos\n\n"
          "| Quién | Qué | Para |\n|---|---|---|\n| Rubén Cárdenas | Entregar el contrato | 2026-10-19 |\n")
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        a_docx(md, t / "m.docx")
        a_xlsx("hito,fecha_linea_base\nDiseño,2026-01-10\n", t / "c.xlsx")
        a_pdf(md + "\nAvance reportado: **54%**\n", t / "i.pdf")
        docx, xlsx = texto.de_docx(t / "m.docx"), texto.de_xlsx(t / "c.xlsx")
        # Lo que el plugin hace con ellos: la línea base desde el Excel, y el hash del
        # texto de un Word, que decide si un documento reguardado se relee.
        import portafolio
        pry = t / "docs" / "PRY-1"
        pry.mkdir(parents=True)
        a_xlsx("hito,fecha_linea_base,fecha_vigente\nDiseño,2026-01-10,2026-01-10\n"
               "Salida,2026-06-30,2026-08-15\n", pry / "2026-02-01-cronograma-v2.xlsx")
        a_mspdi("hito,fecha_linea_base,fecha_vigente,estado\nDiseño,2026-01-10,2026-01-10,cerrado\n"
                "Salida,2026-06-30,2026-09-30,en curso\n", pry / "2026-07-01-cronograma-v3.xml")
        lb = portafolio.lineas_base_csv(pry, t / "docs")
        proj = texto.de_project(pry / "2026-07-01-cronograma-v3.xml")
        return [
            ("project · la línea base sale del XML de Project",
             [(b["version"], b["end_date"], b["baseline_end_date"]) for b in lb if b["version"] == 3],
             [(3, "2026-09-30", "2026-06-30")]),
            ("project · el hito con su avance y su predecesora",
             "| Salida | 2026-06-30 | 2026-09-30 | en curso |" in proj and "| 2 | 2 | Salida |" in proj and "1FS" in proj, True),
            ("xlsx · la línea base sale del cronograma en Excel",
             [(b["version"], b["end_date"], b["baseline_end_date"]) for b in lb if b["version"] == 2],
             [(2, "2026-08-15", "2026-06-30")]),
            ("docx · tiene hash de texto", portafolio.hash_texto(t / "m.docx") is not None, True),
            ("docx · la tabla se lee", "Rubén Cárdenas" in docx and "2026-10-19" in docx, True),
            ("xlsx · encabezado y fila", "hito | fecha_linea_base" in xlsx and "Diseño | 2026-01-10" in xlsx, True),
            ("pdf · encabezado de archivo", (t / "i.pdf").read_bytes()[:8], b"%PDF-1.4"),
        ]


if __name__ == "__main__":
    import sys
    malos = [f"FALLA {n}: {a!r} en vez de {b!r}" for n, a, b in selftest() if a != b]
    print("\n".join(malos) or "formatos: sin errores")
    sys.exit(1 if malos else 0)
