#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corre la verificación completa y dibuja lo que salió, por agente y en conjunto.

    python3 scripts/resultados.py             corre todo y escribe docs/pruebas.html
    python3 scripts/resultados.py --rapido    salta la regeneración del material
    python3 scripts/resultados.py --selftest  se verifica a sí mismo

Existe porque un número suelto en un README no se puede auditar y una tabla de doce
puertas no se lee. **Lo que sale de aquí es una corrida, no un dibujo:** cada cifra de la
página viene de ejecutar el mismo comando que corre `verificar.py`, contar las
comprobaciones que ese comando imprimió, y medir cuánto tardó.

Las puertas se importan de `verificar.py` a propósito. Si esta página tuviera su propia
lista, el día que alguien agregue una puerta la página seguiría diciendo que todo está
verificado con una puerta menos, **y ese es exactamente el defecto que este repositorio
no acepta.** Una puerta nueva sin dueño declarado aquí rompe la corrida.

SVG en línea y librería estándar. Una gráfica que necesita una librería de gráficas es
una gráfica que no se puede reproducir dentro de un año.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from verificar import PUERTAS  # noqa: E402

SALIDA = RAIZ / "docs" / "pruebas.html"
SALIDA_MD = RAIZ / "docs" / "pruebas.md"

# Quién responde por cada puerta. La clave es lo que identifica al comando; el orden
# importa, porque se busca la primera que aparezca en la línea de comando completa.
# Una puerta cuyo comando no case con ninguna de estas rompe la corrida, y así es como
# esta página se mantiene honesta cuando el repositorio crece.
DUENIOS = [
    ("criterio-pmo/scripts/servidor.py", "Rostrum"),
    ("criterio-pmo/scripts/informe.py", "Vera"),
    ("criterio-pmo/scripts/pmo.py", "Vera"),
    ("criterio-pmo/scripts/texto.py", "Vera"),
    ("tests/criterio-pmo/", "Vera"),
    ("criterio-pm/scripts/", "Samuel"),
    ("tests/criterio-pm/", "Samuel"),
    ("criterio-product/scripts/", "Alba"),
    ("tests/criterio-product/", "Alba"),
    ("tests/sintetico/", "La familia"),
    ("tests/coherencia.py", "La familia"),
    ("scripts/validate_plugins.py", "La familia"),
    ("scripts/sincronizar.py", "La familia"),
    ("scripts/resultados.py", "La familia"),
]

QUIEN = {
    "Vera": ("Agente PMO", "Del latín <i>verus</i>: lo verdadero. Dice lo que los "
                           "documentos dicen, no lo que se reporta"),
    "Samuel": ("Agente de proyecto", "«El que escuchó». Su función central es el "
                                     "compromiso dicho y no cumplido"),
    "Alba": ("Agente de producto", "El amanecer: la luz que hay antes de que se vea "
                                   "nada. Trabaja antes de que exista el proyecto"),
    "Rostrum": ("El servidor", "Una tribuna. Sostiene lo que ya está escrito, donde el "
                               "equipo puede leerlo. No decide nada, y por eso no lleva "
                               "nombre de persona"),
    "La familia": ("Lo que los tres comparten", "Que la documentación y el código digan "
                                                "lo mismo, que el marketplace esté "
                                                "completo, que las copias compartidas no "
                                                "se hayan separado, y que el recorrido "
                                                "encuentre los documentos sin importar "
                                                "cómo estén organizados"),
}

ORDEN = ["Vera", "Samuel", "Alba", "Rostrum", "La familia"]

# Cómo cuenta cada script sus comprobaciones. Los selftests imprimen «ok» en minúscula y
# los calificadores «OK» en mayúscula, con sangrías distintas. Se cuentan las dos formas
# y nada más: contar cualquier línea que contenga «ok» sumaría las que dicen «ok» dentro
# de una frase, y esta página se llenaría de comprobaciones que nadie hizo.
RE_CHECK = re.compile(r"^\s+(ok|OK)\s", re.M)
RE_FALLA = re.compile(r"^\s+(FALLA|ROJO)", re.M)

