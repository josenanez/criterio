#!/usr/bin/env python3
"""Criterio — Rostrum, el servidor de todas las familias.

    python3 servidor.py --mapa <carpeta>/.criterio/rostrum/config.json [--puerto 8787]
                        [--host 127.0.0.1] [--abierto]
    python3 servidor.py --informe <carpeta> --estado <estado>      solo la familia PMO
    python3 servidor.py --selftest

Sirve lo que los agentes ya escribieron —el informe de la PMO, los reportes de Clara, Tomás,
Fidel y Constanza, la historia de las corridas— y recibe peticiones para cualquiera de ellos.
Qué agentes hay y dónde está cada estado lo dice el mapa que deja `server-setup` (`mapa.py`);
qué es cada agente, `agentes.json`, que escribe `scripts/familias.py` desde las familias. El
servidor no lleva ningún agente escrito a mano (ADR 0010). Librería estándar, sin dependencias.

**Rostrum no calcula nada y no escribe ninguna ficha.** Es una proyección: lo
que muestra ya estaba escrito en disco antes de que alguien abriera el navegador.
Esa es la razón de que exista como pieza aparte y no como un modo del agente. Un
servidor que calculara al vuelo tendría que leer documentos, y entonces dos
personas abriendo la misma página verían dos portafolios distintos.

Lo único que escribe es la cola de peticiones, en `<estado>/peticiones/` del agente al que
va dirigida. El agente la lee cuando despierta. Nadie del otro lado de la
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
import mapa  # qué agentes hay en la carpeta de trabajo y dónde está cada estado
import portafolio  # la historia la lee él; Rostrum no calcula nada y no escribe nada
import rastro  # la página de una corrida es del arnés
import robots  # todos los de las familias, con los mismos trazos que los README y el portal

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
    '/corridas': 'la historia de todos los agentes · ?agente=, ?que=<comando> y ?caso=<código> para filtrar',
    '/corrida/<agente>/<id>': 'una corrida tal como la dejó el arnés: lo que el agente mostró, con sus cifras',
    '/corrida/<agente>/<caso>/<id>': 'las cifras de una corrida registrada solo por `corrida`',
    '/arrastres': 'lo que se arrastra: señales con varios cortes seguidos y nadie ha decidido',
    '/agente/<agente>': 'qué hace cada agente, función por función, y cada corrida que dejó',
    '/caso/<codigo>': 'todo lo que los agentes han hecho sobre un caso: un proyecto, un producto, un contrato',
    '/familia/<sigla>': 'una familia: cada agente con lo último que escribió y sus reportes',
    '/reporte/<area>/<instancia>/<archivo>': 'un reporte tal como lo escribió el motor del agente',
    '/vence': 'lo que vence: lo que cada motor dejó con fecha y pendiente, de todas las familias',
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
.con-arbol{{display:grid;grid-template-columns:340px minmax(0,1fr);min-height:100vh}}
.arbol{{position:sticky;top:0;max-height:100vh;overflow-y:auto;box-sizing:border-box;
  padding:34px 24px 40px 28px;background:{informe.PANEL_ALTO};
  border-right:1px solid {informe.FILETE};font-size:1rem;line-height:1.45}}
.con-arbol > .hoja{{max-width:1080px;margin:0;padding:48px 56px 96px}}
.arbol .g{{font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;
  color:{informe.ORO};font-weight:700;margin:1.7em 0 .5em}}
.arbol .g:first-child{{margin-top:0}}
.arbol .n{{display:inline-block;min-width:1.6em;padding:0 .45em;margin-left:.35em;border-radius:1em;
  background:{informe.PANEL};color:{informe.CUERPO};font-size:.82rem;font-weight:600;text-align:center;
  letter-spacing:0;text-transform:none}}
.arbol ul{{list-style:none;margin:0;padding:0}}
.arbol li{{margin:.15em 0}}
.arbol a{{display:block;padding:.3em 0;color:{informe.TINTA};border:0;text-decoration:none}}
.arbol a:hover{{color:{informe.ORO}}}
td.exceso{{color:{informe.ERROR};font-weight:700}}
.arbol a.yo{{color:{informe.ORO};font-weight:700}}
.arbol li a{{font-weight:500}}
.arbol li a .d{{display:block;font-weight:400;font-size:.84rem;color:{informe.APAGADO};line-height:1.3}}
td.nw{{white-space:nowrap}}
.menu-caja{{display:none}}
.menu-boton{{display:none}}
@media (max-width:900px){{
  .con-arbol{{display:block}}
  .menu-boton{{display:block;margin:20px 20px 0;padding:12px 16px;border:1px solid {informe.ORO};
    border-radius:8px;color:{informe.ORO};font-weight:700;cursor:pointer;font-size:1rem}}
  .menu-boton::before{{content:"☰  "}}
  .con-arbol > .hoja{{padding:24px 20px 72px}}
  .arbol{{display:none;border-right:0;border-bottom:1px solid {informe.FILETE};background:{informe.PANEL_ALTO};
    max-height:none;padding:12px 20px 24px;position:static;overflow:visible}}
  .menu-caja:checked ~ .arbol{{display:block}}
}}
@media print{{.arbol,.menu-boton{{display:none}}}}
.portada h1{{margin-bottom:.15em}}
.familia{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:26px 0 4px;max-width:720px}}
.familia a{{display:block;text-align:center;color:inherit;border:0;padding:12px 6px 10px;border-radius:10px}}
.familia a:hover{{background:{informe.PANEL_ALTO}}}
.familia a:hover .ln{{stroke:{informe.ORO}}}
.familia svg{{width:100%;max-width:88px;height:auto;display:block;margin:0 auto}}
.familia .n{{display:block;font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:600;
  color:{informe.TINTA};margin-top:.55em}}
.familia .r{{display:block;font-size:.84rem;color:{informe.APAGADO}}}
.agente-cab{{display:flex;gap:22px;align-items:center;margin:4px 0 6px}}
.agente-cab svg{{width:76px;height:auto;flex:0 0 auto}}
.agente-cab .entrada{{margin:0}}
@media (max-width:600px){{.familia{{grid-template-columns:repeat(2,1fr)}}}}
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


def seg(x) -> str:
    """Un tramo de ruta codificado: un caso puede llamarse «tarjeta débito» (ronda 4)."""
    return urllib.parse.quote(str(x), safe='')


def e(x):
    return html.escape(str(x if x is not None else ''))


def pagina(titulo, cuerpo, hoy, nav='', activa=''):
    """La página del informe, con lo que solo el servidor necesita.

    El árbol va **dentro** de la hoja y en un `<nav>` aparte, no sustituyendo al enlace
    de vuelta: una página impresa o abierta desde el disco no tiene servidor que se lo
    sirva, y el informe tiene que seguir leyéndose igual.
    """
    # El pie de `informe.pagina` es el del informe de Vera. Una página que arma el servidor la sirve
    # Rostrum, y lo dice: lo que hay en ella lo escribió el agente que se nombra en la página.
    html_ = informe.pagina(titulo, cuerpo, hoy, nav).replace(
        f'Producido por <strong>Vera</strong>, el agente PMO de Criterio, el {e(hoy)}.',
        f'Servido por <strong>Rostrum</strong>, el portal de Criterio, el {e(hoy)}: lo que hay aquí lo escribió '
        f'el agente que se nombra, y no se recalculó al servirlo.', 1)
    return con_arbol(html_, activa)


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


def celda_paralelo(c: dict) -> str:
    """Cuántos subagentes lanzó la corrida y cuántos a la vez; en rojo si pasó de
    `execution.workers`. Es la medida que evita repetir el día en que un barrido lanzó
    cinco lectores en paralelo y agotó la cuota: lo que se excede se ve en la historia,
    no cuando el plan se acaba."""
    if c.get("subagentes") is None:
        return '<td class="n">—</td>'
    n, a_la_vez = c["subagentes"], c.get("concurrentes")
    texto = "0" if not n else f"{n} · {'¿?' if a_la_vez is None else a_la_vez} a la vez"
    if c.get("exceso"):
        return (f'<td class="n exceso" title="la configuración permite {c.get("workers")} a la vez">'
                f'{e(texto)}</td>')
    return f'<td class="n">{e(texto)}</td>'


def corridas(todas: list, h: dict, hoy: str, agente: str = '', que: str = '',
             caso: str = '') -> str:
    """Nivel 1 · la historia de las corridas de los tres agentes, de las dos fuentes.

    Cada fila dice de quién es, qué comando, sobre qué caso, cuánto tardó y qué encontró,
    y abre la página de esa corrida. Sin eso, una lista que mezcla el portafolio con
    sesenta y cinco productos no se puede leer — y separarla en tres portales sería peor.
    """
    lista = [c for c in todas
             if (not agente or c["agente"] == agente)
             and (not que or c["comando"] == que)
             and (not caso or c.get("caso") == caso)]
    activa = f'/corridas?agente={agente}&que={que}' if agente and que else '/corridas'
    if not lista:
        return pagina('Historia', '<div class="bloque"><p>Todavía no hay corridas '
                      'registradas con ese filtro. Cada comando que corre deja la suya.</p></div>',
                      hoy, nav(), activa)
    filas = []
    for c in lista:
        filas.append(
            f'<tr><td class="nw"><a href="{e(c["ruta"])}">{e((c.get("inicio") or c.get("fecha") or "").replace("T", " ")[:16])}</a></td>'
            f'<td><a href="/agente/{e(c["agente"])}">{e(NOMBRE.get(c["agente"], c["agente"]))}</a></td>'
            f'<td>{e(etiqueta(c["comando"]))}<br><code>{e(c["comando"])}</code></td>'
            f'<td class="nw">{"<a href=" + chr(34) + "/caso/" + e(seg(c["caso"])) + chr(34) + ">" + e(c["caso"]) + "</a>" if c.get("caso") else "—"}</td>'
            f'<td class="n">{e(c.get("documentos") or "—")}</td>'
            f'<td class="n">{e(c.get("segundos") if c.get("segundos") is not None else "—")}</td>'
            f'<td class="n">{e(c.get("hallazgos") if c.get("hallazgos") is not None else "—")}</td>'
            + celda_paralelo(c) +
            f'<td>{"sí" if c.get("salida") else "<em>no</em>"}</td>'
            f'<td class="nw">{"arnés" if c["fuente"] == "arnés" else "solo cifras"}</td></tr>')
    cuerpo = [
        f'<p class="entrada"><b>{len(lista)} corridas</b>'
        + (f' de <code>{e(que)}</code>' if que else '')
        + (f' sobre <b>{e(caso)}</b>' if caso else '')
        + (f' de {e(NOMBRE.get(agente, agente))}' if agente else
           ' de los tres agentes')
        + f', de la del {e(lista[0]["fecha"])} a la del {e(lista[-1]["fecha"])}. Ninguna se '
        f'borra: el rastro de las corridas es la memoria del proyecto, y sin él no se puede '
        f'sostener que algo lleva meses sin resolverse.</p>',
        '<div class="bloque"><table><thead><tr><th>Inicio</th><th>Agente</th>'
        '<th>Comando</th><th>Caso</th><th>Docs</th><th>Seg</th><th>Hallazgos</th>'
        '<th title="subagentes que lanzó, y cuántos a la vez">Paralelo</th>'
        '<th>Salida</th><th>Fuente</th></tr></thead><tbody>',
        "".join(filas), '</tbody></table></div>']

    cuerpo.append('<p class="entrada">Lo que lleva varios cortes sin resolverse está aparte, '
                  'en <a href="/arrastres">lo que se arrastra</a>.</p>')

    if len(h["instantaneas"]) > 1:
        a, b = h["instantaneas"][-2], h["instantaneas"][-1]
        cuerpo.append(f'<p class="entrada">Para ver qué cambió campo por campo entre dos '
                      f'cortes: <a href="/corte?a={a}&b={b}">{a} → {b}</a>.</p>')
    cuerpo.append(AVISO_HISTORIA)
    return pagina('Historia de las corridas', "".join(cuerpo), hoy, nav(), activa)


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
            out.append(f'<tr><td>{e(informe.NOMBRES.get(s, s))}</td><td>{e(x["primera"])}</td>'
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
        # La ficha de hoy pone nombre a cada elemento de lista: «el proveedor «X»».
        try:
            rec = json.loads((estado / 'records' / f'{codigo}.json').read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError):
            rec = {}
        for campo in sorted(set(va) | set(vb)):
            x, y = va.get(campo), vb.get(campo)
            if x != y:
                filas.append(f'<tr><td><a href="/historia/{e(seg(codigo))}">{e(codigo)}</a></td>'
                             f'<td>{e(informe.nombre_campo(rec, campo))}</td>'
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


md_a_html = rastro.md_a_html


def vista_corrida(entradas: list, agente: str, sobre: str, ident: str, hoy: str) -> tuple:
    """Una corrida, entera: las cifras que midió y lo que el comando produjo."""
    for x in entradas:
        quien, cual, d = x["area"], x.get("instancia"), x.get("_estado")
        if d is None:
            continue
        # El caso de la ruta es el del comando (`--caso PRY-200`), que no siempre es el
        # nombre de la carpeta del estado; lo que identifica la corrida es su archivo.
        if quien != agente or ((cual or '-') != sobre and not (d / 'corridas' / f'{ident}.md').is_file()):
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
    '<p class="entrada">Esta es la historia de <b>lo que el agente procesó de los documentos</b>, '
    'no de lo que pasó ni un juicio sobre nadie. Cada hallazgo remite al documento que lo '
    'sostiene, y un documento que se archivó tarde cambia la lectura sin que nadie haya '
    'hecho nada mal.</p>')


# El árbol de la izquierda. No es decoración: si un patrocinador tiene que preguntarle a
# alguien dónde está el histórico, el histórico no es transparente. Y lo que **no** está
# construido aparece marcado en vez de omitido, porque un menú que esconde los huecos
# promete un producto que no existe.
# ---------------------------------------------------------------- el árbol
#
# Rostrum es **uno** para los tres agentes, y el árbol es la estructura completa de la
# PMO: cada agente con sus funciones agrupadas, cada función con sus comandos, cada
# comando con cada corrida que dejó, y aparte lo mismo visto por proyecto y por producto.
# Un comando que no ha corrido aparece igual, en gris: que no haya corrido también es un
# dato, y un árbol que solo muestra lo que existe no deja ver lo que falta.
#
# Las corridas salen del disco, no de una lista que alguien mantiene: del índice que el
# arnés escribe en `.criterio/corridas/<agente>/` (una entrada por invocación de comando,
# con la página de lo que el agente mostró) y de los `corridas.json` de los estados (las
# cifras que `corrida` midió). Lo que está en disco se ve; lo que no, no.

# Los agentes salen de `agentes.json`, que escribe `scripts/familias.py` desde las familias: aquí no
# se escribe ningún nombre. La clave de cada uno es su área, la carpeta de su configuración.
REGISTRO = mapa.registro()
AGENTES = {a["area"]: a for a in REGISTRO["agentes"]}
PLUGIN = {k: a["plugin"] for k, a in AGENTES.items()}
NOMBRE = {k: a["nombre"] for k, a in AGENTES.items()}
TITULO = {k: f'{a["nombre"]} · {a["titulo"]}' for k, a in AGENTES.items()}
ROBOT_DE = {k: a["id"] for k, a in AGENTES.items()}
FAMILIA_DE = {k: a["familia"] for k, a in AGENTES.items()}
FAMILIAS = {f["sigla"]: f for f in REGISTRO["familias"]}
GRUPOS = {k: [(g["titulo"], g["linea"], [c["id"] for c in g["comandos"]]) for g in a["grupos"]]
          for k, a in AGENTES.items()}
ETIQUETA = {c["id"]: c["etiqueta"] for a in REGISTRO["agentes"] + [REGISTRO["servidor"]]
            for g in a["grupos"] for c in g["comandos"]}


def etiqueta(cmd: str) -> str:
    return ETIQUETA.get(cmd, cmd)


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


def entradas_legado(informe_dir: Path, estado: Path) -> list:
    """Sin mapa, la familia PMO como se servía antes: el estado de Vera, el informe que produjo y
    los estados de Samuel y Alba que estén junto a él. Es lo que levanta quien solo tiene la PMO."""
    out = [{"id": "portafolio", "area": "portafolio", "instancia": None, "nombre": None,
            "_estado": estado, "_informe": informe_dir, "_config": None}]
    for quien, cual, d in portafolio.estados_de(estado)[1:]:
        out.append({"id": f"{quien}/{cual}", "area": quien, "instancia": cual, "nombre": cual,
                    "_estado": d, "_informe": None, "_config": None})
    return out


def comandos_si_comparte(area: str) -> set | None:
    """Los comandos de un agente que comparte su estado con otro de su familia —Clara y Tomás,
    Fidel y Constanza—, para que cada uno vea sus corridas y no las del vecino. `None` si el
    estado es solo suyo, como en la familia PMO."""
    a = AGENTES.get(area) or {}
    if not a.get("ambitos"):
        return None
    return {c["id"] for g in a["grupos"] for c in g["comandos"]}


def historia(entradas: list) -> dict:
    """Las corridas de todos los agentes del mapa en una sola línea de tiempo, y de cada caso
    desde cuándo arrastra cada señal. Todos escriben su historia con el mismo esquema, así que se
    lee igual sin importar la familia (ADR 0010)."""
    corridas, casos, instantaneas = [], {}, []
    for x in entradas:
        d = x.get("_estado")
        if d is None or not d.is_dir():
            continue
        try:
            h = portafolio._historia_de(d, comandos_si_comparte(x["area"]))
        except Exception:  # un estado a medio escribir no tumba el portal
            continue
        for c in h["corridas"]:
            corridas.append(dict(c, agente=x["area"], sobre=c.get("caso") or x.get("instancia")))
        for codigo, senales in h["casos"].items():
            destino = casos.setdefault(codigo, {})
            for s, v in senales.items():
                # El mismo caso visto por dos agentes: se queda la racha más larga, que es la
                # que un comité necesita; el problema no empieza de nuevo porque lo mire otro.
                if s not in destino or v["seguidas"] > destino[s]["seguidas"]:
                    destino[s] = dict(v, agente=x["area"])
        if x["area"] == "portafolio":
            instantaneas += h["instantaneas"]
    corridas.sort(key=lambda c: (c.get("fecha") or "", c.get("agente") or ""))
    return {"corridas": corridas, "casos": casos, "total": len(corridas),
            "desde": corridas[0]["fecha"] if corridas else None,
            "hasta": corridas[-1]["fecha"] if corridas else None,
            "instantaneas": sorted(set(instantaneas)),
            "agentes": sorted({c["agente"] for c in corridas})}


def indice(evidencia: Path, entradas: list) -> list:
    """Todas las corridas que hay en disco, de las dos fuentes, en una sola lista.

    Del arnés: `.criterio/corridas/<agente>/corridas.json`, una por invocación, con la
    página de lo que el agente mostró. De los estados: las cifras que `corrida` midió;
    las que el arnés ya incrustó en una página no se repiten, las demás se listan solas,
    porque son corridas anteriores al rastro o hechas sin él.
    """
    corridas, cubiertas = [], set()
    for agente in PLUGIN:
        f = evidencia / agente / "corridas.json"
        if not f.is_file():
            continue
        try:
            entradas = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for x in entradas:
            medidas = x.get("medidas") or []
            for m in medidas:
                if m.get("id"):
                    cubiertas.add((agente, m["id"]))
            corridas.append({
                "fuente": "arnés", "id": x["id"], "agente": agente,
                "comando": x.get("comando"), "caso": x.get("caso"), "fecha": x.get("fecha"),
                "inicio": x.get("inicio"), "fin": x.get("fin"),
                "segundos": x.get("segundos"), "salida": bool(x.get("salida")),
                "subagentes": x.get("subagentes"), "concurrentes": x.get("concurrentes"),
                "workers": x.get("workers"), "exceso": bool(x.get("exceso")),
                "hallazgos": sum((m.get("hallazgos") or 0) for m in medidas) if medidas else None,
                "documentos": next((m.get("documentos") for m in medidas if m.get("documentos")), None),
                "medidas": len(medidas),
                "ruta": f"/corrida/{agente}/{x['id']}",
                "orden": x.get("inicio") or x.get("fecha") or "",
            })
    h = historia(entradas)
    for c in h["corridas"]:
        agente = c.get("agente") or "portafolio"
        if c.get("id") and (agente, c["id"]) in cubiertas:
            continue
        ident = c.get("id") or f'{c["fecha"]}-{c["que"]}'
        corridas.append({
            "fuente": "estado", "id": ident, "agente": agente,
            "comando": comando_de(agente, c["que"]), "caso": c.get("sobre"),
            "fecha": c.get("fecha"), "inicio": c.get("fecha"), "fin": None,
            "segundos": c.get("segundos"), "salida": bool(c.get("salida")),
            "subagentes": None, "concurrentes": None, "workers": None, "exceso": False,
            "hallazgos": c.get("hallazgos"), "documentos": c.get("documentos"),
            "medidas": 1,
            # «tarjeta débito» es un caso válido; en la ruta va codificado (ronda 4, cooperativas).
            "ruta": f'/corrida/{agente}/{seg(c.get("sobre") or "-")}/{ident}',
            "orden": c.get("fecha") or "",
        })
    corridas.sort(key=lambda c: (c["orden"], c["agente"], c["id"]))
    return corridas


def familias_de(entradas: list) -> list:
    """Las familias que tienen al menos un agente en el mapa, en su orden."""
    presentes = {FAMILIA_DE[x["area"]] for x in entradas if x["area"] in FAMILIA_DE}
    return [s for s in FAMILIAS if s in presentes]


def areas_de(entradas: list) -> list:
    """Los agentes de las familias del mapa, en su orden. Una familia se ve entera aunque falte uno
    de sus agentes: su página dice qué hace y que no ha corrido, que también es un dato."""
    fams = set(familias_de(entradas))
    return [k for k in AGENTES if FAMILIA_DE[k] in fams]


def arbol(corridas: list, activa: str = "", entradas: list | None = None) -> str:
    """El menú: corto, en el orden en que alguien entra. El portafolio si está la PMO, las otras
    familias y lo que vence si están, la historia, los agentes del mapa y preguntar. El catálogo de
    funciones vive en la página de cada agente, y un proyecto, un producto o un contrato se abre
    desde su listado: con cincuenta no caben en una columna."""
    def li(ruta, texto, nota="", n=None):
        yo = ' class="yo"' if ruta == activa else ''
        cuenta = f' <span class="n">{n}</span>' if n is not None else ''
        return (f'<li><a href="{e(ruta)}"{yo}>{e(texto)}{cuenta}'
                + (f'<span class="d">{e(nota)}</span>' if nota else '') + '</a></li>')
    entradas = entradas or []
    areas = areas_de(entradas)
    otras = [s for s in familias_de(entradas) if s != "pmo"]
    por_agente = {a: sum(1 for c in corridas if c["agente"] == a) for a in areas}
    out = ['<input type="checkbox" id="menu" class="menu-caja">',
           '<label for="menu" class="menu-boton">Menú</label>',
           '<nav class="arbol" aria-label="Menú">']
    if "portafolio" in areas:
        out += ['<p class="g">Portafolio</p><ul>',
                li('/pmo', 'Cómo va el portafolio', 'el informe: cifras, silencio, contradicciones'),
                li('/decisiones', 'Lo que necesita una decisión', 'el material del comité'),
                li('/proyectos', 'Proyectos', 'uno por uno'),
                li('/productos', 'Productos', 'y los proyectos que los construyen'),
                '</ul>']
    if otras:
        out.append('<p class="g">Las familias</p><ul>')
        for s in otras:
            out.append(li(f'/familia/{s}', FAMILIAS[s]["nombre"]["es"],
                          ' y '.join(NOMBRE[a] for a in FAMILIAS[s]["agentes"] if a in areas)))
        out += [li('/vence', 'Lo que vence', 'lo pendiente con fecha, de todas'), '</ul>']
    out += ['<p class="g">Historia</p><ul>',
            li('/corridas', 'Todas las corridas', 'qué corrió, cuándo, qué encontró', len(corridas)),
            li('/arrastres', 'Lo que se arrastra', 'señales con varios cortes seguidos')]
    if "portafolio" in areas:
        out.append(li('/corte', 'Qué cambió entre dos cortes'))
    out.append('</ul><p class="g">Los agentes</p><ul>')
    for a in areas:
        out.append(li(f'/agente/{a}', TITULO[a], '', por_agente[a]))
    out += ['</ul><p class="g">Preguntar</p><ul>',
            li('/#preguntar', 'Dejar una pregunta a un agente'),
            '</ul></nav>']
    return "".join(out)


def con_arbol(pagina_html: str, activa: str = "") -> str:
    """Deja en la página el sitio del árbol; el servidor lo rellena al servir, porque el
    árbol depende de lo que haya en disco en ese momento."""
    if 'class="arbol"' in pagina_html or '<div class="hoja">' not in pagina_html:
        return pagina_html
    return (pagina_html
            .replace('</style>', EXTRA + '</style>', 1)
            .replace('<div class="hoja">',
                     f'<div class="con-arbol"><!--ARBOL {activa} --><div class="hoja">', 1)
            .replace('</div></body></html>', '</div></div></body></html>', 1))


def rellenar_arbol(pagina_html: str, corridas: list, entradas: list | None = None) -> str:
    m = re.search(r'<!--ARBOL (.*?) -->', pagina_html)
    if not m:
        return pagina_html
    return pagina_html.replace(m.group(0), arbol(corridas, m.group(1).strip(), entradas), 1)


def arrastres(h: dict, hoy: str) -> str:
    """Lo que lleva varios cortes sin resolverse: la lista con la que se arma un comité."""
    filas = []
    for codigo, senales in h["casos"].items():
        for sig, x in senales.items():
            if x["seguidas"] >= 2 and not x.get("resuelta_en"):
                filas.append((x["seguidas"], codigo, sig, x["primera"]))
    filas.sort(reverse=True)
    cuerpo = ['<p class="entrada">Una señal que sonó una vez es ruido. Una que lleva varios '
              'cortes seguidos es una decisión que nadie ha tomado. Esta es la lista, de la más '
              'vieja a la más nueva.</p>']
    if not filas:
        cuerpo.append('<div class="bloque"><p>Nada lleva dos cortes seguidos todavía: hace falta '
                      'más de una corrida para que algo se arrastre.</p></div>')
    else:
        cuerpo += ['<div class="bloque"><table><thead><tr><th>Caso</th><th>Señal</th>'
                   '<th>Cortes seguidos</th><th>Desde</th></tr></thead><tbody>']
        for n_, codigo, sig, desde in filas[:200]:
            cuerpo.append(f'<tr><td><a href="/caso/{e(seg(codigo))}">{e(codigo)}</a></td>'
                          f'<td>{e(informe.NOMBRES.get(sig, sig))}</td><td class="n">{n_}</td>'
                          f'<td>{e(desde)}</td></tr>')
        cuerpo.append('</tbody></table></div>')
    cuerpo.append(AVISO_HISTORIA)
    return pagina('Lo que se arrastra', "".join(cuerpo), hoy, nav(), '/arrastres')


def vista_agente(todas: list, agente: str, hoy: str, entradas: list | None = None) -> tuple:
    """Qué hace un agente, función por función, y cada corrida que dejó.

    Es el catálogo que antes estorbaba en el menú: aquí es lo que alguien busca cuando
    quiere saber qué hizo el agente, con el nombre de cada comando explicado.
    """
    if agente not in GRUPOS:
        return 404, error(404, f'No hay agente {agente}', hoy)
    por = {}
    for c in todas:
        if c["agente"] == agente:
            por.setdefault(c["comando"], []).append(c)
    total = sum(len(v) for v in por.values())
    cuerpo = [f'<div class="agente-cab">{robots.svg(ROBOT_DE[agente], informe.TINTA, informe.ORO)}'
              f'<p class="entrada"><b>{e(NOMBRE[agente])}</b>, {e(TITULO[agente].split(" · ")[1])}, '
              f'de la familia {e(FAMILIAS[FAMILIA_DE[agente]]["nombre"]["es"].lower())}: '
              f'{len(sum((c for _, _, c in GRUPOS[agente]), []))} funciones en '
              f'{len(GRUPOS[agente])} grupos, <b>{total} corridas</b> registradas. Un comando sin '
              f'corridas no ha corrido; que no haya corrido también es un dato.</p></div>']
    for grupo, que_es, cmds in GRUPOS[agente]:
        cuerpo.append(f'<h2>{e(grupo)}</h2><p class="entrada">{e(que_es)}</p>'
                      '<div class="bloque"><table><thead><tr><th>Función</th><th>Comando</th>'
                      '<th>Corridas</th><th>Última</th></tr></thead><tbody>')
        for cmd in cmds:
            suyas = por.get(cmd, [])
            ultima = suyas[-1] if suyas else None
            cuerpo.append(
                f'<tr><td>{e(etiqueta(cmd))}</td><td><code>/{e(PLUGIN[agente])}:{e(cmd)}</code></td>'
                f'<td class="n"><a href="/corridas?agente={e(agente)}&amp;que={e(cmd)}">{len(suyas)}</a></td>'
                f'<td>{"<a href=" + chr(34) + e(ultima["ruta"]) + chr(34) + ">" + e((ultima.get("inicio") or ultima.get("fecha") or "").replace("T", " ")[:16]) + "</a>" if ultima else "—"}</td></tr>')
        cuerpo.append('</tbody></table></div>')
    # Los reportes que dejó su motor, de cada instancia del mapa. Los de la PMO son su informe.
    for x in [x for x in (entradas or []) if x['area'] == agente and agente != 'portafolio']:
        reps = reportes_de(x)
        if not reps:
            continue
        cuerpo.append('<h2>Sus reportes' + (f' · {e(x["nombre"])}' if x.get('nombre') else '') + '</h2>'
                      '<div class="bloque"><table><thead><tr><th>Reporte</th><th>Archivo</th><th>Escrito</th>'
                      '</tr></thead><tbody>')
        for rp in reps:
            cuerpo.append(f'<tr><td><a href="{e(ruta_reporte(x, rp["ruta"]))}">{e(ETIQUETA.get(rp["comando"], rp["comando"]))}</a></td>'
                          f'<td><code>{e(rp["ruta"])}</code></td><td class="nw">{e(rp["escrito"])}</td></tr>')
        cuerpo.append('</tbody></table></div>')
    cuerpo.append(AVISO_HISTORIA)
    return 200, pagina(f'{NOMBRE[agente]} · {TITULO[agente].split(" · ")[1]}', "".join(cuerpo), hoy,
                       nav(), f'/agente/{agente}')


def vista_caso(todas: list, h: dict, informe_dir: Path, codigo: str, hoy: str) -> tuple:
    """Todo lo que los tres agentes han hecho sobre un proyecto o un producto."""
    suyas = [c for c in todas if c.get("caso") == codigo]
    senales = h["casos"].get(codigo) or {}
    if not suyas and not senales and not (informe_dir / f'{codigo}.html').is_file():
        return 404, error(404, f'No hay nada sobre {codigo}', hoy)
    es_producto = codigo.upper().startswith("PRD")
    enlaces = []
    if (informe_dir / f'{codigo}.html').is_file():
        enlaces.append(f'<a href="/p/{e(codigo)}">su informe de hoy</a>')
    if senales:
        enlaces.append(f'<a href="/historia/{e(seg(codigo))}">desde cuándo arrastra cada señal</a>')
    cuerpo = [f'<p class="entrada"><b>{e(codigo)}</b>: {len(suyas)} corridas de los agentes sobre '
              f'este {"producto" if es_producto else "proyecto"}'
              + (' · ' + ' · '.join(enlaces) if enlaces else '') + '.</p>']
    if suyas:
        cuerpo += ['<div class="bloque"><table><thead><tr><th>Inicio</th><th>Agente</th>'
                   '<th>Función</th><th>Seg</th><th>Hallazgos</th><th>Paralelo</th><th>Salida</th></tr></thead><tbody>']
        for c in suyas:
            cuerpo.append(
                f'<tr><td class="nw"><a href="{e(c["ruta"])}">{e((c.get("inicio") or c.get("fecha") or "").replace("T", " ")[:16])}</a></td>'
                f'<td><a href="/agente/{e(c["agente"])}">{e(NOMBRE.get(c["agente"], c["agente"]))}</a></td>'
                f'<td>{e(etiqueta(c["comando"]))}</td>'
                f'<td class="n">{e(c.get("segundos") if c.get("segundos") is not None else "—")}</td>'
                f'<td class="n">{e(c.get("hallazgos") if c.get("hallazgos") is not None else "—")}</td>'
                + celda_paralelo(c) +
                f'<td>{"sí" if c.get("salida") else "<em>no</em>"}</td></tr>')
        cuerpo.append('</tbody></table></div>')
    else:
        cuerpo.append('<div class="bloque"><p>Ningún comando ha corrido sobre este caso en '
                      'particular; lo que sigue viene de las corridas que lo procesaron junto con '
                      'otros, y cada señal dice de qué agente es.</p></div>')
    if senales:
        abiertas = sorted((x["seguidas"], sig, x["primera"], x.get("agente")) for sig, x in senales.items()
                          if not x.get("resuelta_en"))
        if abiertas:
            cuerpo += ['<h2>Lo que sigue abierto</h2>',
                       '<div class="bloque"><table><thead><tr><th>Señal</th><th>Agente</th><th>Desde</th>'
                       '<th>Cortes seguidos</th></tr></thead><tbody>']
            for n_, sig, desde, quien_ in sorted(abiertas, reverse=True, key=lambda z: (z[0], z[1])):
                nombre_s = informe.NOMBRES.get(sig)
                cuerpo.append(f'<tr><td>{e(nombre_s) if nombre_s else "<code>" + e(sig) + "</code>"}</td>'
                              f'<td>{"<a href=" + chr(34) + "/agente/" + e(quien_) + chr(34) + ">" + e(NOMBRE.get(quien_, quien_)) + "</a>" if quien_ else "—"}</td>'
                              f'<td>{e(desde)}</td><td class="n">{n_}</td></tr>')
            cuerpo.append('</tbody></table></div>')
    cuerpo.append(AVISO_HISTORIA)
    return 200, pagina(f'{codigo}', "".join(cuerpo), hoy, nav(), '/corridas')


def vista_rastro(evidencia: Path, agente: str, ident: str, hoy: str) -> tuple:
    """La página de una corrida que dejó el arnés, servida con el árbol encima."""
    f = evidencia / agente / f"{ident}.html"
    if agente not in PLUGIN or not SEGURO.match(ident) or not f.is_file():
        return 404, error(404, f'No hay corrida {ident} de {agente}', hoy)
    que = re.sub(r"-\d+$", "", ident[11:])
    return 200, con_arbol(f.read_text(encoding="utf-8"), f'/corridas?agente={agente}&que={que}')


def nav() -> str:
    return '<a href="/">Portada</a> · <a href="/corridas">Historia</a>'



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
        'para': (datos.get('para') or '').strip()[:80] or None,
        'agente': (datos.get('agente') or '').strip()[:40] or None,
        'de': (datos.get('de') or '').strip()[:80] or None,
        'texto': (datos.get('texto') or '').strip()[:4000],
        'respondida': None,
    }
    (carpeta / f"{registro['id']}.json").write_text(
        json.dumps(registro, ensure_ascii=False, indent=2), encoding='utf-8')
    return registro


def pendientes(estado: Path, agente: str | None = None) -> list:
    """Las peticiones sin responder de un estado; con `agente`, solo las suyas, porque dos agentes
    de una familia pueden compartir el estado."""
    salida = []
    for f in sorted(buzon(estado).glob('*.json')):
        try:
            r = json.loads(f.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            continue
        if not r.get('respondida') and (agente is None or r.get('agente') in (None, agente)):
            salida.append(r)
    return salida


# ---------------------------------------------------------------- frescura

def frescura(informe_dir: Path, estado: Path, entradas: list | None = None) -> dict:
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
    entradas = entradas if entradas is not None else [{"id": "portafolio", "area": "portafolio", "_estado": estado}]
    agentes = []
    for x in entradas:
        ultimo = resultados_de(x)
        agentes.append({'id': x['id'], 'agente': NOMBRE.get(x['area'], x['area']),
                        'ultimo': max((r['escrito'] for r in ultimo), default=None),
                        'peticiones': len(pendientes(x['_estado'], ROBOT_DE.get(x['area']))) if x.get('_estado') else 0})
    return {'informe_generado': generado, 'proxima_corrida': proximo,
            'proyectos': paginas, 'productos': productos,
            'peticiones_abiertas': sum(a['peticiones'] for a in agentes),
            'agentes': agentes}


# ------------------------------------------------------- lo que escriben los motores
#
# Las familias CFO y CLO no producen un informe HTML: su motor escribe `resultados.json` y un
# `reporte-<comando>.md` por comando, donde le toca. Rostrum los encuentra en el estado de cada
# entrada del mapa y los muestra tal cual. No los recalcula: la fecha de cada uno es la del motor.

def resultados_de(x: dict) -> list:
    """El `resultados.json` más reciente de cada ámbito del estado —el cierre, el presupuesto, los
    contratos, el cumplimiento—, con lo que el motor escribió y cuándo."""
    d = x.get('_estado')
    if d is None or not d.is_dir():
        return []
    por_ambito = {}
    suyos = set((AGENTES.get(x['area']) or {}).get('ambitos') or [])
    for f in d.rglob('resultados.json'):
        rel = f.relative_to(d)
        if rel.parts[0] in ('corridas', 'peticiones', 'cache') or (suyos and rel.parts[0] not in suyos):
            continue
        ambito = rel.parts[0]
        if ambito not in por_ambito or f.stat().st_mtime > por_ambito[ambito].stat().st_mtime:
            por_ambito[ambito] = f
    out = []
    for ambito, f in sorted(por_ambito.items()):
        try:
            datos = json.loads(f.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError):
            continue
        out.append({'ambito': ambito, 'ruta': f.relative_to(d).as_posix(), 'datos': datos,
                    'escrito': dt.datetime.fromtimestamp(f.stat().st_mtime, dt.timezone.utc).isoformat(timespec='seconds')})
    return out


def reportes_de(x: dict) -> list:
    """Los reportes que el motor dejó en el estado, del más nuevo al más viejo."""
    d = x.get('_estado')
    if d is None or not d.is_dir():
        return []
    suyos = set((AGENTES.get(x['area']) or {}).get('ambitos') or [])
    fs = [f for f in d.rglob('reporte-*.md') if f.relative_to(d).parts[0] not in ('corridas', 'peticiones', 'cache')
          and (not suyos or f.relative_to(d).parts[0] in suyos)]
    return [{'ruta': f.relative_to(d).as_posix(), 'comando': f.stem[len('reporte-'):],
             'escrito': dt.datetime.fromtimestamp(f.stat().st_mtime, dt.timezone.utc).isoformat(timespec='seconds')[:16].replace('T', ' ')}
            for f in sorted(fs, key=lambda f: (-f.stat().st_mtime, str(f)))]


def ruta_reporte(x: dict, rel: str) -> str:
    return f"/reporte/{seg(x['area'])}/{seg(x.get('instancia') or '-')}/" + "/".join(seg(s) for s in rel.split("/"))


def quien(x: dict) -> str:
    """El agente y su instancia, como se nombran en una tabla: «Clara · Banco Andino»."""
    n = NOMBRE.get(x['area'], x['area'])
    return f"{n} · {x['nombre']}" if x.get('nombre') else n


def edad(iso, ahora=None):
    if not iso:
        return None
    ahora = ahora or dt.datetime.now(dt.timezone.utc)
    try:
        return (ahora - dt.datetime.fromisoformat(iso)).days
    except ValueError:
        return None


# ---------------------------------------------------------------- las páginas

def familia(entradas: list | None = None) -> str:
    """Los agentes del mapa y Rostrum, cada uno llevando a lo suyo: los agentes a su página,
    Rostrum a la historia de las corridas. Es la misma fila que abre el README de cada familia."""
    areas = areas_de(entradas or [])
    filas = []
    for a in areas:
        filas.append(f'<a href="/agente/{e(a)}">{robots.svg(ROBOT_DE[a], informe.TINTA, informe.ORO)}'
                     f'<span class="n">{e(NOMBRE[a])}</span><span class="r">{e(AGENTES[a]["rol"]["es"])}</span></a>')
    filas.append(f'<a href="/corridas">{robots.svg("rostrum", informe.TINTA, informe.ORO)}'
                 f'<span class="n">Rostrum</span><span class="r">Las corridas</span></a>')
    return '<nav class="familia" aria-label="Los agentes">' + "".join(filas) + "</nav>"


def portada(fr: dict, hoy: str, org: str = '', entradas: list | None = None) -> str:
    entradas = entradas if entradas is not None else [{"id": "portafolio", "area": "portafolio"}]
    areas = areas_de(entradas)
    con_pmo = "portafolio" in areas
    otras = [s for s in familias_de(entradas) if s != "pmo"]
    dias = edad(fr.get('informe_generado'))
    if not con_pmo:
        sello = ('Cada familia dice en su página de cuándo es lo que se ve. Nada se recalcula al '
                 'abrir el portal: lo que se sirve es lo que el motor de cada agente ya escribió.')
    elif fr.get('informe_generado') is None:
        sello = ('<strong>Todavía no hay informe de la PMO.</strong> Alguien tiene que correr '
                 '<code>/portfolio-report html</code> antes de que el portafolio muestre algo.')
    elif dias and dias > 7:
        sello = (f"El informe de la PMO que se sirve aquí se produjo hace "
                 f"<strong>{informe.plural(dias, 'día', 'días')}</strong>. "
                 f"No se recalcula al abrir esta página: lo que ves es de esa fecha.")
    else:
        sello = (f"El informe de la PMO que se sirve aquí se produjo "
                 f"{'hoy' if not dias else 'hace ' + informe.plural(dias, 'día', 'días')}. "
                 f"No se recalcula al abrir esta página.")
    prox = fr.get('proxima_corrida')
    if prox and con_pmo:
        sello += f" La próxima corrida de Vera es el <strong>{e(prox)}</strong>."

    abiertas = fr.get('peticiones_abiertas') or 0
    cola = ''
    if abiertas:
        cola = (f'<p class="aviso">Hay {informe.plural(abiertas, "petición sin responder", "peticiones sin responder")}. '
                f'Cada agente toma las suyas en su próxima corrida.</p>')

    n_proy = len(fr.get('proyectos') or [])
    n_prod = len(fr.get('productos') or [])
    opciones = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in ASUNTOS.items())
    destinos = ''.join(f'<option value="{e(x["id"])}">{e(quien(x))}</option>'
                       for x in sorted(entradas, key=lambda x: (list(AGENTES).index(x["area"]) if x["area"] in AGENTES else 99, x["id"]))
                       if x.get("_estado") is not None)

    # Las secciones, en el orden en que alguien las necesita: cómo va todo, después el proyecto
    # que le toca, después el producto que le importa; luego cada familia que trabaja aquí.
    puertas = []
    if con_pmo:
        puertas += [
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
    for s in otras:
        f = FAMILIAS[s]
        suyos = [a for a in f["agentes"] if a in areas]
        puertas.append((s.upper(), f'/familia/{s}', f["nombre"]["es"],
                        ' y '.join(e(NOMBRE[a]) for a in suyos) + ': lo último que escribió cada uno, sus '
                        'señales abiertas y sus reportes, tal como los dejó el motor.'))
    if otras:
        puertas.append(('Lo que vence', '/vence', 'Lo pendiente que tiene fecha',
                        'Vencimientos de contratos, obligaciones de cumplimiento, tareas del cierre: lo que '
                        'cada motor dejó con fecha y sin cumplir, de todas las familias, en una sola lista.'))
    tarjetas = ''.join(f"""<a class="puerta" href="{ruta}">
    <span class="q">{e(q)}</span><span class="t">{e(titulo)}</span>
    <p class="d">{desc}</p></a>""" for q, ruta, titulo, desc in puertas)
    comite = ('<p class="aviso">El comité tiene su propia vista, que no es ninguna de estas recortada: '
              '<a href="/decisiones">lo que necesita una decisión</a>, como pregunta cerrada y con la '
              'consecuencia de no decidirlo.</p>') if con_pmo else ''
    titulo_portada = 'Oficina de proyectos' if areas == [a for a in areas if FAMILIA_DE[a] == 'pmo'] else 'Lo que los agentes ya escribieron'

    cuerpo = f"""<div class="portada">
