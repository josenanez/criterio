#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El registro de versiones de Criterio: qué cambió, qué términos rigen, qué versión tiene cada familia, y su huella.

    python3 scripts/registro.py historia                  arma las entradas de las versiones ya publicadas, desde git
    python3 scripts/registro.py liberar 0.13.0 --familia pmo=0.13.0 [--familia cfo=0.12.2] --destacado "…" [--etiquetar]
    python3 scripts/registro.py liberar 0.12.1 --todas     todas las familias a la misma versión (un cambio común, como los términos)
    python3 scripts/registro.py verificar                 puerta

**Una versión por familia (decisión 0017).** Cada familia —PMO, CFO, CLO, EA y Rostrum— lleva su
propio número en sus plugins, y sube solo cuando ella cambia. El número del marketplace es el del
catálogo: sube con cada entrada del registro. Cada entrada nueva anota la versión de cada familia
(`familias`), la de cada plugin (`versiones`) y cuáles se liberaron en ella (`liberadas`); las
entradas anteriores a la decisión tienen una sola versión para todo, y así se leen.

**La entrada y la etiqueta apuntan al mismo punto.** Desde la 0.3.9 cada entrada guarda su
etiqueta (`v0.3.9`), y `liberar --etiquetar` hace el commit de la versión y crea la etiqueta
sobre ese commit, que es el que contiene la entrada. Las entradas anteriores anotan el commit
donde nació cada versión; la etiqueta `v0.3.6`, creada a mano, marca un commit posterior de la
misma versión, y la `v0.3.8` el commit que la registró. Eso no se corrige reescribiendo el
registro: una entrada pasada no se toca.

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
ACEPTACION_ANTES = "versión de los términos, fecha y nombre en la configuración; sin huella ni comprobante"
ACEPTACION_AHORA = ("una aceptación por versión, con comprobante en Markdown y PDF, huella SHA-256 "
                    "de los términos y del comprobante, y bitácora encadenada")


