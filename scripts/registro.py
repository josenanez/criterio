#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El registro de versiones de Criterio: qué cambió, qué términos rigen, qué versión tiene cada familia, y su huella.

    python3 scripts/registro.py historia                  arma las entradas de las versiones ya publicadas, desde git
    python3 scripts/registro.py liberar 1.0.0 --familia pmo=1.0.0 [--familia cso=0.1.0] --destacado "…" [--etiquetar]
    python3 scripts/registro.py liberar 1.0.1 --todas      todas las familias liberadas suben una corrección (un cambio común, como los términos)
    python3 scripts/registro.py verificar                 puerta

**Una versión por familia (decisión 0017).** Cada familia —PMO, CFO, CLO, EA y Rostrum— lleva su
propio número en sus plugins, y sube solo cuando ella cambia. El número del marketplace es el del
catálogo: sube con cada entrada del registro. Cada entrada nueva anota la versión de cada familia
(`familias`), la de cada plugin (`versiones`) y cuáles se liberaron en ella (`liberadas`); las
entradas anteriores a la decisión tienen una sola versión para todo, y así se leen.

**Diez versiones por entero y una etiqueta de calidad (decisión 0020).** Cada número entero tiene
diez versiones, de x.0 a x.9, y después de la x.9 viene la x+1.0; las correcciones, el tercer
número, no cuentan. La 0.10, la 0.11 y la 0.12 son las únicas excepciones: quien está ahí sube a la
1.0.0. `liberar` falla con una versión que no siga la regla, y anota en la entrada la calidad de cada
familia que libera —laboratorio o estable—, que calcula `scripts/calidad.py` desde la evidencia.

**El lanzamiento abre la 1.0 (decisión 0021).** Una familia se publica —en el marketplace y en el
portal— desde su primera liberación, y se lanza la semana que dice su `familia.json` en
`lanzamiento`, el único dato que se escribe a mano. Una familia lanzada sube a la 1.0.0 en su
primera versión estable, venga de la 0.y que venga: `liberar` falla si no lo hace. Una corrección
—el tercer número— sí puede salir antes.

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


def en_construccion() -> dict[str, str]:
    """Los plugins de las familias que todavía no se han liberado, con la versión que su hoja de ruta
    les planea: la primera que no dice «liberada». Una familia en construcción no está en el
    marketplace, y entra al registro con su primera liberación (`--familia sigla=versión`)."""
    reg = leer()
    ultima = reg["versiones"][-1] if reg["versiones"] else {}
    if "familias" not in ultima:
        return {}
    out = {}
    for sigla, pls in familias().items():
        if sigla in ultima["familias"]:
            continue
        hoja = RAIZ / "families" / f"criterio-{sigla}" / "hoja-de-ruta.json"
        h = json.loads(hoja.read_text(encoding="utf-8")) if hoja.is_file() else {"incrementos": []}
        v = next((i["version"] for i in h["incrementos"] if i["estado"] != "liberada" and i["version"]), None)
        out.update({pl: v for pl in pls})
    return out


def lanzamiento(sigla: str) -> str | None:
    """La semana en que se lanza la familia, de su familia.json (decisión 0021), o None si todavía no
    se lanza. Es el único dato de la familia que se escribe a mano: lo decide quien la lanza."""
    f = RAIZ / "families" / f"criterio-{sigla}" / "familia.json"
    return json.loads(f.read_text(encoding="utf-8")).get("lanzamiento") if f.is_file() else None


def lanzada(sigla: str, hoy: str | None = None) -> bool:
    l = lanzamiento(sigla)
    return bool(l) and l <= (hoy or dt.date.today().isoformat())


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