CREMA, PANEL, PANEL_ALTO = '#f5f4ef', '#efeee8', '#f8f7f3'
TINTA, CUERPO, APAGADO = '#111111', '#3f4450', '#6b675f'
ORO, FILETE, FILETE_SUAVE = '#8a6327', '#c9c6bd', '#d8d5cd'
OK_, OK_FONDO = '#3f6b4a', '#e7eee7'
ERROR, ERROR_FONDO, ERROR_FILETE = '#8f3a2c', '#f3e7e3', '#ddc2ba'
INFO, INFO_FONDO, INFO_FILETE = '#3d5d75', '#e6edf3', '#cfdae3'


def duenio(cmd: list) -> str:
    linea = " ".join(str(x) for x in cmd).replace("\\", "/")
    for marca, quien in DUENIOS:
        if marca in linea:
            return quien
    raise SystemExit(
        f"puerta sin dueño declarado en scripts/resultados.py: {linea}\n"
        "Agrégala a DUENIOS. La página no se dibuja con una puerta que nadie reclama.")


def etiqueta(cmd: list) -> str:
    """El nombre corto de la puerta. Los tres plugins tienen su carpeta `scripts/`, así
    que `scripts/pmo.py` no distingue la copia de Samuel de la fuente de Vera: cuando el
    padre es `scripts`, manda el nombre del plugin."""
    p = Path(cmd[1])
    carpeta = p.parent.name
    if carpeta == "scripts" and p.parent.parent.name.startswith("criterio-"):
        carpeta = p.parent.parent.name
    nombre = f"{carpeta}/{p.name}"
    if len(cmd) > 2 and not str(cmd[2]).startswith("-"):
        nombre += f" {cmd[2]}"
    return nombre


def correr(rapido: bool) -> list:
    filas = []
    for grupo, cmd, porque in PUERTAS:
        if rapido and grupo == "material":
            continue
        t0 = time.time()
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=RAIZ)
        ms = int((time.time() - t0) * 1000)
        salida = r.stdout + r.stderr
        filas.append({
            "grupo": grupo, "cmd": cmd, "porque": porque,
            "quien": duenio(cmd), "etiqueta": etiqueta(cmd),
            "ok": r.returncode == 0, "ms": ms,
            "checks": len(RE_CHECK.findall(salida)),
            "fallas": len(RE_FALLA.findall(salida)),
        })
        print(f"  {'verde' if r.returncode == 0 else 'ROJO '}  "
              f"{filas[-1]['etiqueta']:44} {filas[-1]['checks']:>4} comprobaciones")
    return filas


# ------------------------------------------------------------------ dibujo

def e(t) -> str:
    return html.escape(str(t if t is not None else ""))


def barras(datos: list, ancho=680, alto_fila=34) -> str:
    """Barras horizontales en SVG. Horizontales porque las etiquetas son nombres y un
    nombre girado noventa grados no se lee."""
    if not datos:
        return ""
    tope = max(v for _, v, _ in datos) or 1
    izq, alto = 150, alto_fila * len(datos) + 12
    piezas = [f'<svg viewBox="0 0 {ancho} {alto}" width="100%" height="{alto}" '
              f'role="img" aria-label="comprobaciones por agente">']
    for i, (nombre, valor, color) in enumerate(datos):
        y = i * alto_fila + 6
        largo = int((ancho - izq - 60) * valor / tope)
        piezas.append(
            f'<text x="{izq - 12}" y="{y + 15}" text-anchor="end" font-size="13" '
            f'fill="{CUERPO}" font-weight="600">{e(nombre)}</text>'
            f'<rect x="{izq}" y="{y + 2}" width="{max(largo, 2)}" height="18" rx="3" '
            f'fill="{color}"/>'
            f'<text x="{izq + max(largo, 2) + 8}" y="{y + 16}" font-size="13" '
            f'fill="{APAGADO}">{valor}</text>')
    piezas.append("</svg>")
    return "".join(piezas)


def anillo(verdes: int, rojas: int, lado=132) -> str:
    """Las puertas en verde sobre el total. Un anillo y no una torta: lo que importa es
    la fracción, y una torta de dos porciones donde una es cero es un círculo."""
    total = verdes + rojas
    r, c = lado / 2 - 12, lado / 2
    largo = 2 * 3.14159 * r
    hecho = largo * (verdes / total if total else 0)
    return (f'<svg viewBox="0 0 {lado} {lado}" width="{lado}" height="{lado}" role="img" '
            f'aria-label="{verdes} de {total} puertas en verde">'
            f'<circle cx="{c}" cy="{c}" r="{r:.1f}" fill="none" stroke="{FILETE_SUAVE}" '
            f'stroke-width="10"/>'
            f'<circle cx="{c}" cy="{c}" r="{r:.1f}" fill="none" '
            f'stroke="{OK_ if not rojas else ERROR}" stroke-width="10" '
            f'stroke-dasharray="{hecho:.1f} {largo:.1f}" stroke-linecap="round" '
            f'transform="rotate(-90 {c} {c})"/>'
            f'<text x="{c}" y="{c - 2}" text-anchor="middle" font-size="26" '
            f'font-weight="600" fill="{TINTA}">{verdes}</text>'
            f'<text x="{c}" y="{c + 16}" text-anchor="middle" font-size="11" '
            f'fill="{APAGADO}">de {total} puertas</text></svg>')


