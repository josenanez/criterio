#!/usr/bin/env python3
"""Criterio PMO — el documento a texto.

Convierte la documentación del portafolio a Markdown para que el modelo la lea y
para que el hash del texto sea estable. **No extrae campos**: eso lo hace el modelo
con el skill project-record. Aquí solo se saca el texto de adentro del archivo.

    python3 texto.py --docs <carpeta> --cache <carpeta>
    python3 texto.py --docs <carpeta> --cache <carpeta> --solo PRY-014
    python3 texto.py --selftest

Librería estándar, sin dependencias. Eso es posible porque `.docx`, `.xlsx` y
`.pptx` son archivos ZIP con XML adentro, y `zipfile` y `xml.etree` vienen con
Python. El correo .msg de Outlook es un archivo compuesto de Microsoft (MS-CFB) con las
propiedades del mensaje adentro (MS-OXMSG), y también se procesa aquí, con `struct`. El cronograma de Microsoft Project guardado como XML también es XML, y se
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
import datetime as _dt
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

class _Ignorar(tuple):
    """Lo que ningún recorrido cuenta como documento: lo del sistema operativo y el archivo que
    marca la carpeta raíz (ADR 0011), que es del agente y no de la organización."""
    def __contains__(self, nombre) -> bool:
        if tuple.__contains__(self, nombre):
            return True
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import raiz
        return raiz.es_marcador(str(nombre))


IGNORAR = _Ignorar((".DS_Store", "Thumbs.db"))
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



# ---------------------------------------------------------------- el .msg de Outlook
# Un .msg es un archivo compuesto de Microsoft (MS-CFB): un pequeño sistema de archivos con
# sectores, una tabla de asignación (FAT) y un directorio en árbol. Adentro, cada propiedad del
# mensaje es un flujo «__substg1.0_<id><tipo>» y las de tamaño fijo —las fechas— van juntas en
# «__properties_version1.0» (MS-OXMSG). Se lee lo que procesa el código: quién, a quién, cuándo,
# el asunto, el identificador y a qué responde; y el cuerpo, para la agente.

_FIN, _LIBRE = 0xFFFFFFFE, 0xFFFFFFFF


def _cfb(datos: bytes) -> dict:
    """Los flujos de un archivo compuesto, por ruta («a/b/c»). Falla con un mensaje si no lo es."""
    if datos[:8] != bytes.fromhex("D0CF11E0A1B11AE1"):
        raise ValueError("no es un archivo compuesto de Microsoft")
    sec = 1 << struct.unpack_from("<H", datos, 0x1E)[0]
    mini = 1 << struct.unpack_from("<H", datos, 0x20)[0]
    n_fat, dir1, corte, minifat1, n_minifat, difat1, n_difat = struct.unpack_from("<IIxxxxIIIII", datos, 0x2C)

    def sector(n):
        return datos[(n + 1) * sec:(n + 2) * sec]
    difat = list(struct.unpack_from("<109I", datos, 0x4C))
    n = difat1
    for _ in range(n_difat):
        if n in (_FIN, _LIBRE):
            break
        s_ = sector(n)
        difat += list(struct.unpack_from(f"<{sec // 4 - 1}I", s_))
        n = struct.unpack_from("<I", s_, sec - 4)[0]
    fat: list[int] = []
    for f in difat[:n_fat]:
        fat += list(struct.unpack_from(f"<{sec // 4}I", sector(f)))

    def cadena(ini, tabla, limite=1 << 20):
        out, n = [], ini
        while n not in (_FIN, _LIBRE) and n < len(tabla) and len(out) < limite:
            out.append(n)
            n = tabla[n]
        return out
    directorio = b"".join(sector(x) for x in cadena(dir1, fat))
    entradas = []
    for i in range(len(directorio) // 128):
        e = directorio[i * 128:(i + 1) * 128]
        largo = struct.unpack_from("<H", e, 64)[0]
        nombre = e[:max(largo - 2, 0)].decode("utf-16-le", "replace")
        tipo = e[66]
        izq, der, hijo = struct.unpack_from("<III", e, 68)
        inicio, tam = struct.unpack_from("<IQ", e, 116)
        if sec == 512:
            tam &= 0xFFFFFFFF
        entradas.append({"nombre": nombre, "tipo": tipo, "izq": izq, "der": der, "hijo": hijo, "inicio": inicio, "tam": tam})
    raiz = entradas[0]
    flujo_mini = b"".join(sector(x) for x in cadena(raiz["inicio"], fat))[:raiz["tam"]]
    minifat: list[int] = []
    for x in cadena(minifat1, fat):
        minifat += list(struct.unpack_from(f"<{sec // 4}I", sector(x)))

    def contenido(e):
        if e["tam"] < corte:
            return b"".join(flujo_mini[x * mini:(x + 1) * mini] for x in cadena(e["inicio"], minifat))[:e["tam"]]
        return b"".join(sector(x) for x in cadena(e["inicio"], fat))[:e["tam"]]
    flujos: dict[str, bytes] = {}

    def hijos(i, ruta, vistos):
        # Los hermanos son un árbol: se recorre entero, sin suponer que está balanceado.
        pila = [i]
        while pila:
            j = pila.pop()
            if j in (_LIBRE, _FIN) or j >= len(entradas) or j in vistos:
                continue
            vistos.add(j)
            e = entradas[j]
            pila += [e["izq"], e["der"]]
            r = f"{ruta}/{e['nombre']}" if ruta else e["nombre"]
            if e["tipo"] == 2:
                flujos[r] = contenido(e)
            elif e["tipo"] == 1:
                hijos(e["hijo"], r, vistos)
    hijos(raiz["hijo"], "", set())
    return flujos


def _filetime(v: int):
    return _dt.datetime(1601, 1, 1, tzinfo=_dt.timezone.utc) + _dt.timedelta(microseconds=v // 10) if v else None


def leer_msg(ruta: Path) -> dict:
    """Los encabezados y el cuerpo de un .msg: lo mismo que se toma de un .eml."""
    flujos = _cfb(Path(ruta).read_bytes())

    def texto(pid, base="__substg1.0_"):
        for tipo, cod in (("001F", "utf-16-le"), ("001E", "cp1252")):
            b = flujos.get(f"{base}{pid}{tipo}")
            if b is not None:
                return b.decode(cod, "replace").rstrip("\x00")
        return ""
    fijas = {}
    props = flujos.get("__properties_version1.0", b"")
    for k in range(32, len(props) - 15, 16):
        etiqueta, _, valor = struct.unpack_from("<IIQ", props, k)
        fijas[etiqueta >> 16] = (etiqueta & 0xFFFF, valor)
    fecha_ = None
    for pid in (0x0039, 0x0E06):                       # cuándo se envió; si no, cuándo llegó
        if pid in fijas and fijas[pid][0] == 0x0040:
            fecha_ = _filetime(fijas[pid][1])
            break
    para, copia = [], []
    for r in sorted({k.split("/")[0] for k in flujos if k.startswith("__recip_version1.0_")}):
        dir_ = texto("39FE", f"{r}/__substg1.0_") or texto("3003", f"{r}/__substg1.0_")
        rp = flujos.get(f"{r}/__properties_version1.0", b"")
        tipo = 1
        for k in range(8, len(rp) - 15, 16):
            etq, _, v = struct.unpack_from("<IIQ", rp, k)
            if etq >> 16 == 0x0C15:
                tipo = v & 0xFFFFFFFF
        (para if tipo == 1 else copia).append(dir_.lower())
    de = (texto("5D01") or texto("0C1F") or texto("0065")).lower()
    cabeceras = texto("007D")                          # los encabezados de internet, si llegó por correo
    return {"id": texto("1035").strip(), "de": de, "para": [x for x in para if x], "copia": [x for x in copia if x],
            "asunto": texto("0037"), "fecha": fecha_, "responde_a": re.findall(r"<[^>]+>", texto("1042") + " " + texto("1039")),
            "cuerpo": texto("1000"), "cabeceras": cabeceras}


def de_msg(ruta: Path) -> str:
    m = leer_msg(ruta)
    cabeza = [f"**De:** {m['de']}", f"**Para:** {', '.join(m['para'])}",
              f"**Fecha:** {m['fecha'].isoformat() if m['fecha'] else ''}", f"**Asunto:** {m['asunto']}"]
    return "\n".join(cabeza) + "\n\n" + (m["cuerpo"] or "")


def escribir_msg(ruta: Path, *, mid: str, de: str, para: list, asunto: str, fecha, cuerpo: str, responde: str | None = None) -> None:
    """Un .msg mínimo y válido (MS-CFB versión 3, con su flujo mini): lo usan las pruebas para tener
    correos de Outlook sin depender de Outlook. Todo flujo cabe en el flujo mini (menos de 4.096 bytes)."""
    def u(x):
        return x.encode("utf-16-le")
    raiz = {"__substg1.0_0037001F": u(asunto), "__substg1.0_1000001F": u(cuerpo), "__substg1.0_1035001F": u(mid),
            "__substg1.0_0C1F001F": u(de), "__substg1.0_5D01001F": u(de), "__substg1.0_001A001F": u("IPM.Note"),
            "__substg1.0_0E04001F": u("; ".join(para))}
    if responde:
        raiz["__substg1.0_1042001F"] = u(responde)
        raiz["__substg1.0_1039001F"] = u(responde)
    ft = int((fecha - _dt.datetime(1601, 1, 1, tzinfo=_dt.timezone.utc)).total_seconds() * 10_000_000)
    raiz["__properties_version1.0"] = (struct.pack("<8xIIII8x", len(para), 0, len(para), 0)
                                       + struct.pack("<IIQ", (0x0039 << 16) | 0x0040, 2, ft)
                                       + struct.pack("<IIQ", (0x0E06 << 16) | 0x0040, 2, ft))
    nodos = [("Root Entry", 5, None), ]                # (nombre, tipo, contenido | hijos)
    arbol = {"": dict(raiz)}
    for i, d in enumerate(para):
        arbol[f"__recip_version1.0_#{i:08X}"] = {"__substg1.0_39FE001F": u(d), "__substg1.0_3001001F": u(d),
                                                  "__properties_version1.0": struct.pack("<8x") + struct.pack("<IIQ", (0x0C15 << 16) | 0x0003, 2, 1)}
    # El directorio: la raíz, sus flujos, las carpetas de destinatarios y sus flujos.
    entradas = [{"nombre": "Root Entry", "tipo": 5, "datos": b"", "hijos": []}]

    def agregar(nombre, tipo, datos=b""):
        entradas.append({"nombre": nombre, "tipo": tipo, "datos": datos, "hijos": []})
        return len(entradas) - 1
    for k, v in raiz.items():
        entradas[0]["hijos"].append(agregar(k, 2, v))
    for k, d in arbol.items():
        if not k:
            continue
        j = agregar(k, 1)
        entradas[0]["hijos"].append(j)
        for kk, vv in d.items():
            entradas[j]["hijos"].append(agregar(kk, 2, vv))
    # El flujo mini, en bloques de 64 bytes.
    mini, minifat = b"", []
    for e in entradas[1:]:
        if e["tipo"] != 2:
            continue
        n = max(1, -(-len(e["datos"]) // 64)) if e["datos"] else 0
        e["inicio"] = len(mini) // 64 if n else _FIN
        for k in range(n):
            minifat.append(len(mini) // 64 + 1 if k < n - 1 else _FIN)
            mini += e["datos"][k * 64:(k + 1) * 64].ljust(64, b"\x00")
    clave = lambda e: (len(e["nombre"]), e["nombre"].upper())  # noqa: E731

    def enlazar(hijos):
        # Hermanos en orden, cada uno a la derecha del anterior: un árbol válido de búsqueda.
        orden = sorted(hijos, key=lambda j: clave(entradas[j]))
        for a, b in zip(orden, orden[1:]):
            entradas[a]["der"] = b
        return orden[0] if orden else _LIBRE
    for e in entradas:
        e["hijo"] = enlazar(e["hijos"]) if e["hijos"] else _LIBRE
    S = 512
    sectores: list[bytes] = []

    def poner(datos):
        ini = len(sectores)
        for k in range(0, max(len(datos), 1), S):
            sectores.append(datos[k:k + S].ljust(S, b"\x00"))
        return ini, len(sectores) - ini
    mini_ini, mini_n = poner(mini)
    mf = b"".join(struct.pack("<I", x) for x in minifat) + b"\xff" * 4 * ((-len(minifat)) % (S // 4))
    mf_ini, mf_n = poner(mf)
    dirb = b""
    for i, e in enumerate(entradas):
        nb = u(e["nombre"]) + b"\x00\x00"
        es_raiz = i == 0
        dirb += (nb.ljust(64, b"\x00") + struct.pack("<HBB", len(nb), e["tipo"], 1)
                 + struct.pack("<III", e.get("izq", _LIBRE), e.get("der", _LIBRE), e["hijo"]) + b"\x00" * 36
                 + struct.pack("<IQ", mini_ini if es_raiz else e.get("inicio", 0) if e["tipo"] == 2 else 0,
                               len(mini) if es_raiz else len(e["datos"])))
    dirb += b"\x00" * ((-len(dirb)) % S)
    dir_ini, dir_n = poner(dirb)
    # La FAT: cuántos sectores ocupa ella misma depende de cuántos hay en total.
    n_fat = 1
    while (len(sectores) + n_fat) > n_fat * (S // 4):
        n_fat += 1
    fat = [_LIBRE] * (n_fat * (S // 4))
    for ini, n in ((mini_ini, mini_n), (mf_ini, mf_n), (dir_ini, dir_n)):
        for k in range(n):
            fat[ini + k] = ini + k + 1 if k < n - 1 else _FIN
    fat_ini = len(sectores)
    for k in range(n_fat):
        fat[fat_ini + k] = 0xFFFFFFFD
    for k in range(n_fat):
        sectores.append(b"".join(struct.pack("<I", x) for x in fat[k * (S // 4):(k + 1) * (S // 4)]))
    difat = [fat_ini + k for k in range(n_fat)] + [_LIBRE] * (109 - n_fat)
    cab = (bytes.fromhex("D0CF11E0A1B11AE1") + b"\x00" * 16 + struct.pack("<HHHHH", 0x3E, 3, 0xFFFE, 9, 6) + b"\x00" * 6
           + struct.pack("<IIIIIIIII", 0, n_fat, dir_ini, 0, 4096, mf_ini, mf_n, _FIN, 0)
           + struct.pack("<109I", *difat))
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    Path(ruta).write_bytes(cab + b"".join(sectores))



CONVERTIDORES = {
    ".docx": ("docx", de_docx), ".xlsx": ("xlsx", de_xlsx), ".pptx": ("pptx", de_pptx),
    ".html": ("marcado", de_marcado), ".htm": ("marcado", de_marcado),
    ".eml": ("eml", de_eml), ".msg": ("msg", de_msg),
}

SIN_SOPORTE = {
    ".doc": "Word anterior a 2007. Guárdalo como .docx y se lee.",
    ".xls": "Excel anterior a 2007. Guárdalo como .xlsx y se lee.",
    ".zip": "un contenedor: descomprímelo en la carpeta.",
}


# ---------------------------------------------------------------- correr

def convertir(docs: Path, cache: Path, solo: str | None = None, excluir: set | None = None) -> dict:
    """Convierte a texto los documentos de `docs` en `cache`. `excluir` son las rutas, relativas a
    `docs`, que no se abren: las credenciales, llaves y respaldos que el motor de la CISO deja fuera
    (CISO-4). Van al manifiesto como no convertidas, con su motivo, y no dejan copia en el caché."""
    cache.mkdir(parents=True, exist_ok=True)
    manifiesto, formatos = [], {}
    excluir = excluir or set()

    for ruta in sorted(docs.rglob("*")):
        if not ruta.is_file() or ruta.name in IGNORAR or ruta.name.startswith("."):
            continue
        rel = ruta.relative_to(docs)
        if solo and solo not in str(rel):
            continue
        ext = ruta.suffix.lower()
        formatos[ext] = formatos.get(ext, 0) + 1
        fila = {"path": str(rel), "format": ext}
        if str(rel) in excluir:
            fila.update(converter=None, ok=False, reason="excluido: no se abre")
            manifiesto.append(fila)
            continue

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
    (docs / "binario.msg").write_bytes(b"binario de outlook")
    escribir_msg(docs / "reporte.msg", mid="<r1@banco.test>", de="gerencia@banco.test", para=["pmo@banco.test"],
                 asunto="Reporte de avance", fecha=_dt.datetime(2026, 10, 20, 14, 0, tzinfo=_dt.timezone.utc),
                 cuerpo="El hito de integración se movió al 2026-12-04.", responde="<s1@banco.test>")

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
        ("documentos vistos", r["documents"], 9),
        ("convertidos", r["converted"], 7),
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
        ("msg · el cuerpo", "2026-12-04" in leer("reporte.msg"), True),
        ("msg · el asunto", "Reporte de avance" in leer("reporte.msg"), True),
        ("msg · los encabezados", (lambda m: (m["de"], m["para"], m["id"], m["responde_a"], m["fecha"].isoformat()))(leer_msg(docs / "reporte.msg")),
         ("gerencia@banco.test", ["pmo@banco.test"], "<r1@banco.test>", ["<s1@banco.test>", "<s1@banco.test>"], "2026-10-20T14:00:00+00:00")),
        ("msg · uno que no es compuesto se declara", por_ruta["binario.msg"]["ok"], False),
        ("msg · con la razón", "compuesto" in por_ruta["binario.msg"]["reason"], True),
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
