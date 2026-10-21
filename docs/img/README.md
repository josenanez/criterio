# Las figuras

```
pip install pillow cairosvg
python3 docs/img/graficos.py
```

Las escribe [`graficos.py`](graficos.py) con PIL, en los dos idiomas —también la
cabecera de cada agente—, y **las tipografías
viajan con el repositorio** — `InterTight-400/500/600.ttf`, bajo SIL Open Font License.
Sin ellas el generador no corre, y un generador que solo funciona en la máquina de quien
lo escribió no es un generador.

Las figuras no se editan a mano: se edita el texto en `graficos.py` y se regeneran. El
script tiene aserciones sobre el alto que ocupa cada párrafo, así que un texto que se
salga de su caja rompe la generación en vez de publicar una figura con el texto encima
de otro.

Las capturas del portal, que son otra cosa —salen de un navegador contra el servidor
real—, están en [`portal/`](portal/) con su propio procedimiento.

Los robots no se dibujan aquí: sus trazos **y sus gestos** viven en
[`plugins/criterio-server/scripts/robots.py`](../../plugins/criterio-server/scripts/robots.py),
los mismos con que Rostrum y josenanez.com los dibujan. Cada robot tiene el gesto de su
oficio —el lente de Vera recorre el portafolio, Samuel escribe la minuta, a Alba le sale el
sol, la lupa de Clara se acerca al soporte, las barras de Tomás suben en pares, Fidel traza
su firma y enciende el sello, Constanza marca cada casilla sin parpadear y los carretes de
Rostrum giran— y de esa tabla sale todo lo que se mueve:

| Pieza | Para qué |
|---|---|
| `es/robot-<agente>.gif`, `en/robot-<agente>.gif` | La tarjeta animada de cada agente, en la cabecera de su README |
| `robots/<agente>.svg` | El robot solo, animado con su propia hoja de estilo: el portal lo publica tal cual |
| `robots/robots.json` | Las piezas y los gestos como datos, para la impresora del portal, y el símbolo |
| `es/og-<página>.png`, `en/og-<página>.png` | La tarjeta social de la página de cada familia y de Rostrum, 1200 × 630: el logotipo, la promesa, el título y sus robots. El portal la copia a `public/images/agents/` |
| `marca/simbolo-claro.svg`, `marca/simbolo-oscuro.svg` | El símbolo de Criterio, el corchete y el punto: `-claro` para fondo crema, `-oscuro` para fondo negro |
| `marca/logotipo-*.svg` | El símbolo y «Criterio», con la palabra convertida en trazo |
| `marca/<idioma>/criterio-<sigla>-*.svg` | El logotipo de cada familia con su función en palabras, que sale de su `familia.json` |

Nada de eso se edita a mano. Quien pide reducir el movimiento ve el robot quieto.

El GIF de cada familia (`es/robots.gif` de la PMO, `es/robots-cfo.gif`, `es/robots-clo.gif`
y sus pares en inglés) no sale de aquí: se graba del componente del portal, que es el dueño
de la impresora, junto con el video del post. El procedimiento está en
[`../video/`](../video/).
