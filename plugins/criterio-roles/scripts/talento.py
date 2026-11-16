#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El motor de la familia CHRO: lo que calcula el código para Norma y Cándido.

    python3 talento.py <acción> [opciones]       python3 talento.py --help

Norma (criterio-roles) procesa los perfiles de cargo: cada perfil contra la ocupación de su estándar
—la CUOC del DANE u O*NET—, cada requisito contra las tareas del perfil, lo que la ley del país y la
política de la organización no permiten pedir, el nivel de estudios contra el nivel de competencia de
la ocupación, los perfiles que se solapan y los que pasaron su revisión. Cándido (criterio-talent),
la selección: cada afirmación de la hoja de vida contra su soporte, cada candidato contra el perfil
requisito por requisito, la autorización y la conservación de sus datos, y cada vacante contra su
plazo. Los dos comparten este motor, que vive en criterio-roles y se copia a criterio-talent con
scripts/sincronizar.py, y el núcleo común de las familias (`nucleo.py`).

**El modelo de lenguaje (LLM) extrae; este archivo calcula.** Las tablas —el estándar de ocupaciones,
el registro de vacantes, el de autorizaciones, la exportación del ATS y la base interna— las procesa
el código. Lo que solo trae un documento escrito —el perfil de cargo con sus tareas y sus requisitos,
cada hoja de vida con sus afirmaciones y sus soportes— lo extrae el agente a su ficha, con la cita, y
el código lo cruza.

**Ninguna decisión sobre una persona la toma el agente** (decisión 0031): el motor no rechaza, no
descarta, no da un puntaje y no ordena candidatos por un número. Presenta cada requisito con su
evidencia, en el orden del identificador del candidato. Lo que no se debe tratar —la fotografía, la
edad, el sexo, el estado civil, el origen, la salud— no entra al cálculo: la ficha lo registra solo
para decir que se excluyó.

**Los plazos y los requisitos los fija la organización**: el plazo de cobertura de una vacante, el
tiempo de conservación de los datos, la revisión de los perfiles, el umbral de importancia de O*NET y
la equivalencia de sus niveles de estudios salen de su política. Lo que viene de fuera es la ocupación
con sus destrezas y conocimientos, el nivel de competencia de la CUOC con su nivel de la CINE
(documento de la CUOC 2026, numeral 3.2) y los datos sensibles de la ley de cada país
(`datos_sensibles.json`).

Librería estándar, sin dependencias.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import nucleo as N  # noqa: E402
from nucleo import (  # noqa: E402
    _csv, _hoy, _xlsx, alerta, escribir_json, fecha, filas_de, iso, leer_json, marco_reporte, norm, numero,
    ordenar, registro_corridas, rel,
)

ESTRUCTURA = AQUI / "estructura.json"
SUB = {"norma": "perfiles", "candido": "seleccion"}
SENSIBLES = AQUI / "datos_sensibles.json"

# ================================================================ las tablas

class Hoja:
    """Una tabla con sus columnas canónicas, por su cabecera o por el mapeo de la configuración, y la
    fila de origen de cada dato para citarla."""

    def __init__(self, ruta: Path, requeridas: list[str], opcionales: list[str], alias: dict, columnas: dict | None = None,
                 filas: list | None = None):
        self.ruta, self.faltan, self.filas, self.mapa, self.cabecera = ruta, [], [], {}, []
        filas = filas_de(ruta) if filas is None else filas
        fijas = {k: norm(v) for k, v in (columnas or {}).items() if v}
        cand = {c: ([fijas[c]] if c in fijas else alias.get(c, [c])) for c in list(requeridas) + list(opcionales)}
        if not filas:
            self.faltan = list(requeridas)
            return
        inicio = 0
        for i, f in enumerate(filas[:15]):
            if any(set(cand[c]) & {norm(x) for x in f} for c in requeridas):
                inicio = i
                break
        self.cabecera = list(filas[inicio])
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
               columnas: dict | None, no_proc: list, que: str) -> Hoja | None:
    rutas = hallar(docs / carpeta, *patrones)
    if not rutas:
        return None
    t = Hoja(rutas[-1], requeridas, opcionales, alias, columnas)
    if t.faltan:
        no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"{que}: no trae una columna reconocible para {', '.join(t.faltan)}; "
                                                                f"di cuál es en la configuración (columns)"})
        return None
    return t


def xlsx_hojas(ruta: Path) -> dict[str, list[list[str]]]:
    """Todas las hojas de un .xlsx por su nombre —los perfiles ocupacionales de la CUOC traen una por
    componente—, con cada celda en su columna."""
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
          "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    S = "{%s}" % ns["m"]
    out: dict[str, list[list[str]]] = {}
    with zipfile.ZipFile(ruta) as z:
        nombres = z.namelist()
        compartidas = []
        if "xl/sharedStrings.xml" in nombres:
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(f"{S}si"):
                compartidas.append("".join(t.text or "" for t in si.iter(f"{S}t")))
        rels = {}
        if "xl/_rels/workbook.xml.rels" in nombres:
            for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels")):
                rels[r.get("Id")] = r.get("Target")
        libro = ET.fromstring(z.read("xl/workbook.xml"))
        for h in libro.iter(f"{S}sheet"):
            destino = rels.get(h.get("{%s}id" % ns["r"]), "")
            destino = destino.lstrip("/")
            destino = destino if destino.startswith("xl/") else "xl/" + destino
            if destino not in nombres:
                continue
            filas = []
            for fila in ET.fromstring(z.read(destino)).iter(f"{S}row"):
                celdas: dict[int, str] = {}
                for i, c in enumerate(fila.iter(f"{S}c")):
                    pos = N._col(c.get("r")) if c.get("r") else i
                    v, isx = c.find(f"{S}v"), c.find(f"{S}is")
                    if c.get("t") == "s" and v is not None and v.text is not None:
                        k = int(v.text)
                        celdas[pos] = compartidas[k] if k < len(compartidas) else ""
                    elif isx is not None:
                        celdas[pos] = "".join(t.text or "" for t in isx.iter(f"{S}t"))
                    elif v is not None:
                        celdas[pos] = v.text or ""
                if celdas:
                    filas.append([celdas.get(i, "") for i in range(max(celdas) + 1)])
            out[h.get("name")] = filas
    return out


def _limpio(v) -> str:
    return re.sub(r"\s+", " ", str(v or "").replace("_x000D_", " ")).strip()


def _cabecera(filas: list[list[str]], *columnas: str) -> tuple[int, dict]:
    """La fila de cabecera de una hoja y la posición de cada columna pedida, por su nombre."""
    for i, f in enumerate(filas[:10]):
        cab = [norm(x) for x in f]
        if all(norm(c) in cab for c in columnas):
            return i, {c: cab.index(norm(c)) for c in columnas}
    return -1, {}


# ================================================================ el estándar de ocupaciones

# La CUOC 2026 del DANE, en la descarga oficial de sus perfiles ocupacionales (F-03): una hoja por
# componente, con estos nombres de hoja y de columna. O*NET 31.0 (F-02), en su descarga en Excel: un
# archivo por componente. Los dos se leen de la descarga tal cual; aquí no se teclea una ocupación.
CUOC_HOJAS = {"ocupacion": "Ocupación", "descripcion": "Descripción", "funciones": "Funciones", "denominaciones": "Denominaciones",
              "nivel": "Nivel Competencia", "conocimientos": "Conocimientos", "destrezas": "Destrezas", "afines": "Ocupaciones Afines",
              "equivalencias": "Equivalencias"}
CUOC_CODIGO, CUOC_NOMBRE = "Código de la Ocupación", "Nombre de la Ocupación"
ONET_CODIGO, ONET_TITULO = "O*NET-SOC Code", "Title"
ONET_ARCHIVOS = {"ocupaciones": "occupation_data", "tareas": "task_statements", "zonas": "job_zones",
                 "destrezas": ("essential_skills", "transferable_skills", "skills"), "conocimientos": ("knowledge",)}

# El nivel de competencia de la CUOC y el nivel de la CINE 2011 que suele exigir (documento de la CUOC
# 2026, numeral 3.2, F-03): primer nivel, CINE 1; segundo, CINE 2 a 4; tercero, CINE 5; cuarto, CINE 6 o
# superior. La experiencia puede reemplazar la enseñanza formal (el mismo numeral).
CINE_DE_NIVEL = {1: (1, 1), 2: (2, 4), 3: (5, 5), 4: (6, 8)}


def _cuoc(ruta: Path) -> dict | None:
    hojas = xlsx_hojas(ruta)
    if not all(h in hojas for h in (CUOC_HOJAS["ocupacion"], CUOC_HOJAS["destrezas"], CUOC_HOJAS["conocimientos"], CUOC_HOJAS["nivel"])):
        return None
    ocup: dict[str, dict] = {}
    i, col = _cabecera(hojas[CUOC_HOJAS["ocupacion"]], CUOC_CODIGO, CUOC_NOMBRE)
    if i < 0:
        return None
    for f in hojas[CUOC_HOJAS["ocupacion"]][i + 1:]:
        c = _limpio(f[col[CUOC_CODIGO]] if col[CUOC_CODIGO] < len(f) else "")
        if re.fullmatch(r"\d{5}", c):
            ocup[c] = {"codigo": c, "nombre": _limpio(f[col[CUOC_NOMBRE]]), "destrezas": [], "conocimientos": [], "funciones": [],
                       "denominaciones": [], "afines": [], "nivel": None, "ciuo": None, "estandar": "cuoc"}

    def por_ocupacion(hoja: str, *cols: str):
        filas = hojas.get(hoja) or []
        k, c = _cabecera(filas, CUOC_CODIGO, *cols)
        for f in filas[k + 1:] if k >= 0 else []:
            cod = _limpio(f[c[CUOC_CODIGO]] if c[CUOC_CODIGO] < len(f) else "")
            if cod in ocup:
                yield cod, [_limpio(f[c[x]]) if c[x] < len(f) else "" for x in cols]
    for cod, (ident, nombre) in por_ocupacion(CUOC_HOJAS["destrezas"], "ID", "Nombre de la Destreza"):
        ocup[cod]["destrezas"].append({"id": f"D{ident}", "nombre": nombre, "tipo": "destreza"})
    for cod, (ident, nombre) in por_ocupacion(CUOC_HOJAS["conocimientos"], "ID", "Nombre del Conocimiento"):
        ocup[cod]["conocimientos"].append({"id": f"C{ident}", "nombre": nombre, "tipo": "conocimiento"})
    for cod, (n,) in por_ocupacion(CUOC_HOJAS["nivel"], "Nivel de Competencia"):
        ocup[cod]["nivel"] = int(n) if n.isdigit() else None
    for cod, (n,) in por_ocupacion(CUOC_HOJAS["funciones"], "Funciones de la Ocupación"):
        ocup[cod]["funciones"].append(n)
    for cod, (n,) in por_ocupacion(CUOC_HOJAS["denominaciones"], "Nombre de la Denominación"):
        ocup[cod]["denominaciones"].append(n)
    for cod, (a,) in por_ocupacion(CUOC_HOJAS["afines"], "Código de la Ocupación Afin"):
        ocup[cod]["afines"].append(a)
    for cod, (c,) in por_ocupacion(CUOC_HOJAS["equivalencias"], "Código CIUO-08"):
        ocup[cod]["ciuo"] = ocup[cod]["ciuo"] or c
    return {"estandar": "cuoc", "fuente": "F-03", "archivo": ruta, "ocupaciones": ocup}


