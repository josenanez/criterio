# -*- coding: utf-8 -*-
"""Los robots de Criterio, dibujados una sola vez.

Vera tiene un lente grande: mira el portafolio entero. Samuel escucha —dos antenas— y
lleva una libreta: lo que se prometió en cada reunión. Alba lleva un sol que sale: el
producto antes de que exista el proyecto. Rostrum es un gabinete de cintas y luces: el
servidor donde queda todo.

De la familia CFO, Clara —de *clarus*, ve claro— tiene un ojo con su lupa, la que acerca el
soporte, y en el pecho el libro a dos columnas, debe y haber, con la marca de lo que cuadra.
Tomás, «el gemelo», tiene dos antenas y dos ojos iguales, y en el pecho las barras en pares:
lo presupuestado al lado de lo ejecutado. Áurea —de *aureus*, de oro: la caja— lleva en el pecho
la puerta de una caja fuerte con su perilla, que gira: custodia el dinero y no lo mueve.

De la familia CLO, Fidel —de *fides*, la palabra dada— lleva en el pecho el documento con su
firma y su sello: lo que la empresa firmó. Constanza —de *constantia*— tiene un visor que no
parpadea y en el pecho la lista con cada casilla marcada: cada obligación con su evidencia,
todos los días.

Son los mismos trazos que josenanez.com usa en la página de Criterio. Aquí viven en un
solo lugar para que el servidor los dibuje en sus páginas y `docs/img/graficos.py` los
imprima para los README: si cambia un robot, cambia en todas partes.

Aquí vive también el símbolo de Criterio, el corchete y el punto: una cita, el corchete que
enmarca la evidencia y el punto que la sostiene. Es del mismo trazo redondeado que los robots
y, como ellos, se dibuja una sola vez (`simbolo()`); `docs/design.md` dice cómo se usa.
"""
from __future__ import annotations

ORDEN = ("vera", "samuel", "alba", "rostrum")
ORDEN_CFO = ("clara", "tomas", "aurea")
ORDEN_CLO = ("fidel", "constanza")
ORDEN_EA = ("ofelia",)
ORDEN_CSO = ("augusto", "valeria")
AGENTE = {"vera": "portafolio", "samuel": "proyecto", "alba": "producto", "rostrum": None,
          "clara": "finanzas", "tomas": "presupuesto", "aurea": "tesoreria", "fidel": "legal", "constanza": "cumplimiento",
          "ofelia": "direccion", "augusto": "comercial", "valeria": "ingresos"}

_PIERNAS = [("line", dict(x1=44, y1=134, x2=44, y2=158)), ("line", dict(x1=76, y1=134, x2=76, y2=158)),
            ("line", dict(x1=36, y1=160, x2=52, y2=160)), ("line", dict(x1=68, y1=160, x2=84, y2=160))]