<span class="ante">{e(org) if org else ('Portafolio de proyectos' if con_pmo else 'Criterio')}</span>
<h1>{titulo_portada}</h1>
<p class="pie-cab">{sello}</p>
{familia(entradas)}

<div class="puertas">{tarjetas}</div>
{comite}

<h2 id="preguntar">Pedirle algo a un agente</h2>
<p>Esto no le contesta ahora: <strong>deja la pregunta escrita</strong> y el agente la
toma en su próxima corrida. Sirve para lo que el portal no alcanza a responder —
por qué un dato dice lo que dice, o que algo no coincide con lo que tú sabes.</p>
{cola}
<form class="pide" method="post" action="/peticion">
  <div class="par">
    <div><label for="para">Para quién</label>
      <select id="para" name="para">{destinos}</select></div>
    <div><label for="asunto">De qué se trata</label>
      <select id="asunto" name="asunto">{opciones}</select></div>
  </div>
  <div class="par">
    <div><label for="proyecto">Caso, si aplica</label>
      <input id="proyecto" name="proyecto" placeholder="PRY-001, CTR-101, 2026-09" maxlength="40"></div>
    <div><label for="de">Quién pregunta</label>
      <input id="de" name="de" placeholder="Tu nombre" maxlength="80"></div>
  </div>
  <label for="texto">Qué necesitas</label>
  <textarea id="texto" name="texto" maxlength="4000"
    placeholder="Escríbelo como se lo dirías a la persona responsable."></textarea>
  <button type="submit">Dejar la petición</button>
