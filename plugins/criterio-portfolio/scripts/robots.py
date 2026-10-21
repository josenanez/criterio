# -*- coding: utf-8 -*-
"""Los robots de Criterio, dibujados una sola vez.

Vera tiene un lente grande: mira el portafolio entero. Samuel escucha —dos antenas— y
lleva una libreta: lo que se prometió en cada reunión. Alba lleva un sol que sale: el
producto antes de que exista el proyecto. Rostrum es un gabinete de cintas y luces: el
servidor donde queda todo.

De la familia CFO, Clara —de *clarus*, ve claro— tiene un ojo con su lupa, la que acerca el
soporte, y en el pecho el libro a dos columnas, debe y haber, con la marca de lo que cuadra.
Tomás, «el gemelo», tiene dos antenas y dos ojos iguales, y en el pecho las barras en pares:
lo presupuestado al lado de lo ejecutado.

De la familia CLO, Fidel —de *fides*, la palabra dada— lleva en el pecho el documento con su
firma y su sello: lo que la empresa firmó. Constanza —de *constantia*— tiene un visor que no
parpadea y en el pecho la lista con cada casilla marcada: cada obligación con su evidencia,
todos los días.

Son los mismos trazos que josenanez.com usa en la página de Criterio. Aquí viven en un
solo lugar para que el servidor los dibuje en sus páginas y `docs/img/graficos.py` los
imprima para los README: si cambia un robot, cambia en todas partes.
"""
from __future__ import annotations

ORDEN = ("vera", "samuel", "alba", "rostrum")
ORDEN_CFO = ("clara", "tomas")
ORDEN_CLO = ("fidel", "constanza")
AGENTE = {"vera": "portafolio", "samuel": "proyecto", "alba": "producto", "rostrum": None,
          "clara": "finanzas", "tomas": "presupuesto", "fidel": "contratos", "constanza": "cumplimiento"}

_PIERNAS = [("line", dict(x1=44, y1=134, x2=44, y2=158)), ("line", dict(x1=76, y1=134, x2=76, y2=158)),
            ("line", dict(x1=36, y1=160, x2=52, y2=160)), ("line", dict(x1=68, y1=160, x2=84, y2=160))]