# (tipo de pieza, elemento, atributos). "ln" es trazo; "ojo" y "led" son relleno.
_PIEZAS = {
    "vera": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)), ("ln", "circle", dict(cx=60, cy=50, r=18)),
        ("ojo", "circle", dict(cx=60, cy=50, r=9), "mira"),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=40, y1=98, x2=80, y2=98)), ("ln", "line", dict(x1=40, y1=108, x2=72, y2=108)),
        ("ln", "line", dict(x1=40, y1=118, x2=66, y2=118)),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "samuel": [
        ("ln", "path", dict(d="M24 40 Q8 40 8 26")), ("ln", "path", dict(d="M96 40 Q112 40 112 26")),
        ("led", "circle", dict(cx=8, cy=22, r=4)), ("led", "circle", dict(cx=112, cy=22, r=4), "led.1"),
        ("ln", "rect", dict(x=24, y=20, width=72, height=54, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=44, r=6)), ("ojo", "circle", dict(cx=75, cy=44, r=6)),
        ("ln", "line", dict(x1=44, y1=62, x2=76, y2=62)),
        ("ln", "rect", dict(x=30, y=80, width=60, height=54, rx=4)),
        ("ln", "rect", dict(x=74, y=96, width=28, height=34, rx=2)),
        ("ln", "line", dict(x1=79, y1=106, x2=97, y2=106), "escribe.0"),
        ("ln", "line", dict(x1=79, y1=114, x2=97, y2=114), "escribe.1"),
        ("ln", "line", dict(x1=79, y1=122, x2=92, y2=122), "escribe.2"), ("ln", "line", dict(x1=30, y1=94, x2=14, y2=116)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "alba": [
        ("ln", "path", dict(d="M30 46 A30 30 0 0 1 90 46")), ("led", "circle", dict(cx=60, cy=10, r=4)),
        ("ln", "line", dict(x1=60, y1=14, x2=60, y2=16)),
        ("ln", "rect", dict(x=24, y=46, width=72, height=34, rx=6)),
        ("ojo", "rect", dict(x=38, y=56, width=16, height=8)), ("ojo", "rect", dict(x=66, y=56, width=16, height=8)),
        ("ln", "rect", dict(x=30, y=86, width=60, height=48, rx=4)),
        ("ln", "path", dict(d="M44 120 A16 16 0 0 1 76 120"), "sale"), ("ln", "line", dict(x1=40, y1=120, x2=80, y2=120)),
        ("ln", "line", dict(x1=60, y1=96, x2=60, y2=100), "sale"), ("ln", "line", dict(x1=46, y1=102, x2=49, y2=105), "sale"),
        ("ln", "line", dict(x1=74, y1=102, x2=71, y2=105), "sale"),
        ("ln", "line", dict(x1=30, y1=98, x2=12, y2=86)), ("ln", "line", dict(x1=90, y1=98, x2=108, y2=86)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "clara": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=44, cy=50, r=6)),
        ("ln", "circle", dict(cx=74, cy=48, r=12), "lupa"), ("ojo", "circle", dict(cx=74, cy=48, r=5), "lupa"),
        ("ln", "line", dict(x1=82, y1=57, x2=92, y2=68), "lupa"),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=60, y1=90, x2=60, y2=128)),
        ("ln", "line", dict(x1=36, y1=98, x2=54, y2=98)), ("ln", "line", dict(x1=36, y1=108, x2=54, y2=108)),
        ("ln", "line", dict(x1=66, y1=98, x2=84, y2=98)), ("ln", "line", dict(x1=66, y1=108, x2=84, y2=108)),
        ("ln", "path", dict(d="M66 120 L72 126 L84 114"), "cuadra"),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "tomas": [
        ("ln", "line", dict(x1=46, y1=10, x2=46, y2=22)), ("ln", "line", dict(x1=74, y1=10, x2=74, y2=22)),
        ("led", "circle", dict(cx=46, cy=7, r=4)), ("led", "circle", dict(cx=74, cy=7, r=4), "led.1"),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "rect", dict(x=36, y=40, width=14, height=14)), ("ojo", "rect", dict(x=70, y=40, width=14, height=14)),
        ("ln", "line", dict(x1=48, y1=66, x2=72, y2=66)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=38, y1=126, x2=82, y2=126)),
        ("ln", "line", dict(x1=44, y1=126, x2=44, y2=106), "barra.0"), ("ln", "line", dict(x1=50, y1=126, x2=50, y2=110), "barra.1"),
        ("ln", "line", dict(x1=64, y1=126, x2=64, y2=98), "barra.2"), ("ln", "line", dict(x1=70, y1=126, x2=70, y2=94), "barra.3"),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "aurea": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=46, r=6)), ("ojo", "circle", dict(cx=75, cy=46, r=6)),
        ("ln", "line", dict(x1=48, y1=64, x2=72, y2=64)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "circle", dict(cx=60, cy=109, r=17)), ("ln", "circle", dict(cx=60, cy=109, r=6)),
        ("ln", "line", dict(x1=84, y1=100, x2=84, y2=118)),
        ("led", "circle", dict(cx=67, cy=109, r=2.5), "perilla"),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "fidel": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=46, r=6)), ("ojo", "circle", dict(cx=75, cy=46, r=6)),
        ("ln", "line", dict(x1=46, y1=64, x2=74, y2=64)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "path", dict(d="M40 90 L70 90 L80 100 L80 128 L40 128 Z")), ("ln", "path", dict(d="M70 90 L70 100 L80 100")),
        ("ln", "line", dict(x1=46, y1=100, x2=64, y2=100)), ("ln", "line", dict(x1=46, y1=108, x2=74, y2=108)),
        ("ln", "path", dict(d="M46 120 Q50 113 54 120 T62 120"), "firma"), ("led", "circle", dict(cx=72, cy=120, r=4), "sello"),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "constanza": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ln", "rect", dict(x=32, y=38, width=56, height=18, rx=9)), ("ojo", "rect", dict(x=40, y=43, width=40, height=8, rx=4), "visor"),
        ("ln", "line", dict(x1=48, y1=66, x2=72, y2=66)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
    ] + [p for i, y in enumerate((92, 104, 116)) for p in (
        ("ln", "rect", dict(x=38, y=y, width=9, height=9, rx=1)),
        ("ln", "path", dict(d=f"M39.5 {y + 4.5} L42 {y + 7} L46 {y + 1.5}"), f"marca.{i}"),
        ("ln", "line", dict(x1=53, y1=y + 4.5, x2=82, y2=y + 4.5)))] + [
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    # Ofelia: la agenda en el pecho, y el día que se prepara se marca
    "ofelia": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=46, r=6)), ("ojo", "circle", dict(cx=75, cy=46, r=6)),
        ("ln", "path", dict(d="M48 62 Q60 70 72 62")),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "rect", dict(x=38, y=94, width=44, height=34, rx=2)), ("ln", "line", dict(x1=38, y1=103, x2=82, y2=103)),
        ("ln", "line", dict(x1=48, y1=90, x2=48, y2=97)), ("ln", "line", dict(x1=72, y1=90, x2=72, y2=97)),
        ("led", "circle", dict(cx=47, cy=112, r=2)), ("led", "circle", dict(cx=60, cy=112, r=2), "led.1"),
        ("ln", "path", dict(d="M68 120 L72 124 L78 115"), "dia"),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    # Augusto: la tendencia en el pecho, y el punto del pronóstico al final de la línea
    "augusto": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=46, r=6)), ("ojo", "circle", dict(cx=75, cy=46, r=6)),
        ("ln", "line", dict(x1=48, y1=64, x2=72, y2=64)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=38, y1=92, x2=38, y2=126)), ("ln", "line", dict(x1=38, y1=126, x2=82, y2=126)),
        ("ln", "path", dict(d="M42 120 L52 112 L61 116 L71 104"), "traza"),
        ("ln", "path", dict(d="M71 104 L79 97"), "pronostico"), ("led", "circle", dict(cx=79, cy=97, r=3), "punta"),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    # Valeria: la venta, el contrato y la factura, y cada paso se enciende cuando llega
    "valeria": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=46, r=6)), ("ojo", "circle", dict(cx=75, cy=46, r=6)),
        ("ln", "path", dict(d="M48 62 Q60 70 72 62")),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
    ] + [p for i, x in enumerate((36, 54, 72)) for p in (
        ("ln", "rect", dict(x=x, y=94, width=12, height=16, rx=1)),
        ("ln", "line", dict(x1=x + 3, y1=100, x2=x + 9, y2=100)),
        ("led", "circle", dict(cx=x + 6, cy=120, r=3), f"paso.{i}"))] + [
        ("ln", "line", dict(x1=48, y1=102, x2=54, y2=102)), ("ln", "line", dict(x1=66, y1=102, x2=72, y2=102)),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "rostrum": [
        ("ln", "rect", dict(x=18, y=14, width=84, height=146, rx=3)),
        ("ln", "circle", dict(cx=42, cy=40, r=14)), ("ln", "circle", dict(cx=78, cy=40, r=14)),
        ("ojo", "circle", dict(cx=42, cy=40, r=4), "gira"), ("ojo", "circle", dict(cx=78, cy=40, r=4), "gira.2"),
        ("ln", "line", dict(x1=18, y1=66, x2=102, y2=66)),
    ] + [("led", "circle", dict(cx=cx, cy=80, r=3.5), f"corre.{i}") for i, cx in enumerate((32, 46, 60, 74, 88))] + [
        ("ln", "rect", dict(x=30, y=96, width=60, height=36, rx=2)),
        ("ln", "line", dict(x1=38, y1=108, x2=82, y2=108)), ("ln", "line", dict(x1=38, y1=118, x2=70, y2=118)),
        ("ln", "line", dict(x1=18, y1=144, x2=102, y2=144)),
    ],
}


