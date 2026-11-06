#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La demostración: una organización de prueba con los agentes ya corridos y Rostrum listo.

    python3 scripts/demo.py           arma plugins/criterio-server/demo/criterio-demo.zip
    python3 scripts/demo.py --check   falla si el zip no es el que sale del material

Quien instala Criterio quiere verlo funcionar antes de abrir sus propios documentos. La
demostración es eso: `/criterio-server:server-demo` la descomprime en una carpeta y levanta
Rostrum sobre ella, en unos cinco minutos (decisión 0029).

**No tiene material propio.** Sale del mismo material de prueba de cada familia, sin su clave:
una entidad por familia. Lo que el agente extraería de los documentos lo escribe en el estado la
misma función con la que se prueba el motor (`sembrar`, en tests/criterio-<familia>/evaluar.py), y
las configuraciones son las de la clave, que son las que dejaría el setup. Después corre el motor
de cada agente, el de su propio plugin, como lo correría el agente: `compute` y un `reporte` por
cada parte. Nada se escribe a mano.

**El zip es determinista:** las fechas son las del material, los archivos van en orden y con una
fecha fija. Así `--check` puede compararlo byte a byte, y un cambio en un motor o en el material
que mueva la demostración rompe la verificación hasta que se regenere.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
P = RAIZ / "plugins"
ZIP = P / "criterio-server" / "demo" / "criterio-demo.zip"
ORGANIZACION = "Organización de demostración"
# Una entidad por familia: la de su primera ronda, con defectos sembrados.
DEMO = (("cfo", "banca"), ("clo", "banca"), ("cco", "retail-co"), ("ciso", "banca-co"), ("ea", "banca"))
FECHA_ZIP = (2026, 1, 1, 0, 0, 0)

sys.path.insert(0, str(P / "criterio-finance" / "scripts"))
from nucleo import AREA  # noqa: E402