</form>
<p class="aviso"><strong>Esta página no pide contraseña</strong>, así que quien pregunta
es quien dice ser y nada más. No escribas aquí nada que no pondrías en un correo
interno.</p>
</div>"""
    return pagina(org or 'Criterio', cuerpo, hoy)


# --------------------------------------------------------- las familias CFO y CLO

def _senales(r: dict) -> int:
    return len((r.get('datos') or {}).get('alertas') or [])


def vista_familia(entradas: list, sigla: str, hoy: str) -> tuple:
    """Una familia: cada agente del mapa con lo último que escribió su motor y sus reportes."""
    if sigla not in FAMILIAS or sigla == 'pmo':
        return 404, error(404, f'No hay familia {sigla}', hoy)
    f = FAMILIAS[sigla]
    suyas = [x for x in entradas if FAMILIA_DE.get(x['area']) == sigla]
    if not suyas:
        return 404, error(404, f'La familia {f["nombre"]["es"]} no está en el mapa de este portal', hoy)
    cuerpo = [f'<p class="entrada"><b>{e(f["nombre"]["es"])}</b> · {e(f["estado"]["es"])}. Lo que sigue es lo '
              'último que escribió el motor de cada agente, con la fecha en que lo escribió: aquí no se '
              'recalcula nada. Cada reporte se abre tal como lo dejó el agente.</p>']
    for a in f["agentes"]:
        for x in [x for x in suyas if x['area'] == a]:
            res = resultados_de(x)
            reps = reportes_de(x)
            cuerpo.append(f'<div class="agente-cab">{robots.svg(ROBOT_DE[a], informe.TINTA, informe.ORO)}'
                          f'<p class="entrada"><b><a href="/agente/{e(a)}">{e(NOMBRE[a])}</a></b>, '
                          f'{e(AGENTES[a]["titulo"])}' + (f' · {e(x["nombre"])}' if x.get('nombre') else '')
                          + (f' · <b>{len(pendientes(x["_estado"], ROBOT_DE[a]))}</b> peticiones abiertas' if x.get('_estado') and pendientes(x['_estado'], ROBOT_DE[a]) else '')
                          + '</p></div>')
            if not res and not reps:
                cuerpo.append('<div class="bloque"><p>El agente todavía no ha dejado nada en su estado: '
                              'su primer comando es el setup.</p></div>')
                continue
            if res:
                cuerpo.append('<div class="bloque"><table><thead><tr><th>Ámbito</th><th>Corte</th><th>Señales abiertas</th>'
                              '<th>Calculado</th><th>Escrito</th></tr></thead><tbody>')
                for r in res:
                    d = r['datos']
                    cuerpo.append(f'<tr><td>{e(r["ambito"])}</td><td>{e(d.get("periodo") or d.get("anio") or d.get("corte") or "—")}</td>'
                                  f'<td class="n">{_senales(r)}</td><td class="nw">{e(d.get("hoy") or "—")}</td>'
                                  f'<td class="nw">{e(r["escrito"][:16].replace("T", " "))}</td></tr>')
                cuerpo.append('</tbody></table></div>')
            if reps:
                cuerpo.append('<div class="bloque"><table><thead><tr><th>Reporte</th><th>Comando</th><th>Escrito</th>'
                              '</tr></thead><tbody>')
                for rp in reps[:12]:
                    cuerpo.append(f'<tr><td><a href="{e(ruta_reporte(x, rp["ruta"]))}">{e(ETIQUETA.get(rp["comando"], rp["comando"]))}</a></td>'
                                  f'<td><code>{e(rp["comando"])}</code></td><td class="nw">{e(rp["escrito"])}</td></tr>')
                cuerpo.append('</tbody></table></div>')
                if len(reps) > 12:
                    cuerpo.append(f'<p class="entrada">Se muestran los 12 más recientes de {len(reps)}; el resto está en la '
                                  f'<a href="/agente/{e(a)}">página del agente</a>.</p>')
    cuerpo.append(AVISO_HISTORIA)
    return 200, pagina(f["nombre"]["es"], "".join(cuerpo), hoy, nav(), f'/familia/{sigla}')


def vista_reporte(entradas: list, area: str, instancia: str, rel: str, hoy: str) -> tuple:
    """Un reporte, tal como lo escribió el motor: el servidor solo lo convierte a página."""
    x = next((x for x in entradas if x['area'] == area and (x.get('instancia') or '-') == instancia), None)
    partes = rel.split('/')
    if x is None or x.get('_estado') is None or not partes or not all(SEGURO.match(s) for s in partes) \
            or not partes[-1].startswith('reporte-') or not partes[-1].endswith('.md'):
        return 404, error(404, 'Eso no está aquí', hoy)
    raiz = x['_estado'].resolve()
    f = (raiz / rel).resolve()
    if raiz not in f.parents or not f.is_file():
        return 404, error(404, 'Eso no está aquí', hoy)
    comando = partes[-1][len('reporte-'):-3]
    escrito = dt.datetime.fromtimestamp(f.stat().st_mtime, dt.timezone.utc).isoformat(timespec='minutes').replace('T', ' ')[:16]
    cuerpo = [f'<p class="entrada">{e(quien(x))} · <code>{e(comando)}</code> · escrito por el motor el {e(escrito)}. '
              'Es el reporte tal como quedó en el estado del agente; nada de esto se redactó para el portal.</p>',
              '<div class="bloque">', md_a_html(f.read_text(encoding='utf-8')), '</div>']
    sigla = FAMILIA_DE.get(area)
    return 200, pagina(f'{NOMBRE.get(area, area)} · {ETIQUETA.get(comando, comando)}', "".join(cuerpo), hoy, nav(),
                       f'/familia/{sigla}' if sigla and sigla != 'pmo' else f'/agente/{area}')


def vista_vence(entradas: list, hoy: str) -> tuple:
    """Lo que vence: lo que cada motor dejó con fecha y sin cumplir, de todas las familias. El
    portal solo junta las listas y las ordena por fecha; quién las calculó y cuándo va en cada fila."""
    filas = []
    for x in entradas:
        for r in resultados_de(x):
            # La fecha de cálculo es la del motor (`hoy` de su resultado), no la del archivo.
            for v in (r['datos'].get('vence') or []):
                filas.append((v.get('fecha') or '', x, v, r['datos'].get('hoy') or r['escrito']))
        if x['area'] == 'portafolio' and x.get('_config') and x['_config'].is_file():
            try:
                ciclo = json.loads(x['_config'].read_text(encoding='utf-8')).get('cycle') or {}
            except (OSError, json.JSONDecodeError):
                ciclo = {}
            if ciclo.get('committee_next'):
                filas.append((ciclo['committee_next'], x, {'que': 'Próximo comité', 'caso': None, 'estado': 'programado',
                                                           'comando': 'steering-pack'}, None))
    filas.sort(key=lambda f: (f[0], f[1]['id'], f[2].get('que') or ''))
    cuerpo = ['<p class="entrada">Lo pendiente que tiene fecha, de todos los agentes del mapa: vencimientos y '
              'preavisos de contratos, obligaciones de cumplimiento, tareas del cierre, requerimientos del '
              'auditor, el próximo comité. <b>Cada motor calculó lo suyo</b> en la fecha que dice la última '
              'columna; el portal solo junta las listas y las ordena.</p>']
    if not filas:
        cuerpo.append('<div class="bloque"><p>Ningún agente del mapa ha dejado nada con fecha todavía.</p></div>')
    else:
        cuerpo += ['<div class="bloque"><table><thead><tr><th>Fecha</th><th>Agente</th><th>Qué</th><th>Caso</th>'
                   '<th>Estado</th><th>Calculado</th></tr></thead><tbody>']
        for fecha_, x, v, escrito in filas[:400]:
            caso = v.get('caso')
            cuerpo.append(f'<tr><td class="nw">{e(fecha_)}</td><td><a href="/agente/{e(x["area"])}">{e(quien(x))}</a></td>'
                          f'<td>{e(v.get("que"))}' + (f'<br><code>{e(v["comando"])}</code>' if v.get("comando") else '') + '</td>'
                          '<td class="nw">' + (f'<a href="/caso/{e(seg(caso))}">{e(caso)}</a>' if caso else '—') + '</td>'
                          f'<td>{e(v.get("estado") or "—")}</td><td class="nw">{e((escrito or "configuración")[:10])}</td></tr>')
        cuerpo.append('</tbody></table></div>')
        if len(filas) > 400:
            cuerpo.append(f'<p class="entrada">Se muestran 400 de {len(filas)}.</p>')
    cuerpo.append(AVISO_HISTORIA)
    return 200, pagina('Lo que vence', "".join(cuerpo), hoy, nav(), '/vence')


def recibida(registro: dict, hoy: str) -> str:
    cuerpo = f"""<span class="ante">Petición recibida</span>