# ══════════════════════════════════════════════════════════════════ los gestos
#
# Cada robot tiene un gesto propio, el de su oficio, además de los comunes: el cuerpo se mece,
# los ojos parpadean y las luces titilan. Los gestos son datos, no CSS escrito a mano: de la
# misma tabla salen la hoja de estilo del navegador (servidor, portal y los SVG de los README)
# y los cuadros del GIF de cada tarjeta. Así el robot se mueve igual en todas partes.
#
# Cada gesto: tipo (xy, y, opacidad o trazo), duración en segundos, paso entre piezas con
# índice («escribe.1» va un paso detrás de «escribe.0») y sus claves (fracción, valor), con
# interpolación lineal. «trazo» es la fracción del trazo que falta por dibujar: 1 oculto, 0
# completo. Todas las duraciones dividen VUELTA, para que el GIF cierre sin salto.

VUELTA = 4.8


def _onda(amplitud: float, n: int = 8) -> list:
    import math
    return [(k / n, (0, round(-amplitud * math.sin(math.pi * k / n), 3))) for k in range(n + 1)]


def _orbita(radio: float, n: int = 12) -> list:
    import math
    return [(k / n, (round(radio * math.cos(2 * math.pi * k / n) - radio, 3),
                     round(radio * math.sin(2 * math.pi * k / n), 3))) for k in range(n + 1)]