def _modulo(ruta: Path, nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _motor(plugin: str) -> Path:
    return next(f for f in (P / plugin / "scripts").glob("*.py")
                if f.name in ("finanzas.py", "legal.py", "ventas.py", "seguridad.py", "asistente.py"))


def _correr(motor: Path, *args: str) -> str:
    r = subprocess.run([sys.executable, str(motor), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"{motor.parent.parent.name} {' '.join(args[:1])}: {r.stderr or r.stdout}")
    return r.stdout


def armar(destino: Path) -> list[str]:
    """Arma la organización de demostración en `destino`; devuelve lo que corrió."""
    hecho = []
    for sigla, entidad in DEMO:
        material = RAIZ / "tests" / f"criterio-{sigla}" / "material" / entidad
        clave = json.loads((material / "clave.json").read_text(encoding="utf-8"))
        familia = json.loads((RAIZ / "families" / f"criterio-{sigla}" / "familia.json").read_text(encoding="utf-8"))
        plugin_de = {a["id"]: a["plugin"] for a in familia["agentes"]}
        shutil.copytree(material, destino, dirs_exist_ok=True, ignore=shutil.ignore_patterns("clave.json"))
        primero = next(iter(clave["config"].values()))
        estado = destino / primero["paths"]["state"]
        _modulo(RAIZ / "tests" / f"criterio-{sigla}" / "evaluar.py", f"evaluar_{sigla}").sembrar(clave, estado)
        for agente, cfg in clave["config"].items():
            plugin = plugin_de[agente]
            instancia = Path(cfg["paths"]["documents"]).name
            ruta = destino / ".criterio" / AREA[plugin] / instancia / "config.json"
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            motor = _motor(plugin)
            salida = json.loads(_correr(motor, "compute", "--config", str(ruta), "--today", clave["hoy"]))
            r = json.loads(Path(salida["resultados"]).read_text(encoding="utf-8"))
            for parte in sorted(r.get("partes") or {}):
                _correr(motor, "reporte", "--config", str(ruta), "--today", clave["hoy"], "--what", parte)
            hecho.append(f"{sigla} · {agente} · {salida['total']} señales · {len(r.get('partes') or {})} reportes")
    hecho.append(pmo(destino))
    mapa = _modulo(P / "criterio-server" / "scripts" / "mapa.py", "mapa_demo")
    mapa.guardar(destino, organizacion=ORGANIZACION)
    m = mapa.destino(destino)
    d = json.loads(m.read_text(encoding="utf-8"))
    d["guardado"] = max(json.loads((RAIZ / "tests" / f"criterio-{s}" / "material" / e / "clave.json")
                                   .read_text(encoding="utf-8"))["hoy"] for s, e in DEMO)
    m.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    hecho.append(f"Rostrum · {len(d['entradas'])} entradas en el mapa")
    return hecho


def pmo(destino: Path) -> str:
    """La PMO: el portafolio de prueba de Vera, sus fichas de referencia —las que la ronda compara
    con lo que extrae el agente—, su cálculo y su informe, que es lo que Rostrum sirve."""
    prueba = RAIZ / "tests" / "criterio-portfolio"
    hoy = json.loads((prueba / "expected" / "hallazgos.json").read_text(encoding="utf-8"))["as_of"]
    shutil.copytree(prueba / "input", destino / "proyectos", dirs_exist_ok=True)
    estado = destino / "estado-portafolio"
    (estado / "records").mkdir(parents=True, exist_ok=True)
    for f in sorted((prueba / "expected" / "fichas").glob("*.json")):
        shutil.copyfile(f, estado / "records" / f.name)
    cfg = {"version": "0.1", "role": "pmo", "organization": {"name": ORGANIZACION},
           "paths": {"documents": "proyectos", "state": "estado-portafolio", "reports": "reportes-portafolio"},
           "cycle": {"committee": "biweekly", "report_lead_days": 2, "daily_sweep": True},
           "report": {"format": "html", "language": "es"}}
    ruta = destino / ".criterio" / "portafolio" / "config.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    scripts = P / "criterio-portfolio" / "scripts"
    calculo = json.loads(_correr(scripts / "portafolio.py", "compute", "--state", str(estado), "--today", hoy))
    _correr(scripts / "informe.py", "--state", str(estado), "--config", str(ruta), "--today", hoy)
    # La corrida del informe, como la registra Vera: es de donde Rostrum toma sus hallazgos. Su hora
    # de reloj se fija al día del material, para que la demostración salga igual cada vez.
    _correr(scripts / "portafolio.py", "corrida", "--state", str(estado), "--what", "report", "--today", hoy,
            "--informe", "reportes-portafolio", "--nota", "La demostración de Criterio: el informe sobre el portafolio de prueba")
    corridas = estado / "corridas.json"
    datos = json.loads(corridas.read_text(encoding="utf-8"))
    for c in datos:
        c["escrita"] = dt.datetime.fromisoformat(hoy).replace(tzinfo=dt.timezone.utc).timestamp()
    corridas.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return f"pmo · vera · {len(calculo.get('projects') or [])} proyectos · el informe del portafolio"


def empaquetar(carpeta: Path, zip_: Path) -> None:
    zip_.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(p for p in carpeta.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
            info = zipfile.ZipInfo(f"criterio-demo/{f.relative_to(carpeta).as_posix()}", FECHA_ZIP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, f.read_bytes())


def main() -> int:
    ap = argparse.ArgumentParser(description="La demostración de Criterio.")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        carpeta = Path(tmp) / "criterio-demo"
        hecho = armar(carpeta)
        nuevo = Path(tmp) / "criterio-demo.zip"
        empaquetar(carpeta, nuevo)
        if a.check:
            if not ZIP.is_file() or ZIP.read_bytes() != nuevo.read_bytes():
                print(f"  ✗ {ZIP.relative_to(RAIZ)} no es lo que sale del material y los motores: corre scripts/demo.py")
                return 1
            print(f"  la demostración sale del material: {len(hecho) - 1} agentes y Rostrum, "
                  f"{ZIP.stat().st_size // 1024} KB")
            return 0
        ZIP.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(nuevo, ZIP)
    for h in hecho:
        print(f"  {h}")
    print(f"  {ZIP.relative_to(RAIZ)} · {ZIP.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