<h1>Queda anotada</h1>
<p class="pie-cab">{e(registro['id'])}</p>
<div class="bloque info">
<h3>Qué pasa ahora</h3>
<p>El agente la toma en su próxima corrida. <strong>No hay nadie del otro lado
respondiendo en este momento</strong>, y decirlo es más honesto que un «en breve
te contactamos».</p>
<p>Si es urgente, el camino sigue siendo el de siempre: la persona responsable.</p>
</div>
<div class="decision"><p class="p">{e(ASUNTOS.get(registro['asunto'], registro['asunto']))}</p>
<dl><dt>Para</dt><dd>{e(registro.get('para') or '—')}</dd><dt>Caso</dt><dd>{e(registro['proyecto'] or '—')}</dd>
<dt>Quién pregunta</dt><dd>{e(registro['de'] or 'no lo dijo')}</dd>
<dt>Qué necesita</dt><dd>{e(registro['texto']) or '<em>en blanco</em>'}</dd></dl></div>"""
    return pagina('Petición recibida', cuerpo, hoy,
                  '<div class="nav"><a href="/">← Volver a la portada</a></div>')


def error(codigo: int, que: str, hoy: str) -> str:
    cuerpo = f"""<span class="ante">{codigo}</span>
<h1>{e(que)}</h1>
<p class="pie-cab">Este servidor solo sirve el informe que ya se produjo. No busca
nada más ni ejecuta nada.</p>"""
    return pagina(f'{codigo}', cuerpo, hoy, '<div class="nav"><a href="/">← Portada</a></div>')


# ---------------------------------------------------------------- el servidor

SEGURO = re.compile(r'^[A-Za-z0-9._-]+$')
# Un caso puede ser un producto con nombre —«tarjeta débito», «despacho de flota»—: letras
# de cualquier alfabeto, espacios, punto y guion; nunca una barra ni «..» (ronda 4).
CASO = re.compile(r'^(?!.*\.\.)[\w .-]+$')


class Manejador(BaseHTTPRequestHandler):
    server_version = 'criterio-server'
    sys_version = ''
    # Lo que se sirve es el mapa: una entrada por agente e instancia, con su estado. Sin mapa, la
    # familia PMO como antes (`entradas_legado`). El informe y el estado de la PMO salen de su entrada.
    entradas: list = []
    evidencia: Path = Path('.criterio/corridas')
    organizacion: str = ''
    callado: bool = False

    @property
    def pmo(self) -> dict:
        return next((x for x in self.entradas if x['area'] == 'portafolio'), {})

    @property
    def informe_dir(self) -> Path:
        return self.pmo.get('_informe') or Path('/nonexistent-informe')

    @property
    def estado(self) -> Path:
        return self.pmo.get('_estado') or Path('/nonexistent-estado')

    def todas(self) -> list:
        return indice(self.evidencia, self.entradas)

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
        # Toda página servida lleva el árbol entero, calculado al servir: el estado y el
        # rastro cambian mientras el servidor corre.
        if '<!--ARBOL ' in texto:
            texto = rellenar_arbol(texto, self.todas(), self.entradas)
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
            self.html(200, portada(frescura(self.informe_dir, self.estado, self.entradas), self.hoy(),
                                   self.organizacion, self.entradas))
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
            caso = (q.get('caso') or [''])[0]
            h = historia(self.entradas)
            self.html(200, corridas(self.todas(), h, self.hoy(),
                                    agente, que, caso))
        elif ruta == '/arrastres':
            self.html(200, arrastres(historia(self.entradas), self.hoy()))
        elif ruta.startswith('/agente/'):
            self.html(*vista_agente(self.todas(), ruta[len('/agente/'):], self.hoy(), self.entradas))
        elif ruta.startswith('/familia/'):
            self.html(*vista_familia(self.entradas, ruta[len('/familia/'):], self.hoy()))
        elif ruta == '/vence':
            self.html(*vista_vence(self.entradas, self.hoy()))
        elif ruta.startswith('/reporte/'):
            partes = [urllib.parse.unquote(x) for x in ruta.split('/')[2:]]
            if len(partes) >= 3 and SEGURO.match(partes[0]) and CASO.match(partes[1]):
                self.html(*vista_reporte(self.entradas, partes[0], partes[1], '/'.join(partes[2:]), self.hoy()))
            else:
                self.html(404, error(404, 'Eso no está aquí', self.hoy()))
        elif ruta.startswith('/caso/'):
            codigo = urllib.parse.unquote(ruta[len('/caso/'):])
            if not CASO.match(codigo):
                self.html(404, error(404, 'Eso no está aquí', self.hoy()))
            else:
                self.html(*vista_caso(self.todas(), historia(self.entradas),
                                      self.informe_dir, codigo, self.hoy()))
        elif ruta.startswith('/corrida/'):
            partes = [urllib.parse.unquote(x) for x in ruta.split('/')[2:]]
            if len(partes) == 2 and all(SEGURO.match(x) for x in partes):
                self.html(*vista_rastro(self.evidencia, partes[0], partes[1], self.hoy()))
            elif len(partes) == 3 and SEGURO.match(partes[0]) and CASO.match(partes[1]) \
                    and SEGURO.match(partes[2]):
                self.html(*vista_corrida(self.entradas, partes[0], partes[1], partes[2], self.hoy()))
            else:
                self.html(404, error(404, 'Eso no está aquí', self.hoy()))
        elif ruta.startswith('/historia/'):
            h = historia(self.entradas)
            self.html(*linea_de_tiempo(h, urllib.parse.unquote(ruta[len('/historia/'):]), self.hoy()))
        elif ruta == '/corte':
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            snaps = sorted(x.stem for x in (self.estado / 'snapshots').glob('*.json'))
            a = (q.get('a') or [snaps[-2] if len(snaps) > 1 else ''])[0]
            b = (q.get('b') or [snaps[-1] if snaps else ''])[0]
            if not a or not b:
                # Con un solo corte no hay nada que comparar, y no es un error: es la
                # primera corrida. El árbol enlaza aquí siempre (ronda 2: 404 en las
                # cuatro industrias desde el menú).
                uno = f' el del {e(snaps[-1])}' if snaps else ' ninguno todavía'
                self.html(200, pagina('Qué cambió entre dos cortes',
                    f'<p class="entrada">Hay un solo corte:{uno}. La comparación campo por '
                    'campo aparece cuando la próxima corrida deje el segundo.</p>'
                    + AVISO_HISTORIA, self.hoy(), nav(), '/corte'))
            else:
                self.html(*corte(self.estado, a, b, self.hoy()))
        elif ruta == '/estado.json':
            cuerpo = json.dumps(frescura(self.informe_dir, self.estado, self.entradas),
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
        # La petición va al estado del agente que se eligió; sin elegir, al de la PMO si está, o al
        # primero del mapa. A un destino que no está en el mapa no se escribe.
        para = (campos.get('para') or '').strip()
        destino = next((x for x in self.entradas if x['id'] == para), None) if para else \
            (self.pmo or next(iter(self.entradas), None))
        if destino is None or destino.get('_estado') is None:
            self.html(404, error(404, 'Ese agente no está en este portal', self.hoy()))
            return
        registro = guardar_peticion(destino['_estado'], dict(campos, para=quien(destino),
                                                             agente=ROBOT_DE.get(destino['area'], '')))
        self.html(200, recibida(registro, self.hoy()))


def arrancar(entradas: list, host: str, puerto: int, org: str = '', evidencia: Path = None) -> int:
    Manejador.entradas = entradas
    Manejador.evidencia = evidencia or Path('.criterio') / 'corridas'
    Manejador.organizacion = org
    for x in entradas:
        if x.get('_estado') is not None and x['_estado'].is_dir():
            buzon(x['_estado']).mkdir(parents=True, exist_ok=True)
    pmo = next((x for x in entradas if x['area'] == 'portafolio'), None)
    fr = frescura(pmo['_informe'] if pmo and pmo.get('_informe') else Path('/nonexistent-informe'),
                  pmo['_estado'] if pmo else Path('/nonexistent-estado'), entradas)

    if pmo and fr['informe_generado'] is None:
        print('Aviso: no hay informe de la PMO en su carpeta. La portada lo va a decir.\n'
              '       Corre primero:  /criterio-portfolio:portfolio-report html\n')
    sin_estado = [x['id'] for x in entradas if not (x.get('_estado') and x['_estado'].is_dir())]
    if sin_estado:
        print(f'Aviso: sin estado todavía: {", ".join(sin_estado)}. Se sirven cuando el agente corra.\n')

    with ThreadingHTTPServer((host, puerto), Manejador) as srv:
        real = srv.server_address[1]
        print(f'Rostrum · Criterio · {org or "sirviendo"} · {len(entradas)} agentes e instancias en el mapa')
        print(f'  Portada         http://{host}:{real}/')
        if pmo:
            print(f'  Informes PMO    http://{host}:{real}/pmo')
            print(f'  Comité          http://{host}:{real}/decisiones')
            print(f'  Proyectos       http://{host}:{real}/proyectos'
                  f'   ({len(fr["proyectos"])})')
            print(f'  Productos       http://{host}:{real}/productos'
                  f'   ({len(fr["productos"])})')
        for s in familias_de(entradas):
            if s != 'pmo':
                print(f'  {"Familia " + s.upper():<15} http://{host}:{real}/familia/{s}')
        if any(s != 'pmo' for s in familias_de(entradas)):
            print(f'  Lo que vence    http://{host}:{real}/vence')
        print(f'  Corridas        http://{host}:{real}/corridas'
              f'   ({len(indice(Manejador.evidencia, entradas))})')
        print(f'  Frescura        http://{host}:{real}/estado.json')
        if host not in ('127.0.0.1', 'localhost', '::1'):
            print()
            print('  ATENCIÓN: escuchando fuera de este equipo y SIN AUTENTICACIÓN.')
            print('  Cualquiera que alcance este puerto ve todo lo que está en el mapa.')
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

    Manejador.entradas, Manejador.callado = entradas_legado(inf, est), True
    # La evidencia del arnés también va al temporal: sin esto el selftest lee las
    # corridas reales de `.criterio/corridas/` del repositorio y cuenta lo que no puso.
    Manejador.evidencia = tmp / 'evidencia'
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
            if r in ('/peticion', '/familia/<sigla>', '/reporte/<area>/<instancia>/<archivo>'):
                continue  # son de las familias CFO y CLO: las prueba el mapa, más abajo
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
            elif r.startswith('/agente/'):
                prueba = '/agente/portafolio'
            elif r.startswith('/caso/'):
                prueba = '/caso/PRY-001'
            cod = pedir(prueba)[0]
            if cod in (200, 302):
                vivas.append(r)
        ok('todas las rutas declaradas responden', sorted(vivas),
           sorted(set(RUTAS) - {'/peticion', '/familia/<sigla>', '/reporte/<area>/<instancia>/<archivo>'}))

        # ── la familia: los mismos robots que los README y el portal
        ok('la portada lleva a los cuatro, cada uno a lo suyo',
           (pedir('/')[1].count('class="robot"'), '/agente/proyecto' in pedir('/')[1]), (4, True))
        ok('y la página de un agente lleva el suyo',
           'aria-label="alba"' in pedir('/agente/producto')[1], True)

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
           all(x in cuerpo for x in ('Samuel', 'Alba', '/agente/proyecto',
                                     '/agente/producto')), True)
        # El menú es corto y fijo; el catálogo de funciones vive en la página del agente.
        ok('el menú tiene las cuatro secciones y nada más',
           all(x in cuerpo for x in ('>Portafolio<', '>Historia<', '>Los agentes<', '>Preguntar<'))
           and cuerpo.count('<p class="g">') == 4, True)
        ok('y cuenta las corridas de cada agente',
           '/agente/portafolio' in cuerpo and '/agente/proyecto' in cuerpo and '/agente/producto' in cuerpo, True)
        ok('en pantallas chicas el menú se pliega tras un botón',
           'class="menu-boton"' in cuerpo and '.menu-caja:checked ~ .arbol' in cuerpo, True)
        cod, vera = pedir('/agente/portafolio')
        ok('la página del agente lleva sus 16 funciones, corran o no',
           cod == 200 and vera.count('<code>/criterio-portfolio:') == 16, True)
        ok('cada una con nombre que se entiende y su grupo explicado',
           'Barrido: una ficha por proyecto' in vera
           and 'Instalar, saber qué toca hoy' in vera, True)
        ok('y las de Samuel y Alba también',
           pedir('/agente/proyecto')[1].count('<code>/criterio-project:') == 9
           and pedir('/agente/producto')[1].count('<code>/criterio-product:') == 11, True)
        ok('un agente que no existe responde 404', pedir('/agente/nadie')[0], 404)
        cod, arr = pedir('/arrastres')
        ok('lo que se arrastra tiene página propia',
           cod == 200 and 'desviación en tiempo' in arr and 'variance_time' not in arr and '/caso/PRY-001' in arr, True)
        solo = pedir('/corridas?agente=portafolio&que=portfolio-scan')[1]
        ok('el filtro por comando deja solo las suyas',
           '<td>Barrido: una ficha por proyecto<br>' in solo and 'Informe del portafolio<br>' not in solo, True)
        cod, una = pedir('/corrida/portafolio/-/2026-08-31-sweep-1')
        ok('una corrida registrada solo por `corrida` tiene su página',
           cod == 200 and 'la primera' in una and 'Lo que produjo' in una, True)
        # El rastro del arnés: una invocación con su página, incrustando las cifras.
        ev = tmp / 'rastro'
        (ev / 'portafolio').mkdir(parents=True)
        (ev / 'portafolio' / 'corridas.json').write_text(json.dumps([
            {'id': '2026-09-08-status-report-1', 'agente': 'portafolio',
             'comando': 'status-report', 'args': 'PRY-001', 'caso': 'PRY-001',
             'fecha': '2026-09-08', 'inicio': '2026-09-08T10:00:00',
             'fin': '2026-09-08T10:01:30', 'segundos': 90, 'respuestas': 1,
             'subagentes': 3, 'concurrentes': 3, 'workers': 1, 'exceso': True,
             'salida': True,
             'medidas': [{'que': 'status-report', 'id': '2026-09-08-status-report-1',
                          'hallazgos': 1, 'por_senal': {'variance_time': 1}}]}]),
            encoding='utf-8')
        (ev / 'portafolio' / '2026-09-08-status-report-1.html').write_text(
            portafolio.pagina_corrida('Corrida · 2026-09-08-status-report-1',
                                      '# Corrida\n\n## Lo que el agente mostró\n\n'
                                      'semáforo rojo sin explicar\n', '2026-09-08'),
            encoding='utf-8')
        Manejador.evidencia = ev
        ok('la página de una corrida no se ensancha en un teléfono: su bloque se desplaza',
           '.bloque{overflow-x:auto' in portafolio.pagina_corrida('c', '# c', '2026-09-08'), True)
        con_rastro = pedir('/corridas')[1]
        ok('la corrida del arnés está en la tabla con caso, duración y fuente',
           '2026-09-08 10:00' in con_rastro and '>90<' in con_rastro and 'arnés' in con_rastro, True)
        ok('y el paralelismo que excede lo configurado va en rojo',
           'class="n exceso"' in con_rastro and '3 · 3 a la vez' in con_rastro, True)
        cod, caso = pedir('/caso/PRY-001')
        ok('la página del caso junta lo que los agentes hicieron sobre él',
           cod == 200 and '/corrida/portafolio/2026-09-08-status-report-1' in caso
           and 'Estado de un proyecto' in caso and 'Lo que sigue abierto' in caso, True)
        ok('y la tabla de corridas enlaza al caso y al agente',
           '<a href="/caso/PRY-001">PRY-001</a>' in con_rastro
           and '<a href="/agente/portafolio">Vera</a>' in con_rastro, True)
        cod, una = pedir('/corrida/portafolio/2026-09-08-status-report-1')
        ok('su página abre con el árbol encima',
           cod == 200 and 'semáforo rojo' in una and 'class="arbol"' in una, True)
        ok('y el filtro por caso deja solo las suyas',
           pedir('/corridas?caso=PRY-001')[1].count('<td>Estado de un proyecto<br>'), 1)
        ok('una corrida que no existe responde 404',
           pedir('/corrida/portafolio/2026-01-01-sweep-1')[0], 404)
        ok('ningún hueco del árbol queda sin rellenar',
           '<!--ARBOL' in con_rastro or '<!--ARBOL' in pedir('/index.html')[1], False)
        cuerpo = con_rastro
        ok('con el aviso de que es la historia de lo leído',
           'lo que el agente procesó' in pedir('/corridas')[1], True)
        cod, cuerpo = pedir('/historia/PRY-001')
        ok('la línea de tiempo separa lo abierto de lo resuelto',
           cod == 200 and 'Lo que sigue abierto' in cuerpo
           and 'Lo que se resolvió' in cuerpo, True)
        ok('un caso con nombre abre su página y uno con «..» no',
           (bool(CASO.match('tarjeta débito')), bool(CASO.match('../x')), bool(CASO.match('a/b'))),
           (True, False, False))
        ok('un caso con espacio en el nombre lleva la ruta codificada',
           (seg('tarjeta débito'), pedir('/historia/' + seg('PRY-001'))[0]), ('tarjeta%20d%C3%A9bito', 200))
        ok('la historia nombra la señal, no su clave',
           'desviación en tiempo' in cuerpo and 'variance_time' not in cuerpo, True)
        cod, cuerpo = pedir('/corte?a=2026-08-31&b=2026-09-07')
        ok('el corte muestra el campo que cambió, con su nombre',
           cod == 200 and 'Cuándo cierra' in cuerpo and 'plan.end_date' not in cuerpo
           and '2026-06-30' in cuerpo, True)
        cod, cuerpo = pedir('/corte?a=1999-01-01&b=2026-09-07')
        ok('un corte que no existe lo dice en vez de reventar',
           cod == 404 and 'No hay instantánea del 1999-01-01' in cuerpo, True)
        primero = est / 'snapshots' / '2026-08-31.json'
        primero.rename(primero.with_suffix('.aparte'))
        cod, cuerpo = pedir('/corte')
        primero.with_suffix('.aparte').rename(primero)
        ok('con un solo corte el menú no lleva a un error',
           cod == 200 and 'Hay un solo corte' in cuerpo, True)

        # ── el mapa: las tres familias en un solo portal (ADR 0010)
        raiz = tmp / 'trabajo'

        def escribe(rel, cuerpo):
            f = raiz / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(cuerpo if isinstance(cuerpo, str) else json.dumps(cuerpo), encoding='utf-8')
        escribe('.criterio/portafolio/config.json', {'organization': {'name': 'Banco del Mapa'}, 'cycle': {'committee_next': '2026-10-15'},
                                                     'paths': {'state': 'pmo/estado', 'reports': 'pmo/informe'}})
        escribe('pmo/informe/index.html', informe.pagina('pmo', '<h1>pmo</h1>', '2026-10-06'))
        (raiz / 'pmo' / 'estado').mkdir(parents=True)
        escribe('.criterio/finanzas/900-banco/config.json', {'entity': {'name': 'Banco del Mapa'}, 'paths': {'state': 'estado-finanzas/900-banco'}})
        escribe('estado-finanzas/900-banco/cierre/2026-09/resultados.json', {
            'agente': 'clara', 'periodo': '2026-09', 'alertas': [{'signal': 'project_budget_mismatch', 'key': 'pry:PRY-310'}],
            'vence': [{'fecha': '2026-10-08', 'que': 'T-04 · Conciliaciones firmadas', 'caso': '2026-09', 'estado': 'en plazo', 'comando': 'close-status'}]})
        escribe('estado-finanzas/900-banco/cierre/2026-09/reporte-close-status.md', '# close-status · Banco del Mapa\n\n## Lo que hay que atender\n\nLa tarea T-04 sin soporte.\n')
        escribe('estado-finanzas/900-banco/corridas.json', [{'id': '2026-10-06-close-status-1', 'que': 'close-status', 'fecha': '2026-10-06',
                                                            'hallazgos': 1, 'por_senal': {'project_budget_mismatch': 1},
                                                            'por_caso': {'PRY-310': ['project_budget_mismatch']}, 'salida': True},
                                                           {'id': '2026-10-06-variance-report-1', 'que': 'variance-report', 'fecha': '2026-10-06',
                                                            'hallazgos': 0, 'por_senal': {}, 'por_caso': {}, 'salida': True}])
        # Tomás comparte el estado con Clara: cada uno con lo suyo.
        escribe('.criterio/presupuesto/900-banco/config.json', {'entity': {'name': 'Banco del Mapa'}, 'paths': {'state': 'estado-finanzas/900-banco'}})
        escribe('estado-finanzas/900-banco/presupuesto/2026/resultados.json', {'agente': 'tomas', 'anio': '2026', 'alertas': [], 'vence': []})
        escribe('estado-finanzas/900-banco/presupuesto/2026/reporte-variance-report.md', '# variance-report\n\nLa ejecución del año.\n')
        escribe('estado-finanzas/900-banco/corridas/2026-10-06-close-status-1.md', '# Corrida del 2026-10-06 · close-status\n\n## Lo que produjo\n\nel cierre\n')
        escribe('.criterio/legal/900-banco/config.json', {'entity': {'name': 'Banco del Mapa'}, 'paths': {'state': 'estado-legal/900-banco'}})
        escribe('estado-legal/900-banco/contratos/resultados.json', {
            'agente': 'fidel', 'alertas': [], 'vence': [{'fecha': '2026-11-01', 'que': 'límite del preaviso', 'caso': 'CTR-104',
                                                         'estado': 'pendiente', 'comando': 'obligations-calendar'}]})
        escribe('estado-legal/900-banco/contratos/reporte-obligations-calendar.md', '# obligations-calendar\n\nCTR-104: el preaviso vence el 2026-11-01.\n')
        escribe('estado-legal/900-banco/contratos/secreto.md', 'no es un reporte')
        mapa.guardar(raiz)
        cfg_m, entradas_m, _ = mapa.cargar(mapa.destino(raiz))
        Manejador.entradas, Manejador.evidencia = entradas_m, raiz / '.criterio' / 'corridas'
        cod, port = pedir('/')
        ok('con el mapa, la portada lleva a todos los agentes de las tres familias y a Rostrum',
           (cod, port.count('class="robot"')), (200, 8))
        cod, tomas = pedir('/agente/presupuesto')
        cod2, clara = pedir('/agente/finanzas')
        ok('dos agentes que comparten el estado: cada uno con sus reportes y sus corridas, no los del otro',
           ('reporte-variance-report' in tomas, 'reporte-close-status' in tomas, 'reporte-close-status' in clara,
            'reporte-variance-report' in clara), (True, False, True, False))
        h_m = historia(entradas_m)
        ok('y la historia no duplica la corrida que está en el estado compartido',
           sorted((c['agente'], c['que']) for c in h_m['corridas'] if c['agente'] in ('finanzas', 'presupuesto')),
           [('finanzas', 'close-status'), ('presupuesto', 'variance-report')])
        ok('y una puerta por familia, más lo que vence',
           all(x in port for x in ('/familia/cfo', '/familia/clo', '/vence', '/pmo')), True)
        ok('el formulario deja elegir a quién va la pregunta',
           'value="finanzas/900-banco"' in port and 'Fidel · Banco del Mapa' in port, True)
        cod, fam = pedir('/familia/cfo')
        ok('la página de la familia CFO lleva el reporte de Clara y sus señales abiertas',
           cod == 200 and '/reporte/finanzas/900-banco/cierre/2026-09/reporte-close-status.md' in fam and 'Estado del cierre' in fam, True)
        ok('la familia se ve entera: Tomás está en la portada aunque no haya corrido', '/agente/presupuesto' in port, True)
        ok('una familia que no existe, o la PMO por esta ruta, es 404',
           (pedir('/familia/cxo')[0], pedir('/familia/pmo')[0]), (404, 404))
        cod, rep_ = pedir('/reporte/finanzas/900-banco/cierre/2026-09/reporte-close-status.md')
        ok('el reporte se sirve tal como lo escribió el motor', cod == 200 and 'La tarea T-04 sin soporte' in rep_, True)
        ok('y solo los reportes: ni otro archivo del estado ni una ruta que salga de él',
           (pedir('/reporte/legal/900-banco/contratos/secreto.md')[0],
            pedir('/reporte/legal/900-banco/contratos/resultados.json')[0],
            pedir('/reporte/legal/900-banco/../../pmo/informe/index.html')[0],
            pedir('/reporte/legal/otra/contratos/reporte-obligations-calendar.md')[0]), (404, 404, 404, 404))
        cod, ven = pedir('/vence')
        ok('lo que vence junta las listas de cada motor y el comité, ordenadas por fecha',
           cod == 200 and ven.index('2026-10-08') < ven.index('2026-10-15') < ven.index('2026-11-01')
           and 'Próximo comité' in ven and '/caso/CTR-104' in ven, True)
        cod, hist = pedir('/corridas')
        ok('la historia trae las corridas de Clara con las de la PMO',
           cod == 200 and '<a href="/agente/finanzas">Clara</a>' in hist, True)
        ok('y el menú tiene las familias', '>Las familias<' in hist and '/familia/clo' in hist, True)
        cod, caso_ = pedir('/caso/PRY-310')
        ok('el caso cruza familias: la señal de Clara sobre un proyecto de la PMO, con quién la levantó',
           cod == 200 and 'project_budget_mismatch' in caso_ and '<a href="/agente/finanzas">Clara</a>' in caso_, True)
        cod, fidel = pedir('/agente/legal')
        ok('la página de Fidel lleva sus siete comandos y sus reportes',
           cod == 200 and fidel.count('<code>/criterio-legal:') == 7 and 'Sus reportes' in fidel, True)
        cod, _r = pedir('/peticion', 'POST', urllib.parse.urlencode({'para': 'legal/900-banco', 'texto': '¿Quién decide CTR-104?'}))
        ok('la petición llega al estado del agente que se eligió, y a ningún otro',
           (cod, len(pendientes(raiz / 'estado-legal' / '900-banco')), len(pendientes(raiz / 'pmo' / 'estado'))), (200, 1, 0))
        pedir('/peticion', 'POST', urllib.parse.urlencode({'para': 'finanzas/900-banco', 'texto': '¿Y la T-04?'}))
        ok('en un estado compartido, la petición es de quien se eligió: Clara la ve y Tomás no',
           (len(pendientes(raiz / 'estado-finanzas' / '900-banco', 'clara')), len(pendientes(raiz / 'estado-finanzas' / '900-banco', 'tomas'))),
           (1, 0))
        ok('a un agente que no está en el mapa no se escribe',
           pedir('/peticion', 'POST', urllib.parse.urlencode({'para': 'cumplimiento/900-banco', 'texto': 'x'}))[0], 404)
        ok('la frescura dice de cuándo es lo de cada agente y cuántas peticiones tiene',
           sorted((a['id'], a['peticiones']) for a in json.loads(pedir('/estado.json')[1])['agentes']),
           [('finanzas/900-banco', 1), ('legal/900-banco', 1), ('portafolio', 0), ('presupuesto/900-banco', 0)])
        Manejador.entradas = entradas_legado(inf, est)

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
    ap = argparse.ArgumentParser(description='Rostrum — el servidor de Criterio, uno para todas las familias.')
    ap.add_argument('--mapa', type=Path, default=None,
                    help='el mapa que deja server-setup: <carpeta>/.criterio/rostrum/config.json')
    ap.add_argument('--informe', type=Path, help='sin mapa: la carpeta que produjo informe.py')
    ap.add_argument('--estado', type=Path, help='sin mapa: la carpeta de estado de la PMO')
    ap.add_argument('--config', type=Path, default=None,
                    help='sin mapa: la configuración de la PMO, para saber de quién es')
    ap.add_argument('--evidencia', type=Path, default=None,
                    help='carpeta del rastro del arnés; por defecto <carpeta>/.criterio/corridas')
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
    if args.mapa:
        cfg, entradas, raiz = mapa.cargar(args.mapa)
        org = (cfg.get('organization') or {}).get('name') or ''
        evidencia = args.evidencia or raiz / '.criterio' / 'corridas'
    else:
        if not args.informe or not args.estado:
            ap.error('--mapa, o --informe y --estado para servir solo la PMO (o usa --selftest)')
        if not args.estado.exists():
            ap.error(f'no existe la carpeta de estado: {args.estado}')
        entradas = entradas_legado(args.informe, args.estado)
        if args.config:
            entradas[0]['_config'] = args.config
        org = informe.nombre_organizacion(args.config)
        evidencia = args.evidencia

    host = args.host or ('0.0.0.0' if args.abierto else '127.0.0.1')
    try:
        return arrancar(entradas, host, args.puerto, org, evidencia)
    except OSError as err:
        print(f'No se pudo levantar en {host}:{args.puerto} — {err}', file=sys.stderr)
        if getattr(err, 'errno', None) in (48, 98, 10048):
            print('Ese puerto ya está ocupado. Prueba con --puerto 8788.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