GESTOS = {
    # los comunes
    "cuerpo":   {"tipo": "xy", "dura": 1.6, "claves": _onda(3)},
    "parpadeo": {"tipo": "opacidad", "dura": 4.8, "claves": [(0, 1), (.9, 1), (.93, .1), (.96, 1), (1, 1)]},
    "led":      {"tipo": "opacidad", "dura": .8, "paso": .4, "claves": [(0, 1), (.5, 1), (.5, .35), (1, .35)]},
    # Vera: el lente recorre el portafolio de un lado al otro
    "mira":     {"tipo": "xy", "dura": 4.8, "claves": [(0, (0, 0)), (.2, (-6, 0)), (.45, (-6, 0)), (.65, (6, 0)),
                                                       (.85, (6, 0)), (1, (0, 0))]},
    # Samuel: la minuta, renglón por renglón
    "escribe":  {"tipo": "trazo", "dura": 2.4, "paso": .5, "claves": [(0, 1), (.25, 0), (.8, 0), (.85, 1), (1, 1)]},
    # Alba: el sol sale sobre el horizonte
    "sale":     {"tipo": "xy", "dura": 2.4, "claves": [(0, (0, 5)), (.4, (0, 0)), (.8, (0, 0)), (1, (0, 5))]},
    # Clara: la lupa se acerca al soporte, y lo que cuadra se marca
    "lupa":     {"tipo": "xy", "dura": 4.8, "claves": [(0, (0, 0)), (.25, (-4, 3)), (.5, (-4, 3)), (.75, (2, -1)),
                                                       (1, (0, 0))]},
    "cuadra":   {"tipo": "trazo", "dura": 2.4, "claves": [(0, 1), (.35, 1), (.55, 0), (.9, 0), (1, 1)]},
    # Tomás: las barras en pares, lo presupuestado al lado de lo ejecutado
    "barra":    {"tipo": "trazo", "dura": 2.4, "paso": .15, "claves": [(0, 1), (.3, 0), (.8, 0), (.95, 1), (1, 1)]},
    # Áurea: la perilla de la caja fuerte da la vuelta
    "perilla":  {"tipo": "xy", "dura": 2.4, "claves": _orbita(7)},
    # Fidel: la firma se traza y después se enciende el sello
    "firma":    {"tipo": "trazo", "dura": 2.4, "claves": [(0, 1), (.35, 0), (.85, 0), (.9, 1), (1, 1)]},
    "sello":    {"tipo": "opacidad", "dura": 2.4, "claves": [(0, .3), (.4, .3), (.45, 1), (.85, 1), (.9, .3), (1, .3)]},
    # Constanza: el visor no parpadea, barre; cada casilla se marca, todos los días
    "visor":    {"tipo": "xy", "dura": 2.4, "claves": [(0, (0, 0)), (.25, (-3, 0)), (.75, (3, 0)), (1, (0, 0))]},
    "marca":    {"tipo": "trazo", "dura": 2.4, "paso": .4, "claves": [(0, 1), (.15, 0), (.8, 0), (.85, 1), (1, 1)]},
    # Ofelia: el día de la agenda se marca cuando queda preparado
    "dia":      {"tipo": "trazo", "dura": 2.4, "claves": [(0, 1), (.3, 1), (.5, 0), (.9, 0), (1, 1)]},
    # Augusto: la tendencia se traza, el pronóstico la sigue y su punto se enciende
    "traza":    {"tipo": "trazo", "dura": 2.4, "claves": [(0, 1), (.3, 0), (.85, 0), (.9, 1), (1, 1)]},
    "pronostico": {"tipo": "trazo", "dura": 2.4, "claves": [(0, 1), (.3, 1), (.45, 0), (.85, 0), (.9, 1), (1, 1)]},
    "punta":    {"tipo": "opacidad", "dura": 2.4, "claves": [(0, .3), (.45, .3), (.5, 1), (.85, 1), (.9, .3), (1, .3)]},
    # Valeria: la venta, el contrato y la factura se encienden uno detrás de otro
    "paso":     {"tipo": "opacidad", "dura": 2.4, "paso": .4, "claves": [(0, .3), (.15, 1), (.8, 1), (.85, .3), (1, .3)]},
    # Rostrum: los carretes giran y las luces corren
    "gira":     {"tipo": "xy", "dura": 1.6, "paso": .4, "claves": _orbita(5)},
    "corre":    {"tipo": "opacidad", "dura": 1.2, "paso": .24, "claves": [(0, 1), (.2, 1), (.2, .3), (1, .3)]},
}
QUIETOS = ("rostrum",)   # un gabinete no se mece
_COMUN = {"ojo": "parpadeo", "led": "led"}


