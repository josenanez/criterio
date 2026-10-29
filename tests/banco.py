#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El banco de pruebas del agente: un entorno por industria, una calificación por corrida.

    python3 tests/banco.py armar <entorno> <carpeta> [--proyectos 12 --productos 10]
    python3 tests/banco.py calificar <carpeta> --version 0.3.5 --tipo primera
    python3 tests/banco.py origen <id> --agente 0 --codigo 10 --clave 6
    python3 tests/banco.py verificar
    python3 tests/banco.py tabla

Entornos: bancos, cooperativas, retail, mineria, construccion, oil-gas, telecomunicaciones, logistica (`tests/sintetico/sectores.py`).

**Qué mide.** La cadena completa: el comando que el modelo ejecuta, los skills que carga y
las fichas que escribe leyendo documentos; después el script calcula las señales sobre
esas fichas y se comparan con la clave. Es la cifra que importa, porque es el producto.
`fiabilidad.py` mide otra cosa —el script sobre fichas bien construidas— y no se mezclan.

**Cómo se arma.** `armar` deja `clave/` (lo que el simulador sabe: los hechos y la clave)
y `espacio/documentos/` (lo único que el agente ve). El agente se corre dentro de
`espacio/`. Una clave al alcance del agente invalida la prueba.

**Cómo se reporta.** Cada calificación guarda los conteos, no solo porcentajes, y dos
intervalos de confianza del 95%: Wilson, que supone hallazgos independientes, y bootstrap
por proyecto, que no lo supone —los hallazgos de un mismo proyecto fallan juntos—. Se
publica el más ancho de los dos. Y cada una dice si es la **primera** corrida de esa
versión sobre ese material o una **corregida** después de verlo: la segunda no es una
medición independiente, y la página no las mezcla.

`origen` es lo único que escribe una persona: de los errores, cuántos fueron de la
lectura del modelo, cuántos del código y cuántos de la clave. Va marcado como anotado y
la puerta exige que sume lo mismo que los errores.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import random
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tests" / "sintetico"))
import fiabilidad  # noqa: E402
import sectores  # noqa: E402

REGISTRO = RAIZ / "tests" / "evidencias" / "calificaciones.json"


def leer() -> list:
    return json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.is_file() else []


def guardar(filas: list) -> None:
    REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    REGISTRO.write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def wilson(k: int, n: int, z: float = 1.96) -> list:
    if n == 0:
        return [None, None]
    p, d = k / n, 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(100 * max(0.0, c - h), 1), round(100 * min(1.0, c + h), 1)]


def bootstrap(por_caso: dict, que: str, veces: int = 4000) -> list:
    """Remuestrea proyectos, no hallazgos. Semilla fija: la misma corrida da el mismo
    intervalo cada vez que se califica."""
    casos = list(por_caso.values())
    if not casos:
        return [None, None]
    rnd, valores = random.Random(20261015), []
    for _ in range(veces):
        m = [rnd.choice(casos) for _ in casos]
        a = sum(c["aciertos"] for c in m)
        otro = sum(len(c["falsos_positivos" if que == "precision" else "falsos_negativos"]) for c in m)
        if a + otro:
            valores.append(100 * a / (a + otro))
    valores.sort()
    if not valores:
        return [None, None]
    return [round(valores[int(0.025 * len(valores))], 1),
            round(valores[min(len(valores) - 1, int(0.975 * len(valores)))], 1)]


def ancho(a: list, b: list) -> list:
    if None in a:
        return b
    if None in b:
        return a
    return [min(a[0], b[0]), max(a[1], b[1])]


# ── armar ─────────────────────────────────────────────────────────────────

def armar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    clave, espacio = carpeta / "clave", carpeta / "espacio"
    if a.dia == 1 and carpeta.exists():
        sys.exit(f"{carpeta} ya existe; un entorno no se rearma encima de una prueba")
    # Con --semanas N el simulador corre los días 1..N y el último cae hoy: la
    # organización llega con N semanas de vida —minutas, compromisos reprogramados,
    # proyectos que se callaron—, que es lo que un agente encuentra en una carpeta real.
    dias = range(1, a.semanas + 1) if a.semanas else [a.dia]
    for d in dias:
        cmd = [sys.executable, str(RAIZ / "tests" / "sintetico" / "simulador.py"), str(clave),
               "--dia", str(d), "--proyectos", str(a.proyectos), "--productos", str(a.productos),
               "--formatos", "--dias", str(a.semanas or a.dias), "--ronda", str(a.ronda)]
        cmd += ["--disposicion", a.disposicion] if a.disposicion else []
        cmd += ["--sector", a.entorno] if d == 1 else []
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr)
    docs = espacio / "documentos"
    if docs.exists():
        shutil.rmtree(docs)
    shutil.copytree(clave / "documentos", docs, copy_function=shutil.copy2)
    shutil.rmtree(clave / "documentos")
    (espacio / "estado").mkdir(parents=True, exist_ok=True)
    n = sum(1 for f in docs.rglob("*") if f.is_file())
    print(f"{a.entorno} · {a.semanas or 1} semana(s) · {n} documentos en {docs}")
    print(f"la clave queda en {clave}; el agente se corre en {espacio}")
    return 0


