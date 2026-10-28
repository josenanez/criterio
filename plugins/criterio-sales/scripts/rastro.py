#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# COPIA. No se edita aquí.
#
# La fuente es plugins/criterio-portfolio/scripts/rastro.py. Este archivo lo escribe
# scripts/sincronizar.py, y tests/coherencia.py falla si las dos versiones se
# separan. Se copia en vez de importarse porque un plugin instalado tiene que
# correr solo: un import a la ruta del otro plugin funciona en el repositorio y
# falla en el equipo de quien lo instaló.
# ─────────────────────────────────────────────────────────────────────────────
"""Criterio — el rastro de cada corrida, escrito por el arnés y no por el modelo.

    hooks/hooks.json  →  python3 rastro.py enviar   (UserPromptSubmit)
                      →  python3 rastro.py parar    (Stop)
                      →  python3 rastro.py subagente-inicio (SubagentStart)
                      →  python3 rastro.py subagente-fin    (SubagentStop)
                      →  python3 rastro.py subagente-antes  (PreToolUse, Task|Agent)
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

Todos los plugins de agente llevan este archivo y su `hooks.json`, de las tres familias
(ADR 0010). Cada hook actúa solo cuando el comando es de su propio agente: en una sesión con
varios instalados todos oyen la misma invocación, y solo uno la registra.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import time
from pathlib import Path

# El área de cada agente es la carpeta de su configuración, `.criterio/<área>/`, y la de su
# rastro, `.criterio/corridas/<área>/`.
AGENTE = {"criterio-portfolio": "portafolio", "criterio-project": "proyecto",
          "criterio-product": "producto", "criterio-finance": "finanzas",
          "criterio-budget": "presupuesto", "criterio-treasury": "tesoreria", "criterio-legal": "legal",
          "criterio-compliance": "cumplimiento", "criterio-assistant": "direccion"}
NOMBRE = {"portafolio": "Vera", "proyecto": "Samuel", "producto": "Alba", "finanzas": "Clara",
          "presupuesto": "Tomás", "tesoreria": "Áurea", "legal": "Fidel", "cumplimiento": "Constanza",
          "direccion": "Ofelia"}
INVOCACION = re.compile(r"^\s*/(criterio-[a-z]+):([a-z0-9-]+)\s*(.*)$", re.S)
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


def antes_de_subagente(d: dict, agente: str) -> int:
    """PreToolUse sobre la herramienta de subagentes: con `workers: 1`, no se lanza.

    La regla estuvo escrita en el barrido, luego en los 37 comandos, y en tres corridas
    seguidas el agente lanzó subagentes igual. Una instrucción se salta; un hook que
    devuelve 2 no: Claude Code bloquea la llamada y le entrega el motivo al modelo.
    """
    marca = raiz_de(d) / "en-curso" / f"{d.get('session_id') or 'sesion'}.json"
    try:
        m = json.loads(marca.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0
    if m.get("agente") != agente:
        return 0
    workers = workers_configurados(Path(d.get("cwd") or os.getcwd()), agente, m.get("caso"))
    vivos = sum(1 for s in m.get("subagentes") or [] if s.get("inicio") and not s.get("fin"))
    if workers == 1 or vivos >= workers:
        sys.stderr.write(
            f"Criterio: la configuración permite {workers} a la vez (execution.workers) y "
            f"{'no se lanzan subagentes' if workers == 1 else f'ya hay {vivos} corriendo'}. "
            "Lee los documentos tú, uno tras otro, en esta conversación.\n")
        return 2
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


ROL = {"pmo": "portafolio", "pm": "proyecto", "product": "producto", "contralor": "finanzas",
       "fpa": "presupuesto", "juridico": "legal", "cumplimiento": "cumplimiento"}


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
            # Relativa a la carpeta de la sesión: el rastro se versiona y una ruta absoluta
            # publica el nombre de usuario y la estructura de carpetas de quien corrió.
            try:
                donde = str(f.parent.resolve().relative_to(cwd.resolve()))
            except ValueError:
                donde = f.parent.name
            salida.append(dict(x, _estado=donde))
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


# ------------------------------------------------------------ la corrida como página
# Cada corrida deja un HTML al lado de su markdown. Es la evidencia que se puede abrir sin
# servidor, mandar por correo o archivar; Rostrum sirve el mismo archivo con el árbol
# encima. Los colores son los del informe, declarados aquí porque los tres agentes
# comparten este módulo y solo Vera lleva `informe.py`. Vive aquí, y no en el motor de la PMO,
# porque todos los agentes llevan el arnés y no todos llevan ese motor.
_PALETA = {"crema": "#f5f4ef", "panel": "#efeee8", "tinta": "#111111", "cuerpo": "#3f4450",
           "apagado": "#6b675f", "oro": "#8a6327", "filete": "#c9c6bd"}


def _e(x) -> str:
    import html as _html
    return _html.escape(str(x), quote=True)


def md_a_html(md: str) -> str:
    """Markdown a HTML, lo justo para lo que una corrida escribe: títulos, párrafos,
    listas, tablas, citas y código. No es un procesador de Markdown y no pretende serlo."""
    out, parrafo, lista, tabla, codigo = [], [], None, [], False
    def cierra():
        nonlocal parrafo, lista, tabla
        if parrafo:
            out.append('<p>' + inl(' '.join(parrafo)) + '</p>'); parrafo = []
        if lista:
            out.append(f'</{lista}>'); lista = None
        if tabla:
            filas = [f for f in tabla if not set(f.replace('|', '').strip()) <= set('-: ')]
            if filas:
                celdas = lambda f: [c.strip() for c in f.strip().strip('|').split('|')]
                out.append('<table><thead><tr>' + ''.join(f'<th>{inl(c)}</th>' for c in celdas(filas[0]))
                           + '</tr></thead><tbody>'
                           + ''.join('<tr>' + ''.join(f'<td>{inl(c)}</td>' for c in celdas(f)) + '</tr>'
                                     for f in filas[1:]) + '</tbody></table>')
            tabla = []
    def inl(t):
        t = _e(t)
        # En el código, un nombre largo («einvoice_amount_mismatch», una ruta) se parte por sus
        # guiones bajos y sus barras, no a mitad de palabra.
        t = re.sub(r'`([^`]+)`', lambda m: '<code>' + re.sub(r'([_/])', r'\1<wbr>', m.group(1)) + '</code>', t)
        t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
        t = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', t)
        t = re.sub(r'(?<![\w<])_([^_<>]+)_(?![\w>])', r'<i>\1</i>', t)
        return t
    for linea in md.splitlines():
        if linea.startswith('```'):
            cierra()
            out.append('<pre>' if not codigo else '</pre>'); codigo = not codigo; continue
        if codigo:
            out.append(_e(linea)); continue
        l = linea.rstrip()
        if not l.strip():
            cierra(); continue
        if l.lstrip().startswith('|'):
            if parrafo or lista: cierra()
            tabla.append(l); continue
        m = re.match(r'^(#{1,6})\s+(.*)', l)
        if m:
            cierra(); n = min(len(m.group(1)) + 1, 6)
            out.append(f'<h{n}>{inl(m.group(2))}</h{n}>'); continue
        if l.startswith('>'):
            cierra(); out.append(f'<blockquote>{inl(l.lstrip("> "))}</blockquote>'); continue
        m = re.match(r'^\s*([-*]|\d+\.)\s+(.*)', l)
        if m:
            if parrafo or tabla: cierra()
            tipo = 'ol' if m.group(1)[0].isdigit() else 'ul'
            if lista != tipo:
                if lista: out.append(f'</{lista}>')
                out.append(f'<{tipo}>'); lista = tipo
            out.append(f'<li>{inl(m.group(2))}</li>'); continue
        if lista or tabla: cierra()
        parrafo.append(l.strip())
    cierra()
    if codigo: out.append('</pre>')
    return '\n'.join(out)



def pagina_corrida(titulo: str, md: str, hoy: str) -> str:
    """El HTML de una corrida, autocontenido, en la paleta del informe."""
    p = _PALETA
    css = (f"body{{margin:0;background:{p['crema']};color:{p['cuerpo']};font:16px/1.6 'Inter Tight','Inter',"
           f"-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}.hoja{{max-width:900px;margin:0 auto;padding:38px 24px}}"
           f".saltar{{position:absolute;left:12px;top:-60px;padding:10px 16px;background:{p['tinta']};color:{p['crema']};"
           f"border-radius:6px;font-weight:600;text-decoration:none}}.saltar:focus{{top:12px}}main:focus{{outline:none}}"
           f"a:focus-visible{{outline:3px solid {p['oro']};outline-offset:2px}}"
           f"h1,h2,h3{{color:{p['tinta']};letter-spacing:-.02em;line-height:1.15}}h1{{font-size:1.9rem}}"
           f"h2{{font-size:1.25rem;margin-top:2em}}.nav a{{color:{p['oro']};text-decoration:none}}"
           f"table{{border-collapse:collapse;width:100%;margin:1em 0;font-size:.95rem}}"
           f"th,td{{text-align:left;padding:.45em .6em;border-bottom:1px solid {p['filete']}}}"
           f"th{{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:{p['apagado']}}}"
           f"code{{background:{p['panel']};padding:.1em .35em;border-radius:3px;font-size:.9em;overflow-wrap:break-word}}"
           f"pre{{background:{p['panel']};padding:1em;overflow:auto}}"
           f"@media (max-width:640px){{table{{display:block;max-width:100%;overflow-x:auto}}}}"
           # La tabla que se desplaza por dentro no basta: en la ronda 6 una corrida de
           # product-setup seguía ensanchando la página a 616 px en un teléfono. El bloque
           # que la contiene se desplaza él mismo, y la página no pasa del ancho.
           f".bloque{{overflow-x:auto;max-width:100%}}"
           f"blockquote{{margin:1em 0;padding:.2em 1em;border-left:3px solid {p['oro']};color:{p['apagado']}}}"
           f".pie{{margin-top:3em;padding-top:1em;border-top:1px solid {p['filete']};font-size:.85rem;"
           f"color:{p['apagado']}}}")
    return (f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex,nofollow"><link rel="icon" href="data:,"><title>{_e(titulo)}</title>'
            f'<style>{css}</style></head><body><a class="saltar" href="#contenido">Saltar al contenido</a>'
            f'<div class="hoja"><main id="contenido" tabindex="-1">'
            f'<div class="nav"><a href="/corridas">← Historia de las corridas</a></div>'
            f'<h1>{_e(titulo)}</h1><div class="bloque">{md_a_html(md)}</div></main>'
            f'<footer class="pie">Esta corrida se escribió sola al terminar el comando, el {_e(hoy)}; '
            f'nada de esto se redactó después. Es la historia de lo que el agente procesó de los '
            f'documentos, no de lo que pasó ni un juicio sobre nadie.</footer></div></body></html>\n')


def _pagina(titulo: str, md: str, hoy: str) -> str:
    """La página de la corrida es la misma para todos los agentes."""
    return pagina_corrida(titulo, md, hoy)


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
        # 2b. los agentes de las otras familias también dejan su rastro, cada uno en su área
        s2 = {"cwd": str(cwd), "session_id": "s-clo"}
        enviar(dict(s2, user_input="/criterio-legal:obligations-calendar"), "legal")
        parar(dict(s2, last_assistant_message="CTR-101 vence en 45 días."), "legal")
        ok("un comando de Fidel queda en el rastro de su área",
           any((cwd / ".criterio" / "corridas" / "legal").glob("*-obligations-calendar-1.html")), True)
        enviar(dict(s2, user_input="/criterio-legal:obligations-calendar"), "finanzas")
        ok("y el hook de Clara no lo registra como suyo",
           (cwd / ".criterio" / "corridas" / "finanzas").exists(), False)
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
        ok("con workers 1 el hook bloquea el subagente", antes_de_subagente(s, "portafolio"), 2)
        ok("y el de otro agente no se mete", antes_de_subagente(s, "proyecto"), 0)
        ok("sin inicio registrado la concurrencia no se inventa, y es exceso",
           (su["subagentes"], su["concurrentes"], su["exceso"]), (2, None, True))
    print("\n" + ("todo pasa" if not fallas else f"{len(fallas)} falla(s)"))
    return 1 if fallas else 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    if len(sys.argv) < 2 or sys.argv[1] not in ("enviar", "parar", "subagente-inicio",
                                                   "subagente-fin", "subagente-antes"):
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
        if sys.argv[1] == "subagente-antes":
            return antes_de_subagente(d, agente)
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