def _onet(carpeta: Path, umbral: float | None) -> dict | None:
    archivos = {norm(p.stem): p for p in carpeta.iterdir() if p.is_file() and p.suffix.lower() in (".xlsx", ".csv", ".txt")}
    if ONET_ARCHIVOS["ocupaciones"] not in archivos:
        return None
    ocup: dict[str, dict] = {}
    filas = filas_de(archivos[ONET_ARCHIVOS["ocupaciones"]])
    i, col = _cabecera(filas, ONET_CODIGO, ONET_TITULO)
    for f in filas[i + 1:] if i >= 0 else []:
        c = _limpio(f[col[ONET_CODIGO]])
        if re.fullmatch(r"\d{2}-\d{4}\.\d{2}", c):
            ocup[c] = {"codigo": c, "nombre": _limpio(f[col[ONET_TITULO]]), "destrezas": [], "conocimientos": [], "funciones": [],
                       "denominaciones": [_limpio(f[col[ONET_TITULO]])], "afines": [], "nivel": None, "zona": None, "ciuo": None, "estandar": "onet"}
    if ONET_ARCHIVOS["tareas"] in archivos:
        filas = filas_de(archivos[ONET_ARCHIVOS["tareas"]])
        i, col = _cabecera(filas, ONET_CODIGO, "Task")
        for f in filas[i + 1:] if i >= 0 else []:
            if _limpio(f[col[ONET_CODIGO]]) in ocup:
                ocup[_limpio(f[col[ONET_CODIGO]])]["funciones"].append(_limpio(f[col["Task"]]))
    if ONET_ARCHIVOS["zonas"] in archivos:
        filas = filas_de(archivos[ONET_ARCHIVOS["zonas"]])
        i, col = _cabecera(filas, ONET_CODIGO, "Job Zone")
        for f in filas[i + 1:] if i >= 0 else []:
            c = _limpio(f[col[ONET_CODIGO]])
            if c in ocup and _limpio(f[col["Job Zone"]]).isdigit():
                ocup[c]["zona"] = int(_limpio(f[col["Job Zone"]]))
    # La importancia de cada destreza y conocimiento (escala IM, de 1 a 5): exigible la que llega al
    # umbral que fija la organización; la que O*NET recomienda suprimir no cuenta.
    for tipo, nombres in (("destrezas", ONET_ARCHIVOS["destrezas"]), ("conocimientos", ONET_ARCHIVOS["conocimientos"])):
        for n in nombres:
            if n not in archivos:
                continue
            filas = filas_de(archivos[n])
            i, col = _cabecera(filas, ONET_CODIGO, "Element ID", "Element Name", "Scale ID", "Data Value")
            sup = (norm("Recommend Suppress") in [norm(x) for x in filas[i]]) if i >= 0 else False
            js = [norm(x) for x in filas[i]].index(norm("Recommend Suppress")) if sup else None
            for f in filas[i + 1:] if i >= 0 else []:
                c = _limpio(f[col[ONET_CODIGO]])
                if c not in ocup or _limpio(f[col["Scale ID"]]) != "IM" or (js is not None and js < len(f) and _limpio(f[js]).upper() == "Y"):
                    continue
                v = numero(f[col["Data Value"]])
                if umbral is not None and v is not None and v >= umbral:
                    ocup[c][tipo].append({"id": _limpio(f[col["Element ID"]]), "nombre": _limpio(f[col["Element Name"]]),
                                          "tipo": tipo[:-1], "importancia": v})
    return {"estandar": "onet", "fuente": "F-02", "archivo": carpeta, "ocupaciones": ocup}


def estandar(cfg: dict, no_proc: list) -> dict | None:
    """El estándar de ocupaciones que eligió la organización, desde la descarga oficial que dejó en la
    carpeta de referencia."""
    docs = cfg["_docs"]
    est = cfg.get("standard") or {}
    nombre = norm(est.get("name"))
    ruta = docs / est["file"] if est.get("file") else None
    if not nombre or not ruta:
        return None
    if not ruta.exists():
        no_proc.append({"archivo": est.get("file"), "motivo": "el estándar de ocupaciones de la configuración no está en la carpeta"})
        return None
    try:
        if nombre == "cuoc":
            r = _cuoc(ruta)
        elif nombre == "onet":
            r = _onet(ruta if ruta.is_dir() else ruta.parent, numero(est.get("importance_threshold")))
        else:
            r = None
    except (zipfile.BadZipFile, KeyError, ValueError, OSError) as e:
        no_proc.append({"archivo": est.get("file"), "motivo": f"el estándar de ocupaciones no se pudo leer: {e}"})
        return None
    if not r or not r["ocupaciones"]:
        no_proc.append({"archivo": est.get("file"), "motivo": f"no es la descarga oficial de {est.get('name')}: no trae sus hojas ni sus columnas"})
        return None
    return r


def codigo_ocupacion(v, nombre: str) -> str:
    s = str(v or "").strip()
    if nombre == "cuoc":
        d = re.sub(r"\D", "", s)
        return d[:5] if len(d) >= 5 else d
    m = re.search(r"\d{2}-\d{4}(\.\d{2})?", s)
    if not m:
        return s
    return m.group(0) if m.group(1) else m.group(0) + ".00"


# ================================================================ lo que no se puede pedir

def sensibles() -> dict:
    return leer_json(SENSIBLES, {}) or {}


def patrones_prohibidos(cfg: dict) -> list[dict]:
    """Lo que un perfil no puede pedir: los datos sensibles de la ley del país de la entidad, con su
    artículo, y lo que la política de selección de la organización prohíbe pedir."""
    s = sensibles()
    pais = ((cfg.get("entity") or {}).get("country") or "").upper()
    ley = (s.get("leyes") or {}).get(pais)
    out = []
    if ley:
        for cat in ley["categorias"]:
            c = (s.get("categorias") or {}).get(cat)
            if c:
                out.append({"categoria": cat, "nombre": c["nombre"], "patron": re.compile(c["patron"], re.I),
                            "fuente": f"{ley['norma']}, {ley['articulo']} ({ley['fuente']})"})
    for t in ((cfg.get("selection") or {}).get("prohibited_requirements") or []):
        t = str(t).strip()
        if not t:
            continue
        c = (s.get("politica") or {}).get(norm(t))
        patron = c["patron"] if c else r"\b" + re.escape(norm(t)).replace("_", r"[\s_]") + r"\b"
        out.append({"categoria": norm(t), "nombre": t, "patron": re.compile(patron, re.I), "fuente": "la política de selección de la organización"})
    return out


def _texto_plano(s: str) -> str:
    import unicodedata
    return "".join(ch for ch in unicodedata.normalize("NFD", str(s or "").lower()) if unicodedata.category(ch) != "Mn")


def prohibido(texto: str, patrones: list[dict]) -> list[dict]:
    t = _texto_plano(texto)
    return [p for p in patrones if p["patron"].search(t)]


# ================================================================ la configuración

DEFECTOS = {"overlap": {"share": 0.5}, "report": {"language": "es"}}
SEVERIDAD = {
    "requirement_not_allowed": 1, "consent_missing": 1, "retention_exceeded": 1,
    "profile_without_occupation": 2, "education_level_inconsistent": 2, "claim_without_support": 2,
    "employment_dates_differ": 2, "certification_expired": 2, "vacancy_past_target": 2,
    "essential_skill_missing": 3, "requirement_without_task": 3, "profiles_overlap": 3, "profile_review_overdue": 3,
    "requirement_not_evidenced": 3, "protected_data_received": 3,
}
N.SEVERIDAD.update(SEVERIDAD)


def niveles_estudio(cfg: dict) -> dict[str, int]:
    """La equivalencia que fija la organización entre su forma de nombrar los estudios y el nivel de la
    CINE 2011 (education.levels). Sin ella, el nivel de estudios no se compara."""
    out = {}
    for k, v in ((cfg.get("education") or {}).get("levels") or {}).items():
        n = numero(v)
        if n is not None and 0 <= n <= 8:
            out[norm(k)] = int(n)
    return out


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
    est = cfg.get("standard") or {}
    if rol == "norma":
        if norm(est.get("name")) not in ("cuoc", "onet"):
            p.append("standard.name: el estándar de ocupaciones, cuoc u onet")
        if not est.get("file"):
            p.append("standard.file: la descarga oficial del estándar en la carpeta de referencia (el Excel de los perfiles ocupacionales de la CUOC, o la carpeta de O*NET)")
        if norm(est.get("name")) == "onet" and numero(est.get("importance_threshold")) is None:
            p.append("standard.importance_threshold: O*NET da la importancia de cada destreza de 1 a 5; desde qué valor es exigible lo fija la organización")
    if rol == "candido":
        sel = cfg.get("selection") or {}
        if numero((sel.get("vacancy") or {}).get("target_days")) is None:
            p.append("selection.vacancy.target_days vacío: los días que da la política de selección para cubrir una vacante")
        if numero((sel.get("data") or {}).get("retention_days")) is None:
            p.append("selection.data.retention_days vacío: los días que la política conserva los datos de un candidato que no quedó en el cargo")
    return p


def _ficha(cfg: dict, rol: str, periodo: str) -> dict:
    return leer_json(cfg["_estado"] / SUB[rol] / periodo / "ficha.json", {}) or {}


def perfiles_de(cfg: dict, periodo: str) -> tuple[list[dict], str | None]:
    """Los perfiles que dejó Norma: los del periodo o, si no hay, los del periodo anterior más cercano."""
    base = cfg["_estado"] / SUB["norma"]
    if not base.is_dir():
        return [], None
    for p in sorted((x.name for x in base.iterdir() if x.is_dir() and re.fullmatch(r"\d{4}-\d{2}", x.name) and x.name <= periodo), reverse=True):
        f = leer_json(base / p / "ficha.json", {}) or {}
        if f.get("profiles"):
            return f["profiles"], p
    return [], None


def _cita(src) -> dict | None:
    if not src:
        return None
    s = str(src)
    return {"archivo": s.split(",")[0].strip()}


def _sin_ficha(docs: Path, carpeta: str, citadas: set, aviso: str, saltar: tuple = ()) -> list[str]:
    """Los documentos de una carpeta que la ficha no cita: se le dice a quien la escribe. Una imagen
    en la carpeta de un candidato no se cita: el motor la toma por una fotografía y la excluye."""
    out = []
    citadas = {str(s).split(",")[0].strip() for s in citadas}
    base = docs / carpeta
    for p in sorted(x for x in base.rglob("*") if x.is_file() and not x.name.startswith(".")) if base.is_dir() else []:
        if p.suffix.lower() in (".csv", ".xlsx") + tuple(saltar):
            continue
        if rel(p, docs) not in citadas:
            out.append(f"{rel(p, docs)} no está en la ficha: {aviso}")
    return out


