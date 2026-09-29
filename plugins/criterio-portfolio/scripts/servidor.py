#!/usr/bin/env python3
"""Criterio PMO — Rostrum, el servidor.

    python3 servidor.py --informe <carpeta> --estado <estado> [--puerto 8787]
                        [--host 127.0.0.1] [--abierto] [--selftest]

Sirve el informe que `informe.py` ya produjo, y recibe peticiones para el agente.
Librería estándar, sin dependencias.

**Rostrum no calcula nada y no escribe ninguna ficha.** Es una proyección: lo
que muestra ya estaba escrito en disco antes de que alguien abriera el navegador.
Esa es la razón de que exista como pieza aparte y no como un modo del agente. Un
servidor que calculara al vuelo tendría que leer documentos, y entonces dos
personas abriendo la misma página verían dos portafolios distintos.

Lo único que escribe es la cola de peticiones, en `<estado>/peticiones/`, que es
una carpeta suya. El agente la lee cuando despierta. Nadie del otro lado de la
pantalla puede tocar un dato del portafolio: **el camino de escritura hacia la
ficha no existe en este archivo.**

## Sobre el acceso

**Rostrum no autentica a nadie, y es deliberado.** Un servidor de cien
líneas sobre la librería estándar no va a autenticar mejor que el proxy que el
banco ya tiene, y prometer que sí es exactamente lo que este plugin no hace.

Por eso escucha solo en `127.0.0.1` salvo que se le pase `--abierto`, y cuando se
le pasa lo dice en voz alta. Publicarlo se hace como se publica cualquier cosa
adentro: detrás de lo que la organización ya usa para eso.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.parse
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import informe  # la paleta y la página son suyas; aquí no se vuelven a escribir
import portafolio  # la historia la lee él; Rostrum no calcula nada y no escribe nada

TOPE_PETICION = 16 * 1024          # una petición es un párrafo, no un adjunto

# Las rutas, declaradas y no solo implícitas en el `if` de abajo. Se declaran porque
# se parecen a comandos —`/decisiones` es una ruta, no un `/comando`— y el verificador
# del repositorio necesita poder distinguirlas sin que nadie le escriba una excepción.
RUTAS = {
    '/': 'la portada: las tres secciones, la frescura y el formulario de peticiones',
    '/pmo': 'cómo va el portafolio · el informe de la PMO',
    '/decisiones': 'lo que necesita una decisión · para el comité',
    '/proyectos': 'el listado de proyectos',
    '/p/<codigo>': 'el informe de un proyecto, con enlace a su producto',
    '/productos': 'el listado de productos',
    '/producto/<nombre>': 'el informe de un producto, con enlace a sus proyectos',
    '/estado.json': 'de cuándo es el informe y cuántas peticiones hay abiertas',
    '/corridas': 'la historia de los tres agentes · ?agente=proyecto|producto y ?que=<comando> para filtrar',
    '/corrida/<agente>/<caso>/<id>': 'una corrida: sus cifras y lo que produjo, entero',
    '/historia/<codigo>': 'la línea de tiempo de un caso: desde cuándo arrastra cada señal',
    '/corte': 'qué cambió campo por campo entre dos cortes · ?a=<fecha>&b=<fecha>',
    '/peticion': 'POST · deja una pregunta escrita para el agente',
}

# Cada ruta amable apunta al archivo que `informe.py` escribió, y **redirige** en vez
# de servirlo en su lugar. La razón: las páginas enlazan entre sí por nombre de
# archivo, porque tienen que funcionar también abiertas desde el disco, comprimidas o
# impresas — el servidor es una proyección, no el dueño. Si `/pmo` sirviera el archivo
# sin redirigir, sus enlaces apuntarían a `/proyectos.html`, que desde `/pmo` no existe.
ALIAS = {
    '/pmo': 'index.html',
    '/decisiones': 'decisiones.html',
    '/proyectos': 'proyectos.html',
    '/productos': 'productos.html',
}
# Del archivo a su ruta amable, para que el árbol marque dónde está el lector.
ALIAS_INVERSO = {v: k for k, v in ALIAS.items()}

ASUNTOS = {
    'revisar': 'Que revise un proyecto contra sus documentos',
    'explicar': 'Que explique de dónde salió un dato del informe',
    'corregir': 'Que algo del informe no coincide con lo que sé',
    'otra': 'Otra cosa',
}

EXTRA = f"""
.con-arbol{{display:flex;gap:0;align-items:flex-start}}
.arbol{{flex:0 0 232px;position:sticky;top:0;padding:38px 20px 38px 0;
  border-right:1px solid {informe.FILETE};min-height:100vh;font-size:.93rem}}
.arbol .g{{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;
  color:{informe.ORO};font-weight:600;margin:1.6em 0 .5em}}
.arbol .g:first-child{{margin-top:0}}
.arbol ul{{list-style:none;margin:0;padding:0}}
.arbol li{{margin:.2em 0}}
.arbol a{{display:block;padding:.28em 0;color:{informe.TINTA};border:0}}
.arbol a:hover{{color:{informe.ORO}}}
.arbol a.yo{{color:{informe.ORO};font-weight:600}}
.arbol li.no span{{color:{informe.APAGADO}}}
.arbol li.cmd a{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.8rem;padding-left:.9em;color:{informe.APAGADO}}}
.arbol li.cmd a b{{color:{informe.ORO};font-weight:600}}\n.arbol li.run a{{font-size:.78rem;padding:.12em 0 .12em 1.8em;color:{informe.APAGADO}}}\n.arbol li.run em{{font-style:normal;color:{informe.ORO};opacity:.8}}
.arbol li.no em{{display:block;font-size:.76rem;color:{informe.APAGADO};font-style:normal}}
@media (max-width:900px){{.con-arbol{{display:block}}
  .arbol{{flex:none;border-right:0;border-bottom:1px solid {informe.FILETE};
    min-height:0;padding:20px 0;position:static}}}}
@media print{{.arbol{{display:none}}}}
.portada h1{{margin-bottom:.15em}}
.puertas{{display:flex;flex-wrap:wrap;gap:16px;margin:30px 0 0}}
.puerta{{flex:1 1 320px;border:1px solid {informe.FILETE};border-radius:10px;
  padding:22px 24px;background:{informe.PANEL_ALTO};display:block;
  border-bottom:1px solid {informe.FILETE};color:inherit}}
.puerta:hover{{border-color:{informe.ORO}}}
.puerta .q{{display:block;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;
  color:{informe.ORO};font-weight:600}}
.puerta .t{{display:block;font-size:1.2rem;color:{informe.TINTA};font-weight:500;
  margin:.35em 0 .3em;line-height:1.25}}
.puerta .d{{font-size:.93rem;color:{informe.APAGADO};margin:0}}
form.pide{{margin:14px 0 0;max-width:660px}}
form.pide .par{{display:flex;flex-wrap:wrap;gap:0 18px}}
form.pide .par > div{{flex:1 1 220px}}
label{{display:block;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;
  color:{informe.APAGADO};font-weight:600;margin:16px 0 5px}}