CSS = f"""
*{{box-sizing:border-box}}
body{{margin:0;background:{CREMA};color:{CUERPO};
  font:400 16px/1.55 'Inter Tight','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.hoja{{max-width:960px;margin:0 auto;padding:56px 24px 96px}}
h1{{font-size:2.3rem;line-height:1.14;color:{TINTA};font-weight:500;margin:.2em 0 .1em;
  letter-spacing:-.01em}}
h2{{font-size:1.35rem;color:{TINTA};font-weight:500;margin:2.6em 0 .8em;
  padding-bottom:.4em;border-bottom:1px solid {FILETE}}}
h3{{font-size:1.05rem;color:{TINTA};font-weight:600;margin:0 0 .2em}}
.ante{{font-size:.78rem;letter-spacing:.17em;text-transform:uppercase;color:{ORO};
  font-weight:600}}
.entrada{{color:{APAGADO};margin:.6em 0 0;max-width:62ch}}
.tope{{display:flex;flex-wrap:wrap;gap:26px;align-items:center;margin:30px 0 0;
  background:{PANEL_ALTO};border:1px solid {FILETE};border-radius:10px;padding:22px 26px}}
.cifras{{display:flex;flex-wrap:wrap;gap:14px;flex:1 1 380px}}
.cifra{{flex:1 1 120px;background:{CREMA};border:1px solid {FILETE};border-radius:8px;
  padding:14px 16px}}
.cifra .n{{font-size:1.75rem;color:{TINTA};font-weight:600;line-height:1}}
.cifra .q{{font-size:.8rem;color:{APAGADO};margin-top:5px;display:block}}
.agente{{border:1px solid {FILETE};border-radius:10px;padding:22px 24px;margin:18px 0;
  background:{PANEL_ALTO}}}
.agente .rol{{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;
  color:{ORO};font-weight:600}}
.agente .que{{color:{APAGADO};font-size:.92rem;margin:.3em 0 1em;max-width:70ch}}
table{{width:100%;border-collapse:collapse;font-size:.93rem}}
th{{text-align:left;font-weight:600;color:{APAGADO};font-size:.74rem;letter-spacing:.08em;
  text-transform:uppercase;padding:8px 10px;border-bottom:1px solid {FILETE}}}
td{{padding:9px 10px;border-bottom:1px solid {FILETE_SUAVE};vertical-align:top}}
tr:last-child td{{border-bottom:none}}
td.n{{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}}
td .porque{{display:block;font-size:.83rem;color:{APAGADO};margin-top:2px}}
.sem{{display:inline-block;padding:2px 9px;border-radius:4px;font-size:.76rem;
  font-weight:600;border:1px solid}}
.verde{{color:{OK_};background:{OK_FONDO};border-color:{OK_}}}
.rojo{{color:{ERROR};background:{ERROR_FONDO};border-color:{ERROR}}}
.bloque{{border:1px solid {INFO_FILETE};border-left:3px solid {INFO};background:{INFO_FONDO};
  border-radius:0 8px 8px 0;padding:18px 22px;margin:22px 0}}
.bloque h3{{margin-bottom:.4em}}
.bloque ul{{margin:.4em 0 0;padding-left:1.2em}}
.bloque li{{margin:.4em 0}}
.pie{{margin-top:56px;padding-top:18px;border-top:1px solid {FILETE};color:{APAGADO};
  font-size:.85rem}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.88em;
  background:{PANEL};padding:1px 5px;border-radius:3px}}
@media print{{
  body{{background:#fff}} .hoja{{max-width:none;padding:0}}
  h2{{page-break-after:avoid}} .agente,tr{{page-break-inside:avoid}}
}}
"""