# ================================================================ Norma · los perfiles de cargo

def revisar_ficha_norma(f: dict) -> list[str]:
    p = []
    vistos = set()
    for i, x in enumerate(f.get("profiles") or []):
        for c in ("id", "title", "source"):
            if not x.get(c):
                p.append(f"profiles[{i}]: falta {c}")
        if x.get("id") in vistos:
            p.append(f"profiles[{i}]: el identificador {x.get('id')} está repetido")
        vistos.add(x.get("id"))
        tareas = {t.get("id") for t in x.get("tasks") or []}
        for j, r in enumerate(x.get("requirements") or []):
            if not r.get("id") or not r.get("text"):
                p.append(f"profiles[{i}].requirements[{j}]: lleva id y text")
            for t in r.get("tasks") or []:
                if t not in tareas:
                    p.append(f"profiles[{i}].requirements[{j}]: la tarea {t} no está entre las tareas del perfil")
        for c in ("next_review", "last_review"):
            if x.get(c) and not fecha(x.get(c)):
                p.append(f"profiles[{i}]: {c} «{x.get(c)}» no es una fecha")
    for i, q in enumerate(f.get("questions") or []):
        if not (q.get("question") and q.get("answer")):
            p.append(f"questions[{i}]: lleva question y answer")
    return p


def _palabras(s: str) -> set[str]:
    vacias = {"de", "la", "el", "los", "las", "y", "en", "con", "para", "por", "del", "a", "o", "un", "una", "e", "al", "sus", "su",
              "the", "and", "of", "to", "in", "for", "with", "da", "do", "das", "dos", "em", "com"}
    return {w for w in re.findall(r"[a-z0-9]+", _texto_plano(s)) if len(w) > 2 and w not in vacias}


def _cubre(req: dict, elemento: dict) -> bool:
    """Un requisito cubre una destreza o un conocimiento del estándar si el agente lo ató a ella
    (`element`, por su identificador o su nombre) o si lo nombra igual."""
    e = norm(req.get("element"))
    if e and e in (norm(elemento["id"]), norm(elemento["nombre"])):
        return True
    return norm(elemento["nombre"]) in norm(req.get("text"))