def _gesto(robot: str, tipo: str, marca: str | None) -> tuple[str | None, float]:
    """El gesto de una pieza y su retraso (en segundos, dentro de su ciclo)."""
    nombre = marca or _COMUN.get(tipo)
    if not nombre:
        return None, 0.0
    base, _, idx = nombre.partition(".")
    g = GESTOS[base]
    return base, round(int(idx or 0) * g.get("paso", 0), 3)


def _valor(base: str, local: float):
    """El valor del gesto en una fracción de su ciclo, interpolando entre claves."""
    claves = GESTOS[base]["claves"]
    for (f0, v0), (f1, v1) in zip(claves, claves[1:]):
        if f0 <= local <= f1:
            a = 0 if f1 == f0 else (local - f0) / (f1 - f0)
            if isinstance(v0, tuple):
                return tuple(x0 + (x1 - x0) * a for x0, x1 in zip(v0, v1))
            return v0 + (v1 - v0) * a
    return claves[-1][1]


def _en(base: str, retraso: float, t: float):
    g = GESTOS[base]
    local = round((t - retraso) % g["dura"], 6) % g["dura"]   # sin el error de coma flotante
    return _valor(base, local / g["dura"])


def _largo(elemento: str, a: dict) -> float:
    """El largo de un trazo, para dibujarlo por partes en un cuadro del GIF."""
    import math
    import re
    if elemento == "line":
        return math.dist((a["x1"], a["y1"]), (a["x2"], a["y2"]))
    if elemento != "path":
        raise ValueError(f"un trazo que se dibuja tiene que ser línea o camino, no {elemento}")
    num = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", a["d"])]
    ordenes = re.findall(r"[MLQTZ]", a["d"])
    largo, i, actual, inicio, control = 0.0, 0, None, None, None
    for o in ordenes:
        if o == "M":
            actual = inicio = (num[i], num[i + 1]); i += 2; control = None
        elif o == "L":
            nxt = (num[i], num[i + 1]); i += 2; largo += math.dist(actual, nxt); actual = nxt; control = None
        elif o in "QT":
            if o == "Q":
                c = (num[i], num[i + 1]); nxt = (num[i + 2], num[i + 3]); i += 4
            else:
                c = (2 * actual[0] - control[0], 2 * actual[1] - control[1]) if control else actual
                nxt = (num[i], num[i + 1]); i += 2
            pts = [((1 - u) ** 2 * actual[0] + 2 * (1 - u) * u * c[0] + u * u * nxt[0],
                    (1 - u) ** 2 * actual[1] + 2 * (1 - u) * u * c[1] + u * u * nxt[1]) for u in
                   (k / 24 for k in range(25))]
            largo += sum(math.dist(p, q) for p, q in zip(pts, pts[1:]))
            actual, control = nxt, c
        elif o == "Z":
            largo += math.dist(actual, inicio); actual = inicio
    return largo


