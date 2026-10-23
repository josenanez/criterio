# -*- coding: utf-8 -*-
"""Las piezas gráficas de Criterio, en los dos idiomas.

    pip install pillow cairosvg
    python3 docs/img/graficos.py

Un solo generador para todas, porque comparten vocabulario: fondo negro, un acento
de oro, filetes finos, Inter Tight, y el texto cargando el mensaje. Colores y reglas
en docs/design.md.

Los robots salen de plugins/criterio-server/scripts/robots.py, el mismo archivo con
que el servidor los dibuja y los mismos trazos de josenanez.com: encendido es oro, en
reposo es crema al 38 %, como en el portal. Si cambia un robot, cambia en todas partes.

Sale a docs/img/es/ y docs/img/en/. Los PNG se versionan para que no haya que correr
nada. El GIF de la familia no sale de aquí: se graba del componente del portal, que es
el dueño de la animación (docs/video/). Las fuentes viajan con el repositorio (Inter Tight, SIL Open Font
License); INTER_TIGHT apunta a otra carpeta si se quiere.

Cada figura declara su ritmo vertical en vez de estimarlo. Estimar posiciones es como
se llega a que una frase pise una insignia.
"""
import functools
import io
import json
import os
import sys

import cairosvg
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
sys.path.insert(0, os.path.join(AQUI, '..', '..', 'plugins', 'criterio-server', 'scripts'))
import robots as trazos  # noqa: E402
# El nombre de cada familia —la sigla y la función en palabras— es de familia.json, por medio del
# registro que escribe scripts/familias.py. Aquí no se escribe ninguno.
with open(os.path.join(AQUI, '..', '..', 'plugins', 'criterio-server', 'scripts', 'agentes.json'), encoding='utf-8') as _fh:
    REGISTRO = json.load(_fh)
FAMILIA = {fa['sigla']: fa for fa in REGISTRO['familias']}
FAMILIA_DE = {a['area']: a['familia'] for a in REGISTRO['agentes']}
FUENTES = os.environ.get('INTER_TIGHT', AQUI)
R = os.path.join(FUENTES, 'InterTight-400.ttf')
M5 = os.path.join(FUENTES, 'InterTight-500.ttf')
M6 = os.path.join(FUENTES, 'InterTight-600.ttf')

NEGRO = '#050505'
PANEL = '#0c0c0b'
CREMA = '#f5f4ef'
ORO = '#d5a84b'
ORO_FONDO = '#2a1f0d'
APAGADO = '#8a867e'
FILETE = '#2b2b28'
FILETE_FUERTE = '#4a4740'
TINTA = '#111111'
TINTA_ORO = '#8a6327'


