# -*- coding: utf-8 -*-
"""Los robots de la familia para los README, en los dos idiomas.

    pip install cairosvg
    python3 docs/img/robots.py

Los trazos salen de `plugins/criterio-portfolio/scripts/robots.py`, el mismo archivo con
que el servidor los dibuja: aquí solo se ponen sobre el panel negro de las demás figuras
(docs/design.md), con Inter Tight. Sale a docs/img/es/ y docs/img/en/:

    robots.png            los cuatro en fila, para el README de la familia
    robot-<nombre>.png    uno por agente, para la cabecera de su README
"""
import io
import os
import sys

import cairosvg
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "..", "plugins", "criterio-portfolio", "scripts"))
import robots  # noqa: E402

R = os.path.join(AQUI, "InterTight-400.ttf")
M5 = os.path.join(AQUI, "InterTight-500.ttf")
M6 = os.path.join(AQUI, "InterTight-600.ttf")
NEGRO, PANEL, CREMA, ORO = "#050505", "#0c0c0b", "#f5f4ef", "#d5a84b"
APAGADO, FILETE = "#8a867e", "#2b2b28"

TEXTO = {
    "es": {
        "vera": ("Vera", "Director de proyectos", "Para quien responde por el portafolio completo."),
        "samuel": ("Samuel", "Gerente de proyecto", "Para quien responde por un proyecto."),
        "alba": ("Alba", "Gerente de producto", "Para quien define qué se construye."),
        "rostrum": ("Rostrum", "El servidor", "Donde quedan las corridas de los tres."),
        "fila": "CRITERIO · PMO",
        "rol": {"vera": "El portafolio", "samuel": "Un proyecto", "alba": "Un producto", "rostrum": "El servidor"},
    },
    "en": {
        "vera": ("Vera", "Project director", "For whoever answers for the whole portfolio."),
        "samuel": ("Samuel", "Project manager", "For whoever answers for one project."),
        "alba": ("Alba", "Product manager", "For whoever defines what gets built."),
        "rostrum": ("Rostrum", "The server", "Where the three agents' runs are kept."),
        "fila": "CRITERIO · PMO",
        "rol": {"vera": "The portfolio", "samuel": "One project", "alba": "One product", "rostrum": "The server"},
    },
}


def f(ruta, px):
    return ImageFont.truetype(ruta, px)


def robot_png(nombre, ancho):
    svg = robots.svg(nombre, CREMA, ORO, ancho=120, grosor=2.5)
    datos = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=ancho)
    return Image.open(io.BytesIO(datos)).convert("RGBA")


def track(d, xy, texto, fuente, fill, tr=3.0):
    x, y = xy
    for ch in texto:
        d.text((x, y), ch, font=fuente, fill=fill)
        x += d.textlength(ch, font=fuente) + tr


def tarjeta(idioma, nombre):
    nom, rol, frase = TEXTO[idioma][nombre]
    img = Image.new("RGB", (720, 720), NEGRO)
    d = ImageDraw.Draw(img)
    d.rectangle([32, 32, 687, 687], outline=FILETE, width=2)
    r = robot_png(nombre, 200)
    img.paste(r, (82, 70), r)
    d.text((82, 380), nom, font=f(M6, 96), fill=ORO)
    d.line([82, 512, 638, 512], fill=FILETE, width=2)
    d.text((82, 534), rol, font=f(M5, 32), fill=CREMA)
    d.text((82, 584), frase, font=f(R, 25), fill=APAGADO)
    return img


def fila(idioma):
    img = Image.new("RGB", (1680, 600), NEGRO)
    d = ImageDraw.Draw(img)
    d.rectangle([72, 60, 1607, 540], fill=PANEL, outline=FILETE, width=2)
    track(d, (108, 92), TEXTO[idioma]["fila"], f(M6, 20), ORO)
    col = (1607 - 72) / 4
    for i, nombre in enumerate(robots.ORDEN):
        cx = 72 + col * i + col / 2
        r = robot_png(nombre, 180)
        img.paste(r, (int(cx - r.width / 2), 150), r)
        nom = TEXTO[idioma][nombre][0].upper()
        fn = f(M6, 24)
        w = d.textlength(nom, font=fn) + 3 * (len(nom) - 1)
        track(d, (cx - w / 2, 430), nom, fn, CREMA)
        rol = TEXTO[idioma]["rol"][nombre]
        fr = f(R, 22)
        d.text((cx - d.textlength(rol, font=fr) / 2, 470), rol, font=fr, fill=ORO)
    return img


def guardar(img, idioma, archivo):
    ruta = os.path.join(AQUI, idioma, archivo)
    img.save(ruta, optimize=True)
    print(ruta)


if __name__ == "__main__":
    for idioma in ("es", "en"):
        guardar(fila(idioma), idioma, "robots.png")
        for nombre in robots.ORDEN:
            guardar(tarjeta(idioma, nombre), idioma, f"robot-{nombre}.png")