input,select,textarea{{width:100%;padding:10px 12px;border:1px solid {informe.FILETE};
  border-radius:6px;background:#fff;color:{informe.CUERPO};font:inherit;font-size:.95rem}}
input:focus,select:focus,textarea:focus{{outline:2px solid {informe.ORO};outline-offset:-1px}}
textarea{{min-height:110px;resize:vertical}}
button{{margin-top:20px;padding:11px 24px;border:1px solid {informe.ORO};border-radius:6px;
  background:{informe.ORO};color:{informe.CREMA};font:inherit;font-weight:600;cursor:pointer}}
button:hover{{background:{informe.TINTA};border-color:{informe.TINTA}}}
.aviso{{font-size:.88rem;color:{informe.APAGADO};margin:.6em 0 0;max-width:660px}}
@media print{{.puertas,form.pide{{display:none}}}}
"""


def e(x):
    return html.escape(str(x if x is not None else ''))


def pagina(titulo, cuerpo, hoy, nav='', activa=''):
    """La página del informe, con lo que solo el servidor necesita.

    El árbol va **dentro** de la hoja y en un `<nav>` aparte, no sustituyendo al enlace
    de vuelta: una página impresa o abierta desde el disco no tiene servidor que se lo
    sirva, y el informe tiene que seguir leyéndose igual.
    """
    return con_arbol(informe.pagina(titulo, cuerpo, hoy, nav), activa)


# ------------------------------------------------------------- la historia
#
# Una organización real produce documentos todos los días, y ese rastro es la memoria del
# proyecto. El portal mostraba solo el presente y se sobreescribía, así que nadie podía
# saber qué se dijo antes de una decisión — ni presentar un avance, ni entender dónde está
# un proyecto. Y hay una simetría que el producto necesita: Criterio le exige a una PMO que
# lo declarado tenga evidencia; si su propio informe se sobreescribe, a la PMO no la puede
# auditar nadie.
#
# Estas tres vistas leen y no escriben, como todo lo que hace Rostrum.


SIN_SALIDA = ' <em title="sin salida entregada">·</em>'


def corridas(h: dict, hoy: str, agente: str = '', que: str = '') -> str:
    """Nivel 1 · la historia de las corridas de los tres agentes.

    Cada fila dice de quién es y sobre qué. Sin eso, una lista que mezcla el portafolio con
    sesenta y cinco productos no se puede leer — y separarla en tres portales sería peor.
    """
    if agente or que:
        h = dict(h, corridas=[c for c in h["corridas"]
                              if (not agente or c.get("agente") == agente)
                              and (not que or comando_de(c.get("agente") or "portafolio",
                                                         c["que"]) == que)])
        h["total"] = len(h["corridas"])
    if not h["total"]:
        return pagina('Historia', '<div class="bloque"><p>Todavía no hay corridas '
                      'registradas. Cada comando que produce algo deja la suya.</p></div>',
                      hoy, nav())
    filas = []
    previo = None
    for c in h["corridas"]:
        d = (c.get("hallazgos") or 0) - (previo or 0) if previo is not None else None
        delta = ('—' if d is None else
                 f'<span class="{"mal" if d > 0 else "bien" if d < 0 else ""}">{d:+d}</span>')
        rel = c.get("relectura") or {}
        quien = c.get("agente") or 'portafolio'
        sobre = c.get("sobre")
        filas.append(
            f'<tr><td><a href="{ruta_corrida(c)}">{e(c["fecha"])}</a></td>'
            f'<td>{e(quien)}{" · " + e(sobre) if sobre else ""}</td>'
            f'<td>{e(c["que"])}{"" if c.get("salida") else SIN_SALIDA}</td>'
            f'<td class="n">{e(c.get("proyectos") or c.get("requerimientos"))}</td>'
            f'<td class="n">{e(c.get("documentos") or "—")}</td>'
            f'<td class="n">{e(rel.get("releidos") or "—")}</td>'
            f'<td class="n">{e(c.get("segundos") or "—")}</td>'
            f'<td class="n">{e(c.get("hallazgos"))}</td><td class="n">{delta}</td>'
            f'<td>{e(c.get("nota") or "")}</td></tr>')
        previo = c.get("hallazgos") or 0

    cuerpo = [
        f'<p class="entrada"><b>{h["total"]} corridas</b>'
        + (f' de <code>{e(que)}</code>' if que else '')
        + (f' del agente de {e(agente)}' if agente else
           f' de los agentes que trabajan sobre este portafolio')
        + f', de la del {e(h["desde"])} a la del {e(h["hasta"])}. Ninguna se borra: el '
        f'rastro de las corridas es la memoria del proyecto, y sin él no se puede '
        f'sostener que algo lleva meses sin resolverse.</p>',
        '<div class="bloque"><table><thead><tr><th>Corte</th><th>Agente</th>'
        '<th>Qué</th><th>Casos</th><th>Docs</th><th>Releídos</th><th>Seg</th>'
        '<th>Hallazgos</th><th>Cambio</th><th>Nota</th></tr></thead><tbody>',
        "".join(filas), '</tbody></table></div>']

    # Lo que lleva más tiempo sin resolverse: la lista con la que se arma un comité.
    arrastres = []
    for codigo, senales in h["casos"].items():
        for s, x in senales.items():
            if x["seguidas"] >= 2 and not x.get("resuelta_en"):
                arrastres.append((x["seguidas"], codigo, s, x["primera"]))
    if arrastres:
        arrastres.sort(reverse=True)
        cuerpo += ['<h2>Lo que se arrastra</h2>',
                   '<p class="entrada">Una señal que sonó una vez es ruido. Una que lleva '
                   'varios cortes seguidos es una decisión que nadie ha tomado.</p>',
                   '<div class="bloque"><table><thead><tr><th>Caso</th><th>Señal</th>'
                   '<th>Cortes seguidos</th><th>Desde</th></tr></thead><tbody>']
        for n_, codigo, s, desde in arrastres[:40]:
            cuerpo.append(f'<tr><td><a href="/historia/{e(codigo)}">{e(codigo)}</a></td>'
                          f'<td><code>{e(s)}</code></td><td class="n">{n_}</td>'
                          f'<td>{e(desde)}</td></tr>')
        cuerpo.append('</tbody></table></div>')

    if len(h["instantaneas"]) > 1:
        a, b = h["instantaneas"][-2], h["instantaneas"][-1]
        cuerpo.append(f'<p class="entrada">Para ver qué cambió campo por campo entre dos '
                      f'cortes: <a href="/corte?a={a}&b={b}">{a} → {b}</a>.</p>')
    cuerpo.append(AVISO_HISTORIA)
    return pagina('Historia de las corridas', "".join(cuerpo), hoy, nav(), '/corridas')


def linea_de_tiempo(h: dict, codigo: str, hoy: str) -> tuple:
    """Nivel 2 · desde cuándo este caso arrastra cada señal, y cuál se resolvió.

    Devuelve (código, cuerpo). Una vista que puede fallar tiene que decir con qué estado
    responder: devolvía la página de error y el servidor la enviaba con 200, así que el
    cliente recibía un «no está» marcado como «aquí está».
    """
    senales = h["casos"].get(codigo)
    if not senales:
        return 404, error(404, f'No hay historia registrada de {codigo}', hoy)
    abiertas = {s: x for s, x in senales.items() if not x.get("resuelta_en")}
    cerradas = {s: x for s, x in senales.items() if x.get("resuelta_en")}

    def tabla(d, cabeza, extra):
        if not d:
            return ''
        out = [f'<h2>{cabeza}</h2>', '<div class="bloque"><table><thead><tr>'
               f'<th>Señal</th><th>Desde</th><th>Cortes</th><th>Seguidos</th>{extra}'
               '</tr></thead><tbody>']
        for s, x in sorted(d.items(), key=lambda i: -i[1]["seguidas"]):
            fin = f'<td>{e(x.get("resuelta_en"))}</td>' if extra else ''
            out.append(f'<tr><td><code>{e(s)}</code></td><td>{e(x["primera"])}</td>'
                       f'<td class="n">{x["corridas"]}</td>'
                       f'<td class="n">{x["seguidas"]}</td>{fin}</tr>')
        out.append('</tbody></table></div>')
        return "".join(out)

    cuerpo = [f'<p class="entrada">Lo que las corridas han dicho de <b>{e(codigo)}</b> '
              f'entre el {e(h["desde"])} y el {e(h["hasta"])}. '
              f'<a href="/p/{e(codigo)}">Ver su informe de hoy</a>.</p>',
              tabla(abiertas, 'Lo que sigue abierto', ''),
              tabla(cerradas, 'Lo que se resolvió', '<th>Resuelta en</th>'),
              AVISO_HISTORIA]
    return 200, pagina(f'Historia · {codigo}', "".join(cuerpo), hoy, nav(), '/corridas')


def corte(estado: Path, a: str, b: str, hoy: str) -> tuple:
    """Nivel 3 · qué cambió campo por campo entre dos cortes. Devuelve (código, cuerpo)."""
    snaps = estado / 'snapshots'
    fa, fb = snaps / f'{a}.json', snaps / f'{b}.json'
    for f, cual in ((fa, a), (fb, b)):
        if not f.is_file():
            return 404, error(404, f'No hay instantánea del {cual}', hoy)
    da = json.loads(fa.read_text(encoding='utf-8'))
    db = json.loads(fb.read_text(encoding='utf-8'))
    pa = {k: v for k, v in (da.get('projects') or da).items()} if isinstance(da, dict) else {}
    pb = {k: v for k, v in (db.get('projects') or db).items()} if isinstance(db, dict) else {}

    filas = []
    for codigo in sorted(set(pa) | set(pb)):
        va, vb = pa.get(codigo) or {}, pb.get(codigo) or {}
        if not isinstance(va, dict) or not isinstance(vb, dict):
            continue
        for campo in sorted(set(va) | set(vb)):
            x, y = va.get(campo), vb.get(campo)
            if x != y:
                filas.append(f'<tr><td><a href="/historia/{e(codigo)}">{e(codigo)}</a></td>'
                             f'<td><code>{e(campo)}</code></td>'
                             f'<td>{e(x if x is not None else "—")}</td>'
                             f'<td>{e(y if y is not None else "—")}</td></tr>')
    cuerpo = [f'<p class="entrada">Lo que cambió campo por campo entre el corte del '
              f'{e(a)} y el del {e(b)}: <b>{len(filas)} cambios</b>. Es la vista que '
              f'contesta «desde cuándo» sin que nadie tenga que recordarlo.</p>']
    if filas:
        cuerpo += ['<div class="bloque"><table><thead><tr><th>Proyecto</th><th>Campo</th>'
                   f'<th>{e(a)}</th><th>{e(b)}</th></tr></thead><tbody>',
                   "".join(filas[:500]), '</tbody></table></div>']
        if len(filas) > 500:
            cuerpo.append(f'<p class="entrada">Se muestran 500 de {len(filas)}.</p>')
    else:
        cuerpo.append('<div class="bloque"><p>Ningún campo cambió entre esos dos '
                      'cortes.</p></div>')
    cuerpo.append(AVISO_HISTORIA)
    return 200, pagina(f'Corte {a} → {b}', "".join(cuerpo), hoy, nav(), '/corte')


md_a_html = portafolio.md_a_html


def ruta_corrida(c: dict) -> str:
    """La dirección de una corrida en el portal. Las corridas viejas no tienen `id`: se
    enlazan por fecha y qué, que es lo que había, y la página avisa si no está."""
    return (f'/corrida/{e(c.get("agente") or "portafolio")}/{e(c.get("sobre") or "-")}/'
            f'{e(c.get("id") or (c["fecha"] + "-" + c["que"]))}')


def vista_corrida(estado: Path, agente: str, sobre: str, ident: str, hoy: str) -> tuple:
    """Una corrida, entera: las cifras que midió y lo que el comando produjo."""
    for quien, cual, d in portafolio.estados_de(estado):
        if quien != agente or (cual or '-') != sobre:
            continue
        f = d / 'corridas' / f'{ident}.md'
        if not f.is_file():
            # Las corridas anteriores a la identidad propia se llamaban <fecha>-<que>.md.
            f = d / 'corridas' / f'{ident.rsplit("-", 1)[0]}.md' if ident[-1].isdigit() else f
        if not f.is_file():
            break
        md = f.read_text(encoding='utf-8')
        que = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', ident)
        que = re.sub(r'-\d+$', '', que)
        cmd = comando_de(agente, que)
        cuerpo = [f'<p class="entrada">Corrida <code>{e(ident)}</code> del agente de '
                  f'{e(agente)}{" sobre <b>" + e(sobre) + "</b>" if sobre != "-" else ""}. '
                  f'Lo que sigue es lo que la corrida escribió sola al terminar; nada de esto se '
                  f'redactó después.</p>',
                  '<div class="bloque">', md_a_html(md), '</div>', AVISO_HISTORIA]
        return 200, pagina(f'Corrida · {ident}', ''.join(cuerpo), hoy, nav(),
                           f'/corridas?agente={agente}&que={cmd}')
    return 404, error(404, f'No hay corrida {ident} de {agente}', hoy)


# Va en las tres páginas, y no es un descargo de responsabilidad de relleno: un registro
# de cinco cortes diciendo que un proyecto estuvo en verde sin sustento es un artefacto
# político, y si la página no dice qué es, alguien lo va a usar para lo que no es.
AVISO_HISTORIA = (
    '<p class="entrada">Esta es la historia de <b>lo que el agente leyó en los documentos</b>, '
    'no de lo que pasó ni un juicio sobre nadie. Cada hallazgo remite al documento que lo '
    'sostiene, y un documento que se archivó tarde cambia la lectura sin que nadie haya '
    'hecho nada mal.</p>')


# El árbol de la izquierda. No es decoración: si un patrocinador tiene que preguntarle a
# alguien dónde está el histórico, el histórico no es transparente. Y lo que **no** está
# construido aparece marcado en vez de omitido, porque un menú que esconde los huecos
# promete un producto que no existe.
#
# Los tres agentes viven en el árbol aunque solo uno tenga servidor: el gerente de proyecto
# y el de producto publican su ficha para que la lea el portafolio, y el lector tiene que
# saber que existen y por dónde entra su información.
# **Un solo Rostrum para los tres agentes.** El gerente de proyecto y el de producto no
# tienen portal aparte: publican su estado junto al del portafolio y este mismo servidor lo
# sirve. Un portal por agente obligaría a un patrocinador a saber a cuál entrar, y eso ya no
# es transparencia — es un directorio interno.
ARBOL = [
    ("El portafolio · Vera", [
        ("/pmo", "Cómo va el portafolio", True),
        ("/decisiones", "Lo que necesita una decisión", True),
        ("/proyectos", "Los proyectos, uno por uno", True),
        ("/productos", "Los productos y sus proyectos", True),
    ]),
    ("El proyecto · Samuel", [
        ("/corridas?agente=proyecto", "Sus corridas y qué encontró", True),
    ]),
    ("El producto · Alba", [
        ("/corridas?agente=producto", "Sus corridas y qué encontró", True),
    ]),
    ("La historia de los tres", [
        ("/corridas", "Todas las corridas, y qué se arrastra", True),
        ("/corte", "Qué cambió entre dos cortes", True),
    ]),
    ("Preguntar", [
        ("/#preguntar", "Dejar una pregunta escrita para el agente", True),
    ]),
]


def con_arbol(pagina_html: str, activa: str = "") -> str:
    """Mete el árbol y su estilo en una página que ya venía escrita."""
    if 'class="arbol"' in pagina_html or '<div class="hoja">' not in pagina_html:
        return pagina_html
    return (pagina_html
            .replace('</style>', EXTRA + '</style>', 1)
            .replace('<div class="hoja">',
                     f'<div class="con-arbol">{arbol(activa)}<div class="hoja">', 1)
            .replace('</div></body></html>', '</div></div></body></html>', 1))


# Los tres primeros grupos del árbol son los tres agentes, en este orden. Bajo cada uno
# van sus comandos con cuántas veces corrieron; eso no se puede escribir de antemano
# porque depende del estado, así que el árbol deja un marcador y `rellenar_arbol` lo
# sustituye al servir.
AGENTE_DEL_GRUPO = {0: "portafolio", 1: "proyecto", 2: "producto"}
PLUGIN = {"portafolio": "criterio-portfolio", "proyecto": "criterio-project",
          "producto": "criterio-product"}
# Los tres nombres históricos de `--what`; todo lo demás registra con el nombre del comando.
COMANDO_DE = {("portafolio", "sweep"): "portfolio-scan",
              ("portafolio", "report"): "portfolio-report",
              ("portafolio", "confirmation"): "portfolio-report",
              ("portafolio", "requests"): "portfolio-wake",
              ("proyecto", "sweep"): "pm-minutes", ("proyecto", "report"): "pm-report",
              ("proyecto", "confirmation"): "pm-publish",
              ("producto", "review"): "product-requirements",
              ("producto", "report"): "product-publish",
              ("producto", "crossed"): "product-trace"}


def comando_de(agente: str, que: str) -> str:
    return COMANDO_DE.get((agente, que), que)


def arbol(activa: str = "") -> str:
    """El menú de la izquierda, con lo que hay y lo que todavía no."""
    out = ['<nav class="arbol" aria-label="Secciones">']
    for i, (grupo, hijos) in enumerate(ARBOL):
        out.append(f'<p class="g">{e(grupo)}</p><ul>')
        for ruta, texto, hay in hijos:
            if not hay:
                out.append(f'<li class="no"><span>{e(texto)}</span>'
                           f'<em>sin servidor propio</em></li>')
            else:
                cl = ' class="yo"' if ruta == activa else ''
                out.append(f'<li><a href="{e(ruta)}"{cl}>{e(texto)}</a></li>')
        if i in AGENTE_DEL_GRUPO:
            out.append(f'<!--corridas:{AGENTE_DEL_GRUPO[i]}-->')
        out.append('</ul>')
    out.append('</nav>')
    return "".join(out)


def rellenar_arbol(pagina_html: str, h: dict, activa_que: tuple = ("", "")) -> str:
    """Pone bajo cada agente sus comandos y cuántas veces corrió cada uno.

    Es lo que pidió la prueba de los tres agentes a la vez: ver, sin abrir una tabla, qué
    comandos han corrido y cuáles no. Un comando que no aparece aquí no ha dejado corrida,
    y eso también es un dato.
    """
    por_agente = {}
    for c in h.get("corridas") or []:
        a = c.get("agente") or "portafolio"
        por_agente.setdefault(a, {}).setdefault(comando_de(a, c["que"]), 0)
        por_agente[a][comando_de(a, c["que"])] += 1
    for agente in AGENTE_DEL_GRUPO.values():
        marca = f'<!--corridas:{agente}-->'
        if marca not in pagina_html:
            continue
        cmds = por_agente.get(agente) or {}
        if not cmds:
            filas = '<li class="no"><span>ningún comando ha dejado corrida</span></li>'
        else:
            partes = []
            for cmd, n in sorted(cmds.items()):
                yo = ' class="yo"' if (agente, cmd) == activa_que else ''
                partes.append(
                    f'<li class="cmd"><a href="/corridas?agente={e(agente)}&amp;que={e(cmd)}"{yo}>'
                    f'/{e(PLUGIN[agente])}:{e(cmd)} <b>· {n}</b></a><ul>')
                suyas = [c for c in h.get("corridas") or []
                         if (c.get("agente") or "portafolio") == agente
                         and comando_de(agente, c["que"]) == cmd]
                for c in suyas:
                    etiqueta = c.get("fecha", "") + (f' · {c["sobre"]}' if c.get("sobre") else '')
                    partes.append(f'<li class="run"><a href="{ruta_corrida(c)}">{e(etiqueta)}'
                                  f'{"" if c.get("salida") else " <em>sin salida</em>"}</a></li>')
                partes.append('</ul></li>')
            filas = ''.join(partes)
        pagina_html = pagina_html.replace(marca, filas)
    return pagina_html


def nav() -> str:
    return ('<a href="/">Portada</a> · <a href="/pmo">Portafolio</a> · '
            '<a href="/decisiones">Decisiones</a> · <a href="/corridas">Historia</a>')


# ---------------------------------------------------------------- la cola

def buzon(estado: Path) -> Path:
    return estado / 'peticiones'


def guardar_peticion(estado: Path, datos: dict) -> dict:
    """Escribe una petición y nada más. El agente la lee cuando despierta."""
    carpeta = buzon(estado)
    carpeta.mkdir(parents=True, exist_ok=True)
    ahora = dt.datetime.now(dt.timezone.utc)
    registro = {
        'id': ahora.strftime('%Y%m%d-%H%M%S-') + uuid.uuid4().hex[:6],
        'recibida': ahora.isoformat(timespec='seconds'),
        'asunto': datos.get('asunto') or 'otra',
        'proyecto': (datos.get('proyecto') or '').strip()[:40] or None,
        'de': (datos.get('de') or '').strip()[:80] or None,
        'texto': (datos.get('texto') or '').strip()[:4000],
        'respondida': None,
    }
    (carpeta / f"{registro['id']}.json").write_text(
        json.dumps(registro, ensure_ascii=False, indent=2), encoding='utf-8')
    return registro


def pendientes(estado: Path) -> list:
    salida = []
    for f in sorted(buzon(estado).glob('*.json')):
        try:
            r = json.loads(f.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            continue
        if not r.get('respondida'):
            salida.append(r)
    return salida


# ---------------------------------------------------------------- frescura

def frescura(informe_dir: Path, estado: Path) -> dict:
    """De cuándo es lo que se está mirando. Sin esto, nadie sabe si el informe
    es de hoy o de hace tres semanas, y un informe viejo sin fecha miente."""
    portada = informe_dir / 'index.html'
    generado = None
    if portada.exists():
        generado = dt.datetime.fromtimestamp(
            portada.stat().st_mtime, dt.timezone.utc).isoformat(timespec='seconds')
    cad = estado / 'cadencia.json'
    proximo = None
    if cad.exists():
        try:
            proximo = json.loads(cad.read_text(encoding='utf-8')).get('next_wake')
        except (json.JSONDecodeError, OSError):
            pass
    # Qué hay publicado sale de los archivos, no de una lista aparte: si `informe.py`
    # dejó de escribir una página, aquí se nota en vez de seguir prometiéndola.
    paginas = sorted(p.stem for p in informe_dir.glob('*.html')
                     if p.stem not in ('index', 'decisiones', 'proyectos', 'productos')
                     and not p.stem.startswith('producto-'))
    productos = sorted(p.stem[len('producto-'):] for p in informe_dir.glob('producto-*.html'))
    return {'informe_generado': generado, 'proxima_corrida': proximo,
            'proyectos': paginas, 'productos': productos,
            'peticiones_abiertas': len(pendientes(estado))}


def edad(iso, ahora=None):
    if not iso:
        return None
    ahora = ahora or dt.datetime.now(dt.timezone.utc)
    try:
        return (ahora - dt.datetime.fromisoformat(iso)).days
    except ValueError:
        return None


# ---------------------------------------------------------------- las páginas

def portada(fr: dict, hoy: str, org: str = '') -> str:
    dias = edad(fr.get('informe_generado'))
    if fr.get('informe_generado') is None:
        sello = ('<strong>Todavía no hay informe.</strong> Alguien tiene que correr '
                 '<code>/portfolio-report html</code> antes de que esto muestre algo.')
    elif dias and dias > 7:
        sello = (f"El informe que se sirve aquí se produjo hace "
                 f"<strong>{informe.plural(dias, 'día', 'días')}</strong>. "
                 f"No se recalcula al abrir esta página: lo que ves es de esa fecha.")
    else:
        sello = (f"El informe que se sirve aquí se produjo "
                 f"{'hoy' if not dias else 'hace ' + informe.plural(dias, 'día', 'días')}. "
                 f"No se recalcula al abrir esta página.")
    prox = fr.get('proxima_corrida')
    if prox:
        sello += f" La próxima corrida del agente es el <strong>{e(prox)}</strong>."

    abiertas = fr.get('peticiones_abiertas') or 0
    cola = ''
    if abiertas:
        cola = (f'<p class="aviso">Hay {informe.plural(abiertas, "petición sin responder", "peticiones sin responder")}. '
                f'El agente las toma en su próxima corrida.</p>')

    n_proy = len(fr.get('proyectos') or [])
    n_prod = len(fr.get('productos') or [])
    opciones = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in ASUNTOS.items())

    # Las tres secciones, en el orden en que alguien las necesita: cómo va todo,
    # después el proyecto que le toca, después el producto que le importa.
    puertas = [
        ('Informes PMO', '/pmo', 'Cómo va el portafolio',
         'Lo que solo se ve mirando todo junto: los verdes que la evidencia no sostiene, '
         'lo que lleva semanas en silencio, quién patrocina más de una cosa.'),
        ('Proyectos', '/proyectos',
         informe.plural(n_proy, 'proyecto', 'proyectos') if n_proy else 'El listado',
         'El listado, y el informe de cada uno: qué declara, qué dice la evidencia, y el '
         'documento del que salió cada dato. Cada proyecto enlaza al producto que lo '
         'originó.'),
        ('Productos', '/productos',
         informe.plural(n_prod, 'producto', 'productos') if n_prod else 'El listado',
         'Un proyecto termina; un producto sobrevive a todos los proyectos que lo '
         'construyeron. Aquí se ve el producto completo, incluso cuando lo construyen '
         'proyectos que reportan a comités distintos.'),
    ]
    tarjetas = ''.join(f"""<a class="puerta" href="{ruta}">
    <span class="q">{e(q)}</span><span class="t">{e(titulo)}</span>
    <p class="d">{desc}</p></a>""" for q, ruta, titulo, desc in puertas)

    cuerpo = f"""<div class="portada">
<span class="ante">{e(org) if org else 'Portafolio de proyectos'}</span>
<h1>Oficina de proyectos</h1>
<p class="pie-cab">{sello}</p>

<div class="puertas">{tarjetas}</div>
<p class="aviso">El comité tiene su propia vista, que no es ninguna de estas tres recortada:
<a href="/decisiones">lo que necesita una decisión</a>, como pregunta cerrada y con la
consecuencia de no decidirlo.</p>

<h2>Pedirle algo al agente</h2>
<p>Esto no le contesta ahora: <strong>deja la pregunta escrita</strong> y el agente la
toma en su próxima corrida. Sirve para lo que el informe no alcanza a responder —
por qué un dato dice lo que dice, o que algo no coincide con lo que tú sabes.</p>
{cola}
<form class="pide" method="post" action="/peticion">
  <label for="asunto">De qué se trata</label>
  <select id="asunto" name="asunto">{opciones}</select>
  <div class="par">
    <div><label for="proyecto">Proyecto, si aplica</label>
      <input id="proyecto" name="proyecto" placeholder="PRY-001" maxlength="40"></div>
    <div><label for="de">Quién pregunta</label>
      <input id="de" name="de" placeholder="Tu nombre" maxlength="80"></div>
  </div>
  <label for="texto">Qué necesitas</label>
  <textarea id="texto" name="texto" maxlength="4000"
    placeholder="Escríbelo como se lo dirías a la persona de la PMO."></textarea>
  <button type="submit">Dejar la petición</button>
</form>
<p class="aviso"><strong>Esta página no pide contraseña</strong>, así que quien pregunta
es quien dice ser y nada más. No escribas aquí nada que no pondrías en un correo
interno.</p>
</div>"""
    return pagina('Portafolio de proyectos', cuerpo, hoy)


def recibida(registro: dict, hoy: str) -> str:
    cuerpo = f"""<span class="ante">Petición recibida</span>
<h1>Queda anotada</h1>
<p class="pie-cab">{e(registro['id'])}</p>
<div class="bloque info">
<h3>Qué pasa ahora</h3>
<p>El agente la lee en su próxima corrida. <strong>No hay nadie del otro lado
respondiendo en este momento</strong>, y decirlo es más honesto que un «en breve
te contactamos».</p>
<p>Si es urgente, el camino sigue siendo el de siempre: la persona de la PMO.</p>
</div>
<div class="decision"><p class="p">{e(ASUNTOS.get(registro['asunto'], registro['asunto']))}</p>
<dl><dt>Proyecto</dt><dd>{e(registro['proyecto'] or '—')}</dd>
<dt>Quién pregunta</dt><dd>{e(registro['de'] or 'no lo dijo')}</dd>
<dt>Qué necesita</dt><dd>{e(registro['texto']) or '<em>en blanco</em>'}</dd></dl></div>"""
    return pagina('Petición recibida', cuerpo, hoy,
                  '<div class="nav"><a href="/">← Volver al portafolio</a></div>')


def error(codigo: int, que: str, hoy: str) -> str:
    cuerpo = f"""<span class="ante">{codigo}</span>
<h1>{e(que)}</h1>
<p class="pie-cab">Este servidor solo sirve el informe que ya se produjo. No busca
nada más ni ejecuta nada.</p>"""
    return pagina(f'{codigo}', cuerpo, hoy, '<div class="nav"><a href="/">← Portafolio</a></div>')


# ---------------------------------------------------------------- el servidor

SEGURO = re.compile(r'^[A-Za-z0-9._-]+$')


class Manejador(BaseHTTPRequestHandler):
    server_version = 'criterio-portfolio'
    sys_version = ''
    informe_dir: Path = Path('.')
    estado: Path = Path('.')
    organizacion: str = ''
    callado: bool = False

    # --- utilidades -----------------------------------------------------
    def log_message(self, formato, *args):   # una línea por visita, sin ruido
        if not self.callado:
            sys.stderr.write(f"{self.address_string()} · {formato % args}\n")

    def responder(self, codigo, cuerpo: bytes, tipo='text/html; charset=utf-8'):
        self.send_response(codigo)
        self.send_header('Content-Type', tipo)
        self.send_header('Content-Length', str(len(cuerpo)))
        # El informe lleva datos de proyectos. Que no se quede en caches intermedios.
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(cuerpo)

    def html(self, codigo, texto):
        # Toda página servida lleva bajo cada agente sus comandos con sus corridas. Se
        # calcula al servir, porque el estado cambia mientras el servidor corre.
        if '<!--corridas:' in texto:
            try:
                h = portafolio.historia(self.estado, todos=True)
            except Exception:  # un estado a medio escribir no tumba el portal
                h = {"corridas": []}
            texto = rellenar_arbol(texto, h, getattr(self, '_activa_que', ("", "")))
        self.responder(codigo, texto.encode('utf-8'))

    def hoy(self):
        return dt.date.today().isoformat()

    def archivo(self, nombre):
        """Sirve un archivo del informe, y solo del informe."""
        if not SEGURO.match(nombre):
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        ruta = (self.informe_dir / nombre).resolve()
        raiz = self.informe_dir.resolve()
        if raiz not in ruta.parents or not ruta.is_file():
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        # El árbol se inyecta **al servir**, no se escribe en el archivo. `informe.py`
        # produce páginas que tienen que abrirse desde el disco, comprimidas o impresas,
        # y ahí no hay servidor que sirva `/corridas`: un menú con enlaces muertos es
        # peor que ninguno. Pero servidas sí lo llevan, porque un árbol que aparece en
        # unas páginas y desaparece en otras deja al lector sin saber dónde está.
        crudo = ruta.read_bytes()
        if nombre.endswith('.html'):
            try:
                self.html(200, con_arbol(crudo.decode('utf-8'),
                                         ALIAS_INVERSO.get(nombre, '')))
                return
            except UnicodeDecodeError:
                pass
        self.responder(200, crudo)

    # --- rutas ----------------------------------------------------------
    def do_HEAD(self):
        self.do_GET()

    def a(self, archivo):
        """Redirige a un archivo del informe. Ver el comentario de ALIAS."""
        if not SEGURO.match(archivo) or not (self.informe_dir / archivo).is_file():
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        self.send_response(302)
        self.send_header('Location', '/' + archivo)
        self.send_header('Content-Length', '0')
        self.end_headers()

    def do_GET(self):
        ruta = urllib.parse.urlparse(self.path).path.rstrip('/') or '/'
        if ruta == '/':
            self.html(200, portada(frescura(self.informe_dir, self.estado), self.hoy(),
                                   self.organizacion))
        elif ruta in ALIAS:
            self.a(ALIAS[ruta])
        elif ruta.startswith('/p/'):
            self.a(ruta[3:] + '.html')
        elif ruta.startswith('/producto/'):
            self.a('producto-' + ruta[len('/producto/'):] + '.html')
        elif ruta == '/corridas':
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            agente = (q.get('agente') or [''])[0]
            que = (q.get('que') or [''])[0]
            h = portafolio.historia(self.estado, todos=True)
            self._activa_que = (agente, que)
            self.html(200, corridas(h, self.hoy(), agente, que))
        elif ruta.startswith('/corrida/'):
            partes = ruta.split('/')[2:]
            if len(partes) == 3 and all(SEGURO.match(urllib.parse.unquote(x)) for x in partes):
                agente, sobre, ident = (urllib.parse.unquote(x) for x in partes)
                self.html(*vista_corrida(self.estado, agente, sobre, ident, self.hoy()))
            else:
                self.html(404, error(404, 'Eso no está aquí', self.hoy()))
        elif ruta.startswith('/historia/'):
            h = portafolio.historia(self.estado, todos=True)
            self.html(*linea_de_tiempo(h, ruta[len('/historia/'):], self.hoy()))
        elif ruta == '/corte':
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            snaps = sorted(x.stem for x in (self.estado / 'snapshots').glob('*.json'))
            a = (q.get('a') or [snaps[-2] if len(snaps) > 1 else ''])[0]
            b = (q.get('b') or [snaps[-1] if snaps else ''])[0]
            if not a or not b:
                self.html(404, error(404, 'Hacen falta dos cortes para comparar',
                                     self.hoy()))
            else:
                self.html(*corte(self.estado, a, b, self.hoy()))
        elif ruta == '/estado.json':
            cuerpo = json.dumps(frescura(self.informe_dir, self.estado),
                                ensure_ascii=False, indent=2).encode('utf-8')
            self.responder(200, cuerpo, 'application/json; charset=utf-8')
        elif ruta.endswith('.html'):
            # Las páginas tal como `informe.py` las escribió. Es lo que los enlaces
            # entre páginas usan, y `archivo` comprueba que no se salga de la carpeta.
            self.archivo(ruta.lstrip('/'))
        else:
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))

    def do_POST(self):
        ruta = urllib.parse.urlparse(self.path).path.rstrip('/') or '/'
        if ruta != '/peticion':
            self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            return
        try:
            largo = int(self.headers.get('Content-Length') or 0)
        except ValueError:
            largo = -1
        if largo < 0 or largo > TOPE_PETICION:
            self.html(413, error(413, 'Eso es demasiado largo para una petición',
                                 self.hoy()))
            return
        crudo = self.rfile.read(largo).decode('utf-8', 'replace')
        campos = {k: v[0] for k, v in urllib.parse.parse_qs(crudo).items()}
        registro = guardar_peticion(self.estado, campos)
        self.html(200, recibida(registro, self.hoy()))


def arrancar(informe_dir: Path, estado: Path, host: str, puerto: int, org: str = '') -> int:
    Manejador.informe_dir = informe_dir
    Manejador.estado = estado
    Manejador.organizacion = org
    buzon(estado).mkdir(parents=True, exist_ok=True)
    fr = frescura(informe_dir, estado)

    if fr['informe_generado'] is None:
        print('Aviso: no hay informe en esa carpeta. La portada lo va a decir.\n'
              '       Corre primero:  /portfolio-report html\n')

    with ThreadingHTTPServer((host, puerto), Manejador) as srv:
        real = srv.server_address[1]
        print(f'Rostrum · Criterio PMO · {org or "sirviendo"} {informe_dir}')
        print(f'  Portada         http://{host}:{real}/')
        print(f'  Informes PMO    http://{host}:{real}/pmo')
        print(f'  Comité          http://{host}:{real}/decisiones')
        print(f'  Proyectos       http://{host}:{real}/proyectos'
              f'   ({len(fr["proyectos"])})')
        print(f'  Productos       http://{host}:{real}/productos'
              f'   ({len(fr["productos"])})')
        print(f'  Frescura        http://{host}:{real}/estado.json')
        if host not in ('127.0.0.1', 'localhost', '::1'):
            print()
            print('  ATENCIÓN: escuchando fuera de este equipo y SIN AUTENTICACIÓN.')
            print('  Cualquiera que alcance este puerto ve el portafolio completo.')
            print('  Publícalo únicamente detrás del control de acceso de tu organización.')
        print('\n  Ctrl-C para parar. No escribe ninguna ficha.\n')
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print('\nParado.')
    return 0


# ---------------------------------------------------------------- comprobarse

def selftest() -> int:
    """Lo que este servidor puede romper sin que nadie lo note.

    Dos cosas, y ninguna se ve mirando la pantalla: que sirva un archivo que no
    es del informe, y que la cola de peticiones toque algo que no es suyo.
    """
    import http.client
    import tempfile
    import threading

    fallas = []

    def ok(que, real, esperado):
        if real != esperado:
            fallas.append(f'{que}: {real!r} en vez de {esperado!r}')
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}')

    tmp = Path(tempfile.mkdtemp())
    inf, est = tmp / 'informe', tmp / 'estado'
    inf.mkdir(); (est / 'records').mkdir(parents=True)
    # Con historia, para que las tres vistas se ejerciten de verdad y no solo existan.
    # Dos cortes con un campo distinto entre ellos, y dos corridas con una señal que se
    # arrastra: es el mínimo con el que las tres páginas tienen algo que decir.
    (est / 'snapshots').mkdir(parents=True, exist_ok=True)
    (est / 'snapshots' / '2026-08-31.json').write_text(json.dumps(
        {'projects': {'PRY-001': {'declared.status': 'verde', 'plan.end_date': '2026-06-30'}}}),
        encoding='utf-8')
    (est / 'snapshots' / '2026-09-07.json').write_text(json.dumps(
        {'projects': {'PRY-001': {'declared.status': 'verde', 'plan.end_date': '2026-09-30'}}}),
        encoding='utf-8')
    (est / 'corridas').mkdir(parents=True, exist_ok=True)
    (est / 'corridas' / '2026-08-31-sweep-1.md').write_text(
        '# Corrida del 2026-08-31 · sweep\n\n| Señal | Hallazgos |\n|---|---:|\n| `silent` | 1 |\n\n'
        'la primera\n\n## Lo que produjo\n\nUn proyecto en silencio.\n', encoding='utf-8')
    (est / 'corridas.json').write_text(json.dumps([
        {'id': '2026-08-31-sweep-1', 'salida': True,
         'que': 'sweep', 'fecha': '2026-08-31', 'proyectos': 1, 'documentos': 4,
         'segundos': 2, 'hallazgos': 2, 'por_senal': {'silent': 1, 'variance_time': 1},
         'por_caso': {'PRY-001': ['silent', 'variance_time']}, 'nota': 'la primera'},
        {'que': 'report', 'fecha': '2026-09-07', 'proyectos': 1, 'documentos': 5,
         'segundos': 3, 'hallazgos': 1, 'por_senal': {'variance_time': 1},
         'por_caso': {'PRY-001': ['variance_time']}, 'nota': 'el silencio se resolvió'}]),
        encoding='utf-8')
    for nombre, texto in (('index', 'pmo'), ('decisiones', 'decisiones'),
                          ('proyectos', 'listado de proyectos'),
                          ('productos', 'listado de productos'),
                          ('PRY-001', 'uno'), ('producto-cuenta-transaccional', 'la cuenta')):
        # Páginas completas, como las que `informe.py` escribe de verdad. Con fragmentos
        # el injerto del árbol no tenía dónde agarrarse y la comprobación pasaba en falso.
        (inf / f'{nombre}.html').write_text(
            informe.pagina(texto, f'<h1>{texto}</h1>', '2026-09-28'), encoding='utf-8')
    (est / 'records' / 'PRY-001.json').write_text('{"identity":{}}', encoding='utf-8')
    (tmp / 'secreto.txt').write_text('no debe salir', encoding='utf-8')

    Manejador.informe_dir, Manejador.estado, Manejador.callado = inf, est, True
    Manejador.organizacion = 'Banco del Selftest'
    srv = ThreadingHTTPServer(('127.0.0.1', 0), Manejador)
    hilo = threading.Thread(target=srv.serve_forever, daemon=True); hilo.start()
    puerto = srv.server_address[1]

    def pedir(ruta, metodo='GET', cuerpo=None):
        c = http.client.HTTPConnection('127.0.0.1', puerto, timeout=5)
        cab = {'Content-Type': 'application/x-www-form-urlencoded'} if cuerpo else {}
        c.request(metodo, ruta, cuerpo, cab)
        r = c.getresponse(); datos = r.read().decode('utf-8', 'replace')
        destino = r.getheader('Location'); c.close()
        return (r.status, datos, destino) if destino else (r.status, datos)

    def seguir(ruta):
        """Pide una ruta amable, sigue el 302 y devuelve lo que aterriza.

        Comprueba las dos cosas a la vez: que redirija, y que el archivo al que
        redirige exista. Una redirección a una página que no está es un 404 con
        un rodeo.
        """
        r = pedir(ruta)
        if len(r) != 3 or r[0] != 302:
            return (r[0], f'no redirigió: {r[0]}')
        cod, cuerpo = pedir(r[2])[:2]
        return (cod, cuerpo.strip())

    try:
        portada_html = pedir('/')[1]
        ok('la portada responde', pedir('/')[0], 200)
        ok('la portada nombra las tres secciones',
           all(x in portada_html for x in ('/pmo', '/proyectos', '/productos')), True)
        ok('la portada dice de quién es', 'Banco del Selftest' in portada_html, True)

        # Las rutas amables redirigen al archivo: ver el comentario de ALIAS. Se comprueba
        # por contenido y no por igualdad, porque al servirse la página lleva el árbol.
        def llega(ruta, texto):
            cod, cuerpo = seguir(ruta)
            return cod == 200 and texto in cuerpo

        ok('la sección PMO redirige a su archivo', llega('/pmo', '<h1>pmo</h1>'), True)
        ok('el comité redirige a su archivo',
           llega('/decisiones', '<h1>decisiones</h1>'), True)
        ok('el listado de proyectos redirige',
           llega('/proyectos', '<h1>listado de proyectos</h1>'), True)
        ok('el listado de productos redirige',
           llega('/productos', '<h1>listado de productos</h1>'), True)
        ok('un proyecto redirige', llega('/p/PRY-001', '<h1>uno</h1>'), True)
        ok('un producto redirige',
           llega('/producto/cuenta-transaccional', '<h1>la cuenta</h1>'), True)
        ok('el archivo se sirve con su contenido intacto',
           '<h1>listado de proyectos</h1>' in pedir('/proyectos.html')[1], True)

        # Que el menú del servidor y el de las páginas no se separen nunca.
        ok('las secciones son las mismas que las de informe.py',
           sorted(ALIAS[r] for r in ('/pmo', '/proyectos', '/productos')),
           sorted(a for _, _, a in informe.SECCIONES))

        # Lo de arriba lo ve cualquiera. Esto no.
        ok('no se sale de la carpeta con ..', pedir('/p/../../secreto')[0], 404)
        ok('no se sale con una ruta absoluta', pedir('/p//etc/hostname')[0], 404)
        ok('no sirve un archivo que no es del informe', pedir('/p/secreto')[0], 404)
        ok('ni pidiéndolo por su nombre de archivo', pedir('/../secreto.txt')[0], 404)
        ok('un producto que no existe es 404', pedir('/producto/inventado')[0], 404)
        ok('una ruta inventada es 404', pedir('/administrar')[0], 404)
        ok('no acepta POST en otra ruta', pedir('/pmo', 'POST', 'x=1')[0], 404)

        est_json = json.loads(pedir('/estado.json')[1])
        ok('la frescura dice qué proyectos hay', est_json['proyectos'], ['PRY-001'])
        ok('la frescura dice qué productos hay', est_json['productos'],
           ['cuenta-transaccional'])
        ok('la frescura dice de cuándo es el informe',
           est_json['informe_generado'] is not None, True)

        antes = (est / 'records' / 'PRY-001.json').read_text(encoding='utf-8')
        cod, cuerpo = pedir('/peticion', 'POST',
                            urllib.parse.urlencode({'asunto': 'explicar',
                                                    'proyecto': 'PRY-001',
                                                    'de': 'Quien sea',
                                                    'texto': '¿De dónde sale el verde?'}))
        ok('la petición se acepta', cod, 200)
        ok('la petición se confirma en pantalla', 'Queda anotada' in cuerpo, True)
        ok('la petición quedó en la cola', len(pendientes(est)), 1)
        ok('la ficha NO cambió', (est / 'records' / 'PRY-001.json').read_text(encoding='utf-8'), antes)
        ok('la cola vive en su propia carpeta', buzon(est).name, 'peticiones')

        grande = urllib.parse.urlencode({'texto': 'x' * (TOPE_PETICION + 100)})
        ok('una petición enorme se rechaza', pedir('/peticion', 'POST', grande)[0], 413)
        ok('y no entró en la cola', len(pendientes(est)), 1)

        # Que la tabla de rutas y el `if` digan lo mismo. Una ruta declarada y no
        # servida sale en el README como una promesa que devuelve 404.
        vivas = []
        for r in RUTAS:
            if r == '/peticion':
                continue
            prueba = r
            if r.startswith('/p/'):
                prueba = '/p/PRY-001'
            elif r.startswith('/producto/'):
                prueba = '/producto/cuenta-transaccional'
            elif r.startswith('/historia/'):
                # La historia de un caso que el estado de prueba no tiene responde 404 con
                # razón. Lo que se comprueba aquí es que la ruta exista, no que haya datos.
                prueba = '/historia/PRY-001'
            elif r.startswith('/corrida/'):
                prueba = '/corrida/portafolio/-/2026-08-31-sweep-1'
            cod = pedir(prueba)[0]
            if cod in (200, 302):
                vivas.append(r)
        ok('todas las rutas declaradas responden', sorted(vivas),
           sorted(set(RUTAS) - {'/peticion'}))

        # ── la historia
        cod, cuerpo = pedir('/corridas')
        ok('la historia lista las corridas', cod == 200 and '2026-08-31' in cuerpo, True)
        ok('y dice de qué agente es cada una', 'portafolio' in cuerpo, True)
        ok('el filtro por agente deja solo las suyas',
           pedir('/corridas?agente=producto')[1].count('<tr>'), 0)
        ok('y el del portafolio sí las trae',
           pedir('/corridas?agente=portafolio')[1].count('<tr>') >= 2, True)
        # El árbol tiene que estar en TODAS las páginas servidas, no solo en las que el
        # servidor redacta. Si aparece en /corridas y desaparece en /pmo, el lector se
        # queda sin saber dónde está — y es lo primero que se nota.
        ok('el informe servido lleva el árbol',
           'class="arbol"' in pedir('/index.html')[1], True)
        ok('y marca la rama en la que está',
           'class="yo"' in pedir('/index.html')[1], True)
        ok('el archivo en disco sigue sin árbol, para abrirlo sin servidor',
           'class="arbol"' in (inf / 'index.html').read_text(encoding='utf-8'), False)
        ok('el árbol lleva a los tres agentes por el mismo portal',
           all(x in cuerpo for x in ('Samuel', 'Alba', 'agente=proyecto',
                                     'agente=producto')), True)
        ok('el árbol lista cada comando con cuántas corridas dejó',
           'portfolio-scan <b>· 1</b>' in cuerpo and 'portfolio-report <b>· 1</b>' in cuerpo, True)
        ok('y bajo un agente sin corridas lo dice, en vez de callarse',
           'ningún comando ha dejado corrida' in cuerpo, True)
        solo = pedir('/corridas?agente=portafolio&que=portfolio-scan')[1]
        ok('el filtro por comando deja solo las suyas',
           '<td>sweep</td>' in solo and '<td>report</td>' not in solo, True)
        cod, una = pedir('/corrida/portafolio/-/2026-08-31-sweep-1')
        ok('cada corrida tiene su página en el portal',
           cod == 200 and 'la primera' in una and 'Lo que produjo' in una, True)
        ok('y el árbol la lleva como hoja bajo su comando',
           '/corrida/portafolio/-/2026-08-31-sweep-1' in cuerpo, True)
        ok('una corrida que no existe responde 404',
           pedir('/corrida/portafolio/-/2026-01-01-sweep-1')[0], 404)
        ok('ningún marcador del árbol queda sin rellenar',
           '<!--corridas:' in cuerpo or '<!--corridas:' in pedir('/index.html')[1], False)
        ok('y dice cuánto cambió entre una y la siguiente', '-1' in cuerpo, True)
        ok('y nombra lo que se arrastra', 'variance_time' in cuerpo, True)
        ok('con el aviso de que es la historia de lo leído',
           'lo que el agente leyó' in pedir('/corridas')[1], True)
        cod, cuerpo = pedir('/historia/PRY-001')
        ok('la línea de tiempo separa lo abierto de lo resuelto',
           cod == 200 and 'Lo que sigue abierto' in cuerpo
           and 'Lo que se resolvió' in cuerpo, True)
        cod, cuerpo = pedir('/corte?a=2026-08-31&b=2026-09-07')
        ok('el corte muestra el campo que cambió',
           cod == 200 and 'plan.end_date' in cuerpo and '2026-06-30' in cuerpo, True)
        cod, cuerpo = pedir('/corte?a=1999-01-01&b=2026-09-07')
        ok('un corte que no existe lo dice en vez de reventar',
           cod == 404 and 'No hay instantánea del 1999-01-01' in cuerpo, True)

        ok('el escape impide inyectar en la confirmación',
           '<script>' not in pedir('/peticion', 'POST',
                                   urllib.parse.urlencode({'de': '<script>x</script>'}))[1], True)
    finally:
        srv.shutdown(); srv.server_close()

    print()
    if fallas:
        print(f'{len(fallas)} falla(s)')
        return 1
    print('todo pasa')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description='Rostrum — el servidor del informe de Criterio PMO.')
    ap.add_argument('--informe', type=Path, help='carpeta que produjo informe.py')
    ap.add_argument('--estado', type=Path, help='carpeta de estado del agente')
    ap.add_argument('--config', type=Path, default=None,
                    help='para saber de quién es esta oficina de proyectos')
    ap.add_argument('--puerto', type=int, default=8787)
    ap.add_argument('--host', default=None,
                    help='por defecto 127.0.0.1; con --abierto, 0.0.0.0')
    ap.add_argument('--abierto', action='store_true',
                    help='escuchar fuera de este equipo. SIN AUTENTICACIÓN: solo '
                         'detrás del control de acceso de tu organización')
    ap.add_argument('--selftest', action='store_true')
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.informe or not args.estado:
        ap.error('--informe y --estado son obligatorios (o usa --selftest)')
    if not args.estado.exists():
        ap.error(f'no existe la carpeta de estado: {args.estado}')

    host = args.host or ('0.0.0.0' if args.abierto else '127.0.0.1')
    try:
        return arrancar(args.informe, args.estado, host, args.puerto,
                        informe.nombre_organizacion(args.config))
    except OSError as err:
        print(f'No se pudo levantar en {host}:{args.puerto} — {err}', file=sys.stderr)
        if getattr(err, 'errno', None) in (48, 98, 10048):
            print('Ese puerto ya está ocupado. Prueba con --puerto 8788.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
