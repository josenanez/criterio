#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-finance/scripts/nucleo.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
# -*- coding: utf-8 -*-
"""El núcleo común de los motores: lo que es igual en cualquier función.

Números y fechas como llegan en las exportaciones, tablas en CSV y Excel con su fila de
origen, la estructura recomendada y el inventario de la carpeta, las señales, el marco común
del reporte, el registro de cada corrida y las peticiones. El registro y las peticiones siguen el
contrato de estado común de todos los agentes (ADR 0010): `<estado>/corridas.json` con
`<estado>/corridas/<id>.md`, y `<estado>/peticiones/<id>.json`, con el mismo esquema que la familia
PMO, para que Rostrum los sirva sin saber de qué familia son. Lo propio de cada función vive en su motor
—`finanzas.py`, `legal.py`—, que importa esto. Las reglas de compromiso también viven aquí: las usan
Samuel y Vera desde `portafolio.py` y las va a usar Ofelia (ADR 0012).

La fuente vive en criterio-finance y `scripts/sincronizar.py` la copia a los demás plugins: un
plugin instalado tiene que correr solo. Librería estándar, sin dependencias.
"""
from __future__ import annotations

import calendar
import csv
import datetime as dt
import hashlib
import io
import json
import re
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Cada motor agrega aquí la importancia de sus señales: 1 es la más alta.
SEVERIDAD: dict[str, int] = {}

# ================================================================ texto, números y fechas


