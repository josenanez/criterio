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


def cosechar(a) -> int:
    """Lee las corridas que el agente registró y las trae al registro de pruebas.

    Es la diferencia entre medir y creer. Si estos números los teclea quien conduce la
    prueba desde lo que el agente imprimió, lo que se mide es su transcripción —el mismo
    defecto que este repositorio le encontró a un informe que reescribió una cifra ya
    calculada— y la prueba queda viciada. Así que no se teclean: salen de
    `<estado>/corridas.json`, que la corrida escribe sola.

    Lo único que sigue siendo del operador es lo cualitativo: qué dijo el agente que no
    sabía. Eso ningún script lo puede sacar, y va marcado como anotación.
    """
    estado = Path(a.estado).expanduser()
    f = estado / "corridas.json"
    if not f.is_file():
        sys.exit(f"no hay corridas registradas en {f}. El agente tiene que correr "
                 f"`portafolio.py corrida` al final de cada comando.")
    corridas = json.loads(f.read_text(encoding="utf-8"))

    # Cada tipo de corrida corresponde al comando que la produce, y cada agente tiene su
    # vocabulario. Un `--what` que no está aquí se ignora en vez de atribuirse al azar.
    DE = {
        "portfolio": {"sweep": "portfolio-scan", "report": "portfolio-report",
                      "confirmation": "portfolio-report",
                      "requests": "portfolio-wake"},
        "project": {"sweep": "pm-minutes", "report": "pm-report",
                    "confirmation": "pm-publish"},
        "product": {"review": "product-requirements", "report": "product-publish",
                    "crossed": "product-trace"},
    }[a.agente]
    filas, nuevas = leer(), 0
    for c in corridas:
        # Los comandos que registran con su propio nombre (`--what health-check`) no
        # necesitan traducción; los tres nombres históricos sí.
        comando = DE.get(c["que"], c["que"])
        if not comando or comando not in comandos_de(a.agente):
            continue
        clave = (comando, a.dia, c["fecha"], c["que"])
        if any((x["comando"], x["dia"], x.get("fecha"), x.get("que")) == clave
               for x in filas):
            continue
        filas.append({
            "agente": a.agente, "comando": comando, "dia": a.dia,
            "fecha": c["fecha"], "que": c["que"],
            "segundos": c.get("segundos"), "documentos": c.get("documentos"),
            "hallazgos": c.get("hallazgos"), "por_senal": c.get("por_senal"),
            "relectura": c.get("relectura"), "medido": c.get("medido"),
            "producto": c.get("producto"), "requerimientos": c.get("requerimientos"),
            "no_supo": None, "salida": None, "nota": c.get("nota"),
            "origen": "corrida del agente"})
        nuevas += 1
    filas.sort(key=lambda x: (x["dia"], x["agente"], x["comando"]))
    guardar(filas)
    sin_tiempo = [c for c in corridas if c.get("segundos") is None]
    print(f"{nuevas} corrida(s) cosechada(s) de {f}")
    if sin_tiempo:
        print(f"  {len(sin_tiempo)} sin tiempo medido · falta `corrida-inicio` al "
              f"arrancar el comando")
    return 0


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
                  "nota": a.nota,
                  # Marcado a propósito: lo que escribe una persona vale menos que lo que
                  # midió la corrida, y quien lea el registro tiene que poder distinguirlo.
                  "origen": "anotado a mano"})
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
                medidos = sum(1 for f in de_el if f.get("origen") == "corrida del agente")
                print(f"  ✓ {c:24} {dias:14} "
                      + (f"{min(t)}–{max(t)} s  " if t else "sin tiempo  ")
                      + (f"· {medidos}/{len(de_el)} medidas por la corrida "
                         if medidos < len(de_el) else "· medido ")
                      + (f"· {muda} sin decir que algo faltaba" if muda else ""))
            else:
                print(f"  — {c:24} sin evidencia · no se probó")
    print(f"\n{total - sin_evidencia} de {total} comandos con evidencia. "
          f"Los {sin_evidencia} sin entrada **no se probaron**.")
    return 0


def verificar() -> int:
    """Puerta: el registro no puede prometer una evidencia que no está.

    Y una cifra anotada a mano no cuenta como medida. Es la diferencia entre medir y
    creer: lo que teclea quien conduce la prueba mide su transcripción, no la corrida.
    Una anotación sola es legítima —lo cualitativo no sale de un script— pero no puede
    pasar por estadística.
    """
    filas, malas = leer(), []
    for f in filas:
        if f["comando"] not in comandos_de(f["agente"]):
            malas.append(f"{f['comando']} no es un comando de {AGENTES[f['agente']]}")
        if f["salida"] and not (RAIZ / f["salida"]).is_file():
            malas.append(f"{f['comando']} día {f['dia']} apunta a {f['salida']}, "
                         f"que no existe")
        # Sin `origen` es anterior a la cosecha, y por tanto tecleada. Un hueco que
        # absuelve en silencio es peor que ninguna puerta.
        if f.get("origen", "anotado a mano") != "corrida del agente" and (
                f.get("hallazgos") or 0):
            malas.append(f"{f['comando']} día {f['dia']} publica {f['hallazgos']} "
                         f"hallazgos anotados a mano · una cifra tecleada no es una "
                         f"medición: cosecha la corrida del agente")
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
    c = sub.add_parser("cosechar")
    c.add_argument("--agente", required=True, choices=sorted(AGENTES))
    c.add_argument("--estado", required=True, help="carpeta de estado del agente")
    c.add_argument("--dia", type=int, required=True)
    sub.add_parser("cobertura")
    sub.add_parser("verificar")
    a = ap.parse_args()
    raise SystemExit({"registrar": lambda: registrar(a), "cobertura": cobertura,
                      "cosechar": lambda: cosechar(a),
                      "verificar": verificar}[a.accion]())