def css(selector: str = ".cr-anima") -> str:
    """La hoja de estilo de los gestos, una vez por página. Solo se mueve lo que está dentro de
    `selector`, y nada se mueve si la persona pidió reducir el movimiento."""
    reglas = []
    for base, g in GESTOS.items():
        pasos = []
        for f, v in g["claves"]:
            if g["tipo"] == "xy":
                prop = f"transform:translate({v[0]:g}px,{v[1]:g}px)"
            elif g["tipo"] == "opacidad":
                prop = f"opacity:{v:g}"
            else:
                prop = f"stroke-dashoffset:{v:g}"
            pasos.append(f"{f * 100:g}%{{{prop}}}")
        reglas.append(f"@keyframes cr-{base}{{{''.join(pasos)}}}")
        # Una vuelta y se queda quieto: lo que se mueve solo más de cinco segundos tiene que
        # poderse parar (WCAG 2.2.2). Sigue moviéndose mientras el puntero o el foco están encima.
        veces = round(VUELTA / g["dura"])
        reglas.append(f"{selector} .g-{base}{{animation:cr-{base} {g['dura']:g}s linear {veces}}}")
        reglas.append(f"{selector}:hover .g-{base},a:hover>{selector} .g-{base},"
                      f"a:focus-visible>{selector} .g-{base}{{animation-iteration-count:infinite}}")
    reglas.append("@media (prefers-reduced-motion: reduce){"
                  f"{selector} *{{animation:none!important;stroke-dashoffset:0!important;"
                  "transform:none!important;opacity:1!important}}}")
    return "".join(reglas)


