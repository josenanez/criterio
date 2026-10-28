#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los términos de uso: cuáles rigen esta versión, su huella, y el comprobante de quien acepta.

    python3 terminos.py estado  --config <config>            ¿está vigente la aceptación?
    python3 terminos.py aceptar --config <config> --por "Nombre Apellido" [--idioma es|en]
    python3 terminos.py --selftest

**Una aceptación por versión.** Cada versión de la familia pide aceptar de nuevo, aunque
el texto de los términos no haya cambiado: instalar o actualizar a una versión nueva
exige una aceptación nueva. Lo que queda es una sucesión fechada —quién aceptó, qué
versión, qué texto— y esa sucesión es la trazabilidad.

**El texto se amarra por su huella.** Un número de versión dice qué se aceptó solo si
nadie cambió el texto sin subirlo. La huella SHA-256 del archivo de términos que se le
mostró a la persona sí lo dice: cualquier cambio, por mínimo que sea, da otra huella.

**El comprobante es de la persona.** Queda en `.criterio/terminos/`, en Markdown y en
PDF, con el texto completo aceptado, su nombre, la fecha, la versión de la familia, la
versión y la huella de los términos, y la entrada del registro de versiones. La huella
de cada comprobante queda en la configuración, en el registro de aceptaciones y en un
archivo `.sha256` al lado, que `shasum -a 256 -c` comprueba sin este plugin.

Librería estándar, sin dependencias: un plugin instalado tiene que correr solo.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

RAIZ_PLUGIN = Path(__file__).resolve().parent.parent

# La nota legal de la familia y el registro de versiones viven en el portal, que el
# mantenedor controla, y no solo en el repositorio.
NOTA_LEGAL = {"es": "https://www.josenanez.com/es/agents/criterio-pmo/legal",
              "en": "https://www.josenanez.com/agents/criterio-pmo/legal"}
ARCHIVO = {"es": "TERMS.es.md", "en": "TERMS.md"}
SECCION_CORTA = {"es": "## En corto", "en": "## In short"}