NO_PROBADO = [
    ("La extracción nunca se ha corrido",
     "Los tres corpus siembran el estado desde sus respuestas de referencia, así que la "
     "cadena documento → modelo → ficha no se ha ejercitado. <code>grade.py --fichas</code> "
     "y <code>grade.py --registros</code> existen para eso y no se han ejecutado."),
    ("Ningún comando se ha corrido con un agente de verdad",
     "Los {comandos} comandos están verificados como estructura —existen, declaran, y no "
     "invocan un skill que no esté—, y eso no es lo mismo que haberlos ejercitado."),
    ("Nada se ha corrido sobre la documentación real de una organización",
     "Todo el material es sintético y construido desde cero. Es la diferencia que protege "
     "a quien instale esto: <b>construido y verificado sobre corpus, no probado sobre "
     "documentación real.</b>"),
    ("Lo que produce el modelo no lo mide un calificador determinista",
     "Convertir ocho entrevistas en temas con sus citas, redactar un acta o un informe es "
     "trabajo del modelo. Lo que se verifica aquí es la aritmética de la que salen sus "
     "cifras, y la estructura de lo que se le pide."),
]


def estado_git() -> tuple:
    """El commit sobre el que se corrió, y si el árbol tenía cambios sin confirmar.

    Sin lo segundo, el archivo dice «sobre el commit X» y alguien va a creer que eso es
    lo que hay en X. Casi siempre no lo es: se corre antes de confirmar, que es
    precisamente cuando sirve correr.
    """
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=RAIZ,
                            capture_output=True, text=True).stdout.strip() or "—"
    sucio = bool(subprocess.run(["git", "status", "--porcelain"], cwd=RAIZ,
                                capture_output=True, text=True).stdout.strip())
    return commit, sucio


def pagina(filas: list, rapido: bool) -> str:
    verdes = sum(1 for f in filas if f["ok"])
    rojas = len(filas) - verdes
    checks = sum(f["checks"] for f in filas)
    ms = sum(f["ms"] for f in filas)
    hoy = dt.date.today().isoformat()
    commit, sucio = estado_git()

    # Los dos números que la página afirma sobre el repositorio y no sobre la corrida:
    # se cuentan del disco, no se escriben a mano. Un «treinta comandos» escrito aquí
    # envejece en el primer comando que alguien agregue.
    corpus = sum(1 for g, _, _ in PUERTAS if g == "material")
    comandos = len(list((RAIZ / "plugins").glob("*/commands/*.md")))

    por_quien = {q: [f for f in filas if f["quien"] == q] for q in ORDEN}
    datos = [(q, sum(f["checks"] for f in por_quien[q]),
              ORO if q == "La familia" else OK_)
             for q in ORDEN if por_quien.get(q)]

    p = [f'<!doctype html><html lang="es"><head><meta charset="utf-8">',
         f'<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>Criterio · resultados de las pruebas</title>',
         f'<style>{CSS}</style></head><body><div class="hoja">',
         f'<p class="ante">Criterio · verificación</p>',
         f'<h1>Qué se probó, y qué no</h1>',
         f'<p class="entrada">Esta página sale de una corrida, no de un resumen escrito a '
         f'mano. Cada cifra viene de ejecutar el mismo comando que corre '
         f'<code>scripts/verificar.py</code> y contar las comprobaciones que ese comando '
         f'imprimió. Con la librería estándar y sin instalar nada.</p>',
         '<div class="tope">', anillo(verdes, rojas), '<div class="cifras">',
         f'<div class="cifra"><span class="n">{checks}</span>'
         f'<span class="q">comprobaciones</span></div>',
         f'<div class="cifra"><span class="n">{corpus}</span>'
         f'<span class="q">corpus, cada uno con su control negativo</span></div>',
         f'<div class="cifra"><span class="n">{ms / 1000:.1f} s</span>'
         f'<span class="q">la corrida entera</span></div>',
         '</div></div>',
         '<h2>En conjunto</h2>',
         '<p class="entrada">Comprobaciones por dueño. Los tamaños no son comparables '
         'entre sí y no pretenden serlo: Vera tiene diecisiete comandos y Rostrum es un '
         'servidor de ochocientas líneas. Lo que dice esta gráfica es dónde está puesta '
         'la verificación.</p>',
         barras(datos)]

    for q in ORDEN:
        grupo = por_quien.get(q)
        if not grupo:
            continue
        rol, que = QUIEN[q]
        p.append(f'<div class="agente"><p class="rol">{e(rol)}</p><h3>{e(q)}</h3>'
                 f'<p class="que">{que}</p>'
                 f'<table><thead><tr><th>Puerta</th><th>Qué prueba</th>'
                 f'<th class="n">Comprob.</th><th class="n">Tiempo</th>'
                 f'<th></th></tr></thead><tbody>')
        for f in grupo:
            marca = ('<span class="sem verde">verde</span>' if f["ok"]
                     else f'<span class="sem rojo">{f["fallas"]} en rojo</span>')
            p.append(f'<tr><td><code>{e(f["etiqueta"])}</code></td>'
                     f'<td>{e(f["porque"])}</td>'
                     f'<td class="n">{f["checks"] or "—"}</td>'
                     f'<td class="n">{f["ms"]} ms</td><td>{marca}</td></tr>')
        p.append('</tbody></table></div>')

    p.append('<h2>Lo que esta corrida no cubre</h2>')
    p.append('<p class="entrada">Va aquí y no en un anexo. Una página de resultados que '
             'solo dice lo que pasó es publicidad; lo que la vuelve auditable es lo que '
             'dice que todavía no se sabe.</p>')
    p.append('<div class="bloque"><ul>')
    for titulo, detalle in NO_PROBADO:
        p.append(f'<li><b>{e(titulo)}.</b> {detalle.format(comandos=comandos)}</li>')
    p.append('</ul></div>')

    p.append(f'<div class="pie"><p>Corrida del {hoy} · commit <code>{e(commit)}</code>'
             f'{" · con cambios sin confirmar" if sucio else ""} · '
             f'{"sin regenerar el material sintético" if rapido else "material sintético regenerado en esta corrida"}.</p>'
             f'<p>Reproducirlo: <code>python3 scripts/resultados.py</code>. El detalle de '
             f'qué prueba cada corpus y qué no, en las tres páginas de evidencia bajo '
             f'<code>tests/</code>.</p></div>')
    p.append('</div></body></html>')
    return "".join(p)