def svg(robot: str, trazo: str, acento: str, ancho: float = 120, grosor: float = 2.5,
        clase: str = "robot", animado: bool = False, estilo: bool = True, t: float | None = None) -> str:
    """El robot como `<svg>` autónomo, con los colores puestos en cada pieza: sirve igual
    dentro de una página que convertido a PNG, sin hojas de estilo de por medio.

    `animado` le pone sus gestos para el navegador; con `estilo` lleva su propia hoja (un SVG
    suelto, como el de un README), y sin ella la pone la página, una sola vez (`css()`). `t`
    dibuja el robot quieto en ese segundo de su vuelta: es un cuadro del GIF."""
    partes = []
    for pieza in _PIEZAS[robot]:
        tipo, elemento, atributos = pieza[:3]
        base, retraso = _gesto(robot, tipo, pieza[3] if len(pieza) > 3 else None)
        a = " ".join(f'{k}="{v}"' for k, v in atributos.items())
        if tipo == "ln":
            est = (f'fill="none" stroke="{trazo}" stroke-width="{grosor}" '
                   'stroke-linejoin="round" stroke-linecap="round"')
        else:
            est = f'fill="{acento}" stroke="none"'
        cls, extra = tipo, ""
        if base and animado:
            cls += f" g-{base}"
            if GESTOS[base]["tipo"] == "trazo":
                extra += ' pathLength="1" stroke-dasharray="1"'
            if retraso:
                # Un retraso negativo arranca la pieza ya desfasada, sin esperar en blanco.
                extra += f' style="animation-delay:-{(GESTOS[base]["dura"] - retraso) % GESTOS[base]["dura"]:g}s"'
            if GESTOS[base]["tipo"] == "xy":
                extra += ' transform-origin="center"'
        elif base and t is not None:
            v = _en(base, retraso, t)
            kind = GESTOS[base]["tipo"]
            if kind == "xy":
                extra += f' transform="translate({v[0]:.3f} {v[1]:.3f})"'
            elif kind == "opacidad":
                extra += f' opacity="{v:.3f}"'
            else:
                L = _largo(elemento, atributos)
                extra += f' stroke-dasharray="{L:.3f} {L + 1:.3f}" stroke-dashoffset="{L * v:.3f}"'
        partes.append(f'<{elemento} class="{cls}" {a} {est}{extra}/>')
    cuerpo = "".join(partes)
    if robot not in QUIETOS:
        if animado:
            cuerpo = f'<g class="g-cuerpo">{cuerpo}</g>'
        elif t is not None:
            dy = _en("cuerpo", 0, t)[1]
            cuerpo = f'<g transform="translate(0 {dy:.3f})">{cuerpo}</g>'
    hoja = f"<style>{css('.cr-anima')}</style>" if animado and estilo else ""
    clases = clase + (" cr-anima" if animado else "")
    alto = ancho * 170 / 120
    return (f'<svg class="{clases}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 170" '
            f'width="{ancho:g}" height="{alto:g}" role="img" aria-label="{robot}" overflow="visible">'
            + hoja + cuerpo + "</svg>")


# El símbolo, en una caja de 64 × 64. El trazo engruesa por debajo de 32 px para que se siga
# leyendo a 16 px, el tamaño de una pestaña del navegador.
# Y la promesa, que va con el símbolo en la cabecera de Rostrum, del portal y del README.
PROMESA = {"es": "La evidencia antes de la decisión", "en": "Evidence before the decision"}
SIMBOLO = {"corchete": "M27 11H17.5Q11 11 11 17.5V46.5Q11 53 17.5 53H27", "punto": (39, 32, 7.5),
           "grosor": 5.5, "grosor_chico": 7.5}


def simbolo(color: str, alto: float = 64, titulo: str | None = "Criterio", clase: str = "simbolo") -> str:
    """El corchete y el punto como `<svg>`. Con `titulo` se anuncia como imagen; sin él es
    decorativo (va junto a la palabra «Criterio», que ya lo dice)."""
    g = SIMBOLO["grosor"] if alto >= 32 else SIMBOLO["grosor_chico"]
    cx, cy, r = SIMBOLO["punto"]
    rol = (f'role="img" aria-label="{titulo}"' if titulo else 'aria-hidden="true" focusable="false"')
    return (f'<svg class="{clase}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="{alto:g}" '
            f'height="{alto:g}" {rol}><path d="{SIMBOLO["corchete"]}" fill="none" stroke="{color}" '
            f'stroke-width="{g}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/></svg>')


def datos() -> dict:
    """Los robots como datos, para quien los dibuja con su propio marcado (el portal): las
    piezas, el gesto y el retraso de cada una, y la hoja de los gestos."""
    out = {}
    for robot, piezas in _PIEZAS.items():
        lista = []
        for pieza in piezas:
            tipo, elemento, atributos = pieza[:3]
            base, retraso = _gesto(robot, tipo, pieza[3] if len(pieza) > 3 else None)
            d = {"tipo": tipo, "elemento": elemento, "attrs": atributos}
            if base:
                g = GESTOS[base]
                d["gesto"] = base
                d["trazo"] = g["tipo"] == "trazo"
                if retraso:
                    d["retraso"] = round((g["dura"] - retraso) % g["dura"], 3)
            lista.append(d)
        out[robot] = {"piezas": lista, "quieto": robot in QUIETOS}
    return {"robots": out, "css": css(".cr-anima"), "vuelta": VUELTA, "simbolo": SIMBOLO, "promesa": PROMESA}


