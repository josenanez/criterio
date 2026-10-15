#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El registro de versiones de la familia de agentes: qué cambió, qué términos la rigen, y su huella.

    python3 scripts/registro.py historia                  arma las entradas de las versiones ya publicadas, desde git
    python3 scripts/registro.py liberar 0.3.8 --destacado "…" [--destacado "…"]
    python3 scripts/registro.py verificar                 puerta

**Como una patente.** Cada versión deja una entrada que no se borra ni se reescribe: la
fecha, el commit, los cambios, los términos que la rigen con su huella SHA-256, y la
huella de lo que hace cada agente (sus comandos, sus skills y sus scripts). Cada entrada
lleva la huella de la anterior, así que una entrada alterada o quitada rompe la cadena y
la puerta falla. Las aceptaciones de cada persona citan la entrada de su versión.

La fuente es `registro/versiones.json`; cada plugin lleva una copia idéntica
(`REGISTRO.json`), que escribe `scripts/sincronizar.py`, para que el agente instalado sepa
qué versión acepta quien lo usa sin depender del repositorio. El portal publica el
registro en la nota legal de la familia.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "registro" / "versiones.json"
MARKET = RAIZ / ".claude-plugin" / "marketplace.json"
FAMILIA = ("criterio-portfolio", "criterio-project", "criterio-product")
ACEPTACION_ANTES = "versión de los términos, fecha y nombre en la configuración; sin huella ni comprobante"
ACEPTACION_AHORA = ("una aceptación por versión, con comprobante en Markdown y PDF, huella SHA-256 "
                    "de los términos y del comprobante, y bitácora encadenada")


def git(*a: str) -> str:
    return subprocess.run(["git", "-C", str(RAIZ), *a], capture_output=True, text=True, check=True).stdout


def canon(d: dict) -> bytes:
    return json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sellar(e: dict) -> dict:
    e = {k: v for k, v in e.items() if k != "sha256"}
    e["sha256"] = hashlib.sha256(canon(e)).hexdigest()
    return e


def leer() -> dict:
    if FUENTE.is_file():
        return json.loads(FUENTE.read_text(encoding="utf-8"))
    return {"descripcion": ("Registro de versiones de la familia de agentes Criterio. Cada entrada lleva la "
                            "huella SHA-256 de la anterior: no se borra ni se reescribe."),
            "versiones": []}


def escribir(reg: dict) -> None:
    FUENTE.parent.mkdir(parents=True, exist_ok=True)
    FUENTE.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _huella(archivos: list[tuple[str, bytes]]) -> str:
    """El mismo cálculo que `huella_plugin` en portafolio.py, con la huella entera."""
    h = hashlib.sha256()
    for rel, datos in archivos:
        h.update(rel.encode())
        h.update(datos)
    return h.hexdigest()


def _orden(rels: list[str]) -> list[str]:
    cmd = sorted(r for r in rels if re.fullmatch(r"commands/[^/]+\.md", r))
    sk = sorted(r for r in rels if re.fullmatch(r"skills/[^/]+/SKILL\.md", r))
    py = sorted(r for r in rels if re.fullmatch(r"scripts/[^/]+\.py", r))
    return cmd + sk + py


def huellas_en(commit: str | None) -> dict:
    """La huella de cada agente con comandos, en un commit o en el árbol de trabajo."""
    out = {}
    if commit is None:
        for d in sorted((RAIZ / "plugins").iterdir()):
            rels = [p.relative_to(d).as_posix() for p in d.rglob("*") if p.is_file()]
            orden = _orden(rels)
            if orden:
                out[d.name] = _huella([(r, (d / r).read_bytes()) for r in orden])
        return out
    todos = git("ls-tree", "-r", "--name-only", commit, "plugins/").split()
    plugins = sorted({p.split("/")[1] for p in todos})
    for pl in plugins:
        rels = [p[len(f"plugins/{pl}/"):] for p in todos if p.startswith(f"plugins/{pl}/")]
        orden = _orden(rels)
        if orden:
            datos = []
            for r in orden:
                b = subprocess.run(["git", "-C", str(RAIZ), "show", f"{commit}:plugins/{pl}/{r}"],
                                   capture_output=True, check=True).stdout
                datos.append((r, b))
            out[pl] = _huella(datos)
    return out


def terminos_en(commit: str | None) -> dict:
    out = {"version": None, "fecha": None, "sha256": {}}
    for idioma, f in (("es", "TERMS.es.md"), ("en", "TERMS.md")):
        if commit is None:
            p = RAIZ / f
            datos = p.read_bytes() if p.is_file() else None
        else:
            r = subprocess.run(["git", "-C", str(RAIZ), "show", f"{commit}:{f}"], capture_output=True)
            datos = r.stdout if r.returncode == 0 else None
        if datos is None:
            continue
        out["sha256"][idioma] = hashlib.sha256(datos).hexdigest()
        m = re.search(r"(?:Versión|Version) (\d+(?:\.\d+)*) · (\d{4}-\d{2}-\d{2})", datos.decode("utf-8"))
        if m:
            out["version"], out["fecha"] = m.group(1), m.group(2)
    return out