# ─────────────────────────────────────────────────────────────────────────────
# El resultado por agente
#
# La página combinada sirve para mirar el conjunto. Pero el que instala `criterio-pm`
# no instala el conjunto: instala un agente, y lo que necesita saber es qué se probó de
# **ese**. Por eso además de la página hay un archivo por agente, en markdown, dentro de
# su carpeta de pruebas — markdown porque se lee en GitHub sin descargar nada.

PLUGIN_DE = {
    "Vera": "criterio-pmo",
    "Rostrum": "criterio-pmo",
    "Samuel": "criterio-pm",
    "Alba": "criterio-product",
}

# Qué no cubre la corrida de cada agente. Va en el mismo archivo que los resultados y no
# en un anexo: un resultado de pruebas que solo dice lo que pasó es publicidad.
NO_CUBRE = {
    "criterio-pmo": [
        ("La extracción nunca se ha corrido",
         "El estado se siembra copiando `expected/fichas/`, así que la cadena documento "
         "→ modelo → ficha no se ha ejercitado. `grade.py --fichas` existe para eso."),
        ("Los diecisiete comandos no se han corrido con un agente de verdad",
         "Están verificados como estructura —existen, declaran, y no invocan un skill "
         "que no esté—, y eso no es lo mismo que haberlos ejercitado."),
        ("Nada se ha corrido sobre la documentación real de una organización",
         "Todo el material es sintético y construido desde cero."),
    ],
    "criterio-pm": [
        ("La extracción nunca se ha corrido",
         "El corpus siembra las fichas, así que la cadena documento → modelo → ficha no "
         "se ha ejercitado. `grade.py --fichas` existe para eso."),
        ("La agenda, el acta y el informe no se califican con esto",
         "Lo que producen es redacción sobre la minuta, y un calificador determinista no "
         "la mide. Lo que sí se verifica es la aritmética de la que salen sus cifras."),
        ("La ficha publicada y su contraste no se han corrido de punta a punta",
         "`/pm-publish` escribe y `contrastar()` emite la señal con sus dos citas, "
         "verificado sobre fichas sintéticas. Falta que un agente de verdad publique y "
         "otro de verdad lea."),
    ],
    "criterio-product": [
        ("La extracción nunca se ha corrido",
         "El corpus siembra los registros, así que la cadena documento → modelo → "
         "registro no se ha ejercitado. `grade.py --registros` existe para eso."),
        ("La síntesis de descubrimiento no se puede calificar con esto",
         "Convertir ocho entrevistas en temas con sus citas es trabajo del modelo. Las "
         "entrevistas del corpus llevan el conteo explícito —«6 de 8»— para que el día "
         "que se califique haya contra qué."),
        ("El barrido normativo no se prueba en ninguna parte",
         "Su salida depende de conocimiento externo al repositorio, y su regla dura —*no "
         "dice si cumple*— no se puede verificar con una aserción."),
    ],
}

