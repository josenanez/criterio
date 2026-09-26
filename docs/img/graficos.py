# -*- coding: utf-8 -*-
"""Las piezas gráficas de Criterio, en los dos idiomas.

    INTER_TIGHT=/ruta python3 docs/img/graficos.py

Un solo generador para todas, porque comparten vocabulario: fondo negro, un acento
de oro, filetes finos, Inter Tight, y el texto cargando el mensaje. Colores y reglas
en docs/design.md.

Sale a docs/img/es/ y docs/img/en/. Los PNG se versionan para que no haya que correr
nada. Las fuentes no: una fuente redistribuida sin su licencia al lado es un cabo
suelto en un repositorio Apache 2.0. Se bajan de Google Fonts —Inter Tight 400, 500
y 600— y se apuntan con INTER_TIGHT.

Cada figura declara su ritmo vertical en vez de estimarlo. Estimar posiciones es como
se llega a que una frase pise una insignia.
"""
import os
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
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
        # ── emblemas ──
        'pmo_fn': 'Oficina de proyectos',
        'pmo_fr': 'Leo la documentación que tu PMO ya tiene, y digo qué no se sostiene.',
        'cfo_fn': 'Cierre, control y reporte',
        'cfo_fr': 'Cierro contra lo que dicen los documentos, no contra lo que se declara.',
        'clo_fn': 'Contratos y cumplimiento',
        'clo_fr': 'Sé qué firmaste, qué vence, y a qué te obligaste.',
        'disponible': 'Disponible',
        'declarada': 'Capacidad declarada',
        'construccion': 'En construcción',
        'sin_construir': 'Sin construir',
        # ── familia ──
        'fam_ante': 'La familia PMO',
        'fam_tit': 'Tres agentes, un solo contrato de datos',
        'n1': 'Vera', 'n2': 'Samuel', 'n3': 'Alba',
        'ag1': 'Agente PMO',
        'ag1_para': 'Para el gerente de la PMO y sus analistas',
        'ag1_desc': 'Cuarenta proyectos. Barrido amplio, cadencia de comité.',
        'ag2': 'Agente PM',
        'ag2_para': 'Para cada gerente de proyecto',
        'ag2_desc': 'Un proyecto. Profundidad, cadencia por reunión.',
        'ag3': 'Agente de producto',
        'ag3_para': 'Para quien define qué se construye',
        'ag3_desc': 'Antes de que exista el proyecto.',
        'comparten': 'Lo que comparten',
        'ficha_tit': 'La ficha de proyecto',
        'ficha_desc': 'Cada dato con la cita del documento del que salió, y su fecha. '
                      'Ningún agente lee documentos crudos por su cuenta.',
        'regla': 'La ficha del PM es una declaración. El hallazgo del PMO es evidencia. '
                 'Nunca se fusionan, y la diferencia entre las dos es la señal.',
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
                           'Agregar marketplace desde GitHub', 'josenanez-company/criterio'],
        'i_pasos_code': ['/plugin marketplace add josenanez-company/criterio', '/plugin install criterio-pmo@criterio'],
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
    },
    'en': {
        'pmo_fn': 'Project management office',
        'pmo_fr': 'I read the documentation your PMO already has, and say what does not hold.',
        'cfo_fn': 'Close, control and reporting',
        'cfo_fr': 'I close against what the documents say, not against what is declared.',
        'clo_fn': 'Contracts and compliance',
        'clo_fr': 'I know what you signed, what expires, and what you committed to.',
        'disponible': 'Available',
        'declarada': 'Declared capability',
        'construccion': 'Being built',
        'sin_construir': 'Not built',
        'fam_ante': 'The PMO family',
        'fam_tit': 'Three agents, one data contract',
        'n1': 'Vera', 'n2': 'Samuel', 'n3': 'Alba',
        'ag1': 'PMO agent',
        'ag1_para': 'For the PMO manager and their analysts',
        'ag1_desc': 'Forty projects. Broad sweep, committee cadence.',
        'ag2': 'PM agent',
        'ag2_para': 'For each project manager',
        'ag2_desc': 'One project. Depth, per-meeting cadence.',
        'ag3': 'Product agent',
        'ag3_para': 'For whoever defines what gets built',
        'ag3_desc': 'Before the project exists.',
        'comparten': 'What they share',
        'ficha_tit': 'The project record',
        'ficha_desc': 'Every field with the citation of the document it came from, and its '
                      'date. No agent reads raw documents on its own.',
        'regla': "The PM's record is a declaration. The PMO's finding is evidence. They never "
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
                           'Add marketplace from GitHub', 'josenanez-company/criterio'],
        'i_pasos_code': ['/plugin marketplace add josenanez-company/criterio', '/plugin install criterio-pmo@criterio'],
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
    },
}

