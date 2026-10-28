#!/usr/bin/env python3
"""Criterio — el mapa de Rostrum: qué agentes trabajan en una carpeta y dónde está cada estado.

    python3 mapa.py descubrir --raiz <carpeta>       lo que encuentra, sin escribir nada
    python3 mapa.py guardar --raiz <carpeta> [--sin <id> ...] [--organizacion "<nombre>"]
    python3 mapa.py revisar --mapa <carpeta>/.criterio/rostrum/config.json
    python3 mapa.py terminos --config <mapa>            ¿está vigente la aceptación de los términos?
    python3 mapa.py aceptar --config <mapa> --por "Nombre Apellido"
    python3 mapa.py --selftest

Cada agente deja su configuración en la carpeta donde trabaja, en `.criterio/<área>/config.json`
o `.criterio/<área>/<instancia>/config.json` —la PMO en `portafolio/`, Clara en
`finanzas/<entidad>/`, Fidel en `legal/<entidad>/`…—, y esa configuración dice dónde está su
estado. Rostrum no adivina nada más: **lo que no está en el mapa no se sirve** (ADR 0010).

`descubrir` lee esas configuraciones y devuelve lo que encontró; `guardar` escribe el mapa en
`.criterio/rostrum/config.json` con lo que la persona confirmó, y `revisar` compara un mapa
guardado con lo que hay hoy en el disco: una familia que se instaló después aparece como nueva
y entra volviendo a guardar, sin tocar el servidor. Nada de esto escribe en el estado de ningún
agente. Librería estándar, sin dependencias.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import raiz as raiz_mod  # noqa: E402  la marca de la carpeta raíz, la misma de cada agente


def registro() -> dict:
    """Los agentes de todas las familias, como los escribe scripts/familias.py."""
    return json.loads((AQUI / "agentes.json").read_text(encoding="utf-8"))


def _leer(f: Path):
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _ruta(v: str | None, raiz: Path) -> Path | None:
    """Una ruta de una configuración: relativa a la carpeta donde corre el agente, que es la raíz."""
    if not v:
        return None
    p = Path(v).expanduser()
    return p if p.is_absolute() else raiz / p


def _relativa(p: Path | None, raiz: Path) -> str | None:
    if p is None:
        return None
    try:
        return p.resolve().relative_to(raiz.resolve()).as_posix()
    except ValueError:
        return str(p)


def privados(agente: dict, cfg: dict) -> dict:
    """Los comandos de un agente que no se publican, con las señales que no se muestran: los que su
    familia marca como privados y su configuración no abre (ADR 0019, las comisiones de Valeria)."""
    out = {}
    for cmd, p in (agente.get("privados") or {}).items():
        v = cfg
        for k in str(p.get("config") or "").split("."):
            v = v.get(k) if isinstance(v, dict) else None
        if v is not True:
            out[cmd] = sorted(p.get("senales") or [])
    return out


def descubrir(raiz: Path) -> dict:
    """Las configuraciones de agente bajo `<raiz>/.criterio/`, con su estado."""
    reg = registro()
    entradas, problemas, no_publica = [], [], []
    for a in reg["agentes"]:
        base = raiz / ".criterio" / a["area"]
        if not base.is_dir():
            continue
        for f in [base / "config.json"] + sorted(base.glob("*/config.json")):
            if not f.is_file():
                continue
            cfg = _leer(f)
            instancia = None if f.parent == base else f.parent.name
            ident = a["area"] if instancia is None else f"{a['area']}/{instancia}"
            if not isinstance(cfg, dict):
                problemas.append(f"{_relativa(f, raiz)}: no se puede leer como JSON")
                continue
            # Una configuración que dice que no se publica no entra al mapa: la de Ofelia, por
            # omisión (ADR 0012). Se dice, para que nadie la busque en el portal.
            if cfg.get("publish_rostrum") is False:
                no_publica.append(ident)
                continue
            paths = cfg.get("paths") or {}
            estado = _ruta(paths.get("state"), raiz)
            nombre = (cfg.get("organization") or {}).get("name") or (cfg.get("entity") or {}).get("name") or instancia
            e = {"id": ident, "area": a["area"], "agente": a["id"], "nombre_agente": a["nombre"], "familia": a["familia"],
                 "instancia": instancia, "nombre": nombre, "config": _relativa(f, raiz), "estado": _relativa(estado, raiz),
                 "informe": None, "existe": bool(estado and estado.is_dir()), "privados": privados(a, cfg)}
            if a["area"] == "portafolio":
                e["informe"] = _relativa(_ruta(paths.get("reports"), raiz), raiz)
            docs = _ruta(paths.get("documents"), raiz)
            e["documentos"] = _relativa(docs, raiz)
            marca = raiz_mod.leer(docs, a["plugin"]) if docs and docs.is_dir() and a["plugin"] in raiz_mod.DESTINO else None
            e["marcada"] = marca["archivo"] if marca else None
            if estado is None:
                problemas.append(f"{ident}: {e['config']} no dice dónde está el estado (paths.state)")
            elif not e["existe"]:
                problemas.append(f"{ident}: la carpeta de estado {e['estado']} no existe todavía; el agente no ha corrido")
            entradas.append(e)
    return {"raiz": str(raiz), "entradas": entradas, "problemas": problemas, "no_publica": no_publica,
            "sin_marca": [e["id"] for e in entradas if e["documentos"] and not e["marcada"]],
            "familias": sorted({e["familia"] for e in entradas})}


def destino(raiz: Path) -> Path:
    return raiz / ".criterio" / "rostrum" / "config.json"


def guardar(raiz: Path, sin: list[str] | None = None, organizacion: str | None = None) -> dict:
    """Escribe el mapa con lo encontrado, menos lo que la persona dejó fuera."""
    d = descubrir(raiz)
    entradas = [e for e in d["entradas"] if e["id"] not in set(sin or [])]
    previo = _leer(destino(raiz)) or {}
    org = organizacion or (previo.get("organization") or {}).get("name") \
        or next((e["nombre"] for e in entradas if e["area"] == "portafolio" and e["nombre"]), None)
    mapa = {"version": "0.1", "role": "servidor",
            "organization": {"name": org} if org else {},
            "entradas": [{k: v for k, v in e.items() if k != "existe"} for e in entradas],
            "fuera": sorted(set(sin or [])), "guardado": dt.date.today().isoformat()}
    f = destino(raiz)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(mapa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"mapa": _relativa(f, raiz), "entradas": [e["id"] for e in mapa["entradas"]], "fuera": mapa["fuera"],
            "no_publica": d["no_publica"], "problemas": d["problemas"]}


def cargar(mapa: Path) -> tuple[dict, list[dict], Path]:
    """El mapa guardado, con cada estado como ruta. La raíz es la carpeta que contiene `.criterio/`."""
    cfg = _leer(mapa)
    if not isinstance(cfg, dict):
        raise SystemExit(f"{mapa} no existe o no es un mapa: corre /criterio-server:server-setup")
    raiz = mapa.resolve().parent.parent.parent
    entradas = []
    for e in cfg.get("entradas") or []:
        x = dict(e)
        x["_estado"] = _ruta(e.get("estado"), raiz)
        x["_informe"] = _ruta(e.get("informe"), raiz)
        x["_config"] = _ruta(e.get("config"), raiz)
        # Dónde trabaja el agente, completo: la carpeta raíz, la que tiene `.criterio/`, y la de sus
        # documentos. Rostrum la muestra en cada familia para que nadie tenga que adivinarla.
        x["_raiz"] = raiz
        x["_documentos"] = _ruta(e.get("documentos"), raiz)
        # Lo privado se lee de la configuración de hoy, no del mapa guardado: abrir o cerrar las
        # comisiones no pide volver a armar el mapa.
        ag = next((a for a in registro()["agentes"] if a["area"] == e.get("area")), {})
        cfg_ag = _leer(x["_config"]) if x["_config"] and x["_config"].is_file() else None
        x["privados"] = privados(ag, cfg_ag) if isinstance(cfg_ag, dict) else privados(ag, {})
        entradas.append(x)
    return cfg, entradas, raiz


def revisar(mapa: Path) -> dict:
    """El mapa contra el disco: lo nuevo, lo que desapareció y lo que todavía no tiene estado."""
    cfg, entradas, raiz = cargar(mapa)
    hoy = {e["id"]: e for e in descubrir(raiz)["entradas"]}
    en_mapa = {e["id"] for e in entradas}
    fuera = set(cfg.get("fuera") or [])
    return {"nuevas": sorted(set(hoy) - en_mapa - fuera),
            "desaparecidas": sorted(en_mapa - set(hoy)),
            "sin_estado": sorted(e["id"] for e in entradas if not (e["_estado"] and e["_estado"].is_dir())),
            "entradas": sorted(en_mapa), "fuera": sorted(fuera)}


def selftest() -> int:
    import tempfile
    fallas = []

    def ok(que, real, esperado):
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}')
        if real != esperado:
            fallas.append(f"{que}: {real!r} en vez de {esperado!r}")

    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp)

        def config(rel, cuerpo):
            f = raiz / ".criterio" / rel / "config.json"
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps(cuerpo), encoding="utf-8")
        config("portafolio", {"organization": {"name": "Banco de Prueba"},
                              "paths": {"state": "pmo/estado", "reports": "pmo/informe"}})
        config("finanzas/900-banco", {"entity": {"name": "Banco de Prueba"},
                                      "paths": {"state": "estado-finanzas/900-banco", "documents": "finanzas/900-banco"}})
        (raiz / "finanzas/900-banco").mkdir(parents=True)
        raiz_mod.marcar(raiz / "finanzas/900-banco", "criterio-finance", "Banco de Prueba", "prueba", hoy=dt.date(2026, 10, 21))
        config("legal/900-banco", {"entity": {"name": "Banco de Prueba"},
                                   "paths": {"state": "estado-legal/900-banco", "documents": "legal/900-banco"}})
        config("presupuesto/900-banco", {"paths": {}})
        (raiz / ".criterio" / "otra-cosa").mkdir()
        for d in ("pmo/estado", "estado-finanzas/900-banco"):
            (raiz / d).mkdir(parents=True)
        d = descubrir(raiz)
        ok("encuentra cada agente por la carpeta de su configuración",
           [e["id"] for e in d["entradas"]], ["portafolio", "finanzas/900-banco", "presupuesto/900-banco", "legal/900-banco"])
        ok("con su familia", d["familias"], ["cfo", "clo", "pmo"])
        ok("y lo que falta lo dice: un estado que no existe, una configuración sin estado",
           sorted(p.split(":")[0] for p in d["problemas"]), ["legal/900-banco", "presupuesto/900-banco"])
        fin = next(e for e in d["entradas"] if e["id"] == "finanzas/900-banco")
        ok("cada entrada dice dónde están sus documentos y si la raíz está marcada",
           (fin["documentos"], fin["marcada"]), ("finanzas/900-banco", "_CRITERIO_FINANZAS.txt"))
        ok("y una raíz sin marca se ve", d["sin_marca"], ["legal/900-banco"])
        ok("el informe de la PMO va con su entrada",
           next(e["informe"] for e in d["entradas"] if e["area"] == "portafolio"), "pmo/informe")
        g = guardar(raiz, sin=["presupuesto/900-banco"])
        ok("el mapa guarda lo confirmado y deja fuera lo que la persona quitó",
           (g["entradas"], g["fuera"]), (["portafolio", "finanzas/900-banco", "legal/900-banco"], ["presupuesto/900-banco"]))
        cfg, entradas, r = cargar(destino(raiz))
        ok("al cargarlo, la raíz es la carpeta de trabajo", r.resolve(), raiz.resolve())
        ok("y el nombre de la organización sale de la PMO", cfg["organization"]["name"], "Banco de Prueba")
        ok("las rutas del mapa son relativas: el mapa no publica la carpeta del usuario",
           all(not Path(e["estado"]).is_absolute() for e in cfg["entradas"]), True)
        fin_c = next(e for e in entradas if e["id"] == "finanzas/900-banco")
        ok("pero al cargarlo cada entrada sabe dónde trabaja, completo: la raíz y sus documentos",
           (fin_c["_raiz"].resolve(), fin_c["_documentos"].resolve()),
           (raiz.resolve(), (raiz / "finanzas" / "900-banco").resolve()))
        config("cumplimiento/900-banco", {"paths": {"state": "estado-legal/900-banco"}})
        rv = revisar(destino(raiz))
        ok("una familia instalada después aparece como nueva, y lo dejado fuera no vuelve",
           (rv["nuevas"], rv["fuera"]), (["cumplimiento/900-banco"], ["presupuesto/900-banco"]))
        ok("y el estado que falta se ve", rv["sin_estado"], ["legal/900-banco"])
        config("direccion/presidencia", {"entity": {"name": "Banco de Prueba"}, "publish_rostrum": False,
                                         "paths": {"state": "estado-direccion/presidencia", "documents": "direccion/presidencia"}})
        d = descubrir(raiz)
        ok("la oficina que no publica no entra al mapa, y se dice",
           ("direccion/presidencia" in [e["id"] for e in d["entradas"]], d["no_publica"]), (False, ["direccion/presidencia"]))
        config("direccion/presidencia", {"entity": {"name": "Banco de Prueba"}, "publish_rostrum": True,
                                         "paths": {"state": "estado-direccion/presidencia", "documents": "direccion/presidencia"}})
        ok("y si su configuración lo dice, entra", "direccion/presidencia" in [e["id"] for e in descubrir(raiz)["entradas"]], True)
        # Las comisiones de Valeria no se publican salvo que su configuración lo diga (ADR 0019).
        val = {"privados": {"commission-check": {"config": "revenue.publish_commissions", "senales": ["commission_differs_from_plan"]}}}
        ok("un comando privado queda fuera por omisión, con sus señales",
           privados(val, {"revenue": {}}), {"commission-check": ["commission_differs_from_plan"]})
        ok("y la configuración lo abre", privados(val, {"revenue": {"publish_commissions": True}}), {})
    print()
    if fallas:
        print(f"{len(fallas)} falla(s)")
        return 1
    print("todo pasa")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="El mapa de Rostrum: qué agentes hay y dónde está cada estado.")
    ap.add_argument("action", choices=["descubrir", "guardar", "revisar", "terminos", "aceptar"], nargs="?")
    ap.add_argument("--config", type=Path, default=None, help="el mapa, para los términos")
    ap.add_argument("--por", default=None)
    ap.add_argument("--idioma", default=None)
    ap.add_argument("--raiz", type=Path, default=None, help="la carpeta de trabajo; por defecto, donde corre")
    ap.add_argument("--mapa", type=Path, default=None)
    ap.add_argument("--sin", action="append", default=[], help="una entrada que no se sirve")
    ap.add_argument("--organizacion", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    raiz = (a.raiz or Path.cwd()).expanduser()
    if a.action == "descubrir":
        print(json.dumps(descubrir(raiz), ensure_ascii=False, indent=2))
    elif a.action == "guardar":
        print(json.dumps(guardar(raiz, a.sin, a.organizacion), ensure_ascii=False, indent=2))
    elif a.action == "revisar":
        print(json.dumps(revisar(a.mapa or destino(raiz)), ensure_ascii=False, indent=2))
    elif a.action in ("terminos", "aceptar"):
        # Los términos se aceptan como en cualquier agente: el comprobante queda en `.criterio/terminos/`.
        sys.path.insert(0, str(AQUI))
        import terminos
        cfg = a.config or destino(raiz)
        if a.action == "terminos":
            r = terminos.estado(cfg)
            print(json.dumps(r, ensure_ascii=False, indent=2))
            return 0 if r["vigente"] else 3
        print(json.dumps(terminos.aceptar(cfg, a.por, a.idioma), ensure_ascii=False, indent=2))
    else:
        ap.error("descubrir, guardar o revisar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
