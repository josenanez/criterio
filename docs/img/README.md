# Las figuras

```
INTER_TIGHT=. python3 graficos.py
```

Las escribe [`graficos.py`](graficos.py) con PIL, en los dos idiomas, y **las tipografías
viajan con el repositorio** — `InterTight-400/500/600.ttf`, bajo SIL Open Font License.
Sin ellas el generador no corre, y un generador que solo funciona en la máquina de quien
lo escribió no es un generador.

Las figuras no se editan a mano: se edita el texto en `graficos.py` y se regeneran. El
script tiene aserciones sobre el alto que ocupa cada párrafo, así que un texto que se
salga de su caja rompe la generación en vez de publicar una figura con el texto encima
de otro.

Las capturas del portal, que son otra cosa —salen de un navegador contra el servidor
real—, están en [`portal/`](portal/) con su propio procedimiento.