def norm(s) -> str:
    """Una cabecera o un nombre, comparables: sin tildes, en minúscula, con guion bajo."""
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def numero(v) -> float | None:
    """Un valor de una exportación: 1.234.567,89 · 1,234,567.89 · (123) · -123 · 1234.5."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(" ", "").replace(" ", "").replace("$", "")
    if not s:
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()")
    if s.startswith("-"):
        neg, s = not neg, s[1:]
    if "," in s and "." in s:
        dec = "," if s.rfind(",") > s.rfind(".") else "."
        mil = "." if dec == "," else ","
        s = s.replace(mil, "").replace(dec, ".")
    elif "," in s:
        s = s.replace(",", "") if re.fullmatch(r"\d{1,3}(,\d{3})+", s) else s.replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3}){2,}", s):
        s = s.replace(".", "")
    try:
        x = float(s)
    except ValueError:
        return None
    return -x if neg else x


def fecha(v) -> dt.date | None:
    """ISO, dd/mm/aaaa, dd-mm-aaaa, aaaa/mm/dd o el número de serie de Excel."""
    if v is None or v == "":
        return None
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    s = str(v).strip()
    m = re.match(r"^(\d{4})[-/](\d{1,2})[-/](\d{1,2})", s)
    if m:
        try:
            return dt.date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            return None
    m = re.match(r"^(\d{1,2})[-/](\d{1,2})[-/](\d{4})", s)
    if m:
        try:
            return dt.date(int(m[3]), int(m[2]), int(m[1]))
        except ValueError:
            return None
    if re.fullmatch(r"\d{5}(\.\d+)?", s):                      # serie de Excel
        return dt.date(1899, 12, 30) + dt.timedelta(days=int(float(s)))
    return None


# El registro único de países: paises.json, junto a este archivo. Ningún motor escribe el nombre ni
# el código de un país; lo que cambia de uno a otro —el separador decimal, la identificación fiscal,
# la moneda, y para la CFO su factura— sale de ahí. Agregar un país es agregar su entrada.
PAISES = {p["codigo"]: p for p in json.loads((Path(__file__).resolve().parent / "paises.json").read_text(encoding="utf-8"))["paises"]}
POR_OMISION = next(iter(PAISES))

_PAIS = [POR_OMISION]


def pais_de(cfg_o_entidad: dict) -> str:
    """El código del país de la entidad, de la configuración o de la entidad misma."""
    ent = cfg_o_entidad.get("entity", cfg_o_entidad) if isinstance(cfg_o_entidad, dict) else {}
    return ((ent or {}).get("country") or POR_OMISION).upper()


def revisar_pais(ent: dict) -> list[str]:
    """Lo que falla del país de una entidad: vacío si está en el registro."""
    c = (ent.get("country") or "").upper()
    if c in PAISES:
        return []
    return [f"entity.country debe ser uno de {', '.join(PAISES)} en esta versión"]


def mon(x) -> str:
    """Una cifra como se lee en el país de la entidad, con el separador decimal de su registro."""
    if x is None:
        return "—"
    t = f"{x:,.2f}"
    return t.replace(",", "§").replace(".", ",").replace("§", ".") if PAISES.get(_PAIS[0], {}).get("decimal") == "," else t


def pc(x: float, signo: bool = False) -> str:
    t = f"{x:+.1f}" if signo else f"{x:.1f}"
    return t.replace(".", ",") if PAISES.get(_PAIS[0], {}).get("decimal") == "," else t


def iso(d) -> str | None:
    return d.isoformat() if d else None


def redondo(x: float | None) -> float | None:
    return None if x is None else round(x + 0.0, 2)


def ident(v) -> str:
    """NIT, RUC o número de documento comparables: solo dígitos y letras, sin ceros a la izquierda."""
    s = re.sub(r"[^0-9A-Za-z]", "", str(v or "")).upper()
    return s.lstrip("0") or s


def nit_sin_dv(v) -> str:
    """El NIT sin el dígito de verificación, cuando viene con guion: 900123456-7 → 900123456."""
    s = str(v or "").strip()
    m = re.match(r"^([0-9.]+)-\d$", s)
    return ident(m[1] if m else s)


def fin_de_mes(periodo: str) -> dt.date:
    a, m = (int(x) for x in periodo.split("-"))
    return dt.date(a, m, calendar.monthrange(a, m)[1])


def inicio_de_mes(periodo: str) -> dt.date:
    a, m = (int(x) for x in periodo.split("-"))
    return dt.date(a, m, 1)


def dia_habil(desde: dt.date, n: int, feriados: set) -> dt.date:
    """El día hábil número n después de `desde` (sin contarlo)."""
    d, k = desde, 0
    while k < n:
        d += dt.timedelta(days=1)
        if d.weekday() < 5 and d.isoformat() not in feriados:
            k += 1
    return d


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def leer_json(p: Path, defecto=None):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return defecto
    except json.JSONDecodeError as e:
        raise SystemExit(f"{p}: JSON inválido: {e}")


def escribir_json(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ================================================================ tablas: CSV y Excel

S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def _col(ref: str) -> int:
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def xlsx_filas(ruta: Path) -> list[list[str]]:
    """La primera hoja de un .xlsx, con cada celda en su columna (las vacías no corren las demás)."""
    with zipfile.ZipFile(ruta) as z:
        nombres = z.namelist()
        compartidas = []
        if "xl/sharedStrings.xml" in nombres:
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(f"{S}si"):
                compartidas.append("".join(t.text or "" for t in si.iter(f"{S}t")))
        hojas = sorted((n for n in nombres if re.match(r"xl/worksheets/sheet\d+\.xml$", n)),
                       key=lambda n: int(re.search(r"(\d+)\.xml$", n)[1]))
        if not hojas:
            return []
        filas = []
        for fila in ET.fromstring(z.read(hojas[0])).iter(f"{S}row"):
            celdas: dict[int, str] = {}
            for i, c in enumerate(fila.iter(f"{S}c")):
                pos = _col(c.get("r")) if c.get("r") else i
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
        return filas


def csv_filas(ruta: Path) -> list[list[str]]:
    crudo = ruta.read_bytes()
    for cod in ("utf-8-sig", "latin-1"):
        try:
            texto = crudo.decode(cod)
            break
        except UnicodeDecodeError:
            continue
    muestra = texto[:4096]
    delim = max((";", ",", "\t", "|"), key=lambda d: muestra.count(d))
    return [r for r in csv.reader(io.StringIO(texto), delimiter=delim)]


def _celdas(linea: str) -> list[tuple[int, int, str]]:
    """Los trozos de una línea con su posición: una palabra suelta sigue en su celda; dos espacios
    o más separan una celda de la siguiente."""
    return [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"\S+(?: \S+)*", linea)]


def pdf_filas(ruta: Path) -> list[list[str]]:
    """Una tabla dentro de un PDF con capa de texto —el extracto que el banco entrega en PDF—.

    `pdftotext -layout` deja cada palabra en su columna; la cabecera fija dónde está cada una y
    cada línea se reparte por posición. Una línea que no llena al menos dos columnas —el pie de
    página, la segunda línea de una descripción— no es una fila. La cabecera que se repite en cada
    página se salta. Sin `pdftotext`, o con un escaneo sin texto, no hay tabla: lo dice el error,
    y el que llama lo deja en lo no procesado. Ninguna fila se adivina."""
    import shutil
    import subprocess
    if not shutil.which("pdftotext"):
        raise ValueError(f"{ruta.name}: para leer un PDF hace falta pdftotext (poppler); sin él, pide la exportación en Excel o CSV")
    r = subprocess.run(["pdftotext", "-layout", str(ruta), "-"], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise ValueError(f"{ruta.name}: pdftotext terminó en {r.returncode}")
    nombres = {a for v in ALIAS.values() for a in v} | set(ALIAS)
    lineas = r.stdout.replace("\f", "\n").splitlines()
    cab, inicio = None, 0
    for i, l in enumerate(lineas):
        c = _celdas(l)
        if len(c) >= 2 and sum(norm(x[2]) in nombres for x in c) >= 2:
            cab, inicio = c, i
            break
    if cab is None:
        raise ValueError(f"{ruta.name}: el PDF no trae una tabla con texto (¿es un escaneo?); pide la exportación en Excel o CSV")
    firma = [norm(x[2]) for x in cab]
    filas = [[x[2] for x in cab]]
    for l in lineas[inicio + 1:]:
        c = _celdas(l)
        if [norm(x[2]) for x in c] == firma:
            continue
        fila = [""] * len(cab)
        for a, b, t in c:
            solape = [max(0, min(b, cb) - max(a, ca)) for ca, cb, _ in cab]
            k = max(range(len(cab)), key=lambda j: solape[j]) if max(solape) > 0 else \
                min(range(len(cab)), key=lambda j: abs((a + b) / 2 - (cab[j][0] + cab[j][1]) / 2))
            fila[k] = (fila[k] + " " + t).strip()
        if sum(1 for x in fila if x) >= 2:
            filas.append(fila)
    return filas


def filas_de(ruta: Path) -> list[list[str]]:
    ext = ruta.suffix.lower()
    if ext == ".xlsx":
        return xlsx_filas(ruta)
    if ext in (".csv", ".txt", ".tsv"):
        return csv_filas(ruta)
    if ext == ".pdf":
        return pdf_filas(ruta)
    raise ValueError(f"{ruta.name}: una tabla llega en .csv, .xlsx o un PDF con texto, no en {ext}")


# Los nombres con que llega cada columna en las exportaciones. La organización puede fijar
# los suyos en la configuración (`columns`); si no, se detectan por el nombre.
ALIAS = {
    "cuenta": ["cuenta", "codigo", "codigo_cuenta", "cta", "cuenta_contable", "account"],
    "nombre": ["nombre", "nombre_cuenta", "descripcion_cuenta", "account_name"],
    "naturaleza": ["naturaleza", "nature"],
    "saldo_inicial": ["saldo_inicial", "saldo_anterior", "opening_balance"],
    "debito": ["debito", "debitos", "debe", "cargos", "debit"],
    "credito": ["credito", "creditos", "haber", "abonos", "credit"],
    "saldo_final": ["saldo_final", "nuevo_saldo", "saldo", "closing_balance", "balance"],
    "fecha": ["fecha", "fecha_movimiento", "fecha_contable", "fecha_documento", "date"],
    "tercero": ["tercero", "nit", "ruc", "identificacion", "id_tercero", "nit_tercero"],
    "documento": ["documento", "numero_documento", "num_documento", "factura", "doc", "numero"],
    "comprobante": ["comprobante", "asiento", "numero_asiento", "voucher"],
    "centro_costo": ["centro_costo", "centro_de_costo", "cc", "cost_center"],
    "descripcion": ["descripcion", "detalle", "concepto", "description"],
    "referencia": ["referencia", "ref", "numero_referencia", "reference"],
    "valor": ["valor", "monto", "importe", "amount"],
    "moneda": ["moneda", "divisa", "currency"],
    "id": ["id", "codigo_tarea", "tarea_id"],
    "tarea": ["tarea", "actividad", "task"],
    "area": ["area", "gerencia", "unidad"],
    "responsable": ["responsable", "owner", "encargado"],
    "dia_limite": ["dia_limite", "fecha_limite", "vence", "due"],
    "depende_de": ["depende_de", "dependencias", "predecesoras"],
    "evidencia_esperada": ["evidencia_esperada", "evidencia"],
    "criticidad": ["criticidad", "prioridad"],
    "estado": ["estado", "status"],
    "solicitud": ["solicitud", "requerimiento", "request"],
    "linea": ["linea", "linea_presupuestal", "rubro", "line"],
    "total": ["total", "total_anual", "anual"],
    "proveedor": ["proveedor", "vendor"],
    "saldo": ["saldo_por_ejecutar", "saldo_pendiente", "pendiente", "saldo"],
    "proyeccion": ["proyeccion", "proyeccion_cierre", "forecast"],
    "version": ["version", "version_presupuesto"],
}
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
MESES_LARGO = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
               "septiembre", "octubre", "noviembre", "diciembre"]


def _mes_de(cab: str) -> int | None:
    n = norm(cab)
    if n in MESES:
        return MESES.index(n) + 1
    if n in MESES_LARGO:
        return MESES_LARGO.index(n) + 1
    m = re.fullmatch(r"m_?(\d{1,2})|mes_?(\d{1,2})", n)
    if m:
        k = int(m[1] or m[2])
        return k if 1 <= k <= 12 else None
    return None


class Tabla:
    """Una tabla con sus columnas canónicas y la fila de origen de cada dato, para citarla."""

    def __init__(self, ruta: Path, requeridas: list[str], opcionales: list[str] = (),
                 columnas: dict | None = None, meses: bool = False):
        self.ruta, self.faltan, self.filas, self.mapa, self.meses = ruta, [], [], {}, {}
        filas = filas_de(ruta)
        # La cabecera es la primera fila que nombra al menos una columna requerida.
        inicio = 0
        for i, f in enumerate(filas[:15]):
            nf = {norm(x) for x in f}
            if any(set(ALIAS.get(c, [c])) & nf for c in requeridas):
                inicio = i
                break
        if not filas:
            self.faltan = list(requeridas)
            return
        cab = [norm(x) for x in filas[inicio]]
        fijas = {k: norm(v) for k, v in (columnas or {}).items()}
        for campo in list(requeridas) + list(opcionales):
            candidatos = [fijas[campo]] if campo in fijas else ALIAS.get(campo, [campo])
            for c in candidatos:
                if c in cab and cab.index(c) not in self.mapa.values():
                    self.mapa[campo] = cab.index(c)
                    break
        self.faltan = [c for c in requeridas if c not in self.mapa]
        if meses:
            for i, c in enumerate(filas[inicio]):
                m = _mes_de(c)
                if m:
                    self.meses[m] = i
        for k, f in enumerate(filas[inicio + 1:], start=inicio + 2):
            if not any(str(x).strip() for x in f):
                continue
            fila = {"_fila": k}
            for campo, i in self.mapa.items():
                fila[campo] = f[i].strip() if i < len(f) and isinstance(f[i], str) else (f[i] if i < len(f) else "")
            if meses:
                fila["_meses"] = {m: numero(f[i]) if i < len(f) else None for m, i in self.meses.items()}
            self.filas.append(fila)

    def cita(self, fila: dict, base: Path) -> dict:
        return {"archivo": rel(self.ruta, base), "fila": fila.get("_fila")}


def rel(p: Path, base: Path) -> str:
    try:
        return Path(p).resolve().relative_to(Path(base).resolve()).as_posix()
    except ValueError:
        return str(p)


def buscar(carpeta: Path, patron: str, pdf: bool = False) -> list[Path]:
    """Los archivos de tabla de una carpeta cuyo nombre empieza por el patrón. Con `pdf`, también
    el PDF —el extracto que el banco entrega así—, después de cualquier CSV o Excel."""
    if not carpeta.is_dir():
        return []
    tipos = (".csv", ".xlsx", ".pdf") if pdf else (".csv", ".xlsx")
    return sorted((p for p in carpeta.iterdir()
                   if p.is_file() and not p.name.startswith(".") and p.suffix.lower() in tipos
                   and norm(p.stem).startswith(norm(patron))),
                  key=lambda p: (p.suffix.lower() == ".pdf", p.name))


def cargar_config(ruta: Path) -> tuple[dict, Path]:
    cfg = leer_json(ruta)
    if cfg is None:
        raise SystemExit(f"{ruta} no existe: corre el setup del agente")
    # Las rutas relativas se resuelven desde la carpeta donde vive `.criterio/`, no desde donde
    # esté parada la sesión: un `cd` previo dejaba el estado escrito en otra parte y levantaba
    # señales sobre una carpeta vacía.
    r = Path(ruta).resolve()
    base = next((x.parent for x in r.parents if x.name == ".criterio"), Path.cwd())

    def ruta_de(k):
        v = (cfg.get("paths") or {}).get(k)
        if not v:
            return None
        p = Path(v).expanduser()
        return p if p.is_absolute() else base / p
    cfg["_docs"], cfg["_estado"] = ruta_de("documents"), ruta_de("state")
    cfg["_raiz"] = base
    return cfg, ruta


# ================================================================ la estructura recomendada

def estructura(ruta: Path) -> dict:
    """La estructura recomendada de la familia, como la deja `scripts/familias.py` junto al motor."""
    return leer_json(ruta, {"niveles": []}) or {"niveles": []}


def _nivel_de(partes: list[str], est: dict):
    """El nivel de la estructura al que pertenece una ruta, y cuántas partes forman su carpeta."""
    for n in est.get("niveles", []):
        if not n.get("ruta"):
            continue
        k = n.get("profundidad", 1)
        if len(partes) > k and re.fullmatch(n["ruta"], "/".join(partes[:k])):
            return n, k
    base = next((n for n in est.get("niveles", []) if not n.get("ruta")), {"id": "entidad", "carpetas": []})
    return base, 0


def clasificar(ruta_rel: str, est: dict) -> dict:
    """Dónde está un archivo, y dónde iría según la estructura recomendada (ADR 0007)."""
    partes = ruta_rel.split("/")
    nivel, k = _nivel_de(partes, est)
    out = {"nivel": nivel["id"], "instancia": "/".join(partes[:k]) or None, "carpeta": None, "en_su_lugar": False, "iria": None}
    sub = partes[k] if len(partes) > k + 1 else None
    if sub in [c["carpeta"] for c in nivel.get("carpetas", [])]:
        out["carpeta"] = sub
    nombre = norm(partes[-1])
    destino = None
    for n in est.get("niveles", []):
        for c in n.get("carpetas", []):
            if any(re.search(pat, nombre) for pat in c.get("patrones", [])):
                destino = (n, c["carpeta"])
                break
        if destino:
            break
    if destino and out["carpeta"] == destino[1] and out["nivel"] == destino[0]["id"]:
        out["en_su_lugar"] = True
    elif destino:
        out["iria"] = (destino[0].get("etiqueta") or "") + destino[1] + "/"
    else:
        out["en_su_lugar"] = out["carpeta"] is not None
    return out


TABLAS = {".csv", ".xlsx"}
LEGIBLES = TABLAS | {".xml", ".md", ".txt", ".docx", ".pdf", ".eml", ".pptx", ".html"}


def inventario(docs: Path, estado: Path | None, est: dict) -> dict:
    """Qué hay, qué cambió desde la corrida anterior y qué está fuera de su lugar."""
    previo = leer_json(estado / "indice.json", {}) if estado else {}
    previo = previo or {}
    archivos, nuevos, cambiados, fuera, ilegibles = {}, [], [], [], []
    instancias: dict[str, set] = {}
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import raiz  # el archivo que marca la raíz es del agente, no un documento (ADR 0011)
    for p in sorted(docs.rglob("*")):
        if not p.is_file() or p.name.startswith(".") or any(x.startswith(".") for x in p.relative_to(docs).parts) \
                or raiz.es_marcador(p.name):
            continue
        r = p.relative_to(docs).as_posix()
        h = sha256(p)
        cl = clasificar(r, est)
        if cl["instancia"]:
            instancias.setdefault(cl["nivel"], set()).add(cl["instancia"])
        archivos[r] = {"sha256": h, "bytes": p.stat().st_size, "nivel": cl["nivel"], "carpeta": cl["carpeta"]}
        if r not in previo.get("archivos", {}):
            nuevos.append(r)
        elif previo["archivos"][r]["sha256"] != h:
            cambiados.append(r)
        if not cl["en_su_lugar"]:
            fuera.append({"archivo": r, "iria": cl["iria"]})
        if p.suffix.lower() not in LEGIBLES:
            ilegibles.append({"archivo": r, "motivo": f"formato {p.suffix.lower() or 'sin extensión'} no soportado"})
    borrados = sorted(set(previo.get("archivos", {})) - set(archivos))
    out = {"archivos": archivos, "total": len(archivos), "nuevos": nuevos, "cambiados": cambiados,
           "borrados": borrados, "fuera_de_lugar": fuera, "ilegibles": ilegibles,
           "instancias": {k: sorted(v) for k, v in sorted(instancias.items())}, "por_carpeta": {}}
    for r, a in archivos.items():
        k = (a["nivel"] or "?") + ":" + (a["carpeta"] or "(fuera de la estructura)")
        out["por_carpeta"][k] = out["por_carpeta"].get(k, 0) + 1
    return out


CRITICIDAD = {"alta": 1, "media": 2, "baja": 3}


def alerta(signal: str, detalle: str, cita: dict | list | None = None, monto: float | None = None,
           responsable: str | None = None, dias: int | None = None, severidad: int | None = None,
           clave: str | None = None) -> dict:
    return {"signal": signal, "detail": detalle, "cite": cita, "amount": redondo(monto),
            "owner": responsable, "age_days": dias, "severity": severidad or SEVERIDAD.get(signal, 3),
            "key": clave or detalle}


def ordenar(alertas: list[dict]) -> list[dict]:
    return sorted(alertas, key=lambda a: (a["severity"], -abs(a["amount"] or 0), -(a["age_days"] or 0), a["signal"], a["key"]))


# ---------------------------------------------------------------- los compromisos
# Las reglas de compromiso de la familia PMO, comunes a Samuel, a Vera y a Ofelia (ADR 0012). Un
# compromiso viene de una ficha: cada campo es un valor o {value, source, source_date, state}.
# Salen de aquí iguales para todos: el resultado y los textos no cambian según quién los llame.

def valor_campo(campo):
    """El valor de un campo de ficha. `not_found` es un estado, nunca un valor: la ficha que lo
    escribe como valor dice que el campo está vacío."""
    if isinstance(campo, dict) and "value" in campo:
        campo = campo["value"]
    if isinstance(campo, str) and campo.strip().lower() == "not_found":
        return None
    return campo


def fuente_campo(campo):
    return campo.get("source") if isinstance(campo, dict) else None


def fecha_campo(campo) -> dt.date | None:
    v = valor_campo(campo)
    if not v:
        return None
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def compromisos(lista: list, hoy: dt.date, reprogramaciones: int) -> dict:
    """Los compromisos vencidos, los que nadie fechó y los reprogramados, y lo que la ficha tiene
    que corregir. `reprogramaciones` es el umbral: cuántas veces se movió para que suene."""
    vencidos, sin_fecha, reprogramados, arreglos = [], [], [], []
    for c in lista or []:
        due = fecha_campo(c.get("due_date"))
        st = valor_campo(c.get("state"))
        quien = valor_campo(c.get("who"))
        que = valor_campo(c.get("what"))
        fuente = fuente_campo(c.get("what")) or valor_campo(c.get("source"))
        if due is None:
            # El skill registra un compromiso sin fecha como `no_declarada`. No puede estar
            # vencido, y por eso mismo desaparecía del informe. Un compromiso que nadie fechó es
            # un hallazgo, no un vacío.
            sin_fecha.append({"who": quien, "what": que, "source": fuente})
        # Vencido es aritmética, no una etiqueta: lo que no está cumplido y tiene la fecha atrás
        # está vencido, lo haya marcado el modelo `overdue` o no. En la fase 2 el agente escribió
        # `state: overdue` y la regla, que solo miraba `open`, dejó pasar el único vencido del caso.
        elif due < hoy and st != "met":
            vencidos.append({"who": quien, "what": que, "due": due.isoformat(),
                             "days": (hoy - due).days, "source": fuente})
        veces = len(c.get("reschedules") or [])
        # Fechar no es reprogramar: si la promesa original no tenía fecha, la primera que se le
        # puso es su fecha, no una reprogramación (rondas 3 y 4 de la PMO). El conteo se corrige
        # aquí aunque la ficha la traiga así, y se le dice a quien la escribe qué corregir: el
        # núcleo no reescribe una ficha, que tiene un solo escritor (ronda 6, minería: D042).
        if veces and valor_campo(c.get("original_due_date")) == "no_declarada":
            veces -= 1
            arreglos.append({
                "who": quien, "what": que, "field": "commitments.reschedules",
                "fix": "la promesa no tenía fecha: la primera que se le puso va en "
                       "original_due_date y sale de reschedules"})
        # Un compromiso cumplido con acta ya no es un bloqueo: su historia queda en la ficha, pero
        # la señal es para lo que sigue abierto (ronda 5, minería).
        if veces >= reprogramaciones and st != "met":
            reprogramados.append({"who": quien, "what": que, "times": veces,
                                  "original": valor_campo(c.get("original_due_date")),
                                  "dates": [valor_campo(r.get("due_date")) for r in c.get("reschedules") or []]})
    return {"vencidos": vencidos, "sin_fecha": sin_fecha, "reprogramados": reprogramados, "arreglos": arreglos}


def _m(x) -> str:
    return "—" if x is None else f"{mon(x)}"


def _nombres() -> dict:
    """Los nombres en palabras de las señales y los comandos de la familia (`nombres.json`, que
    escribe scripts/familias.py). Sin el archivo, el reporte sale con el código, como antes."""
    try:
        return json.loads((Path(__file__).resolve().parent / "nombres.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


NOMBRES = _nombres()


def nombre_senal(s: str) -> str:
    """«Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`)»."""
    n = (NOMBRES.get("senales") or {}).get(s)
    return f"{n} (`{s}`)" if n else f"`{s}`"


def nombre_comando(c: str) -> str:
    return (NOMBRES.get("comandos") or {}).get(c) or c


def _cita(c) -> str:
    if not c:
        return ""
    if isinstance(c, list):
        return " · ".join(_cita(x) for x in c if x)
    return f"`{c.get('archivo')}`" + (f" fila {c['fila']}" if c.get("fila") else "")


def marco_reporte(r: dict, comando: str, version: str, *, agente: str, senales: set | None, alcance: str,
                  cuerpo, extra: str = "", familia: str = "") -> str:
    """El reporte en el orden común a todos los agentes: encabezado, lo que hay que atender, el
    resultado, lo que no se pudo procesar, las preguntas que hizo y las fuentes. Toda cifra sale
    de `r`; el resultado lo escribe `cuerpo(r, comando, parte)` de cada motor."""
    ent = r.get("entidad") or {}
    _PAIS[0] = pais_de(ent)
    alertas = [a for a in r["alertas"] if senales is None or a["signal"] in senales]
    l = [f"# {nombre_comando(comando)} · {ent.get('name')} · {alcance}", "",
         f"**Entidad:** {ent.get('name')} ({ent.get('id')}) · **Fecha de corte:** {r.get('corte')} · **Procesado:** {r.get('hoy')} · **Agente:** {agente}, versión {version}{extra} · **Comando:** `{comando}`", ""]
    l += ["## Lo que hay que atender", ""]
    if alertas:
        l += ["| # | Señal | Qué | Monto | Responsable | Días | Cita |", "|---|---|---|---|---|---|---|"]
        for i, a in enumerate(alertas, 1):
            l.append(f"| {i} | {nombre_senal(a['signal'])} | {a['detail'].replace('|', '/')} | {_m(a['amount'])} | {a['owner'] or '—'} | {a['age_days'] if a['age_days'] is not None else '—'} | {_cita(a['cite'])} |")
    else:
        l.append("Nada abierto en lo que procesa este comando.")
    l += ["", "## El resultado", ""]
    p = (r.get("partes") or {}).get(comando)
    l += cuerpo(r, comando, p)
    no = list(r.get("no_procesado") or []) + list((p or {}).get("no_procesado") or [])
    l += ["## Lo que no se pudo procesar", ""]
    l += [f"- `{x['archivo']}`: {x['motivo']}" for x in no] or ["Todo lo que llegó se procesó."]
    l += ["", "## Las preguntas que hizo", ""]
    l += [f"- {q['question']} → {q['answer']}" for q in (r.get("preguntas") or [])] or ["Ninguna en esta corrida."]
    citas = sorted({c["archivo"] for a in alertas for c in (a["cite"] if isinstance(a["cite"], list) else [a["cite"]]) if c and c.get("archivo")})
    fuentes = sorted(set((p or {}).get("fuentes") or []))
    l += ["", "## Fuentes", ""]
    l += [f"- `{c}`" for c in citas] or ["- Sin documentos citados."]
    if fuentes:
        l.append("- Fuentes técnicas: " + ", ".join(fuentes) + f" (families/{familia}/FUENTES.es.md)")
    return "\n".join(l) + "\n"


# ================================================================ el registro de las corridas

CASO = re.compile(r"\b([A-Z]{2,5}-\d{2,})\b")


def registro_corridas(estado: Path) -> list[dict]:
    """Las corridas del estado, con `comando` y `fecha`. Las del registro anterior a la 0.7.0,
    `corridas/registro.json`, se leen también: la historia no se pierde por cambiar de formato."""
    nuevas = leer_json(estado / "corridas.json", []) or []
    viejas = leer_json(estado / "corridas" / "registro.json", []) or []
    return [dict(c, comando=c.get("que")) for c in nuevas] + viejas


def _ambito(r: dict) -> str:
    return str(r.get("periodo") or r.get("anio") or r.get("year") or r.get("agente") or "-")


def corrida(estado: Path, que: str, salida: Path | None, caso: str | None, nota: str | None, hoy: dt.date,
            r: dict | None = None, version: str | None = None) -> dict:
    """Deja la corrida en el formato común: qué se corrió, sobre qué, qué encontró y lo que el
    comando mostró. Los hallazgos salen de lo que el motor calculó (`r`), no de lo que el agente
    diga; por caso, el código que trae la clave de la señal —un contrato, un proyecto— o el ámbito
    de la corrida, para que se pueda saber después desde cuándo se arrastra cada una."""
    import time
    from collections import Counter
    carpeta = estado / "corridas"
    carpeta.mkdir(parents=True, exist_ok=True)
    f = estado / "corridas.json"
    previas = leer_json(f, []) or []
    n = 1 + sum(1 for c in previas if c.get("que") == que and c.get("fecha") == hoy.isoformat())
    ident = f"{hoy.isoformat()}-{que}-{n}"
    alertas = (r or {}).get("alertas") or []
    por_senal = Counter(a["signal"] for a in alertas)
    por_caso: dict[str, list] = {}
    for a in alertas:
        m = CASO.search(str(a.get("key") or ""))
        por_caso.setdefault(m.group(1) if m else _ambito(r), []).append(a["signal"])
    cuerpo = salida.read_text(encoding="utf-8").strip() if salida and salida.is_file() else ""
    entrada = {"id": ident, "que": que, "fecha": hoy.isoformat(), "caso": caso, "plugin": {"version": version},
               "hallazgos": len(alertas) if r is not None else None, "por_senal": dict(por_senal.most_common()),
               "por_caso": {k: sorted(v) for k, v in sorted(por_caso.items())}, "salida": bool(cuerpo),
               "escrita": time.time(), "nota": nota}
    lineas = [f"# Corrida del {hoy.isoformat()} · {nombre_comando(que)}", "",
              (f"Caso: {caso} · " if caso else "") + (f"{len(alertas)} hallazgos" if r is not None else "sin cálculo"), ""]
    if por_senal:
        lineas += ["| Señal | Hallazgos |", "|---|---:|"] + [f"| {nombre_senal(s)} | {k} |" for s, k in por_senal.most_common()] + [""]
    if nota:
        lineas += [nota, ""]
    lineas += ["## Lo que produjo", "", cuerpo or "_(el comando no dejó su salida)_", ""]
    (carpeta / f"{ident}.md").write_text("\n".join(lineas), encoding="utf-8")
    previas.append(entrada)
    escribir_json(f, previas)
    return {"registrada": f"{ident}.md", "id": ident, "hallazgos": entrada["hallazgos"]}


# ================================================================ las peticiones

def peticiones_abiertas(estado: Path, agente: str | None = None) -> list[dict]:
    """Las que alguien dejó en Rostrum para este agente y nadie ha respondido, de la más vieja
    a la más nueva. Las escribe el servidor; el agente solo las responde. Dos agentes de una
    familia comparten el estado, así que cada uno toma las que van para él (`agente`)."""
    out = []
    for f in sorted((estado / "peticiones").glob("*.json")) if (estado / "peticiones").is_dir() else []:
        p = leer_json(f, None)
        if isinstance(p, dict) and not p.get("respondida") and (agente is None or p.get("agente") in (None, agente)):
            out.append(p)
    return out


def responder_peticion(estado: Path, ident: str, hoy: dt.date) -> dict:
    """Marca una petición como respondida. Es lo único que el agente le escribe."""
    f = estado / "peticiones" / f"{ident}.json"
    p = leer_json(f, None)
    if not isinstance(p, dict) or not re.fullmatch(r"[A-Za-z0-9._-]+", ident):
        return {"ok": False, "motivo": f"no hay petición {ident}"}
    p["respondida"] = hoy.isoformat()
    escribir_json(f, p)
    return {"ok": True, "id": ident, "respondida": p["respondida"]}


def _hoy(a) -> dt.date:
    return dt.date.fromisoformat(a.today) if a.today else dt.date.today()


def _xlsx(ruta: Path, filas: list[list]) -> None:
    """Un .xlsx mínimo, con cadenas en línea: lo justo para probar el lector."""
    def celda(i, j, v):
        ref = ""
        k = j + 1
        while k:
            k, r = divmod(k - 1, 26)
            ref = chr(65 + r) + ref
        ref += str(i + 1)
        if isinstance(v, (int, float)):
            return f'<c r="{ref}"><v>{v}</v></c>'
        t = str(v).replace("&", "&amp;").replace("<", "&lt;")
        return f'<c r="{ref}" t="inlineStr"><is><t>{t}</t></is></c>'
    hoja = "".join(f'<row r="{i + 1}">' + "".join(celda(i, j, v) for j, v in enumerate(f) if v != "") + "</row>" for i, f in enumerate(filas))
    with zipfile.ZipFile(ruta, "w") as z:
        z.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
        z.writestr("xl/workbook.xml", f'<workbook xmlns="{S[1:-1]}"><sheets><sheet name="Hoja1" sheetId="1"/></sheets></workbook>')
        z.writestr("xl/worksheets/sheet1.xml", f'<worksheet xmlns="{S[1:-1]}"><sheetData>{hoja}</sheetData></worksheet>')


# El ancho de cada carácter en Helvetica, en milésimas del cuerpo: lo justo para alinear una cifra
# a la derecha. Lo que no está aquí se cuenta como un dígito.
_ANCHO = {**{c: 556 for c in "0123456789$"}, ".": 278, ",": 278, "-": 333, " ": 278, "(": 333, ")": 333}


def _pdf_tabla(ruta: Path, titulo: list[str], filas: list[list], columnas: list[tuple[int, str]],
               cuerpo: int = 8) -> None:
    """Un PDF con capa de texto y una tabla, como el extracto que entrega un banco: el título arriba,
    la cabecera repetida en cada página, cada celda en su columna (`(x, "i")` a la izquierda, `(x,
    "d")` alineada a la derecha en x). Lo usan la prueba del lector y el material de prueba."""
    def esc(t):
        b = str(t).encode("cp1252", errors="replace")
        return "".join(f"\\{c:03o}" if c > 126 or c in (40, 41, 92) else chr(c) for c in b)

    def linea(celdas, y):
        out = ""
        for (x, al), v in zip(columnas, celdas):
            v = str(v)
            if al == "d":
                x = x - sum(_ANCHO.get(c, 556) for c in v) * cuerpo / 1000
            out += f"BT /F1 {cuerpo} Tf {x:.1f} {y} Td ({esc(v)}) Tj ET\n"
        return out
    paginas, flujo, y = [], "", 790
    for t in titulo:
        flujo += f"BT /F1 {cuerpo + 2} Tf 40 {y} Td ({esc(t)}) Tj ET\n"
        y -= cuerpo + 8
    flujo, y = flujo + linea(filas[0], y - 6), y - 6 - (cuerpo + 6)
    for f in filas[1:]:
        if y < 50:
            paginas.append(flujo)
            flujo, y = linea(filas[0], 790), 790 - (cuerpo + 6)
        flujo += linea(f, y)
        y -= cuerpo + 5
    paginas.append(flujo)
    objs = ["<< /Type /Catalog /Pages 2 0 R /Lang (es) >>", None,
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"]
    kids = []
    for pg in paginas:
        objs.append(f"<< /Length {len(pg.encode('latin-1'))} >>\nstream\n{pg}endstream")
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 3 0 R >> >> /Contents {len(objs)} 0 R >>")
        kids.append(len(objs))
    objs[1] = f"<< /Type /Pages /Kids [{' '.join(f'{k} 0 R' for k in kids)}] /Count {len(kids)} >>"
    salida, offs = "%PDF-1.4\n", []
    for i, o in enumerate(objs, start=1):
        offs.append(len(salida.encode("latin-1")))
        salida += f"{i} 0 obj\n{o}\nendobj\n"
    xref = len(salida.encode("latin-1"))
    salida += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n" + "".join(f"{o:010d} 00000 n \n" for o in offs)
    salida += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(salida.encode("latin-1"))


def _csv(ruta: Path, filas: list[list]) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter=";").writerows(filas)


# ================================================================ la línea de comandos, igual en todos los motores

def plugin(aqui: Path) -> dict:
    """El nombre y la versión del plugin instalado, de su manifiesto."""
    m = leer_json(aqui.parent / ".claude-plugin" / "plugin.json", {}) or {}
    return {"name": m.get("name"), "version": m.get("version", "?")}


def argumentos(descripcion: str):
    import argparse
    ap = argparse.ArgumentParser(description=descripcion)
    for op, t in (("--config", Path), ("--state", Path), ("--docs", Path), ("--salida", Path), ("--file", Path)):
        ap.add_argument(op, type=t)
    for op in ("--period", "--year", "--today", "--what", "--caso", "--nota", "--por", "--idioma", "--id", "--entidad"):
        ap.add_argument(op)
    return ap


# La carpeta de la configuración de cada agente, `.criterio/<area>/<entidad>/config.json`. Es la
# misma `area` de families/criterio-<familia>/familia.json, y scripts/familias.py comprueba que
# coincidan. Dos agentes que comparten el estado no comparten la configuración.
AREA = {"criterio-finance": "finanzas", "criterio-budget": "presupuesto", "criterio-treasury": "tesoreria",
        "criterio-legal": "legal", "criterio-compliance": "cumplimiento", "criterio-assistant": "direccion"}


def despachar(a, ap, *, aqui: Path, rol: str, estructura_json: Path, subcarpetas: tuple, revisar_config, calcular,
              reporte, despertar) -> int:
    """Las acciones que todos los motores hacen igual. Las propias de cada uno las atiende el motor
    antes de llegar aquí."""
    import sys
    area = AREA.get(plugin(aqui).get("name"))
    if area and getattr(a, "config", None) and Path(a.config).resolve().parent.parent.name != area:
        print(json.dumps({"ok": False, "motivo": f"{a.config} no es una configuración de este agente: la suya va en "
                          f".criterio/{area}/<entidad>/config.json, aunque comparta el estado con otro agente"},
                         ensure_ascii=False))
        return 1
    if a.action in ("terminos", "aceptar"):
        if not a.config:
            ap.error("--config es obligatorio")
        sys.path.insert(0, str(aqui))
        import terminos
        if a.action == "terminos":
            r = terminos.estado(a.config)
            print(json.dumps(r, ensure_ascii=False, indent=2))
            return 0 if r["vigente"] else 3
        print(json.dumps(terminos.aceptar(a.config, a.por, a.idioma, _hoy(a) if a.today else None), ensure_ascii=False, indent=2))
        return 0
    if a.action in ("buscar-raiz", "marcar-raiz"):
        # La carpeta raíz: se busca por su marca y por la estructura que tiene adentro, y se marca solo
        # con el sí de la persona (ADR 0011).
        sys.path.insert(0, str(aqui))
        import raiz
        if a.action == "buscar-raiz":
            print(json.dumps(raiz.buscar(a.docs or Path.cwd(), plugin(aqui)["name"]), ensure_ascii=False, indent=2))
            return 0
        if not a.docs:
            ap.error("--docs es la carpeta que la persona eligió")
        r = raiz.marcar(a.docs, plugin(aqui)["name"], a.entidad, a.por)
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 0 if r["ok"] else 1
    if a.action == "init":
        if not a.state:
            ap.error("--state es obligatorio")
        for sub in tuple(subcarpetas) + ("corridas", "cache"):
            (a.state / sub).mkdir(parents=True, exist_ok=True)
        print(json.dumps({"estado": str(a.state), "listo": True}, ensure_ascii=False))
        return 0
    if a.action == "inventario":
        docs, estado = a.docs, a.state
        if a.config:
            cfg, _ = cargar_config(a.config)
            docs, estado = docs or cfg["_docs"], estado or cfg["_estado"]
        if not docs:
            ap.error("--docs o --config")
        inv = inventario(docs, estado, estructura(estructura_json))
        if estado:
            escribir_json(estado / "indice.json", {"archivos": inv["archivos"], "fecha": iso(_hoy(a))})
        print(json.dumps({k: v for k, v in inv.items() if k != "archivos"}, ensure_ascii=False, indent=2))
        return 0
    if a.action == "convertir":
        sys.path.insert(0, str(aqui))
        import texto
        cfg, _ = cargar_config(a.config)
        print(json.dumps(texto.convertir(cfg["_docs"], cfg["_estado"] / "cache", a.caso), ensure_ascii=False, indent=2)[:20000])
        return 0
    if not a.config:
        ap.error("--config es obligatorio")
    cfg, _ = cargar_config(a.config)
    if a.action == "config":
        p = revisar_config(cfg, rol)
        print(json.dumps({"ok": not p, "problemas": p, "entidad": cfg.get("entity"), "documentos": str(cfg["_docs"]),
                          "estado": str(cfg["_estado"])}, ensure_ascii=False, indent=2))
        return 0 if not p else 1
    if a.action == "compute":
        r, destino = calcular(cfg, rol, a)
        cuenta: dict[str, int] = {}
        for x in r["alertas"]:
            cuenta[x["signal"]] = cuenta.get(x["signal"], 0) + 1
        print(json.dumps({"resultados": str(destino), "senales": cuenta, "total": len(r["alertas"]),
                          "record_issues": r["record_issues"], "no_procesado": len(r.get("no_procesado") or []) +
                          sum(len(p.get("no_procesado") or []) for p in r["partes"].values())}, ensure_ascii=False, indent=2))
        return 0
    if a.action == "reporte":
        if not a.what:
            ap.error("--what es el comando cuyo reporte se escribe")
        r, destino = calcular(cfg, rol, a)
        md = reporte(r, a.what, plugin(aqui)["version"])
        (destino.parent / f"reporte-{a.what}.md").write_text(md, encoding="utf-8")
        print(md)
        return 0
    if a.action == "despertar":
        d = despertar(cfg, rol, _hoy(a))
        # Una petición que alguien dejó en Rostrum despierta al agente aunque no toque nada más.
        d["peticiones"] = peticiones_abiertas(cfg["_estado"], rol)
        d["callado"] = d.get("callado", False) and not d["peticiones"]
        print(json.dumps(d, ensure_ascii=False, indent=2))
        return 0
    if a.action == "responder":
        if not a.id:
            ap.error("--id es la petición que se respondió")
        print(json.dumps(responder_peticion(cfg["_estado"], a.id, _hoy(a)), ensure_ascii=False))
        return 0
    if a.action == "corrida":
        if not a.what:
            ap.error("--what es el comando que corrió")
        try:
            r, _ = calcular(cfg, rol, a)
        except (SystemExit, Exception):  # una corrida que no se puede calcular se registra igual
            r = None
        print(json.dumps(corrida(cfg["_estado"], a.what, a.salida, a.caso, a.nota, _hoy(a), r, plugin(aqui)["version"]),
                         ensure_ascii=False))
        return 0
    return 1
