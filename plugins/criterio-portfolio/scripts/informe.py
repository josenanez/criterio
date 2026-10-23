#!/usr/bin/env python3
"""Criterio PMO — el informe.

    python3 informe.py --state <estado> --config <archivo>          (va a paths.reports)
    python3 informe.py --state <estado> --salida <carpeta>         (sin configuración)
                       [--today AAAA-MM-DD]

Toma lo que calculó `portafolio.py compute` y las fichas, y produce el informe en HTML con
el diseño del producto (docs/design.md). Librería estándar, sin dependencias.

**Dos vistas, y no se diferencian por detalle sino por autoridad.**

`index.html` es la vista interna: por campo, con la cadena de evidencia completa —
el dato, el documento del que salió y su fecha. Quien la lee va a actuar, y para
actuar necesita poder abrir el documento.

`decisiones.html` es la vista del patrocinador: por decisión. No es la interna
recortada: es otro objeto. Solo lo que necesita una decisión suya, formulado como
pregunta con sus opciones y con la consecuencia de no decidir. A un patrocinador se
le entrega la interna filtrada y hace lo que hacen los patrocinadores: se clava en
un detalle y desvía el comité.

Modo claro a propósito. El informe se imprime, y un informe en modo oscuro gasta
tóner y se lee peor en papel. Los colores son los del modo claro de la paleta, que
no son los mismos del modo oscuro aunque cumplan el mismo rol.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------- la paleta
# Modo claro de docs/design.md. Usar un valor del modo oscuro aquí es el error
# que más ha costado en el portal.
CREMA = '#f5f4ef'
PANEL = '#efeee8'
PANEL_ALTO = '#f8f7f3'
LAVADO_ORO = '#fffaf0'
TINTA = '#111111'
CUERPO = '#3f4450'
APAGADO = '#6b675f'
APAGADO_FRIO = '#616a7e'
ORO = '#8a6327'
FILETE = '#c9c6bd'
FILETE_SUAVE = '#d8d5cd'
FILETE_ORO = '#d7c7a4'
OK_ = '#3f6b4a'
OK_FONDO = '#e7eee7'
ERROR = '#8f3a2c'
ERROR_FONDO = '#f3e7e3'
ERROR_FILETE = '#ddc2ba'
ALERTA = '#8a4412'
ALERTA_FONDO = '#f4ead9'
INFO = '#3d5d75'
INFO_FONDO = '#e6edf3'
INFO_FILETE = '#cfdae3'

CSS = f"""
*{{box-sizing:border-box}}
body{{margin:0;background:{CREMA};color:{CUERPO};
  font:400 16px/1.55 'Inter Tight','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
.hoja{{max-width:1080px;margin:0 auto;padding:56px 32px 96px}}
a{{color:{ORO};text-decoration:none;border-bottom:1px solid {FILETE_ORO}}}
a:hover{{border-bottom-color:{ORO}}}
a:focus-visible,button:focus-visible,summary:focus-visible,label:focus-visible,[tabindex]:focus-visible{{
  outline:3px solid {ORO};outline-offset:2px;border-radius:2px}}
.saltar{{position:absolute;left:12px;top:-60px;z-index:10;padding:10px 16px;background:{TINTA};
  color:{CREMA};border:0;border-radius:6px;font-weight:600}}
.saltar:focus{{top:12px}}
main:focus{{outline:none}}
h1{{font-size:2.35rem;line-height:1.14;color:{TINTA};font-weight:500;margin:.2em 0 .1em;
  letter-spacing:-.01em}}
h2{{font-size:1.4rem;color:{TINTA};font-weight:500;margin:2.6em 0 .8em;
  padding-bottom:.4em;border-bottom:1px solid {FILETE}}}
h3{{font-size:1.06rem;color:{TINTA};font-weight:600;margin:1.8em 0 .5em}}
.ante{{font-size:.78rem;letter-spacing:.17em;text-transform:uppercase;color:{ORO};
  font-weight:600}}
.pie-cab{{color:{APAGADO};font-size:.92rem;margin:.5em 0 0}}
.cifras{{display:flex;flex-wrap:wrap;gap:14px;margin:26px 0 0}}
.cifra{{flex:1 1 150px;background:{PANEL_ALTO};border:1px solid {FILETE};border-radius:8px;
  padding:16px 18px}}
.cifra .n{{font-size:1.9rem;color:{TINTA};font-weight:600;line-height:1}}
.cifra .q{{font-size:.84rem;color:{APAGADO};margin-top:6px;display:block}}
.cifra.mala{{background:{ERROR_FONDO};border-color:{ERROR_FILETE}}}
.cifra.mala .n{{color:{ERROR}}}
table{{width:100%;border-collapse:collapse;margin:.6em 0 0;font-size:.95rem}}
code{{overflow-wrap:break-word}}
/* Un enlace o una ruta larga en un párrafo se parte antes que ensanchar la página: la línea
   de los términos, con su dirección, la llevaba a 401 px en un teléfono (ronda 11). */
p,li,td,dd{{overflow-wrap:anywhere}}
th{{text-align:left;font-weight:600;color:{APAGADO};font-size:.78rem;
  letter-spacing:.08em;text-transform:uppercase;padding:8px 10px;
  border-bottom:1px solid {FILETE}}}
td{{padding:10px;border-bottom:1px solid {FILETE_SUAVE};vertical-align:top}}
tr:last-child td{{border-bottom:none}}
.sem{{display:inline-block;padding:2px 9px;border-radius:4px;font-size:.78rem;
  font-weight:600;border:1px solid}}
.verde{{color:{OK_};background:{OK_FONDO};border-color:{OK_}}}
.amarillo{{color:{ALERTA};background:{ALERTA_FONDO};border-color:{ALERTA}}}
.rojo{{color:{ERROR};background:{ERROR_FONDO};border-color:{ERROR}}}
.nada{{color:{APAGADO};background:{PANEL};border-color:{FILETE}}}
.senal{{display:inline-block;padding:2px 8px;margin:2px 4px 2px 0;border-radius:4px;
  font-size:.76rem;border:1px solid {FILETE};color:{APAGADO};background:{PANEL}}}
.senal.dura{{color:{ERROR};border-color:{ERROR_FILETE};background:{ERROR_FONDO}}}
.cita{{display:block;font-size:.8rem;color:{APAGADO_FRIO};margin-top:3px}}
.vacio{{color:{APAGADO};font-style:italic}}
.bloque{{border:1px solid {FILETE};border-left:3px solid {ORO};background:{LAVADO_ORO};
  border-radius:0 8px 8px 0;padding:18px 22px;margin:20px 0}}
.bloque h3,.bloque h2.t{{margin-top:0}}
h2.t{{font-size:1.06rem;font-weight:600;margin:1.8em 0 .5em;padding:0;border:0}}
.bloque > :first-child{{margin-top:0}}
.tabla{{max-width:100%;overflow-x:auto}}
.grafico{{max-width:100%;overflow-x:auto;margin:.6em 0 0;background:{PANEL_ALTO};border:1px solid {FILETE};
  border-radius:8px;padding:14px 14px 8px}}
.grafico svg{{display:block;font-family:inherit}}
.leyenda{{font-size:.84rem;color:{APAGADO};margin:.6em 0 0;line-height:2}}
.leyenda .m{{display:inline-block;width:18px;height:10px;border-radius:3px;margin:0 6px 0 10px;vertical-align:middle}}
.leyenda .l{{display:inline-block;width:22px;height:0;margin:0 6px 0 10px;vertical-align:middle}}
.leyenda .r{{display:inline-block;width:10px;height:10px;transform:rotate(45deg);border:2px solid;margin:0 7px 0 12px;vertical-align:middle}}
.leyenda .i{{white-space:nowrap;margin-right:14px}}
.leyenda .i > span{{margin-left:0}}
.tabla > table{{margin-top:0}}
.bloque.info{{background:{INFO_FONDO};border-color:{INFO_FILETE};border-left-color:{INFO}}}
.decision{{border:1px solid {FILETE};border-radius:8px;padding:22px 24px;margin:18px 0;
  background:{PANEL_ALTO}}}
.decision .p{{font-size:1.16rem;color:{TINTA};font-weight:500;margin:0 0 .5em}}
.decision dl{{margin:.6em 0 0;display:grid;grid-template-columns:270px 1fr;gap:6px 20px}}
@media (max-width:640px){{.decision dl{{grid-template-columns:1fr;gap:2px 0}}
  .decision dd{{margin-bottom:.8em}}
  .hoja{{padding:32px 18px 72px}}
  h1{{font-size:1.9rem}}
  table.apila,table.apila tbody,table.apila tr,table.apila td{{display:block;width:100%}}
  table.apila thead{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
  table.apila tr{{padding:10px 0;border-bottom:1px solid {FILETE}}}
  table.apila td{{border:0;padding:3px 0}}
  table.apila td[data-col]{{position:relative;padding-left:8.2em;min-height:1.6em}}
  table.apila td[data-col]::before{{content:attr(data-col);position:absolute;left:0;top:.45em;width:7.6em;
    font-size:.75rem;line-height:1.25;letter-spacing:.04em;text-transform:uppercase;color:{APAGADO};font-weight:600}}}}
.decision dt{{color:{APAGADO};font-size:.82rem;text-transform:uppercase;
  letter-spacing:.06em;font-weight:600;padding-top:2px}}
.decision dd{{margin:0}}
.pie{{margin-top:64px;padding-top:20px;border-top:1px solid {FILETE};
  color:{APAGADO};font-size:.86rem}}
.nav{{margin:0 0 30px;font-size:.92rem}}
.nav a{{margin-right:18px;display:inline-block;padding:3px 0}}
.barra{{border-bottom:1px solid {FILETE};margin:-20px 0 34px;padding-bottom:14px;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 26px}}
.barra .casa{{font-size:.95rem;font-weight:600;color:{TINTA};border:none;
  margin-right:8px}}
.barra .casa span{{display:block;font-size:.75rem;letter-spacing:.14em;
  text-transform:uppercase;color:{ORO};font-weight:600}}
.barra nav{{display:flex;flex-wrap:wrap;gap:4px 22px;margin-left:auto}}
.barra nav a{{border:none;color:{APAGADO};font-size:.95rem;padding:4px 0;
  border-bottom:2px solid transparent}}
.barra nav a:hover{{color:{TINTA}}}
.barra nav a.aqui{{color:{TINTA};font-weight:600;border-bottom-color:{ORO}}}
.migas{{font-size:.9rem;color:{APAGADO};margin:0 0 6px}}
.migas a{{border-bottom:1px solid {FILETE_ORO}}}
.par{{display:flex;flex-wrap:wrap;gap:16px;margin:26px 0 0}}
.par > *{{flex:1 1 300px}}
@media print{{
  body{{background:#fff}}
  .hoja{{max-width:none;padding:0}}
  .nav,.barra nav,.saltar{{display:none}}
  .barra{{margin-top:0}}
  h2{{page-break-after:avoid}}
  .decision,.bloque,tr{{page-break-inside:avoid}}
  a{{border:none;color:{TINTA}}}
}}
"""

# Señales que un informe muestra en rojo: son las que piden una acción.
DURAS = {'declared_vs_evidence', 'rebaseline_unauthorized', 'milestone_overdue',
         'milestone_met_without_evidence',
         'progress_vs_plan',
         'vendor_invoiced_over_accepted', 'vendor_invoiced_without_delivery',
         'commitment_rescheduled', 'change_without_baseline'}

NOMBRES = {
    'silent': 'en silencio', 'variance_time': 'desviación en tiempo',
    'variance_cost': 'desviación en costo', 'budget_committed': 'presupuesto comprometido',
    'milestone_overdue': 'hito vencido sin evidencia',
    'milestone_met_without_evidence': 'hito declarado cerrado, sin evidencia',
    'progress_vs_plan': 'el avance declarado y el cronograma no coinciden',
    'commitment_overdue': 'compromiso vencido', 'commitment_undated': 'compromiso sin fecha',
    'commitment_rescheduled': 'compromiso reprogramado',
    'contradiction': 'contradicción entre documentos',
    'governance_change': 'cambio de gobierno',
    'declared_vs_evidence': 'la evidencia no explica el verde',
    'declaration_stale': 'declaración vieja',
    'pm_vs_pmo': 'la ficha del gerente y la de la PMO no coinciden',
    'rebaseline_unauthorized': 'replanificación sin autorizar',
    'change_without_baseline': 'cambio sin línea base',
    'vendor_deliverable_late': 'entregable de proveedor vencido',
    'vendor_accepted_without_evidence': 'aceptado sin evidencia',
    'vendor_invoiced_without_delivery': 'facturado sin entrega',
    'vendor_invoiced_over_accepted': 'facturado sobre lo aceptado',
}


def e(x):
    return html.escape(str(x if x is not None else ''))


def plata(n):
    if n is None:
        return '—'
    return f'{n:,.0f}'.replace(',', '.')


def pct(n):
    """95.2 % con la coma decimal que usa el lector, y sin el .0 que sobra."""
    if n is None:
        return '—'
    s = f'{n:.1f}'.rstrip('0').rstrip('.')
    return s.replace('.', ',') + '%'


def plural(n, uno, varios):
    """«1 día», no «1 días». Un informe que no concuerda se lee como un volcado."""
    return f'{n} {uno if abs(n) == 1 else varios}'


# ------------------------------------------------- el campo, dicho en castellano
# Una ruta como `plan.milestones[1].evidence` es correcta y no se le muestra a
# nadie. Quien lee el informe no conoce el esquema de la ficha: conoce su proyecto.
LEXICO = {
    'identity.code': 'El código del proyecto',
    'identity.name': 'El nombre del proyecto',
    'identity.sponsor': 'Quién patrocina el proyecto',
    'identity.manager': 'Quién lo gerencia',
    'identity.committee': 'A qué comité reporta',
    'identity.authority': 'Hasta dónde decide el gerente sin subir al comité',
    'identity.product': 'Qué producto construye',
    'identity.aliases': 'Con qué otros nombres aparece',
    'identity.business_area': 'Qué área es dueña del proyecto',
    'identity.phase': 'En qué fase va',
    'declared.status': 'Qué estado declara el gerente',
    'declared.progress_pct': 'Qué avance declara el gerente',
    'declared.as_of': 'De cuándo es la declaración del gerente',
    'declared.source': 'Dónde lo declara el gerente',
    'plan.start_date': 'Cuándo arrancó',
    'plan.end_date': 'Cuándo cierra',
    'plan.scope_summary': 'Qué alcance tiene',
    'plan.exclusions': 'Qué queda fuera del alcance',
    'raid.risks': 'Qué riesgos tiene',
    'raid.assumptions': 'Qué supuestos tiene',
    'raid.issues': 'Qué incidencias tiene',
    'money.currency': 'En qué moneda está el presupuesto',
    'money.approved': 'Cuánto le aprobaron',
    'money.committed': 'Cuánto lleva comprometido',
    'money.executed': 'Cuánto lleva ejecutado',
    'money.projection': 'En cuánto proyecta terminar',
}
# Para las listas: cómo se llama cada elemento, y de qué campo sale su rótulo.
# La clave es el nombre suelto, no la ruta: `plan.milestones` y `milestones` son
# el mismo tramo y la ruta se recorre trozo a trozo.
LISTAS = {
    'milestones': ('el hito', ('name',)),
    'risks': ('el riesgo', ('what', 'description')),
    'issues': ('la incidencia', ('what', 'description')),
    'dependencies': ('la dependencia', ('what', 'description')),
    'assumptions': ('el supuesto', ('what', 'description')),
    'commitments': ('el compromiso', ('what',)),
    'vendors': ('el proveedor', ('name',)),
    'deliverables': ('el entregable', ('name',)),
    'baseline': ('la línea base', ('version',)),
    'changes': ('el cambio', ('ref',)),
    'reschedules': ('la reprogramación', ('due_date',)),
}
HOJAS = {
    'evidence': 'La evidencia de',
    'owner': 'Quién responde por',
    'due': 'Para cuándo es',
    'due_date': 'Para cuándo es',
    'amount': 'Cuánto vale',
    'state': 'En qué estado está',
    'name': 'Cómo se llama',
    'impact': 'Qué impacto tiene',
    'mitigation': 'Cómo se mitiga',
    'approved_on': 'Cuándo se aprobó',
    'start_date': 'Cuándo arranca',
    'end_date': 'Cuándo cierra',
    'reason': 'Por qué se aprobó',
    'version': 'Qué versión es',
    'baseline_date': 'La fecha de línea base de',
    'current_date': 'La fecha vigente de',
    'contract_ref': 'Qué contrato respalda a',
    'invoiced': 'Cuánto ha facturado',
    'on_project': 'De qué proyecto depende',
    'needed_by': 'Para cuándo se necesita',
    'confirmed': 'Si está confirmada',
    'requested_on': 'Cuándo se pidió',
    'scope_impact': 'Qué cambia en el alcance con',
    'time_impact': 'Cuánto tiempo suma',
    'cost_impact': 'Cuánto cuesta',
    'decision': 'Qué se decidió sobre',
    'decided_by': 'Quién decidió',
    'original_due_date': 'Para cuándo se prometió primero',
    'stated_on': 'Cuándo se dijo',
    'source': 'De dónde sale',
    'who': 'Quién responde por',
    'what': 'Qué es',
    'ref': 'Qué referencia tiene',
}


def _trozos(ruta):
    """`vendors[0].deliverables[1].evidence` → [('vendors',0),('deliverables',1),('evidence',None)]"""
    fuera = []
    for parte in ruta.split('.'):
        if parte.endswith(']') and '[' in parte:
            nombre, idx = parte[:-1].split('[', 1)
            fuera.append((nombre, int(idx)))
        else:
            fuera.append((parte, None))
    return fuera


def _recorta(texto, tope=70):
    """Un riesgo puede estar descrito en dos renglones. En una lista de lo que falta
    no cabe: se corta en la palabra, no a la mitad de una."""
    texto = ' '.join(str(texto).split())
    if len(texto) <= tope:
        return texto
    return texto[:tope].rsplit(' ', 1)[0] + '…'


def nombre_campo(rec: dict, ruta: str) -> str:
    if ruta.startswith('pm_record.'):
        # El contraste con la ficha del gerente (Samuel) trae las rutas de su ficha.
        dentro = nombre_campo(rec.get('pm_record') or {}, ruta[len('pm_record.'):])
        return f'En la ficha del gerente: {dentro[:1].lower()}{dentro[1:]}'
    if ruta in LEXICO:
        return LEXICO[ruta]
    trozos = _trozos(ruta)
    hoja = trozos[-1][0]
    # Baja por la ficha hasta el elemento que contiene la hoja, para poder nombrarlo.
    nodo, etiqueta, rotulo = rec, None, None
    for nombre, idx in trozos[:-1]:
        nodo = nodo.get(nombre) if isinstance(nodo, dict) else None
        if nombre in LISTAS:
            etiqueta, claves = LISTAS[nombre]
        elif idx is not None:
            etiqueta, claves = nombre, ('name',)
        else:
            continue  # un contenedor sin índice (`plan`, `raid`) no nombra nada
        if idx is not None:
            nodo = nodo[idx] if isinstance(nodo, list) and idx < len(nodo) else None
            for clave in claves:
                bruto = (nodo or {}).get(clave) if isinstance(nodo, dict) else None
                if isinstance(bruto, dict):
                    bruto = bruto.get('value')
                if bruto:
                    rotulo = _recorta(bruto)
                    break
    if etiqueta is None:
        return ruta
    sujeto = f'{etiqueta} «{rotulo}»' if rotulo else f'{etiqueta} sin nombre'
    frase = f'{HOJAS.get(hoja, hoja)} {sujeto}'
    # «La evidencia de el entregable» delata que la frase la armó una máquina.
    return frase.replace(' de el ', ' del ')


def hojas_del_esquema(esquema: Path | None = None) -> list:
    """Cada campo de la ficha que puede quedar `not_found`, como ruta con índice cero:
    `vendors[0].deliverables[0].evidence`. Sale del esquema del skill, no de una lista
    escrita aquí: si el esquema gana un campo y el léxico no, el selftest lo dice."""
    esquema = esquema or Path(__file__).resolve().parent.parent / 'skills' / 'project-record' / 'references' / 'schema.yaml'
    rutas, pila = [], []          # pila de (sangría, nombre, es_lista)
    for crudo in esquema.read_text(encoding='utf-8').splitlines():
        linea = crudo.split('#', 1)[0].rstrip()
        if not linea.strip() or ':' not in linea:
            continue
        sangria = len(linea) - len(linea.lstrip(' '))
        item = linea.lstrip(' ').startswith('- ')
        if item:
            sangria += 2
            if pila:
                pila[-1] = (pila[-1][0], pila[-1][1], True)
        nombre, resto = linea.lstrip(' -').split(':', 1)
        while pila and pila[-1][0] >= sangria:
            pila.pop()
        base = '.'.join(n + ('[0]' if lista else '') for _, n, lista in pila)
        ruta = f'{base}.{nombre}' if base else nombre
        if resto.strip() in ('', '[]'):
            rutas.append(ruta)
        pila.append((sangria, nombre, False))
    # un contenedor también aparece como hoja vacía: solo quedan las hojas de verdad
    hojas = [r for r in rutas if not any(o.startswith(r + '.') or o.startswith(r + '[') for o in rutas)]
    return [r for r in hojas if not r.startswith(('meta.', 'activity.', 'schema_version'))]


def campo(rec: dict, ruta: str):
    """El campo de la ficha, con su cita. Devuelve (valor, fuente, fecha, estado)."""
    nodo = rec
    for parte in ruta.split('.'):
        if not isinstance(nodo, dict):
            return None, None, None, None
        nodo = nodo.get(parte)
    if not isinstance(nodo, dict):
        return nodo, None, None, None
    # Un campo no encontrado no tiene valor, aunque la ficha haya copiado el estado en el
    # valor («not_found»): el informe dice que no está dicho, no imprime la palabra (D018).
    if nodo.get('state') == 'not_found':
        return None, nodo.get('source'), nodo.get('source_date'), 'not_found'
    return nodo.get('value'), nodo.get('source'), nodo.get('source_date'), nodo.get('state')


def con_cita(rec: dict, ruta: str, formato=str):
    """Un dato tal como se defiende ante un comité: el valor y de dónde salió."""
    valor, fuente, fecha, estado = campo(rec, ruta)
    if valor is None:
        return f'<span class="vacio">no está dicho en ninguna parte</span>'
    pie = f'{e(fuente)} · {e(fecha)}' if fuente else 'sin cita'
    marca = ' · <strong>contradicho</strong>' if estado == 'ambiguous' else ''
    return f'{e(formato(valor))}<span class="cita">{pie}{marca}</span>'


# El orden de gravedad, para poder decir cuál es el peor de un grupo de proyectos.
# Un producto está como está su peor proyecto, no como el promedio: no llega hasta
# que llegan todos.
STATUS_ORDEN = {'verde': 0, 'green': 0, 'amarillo': 1, 'yellow': 1, 'amber': 1,
                'en riesgo': 1, 'at risk': 1, 'rojo': 2, 'red': 2}
ESTADO_NOMBRE = {0: 'verde', 1: 'amarillo', 2: 'rojo'}


def semaforo(valor):
    clase = {'verde': 'verde', 'green': 'verde', 'amarillo': 'amarillo', 'yellow': 'amarillo',
             'rojo': 'rojo', 'red': 'rojo'}.get(str(valor).lower(), 'nada')
    return f'<span class="sem {clase}">{e(valor) if valor else "sin declarar"}</span>'


def senales(alertas, proyecto=None):
    """Las señales sin repetir. Con `proyecto`, cada una lleva su cifra."""
    vistas, salida = set(), []
    for a in alertas:
        s = a['signal']
        if s in vistas:
            continue
        vistas.add(s)
        dura = ' dura' if s in DURAS else ''
        texto = con_cifra(proyecto, s) if proyecto else NOMBRES.get(s, s)
        salida.append(f'<span class="senal{dura}">{e(texto)}</span>')
    return ''.join(salida) or '<span class="vacio">ninguna</span>'


# Las tres secciones del portal, en el orden en que se miran: primero cómo va el
# portafolio, después el proyecto, después el producto. El archivo de cada una es el
# dato: la barra y las rutas del servidor salen de aquí y no pueden separarse.
SECCIONES = (
    ('pmo', 'Informes PMO', 'index.html'),
    ('proyectos', 'Proyectos', 'proyectos.html'),
    ('productos', 'Productos', 'productos.html'),
)


def barra(seccion, org):
    """La misma barra en todas las páginas. Sin esto son informes sueltos; con esto
    es un sitio por el que alguien se mueve sin volver a preguntar el enlace."""
    casa = (f'<a class="casa" href="index.html"><span>Oficina de proyectos</span>'
            f'{e(org)}</a>' if org else
            '<a class="casa" href="index.html"><span>Oficina de proyectos</span>'
            'Portafolio</a>')
    enlaces = ''.join(
        '<a href="{}" class="{}">{}</a>'.format(
            arch, 'aqui' if clave == seccion else '', e(nombre))
        for clave, nombre, arch in SECCIONES)
    return f'<div class="barra">{casa}<nav>{enlaces}</nav></div>'


# Una tabla ancha se desliza dentro de su caja y no empuja la página. Si de verdad se desliza,
# se puede alcanzar con el teclado: el foco solo se le da a la que lo necesita, para no llenar
# la página de paradas inútiles.
# La caja que se desliza se alcanza con el teclado. Una tabla que se desliza ella misma —la de una
# corrida guardada, cuya hoja la vuelve bloque en un teléfono— también (ronda 11, todas las familias).
DESLIZA = ("<script>(function(){function f(){document.querySelectorAll('.tabla, table').forEach(function(t){"
           "if(t.scrollWidth>t.clientWidth+1){t.tabIndex=0}else{t.removeAttribute('tabindex')}})}"
           "f();addEventListener('resize',f)})()</script>")


def apilable(tabla: str, cols: list) -> str:
    """Una tabla de cuatro columnas o más, en un teléfono, se lee fila por fila: cada celda lleva
    el nombre de su columna, y la hoja de estilo la apila. En pantalla ancha no cambia nada."""
    def fila(m):
        i = iter(range(10_000))
        return re.sub(r'<td\b', lambda _: f'<td data-col="{e(cols[min(next(i), len(cols) - 1)])}"', m.group(0))
    tabla = re.sub(r'<tbody>.*?</tbody>', lambda m: re.sub(r'<tr\b.*?</tr>', fila, m.group(0), flags=re.S), tabla, flags=re.S)
    return tabla.replace('<table', '<table class="apila"', 1)


def tablas(html_: str) -> str:
    """Cada tabla dentro de su caja deslizable, con un nombre que la distingue de las demás de la
    página: el título bajo el que está y sus columnas."""
    out, fin, vistos = [], 0, {}
    for m in re.finditer(r'<table\b.*?</table>', html_, flags=re.S):
        antes = html_[:m.start()]
        titulos = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', antes, re.S)
        bajo = re.sub(r'<[^>]+>', '', titulos[-1]).strip() if titulos else ''
        cols = [re.sub(r'<[^>]+>', '', c).strip() for c in re.findall(r'<th[^>]*>(.*?)</th>', m.group(0), re.S)]
        nombre = (bajo or 'Tabla') + (': ' + ', '.join(c for c in cols if c) if cols else '')
        nombre = nombre[:140]
        vistos[nombre] = vistos.get(nombre, 0) + 1
        if vistos[nombre] > 1:
            nombre += f' ({vistos[nombre]})'
        # Un encabezado vacío —la columna de la izquierda de una tabla de dos entradas— no es un
        # encabezado: va como celda (axe, empty-table-header).
        tabla = re.sub(r'<th([^>]*)>\s*</th>', r'<td\1></td>', m.group(0))
        if len(cols) >= 4:
            tabla = apilable(tabla, cols)
        out += [html_[fin:m.start()], f'<div class="tabla" role="region" aria-label="{e(nombre)}">', tabla, '</div>']
        fin = m.end()
    out.append(html_[fin:])
    return ''.join(out)


def pagina(titulo, cuerpo, hoy, nav=''):
    """La página entera. El contenido va en `<main>`, con un enlace para saltar a él: el menú de
    Rostrum va antes, y quien navega con teclado no tiene por qué recorrerlo en cada página."""
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><link rel="icon" href="data:,">
<title>{e(titulo)}</title><style>{CSS}</style></head>
<body><a class="saltar" href="#contenido">Saltar al contenido</a><div class="hoja"><main id="contenido" tabindex="-1">{nav}{tablas(cuerpo)}</main>
<footer class="pie">
Producido por <strong>Vera</strong>, el agente PMO de Criterio, el {e(hoy)}.
Esto es un <strong>borrador de trabajo, no una decisión</strong>: cada dato lleva la cita del
documento del que salió para que se pueda verificar, y «no está dicho en ninguna parte» es un
hallazgo válido. El agente sabe lo que se escribió, no lo que se habló fuera de los documentos.
</footer>{DESLIZA}</div></body></html>
"""


# ---------------------------------------------------------------- las vistas

def slug(texto):
    """El nombre de archivo de un producto. Un producto se llama «Cuenta
    transaccional», no `producto-3`: el archivo se lee en la barra del navegador y
    alguien lo va a mandar por chat."""
    limpio = unicodedata.normalize('NFKD', str(texto))
    limpio = ''.join(c for c in limpio if not unicodedata.combining(c))
    limpio = re.sub(r'[^a-zA-Z0-9]+', '-', limpio).strip('-').lower()
    return limpio or 'sin-nombre'


def archivo_producto(nombre):
    return f'producto-{slug(nombre)}.html'


def vista_pmo(datos, fichas, hoy, org):
    """El informe de la PMO: cómo va el portafolio, no cuál proyecto abrir.

    Lo que aquí aparece es lo que **no existe proyecto por proyecto**: los verdes
    que la evidencia no sostiene, lo que se contradice entre documentos, y quién
    está patrocinando más de una cosa a la vez. El listado de proyectos vive en su
    propia página, porque leer un informe y navegar un portafolio son dos cosas
    distintas y la misma tabla no sirve para las dos.
    """
    t = datos['totals']
    cifras = [
        (t['projects'], 'proyectos', False),
        (t['green_contradicted'], 'verdes que la evidencia no sostiene', t['green_contradicted'] > 0),
        (t['with_alerts'], 'con algo que mirar', False),
        (t['no_baseline'], 'sin línea base', t['no_baseline'] > 0),
        (t.get('no_authority', 0), 'sin autoridad declarada', t.get('no_authority', 0) > 0),
    ]
    tarjetas = ''.join(
        f'<div class="cifra{" mala" if mala else ""}"><span class="n">{n}</span>'
        f'<span class="q">{q}</span></div>' for n, q, mala in cifras)

    # Lo que solo se ve mirando el portafolio entero.
    silenciosos = sorted((p for p in datos['projects'] if p.get('days_silent') is not None),
                         key=lambda x: -x['days_silent'])[:5]
    filas_sil = ''.join(
        f"<tr><td><a href=\"{e(p['code'])}.html\">{e(p['code'])}</a> {e(p.get('name'))}</td>"
        f"<td>{plural(p['days_silent'], 'día', 'días')}</td></tr>"
        for p in silenciosos if p['days_silent'] > 0)
    silencio = (f'<table><tr><th>Proyecto</th><th>Sin un documento nuevo desde hace</th></tr>'
                f'{filas_sil}</table>' if filas_sil
                else '<p class="vacio">Ninguno lleva días sin un documento nuevo.</p>')

    choques = {}
    for p in datos['projects']:
        rec = fichas.get(p['code'], {})
        quien, _, _, _ = campo(rec, 'identity.sponsor')
        if quien:
            choques.setdefault(quien, []).append(p['code'])
    repetidos = {k: v for k, v in choques.items() if len(v) > 1}
    if repetidos:
        filas_rep = ''.join(
            f"<tr><td>{e(k)}</td><td>{', '.join(e(c) for c in sorted(v))}</td></tr>"
            for k, v in sorted(repetidos.items()))
        patrocinio = f"""<table><tr><th>Patrocinador</th><th>Proyectos</th></tr>{filas_rep}</table>
<p class="pie-cab">No es un hallazgo por sí solo. Lo es cuando dos de ellos compiten por la
misma fecha o el mismo equipo, y eso no está en la carpeta: lo sabe la persona.</p>"""
    else:
        patrocinio = '<p class="vacio">Nadie patrocina más de un proyecto.</p>'

    sin_producto = [p for p in datos['projects'] if not p.get('product')]
    resumen_prod = (
        f"<p>{plural(len(datos.get('products') or []), 'producto declarado', 'productos declarados')}"
        f" en el portafolio. "
        + (f"<strong>{plural(len(sin_producto), 'proyecto no dice', 'proyectos no dicen')} "
           f"qué producto construye</strong>, así que su avance no se ve desde el lado del "
           f"producto: {', '.join(e(p['code']) for p in sin_producto)}."
           if sin_producto else 'Todos los proyectos dicen qué producto construyen.')
        + ' <a href="productos.html">Ver los productos</a></p>')

    cuerpo = f"""<span class="ante">Informe PMO</span>
<h1>Cómo va el portafolio</h1>
<p class="pie-cab">Al {e(datos['as_of'])} · cada dato con la cita del documento del que salió ·
<a href="decisiones.html">lo que necesita una decisión del comité</a></p>
<div class="cifras">{tarjetas}</div>

<h2>Lo que solo se ve mirando todo junto</h2>
<h3>Proyectos en silencio</h3>
<p class="pie-cab">Nadie escribió nada nuevo. No significa que no esté pasando nada;
significa que no hay contra qué contrastar lo que se reporta.</p>
{silencio}

<h3>Quién patrocina más de un proyecto</h3>
{patrocinio}

<h2>Por producto</h2>
<p>Un proyecto termina; un producto sobrevive a todos los proyectos que lo construyeron.</p>
{resumen_prod}"""
    return pagina('Informe PMO · el portafolio', cuerpo, hoy, barra('pmo', org))


def vista_proyectos(datos, fichas, hoy, org):
    """El listado. Una sola tabla, ordenada por lo que más pide atención."""
    filas = []
    for p in sorted(datos['projects'], key=lambda x: (-len(x['alerts']), x['code'])):
        silencio = p.get('days_silent')
        prod = p.get('product')
        prod_html = (f'<a href="{archivo_producto(prod)}">{e(prod)}</a>' if prod
                     else '<span class="vacio">no lo dice</span>')
        filas.append(f"""<tr>
<td><a href="{e(p['code'])}.html"><strong>{e(p['code'])}</strong></a><br>{e(p.get('name'))}</td>
<td>{prod_html}</td>
<td>{semaforo(p.get('declared', {}).get('status'))}
  <span class="cita">{e(p.get('declared', {}).get('source') or 'sin fuente')}</span></td>
<td>{senales(p['alerts'])}</td>
<td>{'—' if silencio is None else plural(silencio, 'día', 'días')}</td>
</tr>""")

    cuerpo = f"""<span class="ante">Proyectos</span>
<h1>{plural(len(datos['projects']), 'proyecto', 'proyectos')} en el portafolio</h1>
<p class="pie-cab">Al {e(datos['as_of'])} · ordenados por lo que más pide atención, no por
código · entra en cualquiera para ver de dónde sale cada dato</p>
<table><tr><th>Proyecto</th><th>Producto</th><th>Declara</th>
<th>Lo que la evidencia dice</th><th>Silencio</th></tr>
{''.join(filas)}</table>"""
    return pagina('Proyectos', cuerpo, hoy, barra('proyectos', org))


def vista_productos(datos, fichas, hoy, org):
    """El listado de productos, y los proyectos que no dicen a cuál pertenecen."""
    filas = []
    for g in datos.get('products') or []:
        suyos = [p for p in datos['projects'] if p['code'] in g['projects']]
        comites = sorted({(campo(fichas.get(p['code'], {}), 'identity.committee')[0] or '')
                          for p in suyos} - {''})
        peor = max((STATUS_ORDEN.get(str((p.get('declared') or {}).get('status')).lower(), -1)
                    for p in suyos), default=-1)
        # El semáforo declarado, solo, mentiría: un producto con 10 señales cuyo
        # único proyecto se declara verde saldría en verde, que es exactamente lo
        # que este portal existe para no hacer.
        contradichos = [p['code'] for p in suyos
                        if any(a['signal'] == 'declared_vs_evidence' for a in p['alerts'])]
        marca = (f'<span class="cita"><strong>la evidencia no lo sostiene</strong> en '
                 f'{", ".join(e(c) for c in contradichos)}</span>' if contradichos else '')
        filas.append(f"""<tr>
<td><a href="{archivo_producto(g['product'])}"><strong>{e(g['product'])}</strong></a></td>
<td>{', '.join(f'<a href="{e(c)}.html">{e(c)}</a>' for c in g['projects'])}</td>
<td>{e(' · '.join(comites)) or '<span class="vacio">no está dicho</span>'}
  {'<span class="cita"><strong>más de un comité mira este producto</strong></span>' if len(comites) > 1 else ''}</td>
<td>{semaforo(ESTADO_NOMBRE.get(peor))}{marca}</td>
<td>{g['alerts']}</td>
</tr>""")

    sin = [p for p in datos['projects'] if not p.get('product')]
    huerfanos = ''
    if sin:
        filas_h = ''.join(
            f"<tr><td><a href=\"{e(p['code'])}.html\">{e(p['code'])}</a></td>"
            f"<td>{e(p.get('name'))}</td></tr>" for p in sin)
        huerfanos = f"""<h2>Proyectos que no dicen qué producto construyen</h2>
<p>No es un error de ellos: <strong>hay proyectos que no construyen un producto</strong> —una
migración de infraestructura, una obligación regulatoria—. Pero mientras no esté dicho, su
avance no se ve desde el lado del producto, y nadie puede responder «¿cómo va la cuenta
transaccional?» sin abrirlos uno por uno.</p>
<table><tr><th>Proyecto</th><th>Nombre</th></tr>{filas_h}</table>"""

    cuerpo = f"""<span class="ante">Productos</span>
<h1>{plural(len(datos.get('products') or []), 'producto', 'productos')} en construcción</h1>
<p class="pie-cab">Al {e(datos['as_of'])} · salen de lo que cada proyecto declara en su acta ·
entra en cualquiera para ver qué lo construye</p>
<table><tr><th>Producto</th><th>Lo construyen</th><th>Comité</th>
<th>Lo peor que declaran</th><th>Señales</th></tr>
{''.join(filas) or '<tr><td colspan="5" class="vacio">Ningún proyecto declara un producto.</td></tr>'}</table>
{huerfanos}"""
    return pagina('Productos', cuerpo, hoy, barra('productos', org))


def con_cifra(p, senal):
    """El nombre de la señal con su número, cuando lo tiene.

    «en silencio» y «en silencio desde hace 153 días» no dicen lo mismo, y es la
    segunda la que mueve a alguien a decidir.
    """
    nombre = NOMBRES.get(senal, senal)
    for a in p['alerts']:
        if a['signal'] != senal:
            continue
        d = a['detail'] or {}
        if senal == 'silent' and d.get('days') is not None:
            return f"{nombre} desde hace {plural(d['days'], 'día', 'días')}"
        if senal in ('variance_time',) and d.get('days') is not None:
            return f"{nombre}: {plural(d['days'], 'día', 'días')}"
        if senal in ('variance_cost',) and d.get('pct') is not None:
            return f"{nombre}: {pct(d['pct'])} sobre lo aprobado"
        if senal == 'budget_committed' and d.get('pct') is not None:
            return f"{nombre}: {pct(d['pct'])}"
        break
    return nombre


def vista_decisiones(datos, fichas, hoy, org=None):
    """Por decisión, no por campo. Otro objeto, no la interna recortada."""
    decisiones = []
    con_punto = set()
    for p in sorted(datos['projects'], key=lambda x: x['code']):
        nombre = f"{p['code']} · {p.get('name') or ''}".strip(' ·')
        antes = len(decisiones)
        por_senal = {}
        for a in p['alerts']:
            por_senal.setdefault(a['signal'], []).append(a['detail'])

        if 'declared_vs_evidence' in por_senal:
            d = por_senal['declared_vs_evidence'][0]
            faltan = ', '.join(con_cifra(p, x) for x in d.get('signals', []))
            decisiones.append((nombre,
                '¿Se mantiene el estado reportado, o se corrige?',
                [('Qué se declaró', f"{d.get('declared')}, el {d.get('as_of')}"),
                 ('Qué no explica ese estado', faltan),
                 ('Si no se decide', 'el comité sigue decidiendo sobre un estado que la evidencia no sostiene')]))

        if 'rebaseline_unauthorized' in por_senal:
            d = por_senal['rebaseline_unauthorized'][0]
            decisiones.append((nombre,
                '¿Se ratifican los días que la línea base se movió de más?',
                [('La línea base se movió', plural(d.get('moved') or 0, 'día', 'días')),
                 ('Los cambios aprobados autorizan', plural(d.get('authorized') or 0, 'día', 'días')),
                 ('Ningún documento autoriza', plural(d.get('days') or 0, 'día', 'días')),
                 ('Si no se decide', 'la desviación se reporta contra una fecha que nadie aprobó')]))

        for d in por_senal.get('vendor_invoiced_over_accepted', []):
            declarados = d.get('amounts_declared')
            decisiones.append((nombre,
                f"¿Se aprueba la facturación de {e(d.get('vendor'))} por encima de lo aceptado?",
                [('Facturado', plata(d.get('invoiced'))),
                 ('Entregables aceptados', plata(d.get('accepted_amount'))),
                 ('Diferencia', plata(d.get('difference'))),
                 ('Entregables con monto en el contrato',
                  declarados if declarados else 'no está dicho en ninguna parte'),
                 ('Si no se decide', 'se paga contra entregables que ningún acta sustenta')]))

        for d in por_senal.get('governance_change', []):
            decisiones.append((nombre,
                '¿Quién es hoy el responsable de este rol?',
                [('Dice un documento', f"{d.get('value')} — {d.get('source')}"),
                 ('Dice otro', f"{(d.get('conflict') or {}).get('value')} — {(d.get('conflict') or {}).get('source')}"),
                 ('Si no se decide', 'no hay a quién escalar lo que se escale')]))

        if len(decisiones) > antes:
            con_punto.add(p['code'])

    bloques = ''.join(f"""<div class="decision">
<span class="ante">{e(proy)}</span>
<p class="p">{e(preg)}</p>
<dl>{''.join(f'<dt>{e(k)}</dt><dd>{e(v)}</dd>' for k, v in datos_d)}</dl>
</div>""" for proy, preg, datos_d in decisiones)

    if not decisiones:
        bloques = """<div class="bloque info"><h2 class="t">No hay decisiones pendientes</h2>
<p>Nada de lo que el agente encontró excede la autoridad de quien gerencia cada proyecto.
Eso no significa que todo vaya bien: significa que nada requiere una decisión de este
comité.</p></div>"""

    total = len(datos['projects'])
    alcance = (f"{plural(len(decisiones), 'punto', 'puntos')}, "
               f"en {len(con_punto)} de {plural(total, 'proyecto', 'proyectos')}"
               if decisiones else f"ningún punto, sobre {plural(total, 'proyecto', 'proyectos')}")
    cuerpo = f"""<p class="migas"><a href="index.html">Informes PMO</a> · Decisiones</p>
<span class="ante">Comité · vista de decisiones</span>
<h1>Lo que necesita una decisión</h1>
<p class="pie-cab">Al {e(datos['as_of'])} · {alcance} · la cadena de evidencia completa está
en <a href="index.html">el informe del portafolio</a> y en la página de cada proyecto</p>
{bloques}"""
    return pagina('Comité · decisiones', cuerpo, hoy, barra('pmo', org))


def vista_producto(g, datos, fichas, hoy, org):
    """El informe de un producto.

    Un producto no tiene ficha propia y **no se le va a inventar una**. Todo lo que
    aquí se dice sale de los proyectos que declararon construirlo, y se dice con esa
    salvedad. Lo que un producto real tiene y esta carpeta no —adopción, ingreso,
    incidencias en producción— no aparece, porque no está.

    Lo que sí aporta, y no existe en ninguna otra página: que dos comités estén
    mirando el mismo producto sin saberlo, y que el proyecto sano no lo salve si el
    otro no llega.
    """
    suyos = [p for p in datos['projects'] if p['code'] in g['projects']]
    suyos.sort(key=lambda x: (-len(x['alerts']), x['code']))

    comites, patrocinadores = {}, {}
    for p in suyos:
        rec = fichas.get(p['code'], {})
        for ruta, bolsa in (('identity.committee', comites), ('identity.sponsor', patrocinadores)):
            v = campo(rec, ruta)[0]
            if v:
                bolsa.setdefault(v, []).append(p['code'])

    # Cuándo aterriza: la más lejana de sus fechas de cierre, con quién la pone.
    fechas = [(p.get('end_date'), p['code']) for p in suyos if p.get('end_date')]
    fechas.sort()
    sin_fecha = [p['code'] for p in suyos if not p.get('end_date')]
    if fechas:
        aterriza = e(fechas[-1][0])
        pie_fecha = (f"Cuando cierre el último de sus proyectos. La fecha más lejana la "
                     f"pone {e(fechas[-1][1])}")
        if sin_fecha:
            pie_fecha += f", y {', '.join(e(c) for c in sin_fecha)} no declara ninguna"
    else:
        aterriza = 'no se sabe'
        pie_fecha = 'Ninguno de sus proyectos declara fecha de cierre'

    # El dinero solo se suma si todos lo declaran. Media suma es un número falso.
    aprobados = [(p['money'] or {}).get('approved') for p in suyos]
    if aprobados and all(x is not None for x in aprobados):
        dinero = plata(sum(aprobados))
        pie_dinero = ('Suma de lo aprobado a cada proyecto. No es un presupuesto de '
                      'producto: nadie aprobó esa cifra junta')
    else:
        faltan = [p['code'] for p, a in zip(suyos, aprobados) if a is None]
        dinero = 'no se puede sumar'
        pie_dinero = (f'{", ".join(e(c) for c in faltan)} no declara presupuesto, y media '
                      f'suma es un número falso')

    filas = ''.join(f"""<tr>
<td><a href="{e(p['code'])}.html"><strong>{e(p['code'])}</strong></a><br>{e(p.get('name'))}</td>
<td>{semaforo((p.get('declared') or {}).get('status'))}</td>
<td>{con_cita(fichas.get(p['code'], {}), 'identity.committee')}</td>
<td>{senales(p['alerts'], p)}</td>
</tr>""" for p in suyos)

    # El hallazgo propio de esta página.
    hallazgos = []
    if len(comites) > 1:
        detalle = '; '.join(f'{e(k)} mira {", ".join(e(c) for c in v)}'
                            for k, v in sorted(comites.items()))
        hallazgos.append(
            f'<h3>Ningún comité ve este producto completo</h3>'
            f'<p>Lo construyen {plural(len(suyos), "proyecto", "proyectos")} que reportan a '
            f'<strong>{plural(len(comites), "comité distinto", "comités distintos")}</strong>: '
            f'{detalle}. Cada uno ve su proyecto y ninguno ve el producto, que es exactamente '
            f'lo que esta página existe para mostrar.</p>')
    if len(patrocinadores) > 1:
        hallazgos.append(
            f'<h3>Más de un patrocinador</h3><p>'
            + '; '.join(f'<strong>{e(k)}</strong> responde por {", ".join(e(c) for c in v)}'
                        for k, v in sorted(patrocinadores.items()))
            + '. Si las dos partes no llegan, la pregunta de a quién se le escala el producto '
              'no tiene una respuesta sola.</p>')

    limpios = [p for p in suyos if not p['alerts']]
    con_ruido = [p for p in suyos if p['alerts']]
    if limpios and con_ruido:
        hallazgos.append(
            f'<h3>El proyecto sano no salva al producto</h3>'
            f'<p>{", ".join(e(p["code"]) for p in limpios)} está limpio y '
            f'{", ".join(e(p["code"]) for p in con_ruido)} no. '
            f'<strong>El producto no llega hasta que llegan los dos</strong>, así que el estado '
            f'del producto es el del peor, no el promedio de los dos.</p>')
    if not hallazgos:
        hallazgos.append(
            '<h3>Nada que reportar de este producto</h3>'
            '<p>Un solo proyecto lo construye, un solo comité lo mira, y la evidencia no '
            'contradice lo que declara. Que no haya hallazgo es un resultado, no un vacío.</p>')

    cuerpo = f"""<p class="migas"><a href="productos.html">Productos</a> · {e(g['product'])}</p>
<span class="ante">Informe de producto</span>
<h1>{e(g['product'])}</h1>
<p class="pie-cab">Al {e(datos['as_of'])} · construido a partir de lo que declaran
{plural(len(suyos), 'proyecto', 'proyectos')}</p>

<div class="par">
<div class="cifra"><span class="n">{aterriza}</span><span class="q">{pie_fecha}</span></div>
<div class="cifra"><span class="n">{dinero}</span><span class="q">{pie_dinero}</span></div>
</div>

<h2>Lo que lo construye</h2>
<table><tr><th>Proyecto</th><th>Declara</th><th>Reporta a</th>
<th>Lo que la evidencia dice</th></tr>{filas}</table>

<h2>Lo que se ve desde el producto y no desde el proyecto</h2>
{''.join(hallazgos)}

<div class="bloque info">
<h3>Lo que esta página no puede decir</h3>
<p>De este producto no hay <strong>adopción, ingreso, incidencias en producción ni
satisfacción</strong>, porque nada de eso está en la carpeta de proyectos: son datos de
operación y viven en otro sistema. Lo que hay aquí es <strong>cómo va lo que se está
construyendo</strong>, que es una pregunta distinta y la única que estos documentos
permiten responder.</p>
</div>"""
    return pagina(f"Producto · {g['product']}", cuerpo, hoy, barra('productos', org))


# ---------------------------------------------------------------- el cronograma
# El Gantt y la curva dibujan lo que `portafolio.py compute` dejó en `schedule`: aquí no se
# calcula ni se decide nada. Cada marca lleva su texto (`<title>`) y su estado en palabras, y
# debajo va la misma información en una tabla, para quien no ve el dibujo o lo imprime.

# El ancho del dibujo: cabe en la hoja del informe; en un teléfono el gráfico se desplaza.
ANCHO_GRAFICO = 980
MESES_CORTO = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
ESTADO_HITO = {'met': ('cumplido', OK_), 'pending': ('pendiente', CUERPO),
               'overdue': ('vencido sin evidencia', ERROR),
               'met_without_evidence': ('cumplido sin evidencia', ALERTA)}


def _f(s):
    try:
        return dt.date.fromisoformat(s) if s else None
    except ValueError:
        return None


def _dominio(s):
    """Del primer al último día que aparece en el cronograma, hoy incluido, con un margen."""
    fechas = [_f(s.get('start')), _f(s.get('end')), _f(s.get('today'))]
    for b in s.get('baselines') or []:
        fechas += [_f(b.get('start')), _f(b.get('end'))]
    for h in s.get('milestones') or []:
        fechas += [_f(h.get('baseline')), _f(h.get('current'))]
    fechas = [f for f in fechas if f]
    if len(fechas) < 2:
        return None
    a, b = min(fechas), max(fechas)
    a = a.replace(day=1)
    b = (b.replace(day=28) + dt.timedelta(days=8)).replace(day=1)
    return a, b


def _eje(a, b, x, alto, y0=0, limite=None):
    """Los meses como marcas; con más de un año, uno de cada tres."""
    meses, m = [], a
    while m <= b:
        meses.append(m)
        m = (m.replace(day=28) + dt.timedelta(days=8)).replace(day=1)
    # Una etiqueta de mes pide unos 48 px; si no caben todas, va una de cada dos, tres o seis.
    ancho_mes = (x(b) - x(a)) / max(len(meses), 1)
    paso = next((n for n in (1, 2, 3, 6, 12) if ancho_mes * n >= 48), 12)
    out = []
    for i, m in enumerate(meses):
        if i % paso:
            continue
        xx = x(m)
        if limite is not None and xx + 40 > limite:
            continue
        out.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{alto}" stroke="{FILETE_SUAVE}" stroke-width="1"/>'
                   f'<text x="{xx + 3:.1f}" y="{y0 + 12}" font-size="12" fill="{APAGADO}">'
                   f'{MESES_CORTO[m.month - 1]} {str(m.year)[2:]}</text>')
    return ''.join(out)


def _rombo(cx, cy, r, relleno, borde, titulo):
    pts = f'{cx:.1f},{cy - r:.1f} {cx + r:.1f},{cy:.1f} {cx:.1f},{cy + r:.1f} {cx - r:.1f},{cy:.1f}'
    return (f'<polygon points="{pts}" fill="{relleno}" stroke="{borde}" stroke-width="2">'
            f'<title>{e(titulo)}</title></polygon>')


def _leyenda(items):
    """Cada muestra con su texto, juntos: en un teléfono la leyenda se parte entre elementos."""
    return '<p class="leyenda">' + ''.join(
        f'<span class="i"><span class="{c}" style="{estilo}"></span>{e(texto)}</span>' for c, estilo, texto in items) + '</p>'


def gantt(s):
    """Cada línea base aprobada, el plan vigente y cada hito: dónde estaba y dónde está."""
    dom = _dominio(s or {})
    if not dom:
        return '<p class="vacio">El cronograma no trae fechas suficientes para dibujarlo.</p>'
    a, b = dom
    ancho, izq, der, fila = ANCHO_GRAFICO, 210, 170, 30
    filas = [('base', x) for x in s.get('baselines') or []]
    filas.append(('vigente', None))
    filas += [('hito', h) for h in s.get('milestones') or []]
    alto = 26 + fila * len(filas) + 10
    dias = max((b - a).days, 1)

    def x(f):
        return izq + (ancho - izq - der) * (f - a).days / dias

    partes = [_eje(a, b, x, alto, limite=ancho - der)]
    hoy = _f(s.get('today'))
    for i, (tipo, dato) in enumerate(filas):
        y = 26 + fila * i + fila / 2
        if tipo == 'base':
            ini, fin = _f(dato.get('start')), _f(dato.get('end'))
            etiqueta = f"Línea base {dato.get('version') or i + 1}"
            nota = f"aprobada el {dato.get('approved_on')}" if dato.get('approved_on') else ''
            if ini and fin:
                partes.append(f'<rect x="{x(ini):.1f}" y="{y - 6:.1f}" width="{max(x(fin) - x(ini), 2):.1f}" height="12" rx="4" '
                              f'fill="{FILETE}"><title>{e(etiqueta)}: {e(dato.get("start"))} a {e(dato.get("end"))} · {e(nota)}</title></rect>')
        elif tipo == 'vigente':
            ini, fin = _f(s.get('start')), _f(s.get('end'))
            etiqueta, nota = 'Plan vigente', f"cierre {s.get('end')}" if s.get('end') else 'sin cierre'
            if ini and fin:
                partes.append(f'<rect x="{x(ini):.1f}" y="{y - 6:.1f}" width="{max(x(fin) - x(ini), 2):.1f}" height="12" rx="4" '
                              f'fill="{ORO}"><title>Plan vigente: {e(s.get("start"))} a {e(s.get("end"))}</title></rect>')
        else:
            etiqueta = dato.get('name') or 'Hito sin nombre'
            texto, color = ESTADO_HITO.get(dato.get('status'),
                        ('—', CUERPO))
            nota = texto
            base, act = _f(dato.get('baseline')), _f(dato.get('current'))
            if base and act and base != act:
                partes.append(f'<line x1="{x(base):.1f}" y1="{y:.1f}" x2="{x(act):.1f}" y2="{y:.1f}" '
                              f'stroke="{APAGADO}" stroke-width="2"/>')
            if base:
                partes.append(_rombo(x(base), y, 6, CREMA, APAGADO, f"{etiqueta}: línea base {dato.get('baseline')}"))
            if act:
                partes.append(_rombo(x(act), y, 7, color, color,
                                     f"{etiqueta}: vigente {dato.get('current')} · {texto}"))
        partes.append(f'<text x="0" y="{y + 4:.1f}" font-size="13" fill="{TINTA}">{e(_recorta(etiqueta, 30))}</text>')
        partes.append(f'<text x="{ancho - der + 12}" y="{y + 4:.1f}" font-size="12" fill="{APAGADO}">{e(nota)}</text>')
    if hoy and a <= hoy <= b:
        partes.append(f'<line x1="{x(hoy):.1f}" y1="18" x2="{x(hoy):.1f}" y2="{alto}" stroke="{TINTA}" '
                      f'stroke-width="1.5" stroke-dasharray="4 3"/>'
                      f'<text x="{x(hoy) + 4:.1f}" y="{alto - 4}" font-size="12" fill="{TINTA}">hoy</text>')
    desc = (f"{len(s.get('baselines') or [])} líneas base, el plan vigente y {len(s.get('milestones') or [])} hitos, "
            f"del {a.isoformat()} al {b.isoformat()}. La misma información está en la tabla de hitos.")
    return (f'<div class="grafico" tabindex="0" role="region" aria-label="Gantt de línea base contra vigente">'
            f'<svg viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" role="img" aria-labelledby="gt gd">'
            f'<title id="gt">Línea base contra vigente</title><desc id="gd">{e(desc)}</desc>'
            f'{"".join(partes)}</svg></div>'
            + _leyenda([('m', f"background:{FILETE}", 'línea base aprobada'),
                        ('m', f"background:{ORO}", 'plan vigente'),
                        ('r', f"border-color:{APAGADO};background:{CREMA}", 'hito en la línea base'),
                        ('r', f"border-color:{OK_};background:{OK_}", 'cumplido'),
                        ('r', f"border-color:{CUERPO};background:{CUERPO}", 'pendiente'),
                        ('r', f"border-color:{ERROR};background:{ERROR}", 'vencido sin evidencia'),
                        ('r', f"border-color:{ALERTA};background:{ALERTA}", 'cumplido sin evidencia')]))


def curva(s, declarado=None):
    """Qué parte de los hitos debía estar cumplida en cada fecha, y cuál lo está con evidencia."""
    c = (s or {}).get('curve')
    dom = _dominio(s or {})
    if not c or not dom:
        return '<p class="vacio">Sin hitos en el cronograma no hay curva de avance.</p>'
    a, b = dom
    ancho, izq, der, arriba, abajo = ANCHO_GRAFICO, 44, 20, 24, 30
    alto = 230
    dias = max((b - a).days, 1)
    hoy = _f(s.get('today'))

    def x(f):
        return izq + (ancho - izq - der) * (f - a).days / dias

    def y(p):
        return arriba + (alto - arriba - abajo) * (1 - p / 100)

    inicio = _f(s.get('start')) or a

    def camino(puntos, hasta):
        d = f'M{x(inicio):.1f},{y(0):.1f}'
        for pnt in puntos:
            f = _f(pnt['date'])
            if f:
                d += f' H{x(f):.1f} V{y(pnt["pct"]):.1f}'
        return d + f' H{x(hasta):.1f}'

    partes = [_eje(a, b, x, alto - abajo, arriba - 14, limite=ancho)]
    for p in (0, 50, 100):
        partes.append(f'<line x1="{izq}" y1="{y(p):.1f}" x2="{ancho - der}" y2="{y(p):.1f}" stroke="{FILETE_SUAVE}"/>'
                      f'<text x="{izq - 6}" y="{y(p) + 4:.1f}" font-size="12" fill="{APAGADO}" text-anchor="end">{p} %</text>')
    partes.append(f'<path d="{camino(c["baseline"], b)}" fill="none" stroke="{APAGADO}" stroke-width="2" '
                  f'stroke-dasharray="6 4"><title>Plan de la línea base</title></path>')
    partes.append(f'<path d="{camino(c["current"], b)}" fill="none" stroke="{ORO}" stroke-width="2">'
                  f'<title>Plan vigente</title></path>')
    if hoy:
        partes.append(f'<path d="{camino(c["met"], min(hoy, b))}" fill="none" stroke="{OK_}" stroke-width="2.5">'
                      f'<title>Cumplidos con evidencia</title></path>')
    for pnt in c['met']:
        f = _f(pnt['date'])
        if f:
            partes.append(f'<circle cx="{x(f):.1f}" cy="{y(pnt["pct"]):.1f}" r="4.5" fill="{OK_}" stroke="{CREMA}" stroke-width="2">'
                          f'<title>{pnt["pct"]} % de los hitos cumplidos con evidencia al {pnt["date"]}</title></circle>')
    if declarado and declarado.get('pct') is not None and _f(declarado.get('date')):
        f = _f(declarado['date'])
        if a <= f <= b:
            partes.append(_rombo(x(f), y(declarado['pct']), 7, CREMA, TINTA,
                                 f"Avance declarado: {pct(declarado['pct'])} al {declarado['date']}"))
            partes.append(f'<text x="{x(f) + 12:.1f}" y="{y(declarado["pct"]) + 4:.1f}" font-size="12" '
                          f'fill="{TINTA}">declarado {e(pct(declarado["pct"]))}</text>')
    if hoy and a <= hoy <= b:
        partes.append(f'<line x1="{x(hoy):.1f}" y1="{arriba}" x2="{x(hoy):.1f}" y2="{alto - abajo}" stroke="{TINTA}" '
                      f'stroke-width="1.5" stroke-dasharray="4 3"/>'
                      f'<text x="{x(hoy) + 4:.1f}" y="{alto - abajo - 6}" font-size="12" fill="{TINTA}">hoy</text>')
    desc = (f"El porcentaje de los {c['milestones']} hitos que debía estar cumplido según la línea base y según el "
            f"plan vigente, y el que está cumplido con evidencia. Cuenta hitos, no esfuerzo.")
    return (f'<div class="grafico" tabindex="0" role="region" aria-label="Curva de avance por hitos">'
            f'<svg viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" role="img" aria-labelledby="ct cd">'
            f'<title id="ct">Curva de avance por hitos</title><desc id="cd">{e(desc)}</desc>'
            f'{"".join(partes)}</svg></div>'
            + _leyenda([('l', f"border-top:2px dashed {APAGADO}", 'plan de la línea base'),
                        ('l', f"border-top:2px solid {ORO}", 'plan vigente'),
                        ('l', f"border-top:3px solid {OK_}", 'cumplidos con evidencia'),
                        ('r', f"border-color:{TINTA};background:{CREMA}", 'avance declarado')])
            + f'<p class="cita">La curva cuenta hitos, no esfuerzo: un hito cumplido sin evidencia no suma.</p>')


def corrimiento(dias):
    """«63 días después», «7 días antes» o «a tiempo»: un signo menos no se lee en voz alta."""
    if dias is None:
        return '—'
    if dias == 0:
        return 'a tiempo'
    return f"{plural(abs(dias), 'día', 'días')} {'después' if dias > 0 else 'antes'}"


def tabla_hitos(s):
    hitos = (s or {}).get('milestones') or []
    if not hitos:
        return ''
    filas = ''.join(
        f"<tr><td data-col=\"Hito\">{e(h.get('name'))}</td><td data-col=\"Línea base\">{e(h.get('baseline') or '—')}</td>"
        f"<td data-col=\"Vigente\">{e(h.get('current') or '—')}</td>"
        f"<td data-col=\"Corrimiento\">{corrimiento(h.get('slip_days'))}</td>"
        f"<td data-col=\"Estado\">{e(ESTADO_HITO.get(h.get('status'),
                        ('—',))[0])}</td></tr>"
        for h in hitos)
    return ('<table class="apila"><thead><tr><th>Hito</th><th>Línea base</th><th>Vigente</th><th>Corrimiento</th>'
            f'<th>Estado</th></tr></thead><tbody>{filas}</tbody></table>')


def vista_proyecto(p, rec, hoy, org=None):
    d = p.get('declared', {})
    money = p.get('money', {})
    prod = p.get('product')

    hitos = ''.join(
        f"<tr><td>{e(m.get('name'))}</td><td>{e(m.get('due'))}</td>"
        f"<td>{plural(m.get('days') or 0, 'día', 'días')}</td></tr>"
        for m in p.get('milestones_overdue', []))
    hitos = f'<table><tr><th>Hito</th><th>Fecha</th><th>Vencido hace</th></tr>{hitos}</table>' \
        if hitos else '<p class="vacio">Ninguno vencido sin evidencia.</p>'

    comp = ''.join(
        f"<tr><td>{e(c.get('who'))}</td><td>{e(c.get('what'))}</td>"
        f"<td>{e(c.get('due'))}<span class=\"cita\">{e(c.get('source'))}</span></td></tr>"
        for c in p.get('commitments_overdue', []))
    comp = f'<table><tr><th>Quién</th><th>Qué</th><th>Prometido para</th></tr>{comp}</table>' \
        if comp else '<p class="vacio">Ninguno vencido.</p>'

    faltan = p.get('fields_missing') or []
    vacios = ''.join(f'<li>{e(nombre_campo(rec, x))}</li>' for x in faltan)
    vacios = (f'<ul>{vacios}</ul>' if vacios
              else '<p class="vacio">Nada de lo que la ficha espera quedó sin decir.</p>')

    # El enlace al producto que le dio origen. Es de ida y vuelta a propósito: quien
    # entra por el proyecto quiere saber para qué es, y quien entra por el producto
    # quiere saber quién lo está haciendo.
    if prod:
        origen = (f'<p class="migas"><a href="proyectos.html">Proyectos</a> · {e(p["code"])} · '
                  f'construye <a href="{archivo_producto(prod)}">{e(prod)}</a></p>')
    else:
        origen = (f'<p class="migas"><a href="proyectos.html">Proyectos</a> · {e(p["code"])} · '
                  f'<span class="vacio">no dice qué producto construye</span></p>')

    cuerpo = f"""{origen}
<span class="ante">{e(p['code'])}</span>
<h1>{e(p.get('name') or p['code'])}</h1>
<p class="pie-cab">Al {e(hoy)}</p>

<div class="bloque">
<h2 class="t">La declaración y la evidencia</h2>
<p><strong>Declara:</strong> {semaforo(d.get('status'))}
{f"· {pct(d.get('progress_pct'))} de avance" if d.get('progress_pct') is not None else ''}
· al {e(d.get('as_of'))}
{f"· hace {plural(d['age_days'], 'día', 'días')}" if d.get('age_days') is not None else ''}</p>
<p><strong>Lo que ese estado no explica:</strong> {senales(p['alerts'], p)}</p>
</div>

<h2>Gobierno</h2>
<table>
<tr><th>Campo</th><th>Qué dicen los documentos</th></tr>
<tr><td>Patrocinador</td><td>{con_cita(rec, 'identity.sponsor')}</td></tr>
<tr><td>Gerente</td><td>{con_cita(rec, 'identity.manager')}</td></tr>
<tr><td>Comité</td><td>{con_cita(rec, 'identity.committee')}</td></tr>
<tr><td>Autoridad del gerente</td><td>{con_cita(rec, 'identity.authority')}</td></tr>
<tr><td>Producto</td><td>{con_cita(rec, 'identity.product')}</td></tr>
</table>

<h2>Contra el plan</h2>
<table>
<tr><th>Medida</th><th>Valor</th></tr>
<tr><td>Fecha de cierre vigente</td><td>{con_cita(rec, 'plan.end_date')}</td></tr>
<tr><td>Desviación contra la línea base original</td>
    <td>{'—' if p.get('slip_vs_original_days') is None else plural(p['slip_vs_original_days'], 'día', 'días')}</td></tr>
<tr><td>Desviación contra la vigente</td>
    <td>{'—' if p.get('slip_vs_current_days') is None else plural(p['slip_vs_current_days'], 'día', 'días')}</td></tr>
<tr><td>Replanificaciones</td><td>{p.get('replans', 0)}</td></tr>
<tr><td>Días que ningún documento autoriza</td>
    <td>{'—' if (p.get('changes') or {}).get('unauthorized_days') is None
         else plural(p['changes']['unauthorized_days'], 'día', 'días')}</td></tr>
</table>

<h2>El cronograma: línea base contra vigente</h2>
{gantt(p.get('schedule'))}
{tabla_hitos(p.get('schedule'))}

<h2>La curva de avance</h2>
{curva(p.get('schedule'), {'pct': d.get('progress_pct'), 'date': d.get('as_of')})}

<h2>Dinero</h2>
<table>
<tr><th>Aprobado</th><th>Comprometido</th><th>Ejecutado</th><th>Proyección</th><th>Disponible real</th></tr>
<tr><td>{plata(money.get('approved'))}</td>
<td>{plata(money.get('committed'))}<span class="cita">{pct(money.get('pct_committed'))} de lo aprobado</span></td>
<td>{plata(money.get('executed'))}<span class="cita">{pct(money.get('pct_executed'))} de lo aprobado</span></td>
<td>{plata(money.get('projection'))}<span class="cita">{
    '—' if money.get('projection_over_pct') is None
    else (f"{pct(money['projection_over_pct'])} por encima" if money['projection_over_pct'] > 0
          else f"{pct(abs(money['projection_over_pct']))} por debajo")}</span></td>
<td>{plata(money.get('available_real'))}</td></tr>
</table>

<h2>Hitos vencidos sin evidencia</h2>{hitos}
<h2>Compromisos vencidos</h2>{comp}
<h2>Lo que no está dicho en ninguna parte</h2>{vacios}"""
    return pagina(f"{p['code']} · {p.get('name') or ''}", cuerpo, hoy,
                  barra('proyectos', org))


# ---------------------------------------------------------------- correr

def nombre_organizacion(config: Path | None) -> str:
    """De quién es esta oficina de proyectos. Sale de la configuración y no se
    inventa: un portal que dice «Portafolio» a secas no es de nadie."""
    if not config or not config.exists():
        return ''
    try:
        cfg = json.loads(config.read_text(encoding='utf-8'))
    except (json.JSONDecodeError, OSError):
        return ''
    return str((cfg.get('organization') or {}).get('name') or '').strip()


def generar(state: Path, salida: Path, config: Path | None, hoy: dt.date) -> dict:
    sys.path.insert(0, str(Path(__file__).parent))
    import portafolio

    th = portafolio.load_thresholds(config)
    datos = portafolio.compute(state, hoy, th)
    org = nombre_organizacion(config)
    fichas = {}
    for f in sorted((state / 'records').glob('*.json')):
        rec = json.loads(f.read_text(encoding='utf-8'))
        fichas[portafolio.value(rec.get('identity', {}).get('code')) or f.stem] = rec

    salida.mkdir(parents=True, exist_ok=True)
    hoy_s = hoy.isoformat()
    escribir = lambda n, h: (salida / n).write_text(h, encoding='utf-8')

    escribir('index.html', vista_pmo(datos, fichas, hoy_s, org))
    escribir('decisiones.html', vista_decisiones(datos, fichas, hoy_s, org))
    escribir('proyectos.html', vista_proyectos(datos, fichas, hoy_s, org))
    escribir('productos.html', vista_productos(datos, fichas, hoy_s, org))
    for p in datos['projects']:
        escribir(f"{p['code']}.html",
                 vista_proyecto(p, fichas.get(p['code'], {}), hoy_s, org))
    productos = datos.get('products') or []
    for g in productos:
        escribir(archivo_producto(g['product']), vista_producto(g, datos, fichas, hoy_s, org))

    return {'paginas': 4 + len(datos['projects']) + len(productos), 'salida': str(salida),
            'organizacion': org or None,
            'proyectos': len(datos['projects']), 'productos': len(productos),
            'proyectos_sin_producto': [p['code'] for p in datos['projects']
                                       if not p.get('product')],
            'verdes_contradichos': datos['totals']['green_contradicted']}


# ---------------------------------------------------------------- comprobarse

def selftest() -> int:
    """Lo que este informe puede romper sin que nadie lo note.

    Una ruta de la ficha impresa tal cual —`plan.milestones[1].evidence`— no se ve
    mal: se ve técnica, y quien la lee supone que así se dice. Por eso se comprueba
    aquí y no a ojo.
    """
    fallas = []

    def ok(que, real, esperado):
        if real != esperado:
            fallas.append(f'{que}: {real!r} en vez de {esperado!r}')
        print(f'{"  ok  " if real == esperado else " FALLA"} {que}')

    # ── WCAG 2.2 AA: lo que se puede comprobar sin navegador. El recorrido con axe-core está
    # en tests/criterio-server/accesibilidad.mjs; esto es lo que no puede volver atrás sin que
    # una puerta lo diga.
    def contraste(a_, b_):
        def lum(h):
            c = [int(h.lstrip('#')[k:k + 2], 16) / 255 for k in (0, 2, 4)]
            c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
            return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
        la, lb = sorted((lum(a_), lum(b_)), reverse=True)
        return (la + 0.05) / (lb + 0.05)
    fondos = (CREMA, PANEL, PANEL_ALTO, LAVADO_ORO, '#ffffff')
    textos = (TINTA, CUERPO, APAGADO, APAGADO_FRIO, ORO, ERROR, OK_, ALERTA, INFO)
    ok('todo texto contra todo fondo de la paleta llega a 4,5:1 (WCAG 1.4.3)',
       [(t, f) for t in textos for f in fondos if contraste(t, f) < 4.5], [])
    ok('cada estado contra su fondo llega a 4,5:1',
       [(t, f) for t, f in ((OK_, OK_FONDO), (ERROR, ERROR_FONDO), (ALERTA, ALERTA_FONDO), (INFO, INFO_FONDO))
        if contraste(t, f) < 4.5], [])
    ok('el borde de un campo y el foco se distinguen del fondo a 3:1 (WCAG 1.4.11)',
       min(contraste(APAGADO, '#ffffff'), contraste(ORO, '#ffffff'), contraste(ORO, CREMA)) >= 3, True)
    tamanos = [float(x) for x in re.findall(r'font-size:\s*([0-9.]+)rem', CSS)]
    ok('ninguna letra por debajo de 12 px (.75rem)', [x for x in tamanos if x < .75], [])
    # El Gantt y la curva: lo que dibujan sale de `schedule`, con su texto y su tabla.
    sch = {'start': '2026-01-15', 'end': '2026-11-30', 'today': '2026-09-29',
           'baselines': [{'version': 1, 'approved_on': '2026-01-12', 'start': '2026-01-15', 'end': '2026-09-30'}],
           'milestones': [{'name': 'Diseño', 'baseline': '2026-03-02', 'current': '2026-03-06', 'status': 'met',
                           'evidence': True, 'slip_days': 4},
                          {'name': 'Motor', 'baseline': '2026-05-29', 'current': '2026-07-31', 'status': 'overdue',
                           'evidence': False, 'slip_days': 63}],
           'curve': {'milestones': 2, 'baseline': [{'date': '2026-03-02', 'pct': 50}, {'date': '2026-05-29', 'pct': 100}],
                     'current': [{'date': '2026-03-06', 'pct': 50}, {'date': '2026-07-31', 'pct': 100}],
                     'met': [{'date': '2026-03-06', 'pct': 50}]}}
    g, c = gantt(sch), curva(sch, {'pct': 45, 'date': '2026-09-20'})
    ok('el Gantt y la curva son imágenes con título y descripción, y se desplazan con el teclado (WCAG 1.1.1, 2.1.1)',
       all('role="img"' in x and '<desc id=' in x and 'tabindex="0"' in x for x in (g, c)), True)
    ok('cada hito dice su estado en palabras, no solo en color (WCAG 1.4.1)',
       ('vencido sin evidencia' in g, 'cumplido' in g), (True, True))
    ok('ningún texto del Gantt ni de la curva por debajo de 12 px',
       [x for x in re.findall(r'font-size="([0-9.]+)"', g + c) if float(x) < 12], [])
    ok('la tabla de hitos trae lo mismo que el Gantt', tabla_hitos(sch).count('<tr>'), 3)
    ok('sin fechas no se dibuja nada inventado', 'vacio' in gantt({}) and 'vacio' in curva({}), True)
    muestra = pagina('Prueba', '<h1>Prueba</h1><h2>Uno</h2><table><thead><tr><th>A</th><th>B</th><th>C</th>'
                     '<th>D</th></tr></thead><tbody><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr></tbody></table>'
                     '<h2>Uno</h2><table><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th></tr></thead>'
                     '<tbody><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr></tbody></table>', '2026-10-21')
    ok('la página tiene idioma, salto al contenido, main y pie (WCAG 2.4.1, 1.3.1)',
       all(x in muestra for x in ('<html lang="es">', 'href="#contenido"', '<main id="contenido"', '<footer')), True)
    ok('cada tabla en su región, con un nombre que no repite el de otra (WCAG 1.3.1, 2.1.1)',
       re.findall(r'aria-label="([^"]+)"', muestra), ['Uno: A, B, C, D', 'Uno: A, B, C, D (2)'])
    ok('en un teléfono la tabla ancha se lee fila por fila: cada celda dice su columna',
       'class="apila"' in muestra and 'data-col="D">4<' in muestra, True)

    ok('plural en singular', plural(1, 'día', 'días'), '1 día')
    ok('plural en plural', plural(0, 'día', 'días'), '0 días')
    ok('plural en negativo', plural(-1, 'día', 'días'), '-1 día')
    ok('porcentaje sin cola', pct(78.0), '78%')
    ok('porcentaje con coma', pct(95.23), '95,2%')
    ok('porcentaje ausente', pct(None), '—')
    ok('monto', plata(1850000000), '1.850.000.000')

    import os, tempfile
    with tempfile.TemporaryDirectory() as t:
        raiz = Path(t).resolve()
        cfg = raiz / '.criterio' / 'portafolio' / 'config.json'
        cfg.parent.mkdir(parents=True)
        cfg.write_text(json.dumps({'paths': {'reports': 'reportes'}}), encoding='utf-8')
        (raiz / 'estado').mkdir()
        antes = os.getcwd()
        os.chdir(raiz / 'estado')
        try:
            ok('el informe va a la raíz del espacio aunque el shell esté en estado/',
               carpeta_informe(cfg, None), (raiz / 'reportes', None))
            ok('y una --salida relativa a otro lado se rechaza',
               carpeta_informe(cfg, Path('reportes'))[0], None)
        finally:
            os.chdir(antes)

    ficha = {
        'plan': {'milestones': [{'name': {'value': 'Salida a producción'},
                                 'evidence': {'value': None}}]},
        'raid': {'risks': [{'what': {'value': 'Una frase larguísima ' * 6},
                            'owner': {'value': None}}]},
        'vendors': [{'name': {'value': 'Nubetec'},
                     'deliverables': [{'name': {'value': 'Landing zone'},
                                       'evidence': {'value': None}}]}],
    }
    ok('no encontrado no se imprime', 'not_found' in con_cita(
        {'identity': {'authority': {'value': 'not_found', 'state': 'not_found'}}}, 'identity.authority'), False)
    # Cada campo del esquema, dicho en castellano: ninguna ruta ni palabra del esquema
    # llega a quien lee. En la ronda 2 `identity.phase` salió así en los 52 proyectos.
    crudos = []
    for r in hojas_del_esquema() + ['pm_record.identity.phase', 'pm_record.declared.status']:
        n = nombre_campo({}, r)
        hoja = re.sub(r'\[\d+\]', '', r).split('.')[-1]
        if re.search(r'[_\[]|\w\.\w', n) or re.search(r'\b' + re.escape(hoja) + r'\b', n):
            crudos.append(f'{r} → {n}')
    ok('cada campo del esquema tiene nombre en castellano', crudos, [])
    ok('campo simple', nombre_campo(ficha, 'identity.authority'),
       'Hasta dónde decide el gerente sin subir al comité')
    ok('elemento de lista', nombre_campo(ficha, 'plan.milestones[0].evidence'),
       'La evidencia del hito «Salida a producción»')
    ok('lista anidada', nombre_campo(ficha, 'vendors[0].deliverables[0].evidence'),
       'La evidencia del entregable «Landing zone»')
    ok('rótulo alterno', nombre_campo(ficha, 'raid.risks[0].owner').startswith(
        'Quién responde por el riesgo «Una frase'), True)
    ok('rótulo recortado', nombre_campo(ficha, 'raid.risks[0].owner').endswith('…»'), True)
    ok('elemento sin rótulo', nombre_campo({}, 'plan.milestones[3].evidence'),
       'La evidencia del hito sin nombre')

    # Ninguna traducción puede devolver algo que siga pareciendo una ruta.
    sospechosas = []
    for ruta in ('identity.sponsor', 'plan.end_date', 'money.approved',
                 'plan.milestones[0].state', 'raid.issues[0].owner',
                 'vendors[0].deliverables[0].amount', 'commitments[0].due'):
        t = nombre_campo(ficha, ruta)
        if '[' in t or ('.' in t and ' ' not in t.split('.')[0]):
            sospechosas.append(f'{ruta} → {t}')
    ok('ninguna ruta cruda sobrevive', sospechosas, [])

    ok('las señales duras están nombradas', sorted(DURAS - set(NOMBRES)), [])
    # Toda señal que el motor emite tiene nombre: Rostrum la muestra en la historia de
    # cada caso, y en la ronda 2 salieron como `milestone_met_without_evidence`.
    motor = (Path(__file__).resolve().parent / 'portafolio.py').read_text(encoding='utf-8')
    ok('toda señal del motor tiene nombre',
       sorted(set(re.findall(r'alert\("([a-z_]+)"', motor)) - set(NOMBRES)), [])

    print()
    if fallas:
        print(f'{len(fallas)} falla(s)')
        return 1
    print('todo pasa')
    return 0


def carpeta_informe(config, salida):
    """Dónde va el informe: `paths.reports` de la configuración, contado desde la raíz del
    espacio —la carpeta que contiene `.criterio/`— y no desde donde esté parado el shell.

    En la ronda 8 (bancos) el shell del agente había quedado dentro de `estado/`, el
    informe salió en `estado/reportes/` y Rostrum respondió 404 en cada página. Una ruta
    relativa se lee contra la raíz del espacio; devuelve (carpeta, error)."""
    reportes = None
    if config and Path(config).is_file():
        reportes = (json.loads(Path(config).read_text(encoding='utf-8')).get('paths') or {}).get('reports')
    if not reportes:
        if salida is None:
            return None, 'sin --salida, la configuración tiene que decir paths.reports'
        return Path(salida), None
    raiz = Path(config).resolve().parents[2]
    destino = Path(reportes).expanduser()
    destino = (destino if destino.is_absolute() else raiz / destino).resolve()
    if salida is not None and Path(salida).resolve() != destino:
        return None, (f'el informe va a {destino} (paths.reports de la configuración): '
                      'es la carpeta que Rostrum sirve. Omite --salida.')
    return destino, None


def main() -> int:
    ap = argparse.ArgumentParser(description='Criterio PMO — el informe.')
    ap.add_argument('--state', type=Path)
    ap.add_argument('--salida', type=Path)
    ap.add_argument('--config', type=Path, default=None)
    ap.add_argument('--today', default=None)
    ap.add_argument('--selftest', action='store_true',
                    help='comprueba las traducciones y el formato, sin estado')
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.state:
        ap.error('--state es obligatorio (o usa --selftest)')
    # El informe tiene un solo lugar: `paths.reports` de la configuración, que es la
    # carpeta que Rostrum sirve. En la ronda 3 (retail) el agente eligió una subcarpeta
    # con fecha y Rostrum respondió 404 en cada página del informe.
    args.salida, error = carpeta_informe(args.config, args.salida)
    if error:
        ap.error(error)
    hoy = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    print(json.dumps(generar(args.state, args.salida, args.config, hoy),
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