# (tipo de pieza, elemento, atributos). "ln" es trazo; "ojo" y "led" son relleno.
_PIEZAS = {
    "vera": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)), ("ln", "circle", dict(cx=60, cy=50, r=18)),
        ("ojo", "circle", dict(cx=60, cy=50, r=9)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=40, y1=98, x2=80, y2=98)), ("ln", "line", dict(x1=40, y1=108, x2=72, y2=108)),
        ("ln", "line", dict(x1=40, y1=118, x2=66, y2=118)),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "samuel": [
        ("ln", "path", dict(d="M24 40 Q8 40 8 26")), ("ln", "path", dict(d="M96 40 Q112 40 112 26")),
        ("led", "circle", dict(cx=8, cy=22, r=4)), ("led", "circle", dict(cx=112, cy=22, r=4)),
        ("ln", "rect", dict(x=24, y=20, width=72, height=54, rx=6)),
        ("ojo", "circle", dict(cx=45, cy=44, r=6)), ("ojo", "circle", dict(cx=75, cy=44, r=6)),
        ("ln", "line", dict(x1=44, y1=62, x2=76, y2=62)),
        ("ln", "rect", dict(x=30, y=80, width=60, height=54, rx=4)),
        ("ln", "rect", dict(x=74, y=96, width=28, height=34, rx=2)),
        ("ln", "line", dict(x1=79, y1=106, x2=97, y2=106)), ("ln", "line", dict(x1=79, y1=114, x2=97, y2=114)),
        ("ln", "line", dict(x1=79, y1=122, x2=92, y2=122)), ("ln", "line", dict(x1=30, y1=94, x2=14, y2=116)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "alba": [
        ("ln", "path", dict(d="M30 46 A30 30 0 0 1 90 46")), ("led", "circle", dict(cx=60, cy=10, r=4)),
        ("ln", "line", dict(x1=60, y1=14, x2=60, y2=16)),
        ("ln", "rect", dict(x=24, y=46, width=72, height=34, rx=6)),
        ("ojo", "rect", dict(x=38, y=56, width=16, height=8)), ("ojo", "rect", dict(x=66, y=56, width=16, height=8)),
        ("ln", "rect", dict(x=30, y=86, width=60, height=48, rx=4)),
        ("ln", "path", dict(d="M44 120 A16 16 0 0 1 76 120")), ("ln", "line", dict(x1=40, y1=120, x2=80, y2=120)),
        ("ln", "line", dict(x1=60, y1=96, x2=60, y2=100)), ("ln", "line", dict(x1=46, y1=102, x2=49, y2=105)),
        ("ln", "line", dict(x1=74, y1=102, x2=71, y2=105)),
        ("ln", "line", dict(x1=30, y1=98, x2=12, y2=86)), ("ln", "line", dict(x1=90, y1=98, x2=108, y2=86)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "clara": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "circle", dict(cx=44, cy=50, r=6)),
        ("ln", "circle", dict(cx=74, cy=48, r=12)), ("ojo", "circle", dict(cx=74, cy=48, r=5)),
        ("ln", "line", dict(x1=82, y1=57, x2=92, y2=68)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=60, y1=90, x2=60, y2=128)),
        ("ln", "line", dict(x1=36, y1=98, x2=54, y2=98)), ("ln", "line", dict(x1=36, y1=108, x2=54, y2=108)),
        ("ln", "line", dict(x1=66, y1=98, x2=84, y2=98)), ("ln", "line", dict(x1=66, y1=108, x2=84, y2=108)),
        ("ln", "path", dict(d="M66 120 L72 126 L84 114")),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "tomas": [
        ("ln", "line", dict(x1=46, y1=10, x2=46, y2=22)), ("ln", "line", dict(x1=74, y1=10, x2=74, y2=22)),
        ("led", "circle", dict(cx=46, cy=7, r=4)), ("led", "circle", dict(cx=74, cy=7, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ojo", "rect", dict(x=36, y=40, width=14, height=14)), ("ojo", "rect", dict(x=70, y=40, width=14, height=14)),
        ("ln", "line", dict(x1=48, y1=66, x2=72, y2=66)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
        ("ln", "line", dict(x1=38, y1=126, x2=82, y2=126)),
        ("ln", "line", dict(x1=44, y1=126, x2=44, y2=106)), ("ln", "line", dict(x1=50, y1=126, x2=50, y2=110)),
        ("ln", "line", dict(x1=64, y1=126, x2=64, y2=98)), ("ln", "line", dict(x1=70, y1=126, x2=70, y2=94)),
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
        ("ln", "path", dict(d="M46 120 Q50 113 54 120 T62 120")), ("led", "circle", dict(cx=72, cy=120, r=4)),
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "constanza": [
        ("ln", "line", dict(x1=60, y1=8, x2=60, y2=22)), ("led", "circle", dict(cx=60, cy=6, r=4)),
        ("ln", "rect", dict(x=22, y=22, width=76, height=56, rx=6)),
        ("ln", "rect", dict(x=32, y=38, width=56, height=18, rx=9)), ("ojo", "rect", dict(x=40, y=43, width=40, height=8, rx=4)),
        ("ln", "line", dict(x1=48, y1=66, x2=72, y2=66)),
        ("ln", "rect", dict(x=30, y=84, width=60, height=50, rx=4)),
    ] + [p for y in (92, 104, 116) for p in (
        ("ln", "rect", dict(x=38, y=y, width=9, height=9, rx=1)),
        ("ln", "path", dict(d=f"M39.5 {y + 4.5} L42 {y + 7} L46 {y + 1.5}")),
        ("ln", "line", dict(x1=53, y1=y + 4.5, x2=82, y2=y + 4.5)))] + [
        ("ln", "line", dict(x1=30, y1=96, x2=12, y2=112)), ("ln", "line", dict(x1=90, y1=96, x2=108, y2=112)),
    ] + [("ln", t, a) for t, a in _PIERNAS],
    "rostrum": [
        ("ln", "rect", dict(x=18, y=14, width=84, height=146, rx=3)),
        ("ln", "circle", dict(cx=42, cy=40, r=14)), ("ln", "circle", dict(cx=78, cy=40, r=14)),
        ("ojo", "circle", dict(cx=42, cy=40, r=4)), ("ojo", "circle", dict(cx=78, cy=40, r=4)),
        ("ln", "line", dict(x1=18, y1=66, x2=102, y2=66)),
    ] + [("led", "circle", dict(cx=cx, cy=80, r=3.5)) for cx in (32, 46, 60, 74, 88)] + [
        ("ln", "rect", dict(x=30, y=96, width=60, height=36, rx=2)),
        ("ln", "line", dict(x1=38, y1=108, x2=82, y2=108)), ("ln", "line", dict(x1=38, y1=118, x2=70, y2=118)),
        ("ln", "line", dict(x1=18, y1=144, x2=102, y2=144)),
    ],
}


def svg(robot: str, trazo: str, acento: str, ancho: float = 120, grosor: float = 2.5,
        clase: str = "robot") -> str:
    """El robot como `<svg>` autónomo, con los colores puestos en cada pieza: sirve igual
    dentro de una página que convertido a PNG, sin hojas de estilo de por medio."""
    partes = []
    for tipo, elemento, atributos in _PIEZAS[robot]:
        a = " ".join(f'{k}="{v}"' for k, v in atributos.items())
        if tipo == "ln":
            estilo = (f'fill="none" stroke="{trazo}" stroke-width="{grosor}" '
                      'stroke-linejoin="round" stroke-linecap="round"')
        else:
            estilo = f'fill="{acento}" stroke="none"'
        partes.append(f'<{elemento} class="{tipo}" {a} {estilo}/>')
    alto = ancho * 170 / 120
    return (f'<svg class="{clase}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 170" '
            f'width="{ancho:g}" height="{alto:g}" role="img" aria-label="{robot}">'
            + "".join(partes) + "</svg>")
