# -*- coding: utf-8 -*-
"""El registro de lo que cada comando produjo cuando lo corrió un agente de verdad.

    python3 tests/sintetico/evidencia.py registrar --agente portfolio \\
        --comando portfolio-scan --dia 1 --segundos 95 --documentos 146 \\
        --hallazgos 0 --no-supo "ninguna autoridad de escalamiento en los 50" \\
        --salida /tmp/lo-que-imprimio.md

    python3 tests/sintetico/evidencia.py cobertura      # cuántos de los 37, y cuáles no
    python3 tests/sintetico/evidencia.py verificar      # puerta: el registro no miente

`fiabilidad.py` mide lo que el **script** calcula, y esa capa está cubierta. Esto es la
otra: **lo que el modelo hizo al ejecutar el comando.** Sin registro, cinco días de
corridas dejan cero evidencia de la capa que el repositorio declara sin probar, y la página
de resultados de cada agente sigue diciendo «no se han corrido» para siempre.

Un comando sin entrada aquí **no se probó**. No se cuenta como aprobado, no se redondea, y
la página lo dice con ese nombre.
"""
import argparse
import json
import shutil
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).parent.parent.parent
EVID = RAIZ / "tests" / "evidencias"
REGISTRO = EVID / "registro.json"

AGENTES = {"portfolio": "criterio-portfolio", "project": "criterio-project",
           "product": "criterio-product"}


def comandos_de(agente: str) -> list:
    d = RAIZ / "plugins" / AGENTES[agente] / "commands"
    return sorted(c.stem for c in d.glob("*.md"))


def leer() -> list:
    if not REGISTRO.exists():
        return []
    return json.loads(REGISTRO.read_text(encoding="utf-8"))


def guardar(filas: list):
    EVID.mkdir(parents=True, exist_ok=True)
    REGISTRO.write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")


def registrar(a) -> int:
    if a.comando not in comandos_de(a.agente):
        sys.exit(f"«{a.comando}» no es un comando de {AGENTES[a.agente]}. "
                 f"Son: {', '.join(comandos_de(a.agente))}")

    destino = EVID / f"dia-{a.dia}"
    destino.mkdir(parents=True, exist_ok=True)
    archivo = destino / f"{a.comando}.md"
    if a.salida:
        origen = Path(a.salida).expanduser()
        if not origen.is_file():
            sys.exit(f"no encuentro {origen}")
        # La salida del comando se guarda tal cual. Es la evidencia; resumirla la anula.
        archivo.write_text(
            f"# `/{AGENTES[a.agente]}:{a.comando}` · día {a.dia}\n\n"
            f"Corrido el {date.today().isoformat()} · {a.segundos or '?'} s · "
            f"{a.documentos or '?'} documentos leídos · {a.hallazgos} hallazgos"
            + (f"\n\n**Lo que dijo que no sabía:** {a.no_supo}" if a.no_supo else
               "\n\n**No dijo en ningún momento que algo no estuviera dicho.** Sobre este "
               "material eso es señal de que rellenó huecos.")
            + "\n\n---\n\n" + origen.read_text(encoding="utf-8"),
            encoding="utf-8")

    filas = [f for f in leer()
             if not (f["comando"] == a.comando and f["dia"] == a.dia)]
    filas.append({"agente": a.agente, "comando": a.comando, "dia": a.dia,
                  "fecha": date.today().isoformat(), "segundos": a.segundos,
                  "documentos": a.documentos, "hallazgos": a.hallazgos,
                  "no_supo": a.no_supo,
                  "salida": str(archivo.relative_to(RAIZ)) if a.salida else None,
                  "nota": a.nota})
    filas.sort(key=lambda f: (f["dia"], f["agente"], f["comando"]))
    guardar(filas)
    print(f"día {a.dia} · /{AGENTES[a.agente]}:{a.comando} registrado"
          + (f" → {archivo.relative_to(RAIZ)}" if a.salida else " (sin salida guardada)"))
    return 0


def cobertura() -> int:
    filas = leer()
    corridos = {f["comando"] for f in filas}
    total = sin_evidencia = 0
    for agente, plugin in AGENTES.items():
        cmds = comandos_de(agente)
        total += len(cmds)
        faltan = [c for c in cmds if c not in corridos]
        sin_evidencia += len(faltan)
        print(f"\n{plugin} · {len(cmds) - len(faltan)} de {len(cmds)} con evidencia")
        for c in cmds:
            de_el = [f for f in filas if f["comando"] == c]
            if de_el:
                dias = ", ".join(f"d{f['dia']}" for f in de_el)
                t = [f["segundos"] for f in de_el if f["segundos"]]
                muda = sum(1 for f in de_el if not f["no_supo"])
                print(f"  ✓ {c:24} {dias:14} "
                      + (f"{min(t)}–{max(t)} s  " if t else "")
                      + (f"· {muda} corrida(s) sin decir que algo faltaba" if muda else ""))
            else:
                print(f"  — {c:24} sin evidencia · no se probó")
    print(f"\n{total - sin_evidencia} de {total} comandos con evidencia. "
          f"Los {sin_evidencia} sin entrada **no se probaron**.")
    return 0


def verificar() -> int:
    """Puerta: el registro no puede prometer una evidencia que no está."""
    filas, malas = leer(), []
    for f in filas:
        if f["comando"] not in comandos_de(f["agente"]):
            malas.append(f"{f['comando']} no es un comando de {AGENTES[f['agente']]}")
        if f["salida"] and not (RAIZ / f["salida"]).is_file():
            malas.append(f"{f['comando']} día {f['dia']} apunta a {f['salida']}, "
                         f"que no existe")
    total = sum(len(comandos_de(a)) for a in AGENTES)
    con = len({f["comando"] for f in filas})
    if malas:
        for m in malas:
            print(f"  FALLA {m}")
        print(f"\n{len(malas)} entradas del registro no se sostienen")
        return 1
    if not filas:
        print("  nota  ningún comando se ha corrido con un agente todavía · "
              f"0 de {total}")
    else:
        print(f"  OK    el registro se sostiene · {con} de {total} comandos con evidencia")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="accion", required=True)
    r = sub.add_parser("registrar")
    r.add_argument("--agente", required=True, choices=sorted(AGENTES))
    r.add_argument("--comando", required=True)
    r.add_argument("--dia", type=int, required=True)
    r.add_argument("--segundos", type=int)
    r.add_argument("--documentos", type=int)
    r.add_argument("--hallazgos", type=int, default=0)
    r.add_argument("--no-supo", dest="no_supo",
                   help="qué dijo que no estaba dicho en ninguna parte")
    r.add_argument("--nota")
    r.add_argument("--salida", help="archivo con lo que el comando imprimió")
    sub.add_parser("cobertura")
    sub.add_parser("verificar")
    a = ap.parse_args()
    raise SystemExit({"registrar": lambda: registrar(a), "cobertura": cobertura,
                      "verificar": verificar}[a.accion]())