# ── calificar ─────────────────────────────────────────────────────────────

def calificar(a) -> int:
    carpeta = Path(a.carpeta).expanduser()
    # La clave de una ronda agrega lo que siembran las notas de Samuel; si no hay, la del simulador.
    ronda = carpeta / "clave" / "esperado-ronda.json"
    clave = json.loads((ronda if ronda.is_file() else carpeta / "clave" / "esperado.json").read_text(encoding="utf-8"))
    org = carpeta / "clave" / "organizacion.json"
    entorno = (json.loads(org.read_text(encoding="utf-8")).get("sector")
               if org.is_file() else None) or a.entorno
    if entorno not in sectores.PERFILES:
        sys.exit(f"no sé de qué entorno es {carpeta}: pásalo con --entorno")
    hoy = clave.get("hoy") or clave.get("generado")
    esperado = {k: [x["signal"] if isinstance(x, dict) else x for x in v]
                for k, v in clave["esperado"].items() if k.startswith("PRY")}
    # El estado de Vera es el que dice su configuración: en retail eligió
    # `estado-portafolio/`, y calificar `estado/` a ciegas dio 0 de 36.
    cfg = carpeta / "espacio" / ".criterio" / "portafolio" / "config.json"
    estado = carpeta / "espacio" / (json.loads(cfg.read_text(encoding="utf-8")).get("paths", {}).get("state", "estado")
                                    if cfg.is_file() else "estado")
    if a.commit:
        # Las señales se calculan con el código de esa versión, no con el de hoy: una
        # corrida vieja calificada con el script corregido no es la corrida que pasó.
        import tempfile
        tmp = Path(tempfile.mkdtemp())
        for nombre in ("portafolio.py", "texto.py"):
            r = subprocess.run(["git", "-C", str(RAIZ), "show",
                                f"{a.commit}:plugins/criterio-portfolio/scripts/{nombre}"],
                               capture_output=True, text=True)
            if r.returncode == 0:
                (tmp / nombre).write_text(r.stdout, encoding="utf-8")
        fiabilidad.PORTFOLIO = tmp / "portafolio.py"
    obtenido, _, error = fiabilidad.hallazgos_portafolio(estado, hoy)
    if error:
        sys.exit(f"no se pudo calcular: {error}")
    con_ficha = {f.stem for f in (estado / "records").glob("*.json")}
    cal = fiabilidad.calificar(esperado, obtenido)
    t = fiabilidad.totales(cal)
    ac, fp, fn = t["aciertos"], t["falsos_positivos"], t["falsos_negativos"]
    controles = [c for c in clave.get("controles", []) if c.startswith("PRY")]
    fila = {
        "id": f"{dt.date.today().isoformat()}-{entorno}-{a.agente}-{len(leer()) + 1}",
        "fecha": dt.date.today().isoformat(), "corte": hoy, "entorno": entorno,
        "industria": sectores.INDUSTRIA[entorno], "etiqueta": sectores.PERFILES[entorno]["ETIQUETA"],
        "material": a.material, "agente": a.agente, "version": a.version, "tipo": a.tipo,
        "codigo": a.commit or subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "--short", "HEAD"],
                                             capture_output=True, text=True).stdout.strip(),
        "modelo": a.modelo, "proyectos": len(esperado), "fichas": len(con_ficha & set(esperado)),
        "aciertos": ac, "falsos_positivos": fp, "falsos_negativos": fn,
        "precision": t["precision"], "cobertura": t["cobertura"],
        "ic_precision": ancho(wilson(ac, ac + fp), bootstrap(cal["por_caso"], "precision")),
        "ic_cobertura": ancho(wilson(ac, ac + fn), bootstrap(cal["por_caso"], "cobertura")),
        "controles": len(controles),
        "controles_limpios": sum(1 for c in controles if not obtenido.get(c)),
        # Por proyecto, para que un resumen de varias industrias remuestree proyectos.
        "por_caso": {c: [r["aciertos"], len(r["falsos_positivos"]), len(r["falsos_negativos"])]
                     for c, r in sorted(cal["por_caso"].items())},
        # Por tipo de alerta: es lo que decide si alguien actúa sobre una alerta concreta.
        "por_senal": {k: {"aciertos": v["aciertos"], "falsos_positivos": v["fp"], "falsos_negativos": v["fn"]}
                      for k, v in sorted(cal["por_senal"].items())},
        "errores": {c: {"faltan": r["falsos_negativos"], "sobran": r["falsos_positivos"]}
                    for c, r in sorted(cal["por_caso"].items())
                    if r["falsos_negativos"] or r["falsos_positivos"]},
        "origen": None, "nota": a.nota,
    }
    # Calificar otra vez la misma corrida la reemplaza: una corrida es una fila.
    filas = [f for f in leer() if not (f.get("material") == fila["material"] and f["entorno"] == entorno
                                        and f["version"] == fila["version"] and f["tipo"] == fila["tipo"]
                                        and f["fecha"] == fila["fecha"] and f["agente"] == fila["agente"])]
    fila["id"] = f"{fila['fecha']}-{entorno}-{a.agente}-{len(filas) + 1}"
    origen_previo = next((f.get("origen") for f in leer() if f["id"] == fila["id"]), None)
    fila["origen"] = fila["origen"] or origen_previo
    filas.append(fila)
    guardar(filas)
    print(json.dumps({k: fila[k] for k in ("id", "tipo", "aciertos", "falsos_positivos",
                                          "falsos_negativos", "precision", "cobertura",
                                          "ic_precision", "ic_cobertura", "controles_limpios")},
                     ensure_ascii=False))
    for c, e in fila["errores"].items():
        print(f"  {c}: faltan {e['faltan']} · sobran {e['sobran']}")
    return 0