SKILLS_COMPARTIDOS = ['project-record', 'document-intake', 'baseline-variance',
                      'governance-artifacts', 'raid-taxonomy']
SKILLS_PMO = ['portfolio-health', 'project-diagnosis', 'portfolio-history', 'vendor-control']
SKILLS_PM = ['commitment-tracking']
SKILLS_PROD = ['requirement-record', 'demand-evidence', 'product-health']


# ══════════════════════════════════════════════════════════════════ emblemas

LE, ME = 720, 64


def glifo_pmo(d, x, y):
    lado, hueco, marcado = 26, 12, (1, 2)
    for fila in range(3):
        for col in range(4):
            cx, cy = x + col * (lado + hueco), y + fila * (lado + hueco)
            mio = (fila, col) == marcado
            d.rectangle([(cx, cy), (cx + lado, cy + lado)], fill=ORO if mio else None,
                        outline=ORO if mio else FILETE_FUERTE, width=2)


def glifo_cfo(d, x, y):
    largo, alto, hueco = 152, 9, 19
    for i in range(5):
        an = largo if i < 4 else int(largo * 0.55)
        cy = y + i * (alto + hueco)
        d.rectangle([(x, cy), (x + an, cy + alto)], fill=ORO if i == 4 else FILETE_FUERTE)


def glifo_clo(d, x, y):
    an, al, esq = 120, 150, 34
    d.polygon([(x, y), (x + an - esq, y), (x + an, y + esq), (x + an, y + al), (x, y + al)],
              outline=FILETE_FUERTE, width=2)
    d.line([(x + an - esq, y), (x + an - esq, y + esq), (x + an, y + esq)],
           fill=FILETE_FUERTE, width=2)
    d.ellipse([(x + an - 46, y + al - 46), (x + an + 10, y + al + 10)], outline=ORO, width=3)