def familias() -> dict[str, list[str]]:
    """Qué plugins forman cada familia, de su familia.json. Rostrum, que sirve a todas, es la suya."""
    out = {}
    for f in sorted((RAIZ / "families").glob("criterio-*/familia.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        out[d["sigla"]] = sorted({a["plugin"] for a in d["agentes"]})
    out["rostrum"] = ["criterio-server"]
    return out


def version_de_familia(e: dict, sigla: str) -> str:
    """La versión de una familia en una entrada; antes de la decisión 0017, la única de la entrada."""
    return e.get("familias", {}).get(sigla, e["version"])


def version_de_plugin(e: dict, plugin: str) -> str:
    return e.get("versiones", {}).get(plugin, e["version"])


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


def _poner(f: Path, v: str) -> None:
    t = f.read_text(encoding="utf-8")
    n = re.sub(r'("version":\s*")[^"]+(")', rf"\g<1>{v}\g<2>", t, count=1)
    if n != t:
        f.write_text(n, encoding="utf-8")


def poner_versiones(catalogo: str, por_familia: dict[str, str]) -> None:
    """El catálogo en el marketplace y, en cada familia que se libera, su versión en sus plugins."""
    _poner(MARKET, catalogo)
    fam = familias()
    for sigla, v in por_familia.items():
        for pl in fam[sigla]:
            _poner(RAIZ / "plugins" / pl / ".claude-plugin" / "plugin.json", v)


def clave(v: str) -> tuple:
    return tuple(int(x) for x in v.split("."))


def liberar(v: str, por_familia: dict[str, str], destacados: list[str], etiquetar: bool = False) -> int:
    reg = leer()
    if any(e["version"] == v for e in reg["versiones"]):
        print(f"la versión {v} ya está registrada: una versión no se registra dos veces")
        return 1
    previa = reg["versiones"][-1] if reg["versiones"] else None
    fam = familias()
    if not por_familia:
        print("una versión libera al menos una familia: --familia sigla=versión o --todas")
        return 1
    for sigla, fv in por_familia.items():
        if sigla not in fam:
            print(f"no hay una familia «{sigla}»: las familias son {', '.join(fam)}")
            return 1
        if previa and clave(fv) <= clave(version_de_familia(previa, sigla)):
            print(f"{sigla} está en {version_de_familia(previa, sigla)}: {fv} no la sube")
            return 1
    if previa and clave(v) <= clave(previa["version"]):
        print(f"el catálogo está en {previa['version']}: {v} no lo sube")
        return 1
    poner_versiones(v, por_familia)
    subprocess.run([sys.executable, str(RAIZ / "scripts" / "sincronizar.py")], check=True,
                   capture_output=True)
    base = git("rev-parse", "--short", "HEAD").strip()
    # Desde dónde contar los cambios: la etiqueta de la anterior si existe (es el commit que la
    # registró), si no el commit donde nació, si no el commit sobre el que se liberó.
    desde = None
    for ref in ([previa.get("etiqueta"), f"v{previa['version']}", previa.get("commit"), previa.get("base")]
                if previa else []):
        if ref and subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "-q", "--verify", f"{ref}^{{commit}}"],
                                  capture_output=True).returncode == 0:
            desde = ref
            break
    rango = f"{desde}..HEAD" if desde else "HEAD"
    cambios = git("log", "--reverse", "--format=%s", rango).splitlines()
    # La versión de cada familia y de cada plugin después de esta entrada.
    actuales = {s: por_familia.get(s, version_de_familia(previa, s) if previa else v) for s in fam}
    versiones = {pl: actuales[s] for s, pls in fam.items() for pl in pls}
    e = sellar({"version": v, "fecha": dt.date.today().isoformat(), "commit": None, "base": base,
                "etiqueta": f"v{v}", "familias": actuales, "liberadas": sorted(por_familia), "versiones": versiones,
                "terminos": terminos_en(None), "plugins": huellas_en(None),
                "destacados": destacados, "cambios": cambios, "aceptacion": ACEPTACION_AHORA,
                "anterior": previa["sha256"] if previa else None})
    reg["versiones"].append(e)
    escribir(reg)
    # La hoja de ruta de cada familia liberada dice «liberada» de su versión, y su sección del
    # README se regenera: las dos cosas pasan en el mismo commit.
    for sigla, fv in por_familia.items():
        hoja = RAIZ / "families" / f"criterio-{sigla}" / "hoja-de-ruta.json"
        if not hoja.is_file():
            continue
        h = json.loads(hoja.read_text(encoding="utf-8"))
        for i in h["incrementos"]:
            if i["version"] == fv:
                i["estado"] = "liberada"
        hoja.write_text(json.dumps(h, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(RAIZ / "scripts" / "hoja.py")], check=True, capture_output=True)
    subprocess.run([sys.executable, str(RAIZ / "scripts" / "sincronizar.py")], check=True,
                   capture_output=True)
    print(f"  {v} registrada · {', '.join(f'{s} {fv}' for s, fv in sorted(por_familia.items()))} · base {base} · "
          f"{len(cambios)} cambios desde la anterior · sha256 {e['sha256'][:16]}…")
    if not etiquetar:
        print(f"  Haz el commit de la versión y crea la etiqueta sobre él: git tag v{v}")
        return 0
    # El commit de la versión lleva el registro, los números de versión y las copias; la
    # etiqueta va sobre ese commit, el que contiene la entrada.
    git("add", "registro", ".claude-plugin", "plugins", "families")
    git("commit", "-q", "-m", f"Release {v}, entered in the version register")
    git("tag", "-a", f"v{v}", "-m", f"Criterio {v} · entrada SHA-256 {e['sha256']}")
    print(f"  commit {git('rev-parse', '--short', 'HEAD').strip()} y etiqueta v{v}. "
          f"Súbelos: git push origin main && git push origin v{v}")
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
        # Cada plugin, en la versión de su familia según la última entrada.
        for f in sorted((RAIZ / "plugins").glob("*/.claude-plugin/plugin.json")):
            pl = f.parent.parent.name
            pv = json.loads(f.read_text(encoding="utf-8")).get("version")
            if pv != version_de_plugin(ultima, pl):
                problemas.append(f"{pl} está en {pv} y la última entrada lo registra en {version_de_plugin(ultima, pl)}")
        registrados = {pl for pls in familias().values() for pl in pls}
        for f in sorted((RAIZ / "plugins").glob("*/.claude-plugin/plugin.json")):
            if f.parent.parent.name not in registrados:
                problemas.append(f"{f.parent.parent.name} no pertenece a ninguna familia: falta en su familia.json")
        t = terminos_en(None)
        if t["sha256"] != ultima["terminos"]["sha256"]:
            problemas.append("los términos cambiaron después de la última versión registrada: "
                             "un cambio a los términos sale con una versión nueva")
        # La etiqueta de una entrada apunta a un commit que contiene esa entrada.
        for e in reg["versiones"]:
            etq = e.get("etiqueta")
            if not etq:
                continue
            r = subprocess.run(["git", "-C", str(RAIZ), "show", f"{etq}:registro/versiones.json"],
                               capture_output=True, text=True)
            if r.returncode:
                avisos.append(f"la etiqueta {etq} todavía no existe en este repositorio")
            elif e["sha256"] not in r.stdout:
                problemas.append(f"la etiqueta {etq} apunta a un commit que no contiene la entrada {e['version']}")
        ahora = huellas_en(None)
        movidos = sorted(p for p in ahora if ahora.get(p) != ultima["plugins"].get(p))
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
    ap.add_argument("--familia", action="append", default=[], metavar="SIGLA=VERSION",
                    help="una familia que se libera y su versión nueva; se repite por familia")
    ap.add_argument("--todas", action="store_true", help="todas las familias a la versión del catálogo")
    ap.add_argument("--etiquetar", action="store_true",
                    help="hace el commit de la versión y crea su etiqueta sobre él")
    a = ap.parse_args()
    if a.accion == "historia":
        return historia()
    if a.accion == "verificar":
        return verificar()
    if not a.version or not re.fullmatch(r"\d+\.\d+\.\d+", a.version):
        ap.error("liberar necesita la versión del catálogo, como 0.13.0")
    por_familia = {s: a.version for s in familias()} if a.todas else {}
    for x in a.familia:
        if not re.fullmatch(r"[a-z]+=\d+\.\d+\.\d+", x):
            ap.error(f"--familia va como sigla=versión, por ejemplo cfo=0.13.0: «{x}»")
        s, fv = x.split("=")
        por_familia[s] = fv
    return liberar(a.version, por_familia, a.destacado, a.etiquetar)


if __name__ == "__main__":
    sys.exit(main())
