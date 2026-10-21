#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El núcleo de los motores de las familias CFO y CLO: lo que es igual en cualquier función.

Números y fechas como llegan en las exportaciones, tablas en CSV y Excel con su fila de
origen, la estructura recomendada y el inventario de la carpeta, las señales, el marco común
del reporte y el registro de cada corrida. Lo propio de cada función vive en su motor
—`finanzas.py`, `legal.py`—, que importa esto.

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


_PAIS = ["CO"]


def mon(x) -> str:
    """Una cifra como se lee en el país de la entidad: 1.234.567,89 en Colombia, 1,234,567.89 en Ecuador."""
    if x is None:
        return "—"
    t = f"{x:,.2f}"
    return t.replace(",", "§").replace(".", ",").replace("§", ".") if _PAIS[0] == "CO" else t


def pc(x: float, signo: bool = False) -> str:
    t = f"{x:+.1f}" if signo else f"{x:.1f}"
    return t.replace(".", ",") if _PAIS[0] == "CO" else t


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


def filas_de(ruta: Path) -> list[list[str]]:
    ext = ruta.suffix.lower()
    if ext == ".xlsx":
        return xlsx_filas(ruta)
    if ext in (".csv", ".txt", ".tsv"):
        return csv_filas(ruta)
    raise ValueError(f"{ruta.name}: una tabla llega en .csv o .xlsx, no en {ext}")


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


def buscar(carpeta: Path, patron: str) -> list[Path]:
    """Los archivos de tabla de una carpeta cuyo nombre empieza por el patrón."""
    if not carpeta.is_dir():
        return []
    return sorted(p for p in carpeta.iterdir()
                  if p.is_file() and not p.name.startswith(".") and p.suffix.lower() in (".csv", ".xlsx")
                  and norm(p.stem).startswith(norm(patron)))


def cargar_config(ruta: Path) -> tuple[dict, Path]:
    cfg = leer_json(ruta)
    if cfg is None:
        raise SystemExit(f"{ruta} no existe: corre el setup del agente")
    base = Path.cwd()

    def ruta_de(k):
        v = (cfg.get("paths") or {}).get(k)
        if not v:
            return None
        p = Path(v).expanduser()
        return p if p.is_absolute() else base / p
    cfg["_docs"], cfg["_estado"] = ruta_de("documents"), ruta_de("state")
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
    for p in sorted(docs.rglob("*")):
        if not p.is_file() or p.name.startswith(".") or any(x.startswith(".") for x in p.relative_to(docs).parts):
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


def _m(x) -> str:
    return "—" if x is None else f"{mon(x)}"


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
    _PAIS[0] = (ent.get("country") or "CO").upper()
    alertas = [a for a in r["alertas"] if senales is None or a["signal"] in senales]
    l = [f"# {comando} · {ent.get('name')} · {alcance}", "",
         f"**Entidad:** {ent.get('name')} ({ent.get('id')}) · **Fecha de corte:** {r.get('corte')} · **Procesado:** {r.get('hoy')} · **Agente:** {agente}, versión {version}{extra}", ""]
    l += ["## Lo que hay que atender", ""]
    if alertas:
        l += ["| # | Señal | Qué | Monto | Responsable | Días | Cita |", "|---|---|---|---|---|---|---|"]
        for i, a in enumerate(alertas, 1):
            l.append(f"| {i} | `{a['signal']}` | {a['detail'].replace('|', '/')} | {_m(a['amount'])} | {a['owner'] or '—'} | {a['age_days'] if a['age_days'] is not None else '—'} | {_cita(a['cite'])} |")
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


def registro_corridas(estado: Path) -> list[dict]:
    return leer_json(estado / "corridas" / "registro.json", []) or []


def corrida(estado: Path, que: str, salida: Path | None, caso: str | None, nota: str | None, hoy: dt.date) -> dict:
    carpeta = estado / "corridas"
    carpeta.mkdir(parents=True, exist_ok=True)
    reg = registro_corridas(estado)
    n = 1 + sum(1 for c in reg if c["comando"] == que and c["fecha"] == hoy.isoformat())
    nombre = f"{hoy.isoformat()}-{que}-{n}.md"
    cuerpo = salida.read_text(encoding="utf-8") if salida and salida.is_file() else ""
    (carpeta / nombre).write_text(f"<!-- corrida {que} · {hoy.isoformat()} · caso {caso or '—'} -->\n\n{cuerpo}\n\n---\n\n{nota or ''}\n", encoding="utf-8")
    reg.append({"fecha": hoy.isoformat(), "comando": que, "caso": caso, "archivo": nombre, "nota": nota})
    escribir_json(carpeta / "registro.json", reg)
    return {"registrada": nombre}


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
    for op in ("--period", "--year", "--today", "--what", "--caso", "--nota", "--por", "--idioma"):
        ap.add_argument(op)
    return ap


def despachar(a, ap, *, aqui: Path, rol: str, estructura_json: Path, subcarpetas: tuple, revisar_config, calcular,
              reporte, despertar) -> int:
    """Las acciones que todos los motores hacen igual. Las propias de cada uno las atiende el motor
    antes de llegar aquí."""
    import sys
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
        print(json.dumps(despertar(cfg, rol, _hoy(a)), ensure_ascii=False, indent=2))
        return 0
    if a.action == "corrida":
        if not a.what:
            ap.error("--what es el comando que corrió")
        print(json.dumps(corrida(cfg["_estado"], a.what, a.salida, a.caso, a.nota, _hoy(a)), ensure_ascii=False))
        return 0
    return 1