def origen(a) -> int:
    filas = leer()
    f = next((x for x in filas if x["id"] == a.id), None)
    if not f:
        sys.exit(f"no hay calificación {a.id}")
    f["origen"] = {"agente": a.agente, "codigo": a.codigo, "clave": a.clave,
                   "nota": a.nota, "quien": "anotado a mano"}
    guardar(filas)
    print(f"{a.id}: agente {a.agente} · código {a.codigo} · clave {a.clave}")
    return verificar(None)


# ── la puerta ─────────────────────────────────────────────────────────────

def verificar(_a) -> int:
    malas = []
    for f in leer():
        ac, fp, fn = f["aciertos"], f["falsos_positivos"], f["falsos_negativos"]
        cuenta_errores = sum(len(e["faltan"]) + len(e["sobran"]) for e in f["errores"].values())
        if cuenta_errores != fp + fn:
            malas.append(f"{f['id']}: el detalle suma {cuenta_errores} errores y los totales {fp + fn}")
        for nombre, k, n in (("precision", ac, ac + fp), ("cobertura", ac, ac + fn)):
            if n and f[nombre] != round(100 * k / n, 1):
                malas.append(f"{f['id']}: {nombre} no sale de los conteos")
            lo, hi = f[f"ic_{nombre}"]
            if n and not (lo <= f[nombre] <= hi):
                malas.append(f"{f['id']}: el intervalo de {nombre} no contiene la cifra")
        if f["tipo"] not in ("primera", "corregida"):
            malas.append(f"{f['id']}: tipo «{f['tipo']}» · es primera o corregida")
        o = f.get("origen")
        if o and o["agente"] + o["codigo"] + o["clave"] != fp + fn:
            malas.append(f"{f['id']}: el origen suma {o['agente'] + o['codigo'] + o['clave']} "
                         f"y hubo {fp + fn} errores")
    for m in malas:
        print("  FALLA", m)
    if not malas:
        print(f"  OK    {len(leer())} calificaciones, cada cifra sale de sus conteos")
    return 1 if malas else 0


def tabla(_a) -> int:
    for f in leer():
        o = f.get("origen") or {}
        print(f"{f['id']:40} {f['tipo']:9} v{f['version']:6} {f['aciertos']:3}/{f['aciertos'] + f['falsos_positivos']:<3} "
              f"prec {f['precision']}% {f['ic_precision']}  {f['aciertos']}/{f['aciertos'] + f['falsos_negativos']} "
              f"cob {f['cobertura']}% {f['ic_cobertura']}  origen {o.get('agente', '?')}/{o.get('codigo', '?')}/{o.get('clave', '?')}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="accion", required=True)
    s = sub.add_parser("armar")
    s.add_argument("entorno", choices=sorted(sectores.PERFILES))
    s.add_argument("carpeta")
    s.add_argument("--dia", type=int, default=1)
    s.add_argument("--proyectos", type=int, default=12)
    s.add_argument("--productos", type=int, default=10)
    # Con --dias 1 el material cae en la fecha real: el agente y la clave miran el mismo
    # día. Con el valor del simulador (5) el día 1 caía cuatro semanas atrás.
    s.add_argument("--dias", type=int, default=1)
    s.add_argument("--ronda", type=int, default=0)
    s.add_argument("--semanas", type=int, default=0, help="corre los días 1..N; el último cae hoy")
    s.add_argument("--disposicion", default=None)
    s = sub.add_parser("calificar")
    s.add_argument("carpeta")
    s.add_argument("--version", required=True)
    s.add_argument("--tipo", required=True, choices=("primera", "corregida"))
    s.add_argument("--agente", default="vera")
    s.add_argument("--modelo", default="claude-sonnet-5-5")
    s.add_argument("--material", default="simulador", help="simulador u organizacion (casos escritos a mano)")
    s.add_argument("--entorno", default=None)
    s.add_argument("--nota", default=None)
    s.add_argument("--commit", default=None, help="calcular con el script de ese commit")
    s = sub.add_parser("origen")
    s.add_argument("id")
    for k in ("agente", "codigo", "clave"):
        s.add_argument(f"--{k}", type=int, required=True)
    s.add_argument("--nota", default=None)
    sub.add_parser("verificar")
    sub.add_parser("tabla")
    a = ap.parse_args()
    sys.exit({"armar": armar, "calificar": calificar, "origen": origen,
              "verificar": verificar, "tabla": tabla}[a.accion](a))
