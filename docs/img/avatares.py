# -*- coding: utf-8 -*-
"""Los tres emblemas de las familias de agentes, para la página central.

    python3 docs/img/avatares.py

Uno por familia. Cada uno dice, en una línea, para qué está — y declara si está
disponible o si es una capacidad declarada y sin construir. Esa distinción no es
decorativa: prometer una capacidad que no existe es lo que quema la credibilidad de
las que sí.

Colores y tipografía: docs/design.md. Todo lo de aquí es modo oscuro.

Los PNG están versionados, así que para ver los emblemas no hay que correr nada. Para
regenerarlos hace falta Inter Tight, que NO se versiona aquí: una fuente redistribuida
sin su licencia al lado es un cabo suelto en un repositorio Apache 2.0. Se descarga de
Google Fonts —Inter Tight, pesos 400, 500 y 600— y se apunta con:

    INTER_TIGHT=/ruta/a/las/fuentes python3 docs/img/avatares.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

L = 720                      # cuadrado, para que tres quepan en una fila
M = 64

NEGRO = '#050505'
CREMA = '#f5f4ef'
ORO = '#d5a84b'
APAGADO = '#8a867e'
FILETE = '#2b2b28'
FILETE_FUERTE = '#4a4740'

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTES = os.environ.get('INTER_TIGHT', AQUI)
R = os.path.join(FUENTES, 'InterTight-400.ttf')
M5 = os.path.join(FUENTES, 'InterTight-500.ttf')
M6 = os.path.join(FUENTES, 'InterTight-600.ttf')


def f(ruta, px):
    return ImageFont.truetype(ruta, px)


def track(d, xy, texto, fuente, fill, tr=3.0):
    x, y = xy
    for ch in texto:
        d.text((x, y), ch, font=fuente, fill=fill)
        x += d.textlength(ch, font=fuente) + tr


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


# ---------------------------------------------------------------- los glifos
# Geométricos y sobrios. El texto carga el mensaje; el glifo solo distingue.

def glifo_pmo(d, x, y):
    """Un portafolio: una retícula, y uno que no se sostiene."""
    lado, hueco = 26, 12
    marcado = (1, 2)
    for fila in range(3):
        for col in range(4):
            cx = x + col * (lado + hueco)
            cy = y + fila * (lado + hueco)
            mio = (fila, col) == marcado
            d.rectangle([(cx, cy), (cx + lado, cy + lado)],
                        fill=ORO if mio else None,
                        outline=ORO if mio else FILETE_FUERTE, width=2)


def glifo_cfo(d, x, y):
    """Un cierre: renglones de libro, y la línea que cuadra."""
    largo, alto, hueco = 152, 9, 19
    for i in range(5):
        ancho = largo if i < 4 else int(largo * 0.55)
        cy = y + i * (alto + hueco)
        d.rectangle([(x, cy), (x + ancho, cy + alto)],
                    fill=ORO if i == 4 else FILETE_FUERTE)


def glifo_clo(d, x, y):
    """Lo firmado: una hoja con la esquina doblada, y el sello."""
    an, al, esq = 120, 150, 34
    d.polygon([(x, y), (x + an - esq, y), (x + an, y + esq),
               (x + an, y + al), (x, y + al)], outline=FILETE_FUERTE, width=2)
    d.line([(x + an - esq, y), (x + an - esq, y + esq), (x + an, y + esq)],
           fill=FILETE_FUERTE, width=2)
    d.ellipse([(x + an - 46, y + al - 46), (x + an + 10, y + al + 10)],
              outline=ORO, width=3)


FAMILIAS = [
    {
        'archivo': 'pmo.png',
        'sigla': 'PMO',
        'funcion': 'Oficina de proyectos',
        'frase': 'Leo la documentación que tu PMO ya tiene, y digo qué no se sostiene.',
        'estado': 'Disponible',
        'glifo': glifo_pmo,
    },
    {
        'archivo': 'cfo.png',
        'sigla': 'CFO',
        'funcion': 'Cierre, control y reporte',
        'frase': 'Cierro contra lo que dicen los documentos, no contra lo que se declara.',
        'estado': 'Capacidad declarada',
        'glifo': glifo_cfo,
    },
    {
        'archivo': 'clo.png',
        'sigla': 'CLO',
        'funcion': 'Contratos y cumplimiento',
        'frase': 'Sé qué firmaste, qué vence, y a qué te obligaste.',
        'estado': 'Capacidad declarada',
        'glifo': glifo_clo,
    },
]


def emblema(fam):
    img = Image.new('RGB', (L, L), NEGRO)
    d = ImageDraw.Draw(img)

    # el marco: un filete fino por dentro del borde
    d.rectangle([(M // 2, M // 2), (L - M // 2, L - M // 2)], outline=FILETE, width=2)

    # El ritmo vertical va declarado, no estimado: cada bloque sabe dónde empieza
    # y cuánto ocupa. Estimarlo es como se llega a que una frase pise una insignia.
    X = M + 18
    fam['glifo'](d, X, 108)
    track(d, (X, 258), fam['sigla'], f(M6, 104), ORO, tr=6)       # ..390
    d.line([(X, 414), (L - M - 18, 414)], fill=FILETE_FUERTE, width=2)
    d.text((X, 434), fam['funcion'], font=f(M5, 34), fill=CREMA)  # ..476

    lineas = envolver(d, fam['frase'], f(R, 27), L - 2 * M - 36)
    assert len(lineas) <= 2, f"{fam['sigla']}: la frase no cabe en dos líneas"
    y = 496
    for linea in lineas:
        d.text((X, y), linea, font=f(R, 27), fill=APAGADO)
        y += 38                                                   # ..572

    disponible = fam['estado'] == 'Disponible'
    color = ORO if disponible else APAGADO
    texto = fam['estado'].upper()
    fu = f(M6, 19)
    ancho = sum(d.textlength(c, font=fu) + 2.4 for c in texto)
    caja = [(X, 600), (X + ancho + 36, 642)]
    d.rounded_rectangle(caja, radius=6,
                        fill='#2a1f0d' if disponible else None,
                        outline=color, width=2)
    track(d, (X + 18, 611), texto, fu, color, tr=2.4)
    return img


if __name__ == '__main__':
    for fam in FAMILIAS:
        emblema(fam).save(os.path.join(AQUI, fam['archivo']), 'PNG')
        print('listo', fam['archivo'])