def sigue(previa: str | None, nueva: str, abre: bool = False) -> str | None:
    """Por qué `nueva` no puede seguir a `previa`, o None si puede (decisión 0020): una corrección
    sube el tercer número; una versión sube el segundo hasta el 9; después del 9 —o de la 0.10, la
    0.11 y la 0.12, las excepciones—, la siguiente es el entero que sigue con .0.0. Con `abre`
    —una familia lanzada en su primera versión estable (decisión 0021)—, de cualquier 0.y se sube a
    la 1.0.0."""
    n = clave(nueva)
    if len(n) != 3:
        return f"{nueva} no tiene la forma x.y.z"
    if previa is None:
        return None if n[0] == 0 and n[1] <= 9 and n[2] == 0 else f"una familia nueva empieza en una 0.y.0 con y hasta 9, no en {nueva}"
    p = clave(previa)
    if abre and p[0] == 0 and n == (1, 0, 0):
        return None
    if n[:2] == p[:2] and n[2] > p[2]:
        return None
    if p[1] < 9 and n == (p[0], p[1] + 1, 0):
        return None
    if p[1] >= 9 and n == (p[0] + 1, 0, 0):
        return None
    siguiente = f"{p[0] + 1}.0.0" if p[1] >= 9 else f"{p[0]}.{p[1] + 1}.0"
    return f"después de la {previa} viene la {siguiente} o una corrección {p[0]}.{p[1]}.{p[2] + 1}; {nueva} no sigue la regla de diez versiones por entero"


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
    # La calidad de cada familia que se libera, desde su evidencia (decisión 0020): no se escribe a mano.
    sys.path.insert(0, str(RAIZ / "scripts"))
    import calidad as Q
    calidades = {s: Q.calidad(s) for s in sorted(por_familia) if s != "rostrum"}
    for sigla, fv in por_familia.items():
        if sigla not in fam:
            print(f"no hay una familia «{sigla}»: las familias son {', '.join(fam)}")
            return 1
        anterior = version_de_familia(previa, sigla) if previa and ("familias" not in previa or sigla in previa["familias"]) else None
        if previa and anterior and clave(fv) <= clave(anterior):
            print(f"{sigla} está en {anterior}: {fv} no la sube")
            return 1
        # Una familia lanzada y estable que todavía está en una 0.y abre su 1.0 (decisión 0021).
        abre = (sigla != "rostrum" and lanzada(sigla) and anterior is not None and clave(anterior)[0] == 0
                and calidades[sigla]["etiqueta"] == "estable")
        correccion = anterior is not None and clave(fv)[:2] == clave(anterior)[:2]
        if abre and fv != "1.0.0" and not correccion:
            print(f"{sigla} está lanzada y es estable: su versión siguiente es la 1.0.0, no la {fv}; "
                  f"una corrección {'.'.join(map(str, clave(anterior)[:2]))}.z sí puede salir (decisión 0021)")
            return 1
        motivo = sigue(anterior, fv, abre)
        if motivo:
            print(f"{sigla}: {motivo}")
            return 1
    if previa and clave(v) <= clave(previa["version"]):
        print(f"el catálogo está en {previa['version']}: {v} no lo sube")
        return 1
    motivo = sigue(previa["version"] if previa else None, v)
    if motivo:
        print(f"el catálogo: {motivo}")
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
    # Una familia en construcción que no se libera en esta entrada sigue fuera del registro.
    actuales = {s: por_familia.get(s, version_de_familia(previa, s) if previa else v) for s in fam
                if s in por_familia or not previa or "familias" not in previa or s in previa["familias"]}
    versiones = {pl: actuales[s] for s, pls in fam.items() if s in actuales for pl in pls}
    e = sellar({"version": v, "fecha": dt.date.today().isoformat(), "commit": None, "base": base,
                "etiqueta": f"v{v}", "familias": actuales, "liberadas": sorted(por_familia), "versiones": versiones,
                "calidad": calidades,
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
        # Desde la 0.12.1, la última antes de la decisión 0020, cada entrada sigue la regla de diez
        # versiones por entero: el catálogo y cada familia que se libera.
        vs = reg["versiones"]
        for prev, e in zip(vs, vs[1:]):
            if clave(prev["version"]) < (0, 12, 1):
                continue
            m = sigue(prev["version"], e["version"])
            if m:
                problemas.append(f"la entrada {e['version']}: el catálogo: {m}")
            for s in e.get("liberadas") or []:
                ant = (prev.get("familias") or {}).get(s)
                abre = (e.get("calidad") or {}).get(s, {}).get("etiqueta") == "estable" and lanzada(s, e["fecha"])
                m = sigue(ant, e["familias"][s], abre)
                if m:
                    problemas.append(f"la entrada {e['version']}: {s}: {m}")
        # Cada plugin, en la versión de su familia según la última entrada; el de una familia en
        # construcción, en la que le planea su hoja de ruta, y fuera del marketplace.
        construccion = en_construccion()
        listados = {p["name"] for p in json.loads(MARKET.read_text(encoding="utf-8")).get("plugins", [])}
        for f in sorted((RAIZ / "plugins").glob("*/.claude-plugin/plugin.json")):
            pl = f.parent.parent.name
            pv = json.loads(f.read_text(encoding="utf-8")).get("version")
            if pl in construccion:
                if pv != construccion[pl]:
                    problemas.append(f"{pl} está en {pv} y su familia, en construcción, planea la {construccion[pl]} en su hoja de ruta")
                if pl in listados:
                    problemas.append(f"{pl} es de una familia en construcción y está en el marketplace: se publica con su primera liberación")
                continue
            if pv != version_de_plugin(ultima, pl):
                problemas.append(f"{pl} está en {pv} y la última entrada lo registra en {version_de_plugin(ultima, pl)}")
        # Solo se lanza lo que está publicado: una familia con `lanzamiento` tiene su entrada.
        for s in familias():
            l = lanzamiento(s)
            if l is None:
                continue
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(l)):
                problemas.append(f"{s}: «lanzamiento» va como una fecha AAAA-MM-DD, no «{l}»")
            elif "familias" in ultima and s not in ultima["familias"]:
                problemas.append(f"{s} tiene lanzamiento ({l}) y no tiene ninguna versión liberada: se lanza lo que está publicado")
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
        movidos = sorted(p for p in ahora if ahora.get(p) != ultima["plugins"].get(p) and p not in construccion)
        if construccion:
            avisos.append(f"en construcción, fuera del marketplace: {', '.join(sorted(construccion))}")
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
    ap.add_argument("--todas", action="store_true",
                    help="cada familia liberada sube una corrección de su versión: un cambio común, como los términos")
    ap.add_argument("--etiquetar", action="store_true",
                    help="hace el commit de la versión y crea su etiqueta sobre él")
    a = ap.parse_args()
    if a.accion == "historia":
        return historia()
    if a.accion == "verificar":
        return verificar()
    if not a.version or not re.fullmatch(r"\d+\.\d+\.\d+", a.version):
        ap.error("liberar necesita la versión del catálogo, como 1.0.0")
    por_familia = {}
    if a.todas:
        # Un cambio común sube una corrección en cada familia liberada; una en construcción sigue fuera.
        ultima = (leer()["versiones"] or [{}])[-1]
        for s in familias():
            if "familias" in ultima and s not in ultima["familias"]:
                continue
            x, y, z = clave(version_de_familia(ultima, s))
            por_familia[s] = f"{x}.{y}.{z + 1}"
    for x in a.familia:
        if not re.fullmatch(r"[a-z]+=\d+\.\d+\.\d+", x):
            ap.error(f"--familia va como sigla=versión, por ejemplo cfo=1.0.0: «{x}»")
        s, fv = x.split("=")
        por_familia[s] = fv
    return liberar(a.version, por_familia, a.destacado, a.etiquetar)


if __name__ == "__main__":
    sys.exit(main())