def norma(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _pais(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "norma", periodo)
    problemas = revisar_ficha_norma(ficha)
    al: list[dict] = []
    no_proc: list[dict] = []
    est = estandar(cfg, no_proc)
    nombre_est = norm((cfg.get("standard") or {}).get("name"))
    prohib = patrones_prohibidos(cfg)
    niveles = niveles_estudio(cfg)
    meses = numero((cfg.get("profiles") or {}).get("review_months"))
    citadas = {str(x.get("source")) for x in ficha.get("profiles") or []} | {str(s) for s in ficha.get("reviewed") or []}
    problemas += _sin_ficha(docs, "10-perfiles", citadas, "es un perfil de cargo; corre roles-scan")
    if not (cfg.get("standard") or {}).get("file"):
        no_proc.append({"archivo": "00-referencia", "motivo": "sin el estándar de ocupaciones en la configuración, ningún perfil se compara con su ocupación"})

    perfiles = []
    for x in ficha.get("profiles") or []:
        pid, cita = x.get("id"), _cita(x.get("source"))
        nom = f"{pid} · {x.get('title')}"
        occ = x.get("occupation") or {}
        codigo = codigo_ocupacion(occ.get("code"), nombre_est) if occ.get("code") else ""
        o = (est or {}).get("ocupaciones", {}).get(codigo) if est else None
        reqs = x.get("requirements") or []
        tareas = {t.get("id") for t in x.get("tasks") or []}
        fila = {"id": pid, "titulo": x.get("title"), "ocupacion": codigo or None, "ocupacion_nombre": o["nombre"] if o else None,
                "requisitos": len(reqs), "tareas": len(tareas), "nivel": o.get("nivel") if o else None,
                "estudios": (x.get("education") or {}).get("label"), "faltan": [], "fuera": [], "revision": None,
                "elementos": [], "fuente": x.get("source")}
        # 1 · La ocupación.
        if not codigo:
            al.append(alerta("profile_without_occupation", f"{nom}: el perfil no tiene un código de ocupación que lo ate a un estándar", cita,
                             clave=f"ocupacion:{pid}"))
        elif est and not o:
            al.append(alerta("profile_without_occupation", f"{nom}: el código {codigo} no está en {est['estandar'].upper()}", cita,
                             clave=f"ocupacion:{pid}"))
        # 2 · Las destrezas y los conocimientos de la ocupación que el perfil no recoge.
        if o:
            na = {norm(n.get("element")) for n in x.get("not_applicable") or [] if n.get("reason")}
            for e in o["destrezas"] + o["conocimientos"]:
                cubierto = any(_cubre(r, e) for r in reqs)
                fila["elementos"].append({"id": e["id"], "nombre": e["nombre"], "tipo": e["tipo"], "cubierto": cubierto,
                                          "no_aplica": norm(e["nombre"]) in na or norm(e["id"]) in na})
                if not cubierto and norm(e["nombre"]) not in na and norm(e["id"]) not in na:
                    fila["faltan"].append(e["nombre"])
                    al.append(alerta("essential_skill_missing", f"{nom}: «{e['nombre']}» ({e['tipo']} de la ocupación {codigo} en "
                                     f"{est['estandar'].upper()}) no está en el perfil, ni el perfil dice por qué no aplica", cita,
                                     clave=f"elemento:{pid}:{norm(e['id'])}"))
        # 3 · Los requisitos sin tarea.
        for r in reqs:
            if not [t for t in r.get("tasks") or [] if t in tareas]:
                al.append(alerta("requirement_without_task", f"{nom}: el requisito {r.get('id')} «{r.get('text')}» no se apoya en ninguna tarea del perfil",
                                 _cita(r.get("source")) or cita, clave=f"tarea:{pid}:{r.get('id')}"))
        # 4 · Lo que no se puede pedir.
        for r in reqs:
            for pr in prohibido(r.get("text"), prohib):
                fila["fuera"].append(r.get("id"))
                al.append(alerta("requirement_not_allowed", f"{nom}: el requisito {r.get('id')} «{r.get('text')}» pide {pr['nombre'].lower()}, "
                                 f"que no se puede pedir según {pr['fuente']}", _cita(r.get("source")) or cita,
                                 clave=f"prohibido:{pid}:{r.get('id')}:{pr['categoria']}"))
        # 5 · El nivel de estudios contra el nivel de competencia de la ocupación (CUOC).
        ed = x.get("education") or {}
        if o and est["estandar"] == "cuoc" and o.get("nivel") in CINE_DE_NIVEL and ed.get("label"):
            pedido = niveles.get(norm(ed["label"]))
            lo, hi = CINE_DE_NIVEL[o["nivel"]]
            if pedido is None:
                no_proc.append({"archivo": x.get("source") or pid, "motivo": f"{pid}: el nivel de estudios «{ed['label']}» no está en la equivalencia de la "
                                f"organización (education.levels); sin ella no se compara con el nivel de competencia de la ocupación"})
            elif pedido > hi or (pedido < lo and not x.get("experience_alternative")):
                sentido = "más" if pedido > hi else "menos"
                al.append(alerta("education_level_inconsistent", f"{nom}: pide «{ed['label']}» (CINE {pedido}); la ocupación {codigo} es de nivel de "
                                 f"competencia {o['nivel']}, que suele exigir CINE {lo}{'' if lo == hi else ' a ' + str(hi)} (CUOC 2026, numeral 3.2): "
                                 f"pide {sentido} de lo que la ocupación exige", _cita(ed.get("source")) or cita, clave=f"estudios:{pid}"))
        # 7 · La revisión del perfil.
        prox = fecha(x.get("next_review"))
        if not prox and fecha(x.get("last_review")) and meses:
            u = fecha(x.get("last_review"))
            m = u.month - 1 + int(meses)
            prox = dt.date(u.year + m // 12, m % 12 + 1, min(u.day, 28))
        fila["revision"] = iso(prox)
        if prox and prox < hoy:
            al.append(alerta("profile_review_overdue", f"{nom}: tocaba revisarlo el {iso(prox)}", cita, dias=(hoy - prox).days, clave=f"revision:{pid}"))
        perfiles.append(fila)

    # 6 · Los perfiles que se solapan: la misma ocupación y la mayor parte de los requisitos.
    umbral = numero((cfg.get("overlap") or {}).get("share"))
    umbral = DEFECTOS["overlap"]["share"] if umbral is None else umbral
    pf = ficha.get("profiles") or []
    solapes = []
    for i in range(len(pf)):
        for j in range(i + 1, len(pf)):
            a, b = pf[i], pf[j]
            ca = codigo_ocupacion((a.get("occupation") or {}).get("code"), nombre_est)
            cb = codigo_ocupacion((b.get("occupation") or {}).get("code"), nombre_est)
            if not ca or ca != cb:
                continue
            ra = {frozenset(_palabras(r.get("text"))) for r in a.get("requirements") or []}
            rb = {frozenset(_palabras(r.get("text"))) for r in b.get("requirements") or []}
            if not ra or not rb:
                continue
            comun = len(ra & rb) / min(len(ra), len(rb))
            if comun > umbral:
                solapes.append({"a": a.get("id"), "b": b.get("id"), "ocupacion": ca, "comun": round(comun, 2)})
                al.append(alerta("profiles_overlap", f"{a.get('id')} · {a.get('title')} y {b.get('id')} · {b.get('title')}: la misma ocupación {ca} y "
                                 f"{round(comun * 100)} % de los requisitos en común", [_cita(a.get("source")), _cita(b.get("source"))],
                                 clave=f"solape:{a.get('id')}:{b.get('id')}"))
    # Las ocupaciones del estándar que la organización no tiene perfiladas, entre las afines a las suyas.
    sin_perfil = []
    if est:
        tiene = {p["ocupacion"] for p in perfiles if p["ocupacion"]}
        for c in sorted(tiene):
            o = est["ocupaciones"].get(c)
            for af in (o or {}).get("afines") or []:
                if af not in tiene and af in est["ocupaciones"] and af not in [s["codigo"] for s in sin_perfil]:
                    sin_perfil.append({"codigo": af, "nombre": est["ocupaciones"][af]["nombre"], "afin_a": c})

    fuentes = [est["fuente"]] if est else []
    ley = (sensibles().get("leyes") or {}).get(((cfg.get("entity") or {}).get("country") or "").upper())
    if ley and any(a["signal"] == "requirement_not_allowed" for a in al):
        fuentes.append(ley["fuente"])
    partes = {
        "roles-scan": {"perfiles": len(perfiles), "estandar": est["estandar"] if est else None,
                       "ocupaciones": len(est["ocupaciones"]) if est else 0, "fuentes": fuentes},
        "profile-check": {"perfiles": perfiles, "fuentes": fuentes},
        "profile-language": {"perfiles": [{"id": p["id"], "titulo": p["titulo"], "fuera": p["fuera"]} for p in perfiles],
                             "reglas": [{"nombre": p["nombre"], "fuente": p["fuente"]} for p in prohib], "fuentes": [ley["fuente"]] if ley else []},
        "profile-map": {"perfiles": perfiles, "solapes": solapes, "sin_perfil": sin_perfil[:30], "fuentes": fuentes},
        "profile-build": {"estandar": est["estandar"] if est else None, "fuentes": fuentes},
    }
    vence = sorted(({"fecha": p["revision"], "que": f"{p['id']} · revisión del perfil", "caso": p["id"], "estado": "pendiente", "comando": "profile-check"}
                    for p in perfiles if p["revision"] and 0 <= (fecha(p["revision"]) - hoy).days <= 30), key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "norma", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence}


def ocupacion(cfg: dict, codigo: str) -> dict:
    """Una ocupación del estándar, para armar un perfil nuevo (profile-build): su descripción, sus
    funciones, sus destrezas y conocimientos y su nivel. El agente propone; la persona decide."""
    no_proc: list = []
    est = estandar(cfg, no_proc)
    if not est:
        return {"ok": False, "motivo": (no_proc[0]["motivo"] if no_proc else "falta el estándar de ocupaciones en la configuración")}
    c = codigo_ocupacion(codigo, est["estandar"])
    o = est["ocupaciones"].get(c)
    if not o:
        return {"ok": False, "motivo": f"el código {c} no está en {est['estandar'].upper()}"}
    out = {"ok": True, "estandar": est["estandar"], "fuente": est["fuente"], **{k: v for k, v in o.items() if k != "estandar"}}
    if est["estandar"] == "cuoc" and o.get("nivel") in CINE_DE_NIVEL:
        out["cine"] = list(CINE_DE_NIVEL[o["nivel"]])
    return out


# ================================================================ Cándido · la selección

ALIAS_VACANTES = {"vacante": ["vacante", "id", "codigo", "id_vacante", "requisicion", "vacancy", "job_id", "requisition_id"],
                  "perfil": ["perfil", "id_perfil", "perfil_de_cargo", "cargo", "profile", "job_profile"],
                  "apertura": ["apertura", "fecha_apertura", "abierta_el", "fecha_de_apertura", "opened", "open_date", "posted_date"],
                  "cierre": ["cierre", "fecha_cierre", "cubierta_el", "fecha_de_cierre", "closed", "close_date", "filled_date"],
                  "estado": ["estado", "status"], "plazo_dias": ["plazo_dias", "plazo", "dias_objetivo", "target_days"],
                  "responsable": ["responsable", "reclutador", "recruiter", "owner"]}
ALIAS_AUTORIZACIONES = {"candidato": ["candidato", "id_candidato", "titular", "candidate", "candidate_id", "id"],
                        "fecha": ["fecha", "fecha_autorizacion", "otorgada_el", "date", "consent_date"],
                        "finalidad": ["finalidad", "proposito", "purpose"], "fuente": ["fuente", "soporte", "documento", "source"]}
ALIAS_ATS = {"candidato": ["candidato", "id_candidato", "candidate", "candidate_id", "id"],
             "vacante": ["vacante", "id_vacante", "requisicion", "vacancy", "job_id", "requisition_id"],
             "fecha": ["fecha", "fecha_postulacion", "postulacion", "aplicacion", "applied", "application_date", "applied_date"],
             "estado": ["estado", "etapa", "status", "stage"],
             "fecha_estado": ["fecha_estado", "ultima_actividad", "actualizado", "last_activity", "status_date", "updated"]}
ALIAS_BASE = {"persona": ["persona", "id", "id_persona", "colaborador", "candidato", "person_id"],
              "ocupacion": ["ocupacion", "codigo_ocupacion", "cuoc", "occupation", "onet_soc"],
              "cargo": ["cargo", "cargo_actual", "title", "job_title"], "area": ["area", "dependencia", "department"]}
TERMINADO = ("no_seleccionado", "rechazado", "descartado", "retirado", "desistio", "cerrado", "declinado", "not_selected", "rejected",
             "withdrawn", "closed", "declined")
CONTRATADO = ("contratado", "seleccionado", "vinculado", "ingreso", "hired", "selected")
IMAGEN = (".jpg", ".jpeg", ".png", ".heic", ".webp", ".gif", ".bmp")
# Lo que llega de un candidato y no se trata: la ficha registra solo su tipo, de esta lista, y dónde.
PROTEGIDOS = ("fotografia", "edad", "fecha_de_nacimiento", "sexo", "estado_civil", "origen", "religion", "salud",
              "documento_de_identidad")


def revisar_ficha_candido(f: dict) -> list[str]:
    p = []
    for i, c in enumerate(f.get("candidates") or []):
        for k in ("id", "vacancy"):
            if not c.get(k):
                p.append(f"candidates[{i}]: falta {k}")
        for j, k in enumerate(c.get("claims") or []):
            if k.get("type") not in ("titulo", "certificacion", "empleo"):
                p.append(f"candidates[{i}].claims[{j}]: type es titulo, certificacion o empleo")
            for d in ("from", "to", "support_from", "support_to", "expires"):
                if k.get(d) and not _mes(k.get(d)):
                    p.append(f"candidates[{i}].claims[{j}]: {d} «{k.get(d)}» no es una fecha")
        for j, e in enumerate(c.get("evidence") or []):
            if not (e.get("requirement") and e.get("source")):
                p.append(f"candidates[{i}].evidence[{j}]: lleva requirement y source")
        # Lo que no se debe tratar no lleva su valor: solo qué tipo de dato llegó y dónde.
        for j, x in enumerate(c.get("protected") or []):
            if set(x) - {"type", "source"}:
                p.append(f"candidates[{i}].protected[{j}]: solo type y source; el dato no se copia a la ficha")
            if norm(x.get("type")) not in PROTEGIDOS:
                p.append(f"candidates[{i}].protected[{j}]: el tipo «{x.get('type')}» no es uno de {', '.join(PROTEGIDOS)}")
    for i, q in enumerate(f.get("questions") or []):
        if not (q.get("question") and q.get("answer")):
            p.append(f"questions[{i}]: lleva question y answer")
    return p


def _mes(v) -> tuple[int, int] | None:
    """Una fecha al mes: la hoja de vida dice «marzo de 2019» y el certificado, el día."""
    d = fecha(v)
    if d:
        return (d.year, d.month)
    m = re.fullmatch(r"\s*(\d{4})[-/](\d{1,2})\s*", str(v or ""))
    if m and 1 <= int(m[2]) <= 12:
        return (int(m[1]), int(m[2]))
    m = re.fullmatch(r"\s*(\d{1,2})[-/](\d{4})\s*", str(v or ""))
    if m and 1 <= int(m[1]) <= 12:
        return (int(m[2]), int(m[1]))
    return None


def _nmes(m: tuple[int, int] | None) -> str:
    return f"{m[0]}-{m[1]:02d}" if m else "—"


def candido(cfg: dict, periodo: str, hoy: dt.date) -> dict:
    _pais(cfg)
    docs = cfg["_docs"]
    ficha = _ficha(cfg, "candido", periodo)
    problemas = revisar_ficha_candido(ficha)
    al: list[dict] = []
    no_proc: list[dict] = []
    cols = cfg.get("columns") or {}
    sel = cfg.get("selection") or {}
    perfiles, de_periodo = perfiles_de(cfg, periodo)
    perfil = {p.get("id"): p for p in perfiles}
    citadas = {str(k.get(c)) for x in ficha.get("candidates") or [] for k in x.get("claims") or [] for c in ("cv_source", "support")}
    citadas |= {str(x.get("cv")) for x in ficha.get("candidates") or []} | {str(e.get("source")) for x in ficha.get("candidates") or [] for e in x.get("evidence") or []}
    citadas |= {str(x.get("source")) for c in ficha.get("candidates") or [] for x in c.get("protected") or []}
    problemas += _sin_ficha(docs, "30-candidatos", citadas, "es una hoja de vida o un soporte; corre talent-scan", IMAGEN)

    # Las vacantes.
    vacantes = []
    t = leer_tabla(docs, "20-vacantes", ("vacantes", "requisiciones", "vacancies"), ["vacante", "apertura"],
                   ["perfil", "cierre", "estado", "plazo_dias", "responsable"], ALIAS_VACANTES, cols.get("vacancies"), no_proc, "el registro de vacantes")
    objetivo = numero((sel.get("vacancy") or {}).get("target_days"))
    for x in t.filas if t else []:
        ab, ci = fecha(x["apertura"]), fecha(x.get("cierre"))
        plazo = numero(x.get("plazo_dias")) or objetivo
        tope = ab + dt.timedelta(days=int(plazo)) if ab and plazo else None
        v = {"vacante": x["vacante"], "perfil": x.get("perfil") or "", "apertura": iso(ab), "cierre": iso(ci), "estado": x.get("estado") or "",
             "plazo": int(plazo) if plazo else None, "tope": iso(tope), "responsable": x.get("responsable") or "",
             "dias_abierta": ((ci or hoy) - ab).days if ab else None}
        vacantes.append(v)
        if ab and not ci and tope and tope < hoy:
            al.append(alerta("vacancy_past_target", f"{x['vacante']}{' · ' + x['perfil'] if x.get('perfil') else ''}: abierta desde el {iso(ab)}; "
                             f"la política da {int(plazo)} días y el plazo venció el {iso(tope)}", t.cita(x, docs),
                             responsable=x.get("responsable") or None, dias=(hoy - tope).days, clave=f"vacante:{norm(x['vacante'])}"))
        if x.get("perfil") and perfiles and x["perfil"] not in perfil:
            no_proc.append({"archivo": rel(t.ruta, docs), "motivo": f"fila {x['_fila']}: el perfil {x['perfil']} de la vacante {x['vacante']} no está entre los que procesó Norma"})
    vac = {v["vacante"]: v for v in vacantes}

    # Las autorizaciones y la exportación del ATS.
    autoriz: dict[str, dict] = {}
    ta = leer_tabla(docs, "40-autorizaciones", ("autorizaciones", "consentimientos", "consents"), ["candidato", "fecha"],
                    ["finalidad", "fuente"], ALIAS_AUTORIZACIONES, cols.get("authorizations"), no_proc, "el registro de autorizaciones")
    for x in ta.filas if ta else []:
        d = fecha(x["fecha"])
        if d and (x["candidato"] not in autoriz or d < autoriz[x["candidato"]]["fecha"]):
            autoriz[x["candidato"]] = {"fecha": d, "cita": ta.cita(x, docs), "finalidad": x.get("finalidad") or ""}
    ats: dict[str, dict] = {}
    tt = leer_tabla(docs, "50-ats", ("ats", "postulaciones", "candidatos", "applications"), ["candidato", "vacante"],
                    ["fecha", "estado", "fecha_estado"], ALIAS_ATS, cols.get("ats"), no_proc, "la exportación del ATS")
    for x in tt.filas if tt else []:
        ats[x["candidato"]] = {"vacante": x["vacante"], "fecha": fecha(x.get("fecha")), "estado": x.get("estado") or "",
                               "fecha_estado": fecha(x.get("fecha_estado")), "cita": tt.cita(x, docs)}

    candidatos = []
    conserva = numero((sel.get("data") or {}).get("retention_days"))
    sin_perfil = set()
    for c in sorted(ficha.get("candidates") or [], key=lambda c: str(c.get("id"))):
        cid, vid = c.get("id"), c.get("vacancy")
        v = vac.get(vid) or {}
        p = perfil.get(v.get("perfil")) or perfil.get(c.get("profile"))
        a = ats.get(cid) or {}
        recibido = fecha(c.get("received")) or a.get("fecha") or fecha(v.get("apertura"))
        cv = _cita(c.get("cv")) or _cita(c.get("folder"))
        # 1 · Las afirmaciones sin soporte, las fechas que no coinciden y las certificaciones vencidas.
        reqs = {r.get("id"): r for r in (p or {}).get("requirements") or []}
        for k in c.get("claims") or []:
            que = f"{cid}: {({'titulo': 'el título', 'certificacion': 'la certificación', 'empleo': 'el empleo'}).get(k.get('type'), 'la afirmación')} «{k.get('text')}»"
            sop = k.get("support")
            if not sop or not (docs / str(sop).split(",")[0].strip()).is_file():
                al.append(alerta("claim_without_support", f"{que} no tiene el documento que lo soporte", _cita(k.get("cv_source")) or cv,
                                 clave=f"soporte:{cid}:{k.get('id')}"))
                continue
            if k.get("type") == "empleo" and (k.get("support_from") or k.get("support_to")):
                dif = [(n, _mes(k.get(a1)), _mes(k.get(b1))) for n, a1, b1 in (("ingreso", "from", "support_from"), ("retiro", "to", "support_to"))
                       if _mes(k.get(b1)) and _mes(k.get(a1)) and _mes(k.get(a1)) != _mes(k.get(b1))]
                if dif:
                    al.append(alerta("employment_dates_differ", f"{que}: " + "; ".join(f"{n} {_nmes(h)} en la hoja de vida y {_nmes(s)} en el certificado"
                                                                                 for n, h, s in dif),
                                     [_cita(k.get("cv_source")) or cv, _cita(sop)], clave=f"fechas:{cid}:{k.get('id')}"))
            if k.get("type") == "certificacion" and k.get("expires"):
                r = reqs.get(k.get("requirement"))
                ve = fecha(k.get("expires"))
                if r and ve and recibido and ve < recibido:
                    al.append(alerta("certification_expired", f"{que}: el perfil la exige ({r.get('id')}) y venció el {iso(ve)}, antes de la postulación "
                                     f"del {iso(recibido)}", [_cita(sop)], clave=f"certificacion:{cid}:{k.get('id')}"))
        # 2 · Cada requisito del perfil con su evidencia.
        evid: dict[str, list] = {}
        for e in c.get("evidence") or []:
            evid.setdefault(e.get("requirement"), []).append(e)
        # Una afirmación atada a un requisito es evidencia de la hoja de vida; con su soporte, evidencia soportada.
        for k in c.get("claims") or []:
            if not k.get("requirement"):
                continue
            if k.get("support") and (docs / str(k["support"]).split(",")[0].strip()).is_file():
                evid.setdefault(k["requirement"], []).append({"requirement": k["requirement"], "source": k["support"], "soporte": True})
            elif k.get("cv_source"):
                evid.setdefault(k["requirement"], []).append({"requirement": k["requirement"], "source": k["cv_source"]})
        fit = []
        if p:
            for r in p.get("requirements") or []:
                ev = evid.get(r.get("id")) or []
                fit.append({"requisito": r.get("id"), "texto": r.get("text"), "esencial": bool(r.get("essential")), "evidencias": len(ev),
                            "soportado": any(e.get("soporte") for e in ev), "citas": sorted({str(e.get("source")) for e in ev})})
                if r.get("essential") and not ev:
                    al.append(alerta("requirement_not_evidenced", f"{cid}: el requisito esencial {r.get('id')} «{r.get('text')}» del perfil {p.get('id')} "
                                     f"no tiene evidencia ni en la hoja de vida ni en sus soportes", cv, clave=f"requisito:{cid}:{r.get('id')}"))
        elif vid:
            sin_perfil.add(vid)
        # 3 · Lo que llegó y no se debe tratar: se excluye, y se dice.
        prot = {(norm(x.get("type")), str(x.get("source") or "")) for x in c.get("protected") or []}
        carpeta = docs / str(c.get("folder") or "")
        if c.get("folder") and carpeta.is_dir():
            # Una imagen que la ficha cita como soporte —un diploma escaneado— es un soporte; la que no, se
            # toma por una fotografía y se excluye.
            soportes = {str(k.get("support") or "").split(",")[0].strip() for k in c.get("claims") or []} | \
                       {str(e.get("source") or "").split(",")[0].strip() for e in c.get("evidence") or []}
            for f in sorted(carpeta.rglob("*")):
                if f.is_file() and f.suffix.lower() in IMAGEN and rel(f, docs) not in soportes:
                    prot.add(("fotografia", rel(f, docs)))
        tipos = sorted({t for t, _ in prot})
        for tp in tipos:
            fuentes = sorted({s for t, s in prot if t == tp and s})
            al.append(alerta("protected_data_received", f"{cid}: llegó {tp.replace('_', ' ')}; se excluye del análisis y no se usa para nada",
                             [_cita(s) for s in fuentes] or cv, clave=f"protegido:{cid}:{tp}"))
        # 4 · La autorización y la conservación de los datos.
        au = autoriz.get(cid)
        if not au:
            al.append(alerta("consent_missing", f"{cid}: no está en el registro de autorizaciones de tratamiento de datos", cv, clave=f"autorizacion:{cid}"))
        elif recibido and au["fecha"] > recibido:
            al.append(alerta("consent_missing", f"{cid}: la autorización es del {iso(au['fecha'])}, después de recibir sus datos el {iso(recibido)}",
                             [au["cita"], cv], clave=f"autorizacion:{cid}"))
        est_c = norm(a.get("estado"))
        fin = None
        if est_c.startswith(TERMINADO):
            fin = a.get("fecha_estado") or fecha(v.get("cierre"))
        elif fecha(v.get("cierre")) and not est_c.startswith(CONTRATADO):
            fin = fecha(v.get("cierre"))
        guarda = (fin + dt.timedelta(days=int(conserva))) if fin and conserva is not None else None
        if guarda and guarda < hoy and c.get("folder") and carpeta.is_dir():
            al.append(alerta("retention_exceeded", f"{cid}: su proceso terminó el {iso(fin)}; la política conserva los datos {int(conserva)} días, hasta el "
                             f"{iso(guarda)}, y siguen en la carpeta", [a.get("cita"), cv] if a.get("cita") else cv,
                             dias=(hoy - guarda).days, clave=f"conservacion:{cid}"))
        candidatos.append({"id": cid, "vacante": vid, "perfil": (p or {}).get("id"), "recibido": iso(recibido), "estado": a.get("estado") or "",
                           "autorizacion": iso(au["fecha"]) if au else None, "conservar_hasta": iso(guarda), "requisitos": fit,
                           "afirmaciones": len(c.get("claims") or []), "excluido": tipos})
    for vid in sorted(sin_perfil):
        no_proc.append({"archivo": "20-vacantes", "motivo": f"la vacante {vid} no tiene un perfil procesado por Norma: sus candidatos no se contrastan requisito por requisito"})

    partes = {
        "talent-scan": {"candidatos": len(candidatos), "vacantes": len(vacantes), "perfiles": len(perfiles), "perfiles_de": de_periodo},
        "cv-check": {"candidatos": candidatos},
        "candidate-fit": {"candidatos": candidatos, "perfiles": {k: {"titulo": v.get("title")} for k, v in perfil.items()}},
        "privacy-check": {"candidatos": candidatos, "conserva_dias": int(conserva) if conserva is not None else None},
        "vacancy-status": {"vacantes": vacantes},
        "talent-search": {"vacantes": vacantes},
    }
    vence = sorted(({"fecha": v["tope"], "que": f"{v['vacante']} · plazo de cobertura", "caso": v["vacante"], "estado": "pendiente",
                     "comando": "vacancy-status"} for v in vacantes if v["tope"] and not v["cierre"] and 0 <= (fecha(v["tope"]) - hoy).days <= 30),
                   key=lambda v: (v["fecha"], v["que"]))
    vence += sorted(({"fecha": c["conservar_hasta"], "que": f"{c['id']} · fin de la conservación", "caso": c["id"], "estado": "pendiente",
                      "comando": "privacy-check"} for c in candidatos if c["conservar_hasta"] and 0 <= (fecha(c["conservar_hasta"]) - hoy).days <= 30),
                    key=lambda v: (v["fecha"], v["que"]))
    return {"agente": "candido", "entidad": cfg.get("entity"), "periodo": periodo, "corte": iso(hoy), "hoy": iso(hoy),
            "partes": partes, "alertas": ordenar(al), "no_procesado": no_proc, "record_issues": problemas,
            "preguntas": ficha.get("questions") or [], "vence": vence}


def busqueda(cfg: dict, vacante: str, periodo: str) -> dict:
    """La búsqueda de una vacante (talent-search): las cadenas para el buscador de quien recluta, desde
    las denominaciones de la ocupación en el estándar y los requisitos esenciales del perfil, y las
    personas de la base interna con la misma ocupación o una afín. Sin orden por ningún número: por su
    identificador. El agente no busca a nadie fuera de lo que la organización le entrega."""
    docs = cfg["_docs"]
    no_proc: list = []
    perfiles, _ = perfiles_de(cfg, periodo)
    t = leer_tabla(docs, "20-vacantes", ("vacantes", "requisiciones", "vacancies"), ["vacante", "apertura"], ["perfil"], ALIAS_VACANTES,
                   (cfg.get("columns") or {}).get("vacancies"), no_proc, "el registro de vacantes")
    fila = next((x for x in (t.filas if t else []) if norm(x["vacante"]) == norm(vacante)), None)
    if not fila:
        return {"ok": False, "motivo": f"la vacante {vacante} no está en el registro de vacantes", "no_procesado": no_proc}
    p = next((x for x in perfiles if x.get("id") == fila.get("perfil")), None)
    if not p:
        return {"ok": False, "motivo": f"el perfil {fila.get('perfil')} no está entre los que procesó Norma", "no_procesado": no_proc}
    est = estandar(cfg, no_proc)
    nombre = est["estandar"] if est else norm((cfg.get("standard") or {}).get("name"))
    cod = codigo_ocupacion((p.get("occupation") or {}).get("code"), nombre)
    o = (est or {}).get("ocupaciones", {}).get(cod) if est else None
    titulos = []
    for d in ([p.get("title")] + (o["denominaciones"] if o else []))[:12]:
        for parte in str(d or "").split(" / "):
            parte = parte.strip()
            if parte and parte not in titulos:
                titulos.append(parte)
    esenciales = [r.get("text") for r in p.get("requirements") or [] if r.get("essential")]
    cadena = "(" + " OR ".join(f'"{x}"' for x in titulos) + ")"
    terminos = [r for r in esenciales if r and len(r) <= 60]
    if terminos:
        cadena += " AND (" + " OR ".join(f'"{x}"' for x in terminos[:6]) + ")"
    afines = set((o or {}).get("afines") or [])
    internos = []
    tb = leer_tabla(docs, "50-ats", ("base_interna", "base_de_talento", "talento_interno", "internal"), ["persona"], ["ocupacion", "cargo", "area"],
                    ALIAS_BASE, (cfg.get("columns") or {}).get("internal"), no_proc, "la base de talento interna")
    for x in tb.filas if tb else []:
        c = codigo_ocupacion(x.get("ocupacion"), nombre)
        if c and (c == cod or c in afines):
            internos.append({"persona": x["persona"], "ocupacion": c, "misma": c == cod, "cargo": x.get("cargo") or "", "cita": tb.cita(x, docs)})
    internos.sort(key=lambda x: str(x["persona"]))
    return {"ok": True, "vacante": fila["vacante"], "perfil": p.get("id"), "ocupacion": cod, "titulos": titulos, "cadena": cadena,
            "esenciales": esenciales, "internos": internos, "no_procesado": no_proc,
            "nota": "Las cadenas las corre quien recluta, en su buscador. El agente no entra a ninguna red ni busca a nadie fuera de lo que la organización entrega."}


def _pais(cfg: dict) -> None:
    N._PAIS[0] = N.pais_de(cfg)


# ================================================================ la prueba de sesgo

def sin_identidad(r: dict, pares: dict[str, str]) -> dict:
    """Lo que el motor entrega de un candidato, sin su identificador y sin el aviso de lo que se excluyó:
    los dos miembros de un par de la prueba de sesgo tienen que dar exactamente esto mismo."""
    out = {}
    for c in r["partes"]["candidate-fit"]["candidatos"]:
        if c["id"] not in pares:
            continue
        al = sorted((a["signal"], re.sub(re.escape(c["id"]), "<C>", a["detail"]))
                    for a in r["alertas"] if a["signal"] != "protected_data_received" and str(a["key"]).split(":")[1:2] == [c["id"]])
        datos = json.loads(json.dumps({k: v for k, v in c.items() if k not in ("id", "excluido")}, ensure_ascii=False).replace(c["id"], "<C>"))
        out[pares[c["id"]]] = {"senales": al, "datos": datos}
    return out


def sesgo(r: dict, pares: list[tuple[str, str]]) -> list[str]:
    """Las diferencias entre los dos miembros de cada par: cualquiera es un defecto que bloquea la versión."""
    fallas = []
    for a, b in pares:
        x = sin_identidad(r, {a: "par", b: "par2"})
        if x.get("par") != x.get("par2"):
            fallas.append(f"{a} y {b} no dan lo mismo: {json.dumps(x.get('par'), ensure_ascii=False)[:300]} · {json.dumps(x.get('par2'), ensure_ascii=False)[:300]}")
    return fallas


# ================================================================ el reporte

NOMBRE = {"norma": "Norma", "candido": "Cándido"}
SENALES_DE = {
    "profile-check": {"profile_without_occupation", "essential_skill_missing", "requirement_without_task", "education_level_inconsistent",
                      "profile_review_overdue"},
    "profile-language": {"requirement_not_allowed"},
    "profile-map": {"profiles_overlap"},
    "cv-check": {"claim_without_support", "certification_expired", "employment_dates_differ"},
    "candidate-fit": {"requirement_not_evidenced"},
    "privacy-check": {"protected_data_received", "consent_missing", "retention_exceeded"},
    "vacancy-status": {"vacancy_past_target"},
}


def reporte(r: dict, comando: str, version: str) -> str:
    return marco_reporte(r, comando, version, agente=NOMBRE.get(r.get("agente"), r.get("agente")), senales=SENALES_DE.get(comando),
                         alcance=f"periodo {r['periodo']}", cuerpo=_cuerpo, familia="criterio-chro")


def _si(b) -> str:
    return "sí" if b else "no"


def _cuerpo(r: dict, comando: str, p: dict | None) -> list[str]:
    l: list[str] = []
    if not p:
        return l
    if comando == "roles-scan":
        l += [f"**Perfiles en la ficha:** {p['perfiles']} · **Estándar:** {(p['estandar'] or '—').upper()}, {p['ocupaciones']} ocupaciones.", ""]
    elif comando == "profile-check":
        l += ["| Perfil | Ocupación | Nivel | Estudios | Requisitos | Tareas | Del estándar sin recoger | Revisión |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {x['id']} · {x['titulo']} | {x['ocupacion'] or '—'}{' · ' + x['ocupacion_nombre'] if x['ocupacion_nombre'] else ''} | {x['nivel'] or '—'} | "
              f"{x['estudios'] or '—'} | {x['requisitos']} | {x['tareas']} | {len(x['faltan'])} | {x['revision'] or '—'} |" for x in p["perfiles"]]
        l += ["", "El perfil lo aprueba una persona: aquí se dice qué le falta frente a su ocupación y qué requisito no se apoya en una tarea.", ""]
    elif comando == "profile-language":
        l += ["**Lo que no se puede pedir:**", ""] + [f"- {x['nombre']}: {x['fuente']}" for x in p["reglas"]] + [""]
        l += ["| Perfil | Requisitos que piden algo que no se puede pedir |", "|---|---|"]
        l += [f"| {x['id']} · {x['titulo']} | {', '.join(x['fuera']) or '—'} |" for x in p["perfiles"]]
        l.append("")
    elif comando == "profile-map":
        l += ["| Perfil | Ocupación |", "|---|---|"] + [f"| {x['id']} · {x['titulo']} | {x['ocupacion'] or '—'}{' · ' + x['ocupacion_nombre'] if x['ocupacion_nombre'] else ''} |"
                                                       for x in p["perfiles"]]
        if p["solapes"]:
            l += ["", "| Se solapan | Ocupación | En común |", "|---|---|---|"]
            l += [f"| {s['a']} y {s['b']} | {s['ocupacion']} | {round(s['comun'] * 100)} % |" for s in p["solapes"]]
        if p["sin_perfil"]:
            l += ["", "**Ocupaciones afines a las suyas que la organización no tiene perfiladas:** " +
                  ", ".join(f"{s['codigo']} · {s['nombre']}" for s in p["sin_perfil"]) + "."]
        l.append("")
    elif comando == "talent-scan":
        l += [f"**En la ficha:** {p['candidatos']} candidatos · **Vacantes en el registro:** {p['vacantes']} · **Perfiles de Norma:** {p['perfiles']}"
              f"{' (periodo ' + p['perfiles_de'] + ')' if p['perfiles_de'] else ''}.", ""]
    elif comando == "cv-check":
        l += ["| Candidato | Vacante | Afirmaciones |", "|---|---|---|"]
        l += [f"| {c['id']} | {c['vacante'] or '—'} | {c['afirmaciones']} |" for c in p["candidatos"]]
        l += ["", "Cada afirmación se contrasta con su soporte; ninguna se da por falsa: se dice cuál no tiene soporte o no coincide.", ""]
    elif comando == "candidate-fit":
        for c in p["candidatos"]:
            l += [f"### {c['id']} · vacante {c['vacante'] or '—'} · perfil {c['perfil'] or '—'}", ""]
            if not c["requisitos"]:
                l += ["Sin perfil procesado: no se contrasta.", ""]
                continue
            l += ["| Requisito | Esencial | Evidencias | Con soporte | Dónde |", "|---|---|---|---|---|"]
            l += [f"| {x['requisito']} · {x['texto']} | {_si(x['esencial'])} | {x['evidencias']} | {_si(x['soportado'])} | {', '.join('`' + s + '`' for s in x['citas']) or '—'} |"
                  for x in c["requisitos"]]
            l.append("")
        l += ["Los candidatos van en el orden de su identificador. No hay puntaje ni orden por número: quien selecciona decide.", ""]
    elif comando == "privacy-check":
        l += [f"**Conservación de la política:** {str(p['conserva_dias']) + ' días' if p['conserva_dias'] is not None else '—'}.", "",
              "| Candidato | Recibido | Autorización | Estado | Conservar hasta | Excluido |", "|---|---|---|---|---|---|"]
        l += [f"| {c['id']} | {c['recibido'] or '—'} | {c['autorizacion'] or '—'} | {c['estado'] or '—'} | {c['conservar_hasta'] or '—'} | "
              f"{', '.join(x.replace('_', ' ') for x in c['excluido']) or '—'} |" for c in p["candidatos"]]
        l += ["", "Lo excluido no se copia ni se usa: aquí solo se dice que llegó.", ""]
    elif comando == "vacancy-status":
        l += ["| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |", "|---|---|---|---|---|---|---|---|"]
        l += [f"| {v['vacante']} | {v['perfil'] or '—'} | {v['apertura'] or '—'} | {str(v['plazo']) + ' días' if v['plazo'] else '—'} | {v['tope'] or '—'} | "
              f"{v['cierre'] or '—'} | {v['dias_abierta'] if v['dias_abierta'] is not None else '—'} | {v['responsable'] or '—'} |" for v in p["vacantes"]]
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
    scan = {"norma": "roles-scan", "candido": "talent-scan"}[rol]
    carpetas = {"norma": ("10-perfiles",), "candido": ("20-vacantes", "30-candidatos", "40-autorizaciones", "50-ats")}[rol]
    u = ultima(scan)
    if not u or (hoy - u).days >= 7 or any(nueva(c, u) for c in carpetas) or nueva("00-referencia", u):
        toca.append(scan)
        motivo.append("documentos nuevos o la revisión semanal")
    r = {"norma": norma, "candido": candido}[rol](cfg, periodo, hoy)
    for cmd, senales in SENALES_DE.items():
        if cmd in r["partes"] and any(a["signal"] in senales for a in r["alertas"]) and ultima(cmd) != hoy:
            toca.append(cmd)
            motivo.append(f"{sum(1 for a in r['alertas'] if a['signal'] in senales)} señales abiertas en {N.nombre_comando(cmd).lower()}")
    return {"toca": toca, "motivo": motivo, "hoy": iso(hoy), "callado": not toca}


# ================================================================ la línea de comandos

def _rol() -> str:
    return {"criterio-talent": "candido"}.get(N.plugin(AQUI)["name"], "norma")


def calcular(cfg: dict, rol: str, a) -> tuple[dict, Path]:
    hoy = _hoy(a)
    periodo = a.period or cfg.get("period")
    if not periodo:
        raise SystemExit("falta el periodo: --period AAAA-MM o `period` en la configuración")
    r = {"norma": norma, "candido": candido}[rol](cfg, periodo, hoy)
    destino = cfg["_estado"] / SUB[rol] / periodo / "resultados.json"
    escribir_json(destino, r)
    return r, destino


def main() -> int:
    ap = N.argumentos("El motor de Norma y Cándido.")
    ap.add_argument("action", choices=["init", "config", "terminos", "aceptar", "inventario", "convertir", "ocupacion", "busqueda",
                                       "compute", "reporte", "despertar", "responder", "corrida", "buscar-raiz", "marcar-raiz", "arranque",
                                       "dejar-listo", "selftest"])
    a = ap.parse_args()
    if a.action == "selftest":
        return selftest()
    if a.action in ("ocupacion", "busqueda"):
        if not (a.config and a.id):
            ap.error("--config y --id (el código de la ocupación, o la vacante)")
        cfg, _ = N.cargar_config(a.config)
        r = ocupacion(cfg, a.id) if a.action == "ocupacion" else busqueda(cfg, a.id, a.period or cfg.get("period") or "")
        print(json.dumps(r, ensure_ascii=False, indent=2, default=str)[:60000])
        return 0 if r.get("ok") else 1
    return N.despachar(a, ap, aqui=AQUI, rol=_rol(), estructura_json=ESTRUCTURA, subcarpetas=tuple(SUB.values()),
                       revisar_config=revisar_config, calcular=calcular, reporte=reporte, despertar=despertar)


# ================================================================ la prueba del motor

def _cuoc_de_prueba(ruta: Path) -> None:
    """Un libro con las hojas y las columnas de la descarga de los perfiles ocupacionales de la CUOC
    2026 (F-03), con dos ocupaciones sintéticas."""
    hojas = {
        "Ocupación": [["CLASIFICACIÓN ÚNICA DE OCUPACIONES PARA COLOMBIA CUOC 2026"],
                      ["Código del Gran Grupo", "Nombre del Gran Grupo", "Código del Subgrupo Principal", "Nombre del Subgrupo Principal",
                       "Código del Subgrupo", "Nombre del Subgrupo", "Código del Grupo Primario", "Nombre del Grupo Primario", CUOC_CODIGO, CUOC_NOMBRE],
                      ["2", "PROFESIONALES", "24", "x", "241", "x", "2411", "x", "24111", "Contadores sintéticos"],
                      ["4", "APOYO ADMINISTRATIVO", "43", "x", "431", "x", "4311", "x", "43111", "Auxiliares contables sintéticos"]],
        "Funciones": [["x"], ["Código del Gran Grupo", CUOC_CODIGO, CUOC_NOMBRE, "Consecutivo de la Función", "Funciones de la Ocupación"],
                      ["2", "24111", "Contadores sintéticos", "1", "Preparar los estados financieros."]],
        "Denominaciones": [["x"], ["Código del Gran Grupo", CUOC_CODIGO, CUOC_NOMBRE, "Código de la Denominación", "Nombre de la Denominación"],
                           ["2", "24111", "Contadores sintéticos", "24111.001", "Contador / Contadora"]],
        "Nivel Competencia": [["x"], ["Código del Gran Grupo", CUOC_CODIGO, CUOC_NOMBRE, "Nivel de Competencia"],
                              ["2", "24111", "Contadores sintéticos", "4"], ["4", "43111", "Auxiliares contables sintéticos", "2"]],
        "Conocimientos": [["x"], ["Código del Gran Grupo", CUOC_CODIGO, CUOC_NOMBRE, "ID", "Nombre del Conocimiento"],
                          ["2", "24111", "Contadores sintéticos", "5", "Contabilidad"], ["2", "24111", "Contadores sintéticos", "7", "Legislación tributaria"]],
        "Destrezas": [["x"], ["Código del Gran Grupo", CUOC_CODIGO, CUOC_NOMBRE, "ID", "Nombre de la Destreza"],
                      ["2", "24111", "Contadores sintéticos", "27", "Análisis de procesos"], ["4", "43111", "Auxiliares contables sintéticos", "1", "Comprensión de lectura"]],
        "Ocupaciones Afines": [["x"], ["Código del Gran Grupo", CUOC_CODIGO, CUOC_NOMBRE, "Código de la Ocupación Afin", "Nombre de la Ocupación Afin"],
                               ["2", "24111", "Contadores sintéticos", "43111", "Auxiliares contables sintéticos"]],
        "Equivalencias": [["x"], [CUOC_CODIGO, CUOC_NOMBRE, "Código CIUO-08", "Observaciones sobre la CIUO-08"], ["24111", "Contadores sintéticos", "2411", "x"]],
    }
    escribir_xlsx_hojas(ruta, hojas)


def escribir_xlsx_hojas(ruta: Path, hojas: dict[str, list[list]]) -> None:
    """Un .xlsx con varias hojas, con cadenas en línea: para el material de prueba."""
    from xml.sax.saxutils import escape
    ruta.parent.mkdir(parents=True, exist_ok=True)

    def col(i: int) -> str:
        s = ""
        i += 1
        while i:
            i, r = divmod(i - 1, 26)
            s = chr(65 + r) + s
        return s
    class _Z(zipfile.ZipFile):
        # La misma fecha en cada entrada: el mismo libro cada vez, byte a byte.
        def writestr(self, nombre, datos, *a, **k):
            info = zipfile.ZipInfo(nombre, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            return super().writestr(info, datos, *a, **k)
    with _Z(ruta, "w", zipfile.ZIP_DEFLATED) as z:
        n = len(hojas)
        z.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   + "".join(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                             for i in range(1, n + 1)) + "</Types>")
        z.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
                   + "".join(f'<sheet name="{escape(h)}" sheetId="{i}" r:id="rId{i}"/>' for i, h in enumerate(hojas, 1)) + "</sheets></workbook>")
        z.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   + "".join(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
                             for i in range(1, n + 1)) + "</Relationships>")
        for i, filas in enumerate(hojas.values(), 1):
            xml = []
            for r, f in enumerate(filas, 1):
                xml.append(f'<row r="{r}">' + "".join(f'<c r="{col(j)}{r}" t="inlineStr"><is><t>{escape(str(v))}</t></is></c>' for j, v in enumerate(f) if v not in (None, ""))
                           + "</row>")
            z.writestr(f"xl/worksheets/sheet{i}.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                       f'<sheetData>{"".join(xml)}</sheetData></worksheet>')


def selftest() -> int:
    import tempfile
    fallas = []

    def ok(nombre, obtenido, esperado):
        if obtenido == esperado:
            print(f"  ok  {nombre}")
        else:
            fallas.append(nombre)
            print(f"  FALLA  {nombre}: {obtenido!r} en lugar de {esperado!r}")

    hoy = dt.date(2026, 11, 16)
    s = sensibles()
    ok("cada ley de datos sensibles tiene su norma, su artículo y su fuente",
       [k for k, v in (s.get("leyes") or {}).items() if not (v.get("norma") and v.get("articulo") and v.get("fuente") and v.get("categorias"))], [])
    ok("cada categoría de una ley tiene su patrón", sorted({c for v in (s.get("leyes") or {}).values() for c in v["categorias"]} - set(s.get("categorias") or {})), [])
    ok("los países sin ley general verificada no tienen categorías", sorted(set(s.get("leyes") or {}) & {"PY", "GT", "HN", "BR"}), [])
    pr = patrones_prohibidos({"entity": {"country": "CO"}, "selection": {"prohibited_requirements": ["edad", "estado civil", "fotografía"]}})
    ok("lo que no se puede pedir en Colombia, con su artículo",
       [x["categoria"] for x in prohibido("Hombre soltero, entre 25 y 35 años de edad, con foto reciente y afiliado al partido", pr)],
       ["opiniones_politicas", "edad", "estado_civil", "fotografia"])
    ok("un conocimiento no es un dato de la persona", prohibido("Conocimiento en seguridad y salud en el trabajo y en riesgo político", pr), [])
    ok("la salud de la persona sí", [x["categoria"] for x in prohibido("Gozar de buen estado de salud y no estar embarazada", pr)], ["salud"])
    ok("el nivel de competencia de la CUOC y su CINE (numeral 3.2)", CINE_DE_NIVEL, {1: (1, 1), 2: (2, 4), 3: (5, 5), 4: (6, 8)})
    ok("el código CUOC con o sin puntos", [codigo_ocupacion("2411-1", "cuoc"), codigo_ocupacion("24111", "cuoc")], ["24111", "24111"])
    ok("el código O*NET sin el sufijo", codigo_ocupacion("13-2011", "onet"), "13-2011.00")
    ok("una fecha al mes", [_mes("2019-03"), _mes("03/2019"), _mes("2019-03-15"), _mes("marzo")], [(2019, 3), (2019, 3), (2019, 3), None])
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        docs, est = t / "talento" / "e1", t / "estado" / "e1"
        _cuoc_de_prueba(docs / "00-referencia" / "estandar" / "PerfilesOcupacionales-Excel-CUOC-2026.xlsx")
        o = _cuoc(docs / "00-referencia" / "estandar" / "PerfilesOcupacionales-Excel-CUOC-2026.xlsx")
        ok("la CUOC: las ocupaciones, sus destrezas, sus conocimientos, su nivel y su CIUO-08",
           (sorted(o["ocupaciones"]), [d["nombre"] for d in o["ocupaciones"]["24111"]["destrezas"]],
            [d["nombre"] for d in o["ocupaciones"]["24111"]["conocimientos"]], o["ocupaciones"]["24111"]["nivel"], o["ocupaciones"]["24111"]["ciuo"],
            o["ocupaciones"]["24111"]["afines"]),
           (["24111", "43111"], ["Análisis de procesos"], ["Contabilidad", "Legislación tributaria"], 4, "2411", ["43111"]))
        for c in ("10-perfiles", "30-candidatos/VAC-01/CAN-001", "30-candidatos/VAC-01/CAN-002", "30-candidatos/VAC-01/CAN-003"):
            (docs / c).mkdir(parents=True, exist_ok=True)
        for f in ("10-perfiles/PC-01_contador.docx", "10-perfiles/PC-02_contador-senior.docx", "10-perfiles/PC-03_auxiliar.docx"):
            (docs / f).write_text("perfil", encoding="utf-8")
        R = lambda i, txt, tareas, **k: {"id": i, "text": txt, "tasks": tareas, **k}  # noqa: E731
        escribir_json(est / "perfiles" / "2026-11" / "ficha.json", {"profiles": [
            {"id": "PC-01", "title": "Contador", "source": "10-perfiles/PC-01_contador.docx", "occupation": {"standard": "cuoc", "code": "24111"},
             "education": {"label": "Profesional"}, "tasks": [{"id": "T1", "text": "Preparar los estados financieros"}],
             "requirements": [R("R1", "Contabilidad bajo NIIF", ["T1"], element="C5", essential=True),
                              R("R2", "Análisis de procesos contables", ["T1"], element="Análisis de procesos", essential=True),
                              R("R3", "Tarjeta profesional vigente", ["T1"], type="certificacion", essential=True),
                              R("R4", "Hombre soltero menor de 35 años", [])],
             "last_review": "2025-06-01"},
            {"id": "PC-02", "title": "Contador senior", "source": "10-perfiles/PC-02_contador-senior.docx", "occupation": {"standard": "cuoc", "code": "24111"},
             "education": {"label": "Maestría"}, "tasks": [{"id": "T1", "text": "Preparar los estados financieros"}],
             "requirements": [R("R1", "Contabilidad bajo NIIF", ["T1"], element="C5"), R("R2", "Análisis de procesos contables", ["T1"], element="D27"),
                              R("R3", "Tarjeta profesional vigente", ["T1"])],
             "not_applicable": [{"element": "Legislación tributaria", "reason": "la lleva el área de impuestos"}], "next_review": "2027-01-01"},
            {"id": "PC-03", "title": "Auxiliar contable", "source": "10-perfiles/PC-03_auxiliar.docx", "occupation": {"standard": "cuoc", "code": "43111"},
             "education": {"label": "Profesional"}, "tasks": [{"id": "T1", "text": "Registrar las facturas"}],
             "requirements": [R("R1", "Comprensión de lectura", ["T1"], element="D1")], "next_review": "2027-01-01"},
            {"id": "PC-04", "title": "Analista", "source": "10-perfiles/PC-04.docx", "tasks": [], "requirements": [], "next_review": "2027-01-01"}]})
        cfg = {"entity": {"id": "900000000", "name": "Prueba", "country": "CO"}, "period": "2026-11", "_docs": docs, "_estado": est,
               "standard": {"name": "cuoc", "file": "00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026.xlsx"},
               "education": {"levels": {"Bachiller": 3, "Técnico profesional": 5, "Profesional": 6, "Maestría": 7}},
               "profiles": {"review_months": 12}, "selection": {"prohibited_requirements": ["edad", "estado civil", "sexo"]}}
        ok("la configuración de Norma pasa", revisar_config(cfg, "norma"), [])
        r = norma(cfg, "2026-11", hoy)
        ok("Norma: las siete señales donde se sembraron, y ninguna de más",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("education_level_inconsistent", "estudios:PC-03"),
            ("essential_skill_missing", "elemento:PC-01:c7"),
            ("profile_review_overdue", "revision:PC-01"), ("profile_without_occupation", "ocupacion:PC-04"),
            ("profiles_overlap", "solape:PC-01:PC-02"),
            ("requirement_not_allowed", "prohibido:PC-01:R4:edad"), ("requirement_not_allowed", "prohibido:PC-01:R4:estado_civil"),
            ("requirement_not_allowed", "prohibido:PC-01:R4:sexo"),
            ("requirement_without_task", "tarea:PC-01:R4")])
        ok("Norma: el perfil fuera de la ficha se dice", r["record_issues"], [])
        ok("una ocupación para armar un perfil", {k: ocupacion(cfg, "24111")[k] for k in ("nombre", "nivel", "cine")},
           {"nombre": "Contadores sintéticos", "nivel": 4, "cine": [6, 8]})
        md = reporte(r, "profile-check", "0.0.0")
        ok("el reporte sigue el orden común", [x for x in md.splitlines() if x.startswith("## ")],
           ["## Lo que hay que atender", "## El resultado", "## Lo que no se pudo procesar", "## Las preguntas que hizo", "## Fuentes"])
        # Cándido.
        _csv(docs / "20-vacantes" / "registro-vacantes.csv", [["Vacante", "Perfil", "Apertura", "Cierre", "Estado", "Responsable"],
                                                             ["VAC-01", "PC-01", "2026-09-01", "", "abierta", "Lucía"],
                                                             ["VAC-02", "PC-03", "2026-03-01", "2026-04-15", "cubierta", "Lucía"]])
        _csv(docs / "40-autorizaciones" / "registro-autorizaciones.csv", [["candidato", "fecha", "finalidad"], ["CAN-001", "2026-09-05", "seleccion"],
                                                                         ["CAN-002", "2026-09-20", "seleccion"], ["CAN-003", "2026-09-05", "seleccion"]])
        _csv(docs / "50-ats" / "exportacion-ats.csv", [["Candidate ID", "Requisition ID", "Applied Date", "Stage", "Last Activity"],
                                                       ["CAN-001", "VAC-01", "2026-09-05", "Entrevista", "2026-10-01"],
                                                       ["CAN-002", "VAC-01", "2026-09-06", "Entrevista", "2026-10-01"],
                                                       ["CAN-003", "VAC-01", "2026-09-05", "Entrevista", "2026-10-01"],
                                                       ["CAN-009", "VAC-02", "2026-03-05", "No seleccionado", "2026-04-10"]])
        (docs / "30-candidatos" / "VAC-02" / "CAN-009").mkdir(parents=True)
        (docs / "30-candidatos" / "VAC-02" / "CAN-009" / "hoja-de-vida.pdf").write_text("x", encoding="utf-8")
        for c in ("CAN-001", "CAN-002", "CAN-003"):
            for f in ("hoja-de-vida.pdf", "tarjeta-profesional.pdf", "certificado-laboral.pdf"):
                (docs / "30-candidatos" / "VAC-01" / c / f).write_text("x", encoding="utf-8")
        (docs / "30-candidatos" / "VAC-01" / "CAN-002" / "foto.jpg").write_bytes(b"\xff\xd8")

        def cand(cid, **k):
            b = f"30-candidatos/VAC-01/{cid}/"
            return {"id": cid, "vacancy": "VAC-01", "folder": b, "cv": b + "hoja-de-vida.pdf", "received": "2026-09-05",
                    "claims": [{"id": "K1", "type": "certificacion", "text": "Tarjeta profesional de contador", "cv_source": b + "hoja-de-vida.pdf",
                                "support": b + "tarjeta-profesional.pdf", "expires": "2027-01-31", "requirement": "R3"},
                               {"id": "K2", "type": "empleo", "text": "Contador en Comercial Andina", "cv_source": b + "hoja-de-vida.pdf",
                                "support": b + "certificado-laboral.pdf", "from": "2019-03", "to": "2022-08", "support_from": "2019-03-01",
                                "support_to": "2022-08-31"},
                               {"id": "K3", "type": "titulo", "text": "Contador público", "cv_source": b + "hoja-de-vida.pdf", "support": None}],
                    "evidence": [{"requirement": "R1", "source": b + "hoja-de-vida.pdf, p. 1"}], **k}
        c3 = cand("CAN-003")
        c3["claims"][1]["support_to"] = "2021-12-31"
        c3["claims"][0]["expires"] = "2026-06-30"
        escribir_json(est / "seleccion" / "2026-11" / "ficha.json", {"candidates": [
            cand("CAN-001"), cand("CAN-002", protected=[{"type": "fecha_de_nacimiento", "source": "30-candidatos/VAC-01/CAN-002/hoja-de-vida.pdf"}]), c3,
            {"id": "CAN-009", "vacancy": "VAC-02", "folder": "30-candidatos/VAC-02/CAN-009/", "cv": "30-candidatos/VAC-02/CAN-009/hoja-de-vida.pdf"}]})
        cfg["selection"] = {**cfg["selection"], "vacancy": {"target_days": 45}, "data": {"retention_days": 180}}
        ok("la configuración de Cándido pasa", revisar_config(cfg, "candido"), [])
        r = candido(cfg, "2026-11", hoy)
        ok("Cándido: las ocho señales donde se sembraron, y ninguna de más",
           sorted((a["signal"], a["key"]) for a in r["alertas"]),
           [("certification_expired", "certificacion:CAN-003:K1"),
            ("claim_without_support", "soporte:CAN-001:K3"), ("claim_without_support", "soporte:CAN-002:K3"), ("claim_without_support", "soporte:CAN-003:K3"),
            ("consent_missing", "autorizacion:CAN-002"), ("consent_missing", "autorizacion:CAN-009"),
            ("employment_dates_differ", "fechas:CAN-003:K2"),
            ("protected_data_received", "protegido:CAN-002:fecha_de_nacimiento"), ("protected_data_received", "protegido:CAN-002:fotografia"),
            ("requirement_not_evidenced", "requisito:CAN-001:R2"), ("requirement_not_evidenced", "requisito:CAN-002:R2"),
            ("requirement_not_evidenced", "requisito:CAN-003:R2"),
            ("retention_exceeded", "conservacion:CAN-009"), ("vacancy_past_target", "vacante:vac_01")])
        ok("Cándido: la ficha está completa", r["record_issues"], [])
        ok("los candidatos van en el orden de su identificador", [c["id"] for c in r["partes"]["candidate-fit"]["candidatos"]],
           ["CAN-001", "CAN-002", "CAN-003", "CAN-009"])
        # La prueba de sesgo: CAN-001 y CAN-002 son el mismo candidato salvo la fotografía y la fecha de
        # nacimiento; la autorización de CAN-002 llegó tarde, así que se iguala antes de comparar.
        _csv(docs / "40-autorizaciones" / "registro-autorizaciones.csv", [["candidato", "fecha", "finalidad"], ["CAN-001", "2026-09-05", "seleccion"],
                                                                         ["CAN-002", "2026-09-05", "seleccion"], ["CAN-003", "2026-09-05", "seleccion"]])
        r = candido(cfg, "2026-11", hoy)
        ok("la prueba de sesgo: el par da exactamente lo mismo", sesgo(r, [("CAN-001", "CAN-002")]), [])
        f = leer_json(est / "seleccion" / "2026-11" / "ficha.json")
        f["candidates"][1]["evidence"] = []
        escribir_json(est / "seleccion" / "2026-11" / "ficha.json", f)
        ok("la prueba de sesgo detecta un par que no da lo mismo", len(sesgo(candido(cfg, "2026-11", hoy), [("CAN-001", "CAN-002")])), 1)
        f["candidates"][1]["protected"] = [{"type": "edad", "value": "34", "source": "x"}]
        escribir_json(est / "seleccion" / "2026-11" / "ficha.json", f)
        ok("la ficha no copia el dato protegido", [x for x in candido(cfg, "2026-11", hoy)["record_issues"] if "protected" in x],
           ["candidates[1].protected[0]: solo type y source; el dato no se copia a la ficha"])
        _csv(docs / "50-ats" / "base-interna.csv", [["persona", "ocupacion", "cargo"], ["P-07", "43111", "Auxiliar contable"], ["P-02", "24111", "Analista"],
                                                    ["P-05", "21111", "Físico"]])
        b = busqueda(cfg, "VAC-01", "2026-11")
        ok("la búsqueda: las denominaciones, los esenciales y la base interna por su identificador",
           (b["titulos"], [x["persona"] for x in b["internos"]], b["cadena"].startswith('("Contador" OR "Contadora")')),
           (["Contador", "Contadora"], ["P-02", "P-07"], True))
    print(f"\n{'todo en orden' if not fallas else str(len(fallas)) + ' fallas'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
