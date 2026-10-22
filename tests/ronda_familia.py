#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La ronda con el agente de las familias CFO y CLO: los dos agentes de la familia corren sus
comandos sobre el material de una entidad, y lo que escribieron se califica contra la clave que
no vieron.

    python3 tests/ronda_familia.py armar <carpeta> --familia cfo --entidad banca
    python3 tests/ronda_familia.py correr <carpeta> --tope 5000000 [--solo 1 2]
    python3 tests/ronda_familia.py calificar <carpeta>
    python3 tests/ronda_familia.py publicar <carpeta> --ronda 1 --nombre banca
    python3 tests/ronda_familia.py resumen

La familia queda escrita en `<carpeta>/familia.txt` al armar, y las otras dos acciones la toman
de ahí. Las rondas de la PMO tienen su propio arnés, `tests/ronda.py`.

**El tope es obligatorio.** Antes de cada comando se suma lo que gastaron los anteriores; si
llegó al tope, la ronda para ahí y lo dice. Un comando ya empezado no se corta: el tope se puede
pasar por lo que gaste el último.

**Qué queda de cada comando**, en `<carpeta>/salidas/`: lo que imprimió, cuánto tardó, cuántos
tokens usó y qué archivos cambió, igual que en las rondas de la PMO (`tests/ronda.py`).

**Qué se califica.** Las señales que el motor dejó en `resultados.json` a partir de la
configuración y de la ficha que escribió el agente, contra las esperadas de la clave: una de más
cuenta igual que una de menos. Y la extracción: lo que el agente llevó a la ficha contra lo que
la clave dice que traen los documentos escritos. El `evaluar.py` de cada familia prueba el motor
con la extracción correcta; esto prueba la extracción.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Lo que cambia de una familia a otra: dónde deja cada agente sus resultados y dónde está cada
# ficha que la clave describe. `{k}` es la ficha de una por clave —la de cada contrato—.
FAMILIAS = {
    "cfo": {"resultados": {"clara": "cierre/{periodo}/resultados.json", "tomas": "presupuesto/{anio}/resultados.json"},
            "fichas": {"cierre": ("clara", "cierre/{periodo}/ficha.json"), "presupuesto": ("tomas", "presupuesto/{anio}/ficha.json")},
            "periodos": lambda c: {"periodo": c["config"]["clara"]["period"], "anio": c["config"]["tomas"]["budget"]["year"]}},
    "clo": {"resultados": {"fidel": "contratos/resultados.json", "constanza": "cumplimiento/{periodo}/resultados.json"},
            "fichas": {"contratos": ("fidel", "contratos/{k}.json"), "cumplimiento": ("constanza", "cumplimiento/{periodo}/ficha.json")},
            "periodos": lambda c: {"periodo": c["periodo"]}},
}
# Lo que el agente escribe de suyo y no extrae de un documento: no se califica contra la clave.
PROPIOS = {"questions"}


def familia(sigla: str) -> dict:
    fa = json.loads((RAIZ / "families" / f"criterio-{sigla}" / "familia.json").read_text(encoding="utf-8"))
    return dict(FAMILIAS[sigla], sigla=sigla, material=RAIZ / "tests" / f"criterio-{sigla}" / "material",
                de={a["id"]: {x["id"] for x in a["senales"]} for a in fa["agentes"]},
                orden=[(a["id"], a["plugin"], c["id"]) for a in fa["agentes"] for c in sorted(a["comandos"], key=lambda c: c["n"])])


def de_carpeta(carpeta: Path) -> dict:
    return familia((carpeta / "familia.txt").read_text(encoding="utf-8").strip())
NOTA = ("(Sesión de prueba sin interfaz: nadie va a responder preguntas. La fecha de esta prueba es {hoy}: "
        "pásala al motor con `--today {hoy}` en cada llamada que la acepte. Términos: José Francisco Ñáñez "
        "acepta los términos vigentes de esta versión para esta prueba, fecha {hoy}; cuando el agente los "
        "muestre, regístralo con ese nombre. En cada otra pregunta toma la respuesta sugerida a partir de "
        "los documentos, dila en una línea y sigue. Si un comando pide algo que no existe, dilo y termina; "
        "no lo inventes.)")


