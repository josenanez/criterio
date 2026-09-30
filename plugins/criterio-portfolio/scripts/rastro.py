#!/usr/bin/env python3
"""Criterio — el rastro de cada corrida, escrito por el arnés y no por el modelo.

    hooks/hooks.json  →  python3 rastro.py enviar   (UserPromptSubmit)
                      →  python3 rastro.py parar    (Stop)
                      →  python3 rastro.py subagente-inicio (SubagentStart)
                      →  python3 rastro.py subagente-fin    (SubagentStop)
    python3 rastro.py --selftest

Todo lo que antes dependía de que el agente obedeciera la última instrucción de un
comando («registra la corrida») se saltaba cuando el agente no la obedecía, y un
comando que se salta el cierre deja la evidencia en una conversación que se cierra.
Esto no pasa por el modelo: Claude Code dispara `UserPromptSubmit` cuando la persona
invoca `/criterio-portfolio:health-check PRY-200` y `Stop` cuando el agente termina de
responder, y en los dos casos es este script el que escribe, con lo que el arnés le
entrega: el comando, el argumento, la hora, y el texto completo que el agente mostró.

Lo que queda, por corrida, en `<proyecto>/.criterio/corridas/<agente>/`:

    <fecha>-<comando>-<n>.md      el registro: comando, caso, horas, duración, salida
    <fecha>-<comando>-<n>.html    la misma corrida como página, abrible sin servidor
    corridas.json                 el índice que Rostrum lee para armar el árbol

Una corrida va desde que se invoca un comando hasta que se invoca el siguiente: si el
agente pregunta a mitad y la persona contesta, la respuesta se agrega a la misma
corrida y no abre otra. Las cifras que el comando haya medido con `corrida` (documentos,
señales, tiempo) se buscan en `corridas.json` de los estados por su hora de escritura y
se incrustan en la página, para que la evidencia y la aritmética estén en un solo sitio.

Los tres plugins llevan este archivo y su `hooks.json`. Cada hook actúa solo cuando el
comando es de su propio agente: en una sesión con los tres instalados los tres oyen la
misma invocación, y solo uno la registra.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import time
from pathlib import Path

AGENTE = {"criterio-portfolio": "portafolio", "criterio-project": "proyecto",
          "criterio-product": "producto"}
NOMBRE = {"portafolio": "Vera", "proyecto": "Samuel", "producto": "Alba"}
INVOCACION = re.compile(r"^\s*/(criterio-(?:portfolio|project|product)):([a-z0-9-]+)\s*(.*)$",
                        re.S)
CASO = re.compile(r"\b([A-Z]{2,5}-\d{2,})\b")
SALTAR = {".git", "node_modules", ".criterio", "__pycache__", ".next", ".venv"}


def agente_propio() -> str | None:
    raiz = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    if raiz and Path(raiz).name in AGENTE:
        return AGENTE[Path(raiz).name]
    # Sin la variable (en la prueba, o fuera de Claude Code) se acepta por argumento.
    for a in sys.argv[2:]:
        if a in AGENTE.values():
            return a
    return None


def raiz_de(d: dict) -> Path:
    return Path(d.get("cwd") or os.getcwd()) / ".criterio"


def leer_entrada() -> dict:
    try:
        return json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return {}


# ------------------------------------------------------------------ enviar

def enviar(d: dict, agente: str) -> int:
    """Al invocar un comando: deja la marca de que una corrida de este agente empezó."""
    texto = d.get("user_input") or d.get("prompt") or ""
    m = INVOCACION.match(texto)
    if not m or AGENTE.get(m.group(1)) != agente:
        return 0
    comando, args = m.group(2), m.group(3).strip()
    caso = CASO.search(args)
    marca = raiz_de(d) / "en-curso" / f"{d.get('session_id') or 'sesion'}.json"
    marca.parent.mkdir(parents=True, exist_ok=True)
    marca.write_text(json.dumps({
        "agente": agente, "comando": comando, "args": args,
        "caso": caso.group(1) if caso else None,
        "desde": time.time(), "inicio": dt.datetime.now().isoformat(timespec="seconds"),
        "id": None, "respuestas": 0,
    }, ensure_ascii=False), encoding="utf-8")
    return 0


# --------------------------------------------------------------- subagentes

def subagente(d: dict, agente: str, que: str) -> int:
    """Cada subagente que la corrida lanza queda contado, con su inicio y su fin, para
    saber cuántos corrieron a la vez. Es la medida que faltaba el día en que un barrido
    lanzó cinco lectores en paralelo y agotó la cuota: el rastro vio 223 segundos de
    turno principal y nada de lo que pasó debajo."""
    marca = raiz_de(d) / "en-curso" / f"{d.get('session_id') or 'sesion'}.json"
    if not marca.is_file():
        return 0
    try:
        m = json.loads(marca.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    if m.get("agente") != agente:
        return 0
    subs = m.setdefault("subagentes", [])
    ahora = time.time()
    if que == "inicio":
        subs.append({"inicio": ahora, "fin": None})
    else:
        abierto = next((s for s in subs if s.get("fin") is None), None)
        if abierto is None:                      # sin SubagentStart: se cuenta igual
            subs.append({"inicio": None, "fin": ahora})
        else:
            abierto["fin"] = ahora
    marca.write_text(json.dumps(m, ensure_ascii=False), encoding="utf-8")
    return 0


def concurrencia(subs: list) -> int:
    """Cuántos subagentes estuvieron vivos a la vez, como máximo."""
    eventos = []
    for s in subs:
        if s.get("inicio") is None:
            continue
        eventos.append((s["inicio"], 1))
        eventos.append((s.get("fin") or float("inf"), -1))
    vivos = tope = 0
    for _, delta in sorted(eventos):
        vivos += delta
        tope = max(tope, vivos)
    return tope


def workers_configurados(cwd: Path, agente: str, caso: str | None) -> int:
    """`execution.workers` de la configuración de este agente; 1 si no está."""
    base = cwd / ".criterio" / agente
    rutas = [base / caso / "config.json"] if caso else []
    rutas += [base / "config.json"] + sorted(base.glob("*/config.json"))
    for f in rutas:
        if f.is_file():
            try:
                w = (json.loads(f.read_text(encoding="utf-8")).get("execution") or {}).get("workers")
            except json.JSONDecodeError:
                continue
            if isinstance(w, int) and w >= 1:
                return w
            return 1
    return 1


# ------------------------------------------------------------------- parar

def ultimo_mensaje(transcript: str | None) -> str:
    """Lo que el agente mostró, sacado de la transcripción cuando el hook no lo trae."""
    if not transcript or not Path(transcript).is_file():
        return ""
    ultimo = ""
    for linea in Path(transcript).read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            fila = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if fila.get("type") != "assistant":
            continue
        contenido = (fila.get("message") or {}).get("content")
        if isinstance(contenido, str):
            ultimo = contenido
        elif isinstance(contenido, list):
            trozos = [c.get("text", "") for c in contenido
                      if isinstance(c, dict) and c.get("type") == "text"]
            if trozos:
                ultimo = "\n".join(trozos)
    return ultimo


ROL = {"pmo": "portafolio", "pm": "proyecto", "product": "producto"}


def tambien(comando: str) -> set:
    """Las otras corridas que un comando puede dejar, según el contrato de su plugin: un
    `wake` que hace el barrido deja la de `portfolio-scan`. Todo comando registra con su
    propio nombre —`tests/contratos.py` lo exige—, así que no hay nombres históricos que
    adivinar."""
    f = Path(__file__).resolve().parent.parent / "contratos.json"
    try:
        c = json.loads(f.read_text(encoding="utf-8"))["comandos"].get(comando) or {}
    except (OSError, json.JSONDecodeError, KeyError):
        return set()
    return set((c.get("corrida") or {}).get("tambien") or [])


def _agente_del_estado(estado: Path) -> str | None:
    """De quién es un estado, por el `role` de la configuración que lo acompaña."""
    for carpeta in (estado, estado.parent, estado.parent.parent):
        cfg = carpeta / "config.json"
        if cfg.is_file():
            try:
                return ROL.get(json.loads(cfg.read_text(encoding="utf-8")).get("role"))
            except (json.JSONDecodeError, OSError):
                return None
    return None


def cifras_medidas(cwd: Path, desde: float, comando: str, agente: str = "") -> list:
    """Las entradas que `corrida` escribió en algún estado durante esta corrida.

    Las tres consolas corren en la misma carpeta, así que la hora sola no basta: una
    entrada es de esta corrida si la escribió el estado de este agente —o uno sin dueño
    conocido— con el nombre de este comando o uno de sus nombres históricos.
    """
    salida = []
    for f in _corridas_json(cwd):
        dueno = _agente_del_estado(f.parent)
        if agente and dueno and dueno != agente:
            continue
        try:
            entradas = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for x in entradas:
            if (x.get("escrita") or 0) < desde - 1:
                continue
            if agente and x.get("que") not in ({comando} | tambien(comando)):
                continue
            salida.append(dict(x, _estado=str(f.parent)))
    return salida


def _corridas_json(cwd: Path, tope: int = 6):
    """Los `corridas.json` de los estados bajo el proyecto, sin bajar a lo que no es."""
    pila = [(cwd, 0)]
    while pila:
        carpeta, nivel = pila.pop()
        try:
            hijos = sorted(carpeta.iterdir())
        except OSError:
            continue
        for h in hijos:
            if h.is_dir():
                if h.name in SALTAR or nivel >= tope:
                    continue
                pila.append((h, nivel + 1))
            elif h.name == "corridas.json" and h.parent.name != "corridas":
                yield h


def _n(indice: list, fecha: str, comando: str) -> int:
    return 1 + sum(1 for x in indice if x.get("fecha") == fecha and x.get("comando") == comando)


def parar(d: dict, agente: str) -> int:
    """Al terminar el agente: la corrida en curso de este agente queda escrita."""
    marca = raiz_de(d) / "en-curso" / f"{d.get('session_id') or 'sesion'}.json"
    if not marca.is_file():
        return 0
    try:
        m = json.loads(marca.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    if m.get("agente") != agente:
        return 0

    texto = d.get("last_assistant_message") or ultimo_mensaje(d.get("transcript_path"))
    ahora = time.time()
    carpeta = raiz_de(d) / "corridas" / agente
    carpeta.mkdir(parents=True, exist_ok=True)
    f_indice = carpeta / "corridas.json"
    indice = json.loads(f_indice.read_text(encoding="utf-8")) if f_indice.exists() else []

    fecha = m["inicio"][:10]
    if not m.get("id"):
        m["id"] = f"{fecha}-{m['comando']}-{_n(indice, fecha, m['comando'])}"
        indice.append({"id": m["id"], "agente": agente, "comando": m["comando"],
                       "args": m["args"], "caso": m.get("caso"), "fecha": fecha,
                       "inicio": m["inicio"]})
    entrada = next(x for x in indice if x["id"] == m["id"])
    m["respuestas"] += 1
    entrada["fin"] = dt.datetime.now().isoformat(timespec="seconds")
    entrada["segundos"] = round(ahora - m["desde"])
    entrada["respuestas"] = m["respuestas"]
    medidas = cifras_medidas(Path(d.get("cwd") or os.getcwd()), m["desde"], m["comando"], agente)
    entrada["medidas"] = [{k: v for k, v in x.items() if k in
                           ("que", "fecha", "proyectos", "requerimientos", "documentos",
                            "segundos", "hallazgos", "por_senal", "relectura", "medido",
                            "nota", "id", "_estado")} for x in medidas]
    entrada["salida"] = bool(texto.strip())
    subs = m.get("subagentes") or []
    workers = workers_configurados(Path(d.get("cwd") or os.getcwd()), agente, m.get("caso"))
    entrada["subagentes"] = len(subs)
    entrada["concurrentes"] = concurrencia(subs)
    entrada["workers"] = workers
    # Con `workers: 1` la regla es «uno tras otro en esta conversación»: cualquier
    # subagente ya es exceso. Y sin `SubagentStart` la concurrencia no se puede medir: en
    # la segunda prueba llegaron seis `SubagentStop` sin su inicio, la cuenta dio 0 a la
    # vez y la corrida salió limpia. Lo que no se midió no se reporta como cero.
    sin_inicio = any(s.get("inicio") is None for s in subs)
    if sin_inicio:
        entrada["concurrentes"] = None
    entrada["exceso"] = bool(subs) and (workers == 1 or sin_inicio
                                        or entrada["concurrentes"] > workers)

    # El registro, y su página. Se reescriben enteros con cada respuesta: la corrida es
    # una sola aunque el agente haya preguntado a mitad.
    md = carpeta / f"{m['id']}.md"
    previo = md.read_text(encoding="utf-8") if md.exists() and m["respuestas"] > 1 else None
    if previo is None:
        lineas = [f"# Corrida · {m['id']}", "",
                  f"**Agente:** {NOMBRE[agente]} ({agente}) · **Comando:** `/{_plugin(agente)}:{m['comando']}"
                  + (f" {m['args']}" if m['args'] else "") + "`"
                  + (f" · **Caso:** {m['caso']}" if m.get("caso") else ""), "",
                  f"**Inicio:** {m['inicio']} · **Fin:** {entrada['fin']} · "
                  f"**Duración:** {entrada['segundos']} s", "", _linea_paralelo(entrada), ""]
        if medidas:
            lineas += ["## Cifras medidas por la corrida", "",
                       "| Qué | Casos | Documentos | Segundos | Hallazgos | Nota |",
                       "|---|---:|---:|---:|---:|---|"]
            for x in medidas:
                lineas.append(f"| `{x.get('que')}` | {x.get('proyectos') or x.get('requerimientos') or '—'} | "
                              f"{x.get('documentos') or '—'} | {x.get('segundos') or '—'} | "
                              f"{x.get('hallazgos') if x.get('hallazgos') is not None else '—'} | "
                              f"{(x.get('nota') or '').replace('|', '/')} |")
            for x in medidas:
                if x.get("por_senal"):
                    lineas += ["", f"Por señal (`{x.get('que')}`): "
                               + ", ".join(f"`{s}` {n}" for s, n in x["por_senal"].items())]
            lineas.append("")
        else:
            lineas += ["> Esta corrida no dejó cifras medidas por `corrida`: lo que hay es lo "
                       "que el agente mostró. Si el comando debía correr los scripts y no lo "
                       "hizo, eso es un hallazgo de la prueba.", ""]
        lineas += ["## Lo que el agente mostró", "", texto.strip() or "_(sin texto)_", ""]
    else:
        # Una respuesta más de la misma corrida: se actualizan las horas y se agrega.
        previo = re.sub(r"\*\*Subagentes:\*\* [^\n]*", _linea_paralelo(entrada), previo)
        lineas = re.sub(r"\*\*Fin:\*\* \S+ · \*\*Duración:\*\* \d+ s",
                        f"**Fin:** {entrada['fin']} · **Duración:** {entrada['segundos']} s",
                        previo).rstrip("\n").splitlines()
        lineas += ["", f"## Respuesta {m['respuestas']}", "", texto.strip() or "_(sin texto)_", ""]
    md.write_text("\n".join(lineas), encoding="utf-8")
    (carpeta / f"{m['id']}.html").write_text(
        _pagina(f"Corrida · {m['id']}", "\n".join(lineas), fecha), encoding="utf-8")

    f_indice.write_text(json.dumps(indice, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    marca.write_text(json.dumps(m, ensure_ascii=False), encoding="utf-8")
    return 0


def _linea_paralelo(entrada: dict) -> str:
    n, a_la_vez, w = entrada.get("subagentes") or 0, entrada.get("concurrentes"), entrada.get("workers")
    if a_la_vez is None:
        a_la_vez = "¿?"
    if not n:
        return f"**Subagentes:** ninguno · la configuración permite {w} a la vez"
    texto = f"**Subagentes:** {n}, hasta {a_la_vez} a la vez · la configuración permite {w}"
    if entrada.get("exceso"):
        texto += " · **EXCESO**: la corrida superó lo configurado"
    return texto


def _plugin(agente: str) -> str:
    return {v: k for k, v in AGENTE.items()}[agente]


def _pagina(titulo: str, md: str, hoy: str) -> str:
    """La página de la corrida es la misma para los tres agentes: la de `portafolio.py`."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import portafolio  # noqa: E402
    return portafolio.pagina_corrida(titulo, md, hoy)


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    import tempfile
    fallas = []

    def ok(que, real, esperado):
        if real == esperado:
            print(f"  ok   {que}")
        else:
            print(f" FALLA {que}: {real!r} != {esperado!r}")
            fallas.append(que)

    with tempfile.TemporaryDirectory() as tmp:
        cwd = Path(tmp)
        s = {"cwd": str(cwd), "session_id": "s1"}
        # 1. una invocación de otro agente no deja marca
        enviar(dict(s, user_input="/criterio-project:pm-wake"), "portafolio")
        ok("una invocación de otro agente no deja marca",
           (cwd / ".criterio" / "en-curso" / "s1.json").exists(), False)
        # 2. la propia sí, con el caso
        enviar(dict(s, user_input="/criterio-portfolio:health-check PRY-200 desde 2026-01"), "portafolio")
        m = json.loads((cwd / ".criterio" / "en-curso" / "s1.json").read_text())
        ok("la invocación propia deja la marca con comando y caso",
           (m["comando"], m["caso"]), ("health-check", "PRY-200"))
        # 3. cifras medidas durante la corrida se incrustan
        est = cwd / "org" / "estado"; est.mkdir(parents=True)
        (est / "corridas.json").write_text(json.dumps([
            {"que": "health-check", "fecha": "2026-09-30", "proyectos": 1, "hallazgos": 3,
             "por_senal": {"silent": 3}, "escrita": time.time()}]))
        (est / "corridas.json").parent.joinpath("records").mkdir()
        # 4. al parar, la corrida queda escrita con su página
        parar(dict(s, last_assistant_message="## Diagnóstico\n\nLa carpeta no permite saber el presupuesto."),
              "portafolio")
        carpeta = cwd / ".criterio" / "corridas" / "portafolio"
        hoy = dt.date.today().isoformat()
        ident = f"{hoy}-health-check-1"
        ok("la corrida queda con su markdown", (carpeta / f"{ident}.md").is_file(), True)
        ok("y con su HTML", (carpeta / f"{ident}.html").is_file(), True)
        pagina = (carpeta / f"{ident}.html").read_text(encoding="utf-8")
        ok("la página lleva lo que el agente mostró", "no permite saber el presupuesto" in pagina, True)
        ok("y las cifras medidas por la corrida", "silent" in pagina and "Cifras medidas" in pagina, True)
        indice = json.loads((carpeta / "corridas.json").read_text())
        ok("el índice tiene la corrida con su caso", (indice[0]["id"], indice[0]["caso"]), (ident, "PRY-200"))
        # 5. otro Stop sin nueva invocación se agrega a la misma corrida
        parar(dict(s, last_assistant_message="Confirmado: el patrocinador es X."), "portafolio")
        indice = json.loads((carpeta / "corridas.json").read_text())
        md = (carpeta / f"{ident}.md").read_text(encoding="utf-8")
        ok("una respuesta más no abre otra corrida", len(indice), 1)
        ok("y se agrega a la misma página", "Respuesta 2" in md and "patrocinador es X" in md, True)
        # 6. un Stop de otro agente no toca esta corrida
        parar(dict(s, last_assistant_message="soy Samuel"), "proyecto")
        ok("el Stop de otro agente no escribe", "soy Samuel" in (carpeta / f"{ident}.md").read_text(), False)
        # 7. la siguiente invocación abre otra corrida con su propio ordinal
        enviar(dict(s, user_input="/criterio-portfolio:health-check PRY-201"), "portafolio")
        parar(dict(s, last_assistant_message="segundo"), "portafolio")
        indice = json.loads((carpeta / "corridas.json").read_text())
        ok("la siguiente invocación es otra corrida, numerada",
           [x["id"] for x in indice], [ident, f"{hoy}-health-check-2"])
        # 8. sin `last_assistant_message`, se lee la transcripción
        tr = cwd / "t.jsonl"
        tr.write_text(json.dumps({"type": "user", "message": {"content": "hola"}}) + "\n"
                      + json.dumps({"type": "assistant", "message": {"content": [
                          {"type": "text", "text": "de la transcripción"}]}}) + "\n")
        enviar(dict(s, user_input="/criterio-portfolio:portfolio-wake"), "portafolio")
        parar(dict(s, transcript_path=str(tr)), "portafolio")
        ok("sin el mensaje en el hook, la salida sale de la transcripción",
           "de la transcripción" in (carpeta / f"{hoy}-portfolio-wake-1.md").read_text(), True)
        # 9. los subagentes quedan contados, y el exceso sobre `workers` marcado
        (cwd / ".criterio" / "portafolio").mkdir(parents=True, exist_ok=True)
        (cwd / ".criterio" / "portafolio" / "config.json").write_text(
            json.dumps({"execution": {"workers": 1}}), encoding="utf-8")
        enviar(dict(s, user_input="/criterio-portfolio:portfolio-scan"), "portafolio")
        subagente(s, "portafolio", "inicio"); subagente(s, "portafolio", "inicio")
        subagente(s, "portafolio", "fin"); subagente(s, "portafolio", "inicio")
        subagente(s, "portafolio", "fin"); subagente(s, "portafolio", "fin")
        subagente(s, "proyecto", "inicio")          # de otro agente: no cuenta
        parar(dict(s, last_assistant_message="barrido"), "portafolio")
        scan = json.loads((carpeta / "corridas.json").read_text())[-1]
        ok("la corrida cuenta sus subagentes y cuántos a la vez",
           (scan["subagentes"], scan["concurrentes"], scan["workers"], scan["exceso"]), (3, 2, 1, True))
        ok("dos a la vez con workers 1 es exceso", scan["exceso"], True)
        ok("y la concurrencia es cero sin subagentes", concurrencia([]), 0)
        enviar(dict(s, user_input="/criterio-portfolio:portfolio-setup"), "portafolio")
        subagente(s, "portafolio", "fin"); subagente(s, "portafolio", "fin")
        parar(dict(s, last_assistant_message="setup"), "portafolio")
        su = json.loads((carpeta / "corridas.json").read_text())[-1]
        ok("sin inicio registrado la concurrencia no se inventa, y es exceso",
           (su["subagentes"], su["concurrentes"], su["exceso"]), (2, None, True))
    print("\n" + ("todo pasa" if not fallas else f"{len(fallas)} falla(s)"))
    return 1 if fallas else 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2 or sys.argv[1] not in ("enviar", "parar", "subagente-inicio", "subagente-fin"):
        print(__doc__)
        return 2
    agente = agente_propio()
    if not agente:
        return 0
    d = leer_entrada()
    try:
        if sys.argv[1] == "enviar":
            return enviar(d, agente)
        if sys.argv[1] == "parar":
            return parar(d, agente)
        return subagente(d, agente, sys.argv[1].split("-")[1])
    except Exception as ex:  # el rastro nunca tumba la sesión; deja constancia y sigue
        try:
            (raiz_de(d) / "rastro-errores.log").parent.mkdir(parents=True, exist_ok=True)
            with open(raiz_de(d) / "rastro-errores.log", "a", encoding="utf-8") as f:
                f.write(f"{dt.datetime.now().isoformat(timespec='seconds')} {sys.argv[1]} {ex!r}\n")
        except OSError:
            pass
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