QUE_ES = {
    "criterio-pmo": ("Vera y Rostrum", "el agente de la PMO y el servidor que publica su informe"),
    "criterio-pm": ("Samuel", "el agente del gerente de proyecto"),
    "criterio-product": ("Alba", "el agente del gerente de producto"),
}


def por_agente(filas: list, rapido: bool) -> list:
    """Escribe un RESULTADOS.md por agente y devuelve las rutas."""
    hoy = dt.date.today().isoformat()
    commit, sucio = estado_git()
    familia = [f for f in filas if f["quien"] == "La familia"]
    escritos = []

    for plugin, (nombre, que) in QUE_ES.items():
        suyas = [f for f in filas if PLUGIN_DE.get(f["quien"]) == plugin]
        if not suyas:
            continue
        checks = sum(f["checks"] for f in suyas)
        rojas = [f for f in suyas if not f["ok"]]
        destino = RAIZ / "tests" / plugin / "RESULTADOS.md"

        p = [f"# Resultado de las pruebas · {nombre}", "",
             f"**{que}** · plugin `{plugin}`", "",
             f"Corrida del {hoy}, sobre el commit `{commit}`"
             f"{', con cambios en el árbol todavía sin confirmar' if sucio else ''}"
             f"{' (sin regenerar el material sintético)' if rapido else ''}. "
             f"**{len(suyas)} puertas · {checks} comprobaciones · "
             f"{'todas en verde' if not rojas else f'{len(rojas)} en rojo'}.**", "",
             "> Este archivo lo escribe `python3 scripts/resultados.py` desde una corrida "
             "real. No se edita a mano: la corrida siguiente lo reemplaza.", "",
             "## Lo que se corrió", "",
             "| Puerta | Qué prueba | Comprob. | Tiempo | |",
             "|---|---|---:|---:|---|"]
        for f in suyas:
            marca = "verde" if f["ok"] else f"**{f['fallas']} EN ROJO**"
            p.append(f"| `{f['etiqueta']}` | {f['porque']} | {f['checks'] or '—'} | "
                     f"{f['ms']} ms | {marca} |")

        p += ["", "Una puerta sin comprobaciones no es una puerta vacía: **genera el "
              "material sintético** o verifica una estructura completa, y falla entera "
              "si algo no está.", "",
              "## Lo que esta corrida no cubre", "",
              "Va aquí y no en un anexo. Un resultado de pruebas que solo dice lo que "
              "pasó es publicidad; lo que lo vuelve auditable es lo que dice que todavía "
              "no se sabe.", ""]
        for titulo, detalle in NO_CUBRE.get(plugin, []):
            p.append(f"- **{titulo}.** {detalle}")

        p += ["", "## Qué material se usó, y qué prueba cada pieza", "",
              f"El detalle del corpus —qué planta cada proyecto o producto, por qué, y "
              f"cuál es su control negativo— está en "
              f"[`EVIDENCIA.md`](EVIDENCIA.md), que se escribe a mano y no se genera.", "",
              "**El control negativo es la mitad del valor de estas pruebas.** Un agente "
              "que encuentra hallazgos donde no los hay es un generador de ruido, y eso "
              "no se detecta mirando solo los casos que sí fallan.", "",
              "## Y lo que se verifica para toda la familia", "",
              "| Puerta | Qué prueba | Comprob. | |", "|---|---|---:|---|"]
        for f in familia:
            marca = "verde" if f["ok"] else f"**{f['fallas']} EN ROJO**"
            p.append(f"| `{f['etiqueta']}` | {f['porque']} | {f['checks'] or '—'} | "
                     f"{marca} |")
        p += ["", "El conjunto de los tres agentes, en "
              "[`docs/pruebas.md`](../../docs/pruebas.md) — y con gráficas, para abrir en "
              "un navegador, en [`pruebas.html`](../../docs/pruebas.html). Todo corre con "
              "la librería estándar y sin instalar nada.", ""]

        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text("\n".join(p), encoding="utf-8")
        escritos.append(destino)
    return escritos