def version_en(commit: str) -> str | None:
    try:
        return json.loads(git("show", f"{commit}:.claude-plugin/marketplace.json")).get("version")
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def historia() -> int:
    """Las versiones publicadas antes del registro, reconstruidas de git y no de memoria."""
    reg = leer()
    if reg["versiones"]:
        print("el registro ya tiene entradas: la historia se arma una sola vez")
        return 1
    commits = git("log", "--reverse", "--format=%h %ad", "--date=short", "-G", r'"version": "', "--",
                  ".claude-plugin/marketplace.json").splitlines()
    anterior_commit, anterior = None, None
    vistas = set()
    for linea in commits:
        c, fecha = linea.split()
        v = version_en(c)
        if not v or v in vistas:
            continue
        vistas.add(v)
        rango = f"{anterior_commit}..{c}" if anterior_commit else c
        cambios = git("log", "--reverse", "--format=%s", rango).splitlines()
        e = sellar({"version": v, "fecha": fecha, "commit": c, "terminos": terminos_en(c),
                    "plugins": huellas_en(c), "destacados": [], "cambios": cambios,
                    "aceptacion": ACEPTACION_ANTES, "anterior": anterior})
        reg["versiones"].append(e)
        anterior, anterior_commit = e["sha256"], c
        print(f"  {v}  {fecha}  {c}  · {len(cambios)} cambios")
    escribir(reg)
    return 0


def poner_version(v: str) -> list[str]:
    tocados = []
    for f in [MARKET, *sorted((RAIZ / "plugins").glob("*/.claude-plugin/plugin.json"))]:
        t = f.read_text(encoding="utf-8")
        n = re.sub(r'("version":\s*")[^"]+(")', rf"\g<1>{v}\g<2>", t, count=1)
        if n != t:
            f.write_text(n, encoding="utf-8")
            tocados.append(f.relative_to(RAIZ).as_posix())
    return tocados


def liberar(v: str, destacados: list[str]) -> int:
    reg = leer()
    if any(e["version"] == v for e in reg["versiones"]):
        print(f"la versión {v} ya está registrada: una versión no se registra dos veces")
        return 1
    previa = reg["versiones"][-1] if reg["versiones"] else None
    poner_version(v)
    subprocess.run([sys.executable, str(RAIZ / "scripts" / "sincronizar.py")], check=True,
                   capture_output=True)
    base = git("rev-parse", "--short", "HEAD").strip()
    rango = f"{previa['commit']}..HEAD" if previa and previa.get("commit") else "HEAD"
    cambios = git("log", "--reverse", "--format=%s", rango).splitlines()
    e = sellar({"version": v, "fecha": dt.date.today().isoformat(), "commit": None, "base": base,
                "terminos": terminos_en(None), "plugins": huellas_en(None),
                "destacados": destacados, "cambios": cambios, "aceptacion": ACEPTACION_AHORA,
                "anterior": previa["sha256"] if previa else None})
    reg["versiones"].append(e)
    escribir(reg)
    subprocess.run([sys.executable, str(RAIZ / "scripts" / "sincronizar.py")], check=True,
                   capture_output=True)
    print(f"  {v} registrada · base {base} · {len(cambios)} cambios desde la anterior · sha256 {e['sha256'][:16]}…")
    print("  Haz el commit de la versión y la etiqueta: git tag v" + v)
    return 0


def verificar() -> int:
    reg = leer()
    problemas, avisos = [], []
    anterior = None
    for e in reg["versiones"]:
        if sellar(e)["sha256"] != e.get("sha256"):
            problemas.append(f"la entrada {e.get('version')} fue modificada después de registrada")
        if e.get("anterior") != anterior:
            problemas.append(f"la entrada {e.get('version')} no sigue a la anterior: la cadena se rompió")
        anterior = e.get("sha256")
    if not reg["versiones"]:
        problemas.append("el registro está vacío")
    else:
        ultima = reg["versiones"][-1]
        actual = json.loads(MARKET.read_text(encoding="utf-8")).get("version")
        if actual != ultima["version"]:
            problemas.append(f"la versión publicada es {actual} y la última registrada es {ultima['version']}: "
                             f"una versión sin registro no se libera")
        for f in sorted((RAIZ / "plugins").glob("*/.claude-plugin/plugin.json")):
            pv = json.loads(f.read_text(encoding="utf-8")).get("version")
            if pv != actual:
                problemas.append(f"{f.parent.parent.name} está en {pv} y el market en {actual}")
        t = terminos_en(None)
        if t["sha256"] != ultima["terminos"]["sha256"]:
            problemas.append("los términos cambiaron después de la última versión registrada: "
                             "un cambio a los términos sale con una versión nueva")
        ahora = huellas_en(None)
        movidos = [p for p in FAMILIA if ahora.get(p) != ultima["plugins"].get(p)]
        if movidos:
            avisos.append(f"cambios sin liberar desde la {ultima['version']}: {', '.join(movidos)}")
    for a in avisos:
        print(f"  aviso  {a}")
    if problemas:
        for p in problemas:
            print(f"  FALLA  {p}")
        return 1
    print(f"  OK    {len(reg['versiones'])} versiones registradas, cadena íntegra · "
          f"última {reg['versiones'][-1]['version']}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="El registro de versiones de Criterio.")
    ap.add_argument("accion", choices=["historia", "liberar", "verificar"])
    ap.add_argument("version", nargs="?")
    ap.add_argument("--destacado", action="append", default=[])
    a = ap.parse_args()
    if a.accion == "historia":
        return historia()
    if a.accion == "verificar":
        return verificar()
    if not a.version or not re.fullmatch(r"\d+\.\d+\.\d+", a.version):
        ap.error("liberar necesita la versión, como 0.3.8")
    return liberar(a.version, a.destacado)


if __name__ == "__main__":
    sys.exit(main())