def emblema(t, sigla, fn, fr, estado, glifo):
    img = Image.new('RGB', (LE, LE), NEGRO)
    d = ImageDraw.Draw(img)
    d.rectangle([(ME // 2, ME // 2), (LE - ME // 2, LE - ME // 2)], outline=FILETE, width=2)
    X = ME + 18
    glifo(d, X, 108)
    track(d, (X, 258), sigla, f(M6, 104), ORO, 6)
    d.line([(X, 414), (LE - ME - 18, 414)], fill=FILETE_FUERTE, width=2)
    d.text((X, 434), fn, font=f(M5, 34), fill=CREMA)
    lineas = envolver(d, fr, f(R, 27), LE - 2 * ME - 36)
    assert len(lineas) <= 2, f'{sigla}: la frase no cabe en dos líneas'
    y = 496
    for linea in lineas:
        d.text((X, y), linea, font=f(R, 27), fill=APAGADO)
        y += 38
    insignia(d, (X, 600), estado, estado in (t['disponible'], T['en']['disponible']))
    return img


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


def familia(t):
    W, H = 1680, 1200
    img = Image.new('RGB', (W, H), NEGRO)
    d = ImageDraw.Draw(img)
    M = 72

    titulo(d, (M, 66), t['fam_ante'], t['fam_tit'], W - 2 * M, 50)

    # tres columnas
    col = (W - 2 * M - 2 * 36) // 3
    agentes = [
        # Los tres disponibles. La insignia dice qué se puede instalar hoy, no qué tan
        # probado está: eso lo dice el estado de cada plugin y la página de pruebas, con
        # la distinción que importa — construido y verificado sobre corpus, no probado
        # sobre documentación real.
        (t['n1'], t['ag1'], t['ag1_para'], t['ag1_desc'], t['disponible'], True, SKILLS_PMO),
        (t['n2'], t['ag2'], t['ag2_para'], t['ag2_desc'], t['disponible'], True, SKILLS_PM),
        (t['n3'], t['ag3'], t['ag3_para'], t['ag3_desc'], t['disponible'], True, SKILLS_PROD),
    ]
    TOP, ALTO = 238, 460
    for i, (nombre, rol, para, desc, estado, activo, propios) in enumerate(agentes):
        x = M + i * (col + 36)
        d.rounded_rectangle([(x, TOP), (x + col, TOP + ALTO)], radius=10,
                            fill=PANEL, outline=ORO if activo else FILETE, width=2)
        px = x + 28
        # la insignia va arriba a la derecha: ahí no puede chocar con nada que fluya
        insignia(d, (px, TOP + 26), estado, activo, derecha=x + col - 28)
        d.text((px, TOP + 78), nombre, font=f(M6, 44), fill=ORO if activo else CREMA)
        d.text((px, TOP + 136), rol, font=f(R, 22), fill=APAGADO)
        parrafo(d, (px, TOP + 180), para, f(R, 23), APAGADO, col - 56, 32)
        parrafo(d, (px, TOP + 240), desc, f(R, 25), CREMA, col - 56, 34)
        if propios:
            d.text((px, TOP + 318), t['propias'], font=f(M6, 19), fill=FILETE_FUERTE)
            fin = etiquetas(d, px, TOP + 346, propios, col - 56)
            assert fin < TOP + ALTO - 20, f'{nombre}: las etiquetas se salen de la tarjeta'

    # la banda de lo compartido
    BY = TOP + ALTO + 54
    d.rounded_rectangle([(M, BY), (W - M, BY + 128)], radius=10, outline=FILETE, width=2)
    d.text((M + 28, BY + 24), t['comparten'], font=f(M6, 22), fill=ORO)
    etiquetas(d, M + 28, BY + 62, SKILLS_COMPARTIDOS, W - 2 * M - 56)

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
           '/pmo-setup', font=f(M6, 30), fill=ORO)
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


def guardar(img, idioma, nombre):
    carpeta = os.path.join(AQUI, idioma)
    os.makedirs(carpeta, exist_ok=True)
    img.save(os.path.join(carpeta, nombre), 'PNG')
    print(f'  {idioma}/{nombre}')


if __name__ == '__main__':
    for idioma, t in T.items():
        print(idioma)
        guardar(emblema(t, 'PMO', t['pmo_fn'], t['pmo_fr'], t['disponible'], glifo_pmo),
                idioma, 'pmo.png')
        guardar(emblema(t, 'CFO', t['cfo_fn'], t['cfo_fr'], t['declarada'], glifo_cfo),
                idioma, 'cfo.png')
        guardar(emblema(t, 'CLO', t['clo_fn'], t['clo_fr'], t['declarada'], glifo_clo),
                idioma, 'clo.png')
        guardar(familia(t), idioma, 'familia-pmo.png')
        guardar(quince(t), idioma, 'quince-minutos.png')
        guardar(funciona(t), idioma, 'como-funciona.png')
        guardar(cadencia(t), idioma, 'cadencia.png')
        guardar(instalacion(t), idioma, 'instalacion.png')
        guardar(servidor(t), idioma, 'servidor.png')