# ---------------------------------------------------------------- lo instalado

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def instalado(raiz: Path = RAIZ_PLUGIN) -> dict:
    meta = json.loads((raiz / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    return {"plugin": meta.get("name"), "version": meta.get("version")}


def terminos(idioma: str = "es", raiz: Path = RAIZ_PLUGIN) -> dict:
    f = raiz / ARCHIVO.get(idioma, ARCHIVO["es"])
    if not f.is_file():
        raise SystemExit(f"faltan los términos en el plugin instalado: {f}. Reinstala el plugin.")
    texto = f.read_text(encoding="utf-8")
    m = re.search(r"(?:Versión|Version) (\d+(?:\.\d+)*) · (\d{4}-\d{2}-\d{2})", texto)
    corto = ""
    i = texto.find(SECCION_CORTA.get(idioma, SECCION_CORTA["es"]))
    if i != -1:
        resto = texto[i:].split("\n", 1)[1]
        corto = re.split(r"\n## |\n---", resto, maxsplit=1)[0].strip()
        cita = [x[1:].strip() for x in corto.splitlines() if x.startswith(">")]
        corto = " ".join(cita) if cita else corto     # lo que se muestra es la cita, tal cual
    return {"archivo": f.name, "ruta": f, "texto": texto, "sha256": sha256(f),
            "version": m.group(1) if m else None, "fecha": m.group(2) if m else None,
            "en_corto": corto}


def entrada_registro(version: str, raiz: Path = RAIZ_PLUGIN) -> dict | None:
    """La entrada del registro donde este plugin llegó a su versión. Cada familia lleva su número
    (decisión 0017): una entrada nueva anota la versión de cada plugin; una anterior, una sola."""
    f = raiz / "REGISTRO.json"
    if not f.is_file():
        return None
    plugin = instalado(raiz).get("plugin")
    for e in json.loads(f.read_text(encoding="utf-8")).get("versiones", []):
        if e.get("versiones", {}).get(plugin, e.get("version")) == version:
            return e
    return None


# ---------------------------------------------------------------- la configuración

def carpeta_terminos(config: Path) -> Path:
    """`.criterio/terminos/`, junto a la configuración de cualquier agente."""
    for p in [config.resolve().parent, *config.resolve().parents]:
        if p.name == ".criterio":
            return p / "terminos"
    return config.resolve().parent / "terminos"


def _canon(d: dict) -> bytes:
    return json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sellar(d: dict) -> dict:
    d = {k: v for k, v in d.items() if k != "sha256"}
    d["sha256"] = hashlib.sha256(_canon(d)).hexdigest()
    return d


def estado(config: Path, raiz: Path = RAIZ_PLUGIN) -> dict:
    """¿La aceptación registrada rige para lo que está instalado? Si no, por qué."""
    inst = instalado(raiz)
    out = {"vigente": False, "motivos": [], "instalada": inst["version"], "plugin": inst["plugin"]}
    if not config.is_file():
        out["motivos"].append(f"{config} no existe: corre la configuración del agente")
        return out
    cfg = json.loads(config.read_text(encoding="utf-8"))
    idioma = ((cfg.get("report") or {}).get("language") or "es")[:2]
    t = terminos(idioma, raiz)
    out.update({"idioma": idioma, "terminos": {"version": t["version"], "archivo": t["archivo"],
                                                "sha256": t["sha256"]},
                "en_corto": t["en_corto"], "nota_legal": NOTA_LEGAL.get(idioma, NOTA_LEGAL["es"])})
    a = cfg.get("terms_accepted") or {}
    out["aceptada"] = a.get("family_version")
    if not a:
        out["motivos"].append("no hay aceptación registrada")
    else:
        if a.get("family_version") != inst["version"]:
            out["motivos"].append(f"la aceptación es de la versión {a.get('family_version') or 'sin versión'} "
                                  f"y la instalada es la {inst['version']}: cada versión se acepta de nuevo")
        if a.get("terms_sha256") != t["sha256"]:
            out["motivos"].append("la huella de los términos aceptados no es la de los términos instalados")
        base = config.resolve().parent
        for k in ("receipt_md", "receipt_pdf"):
            ruta = a.get(k)
            if not ruta:
                out["motivos"].append(f"falta el comprobante ({k})")
                continue
            p = Path(ruta) if Path(ruta).is_absolute() else Path.cwd() / ruta
            if not p.is_file():
                p = base / ruta
            if not p.is_file():
                out["motivos"].append(f"no está el comprobante {ruta}")
            elif sha256(p) != a.get(k + "_sha256"):
                out["motivos"].append(f"el comprobante {ruta} cambió después de registrado: su huella no coincide")
    out["vigente"] = not out["motivos"]
    return out


# ---------------------------------------------------------------- el comprobante

TEXTO = {
    "es": {
        "titulo": "Aceptación de términos y condiciones · Criterio",
        "filas": ["Acepta", "Fecha", "Agente", "Versión de la familia", "Términos",
                  "SHA-256 de los términos", "Registro de la versión", "Nota legal y registro de versiones"],
        "terminos": lambda v, f, a: f"versión {v} del {f} · {a}",
        "registro": lambda s: f"entrada SHA-256 {s}" if s else "esta versión no está en el registro",
        "integridad": "Integridad de este documento",
        "nota": ("Este documento conserva su integridad y no puede modificarse. Su huella SHA-256 (SHA-2 de 256 bits) "
                 "queda registrada en la configuración de la instalación, en el registro de aceptaciones "
                 "(`.criterio/terminos/aceptaciones.json`) y en el archivo `.sha256` que lo acompaña. Cualquier cambio, "
                 "por mínimo que sea, produce otra huella y le quita validez como constancia de esta aceptación. "
                 "Se rige por la nota legal de la familia de agentes Criterio, publicada con el registro de versiones "
                 "—qué cambió en cada una, qué términos la rigen y su huella— en {url}."),
        "comprobar": "Para comprobarlo, en la carpeta del comprobante:",
        "mac": "macOS o Linux",
        "win": "Windows: `certutil -hashfile {f} SHA256`, y comparar con el archivo `.sha256`",
        "cada": ("Cada versión de la familia pide aceptar de nuevo, aunque el texto de los términos no haya cambiado, "
                 "y deja un comprobante nuevo. Los anteriores se conservan."),
        "aceptados": "Términos aceptados",
    },
    "en": {
        "titulo": "Acceptance of terms and conditions · Criterio",
        "filas": ["Accepted by", "Date", "Agent", "Family version", "Terms",
                  "Terms SHA-256", "Version register", "Legal notice and version register"],
        "terminos": lambda v, f, a: f"version {v} of {f} · {a}",
        "registro": lambda s: f"entry SHA-256 {s}" if s else "this version is not in the register",
        "integridad": "Integrity of this document",
        "nota": ("This document keeps its integrity and may not be modified. Its SHA-256 fingerprint (SHA-2, 256 bits) "
                 "is recorded in the installation's configuration, in the acceptance log "
                 "(`.criterio/terminos/aceptaciones.json`) and in the `.sha256` file next to it. Any change, however "
                 "small, produces another fingerprint and voids it as a record of this acceptance. "
                 "It is governed by the legal notice of the Criterio agent family, published with the version register "
                 "—what changed in each version, which terms govern it and their fingerprint— at {url}."),
        "comprobar": "To check it, in the receipt's folder:",
        "mac": "macOS or Linux",
        "win": "Windows: `certutil -hashfile {f} SHA256`, and compare with the `.sha256` file",
        "cada": ("Every version of the family asks for acceptance again, even when the terms did not change, "
                 "and leaves a new receipt. Earlier ones are kept."),
        "aceptados": "Terms accepted",
    },
}


def comprobante_md(por: str, fecha: str, inst: dict, t: dict, reg: dict | None,
                   url: str, nombre: str, idioma: str) -> str:
    x = TEXTO.get(idioma, TEXTO["es"])
    valores = [por, fecha, inst["plugin"], inst["version"], x["terminos"](t["version"], t["fecha"], t["archivo"]),
               t["sha256"], x["registro"](reg.get("sha256") if reg else None), f"{url}#v{inst['version']}"]
    filas = "\n".join(f"| {k} | {v} |" for k, v in zip(x["filas"], valores))
    return (f"# {x['titulo']}\n\n| | |\n|---|---|\n{filas}\n\n"
            f"## {x['integridad']}\n\n{x['nota'].format(url=url)}\n\n{x['comprobar']}\n\n"
            f"- {x['mac']}: `shasum -a 256 -c {nombre}.sha256`\n"
            f"- {x['win'].format(f=nombre + '.md')}\n\n{x['cada']}\n\n"
            f"## {x['aceptados']}\n\n{t['texto'].strip()}\n")


# Un PDF con capa de texto, Helvetica y WinAnsi, sin dependencias. Lo justo para que el
# comprobante se pueda archivar, imprimir y reenviar como cualquier documento.

def _plano(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.replace("**", "").replace("`", "").replace("—", "-").replace("–", "-").strip()


def _envolver(s: str, ancho: int = 95) -> list[str]:
    out, linea = [], ""
    for p in s.split():
        if len(linea) + len(p) + 1 > ancho and linea:
            out.append(linea)
            linea = p
        else:
            linea = (linea + " " + p).strip()
    return out + ([linea] if linea else [])


def _pdf_texto(t: str) -> str:
    b = t.encode("cp1252", errors="replace")
    return "".join(f"\\{c:03o}" if c > 126 or c in (40, 41, 92) else chr(c) for c in b)


def lineas_de_md(md: str) -> list[tuple[str, int]]:
    lineas: list[tuple[str, int]] = []
    for crudo in md.splitlines():
        s = crudo.rstrip()
        if not s.strip() or set(s.strip()) <= set("|-: "):
            lineas.append(("", 6))
        elif s.startswith("#"):
            nivel = len(s) - len(s.lstrip("#"))
            lineas += [("", 6), (_plano(s.lstrip("# ")), 14 if nivel == 1 else 12)]
        elif s.startswith("|"):
            celdas = [c for c in (_plano(c) for c in s.strip("|").split("|")) if c]
            fila = f"{celdas[0]}: {'   '.join(celdas[1:])}" if len(celdas) > 1 else " ".join(celdas)
            lineas += [(x, 10) for x in _envolver(fila, 100)]
        else:
            pre = "- " if s.lstrip().startswith(("- ", "* ")) else ""
            cuerpo = s.lstrip()[2:] if pre else s
            lineas += [(x, 10) for x in _envolver(pre + _plano(cuerpo))]
    return lineas


def pdf_de_lineas(lineas: list[tuple[str, int]], destino: Path, idioma: str = "es", titulo: str = "") -> None:
    """El PDF dice su idioma y su título: un lector de pantalla lo lee en español y no anuncia
    un nombre de archivo."""
    paginas, pagina, y = [], [], 790
    for texto, tam in lineas:
        if y < 60:
            paginas.append(pagina)
            pagina, y = [], 790
        if texto:
            pagina.append((texto, tam, y))
        y -= tam + 5
    paginas.append(pagina)
    titulo = titulo or next((x for x, _ in lineas if x), "")
    objs = [f"<< /Type /Catalog /Pages 2 0 R /Lang ({_pdf_texto(idioma)}) "
            f"/ViewerPreferences << /DisplayDocTitle true >> >>", None,
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"]
    kids = []
    for pg in paginas:
        flujo = "".join(f"BT /F1 {t} Tf 50 {y} Td ({_pdf_texto(x)}) Tj ET\n" for x, t, y in pg)
        objs.append(f"<< /Length {len(flujo.encode('latin-1'))} >>\nstream\n{flujo}endstream")
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                    f"/Resources << /Font << /F1 3 0 R >> >> /Contents {len(objs)} 0 R >>")
        kids.append(len(objs))
    objs[1] = f"<< /Type /Pages /Kids [{' '.join(f'{k} 0 R' for k in kids)}] /Count {len(kids)} >>"
    objs.append(f"<< /Title ({_pdf_texto(titulo)}) /Producer (Criterio) >>")
    info = len(objs)
    salida, offs = "%PDF-1.4\n", []
    for i, o in enumerate(objs, start=1):
        offs.append(len(salida.encode("latin-1")))
        salida += f"{i} 0 obj\n{o}\nendobj\n"
    xref = len(salida.encode("latin-1"))
    salida += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n"
    salida += "".join(f"{o:010d} 00000 n \n" for o in offs)
    salida += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R /Info {info} 0 R >>\nstartxref\n{xref}\n%%EOF\n"
    destino.write_bytes(salida.encode("latin-1"))


# ---------------------------------------------------------------- aceptar

def aceptar(config: Path, por: str, idioma: str | None = None, hoy: dt.date | None = None,
            raiz: Path = RAIZ_PLUGIN) -> dict:
    """Registra un sí explícito. Solo se llama después de que la persona lo dijo."""
    por = (por or "").strip()
    if not por:
        raise SystemExit("aceptar: falta --por, el nombre de quien acepta")
    cfg = json.loads(config.read_text(encoding="utf-8")) if config.is_file() else {}
    idioma = (idioma or (cfg.get("report") or {}).get("language") or "es")[:2]
    hoy = hoy or dt.date.today()
    inst, t = instalado(raiz), terminos(idioma, raiz)
    reg = entrada_registro(inst["version"], raiz)
    url = NOTA_LEGAL.get(idioma, NOTA_LEGAL["es"])

    carpeta = carpeta_terminos(config)
    carpeta.mkdir(parents=True, exist_ok=True)
    base = f"aceptacion-{inst['plugin']}-{inst['version']}-{hoy.isoformat()}"
    nombre, n = base, 2
    while (carpeta / f"{nombre}.md").exists():          # nunca se reescribe un comprobante
        nombre, n = f"{base}-{n}", n + 1
    md = carpeta / f"{nombre}.md"
    pdf = carpeta / f"{nombre}.pdf"
    texto = comprobante_md(por, hoy.isoformat(), inst, t, reg, url, nombre, idioma)
    md.write_text(texto, encoding="utf-8")
    pdf_de_lineas(lineas_de_md(texto), pdf, idioma)
    h_md, h_pdf = sha256(md), sha256(pdf)
    (carpeta / f"{nombre}.sha256").write_text(f"{h_md}  {md.name}\n{h_pdf}  {pdf.name}\n", encoding="utf-8")

    bitacora = carpeta / "aceptaciones.json"
    previas = json.loads(bitacora.read_text(encoding="utf-8")) if bitacora.is_file() else []
    entrada = _sellar({
        "n": len(previas) + 1, "fecha": hoy.isoformat(), "por": por,
        "plugin": inst["plugin"], "version_familia": inst["version"],
        "terminos": {"version": t["version"], "archivo": t["archivo"], "sha256": t["sha256"]},
        "registro_sha256": reg.get("sha256") if reg else None,
        "comprobante": {"md": md.name, "md_sha256": h_md, "pdf": pdf.name, "pdf_sha256": h_pdf},
        "anterior": previas[-1]["sha256"] if previas else None,
    })
    bitacora.write_text(json.dumps(previas + [entrada], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def rel(p: Path) -> str:
        try:
            return p.resolve().relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            return str(p)

    cfg["terms_accepted"] = {
        "version": t["version"], "date": hoy.isoformat(), "by": por,
        "family_version": inst["version"], "plugin": inst["plugin"],
        "terms_file": t["archivo"], "terms_sha256": t["sha256"],
        "register_sha256": reg.get("sha256") if reg else None,
        "receipt_md": rel(md), "receipt_md_sha256": h_md,
        "receipt_pdf": rel(pdf), "receipt_pdf_sha256": h_pdf,
        "legal_notice": f"{url}#v{inst['version']}",
    }
    if config.is_file():
        config.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"aceptado": True, "version_familia": inst["version"], "terminos": t["version"],
            "terminos_sha256": t["sha256"], "comprobante_md": rel(md), "comprobante_pdf": rel(pdf),
            "huellas": {md.name: h_md, pdf.name: h_pdf}, "nota_legal": f"{url}#v{inst['version']}",
            "registrado_en_config": config.is_file()}


def bitacora_intacta(carpeta: Path) -> list[str]:
    f = carpeta / "aceptaciones.json"
    if not f.is_file():
        return []
    problemas, anterior = [], None
    for e in json.loads(f.read_text(encoding="utf-8")):
        if _sellar(e)["sha256"] != e.get("sha256"):
            problemas.append(f"la aceptación {e.get('n')} fue modificada después de registrada")
        if e.get("anterior") != anterior:
            problemas.append(f"la aceptación {e.get('n')} no sigue a la anterior: falta o sobra una")
        anterior = e.get("sha256")
    return problemas


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    import os
    import shutil
    import tempfile
    fallos = 0

    def ok(nombre, obtenido, esperado):
        nonlocal fallos
        bien = obtenido == esperado
        fallos += not bien
        print(f"  {'OK ' if bien else 'MAL'}  {nombre}" + ("" if bien else f": {obtenido!r} ≠ {esperado!r}"))

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        raiz = tmp / "plugin"
        (raiz / ".claude-plugin").mkdir(parents=True)
        (raiz / ".claude-plugin" / "plugin.json").write_text('{"name": "criterio-x", "version": "9.1.0"}')
        (raiz / "TERMS.es.md").write_text("# Términos\n\nVersión 2.0 · 2026-10-15\n\n## En corto\n\n"
                                         "Esto produce borradores.\n\n## 1. Otro\n\nTexto.\n", encoding="utf-8")
        (raiz / "REGISTRO.json").write_text('{"versiones": [{"version": "9.1.0", "sha256": "abc"}]}')
        sesion = tmp / "sesion"
        (sesion / ".criterio" / "portafolio").mkdir(parents=True)
        cfg = sesion / ".criterio" / "portafolio" / "config.json"
        cfg.write_text('{"report": {"language": "es"}, "terms_accepted": {"version": "1.0", "date": "2026-09-01"}}')
        cwd = os.getcwd()
        os.chdir(sesion)
        try:
            t = terminos("es", raiz)
            ok("versión de los términos", (t["version"], t["fecha"]), ("2.0", "2026-10-15"))
            ok("el texto corto sale de su sección", t["en_corto"], "Esto produce borradores.")
            ok("una aceptación vieja no está vigente", estado(cfg, raiz)["vigente"], False)
            r = aceptar(cfg, "Ana Pérez", hoy=dt.date(2026, 10, 15), raiz=raiz)
            ok("aceptar deja md y pdf", (Path(r["comprobante_md"]).is_file(), Path(r["comprobante_pdf"]).is_file()), (True, True))
            ok("el pdf es un pdf", Path(r["comprobante_pdf"]).read_bytes()[:8], b"%PDF-1.4")
            ok("con la aceptación, vigente", estado(cfg, raiz)["vigente"], True)
            md = Path(r["comprobante_md"]).read_text(encoding="utf-8")
            ok("el comprobante lleva la huella de los términos", t["sha256"] in md, True)
            ok("y el registro de la versión", "abc" in md, True)
            Path(r["comprobante_md"]).write_text(md + " ", encoding="utf-8")
            ok("un comprobante tocado deja de valer", estado(cfg, raiz)["vigente"], False)
            (raiz / ".claude-plugin" / "plugin.json").write_text('{"name": "criterio-x", "version": "9.2.0"}')
            r2 = aceptar(cfg, "Ana Pérez", hoy=dt.date(2026, 10, 15), raiz=raiz)
            ok("una versión nueva pide otra aceptación, y la deja aparte", r2["comprobante_md"] != r["comprobante_md"], True)
            ok("el comprobante anterior se conserva", Path(r["comprobante_pdf"]).is_file(), True)
            ok("la bitácora queda encadenada", bitacora_intacta(carpeta_terminos(cfg)), [])
            b = carpeta_terminos(cfg) / "aceptaciones.json"
            datos = json.loads(b.read_text(encoding="utf-8"))
            datos[0]["por"] = "Otra Persona"
            b.write_text(json.dumps(datos), encoding="utf-8")
            ok("una aceptación alterada se nota", len(bitacora_intacta(carpeta_terminos(cfg))) > 0, True)
            (raiz / "TERMS.es.md").write_text((raiz / "TERMS.es.md").read_text(encoding="utf-8") + "x", encoding="utf-8")
            ok("términos cambiados sin aceptar: no vigente", estado(cfg, raiz)["vigente"], False)
        finally:
            os.chdir(cwd)
            shutil.rmtree(tmp, ignore_errors=True)
    print("\nselftest: " + ("sin errores" if not fallos else f"{fallos} errores"))
    return 1 if fallos else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Criterio — los términos y su aceptación.")
    ap.add_argument("accion", nargs="?", choices=["estado", "aceptar"])
    ap.add_argument("--config", type=Path)
    ap.add_argument("--por", default=None)
    ap.add_argument("--idioma", default=None)
    ap.add_argument("--fecha", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.accion or not a.config:
        ap.error("estado | aceptar, con --config")
    if a.accion == "estado":
        r = estado(a.config)
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 0 if r["vigente"] else 3
    hoy = dt.date.fromisoformat(a.fecha) if a.fecha else None
    print(json.dumps(aceptar(a.config, a.por, a.idioma, hoy), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