def mezcla(color, fondo, a):
    """`color` con opacidad `a` sobre `fondo`: el GIF no tiene transparencias."""
    uno = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
    dos = [int(fondo[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(round(a * x + (1 - a) * y) for x, y in zip(uno, dos))




def f(ruta, px):
    return ImageFont.truetype(ruta, px)


def sin_glifo(texto):
    """Caracteres que Inter Tight no trae. Una flecha ausente sale como un cuadro
    vacío y no lo nota nadie hasta que la pieza ya está publicada."""
    return [c for c in texto if ord(c) > 0x2000 and c not in '‑–—·…‘’“”€']


def track(d, xy, texto, fuente, fill, tr=3.0):
    x, y = xy
    for ch in texto:
        d.text((x, y), ch, font=fuente, fill=fill)
        x += d.textlength(ch, font=fuente) + tr
    return x


def ancho_track(d, texto, fuente, tr=3.0):
    return sum(d.textlength(c, font=fuente) + tr for c in texto)


def envolver(d, texto, fuente, ancho):
    lineas, linea = [], ''
    for p in texto.split(' '):
        prueba = (linea + ' ' + p).strip()
        if d.textlength(prueba, font=fuente) > ancho and linea:
            lineas.append(linea)
            linea = p
        else:
            linea = prueba
    if linea:
        lineas.append(linea)
    return lineas


def parrafo(d, xy, texto, fuente, fill, ancho, interlinea):
    faltan = sin_glifo(texto)
    assert not faltan, f'la fuente no tiene {faltan!r} en: {texto[:50]}'
    x, y = xy
    for linea in envolver(d, texto, fuente, ancho):
        d.text((x, y), linea, font=fuente, fill=fill)
        y += interlinea
    return y


def insignia(d, xy, texto, activo, derecha=None):
    """La insignia de estado. Con `derecha`, se alinea a ese borde en vez de a `xy[0]`."""
    color = ORO if activo else APAGADO
    fu = f(M6, 18)
    an = ancho_track(d, texto.upper(), fu, 2.4) + 32
    x, y = xy
    if derecha is not None:
        x = derecha - an
    d.rounded_rectangle([(x, y), (x + an, y + 38)], radius=6,
                        fill=ORO_FONDO if activo else None, outline=color, width=2)
    track(d, (x + 16, y + 9), texto.upper(), fu, color, 2.4)
    return y + 38


def titulo(d, xy, antetitulo, texto, ancho, px=54):
    x, y = xy
    if antetitulo:
        track(d, (x, y), antetitulo.upper(), f(M6, 22), ORO, 3.4)
        y += 44
    y = parrafo(d, (x, y), texto, f(M5, px), CREMA, ancho, int(px * 1.24))
    return y


# ══════════════════════════════════════════════════════════════════ contenido

T = {
    'es': {
        # ── emblemas (la función de cada familia sale de su familia.json) ──
        'pmo_fr': 'Proceso la documentación que tu PMO ya tiene, y digo qué no se sostiene.',
        'cfo_fr': 'Cierro contra lo que dicen los documentos, no contra lo que se declara.',
        'clo_fr': 'Sé qué firmaste, qué vence, y a qué te obligaste.',
        'disponible': 'Disponible',
        # ── tarjetas sociales (1200 × 630): el título de cada página y una línea de lo que hacen ──
        'og': {'pmo': ('Extiende la capacidad de tu PMO',
                       'Vera, Samuel y Alba procesan la documentación de cada proyecto, calculan desviaciones y alertas, y preparan el material del comité.'),
               'cfo': ('El cierre y el presupuesto, contra todos sus soportes',
                       'Clara y Tomás procesan cada documento y calculan lo que no cuadra. El estado lo declara siempre una persona.'),
               'clo': ('Lo que la empresa firmó y a qué se obligó, contra sus documentos',
                       'Fidel y Constanza procesan cada contrato y cada obligación, sin opinión jurídica: la decisión es de una persona.'),
               'rostrum': ('Rostrum, el portal de todas las familias',
                           'Lo que pide atención hoy, lo último de cada motor, lo que vence y dónde trabaja cada agente. No calcula ni escribe.')},
        # ── los robots ──
        'rb': {'vera': ('Vera', 'Director de proyectos', 'Para quien responde por el portafolio completo.', 'El portafolio'),
               'samuel': ('Samuel', 'Gerente de proyecto', 'Para quien responde por un proyecto.', 'Un proyecto'),
               'alba': ('Alba', 'Gerente de producto', 'Para quien define qué se construye.', 'Un producto'),
               'rostrum': ('Rostrum', 'El portal', 'Lo que pide atención hoy, de todas las familias, con su rastro.', 'El portal'),
               'clara': ('Clara', 'Contralora', 'Para quien cierra el mes y responde por lo que dicen los libros.', 'El cierre'),
               'tomas': ('Tomás', 'FP&A', 'Para quien pone el presupuesto al lado de lo ejecutado.', 'El presupuesto'),
               'fidel': ('Fidel', 'Contratos', 'Para quien responde por lo que la empresa firmó.', 'Los contratos'),
               'constanza': ('Constanza', 'Cumplimiento', 'Para quien responde por cada obligación y su evidencia.', 'El cumplimiento')},
        'en_prueba': 'Construida · en prueba',
        'declarada': 'Capacidad declarada',
        'construccion': 'En construcción',
        'sin_construir': 'Sin construir',
        # ── familia ──
        'fam_ante': 'La familia',
        'fam_tit': 'Tres agentes, un solo contrato de datos',
        'n1': 'Vera', 'n2': 'Samuel', 'n3': 'Alba',
        'ag1': 'Director de proyectos',
        'ag1_para': 'Para quien responde por el portafolio completo',
        'ag1_desc': 'Cuarenta proyectos. Barrido amplio, cadencia de comité.',
        'ag2': 'Gerente de proyecto',
        'ag2_para': 'Para quien responde por un proyecto',
        'ag2_desc': 'Un proyecto. Profundidad, cadencia por reunión.',
        'ag3': 'Gerente de producto',
        'ag3_para': 'Para quien define qué se construye',
        'ag3_desc': 'Antes de que exista el proyecto.',
        'comparten': 'Lo que comparten',
        'ficha_tit': 'La ficha de proyecto',
        'ficha_desc': 'Cada dato con la cita del documento del que salió, y su fecha. '
                      'Ningún agente vuelve por su cuenta a los documentos crudos.',
        'regla': 'La ficha del gerente es una declaración. El hallazgo de Vera es '
                 'evidencia. Nunca se fusionan, y la diferencia entre las dos es la señal.',
        'propias': 'Propias',
        'q_ante': 'Los primeros quince minutos',
        'q_tit': 'Configurar es una conversación, y termina con un resultado',
        'q': [('0–2 min', 'Instalar', 'Dos comandos, o cuatro clics.'),
              ('2–4 min', 'Mira antes de preguntar', 'Le señalas la carpeta. Lista qué encontró, qué formatos, y qué no va a poder leer.'),
              ('4–8 min', 'Cinco preguntas', 'Una a la vez, cada una con respuesta sugerida. «No sé» vale.'),
              ('8–15 min', 'Un primer resultado', 'Barre tres proyectos, no el portafolio. Qué supo, qué no está dicho, qué se contradice.'),
              ('Después', 'Tú decides la cadencia', 'Corre solo y habla solo cuando algo cruza un umbral.')],
        'f_ante': 'Cómo funciona',
        'f_tit': 'El modelo extrae. El código calcula.',
        'f': ['Tus documentos', 'Texto', 'La ficha', 'Aritmética', 'Señales'],
        'f_sub': ['Como estén, donde estén', 'docx · xlsx · pptx · pdf · eml', 'Cada dato con su cita', 'Determinística y probada', 'Solo lo que cruzó un umbral'],
        'f_extrae': 'El modelo extrae',
        'f_calcula': 'El código calcula',
        'f_nota': 'Ningún número de un informe sale de una estimación. Y lo que no está dicho en ninguna parte se declara, no se rellena.',
        'c_ante': 'El agente no espera a que lo llamen',
        'c_tit': 'Se activa solo, y casi siempre se calla',
        'c_pregunta': '¿Qué toca hoy?',
        'c_ramas': [('Barrido', 'Qué cambió en la carpeta', 'daily_sweep'),
                    ('Informe de comité', 'Aterriza antes, para que alcances a reaccionar', 'committee_next · report_lead_days'),
                    ('Confirmación', 'Cinco campos, los que envejecen peor', 'confirmation.every')],
        'c_silencio': 'Nada cruzó un umbral',
        'c_silencio_sub': 'No produce nada. Esa es la característica: un agente que reporta todas las semanas haya o no noticia se ignora en un mes.',
        'i_ante': 'Instalación',
        'i_tit': 'Cuatro clics, o dos comandos',
        'i_cowork': 'Claude Cowork',
        'i_code': 'Claude Code',
        'i_pasos_cowork': ['Personalizar', 'Explorar plugins, Personal, y el botón +',
                           'Agregar marketplace desde GitHub', 'josenanez/criterio'],
        'i_pasos_code': ['/plugin marketplace add josenanez/criterio', '/plugin install criterio-portfolio@criterio'],
        'i_luego': 'Y después, una sola cosa:',
        's_ante': 'Rostrum · el servidor',
        's_tit': 'El informe, para quien no abre una carpeta',
        's_dentro': ['Tus documentos', 'Vera', 'El informe'],
        's_dentro_sub': [
            'Como estén, donde estén. El agente los lee; nadie más.',
            'Calcula, y escribe la ficha de cada proyecto.',
            'Páginas ya escritas en disco. Dos vistas y una por proyecto.'],
        's_srv': 'Rostrum',
        's_srv_sub': 'Sostiene lo que ya está escrito. No calcula nada al abrir.',
        's_lee': 'solo lee',
        's_lado_dentro': 'Donde el agente trabaja',
        's_lado_fuera': 'Donde está la gente',
        's_quien': ['El comité', 'Quien va a actuar'],
        's_que': ['Lo que necesita una decisión.',
                  'Campo por campo, con la cita de cada dato.'],
        's_vuelta': 'Una petición, que el agente lee al despertar',
        's_nota': 'No autentica a nadie, y es a propósito: se publica detrás del control de acceso que la organización ya tiene. Lo único que escribe es la petición, en su propia carpeta.',
        # ── cómo operan los tres ──
        'fl_ante': 'CÓMO OPERAN LOS TRES',
        'fl_tit': 'Ninguna flecha va de un agente a otro',
        'fl_cajas': [('LA DEFINICIÓN', 'Alba', 'Antes de que exista el proyecto'), ('EL PROYECTO', 'Samuel', 'Un proyecto, cadencia de reunión'), ('EL PORTAFOLIO', 'Vera', 'Cuarenta proyectos, cadencia de comité'), ('EL EQUIPO', 'Rostrum', 'Quien no va a abrir una carpeta')],
        'fl_peticion': 'la petición: revisar · explicar · corregir',
        'fl_traza': '¿se está construyendo mi producto? · Alba procesa la ficha del proyecto',
        'fl_gente': 'Y LAS PERSONAS, QUE NO SE VAN',
        'fl_personas': [('El gerente de producto', 'Habla con el cliente, decide qué se construye y firma el acta.'), ('El gerente de proyecto', 'Dirige la reunión, negocia, y declara el estado de su proyecto.'), ('El gerente de la PMO', 'Decide qué escala y persigue lo que el informe pide.')],
        'fl_nota': 'Todo cruza por un documento. Dos agentes que se hablan directo son dos agentes que hay que desplegar juntos, y el insumo de cada uno lo produce el trabajo no delegable de su persona.',

        'fl_cruza': [('el acta de constitución', 'y con ella nace la ficha del proyecto'),
                     ('ficha-pm.json', 'publicada en la carpeta de gobierno del proyecto, y Vera la procesa como procesa todo lo demás'),
                     ('el informe', 'en una dirección, para quien no va a abrir una carpeta')],
        # ── el único contrato ──
        'ct_ante': 'EL ÚNICO CONTRATO',
        'ct_tit': 'Nada se habla con nada directamente',
        'ct_ficha': 'La ficha de proyecto',
        'ct_ficha_sub': 'Cada dato con la cita del documento del que salió, y su fecha.',
        'ct_escriben': [('Alba', 'La crea, con el acta de constitución'), ('Samuel', 'Escribe la ficha del proyecto, salvo el estado declarado'), ('Vera', 'Escribe su análisis del portafolio, y procesa todas')],
        'ct_lee': ('Rostrum', 'Publica el informe donde el equipo lo lea'),
        'ct_solo_lee': 'solo publica',
        'ct_orden': 'Y EL ORDEN EN EL TIEMPO',
        'ct_tiempo': [('Alba', 'Define. Su entrega cierra con el acta, que es el certificado de nacimiento de la ficha.'), ('Samuel', 'Ejecuta. Un proyecto, con cadencia de reunión.'), ('Vera', 'Vigila el conjunto, con cadencia de comité.')],
        'ct_nota': 'Ningún agente escribe el estado declarado: eso lo escribe una persona. Y la ficha del gerente y el análisis de la PMO no se fusionan nunca — la diferencia entre las dos es el hallazgo.',
    },
    'en': {
        'pmo_fr': 'I process the documentation your PMO already has, and say what does not hold.',
        'cfo_fr': 'I close against what the documents say, not against what is declared.',
        'clo_fr': 'I know what you signed, what expires, and what you committed to.',
        'disponible': 'Available',
        'og': {'pmo': ('Extend your PMO’s capacity',
                       'Vera, Samuel and Alba process every project’s documentation, compute variances and alerts, and prepare the committee material.'),
               'cfo': ('The close and the budget, against all of their evidence',
                       'Clara and Tomás process every document and calculate what does not tie out. The status is always declared by a person.'),
               'clo': ('What the company signed and what it committed to, against its documents',
                       'Fidel and Constanza process every contract and every obligation, with no legal opinion: the decision is a person’s.'),
               'rostrum': ('Rostrum, the portal for every family',
                           'What needs attention today, the latest from each engine, what falls due and where each agent works. It calculates and writes nothing.')},
        'en_prueba': 'Built · in testing',
        # ── the robots ──
        'rb': {'vera': ('Vera', 'Project director', 'For whoever answers for the whole portfolio.', 'The portfolio'),
               'samuel': ('Samuel', 'Project manager', 'For whoever answers for one project.', 'One project'),
               'alba': ('Alba', 'Product manager', 'For whoever defines what gets built.', 'One product'),
               'rostrum': ('Rostrum', 'The portal', 'What needs attention today, across every family, with its trail.', 'The portal'),
               'clara': ('Clara', 'Controller', 'For whoever closes the month and answers for what the books say.', 'The close'),
               'tomas': ('Tomás', 'FP&A', 'For whoever puts the budget next to actual spend.', 'The budget'),
               'fidel': ('Fidel', 'Contracts', 'For whoever answers for what the company signed.', 'The contracts'),
               'constanza': ('Constanza', 'Compliance', 'For whoever answers for every obligation and its evidence.', 'Compliance')},
        'declarada': 'Declared capability',
        'construccion': 'Being built',
        'sin_construir': 'Not built',
        'fam_ante': 'The family',
        'fam_tit': 'Three agents, one data contract',
        'n1': 'Vera', 'n2': 'Samuel', 'n3': 'Alba',
        'ag1': 'Project director',
        'ag1_para': 'For whoever answers for the whole portfolio',
        'ag1_desc': 'Forty projects. Broad sweep, committee cadence.',
        'ag2': 'Project manager',
        'ag2_para': 'For whoever answers for one project',
        'ag2_desc': 'One project. Depth, per-meeting cadence.',
        'ag3': 'Product manager',
        'ag3_para': 'For whoever defines what gets built',
        'ag3_desc': 'Before the project exists.',
        'comparten': 'What they share',
        'ficha_tit': 'The project record',
        'ficha_desc': 'Every field with the citation of the document it came from, and its '
                      'date. No agent goes back to the raw documents on its own.',
        'regla': "The manager's record is a declaration. Vera's finding is evidence. They never "
                 "merge, and the gap between them is the signal.",
        'propias': 'Its own',
        'q_ante': 'The first fifteen minutes',
        'q_tit': 'Setting it up is a conversation, and it ends with a result',
        'q': [('0–2 min', 'Install', 'Two commands, or four clicks.'),
              ('2–4 min', 'It looks before it asks', 'You point it at the folder. It lists what it found, which formats, and what it will not be able to read.'),
              ('4–8 min', 'Five questions', 'One at a time, each with a suggested answer. «I do not know» counts.'),
              ('8–15 min', 'A first result', 'It sweeps three projects, not the portfolio. What it knew, what is not stated, what contradicts itself.'),
              ('After', 'You decide the cadence', 'It runs on its own and speaks only when something crosses a threshold.')],
        'f_ante': 'How it works',
        'f_tit': 'The model extracts. The code computes.',
        'f': ['Your documents', 'Text', 'The record', 'Arithmetic', 'Signals'],
        'f_sub': ['However they are, wherever they are', 'docx · xlsx · pptx · pdf · eml', 'Every field with its citation', 'Deterministic and tested', 'Only what crossed a threshold'],
        'f_extrae': 'The model extracts',
        'f_calcula': 'The code computes',
        'f_nota': 'No number in a report comes from an estimate. And what is not stated anywhere is declared, not filled in.',
        'c_ante': 'The agent does not wait to be called',
        'c_tit': 'It wakes on its own, and almost always stays quiet',
        'c_pregunta': 'What is due today?',
        'c_ramas': [('Sweep', 'What changed in the folder', 'daily_sweep'),
                    ('Committee report', 'Lands early, so you can react to what it finds', 'committee_next · report_lead_days'),
                    ('Confirmation', 'Five fields, the ones that age worst', 'confirmation.every')],
        'c_silencio': 'Nothing crossed a threshold',
        'c_silencio_sub': 'It produces nothing. That is the feature: an agent that reports every week whether or not there is news is ignored within a month.',
        'i_ante': 'Installation',
        'i_tit': 'Four clicks, or two commands',
        'i_cowork': 'Claude Cowork',
        'i_code': 'Claude Code',
        'i_pasos_cowork': ['Customise', 'Explore plugins, Personal, then the + button',
                           'Add marketplace from GitHub', 'josenanez/criterio'],
        'i_pasos_code': ['/plugin marketplace add josenanez/criterio', '/plugin install criterio-portfolio@criterio'],
        'i_luego': 'And then, one thing:',
        's_ante': 'Rostrum · the server',
        's_tit': 'The report, for whoever does not open a folder',
        's_dentro': ['Your documents', 'Vera', 'The report'],
        's_dentro_sub': [
            'However they are. Only the agent reads them.',
            'Computes, and writes each project record.',
            'Pages already on disk. Two views, one per project.'],
        's_srv': 'Rostrum',
        's_srv_sub': 'Holds up what is already written. It computes nothing.',
        's_lee': 'reads only',
        's_lado_dentro': 'Where the agent works',
        's_lado_fuera': 'Where the people are',
        's_quien': ['The committee', 'Whoever will act'],
        's_que': ['What needs a decision.',
                  'Field by field, with every citation.'],
        's_vuelta': 'A request, read when the agent wakes',
        's_nota': 'It authenticates nobody, and that is deliberate: it is published behind the access control the organisation already has. The only thing it writes is the request, in a folder of its own.',
        # ── cómo operan los tres ──
        'fl_ante': 'HOW THE THREE OPERATE',
        'fl_tit': 'No arrow goes from one agent to another',
        'fl_cajas': [('THE DEFINITION', 'Alba', 'Before the project exists'), ('THE PROJECT', 'Samuel', 'One project, meeting cadence'), ('THE PORTFOLIO', 'Vera', 'Forty projects, committee cadence'), ('THE TEAM', 'Rostrum', 'Whoever will not open a folder')],
        'fl_peticion': 'the request: review · explain · correct',
        'fl_traza': 'is my product being built? · Alba processes the project record',
        'fl_gente': 'AND THE PEOPLE, WHO DO NOT LEAVE',
        'fl_personas': [('The product manager', 'Talks to the customer, decides what gets built and signs the charter.'), ('The project manager', 'Runs the meeting, negotiates, and declares the project status.'), ('The PMO manager', 'Decides what escalates and chases what the report asks for.')],
        'fl_nota': "Everything crosses through a document. Two agents talking directly are two agents you have to deploy together, and each one's input is produced by work its person cannot delegate.",

        'fl_cruza': [('the project charter', "and with it the project's record is born"),
                     ('ficha-pm.json', "published into the project's governance folder, where Vera processes it like any other document"),
                     ('the report', 'at an address, for whoever will not open a folder')],
        # ── el único contrato ──
        'ct_ante': 'THE SINGLE CONTRACT',
        'ct_tit': 'Nothing talks to anything directly',
        'ct_ficha': 'The project record',
        'ct_ficha_sub': 'Every value with the citation of the document it came from, and its date.',
        'ct_escriben': [('Alba', 'Creates it, with the project charter'), ('Samuel', "Writes the project's record, except the declared status"), ('Vera', 'Writes her portfolio analysis, and processes all of them')],
        'ct_lee': ('Rostrum', 'Publishes the report where the team will read it'),
        'ct_solo_lee': 'only publishes',
        'ct_orden': 'AND THE ORDER IN TIME',
        'ct_tiempo': [('Alba', "Defines. Her delivery closes with the charter, the record's birth certificate."), ('Samuel', 'Executes. One project, meeting cadence.'), ('Vera', 'Watches the whole, committee cadence.')],
        'ct_nota': "No agent writes the declared status: a person writes that. And the manager's record and the PMO's analysis never merge — the difference between them is the finding.",
    },
}

SKILLS_COMPARTIDOS = ['project-record', 'document-intake', 'baseline-variance',
                      'governance-artifacts', 'raid-taxonomy']
SKILLS_PMO = ['portfolio-health', 'project-diagnosis', 'portfolio-history', 'vendor-control']
SKILLS_PM = ['commitment-tracking']
SKILLS_PROD = ['requirement-record', 'demand-evidence', 'product-health']


# ══════════════════════════════════════════════ las figuras de la CFO y la CLO
# La misma forma que las de la PMO —la familia, cómo operan, el contrato—, con el texto de cada
# familia. Los agentes, sus roles y sus skills salen de familia.json y de las carpetas de cada
# plugin; aquí solo va lo que se dice en la figura.

def _familia_json(sg):
    with open(os.path.join(RAIZ, 'families', f'criterio-{sg}', 'familia.json'), encoding='utf-8') as fh:
        return json.load(fh)


def _skills(plugin):
    carpeta = os.path.join(RAIZ, 'plugins', plugin, 'skills')
    return sorted(x for x in os.listdir(carpeta) if os.path.isdir(os.path.join(carpeta, x)))


def compartidos_de(sg):
    """Los skills que tienen todos los agentes de la familia: copias literales."""
    conjuntos = [set(_skills(a['plugin'])) for a in _familia_json(sg)['agentes']]
    return sorted(set.intersection(*conjuntos))


def agentes_de(sg, t):
    comunes = set(compartidos_de(sg))
    salida = []
    for a in _familia_json(sg)['agentes']:
        idioma = t['_idioma']
        para, desc = t['fig_agentes'][a['id']]
        propios = [x for x in _skills(a['plugin']) if x not in comunes]
        salida.append((a['id'], a['nombre'], a['rol'][idioma], para, desc, t['disponible'], True, propios))
    return salida


FIG = {
    'cfo': {
        'es': {
            '_idioma': 'es',
            'fam_tit': 'Dos agentes, una ficha cada uno',
            'fig_agentes': {
                'clara': ('Para quien cierra el mes y responde por lo que dicen los libros',
                          'Un cierre por periodo. Todos los documentos del mes, no una muestra.'),
                'tomas': ('Para quien pone el presupuesto al lado de lo ejecutado',
                          'Un presupuesto por área y año, contra la contabilidad que cierra Clara.'),
            },
            'ficha_tit': 'Las fichas del cierre y del presupuesto',
            'ficha_desc': 'Cada dato con la cita del documento del que salió, y su fecha. Las tablas las '
                          'procesa el motor; la ficha lleva lo que solo dice un documento escrito.',
            'regla': 'El estado del cierre lo declara el contralor y el del presupuesto, el responsable '
                     'del área. Lo declarado y lo evidenciado nunca se fusionan: la diferencia es la señal.',
            'fl_ante': 'Cómo operan los dos',
            'fl_cajas': [('EL CIERRE', 'Clara', 'Una entidad y un periodo, cadencia mensual', 'clara'),
                         ('EL PRESUPUESTO', 'Tomás', 'Un área y un año, cadencia de comité', 'tomas'),
                         ('EL EQUIPO', 'Rostrum', 'Quien no va a abrir una carpeta', 'rostrum')],
            'fl_cruza': [('la contabilidad cerrada del periodo',
                          'en 10-contabilidad/: Tomás toma de ahí la ejecución, sin copiarla'),
                         ('el informe', 'en una dirección, para quien no va a abrir una carpeta')],
            'fl_lazos': ((2, 0, 'la pregunta escrita en Rostrum: Clara o Tomás la atienden en su siguiente corrida', 60),),
            'fl_personas': [('El contralor', 'Registra los asientos, firma y declara el estado del cierre.'),
                            ('El responsable del área', 'Aprueba los traslados y declara el estado de su presupuesto.'),
                            ('El comité', 'Decide con el material que prepara Tomás.')],
            'fl_nota': 'Todo cruza por un documento: la contabilidad cerrada, la ficha, el informe. Y el '
                       'insumo de cada agente lo produce el trabajo no delegable de su persona.',
            'ct_ante': 'El contrato',
            'ct_ficha': 'Las fichas',
            'ct_ficha_sub': 'La del cierre y la del presupuesto: cada dato con su cita y su fecha.',
            'ct_escriben': [('Clara', 'Escribe la ficha del cierre, salvo el estado declarado'),
                            ('Tomás', 'Escribe la ficha del presupuesto, salvo el estado declarado')],
            'ct_lee': ('Rostrum', 'Publica el informe donde el equipo lo vea'),
            'ct_solo_lee': 'solo publica',
            'ct_tiempo': [('Clara', 'Cierra el periodo con su checklist y su evidencia.'),
                          ('Tomás', 'Toma la ejecución de esa misma contabilidad.'),
                          ('El comité', 'Decide con el material de Tomás.')],
            'ct_nota': 'Ningún agente declara el estado: lo declara el contralor o el responsable del área. '
                       'Y lo declarado y lo evidenciado no se fusionan nunca — la diferencia es el hallazgo.',
        },
        'en': {
            '_idioma': 'en',
            'fam_tit': 'Two agents, one record each',
            'fig_agentes': {
                'clara': ('For whoever closes the month and answers for what the books say',
                          'One close per period. Every document of the month, not a sample.'),
                'tomas': ('For whoever sets the budget beside what was spent',
                          'One budget per area and year, against the books Clara closes.'),
            },
            'ficha_tit': 'The close and budget records',
            'ficha_desc': 'Every item cited to the document it came from, with its date. The engine '
                          'processes the tables; the record carries what only a written document says.',
            'regla': 'The controller declares the status of the close and the area owner that of the '
                     'budget. Declared and evidenced never merge: the difference is the signal.',
            'fl_ante': 'How the two operate',
            'fl_cajas': [('THE CLOSE', 'Clara', 'One entity and one period, monthly cadence', 'clara'),
                         ('THE BUDGET', 'Tomás', 'One area and one year, committee cadence', 'tomas'),
                         ('THE TEAM', 'Rostrum', 'Whoever will not open a folder', 'rostrum')],
            'fl_cruza': [("the period's closed books",
                          'in 10-contabilidad/: Tomás takes the execution from there, without copying it'),
                         ('the report', 'one way, for whoever will not open a folder')],
            'fl_lazos': ((2, 0, 'the question written in Rostrum: Clara or Tomás answer it on their next run', 60),),
            'fl_personas': [('The controller', 'Posts the entries, signs and declares the status of the close.'),
                            ('The area owner', 'Approves transfers and declares the status of their budget.'),
                            ('The committee', 'Decides on the material Tomás prepares.')],
            'fl_nota': "Everything crosses through a document: the closed books, the record, the report. And "
                       "each agent's input is produced by its person's non-delegable work.",
            'ct_ante': 'The contract',
            'ct_ficha': 'The records',
            'ct_ficha_sub': 'The close record and the budget record: every item with its citation and date.',
            'ct_escriben': [('Clara', 'Writes the close record, except the declared status'),
                            ('Tomás', 'Writes the budget record, except the declared status')],
            'ct_lee': ('Rostrum', 'Publishes the report where the team will see it'),
            'ct_solo_lee': 'only publishes',
            'ct_tiempo': [('Clara', 'Closes the period with its checklist and evidence.'),
                          ('Tomás', 'Takes the execution from those same books.'),
                          ('The committee', 'Decides on the material Tomás prepares.')],
            'ct_nota': 'No agent declares the status: the controller or the area owner does. And declared '
                       'and evidenced never merge — the difference is the finding.',
        },
    },
    'clo': {
        'es': {
            '_idioma': 'es',
            'fam_tit': 'Dos agentes, cada uno con sus fichas',
            'fig_agentes': {
                'fidel': ('Para quien responde por lo que la empresa firmó',
                          'Cada contrato vigente: lo que obliga, lo que vence y quién lo firmó.'),
                'constanza': ('Para quien responde por cada obligación y su evidencia',
                              'Cada obligación de cumplimiento contra su evidencia, a su plazo.'),
            },
            'ficha_tit': 'Las fichas del contrato y del periodo',
            'ficha_desc': 'Cada dato con la cita del documento y la cláusula de la que salió. Ninguno '
                          'interpreta una cláusula ni da una opinión jurídica.',
            'regla': 'Renovar, terminar o cómo se interpreta una norma lo decide siempre una persona. Lo '
                     'declarado y lo evidenciado nunca se fusionan: la diferencia es la señal.',
            'fl_ante': 'Cómo operan los dos',
            'fl_cajas': [('LOS CONTRATOS', 'Fidel', 'Cada contrato, con su calendario de vencimientos', 'fidel'),
                         ('EL CUMPLIMIENTO', 'Constanza', 'Una entidad y un periodo de cumplimiento', 'constanza'),
                         ('EL EQUIPO', 'Rostrum', 'Quien no va a abrir una carpeta', 'rostrum')],
            'fl_cruza': [('la ficha de cada contrato',
                          'en su carpeta de contratos/: Constanza toma de ahí las obligaciones de cumplimiento, sin copiarlas'),
                         ('el informe', 'en una dirección, para quien no va a abrir una carpeta')],
            'fl_lazos': ((2, 0, 'la pregunta escrita en Rostrum: Fidel o Constanza la atienden en su siguiente corrida', 60),),
            'fl_personas': [('Quien decide sobre el contrato', 'Decide renovar o terminar, y cómo se interpreta una cláusula.'),
                            ('El oficial de cumplimiento', 'Declara el estado del cumplimiento del periodo.'),
                            ('La organización', 'Define cada obligación en su matriz, con su fuente.')],
            'fl_nota': 'Todo cruza por un documento: la ficha del contrato, la del periodo, el informe. Y el '
                       'insumo de cada agente lo produce el trabajo no delegable de su persona.',
            'ct_ante': 'El contrato',
            'ct_ficha': 'Las fichas',
            'ct_ficha_sub': 'La de cada contrato y la del periodo: cada dato con su cita y su fecha.',
            'ct_escriben': [('Fidel', 'Escribe la ficha de cada contrato, salvo la decisión de renovar'),
                            ('Constanza', 'Escribe la ficha del periodo, salvo el estado declarado')],
            'ct_lee': ('Rostrum', 'Publica el informe donde el equipo lo vea'),
            'ct_solo_lee': 'solo publica',
            'ct_tiempo': [('Fidel', 'Registra cada contrato, sus fechas y sus obligaciones.'),
                          ('Constanza', 'Toma de esas fichas las obligaciones de cumplimiento.'),
                          ('El oficial de cumplimiento', 'Declara el estado del periodo.')],
            'ct_nota': 'Ningún agente declara ni decide: el estado lo declara el oficial de cumplimiento y '
                       'renovar lo decide una persona. Lo declarado y lo evidenciado no se fusionan nunca.',
        },
        'en': {
            '_idioma': 'en',
            'fam_tit': 'Two agents, each with its records',
            'fig_agentes': {
                'fidel': ('For whoever answers for what the company signed',
                          'Every contract in force: what it commits to, what expires and who signed it.'),
                'constanza': ('For whoever answers for each obligation and its evidence',
                              'Every compliance obligation against its evidence, by its deadline.'),
            },
            'ficha_tit': 'The contract and period records',
            'ficha_desc': 'Every item cited to the document and clause it came from. Neither interprets a '
                          'clause or gives a legal opinion.',
            'regla': 'Renewing, terminating or how a rule is read is always decided by a person. Declared '
                     'and evidenced never merge: the difference is the signal.',
            'fl_ante': 'How the two operate',
            'fl_cajas': [('THE CONTRACTS', 'Fidel', 'Every contract, with its expiry calendar', 'fidel'),
                         ('COMPLIANCE', 'Constanza', 'One entity and one compliance period', 'constanza'),
                         ('THE TEAM', 'Rostrum', 'Whoever will not open a folder', 'rostrum')],
            'fl_cruza': [("each contract's record",
                          'in its contratos/ folder: Constanza takes the compliance obligations from there, without copying them'),
                         ('the report', 'one way, for whoever will not open a folder')],
            'fl_lazos': ((2, 0, 'the question written in Rostrum: Fidel or Constanza answer it on their next run', 60),),
            'fl_personas': [('Whoever decides on the contract', 'Decides to renew or terminate, and how a clause is read.'),
                            ('The compliance officer', "Declares the period's compliance status."),
                            ('The organisation', 'Defines each obligation in its matrix, with its source.')],
            'fl_nota': "Everything crosses through a document: the contract record, the period record, the "
                       "report. And each agent's input is produced by its person's non-delegable work.",
            'ct_ante': 'The contract',
            'ct_ficha': 'The records',
            'ct_ficha_sub': "Each contract's and the period's: every item with its citation and date.",
            'ct_escriben': [('Fidel', "Writes each contract's record, except the decision to renew"),
                            ('Constanza', "Writes the period's record, except the declared status")],
            'ct_lee': ('Rostrum', 'Publishes the report where the team will see it'),
            'ct_solo_lee': 'only publishes',
            'ct_tiempo': [('Fidel', 'Records each contract, its dates and obligations.'),
                          ('Constanza', 'Takes the compliance obligations from those records.'),
                          ('The compliance officer', "Declares the period's status.")],
            'ct_nota': 'No agent declares or decides: the compliance officer declares the status and a person '
                       'decides to renew. Declared and evidenced never merge.',
        },
    },
}


# ══════════════════════════════════════════════════════════════════ emblemas

LE, ME = 720, 64


@functools.lru_cache(maxsize=None)
def simbolo_png(alto, color=ORO):
    """El símbolo de Criterio en PNG, del mismo trazo con que lo dibujan Rostrum y el portal."""
    png = cairosvg.svg2png(bytestring=trazos.simbolo(color, alto).encode('utf-8'), output_width=alto)
    return Image.open(io.BytesIO(png)).convert('RGBA')


def logotipo(img, d, x, y, alto, sigla=None, texto=CREMA):
    """El símbolo y «Criterio» en Inter Tight 600; con `sigla`, la de la familia en oro.
    `y` es el borde de arriba del símbolo; la palabra se apoya en la base del corchete."""
    pegar(img, simbolo_png(alto), x, y)
    fu = f(M6, int(alto * 0.9))
    base = y + alto * 53 / 64
    xt = x + alto * 1.2
    d.text((xt, base), 'Criterio', font=fu, fill=texto, anchor='ls')
    if sigla:
        d.text((xt + d.textlength('Criterio ', font=fu), base), sigla, font=fu, fill=ORO, anchor='ls')


def emblema(t, sigla, fn, fr, estado):
    """El emblema de una familia: el logotipo arriba, la sigla grande en oro, la función en
    palabras y la frase. La familia se reconoce por su sigla y su función, no por un color."""
    img = Image.new('RGB', (LE, LE), NEGRO)
    d = ImageDraw.Draw(img)
    d.rectangle([(ME // 2, ME // 2), (LE - ME // 2, LE - ME // 2)], outline=FILETE, width=2)
    X = ME + 18
    logotipo(img, d, X, 104, 72)
    track(d, (X, 236), sigla, f(M6, 132), ORO, 6)
    d.line([(X, 414), (LE - ME - 18, 414)], fill=FILETE_FUERTE, width=2)
    d.text((X, 434), fn, font=f(M5, 34), fill=CREMA)
    lineas = envolver(d, fr, f(R, 27), LE - 2 * ME - 36)
    assert len(lineas) <= 2, f'{sigla}: la frase no cabe en dos líneas'
    y = 496
    for linea in lineas:
        d.text((X, y), linea, font=f(R, 27), fill=APAGADO)
        y += 38
    insignia(d, (X, 600), estado, True)
    return img


# ══════════════════════════════════════════════════════════════════ la marca
#
# El símbolo y los logotipos en SVG, con la palabra convertida en trazo: se ven igual en un
# navegador que no tiene Inter Tight. «claro» es para fondo crema (oro #8a6327 y tinta) y
# «oscuro» para fondo negro (oro #d5a84b y crema), como dice docs/design.md.

FONDOS = {'claro': (TINTA_ORO, TINTA, '#6b675f'), 'oscuro': (ORO, CREMA, APAGADO)}


@functools.lru_cache(maxsize=None)
def _fuente(ruta):
    tt = TTFont(ruta)
    return tt, tt.getGlyphSet(), tt.getBestCmap(), tt['head'].unitsPerEm


def trazo_texto(texto, ruta, px, x, base, espacio=-0.01):
    """`texto` como el `d` de un `<path>`, apoyado en `base`. Devuelve el camino y dónde termina."""
    tt, glifos, cmap, upm = _fuente(ruta)
    esc, partes = px / upm, []
    for ch in texto:
        nombre = cmap[ord(ch)]
        pluma = SVGPathPen(glifos)
        glifos[nombre].draw(TransformPen(pluma, (esc, 0, 0, -esc, x, base)))
        partes.append(pluma.getCommands())
        x += tt['hmtx'][nombre][0] * esc + espacio * px
    return ' '.join(p for p in partes if p), x


def logotipo_svg(fondo, sigla=None, funcion=None):
    """El logotipo en una caja de 64 de alto: el símbolo, «Criterio» y, en una familia, su sigla
    en oro y la función en palabras debajo."""
    oro, tinta, apagado = FONDOS[fondo]
    s_ = trazos.SIMBOLO
    cx, cy, r = s_['punto']
    piezas = [f'<path d="{s_["corchete"]}" fill="none" stroke="{oro}" stroke-width="{s_["grosor"]}" '
              f'stroke-linecap="round" stroke-linejoin="round"/>', f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{oro}"/>']
    d_, fin = trazo_texto('Criterio', M6, 58, 78, 53)
    piezas.append(f'<path d="{d_}" fill="{tinta}"/>')
    if sigla:
        d_, fin = trazo_texto(sigla, M6, 58, fin + 15, 53)
        piezas.append(f'<path d="{d_}" fill="{oro}"/>')
    alto = 64
    if funcion:
        d_, fin2 = trazo_texto(funcion, R, 24, 78, 96, 0)
        piezas.append(f'<path d="{d_}" fill="{apagado}"/>')
        fin, alto = max(fin, fin2), 108
    ancho = round(fin + 4)
    nombre = 'Criterio' + (f' {sigla}' if sigla else '') + (f' · {funcion}' if funcion else '')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" '
            f'role="img" aria-label="{nombre}"><title>{nombre}</title>' + ''.join(piezas) + '</svg>\n')


def marca():
    carpeta = os.path.join(AQUI, 'marca')
    os.makedirs(carpeta, exist_ok=True)

    def escribe(rel, texto):
        ruta = os.path.join(carpeta, rel)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as fh:
            fh.write(texto)
        print(f'  marca/{rel}')
    for fondo, (oro, _, _) in FONDOS.items():
        escribe(f'simbolo-{fondo}.svg', trazos.simbolo(oro, 64) + '\n')
        escribe(f'logotipo-{fondo}.svg', logotipo_svg(fondo))
        for idioma in ('es', 'en'):
            for sg, fa in FAMILIA.items():
                escribe(f'{idioma}/criterio-{sg}-{fondo}.svg', logotipo_svg(fondo, sg.upper(), fa['nombre'][idioma]))


# ══════════════════════════════════════════════════════════════════ tarjetas sociales

OG_ROBOTS = {'pmo': trazos.ORDEN[:3], 'cfo': trazos.ORDEN_CFO, 'clo': trazos.ORDEN_CLO,
             'rostrum': ('rostrum', trazos.ORDEN[0], trazos.ORDEN_CFO[0], trazos.ORDEN_CLO[0])}


def tarjeta_social(t, clave, idioma):
    """La imagen que acompaña el enlace de cada página de Criterio en las redes: el logotipo de la
    familia, la promesa, el título de la página y sus robots, el primero encendido."""
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (W, 6)], fill=ORO)
    X = 84
    logotipo(img, d, X, 74, 46, None if clave == 'rostrum' else clave.upper())
    track(d, (X, 156), trazos.PROMESA[idioma].upper(), f(M6, 18), ORO, 2.2)
    titulo_, linea = t['og'][clave]
    fu = f(M5, 50)
    lineas = envolver(d, titulo_, fu, 600)
    assert len(lineas) <= 3, f'og {clave}: el título no cabe en tres líneas'
    y = 196
    for ln in lineas:
        d.text((X, y), ln, font=fu, fill=CREMA)
        y += 60
    d.line([(X, y + 18), (X + 96, y + 18)], fill=ORO, width=3)
    fr = f(R, 23)
    lr = envolver(d, linea, fr, 600)
    assert len(lr) <= 3, f'og {clave}: la línea no cabe en tres líneas'
    y += 44
    for ln in lr:
        d.text((X, y), ln, font=fr, fill=APAGADO)
        y += 33
    assert y < 520, f'og {clave}: el texto pisa el pie'
    bots = OG_ROBOTS[clave]
    ancho = 78 if len(bots) > 3 else 120  # el texto llega hasta x = 684: los robots empiezan después
    paso = ancho + 14
    x0 = W - 84 - paso * len(bots) + 14
    assert x0 >= X + 600 + 24, f'og {clave}: los robots pisan el texto'
    for k, b in enumerate(bots):
        trazo = ORO if k == 0 else mezcla(CREMA, NEGRO, 0.38)
        pegar(img, robot(b, ancho, trazo, trazo), x0 + k * paso, 210)
    d.line([(X, 534), (W - 84, 534)], fill=FILETE, width=1)
    d.text((X, 562), 'josenanez.com', font=f(R, 22), fill=APAGADO)
    fn = f(M5, 22)
    d.text((W - 84 - d.textlength('José Ñáñez', font=fn), 562), 'José Ñáñez', font=fn, fill=ORO)
    return img


# ══════════════════════════════════════════════════════════════════ los robots

@functools.lru_cache(maxsize=None)
def robot(nombre, ancho, trazo=ORO, ojo=ORO, t=None):
    """El robot en PNG. El trazo engrosa al achicarse: por debajo de cien píxeles, 2.5 se
    vuelve un hilo. Con `t`, es el robot en ese segundo de su gesto: un cuadro del GIF."""
    grosor = max(2.5, 2.5 * 100 / ancho)
    svg = trazos.svg(nombre, trazo, ojo, ancho=120, grosor=round(grosor, 2), t=t)
    png = cairosvg.svg2png(bytestring=svg.encode('utf-8'), output_width=ancho)
    return Image.open(io.BytesIO(png)).convert('RGBA')


def pegar(img, r, x, y):
    img.paste(r, (int(x), int(y)), r)
    return int(y) + r.height


def tarjeta(t, nombre):
    """La cabecera del README de cada agente, animada: el robot hace su gesto (los gestos
    viven en robots.py) sobre la tarjeta quieta. Una vuelta completa, en bucle."""
    nom, rol, frase, _ = t['rb'][nombre]
    fondo = Image.new('RGB', (720, 720), NEGRO)
    d = ImageDraw.Draw(fondo)
    d.rectangle([32, 32, 687, 687], outline=FILETE, width=2)
    # El logotipo de su familia, arriba a la derecha; Rostrum es de todas: lleva solo «Criterio».
    sg = FAMILIA_DE.get(trazos.AGENTE.get(nombre))
    fu = f(M6, 32)
    ancho_logo = 36 * 1.2 + d.textlength('Criterio' + (f' {sg.upper()}' if sg else ''), font=fu)
    logotipo(fondo, d, 638 - ancho_logo, 82, 36, sg.upper() if sg else None)
    d.text((82, 380), nom, font=f(M6, 96), fill=ORO)
    d.line([82, 512, 638, 512], fill=FILETE_FUERTE, width=2)
    d.text((82, 534), rol, font=f(M5, 32), fill=CREMA)
    parrafo(d, (82, 584), frase, f(R, 25), APAGADO, 556, 34)
    cuadros = []
    for k in range(CUADROS):
        img = fondo.copy()
        pegar(img, robot(nombre, 200, t=round(k * trazos.VUELTA / CUADROS, 4)), 82, 70)
        cuadros.append(img)
    return cuadros


CUADROS = 48   # 100 ms cada uno: la vuelta de 4,8 s


def guardar_gif(cuadros, idioma, nombre):
    """Un GIF con una sola paleta para todos los cuadros: así cada cuadro guarda solo lo que
    cambió, el robot, y la tarjeta pesa poco."""
    carpeta = os.path.join(AQUI, idioma)
    os.makedirs(carpeta, exist_ok=True)
    muestra = Image.new('RGB', (720, 720 * 2))
    muestra.paste(cuadros[0], (0, 0))
    muestra.paste(cuadros[len(cuadros) // 2], (0, 720))
    paleta = muestra.quantize(colors=64, dither=Image.Dither.NONE)
    p = [c.quantize(palette=paleta, dither=Image.Dither.NONE) for c in cuadros]
    p[0].save(os.path.join(carpeta, nombre), save_all=True, append_images=p[1:],
              duration=int(trazos.VUELTA * 1000 / len(cuadros)), loop=0, optimize=False, disposal=1)
    print(f'  {idioma}/{nombre}')


# ══════════════════════════════════════════════════════════════════ la familia

def etiquetas(d, x, y, items, ancho, fill=APAGADO, borde=FILETE_FUERTE):
    """Los skills como etiquetas, envueltas dentro de un ancho."""
    fu = f(R, 21)
    cx, cy = x, y
    for it in items:
        an = d.textlength(it, font=fu) + 26
        if cx + an > x + ancho:
            cx, cy = x, cy + 42
        d.rounded_rectangle([(cx, cy), (cx + an, cy + 33)], radius=5, outline=borde, width=1)
        d.text((cx + 13, cy + 5), it, font=fu, fill=fill)
        cx += an + 10
    return cy + 33


def familia(t, agentes=None, compartidos=None):
    W, H = 1680, 1260
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    M = 72

    titulo(d, (M, 66), t['fam_ante'], t['fam_tit'], W - 2 * M, 50)

    if agentes is None:
        agentes = [
        # Los tres disponibles. La insignia dice qué se puede instalar hoy, no qué tan
        # probado está: eso lo dice el estado de cada plugin y la página de pruebas, con
        # la distinción que importa — construido y verificado sobre corpus, no probado
        # sobre documentación real.
        (trazos.ORDEN[0], t['n1'], t['ag1'], t['ag1_para'], t['ag1_desc'], t['disponible'], True, SKILLS_PMO),
        (trazos.ORDEN[1], t['n2'], t['ag2'], t['ag2_para'], t['ag2_desc'], t['disponible'], True, SKILLS_PM),
        (trazos.ORDEN[2], t['n3'], t['ag3'], t['ag3_para'], t['ag3_desc'], t['disponible'], True, SKILLS_PROD),
        ]
    compartidos = SKILLS_COMPARTIDOS if compartidos is None else compartidos
    # una columna por agente
    n = len(agentes)
    col = (W - 2 * M - (n - 1) * 36) // n
    TOP, ALTO = 238, 520
    ROBOT = 96                 # de ancho; de alto, 136
    for i, (rid, nombre, rol, para, desc, estado, activo, propios) in enumerate(agentes):
        x = M + i * (col + 36)
        d.rounded_rectangle([(x, TOP), (x + col, TOP + ALTO)], radius=10,
                            fill=PANEL, outline=ORO if activo else FILETE, width=2)
        px = x + 28
        # la insignia va arriba a la derecha, y el robot debajo de ella: el texto de la
        # izquierda se envuelve en el ancho que el robot le deja
        insignia(d, (px, TOP + 26), estado, activo, derecha=x + col - 28)
        bajo_robot = pegar(img, robot(rid, ROBOT), x + col - 28 - ROBOT, TOP + 84)
        d.text((px, TOP + 78), nombre, font=f(M6, 44), fill=ORO if activo else CREMA)
        d.text((px, TOP + 136), rol, font=f(R, 22), fill=APAGADO)
        y = parrafo(d, (px, TOP + 180), para, f(R, 23), APAGADO, col - 56 - ROBOT - 24, 32)
        y = max(y + 14, bajo_robot + 10)
        fin = parrafo(d, (px, y), desc, f(R, 25), CREMA, col - 56, 34)
        assert fin < TOP + 370, f'{nombre}: la descripción pisa las etiquetas'
        if propios:
            d.text((px, TOP + 380), t['propias'], font=f(M6, 19), fill=FILETE_FUERTE)
            fin = etiquetas(d, px, TOP + 408, propios, col - 56)
            assert fin < TOP + ALTO - 20, f'{nombre}: las etiquetas se salen de la tarjeta'

    # la banda de lo compartido
    BY = TOP + ALTO + 54
    d.rounded_rectangle([(M, BY), (W - M, BY + 128)], radius=10, outline=FILETE, width=2)
    d.text((M + 28, BY + 24), t['comparten'], font=f(M6, 22), fill=ORO)
    etiquetas(d, M + 28, BY + 62, compartidos, W - 2 * M - 56)

    # la ficha, que es el contrato
    FY = BY + 128 + 54
    d.rounded_rectangle([(M, FY), (W - M, FY + 148)], radius=10, fill=PANEL,
                        outline=ORO, width=2)
    d.text((M + 28, FY + 26), t['ficha_tit'], font=f(M6, 32), fill=ORO)
    parrafo(d, (M + 28, FY + 74), t['ficha_desc'], f(R, 24), CREMA, W - 2 * M - 56, 33)

    # la regla
    RY = FY + 148 + 40
    d.line([(M, RY), (M + 64, RY)], fill=ORO, width=3)
    parrafo(d, (M + 84, RY - 14), t['regla'], f(M5, 25), APAGADO, W - 2 * M - 104, 34)
    return img


# ══════════════════════════════════════════════ los quince minutos

def quince(t):
    W, H, M = 1680, 700, 72
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['q_ante'], t['q_tit'], W - 2 * M, 46)

    YL = 300                                   # la línea de tiempo
    col = (W - 2 * M) // len(t['q'])
    d.line([(M + 22, YL), (W - M - col + 22, YL)], fill=FILETE_FUERTE, width=2)
    for i, (cuando, que, como) in enumerate(t['q']):
        x = M + i * col
        activo = i < len(t['q']) - 1
        d.text((x, YL - 62), cuando, font=f(M6, 24), fill=ORO if activo else APAGADO)
        d.ellipse([(x + 14, YL - 8), (x + 30, YL + 8)],
                  fill=ORO if activo else NEGRO, outline=ORO if activo else FILETE_FUERTE,
                  width=2)
        y = parrafo(d, (x, YL + 40), que, f(M5, 29), CREMA, col - 34, 36)
        fin = parrafo(d, (x, y + 12), como, f(R, 21), APAGADO, col - 34, 30)
        assert fin < H - 40, f'{que}: el texto se sale'
    return img


# ══════════════════════════════════════════════ cómo funciona

def funciona(t):
    W, H, M = 1680, 760, 72
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['f_ante'], t['f_tit'], W - 2 * M, 46)

    n = len(t['f'])
    hueco = 26
    col = (W - 2 * M - hueco * (n - 1)) // n
    TOP, ALTO = 300, 190
    for i, (nombre, sub) in enumerate(zip(t['f'], t['f_sub'])):
        x = M + i * (col + hueco)
        ficha = nombre == t['f'][2]
        d.rounded_rectangle([(x, TOP), (x + col, TOP + ALTO)], radius=10,
                            fill=PANEL if ficha else None,
                            outline=ORO if ficha else FILETE_FUERTE, width=2)
        d.text((x + 22, TOP + 26), nombre, font=f(M5, 30), fill=ORO if ficha else CREMA)
        parrafo(d, (x + 22, TOP + 76), sub, f(R, 20), APAGADO, col - 44, 28)
        if i < n - 1:
            cx = x + col
            d.line([(cx + 6, TOP + ALTO // 2), (cx + hueco - 6, TOP + ALTO // 2)],
                   fill=FILETE_FUERTE, width=2)

    # las dos mitades: quién hace qué
    def tramo(x0, x1, texto, color):
        y = TOP + ALTO + 34
        d.line([(x0, y), (x1, y)], fill=color, width=2)
        d.line([(x0, y - 8), (x0, y + 8)], fill=color, width=2)
        d.line([(x1, y - 8), (x1, y + 8)], fill=color, width=2)
        fu = f(M6, 22)
        an = d.textlength(texto, font=fu)
        d.text(((x0 + x1) / 2 - an / 2, y + 18), texto, font=fu, fill=color)

    tramo(M, M + 3 * col + 2 * hueco, t['f_extrae'], APAGADO)
    tramo(M + 3 * (col + hueco), W - M, t['f_calcula'], ORO)

    d.line([(M, 660), (M + 64, 660)], fill=ORO, width=3)
    parrafo(d, (M + 84, 646), t['f_nota'], f(M5, 24), APAGADO, W - 2 * M - 104, 33)
    return img


# ══════════════════════════════════════════════ la cadencia

def cadencia(t):
    W, H, M = 1680, 820, 72
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['c_ante'], t['c_tit'], W - 2 * M, 46)

    # el nodo de la pregunta
    PY_, PALTO = 290, 108
    pan = 380
    d.rounded_rectangle([(M, PY_), (M + pan, PY_ + PALTO)], radius=10, fill=ORO_FONDO,
                        outline=ORO, width=2)
    fu = f(M5, 32)
    an = d.textlength(t['c_pregunta'], font=fu)
    d.text((M + pan / 2 - an / 2, PY_ + 34), t['c_pregunta'], font=fu, fill=ORO)

    # las tres ramas
    x0 = M + pan + 60
    ancho = W - M - x0
    alto, hueco = 104, 20
    for i, (nombre, desc, clave) in enumerate(t['c_ramas']):
        y = 238 + i * (alto + hueco)
        d.rounded_rectangle([(x0, y), (W - M, y + alto)], radius=10, outline=FILETE_FUERTE,
                            width=2)
        d.line([(M + pan + 14, PY_ + PALTO / 2), (x0 - 10, y + alto / 2)],
               fill=FILETE_FUERTE, width=2)
        d.text((x0 + 24, y + 18), nombre, font=f(M5, 27), fill=CREMA)
        d.text((x0 + 24, y + 56), desc, font=f(R, 21), fill=APAGADO)
        fu2 = f(R, 19)
        anc = d.textlength(clave, font=fu2)
        d.text((W - M - 24 - anc, y + 58), clave, font=fu2, fill=FILETE_FUERTE)

    # el cuarto resultado, que es el que sostiene todo
    SY = 596
    d.rounded_rectangle([(M, SY), (W - M, SY + 150)], radius=10, fill=PANEL, outline=ORO,
                        width=2)
    d.text((M + 28, SY + 26), t['c_silencio'], font=f(M6, 30), fill=ORO)
    parrafo(d, (M + 28, SY + 76), t['c_silencio_sub'], f(R, 23), CREMA, W - 2 * M - 56, 32)
    return img


# ══════════════════════════════════════════════ la instalación

def instalacion(t):
    W, H, M = 1680, 660, 72
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['i_ante'], t['i_tit'], W - 2 * M, 46)

    col = (W - 2 * M - 48) // 2
    TOP, ALTO = 250, 300
    for i, (cual, pasos, mono) in enumerate([
            (t['i_cowork'], t['i_pasos_cowork'], False),
            (t['i_code'], t['i_pasos_code'], True)]):
        x = M + i * (col + 48)
        d.rounded_rectangle([(x, TOP), (x + col, TOP + ALTO)], radius=10, fill=PANEL,
                            outline=FILETE_FUERTE, width=2)
        d.text((x + 28, TOP + 24), cual, font=f(M6, 28), fill=ORO)
        assert len(pasos) <= 4, f'{cual}: más pasos de los que promete el título'
        y = TOP + 82
        for j, paso in enumerate(pasos, start=1):
            d.ellipse([(x + 28, y), (x + 56, y + 28)], outline=FILETE_FUERTE, width=2)
            nf = f(M6, 17)
            nn = d.textlength(str(j), font=nf)
            d.text((x + 42 - nn / 2, y + 5), str(j), font=nf, fill=APAGADO)
            fu = f(R, 21 if mono else 23)
            y = parrafo(d, (x + 72, y + 1), paso, fu, CREMA, col - 110, 30) + 16

    d.line([(M, 596), (M + 64, 596)], fill=ORO, width=3)
    d.text((M + 84, 580), t['i_luego'], font=f(M5, 26), fill=APAGADO)
    d.text((M + 84 + d.textlength(t['i_luego'], font=f(M5, 26)) + 18, 578),
           '/portfolio-setup', font=f(M6, 30), fill=ORO)
    return img


# ══════════════════════════════════════════════════════════════════ salida

# ══════════════════════════════════════════════ el servidor

def servidor(t):
    """Dónde está la frontera.

    La pieza tiene un solo trabajo: que se vea que el servidor está del lado de
    afuera, que lo único que cruza hacia adentro es una pregunta escrita, y que
    nada vuelve a calcularse cuando alguien abre la página.

    Las cajas no se dimensionan a ojo. `parrafo` devuelve dónde terminó el texto
    y aquí se comprueba contra el borde: así un texto más largo en inglés falla al
    generar la pieza y no en la página ya publicada.
    """
    W, H, M = 1680, 800, 72
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['s_ante'], t['s_tit'], W - 2 * M, 46)

    # Ritmo vertical declarado.
    FILA, ALTO = 276, 190
    FRONT, FRONT_FIN = FILA - 42, FILA + ALTO + 96
    LADOS = FRONT_FIN + 20
    VUELTA = FILA + ALTO + 72
    PIE = 700

    col, hueco = 230, 20
    xs = [M + i * (col + hueco) for i in range(3)]
    frontera = xs[2] + col + 48
    x_srv = frontera + 48
    col_srv = 250
    x_aud = x_srv + col_srv + 36
    col_aud = W - M - x_aud

    def caja(x, ancho, top, alto, nombre, sub, acento=False):
        d.rounded_rectangle([(x, top), (x + ancho, top + alto)], radius=10,
                            fill=PANEL if acento else None,
                            outline=ORO if acento else FILETE_FUERTE, width=2)
        d.text((x + 20, top + 22), nombre, font=f(M5, 27), fill=ORO if acento else CREMA)
        fin = parrafo(d, (x + 20, top + 68), sub, f(R, 20), APAGADO, ancho - 40, 28)
        assert fin <= top + alto - 12, f'«{nombre}» se sale de su caja por {fin - top - alto}px'

    for i, (nombre, sub) in enumerate(zip(t['s_dentro'], t['s_dentro_sub'])):
        caja(xs[i], col, FILA, ALTO, nombre, sub)
        if i < 2:
            cx = xs[i] + col
            d.line([(cx + 5, FILA + ALTO // 2), (cx + hueco - 5, FILA + ALTO // 2)],
                   fill=FILETE_FUERTE, width=2)

    caja(x_srv, col_srv, FILA, ALTO, t['s_srv'], t['s_srv_sub'], acento=True)

    # la frontera, y lo que significa cada lado
    for y in range(FRONT, FRONT_FIN, 16):
        d.line([(frontera, y), (frontera, min(y + 9, FRONT_FIN))], fill=ORO, width=2)
    fu = f(M6, 21)
    for texto, x0, x1, color in ((t['s_lado_dentro'], M, frontera - 14, APAGADO),
                                 (t['s_lado_fuera'], frontera + 14, W - M, ORO)):
        an = d.textlength(texto, font=fu)
        d.text(((x0 + x1) / 2 - an / 2, LADOS), texto, font=fu, fill=color)

    # lo único que el servidor hace hacia adentro: leer el informe ya escrito
    ymid = FILA + ALTO // 2
    d.line([(xs[2] + col + 4, ymid), (x_srv - 4, ymid)], fill=ORO, width=2)
    d.polygon([(xs[2] + col + 14, ymid - 7), (xs[2] + col + 14, ymid + 7),
               (xs[2] + col + 2, ymid)], fill=ORO)
    # El rótulo va encima de la flecha, no sobre ella: borrar un trozo de flecha
    # para escribir dentro se comió la flecha entera la primera vez.
    fu = f(R, 18)
    an = d.textlength(t['s_lee'], font=fu)
    hueco_srv = x_srv - (xs[2] + col)
    assert an <= hueco_srv - 8, f'«{t["s_lee"]}» no cabe en el hueco por {an - hueco_srv + 8:.0f}px'
    cx = (xs[2] + col + x_srv) / 2
    # El recorte llega hasta 14px por encima de la flecha: despeja la frontera
    # detrás del rótulo sin tocar la flecha, que va más abajo.
    d.rectangle([(cx - an / 2 - 6, ymid - 36), (cx + an / 2 + 6, ymid - 12)], fill=NEGRO)
    d.text((cx - an / 2, ymid - 32), t['s_lee'], font=fu, fill=ORO)

    # las dos audiencias, y su texto comprobado contra el borde
    ALTO_AUD = (ALTO - 20) // 2
    for i, (quien, que) in enumerate(zip(t['s_quien'], t['s_que'])):
        top = FILA + i * (ALTO_AUD + 20)
        d.rounded_rectangle([(x_aud, top), (x_aud + col_aud, top + ALTO_AUD)],
                            radius=10, outline=FILETE_FUERTE, width=2)
        track(d, (x_aud + 20, top + 16), quien.upper(), f(M6, 17), ORO, 2.6)
        fin = parrafo(d, (x_aud + 20, top + 44), que, f(R, 20), CREMA, col_aud - 40, 28)
        assert fin <= top + ALTO_AUD - 10, f'«{quien}» se sale de su caja por {fin - top - ALTO_AUD}px'
        d.line([(x_srv + col_srv + 6, top + ALTO_AUD // 2),
                (x_aud - 6, top + ALTO_AUD // 2)], fill=FILETE_FUERTE, width=2)

    # la petición: lo único que va hacia atrás, y no llega sola ni llega ahora
    x_sale, x_entra = x_srv + 36, xs[1] + 40
    d.line([(x_sale, FILA + ALTO + 6), (x_sale, VUELTA)], fill=APAGADO, width=2)
    d.line([(x_entra, VUELTA), (x_sale, VUELTA)], fill=APAGADO, width=2)
    d.line([(x_entra, FILA + ALTO + 16), (x_entra, VUELTA)], fill=APAGADO, width=2)
    d.polygon([(x_entra - 6, FILA + ALTO + 18), (x_entra + 6, FILA + ALTO + 18),
               (x_entra, FILA + ALTO + 5)], fill=APAGADO)
    # El rótulo se alinea a la izquierda a propósito: centrado pisa la frontera,
    # y borrar un trozo de la frontera para escribir encima deja un hueco que
    # parece un error de dibujo.
    fu = f(R, 20)
    an = d.textlength(t['s_vuelta'], font=fu)
    x0 = x_entra + 16
    assert x0 + an < frontera - 20, 'el rótulo de la petición pisa la frontera'
    d.rectangle([(x0 - 10, VUELTA - 14), (x0 + an + 10, VUELTA + 14)], fill=NEGRO)
    d.text((x0, VUELTA - 12), t['s_vuelta'], font=fu, fill=APAGADO)

    d.line([(M, PIE + 14), (M + 64, PIE + 14)], fill=ORO, width=3)
    parrafo(d, (M + 84, PIE), t['s_nota'], f(M5, 24), APAGADO, W - 2 * M - 104, 33)
    return img


# ══════════════════════════════════════════════ cómo operan los tres


def flujo(t):
    """El orden temporal de los tres agentes, y lo que cruza entre ellos.

    Lo que esta pieza tiene que dejar claro en tres segundos: **ninguna flecha va de un
    agente a otro.** Todas pasan por un documento, y ese es el diseño entero. Por eso lo
    que cruza va escrito al lado de la flecha, con su nombre real de archivo cuando lo
    tiene.

    Va en vertical y no en horizontal a propósito: «el acta de constitución» y
    «publicada en la carpeta del proyecto» no caben en el hueco entre dos tarjetas, y la
    primera versión de esta figura los escribió encima del nombre del agente siguiente.
    En vertical el texto tiene todo el ancho que necesite.
    """
    CAJA, SALTO = 128, 124
    TOP = 246
    cajas = t['fl_cajas']
    # el alto sale del número de cajas: con las cuatro de la PMO da los mismos 1560
    W, M = 1680, 72
    H = TOP + len(cajas) * (CAJA + SALTO) - SALTO + 74 + 196 + 160
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['fl_ante'], t['fl_tit'], W - 2 * M, 46)

    ANCHO = 940            # la tarjeta; a la derecha quedan los lazos de vuelta
    ys = []
    for i, caja in enumerate(cajas):
        etapa, nombre, quien = caja[:3]
        rid = caja[3] if len(caja) > 3 else nombre.lower()
        y = TOP + i * (CAJA + SALTO)
        ys.append(y)
        agente = i < len(cajas) - 1      # la última es Rostrum, que no es agente
        d.rounded_rectangle([(M, y), (M + ANCHO, y + CAJA)], radius=10,
                            fill=PANEL if agente else None,
                            outline=ORO if agente else FILETE_FUERTE, width=2)
        track(d, (M + 26, y + 22), etapa, f(M6, 18), APAGADO, 2.4)
        d.text((M + 26, y + 56), nombre, font=f(M5, 40), fill=ORO if agente else CREMA)
        # el agente encendido; Rostrum, que no es agente, en crema
        r = robot(rid, 70, ORO if agente else CREMA)
        pegar(img, r, M + ANCHO - 30 - r.width, y + (CAJA - r.height) // 2)
        fin = parrafo(d, (M + 300, y + 62), quien, f(R, 22), APAGADO, ANCHO - 330 - 100, 30)
        assert fin < y + CAJA - 8, f'{nombre}: el texto se sale de la tarjeta'

        # la flecha hacia la siguiente, con lo que cruza escrito al lado
        if i < len(cajas) - 1:
            cx = M + 110
            y0, y1 = y + CAJA + 12, y + CAJA + SALTO - 12
            d.line([(cx, y0), (cx, y1)], fill=ORO, width=2)
            p = 10
            d.polygon([(cx, y1), (cx - p + 2, y1 - p), (cx + p - 2, y1 - p)], fill=ORO)
            que, sub = t['fl_cruza'][i]
            d.text((cx + 28, y0 + 6), que, font=f(M5, 24), fill=ORO)
            fin = parrafo(d, (cx + 28, y0 + 40), sub, f(R, 20), APAGADO, ANCHO - 200, 27)
            assert fin < y1 + 6, f'{que}: el texto del cruce se sale del salto'

    # los dos lazos de vuelta, por la derecha. Cada uno sube de una caja a otra.
    def lazo(desde, hasta, texto, carril):
        x = M + ANCHO + carril
        y0 = ys[desde] + CAJA // 2
        y1 = ys[hasta] + CAJA // 2
        d.line([(M + ANCHO + 6, y0), (x, y0)], fill=FILETE_FUERTE, width=2)
        d.line([(x, y0), (x, y1)], fill=FILETE_FUERTE, width=2)
        d.line([(x, y1), (M + ANCHO + 6, y1)], fill=FILETE_FUERTE, width=2)
        p = 9
        d.polygon([(M + ANCHO + 6, y1), (M + ANCHO + 6 + p, y1 - p + 2),
                   (M + ANCHO + 6 + p, y1 + p - 2)], fill=FILETE_FUERTE)
        fin = parrafo(d, (x + 20, min(y0, y1) + abs(y1 - y0) // 2 - 28), texto,
                      f(R, 20), APAGADO, W - M - x - 28, 27)
        assert fin < H - 380, 'el texto del lazo se sale de la figura'

    for desde, hasta, texto, carril in t.get('fl_lazos', ((3, 2, t['fl_peticion'], 60), (2, 0, t['fl_traza'], 150))):
        lazo(desde, hasta, texto, carril)

    # la banda de las personas: cada agente se alimenta de trabajo no delegable
    BY = ys[-1] + CAJA + 74
    d.rounded_rectangle([(M, BY), (W - M, BY + 196)], radius=10, fill=PANEL,
                        outline=FILETE_FUERTE, width=2)
    track(d, (M + 28, BY + 24), t['fl_gente'], f(M6, 18), ORO, 2.4)
    paso = (W - 2 * M - 56) // len(t['fl_personas'])
    for i, (quien, hace) in enumerate(t['fl_personas']):
        x = M + 28 + i * paso
        fin = parrafo(d, (x, BY + 106), hace, f(R, 20), APAGADO, paso - 34, 27)
        d.text((x, BY + 64), quien, font=f(M5, 24), fill=CREMA)
        assert fin < BY + 196 - 8, f'{quien}: el texto se sale de la banda'

    d.line([(M, H - 92), (M + 64, H - 92)], fill=ORO, width=3)
    fin = parrafo(d, (M + 84, H - 106), t['fl_nota'], f(M5, 23), APAGADO,
                  W - 2 * M - 104, 31)
    assert fin < H - 12, 'la nota se sale de la figura'
    return img


# ══════════════════════════════════════════════ el único contrato


def contrato(t):
    """La ficha en el centro, y quién escribe y quién lee.

    `como-funciona` ya muestra la tubería —documento, texto, ficha, aritmética, señal—.
    Lo que esta pieza agrega es lo que aquella no dice: **quién puede escribir en la ficha
    y quién solo la lee.** Por eso la ficha va al centro y no en una fila: lo que importa
    aquí son las flechas, no el orden.
    """
    W, H, M = 1680, 1000, 72
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    titulo(d, (M, 66), t['ct_ante'], t['ct_tit'], W - 2 * M, 46)

    # la ficha, en el centro
    FW, FH = 420, 200
    fx = (W - FW) // 2
    fy = 300
    d.rounded_rectangle([(fx, fy), (fx + FW, fy + FH)], radius=12, fill=ORO_FONDO,
                        outline=ORO, width=3)
    fu = f(M5, 34)
    an = d.textlength(t['ct_ficha'], font=fu)
    d.text((fx + FW / 2 - an / 2, fy + 40), t['ct_ficha'], font=fu, fill=ORO)
    fin = parrafo(d, (fx + 28, fy + 96), t['ct_ficha_sub'], f(R, 21), CREMA, FW - 56, 29)
    assert fin < fy + FH - 10, 'la ficha: el texto se sale de la caja'

    # los tres que escriben, a la izquierda
    CW, CH, HUECO = 340, 116, 20
    ALTO = len(t['ct_escriben']) * CH + (len(t['ct_escriben']) - 1) * HUECO
    y0 = fy + FH // 2 - ALTO // 2
    for i, (quien, que) in enumerate(t['ct_escriben']):
        y = y0 + i * (CH + HUECO)
        d.rounded_rectangle([(M, y), (M + CW, y + CH)], radius=10, fill=PANEL,
                            outline=ORO, width=2)
        d.text((M + 24, y + 18), quien, font=f(M5, 28), fill=ORO)
        fin = parrafo(d, (M + 24, y + 56), que, f(R, 19), APAGADO, CW - 48, 25)
        assert fin < y + CH - 4, f'{quien}: el texto se sale de la caja'
        # la flecha hasta la ficha
        x0, x1 = M + CW + 10, fx - 12
        cy = y + CH // 2
        medio = (x0 + x1) / 2
        d.line([(x0, cy), (medio, cy)], fill=ORO, width=2)
        d.line([(medio, cy), (medio, fy + FH // 2)], fill=ORO, width=2)
        d.line([(medio, fy + FH // 2), (x1, fy + FH // 2)], fill=ORO, width=2)
        p = 9
        d.polygon([(x1, fy + FH // 2), (x1 - p, fy + FH // 2 - p + 2),
                   (x1 - p, fy + FH // 2 + p - 2)], fill=ORO)

    # el que solo lee, a la derecha
    rx = fx + FW + 150
    ry = fy + FH // 2 - CH // 2
    d.rounded_rectangle([(rx, ry), (rx + CW, ry + CH)], radius=10,
                        outline=FILETE_FUERTE, width=2)
    d.text((rx + 24, ry + 18), t['ct_lee'][0], font=f(M5, 28), fill=CREMA)
    parrafo(d, (rx + 24, ry + 56), t['ct_lee'][1], f(R, 19), APAGADO, CW - 48, 25)
    cy = fy + FH // 2
    d.line([(fx + FW + 12, cy), (rx - 12, cy)], fill=FILETE_FUERTE, width=2)
    p = 9
    d.polygon([(rx - 12, cy), (rx - 12 - p, cy - p + 2), (rx - 12 - p, cy + p - 2)],
              fill=FILETE_FUERTE)
    fu2 = f(R, 19)
    an2 = d.textlength(t['ct_solo_lee'], font=fu2)
    d.text(((fx + FW + rx) / 2 - an2 / 2, cy - 30), t['ct_solo_lee'], font=fu2,
           fill=FILETE_FUERTE)

    # el orden en el tiempo, abajo
    BY = fy + FH + 96
    d.rounded_rectangle([(M, BY), (W - M, BY + 190)], radius=10, fill=PANEL,
                        outline=FILETE_FUERTE, width=2)
    track(d, (M + 28, BY + 24), t['ct_orden'], f(M6, 18), ORO, 2.4)
    paso = (W - 2 * M - 56) // len(t['ct_tiempo'])
    for i, (quien, que) in enumerate(t['ct_tiempo']):
        x = M + 28 + i * paso
        d.text((x, BY + 62), quien, font=f(M5, 26), fill=CREMA)
        fin = parrafo(d, (x, BY + 100), que, f(R, 19), APAGADO, paso - 80, 25)
        assert fin < BY + 190 - 6, f'{quien}: el texto se sale de la banda'
        if i < len(t['ct_tiempo']) - 1:
            ax = x + paso - 52
            ay = BY + 74
            d.line([(ax, ay), (ax + 28, ay)], fill=ORO, width=2)
            p = 8
            d.polygon([(ax + 28, ay), (ax + 28 - p, ay - p + 2), (ax + 28 - p, ay + p - 2)],
                      fill=ORO)

    d.line([(M, H - 66), (M + 64, H - 66)], fill=ORO, width=3)
    fin = parrafo(d, (M + 84, H - 80), t['ct_nota'], f(M5, 23), APAGADO,
                  W - 2 * M - 104, 31)
    assert fin < H - 8, 'la nota se sale de la figura'
    return img


def guardar(img, idioma, nombre):
    carpeta = os.path.join(AQUI, idioma)
    os.makedirs(carpeta, exist_ok=True)
    img.save(os.path.join(carpeta, nombre), 'PNG')
    print(f'  {idioma}/{nombre}')


if __name__ == '__main__':
    marca()
    for idioma, t in T.items():
        print(idioma)
        # el estado de cada familia es el de su familia.json, por medio del registro
        for sg in ('pmo', 'cfo', 'clo'):
            guardar(emblema(t, sg.upper(), FAMILIA[sg]['nombre'][idioma], t[f'{sg}_fr'], FAMILIA[sg]['estado'][idioma]), idioma, f'{sg}.png')
        guardar(familia(t), idioma, 'familia.png')
        # las tres figuras de la PMO, con la misma forma, para la CFO y la CLO
        for sg in ('cfo', 'clo'):
            tf = {**t, **FIG[sg][idioma]}
            guardar(familia(tf, agentes_de(sg, tf), compartidos_de(sg)), idioma, f'familia-{sg}.png')
            guardar(flujo(tf), idioma, f'flujo-{sg}.png')
            guardar(contrato(tf), idioma, f'contrato-{sg}.png')
        for clave in ('pmo', 'cfo', 'clo', 'rostrum'):
            guardar(tarjeta_social(t, clave, idioma), idioma, f'og-{clave}.png')
        guardar(flujo(t), idioma, 'flujo.png')
        guardar(contrato(t), idioma, 'contrato.png')
        guardar(quince(t), idioma, 'quince-minutos.png')
        guardar(funciona(t), idioma, 'como-funciona.png')
        guardar(cadencia(t), idioma, 'cadencia.png')
        guardar(instalacion(t), idioma, 'instalacion.png')
        guardar(servidor(t), idioma, 'servidor.png')
        for nombre in trazos.ORDEN + trazos.ORDEN_CFO + trazos.ORDEN_CLO:
            guardar_gif(tarjeta(t, nombre), idioma, f'robot-{nombre}.gif')
    # El trazo de cada robot, solo y con su gesto, para que el portal lo dibuje sin copiarlo.
    # Es un SVG animado: se mueve igual en un README, en el portal y en Rostrum.
    os.makedirs(os.path.join(AQUI, 'robots'), exist_ok=True)
    for nombre in trazos.ORDEN + trazos.ORDEN_CFO + trazos.ORDEN_CLO:
        with open(os.path.join(AQUI, 'robots', f'{nombre}.svg'), 'w', encoding='utf-8') as fh:
            fh.write(trazos.svg(nombre, ORO, ORO, animado=True) + '\n')
    # Y como datos, para quien dibuja el robot con su propio marcado: la impresora del portal.
    with open(os.path.join(AQUI, 'robots', 'robots.json'), 'w', encoding='utf-8') as fh:
        json.dump(trazos.datos(), fh, ensure_ascii=False, indent=1)
        fh.write('\n')