def _j(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def _w(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def manifiesto(raiz: Path) -> dict:
    return {str(f.relative_to(raiz)): hashlib.sha1(f.read_bytes()).hexdigest()[:12]
            for f in raiz.rglob("*") if f.is_file() and ".claude" not in f.parts and ".git" not in f.parts}


def armar(a) -> int:
    """El espacio del agente es el material de la entidad sin su clave; la clave queda afuera."""
    F = familia(a.familia)
    origen = F["material"] / a.entidad
    if not (origen / "clave.json").is_file():
        print(f"no hay material para «{a.entidad}»: corre tests/criterio-{a.familia}/generar.py")
        return 1
    carpeta = Path(a.carpeta).expanduser()
    espacio = carpeta / "espacio"
    if espacio.exists():
        print(f"{espacio} ya existe; usa otra carpeta")
        return 1
    shutil.copytree(origen, espacio, ignore=shutil.ignore_patterns("clave.json"))
    shutil.copy2(origen / "clave.json", carpeta / "clave.json")
    (carpeta / "familia.txt").write_text(a.familia + "\n", encoding="utf-8")
    print(f"armado: {a.entidad} en {espacio}")
    return 0


def instalar(espacio: Path, orden: list) -> None:
    if (espacio / ".claude" / "settings.json").is_file():
        return
    subprocess.run(["git", "init", "-q"], cwd=espacio)
    for p in sorted({p for _, p, _ in orden}):
        subprocess.run(["claude", "plugin", "install", f"{p}@criterio", "--scope", "project"],
                       cwd=espacio, capture_output=True)


def correr(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio, sal = carpeta / "espacio", carpeta / "salidas"
    clave, F = _j(carpeta / "clave.json"), de_carpeta(carpeta)
    sal.mkdir(exist_ok=True)
    instalar(espacio, F["orden"])
    docs = next(iter(clave["config"].values()))["paths"]["documents"]
    gastado = sum(_j(f).get("tokens") or 0 for f in sal.glob("*.json"))
    for n, (agente, plugin, cmd) in enumerate(F["orden"], start=1):
        base = sal / f"{n:02d}-{cmd}"
        if base.with_suffix(".json").is_file() or (a.solo and n not in a.solo):
            continue
        if gastado >= a.tope:
            print(f"tope alcanzado: {gastado / 1e6:.2f} M de {a.tope / 1e6:.2f} M tokens; la ronda para antes de {cmd}")
            return 2
        arg = docs if cmd.endswith("-setup") else ""
        prompt = f"/{plugin}:{cmd} {arg}".strip() + "\n\n" + NOTA.format(hoy=clave["hoy"])
        antes, t0 = manifiesto(espacio), time.time()
        try:
            r = subprocess.run(["claude", "-p", prompt, "--permission-mode", "bypassPermissions",
                                "--output-format", "json"], cwd=espacio, capture_output=True,
                               text=True, timeout=a.limite)
            salida = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"subtype": "error", "result": r.stdout + r.stderr}
        except subprocess.TimeoutExpired:
            salida = {"subtype": "timeout", "result": f"no terminó en {a.limite} s"}
        despues, u = manifiesto(espacio), salida.get("usage") or {}
        fila = {"n": n, "agente": agente, "comando": cmd, "argumento": arg,
                "inicio": dt.datetime.fromtimestamp(t0, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
                "estado": salida.get("subtype"), "error": bool(salida.get("is_error")) or salida.get("subtype") != "success",
                "segundos": round(time.time() - t0), "turnos": salida.get("num_turns"),
                "tokens": sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens",
                                                       "cache_read_input_tokens", "output_tokens")),
                "tokens_salida": u.get("output_tokens"), "costo_usd": salida.get("total_cost_usd"),
                "modelo": next(iter(salida.get("modelUsage") or {}), None),
                "cambios": {"nuevos": sorted(set(despues) - set(antes)),
                            "modificados": sorted(k for k in set(antes) & set(despues) if antes[k] != despues[k]),
                            "borrados": sorted(set(antes) - set(despues))}}
        _w(base.with_suffix(".json"), fila)
        base.with_suffix(".md").write_text(f"# /{plugin}:{cmd} {arg}\n\n" + (salida.get("result") or ""), encoding="utf-8")
        gastado += fila["tokens"]
        print(f"{n:02d} {cmd:22} {fila['estado']:8} {fila['segundos']:4d} s {fila['tokens'] // 1000:6d} k "
              f"(acumulado {gastado / 1e6:.2f} M) +{len(fila['cambios']['nuevos'])} ~{len(fila['cambios']['modificados'])}",
              flush=True)
    return 0


def _norma(x):
    """3000000.0 y 3000000 son la misma cifra."""
    if isinstance(x, float) and x.is_integer():
        return int(x)
    if isinstance(x, dict):
        return {k: _norma(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_norma(v) for v in x]
    return x


def _igual(esperado, obtenido) -> bool:
    """Igual campo por campo, con una tolerancia: un texto del agente que contiene el de la clave
    —el mismo compromiso, dicho con más detalle— cuenta como bien. La diferencia se reporta igual."""
    esperado, obtenido = _norma(esperado), _norma(obtenido)
    if isinstance(esperado, str) and isinstance(obtenido, str):
        return esperado.strip().lower() in obtenido.strip().lower()
    if isinstance(esperado, dict) and isinstance(obtenido, dict):
        return all(_igual(v, obtenido.get(k)) for k, v in esperado.items())
    if isinstance(esperado, list) and isinstance(obtenido, list):
        return len(esperado) == len(obtenido) and all(_igual(a, b) for a, b in zip(esperado, obtenido))
    return esperado == obtenido


def _plano(x, pre=""):
    """Un dict anidado como pares ruta → valor, para comparar la ficha campo por campo."""
    if isinstance(x, dict):
        for k, v in x.items():
            yield from _plano(v, f"{pre}.{k}" if pre else k)
    else:
        yield pre, x


def calificar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    espacio, clave, F = carpeta / "espacio", _j(carpeta / "clave.json"), de_carpeta(carpeta)
    obtenido = set()
    # Solo el estado que dice la configuración que dejó el agente: un archivo escrito en otra
    # parte no es el resultado, y no se califica.
    estados = {espacio / _j(c)["paths"]["state"] for c in espacio.glob(".criterio/*/*/config.json")
               if (_j(c).get("paths") or {}).get("state")}
    # El periodo que dice la clave: un comando que calcula también el mes en curso deja otro
    # resultado, y ese no es el que se califica.
    per = F["periodos"](clave)
    for rol, patron in F["resultados"].items():
        for f in sorted(x for e in estados for x in e.glob(patron.format(**per))):
            obtenido |= {(x["signal"], x["key"]) for x in _j(f).get("alertas") or [] if x["signal"] in F["de"][rol]}
    corridos = {_j(f)["agente"] for f in (carpeta / "salidas").glob("*.json")}
    esperado = {(x["signal"], x["key"]) for x in clave["esperado"]
                if any(x["signal"] in F["de"][r] for r in corridos)}
    ok, sobran, faltan = obtenido & esperado, obtenido - esperado, esperado - obtenido
    extraccion = []
    for sub, ref in (clave.get("extraccion") or {}).items():
        rol, patron = F["fichas"][sub]
        if rol not in corridos:
            continue
        # Una ficha por clave (cada contrato), o una sola ficha: la más reciente de su patrón.
        partes = ({k: v for k, v in ref.items()} if "{k}" in patron else {"": ref})
        for k, esperado_k in partes.items():
            hallados = sorted(x for e in estados for x in e.glob(patron.format(k=k, **per)))
            hecho = dict(_plano(_j(hallados[-1]))) if hallados else {}
            for ruta, valor in _plano(esperado_k):
                if ruta.split(".")[0] in PROPIOS:
                    continue
                extraccion.append({"ficha": f"{sub}/{k}" if k else sub, "campo": ruta, "esperado": valor,
                                   "obtenido": hecho.get(ruta), "bien": _igual(valor, hecho.get(ruta))})
    tokens = sum(_j(f).get("tokens") or 0 for f in (carpeta / "salidas").glob("*.json"))
    res = {"entidad": clave["entidad"], "agentes": sorted(corridos), "tokens": tokens,
           "senales": {"esperadas": len(esperado), "acertadas": len(ok), "de_mas": sorted(map(list, sobran)),
                       "faltantes": sorted(map(list, faltan))},
           "extraccion": {"campos": len(extraccion), "bien": sum(x["bien"] for x in extraccion),
                          "mal": [x for x in extraccion if not x["bien"]]}}
    _w(carpeta / "calificacion.json", res)
    print(f"{clave['entidad']} · {', '.join(res['agentes'])} · {tokens / 1e6:.2f} M tokens")
    print(f"  señales: {len(ok)} de {len(esperado)} esperadas, {len(sobran)} de más, {len(faltan)} faltantes")
    print(f"  extracción: {res['extraccion']['bien']} de {res['extraccion']['campos']} campos bien")
    return 0 if not sobran and not faltan and not res["extraccion"]["mal"] else 1


EVIDENCIAS = RAIZ / "tests" / "evidencias" / "familias"


def _limpio(texto: str, carpeta: Path) -> str:
    """Sin rutas de la máquina donde corrió: el repositorio es público."""
    for ruta, nombre in ((carpeta / "espacio", "<espacio>"), (carpeta, "<ronda>"), (RAIZ, "<repositorio>"),
                         (Path.home() / ".claude", "<claude>")):
        texto = texto.replace(str(ruta.resolve()), nombre).replace(str(ruta), nombre)
    texto = re.sub(r"en-curso/[0-9a-f-]{36}", "en-curso/<sesion>", texto)
    return re.sub(r"/tmp/[^\s\"'`)]*", "<temporal>", texto)


def publicar(a) -> int:
    """Lo que dejó la ronda, al repositorio: cada salida con su costo, las que se repitieron tras
    corregir un defecto y la calificación. Lo que el agente escribió en su estado no se copia: lo
    resume la calificación, y el material lo vuelve a generar `generar.py`."""
    carpeta = Path(a.carpeta).expanduser()
    F = de_carpeta(carpeta)
    if not (carpeta / "calificacion.json").is_file():
        print("primero calificar")
        return 1
    destino = EVIDENCIAS / F["sigla"] / f"ronda-{a.ronda}" / a.nombre
    if destino.exists():
        shutil.rmtree(destino)
    for sub, nombre in (("salidas", "salidas"), ("primera", "repetidas")):
        for f in sorted((carpeta / sub).glob("*")) if (carpeta / sub).is_dir() else []:
            (destino / nombre).mkdir(parents=True, exist_ok=True)
            (destino / nombre / f.name).write_text(_limpio(f.read_text(encoding="utf-8"), carpeta), encoding="utf-8")
    (destino / "calificacion.json").write_text(_limpio((carpeta / "calificacion.json").read_text(encoding="utf-8"), carpeta),
                                              encoding="utf-8")
    print(f"publicado en {destino.relative_to(RAIZ)}")
    return 0


def resumen(_a) -> int:
    """La tabla de cada familia, desde las calificaciones publicadas. No se escribe a mano."""
    for fam in sorted(d for d in EVIDENCIAS.iterdir() if d.is_dir()) if EVIDENCIAS.is_dir() else []:
        filas = []
        for c in sorted(fam.glob("ronda-*/*/calificacion.json")):
            d = _j(c)
            rep_ = sum((_j(f).get("tokens") or 0) for f in (c.parent / "repetidas").glob("*.json")) if (c.parent / "repetidas").is_dir() else 0
            s_, e_ = d["senales"], d["extraccion"]
            filas.append(f"| {c.parent.parent.name} | [{c.parent.name}]({c.parent.parent.name}/{c.parent.name}/) | {d['entidad']} | "
                         f"{', '.join(d['agentes'])} | {s_['acertadas']} de {s_['esperadas']} · {len(s_['de_mas'])} de más | "
                         f"{e_['bien']} de {e_['campos']} | {d['tokens'] / 1e6:.2f} M" + (f" + {rep_ / 1e6:.2f} M repetidos" if rep_ else "") + " |")
        texto = (f"# criterio-{fam.name} · las rondas con el agente\n\n"
                 "<!-- generado por tests/ronda_familia.py resumen desde cada calificacion.json; no se edita a mano -->\n\n"
                 "Cada fila es una entidad del material corrida por los agentes con `tests/ronda_familia.py`, con un tope "
                 "de tokens fijado antes de empezar. Las señales se comparan por su nombre y su clave contra la clave que "
                 "el agente no ve; la extracción, campo por campo contra lo que traen los documentos escritos. En "
                 "`repetidas/` están las corridas que se repitieron después de corregir un defecto, con su costo.\n\n"
                 "| Ronda | Carpeta | Entidad | Agentes | Señales | Extracción | Tokens |\n|---|---|---|---|---|---|---|\n"
                 + "\n".join(filas) + "\n")
        (fam / "RONDAS.md").write_text(texto, encoding="utf-8")
        print(f"  {(fam / 'RONDAS.md').relative_to(RAIZ)} · {len(filas)} filas")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="accion", required=True)
    s = sp.add_parser("armar")
    s.add_argument("carpeta")
    s.add_argument("--familia", required=True, choices=sorted(FAMILIAS))
    s.add_argument("--entidad", required=True, help="una carpeta de tests/criterio-<familia>/material/")
    s = sp.add_parser("correr")
    s.add_argument("carpeta")
    s.add_argument("--tope", type=int, required=True, help="tokens; la ronda para antes del comando que lo pase")
    s.add_argument("--limite", type=int, default=900, help="segundos por comando")
    s.add_argument("--solo", type=int, nargs="*")
    s = sp.add_parser("calificar")
    s.add_argument("carpeta")
    s = sp.add_parser("publicar")
    s.add_argument("carpeta")
    s.add_argument("--ronda", type=int, required=True)
    s.add_argument("--nombre", required=True, help="la carpeta de la entidad en la evidencia")
    sp.add_parser("resumen")
    a = ap.parse_args()
    return {"armar": armar, "correr": correr, "calificar": calificar, "publicar": publicar, "resumen": resumen}[a.accion](a)


if __name__ == "__main__":
    sys.exit(main())