# ─────────────────────────────────────────────────────────────────────────────
# El conjunto, en markdown
#
# La página con gráficas es HTML, y GitHub no la muestra: la sirve como código fuente.
# Quien llega al repositorio desde un enlace no va a clonar nada para ver cómo salió una
# corrida, así que el mismo contenido va también en markdown. La gráfica de barras se
# dibuja con el carácter de bloque, que es lo único que un markdown puede dibujar sin
# depender de nada.

BLOQUE = "█"


def barra_texto(valor: int, tope: int, ancho: int = 28) -> str:
    return BLOQUE * max(1, round(ancho * valor / tope)) if tope else ""


def pagina_md(filas: list, rapido: bool) -> str:
    hoy = dt.date.today().isoformat()
    commit, sucio = estado_git()
    verdes = sum(1 for f in filas if f["ok"])
    rojas = len(filas) - verdes
    checks = sum(f["checks"] for f in filas)
    ms = sum(f["ms"] for f in filas)
    corpus = sum(1 for g, _, _ in PUERTAS if g == "material")
    comandos = len(list((RAIZ / "plugins").glob("*/commands/*.md")))

    por_quien = {q: [f for f in filas if f["quien"] == q] for q in ORDEN}
    datos = [(q, sum(f["checks"] for f in por_quien[q]))
             for q in ORDEN if por_quien.get(q)]
    tope = max((v for _, v in datos), default=1)

    p = ["# Qué se probó, y qué no", "",
         "Esta página sale de una corrida, no de un resumen escrito a mano. Cada cifra viene "
         "de ejecutar el mismo comando que corre `scripts/verificar.py` y contar las "
         "comprobaciones que ese comando imprimió. Con la librería estándar y sin instalar "
         "nada.", "",
         f"Corrida del {hoy}, sobre el commit `{commit}`"
         f"{', con cambios en el árbol todavía sin confirmar' if sucio else ''}"
         f"{' (sin regenerar el material sintético)' if rapido else ''}.", "",
         f"**{verdes} de {len(filas)} puertas en verde · {checks} comprobaciones · "
         f"{corpus} corpus, cada uno con su control negativo · {ms / 1000:.1f} s la corrida "
         f"entera.**", "",
         "> La versión con gráficas, para abrir en un navegador, está en "
         "[`pruebas.html`](pruebas.html). Esta es la misma corrida, legible en GitHub.", "",
         "## En conjunto", "",
         "Comprobaciones por dueño. Los tamaños no son comparables entre sí y no pretenden "
         "serlo: lo que dice esta gráfica es dónde está puesta la verificación.", "",
         "| Dueño | | Comprob. |", "|---|---|---:|"]
    for quien, valor in datos:
        p.append(f"| **{quien}** | `{barra_texto(valor, tope)}` | {valor} |")

    for quien in ORDEN:
        grupo = por_quien.get(quien)
        if not grupo:
            continue
        rol, que = QUIEN[quien]
        p += ["", f"## {quien} · {rol}", "", f"{que.replace('<i>', '*').replace('</i>', '*')}.",
              "", "| Puerta | Qué prueba | Comprob. | Tiempo | |",
              "|---|---|---:|---:|---|"]
        for f in grupo:
            marca = "verde" if f["ok"] else f"**{f['fallas']} EN ROJO**"
            p.append(f"| `{f['etiqueta']}` | {f['porque']} | {f['checks'] or '—'} | "
                     f"{f['ms']} ms | {marca} |")
        plugin = PLUGIN_DE.get(quien)
        if plugin:
            p += ["", f"Su análisis propio, con qué material se usó y qué no cubre, en "
                      f"[`tests/{plugin}/RESULTADOS.md`](../tests/{plugin}/RESULTADOS.md)."]

    p += ["", "## Lo que esta corrida no cubre", "",
          "Va aquí y no en un anexo. Una página de resultados que solo dice lo que pasó es "
          "publicidad; lo que la vuelve auditable es lo que dice que todavía no se sabe.", ""]
    for titulo, detalle in NO_PROBADO:
        limpio = (detalle.format(comandos=comandos)
                  .replace("<code>", "`").replace("</code>", "`")
                  .replace("<b>", "**").replace("</b>", "**"))
        p.append(f"- **{titulo}.** {limpio}")

    p += ["", "---", "", "Reproducirlo: `python3 scripts/resultados.py`. El detalle de qué "
          "prueba cada corpus y qué no, en las tres páginas de evidencia bajo `tests/`.", ""]
    return "\n".join(p)


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    fallas = []

    def ok(cond, que):
        if not cond:
            fallas.append(que)
        print(f"  {'ok  ' if cond else 'FALLA'} {que}")

    print("\nCada puerta tiene dueño")
    for _, cmd, _ in PUERTAS:
        duenio(cmd)
    ok(True, f"las {len(PUERTAS)} puertas de verificar.py tienen dueño declarado")

    print("\nContar comprobaciones")
    ok(len(RE_CHECK.findall("  ok   algo\n  FALLA otra\n   OK  tercera\n")) == 2,
       "cuenta las dos formas de escribir una comprobación y no la falla")
    ok(len(RE_CHECK.findall("esto dice ok en medio de una frase\n")) == 0,
       "y no cuenta un «ok» dentro de una frase")
    ok(len(RE_FALLA.findall("  FALLA algo\n  ok bien\n")) == 1, "y cuenta las fallas")

    print("\nEl dibujo")
    ok('viewBox' in barras([("Vera", 10, OK_)]), "las barras salen en SVG")
    ok(barras([]) == "", "sin datos no se dibuja una gráfica vacía")
    a = anillo(3, 0)
    ok('stroke-dasharray' in a and 'de 3 puertas' in a, "el anillo dice cuántas de cuántas")
    ok('&lt;b&gt;' in e("<b>"), "lo que entra a la página va escapado")

    print("\nEl archivo por agente")
    sin_plugin = sorted({q for q in ORDEN if q != "La familia" and q not in PLUGIN_DE})
    ok(not sin_plugin, f"cada dueño sabe en qué plugin vive{' · falta ' + str(sin_plugin) if sin_plugin else ''}")
    ok(set(NO_CUBRE) == set(QUE_ES),
       "y cada plugin dice qué no cubre su corrida, que es la mitad del archivo")

    print("\nLa página con datos de mentira")
    demo = [{"grupo": "código", "cmd": PUERTAS[2][1], "porque": "prueba",
             "quien": "Vera", "etiqueta": "x.py", "ok": True, "ms": 12,
             "checks": 7, "fallas": 0}]
    salida = pagina(demo, True)
    ok(salida.startswith("<!doctype html>") and salida.endswith("</html>"),
       "la página es un documento completo")
    ok("Lo que esta corrida no cubre" in salida,
       "y lleva siempre lo que todavía no se sabe")
    md = pagina_md(demo, True)
    ok(md.startswith("# ") and "Lo que esta corrida no cubre" in md,
       "y la versión en markdown, que es la que GitHub sí muestra")
    ok("<code>" not in md and "<b>" not in md,
       "sin etiquetas de HTML sueltas en el markdown")
    ok("{comandos}" not in salida, "y ningún hueco del texto se quedó sin rellenar")
    ok(etiqueta(["py", str(RAIZ / "plugins/criterio-pm/scripts/pmo.py"), "selftest"])
       == "criterio-pm/pmo.py selftest",
       "la copia de Samuel no se confunde con la fuente de Vera")

    print(f"\n{'todo en verde' if not fallas else f'{len(fallas)} FALLAS'}")
    return 0 if not fallas else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Dibuja los resultados de la verificación.")
    ap.add_argument("--rapido", action="store_true",
                    help="no regenera el material sintético")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    print("\nCriterio · corriendo la verificación para dibujarla\n")
    filas = correr(args.rapido)
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(pagina(filas, args.rapido), encoding="utf-8")
    SALIDA_MD.write_text(pagina_md(filas, args.rapido), encoding="utf-8")
    escritos = [SALIDA_MD] + por_agente(filas, args.rapido)
    rojas = [f for f in filas if not f["ok"]]
    print(f"\n{SALIDA.relative_to(RAIZ)} · {sum(f['checks'] for f in filas)} "
          f"comprobaciones en {len(filas)} puertas")
    for e in escritos:
        print(f"{e.relative_to(RAIZ)}")
    if rojas:
        print(f"{len(rojas)} en rojo, y la página lo dice")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
