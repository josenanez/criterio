# Las figuras

```
pip install pillow cairosvg
python3 docs/img/graficos.py
```

Las escribe [`graficos.py`](graficos.py) con PIL, en los dos idiomas —también el GIF de
la familia y la cabecera de cada agente—, y **las tipografías
viajan con el repositorio** — `InterTight-400/500/600.ttf`, bajo SIL Open Font License.
Sin ellas el generador no corre, y un generador que solo funciona en la máquina de quien
lo escribió no es un generador.

Las figuras no se editan a mano: se edita el texto en `graficos.py` y se regeneran. El
script tiene aserciones sobre el alto que ocupa cada párrafo, así que un texto que se
salga de su caja rompe la generación en vez de publicar una figura con el texto encima
de otro.

Las capturas del portal, que son otra cosa —salen de un navegador contra el servidor
real—, están en [`portal/`](portal/) con su propio procedimiento.

Los robots no se dibujan aquí: sus trazos viven en
[`plugins/criterio-portfolio/scripts/robots.py`](../../plugins/criterio-portfolio/scripts/robots.py),
los mismos con que el servidor y josenanez.com los dibujan. El generador solo les pone
color —oro el que trabaja, crema al 38 % el que espera— y los anima.