def selftest() -> int:
    fallas = []

    def ok(que, cond):
        print(f'{"  ok  " if cond else " FALLA"} {que}')
        if not cond:
            fallas.append(que)
    todos = ORDEN + ORDEN_CFO + ORDEN_CLO + ORDEN_EA + ORDEN_CSO
    ok("cada duración divide la vuelta: el GIF cierra sin salto",
       all(abs(VUELTA / g["dura"] - round(VUELTA / g["dura"])) < 1e-9 for g in GESTOS.values()))
    propios = {r: {p[3].split(".")[0] for p in _PIEZAS[r] if len(p) > 3} - set(_COMUN.values()) for r in todos}
    ok("cada robot tiene un gesto propio, el de su oficio", all(propios[r] for r in todos))
    ok("y ningún gesto propio se repite entre robots",
       len(set().union(*propios.values())) == sum(len(v) for v in propios.values()))
    ok("todo gesto marcado existe", all(p[3].split(".")[0] in GESTOS for r in todos for p in _PIEZAS[r] if len(p) > 3))
    ok("los trazos que se dibujan son líneas o caminos con largo",
       all(_largo(p[1], p[2]) > 0 for r in todos for p in _PIEZAS[r]
           if len(p) > 3 and GESTOS[p[3].split(".")[0]]["tipo"] == "trazo"))
    ok("Constanza no parpadea", not any(p[0] == "ojo" and len(p) < 4 for p in _PIEZAS["constanza"]))
    quieto = svg("vera", "#000", "#000")
    ok("sin animar, el robot es el de siempre: ni hoja ni clases de gesto", "<style>" not in quieto and "g-" not in quieto)
    vivo = svg("samuel", "#000", "#000", animado=True)
    ok("animado, lleva su hoja, sus gestos y el retraso de cada renglón",
       "<style>" in vivo and "g-escribe" in vivo and "animation-delay" in vivo and "prefers-reduced-motion" in vivo)
    ok("sin hoja propia, la pone la página", "<style>" not in svg("samuel", "#000", "#000", animado=True, estilo=False))
    c0, c1 = svg("fidel", "#000", "#000", t=0.1), svg("fidel", "#000", "#000", t=1.5)
    ok("un cuadro del GIF es un SVG quieto, y dos segundos distintos se ven distintos",
       "<style>" not in c0 and "stroke-dashoffset" in c0 and c0 != c1)
    ok("y la vuelta cierra: el segundo 0 y el de la vuelta son el mismo cuadro",
       svg("tomas", "#000", "#000", t=0) == svg("tomas", "#000", "#000", t=VUELTA))
    hoja = css()
    ok("se mueve una vuelta y se para; sigue solo con el puntero o el foco encima (WCAG 2.2.2)",
       "linear infinite" not in hoja and f"linear {round(VUELTA / GESTOS['cuerpo']['dura'])}" in hoja
       and "animation-iteration-count:infinite" in hoja and VUELTA <= 5)
    d = datos()
    ok("los datos del portal traen los ocho robots y la misma hoja", set(d["robots"]) == set(todos) and d["css"] == css())
    ok("el portal recibe el símbolo de aquí, no una copia", d["simbolo"] == SIMBOLO)
    chico, grande = simbolo("#000", 16, None), simbolo("#000", 64)
    ok("el símbolo engruesa por debajo de 32 px y, junto a la palabra, no se anuncia dos veces",
       f'stroke-width="{SIMBOLO["grosor_chico"]}"' in chico and 'aria-hidden="true"' in chico
       and 'aria-label="Criterio"' in grande)
    print()
    if fallas:
        print(f"{len(fallas)} falla(s)")
        return 1
    print("todo pasa")
    return 0


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    print(__doc__)
