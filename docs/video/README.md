# Los videos y los GIF de las familias

```
cd docs/video
npm ci
npx playwright install chromium
PORTAL=<carpeta del portal> npm run grabar
```

La impresora tiene un solo dueño por parte. **La mecánica** es el componente del portal,
`components/criterio/CriterioFamily.tsx`: la hoja que se imprime y el robot que se enciende
cuando la hoja habla de él. **El texto de la hoja** de cada familia está en su
`families/criterio-<familia>/familia.json` (`impresora`), y **los robots, con sus gestos**, en
`plugins/criterio-server/scripts/robots.py`. El portal publica los dos en
`lib/criterioImpresora.ts` con `scripts/criterio-familias.mjs`. [`grabar.mjs`](grabar.mjs) trae
el componente y esa hoja, los monta en una página propia y graba (el video de YouTube, más abajo):

| Pieza | Formato | Para qué |
|---|---|---|
| [`criterio-pmo-familia-es.mp4`](criterio-pmo-familia-es.mp4) · [`criterio-pmo-familia-en.mp4`](criterio-pmo-familia-en.mp4) | Vertical 4:5, 1080×1350, H.264, con la tarjeta final de cifras | El post de LinkedIn |
| [`criterio-cfo-familia-es.mp4`](criterio-cfo-familia-es.mp4) · [`criterio-cfo-familia-en.mp4`](criterio-cfo-familia-en.mp4) | Igual, la CFO, con su tarjeta final | El post de LinkedIn de la CFO |
| [`../img/es/robots.gif`](../img/es/robots.gif) · [`../img/en/robots.gif`](../img/en/robots.gif) | Apaisado, 1120 px, la impresión completa de la PMO | El README de la familia PMO |
| [`../img/es/robots-cfo.gif`](../img/es/robots-cfo.gif) · [`../img/en/robots-cfo.gif`](../img/en/robots-cfo.gif) | Igual, la CFO | El diseño de la familia CFO |
| [`../img/es/robots-clo.gif`](../img/es/robots-clo.gif) · [`../img/en/robots-clo.gif`](../img/en/robots-clo.gif) | Igual, la CLO | El diseño de la familia CLO |
| [`../img/es/robots-ea.gif`](../img/es/robots-ea.gif) · [`../img/en/robots-ea.gif`](../img/en/robots-ea.gif) | Igual, la EA | La página de la familia EA |
| `youtube/criterio-<familia>-youtube-{es,en}.mp4` | Horizontal 16:9, 1920×1080, H.264, unos dos minutos y medio | El canal de YouTube; no se versiona (pesa decenas de megas) |

`FAMILIAS=cfo,clo` graba solo esas; `PIEZAS=youtube` solo el video de YouTube (o `video`, `gif`);
`IDIOMAS=es` solo ese idioma.

**El video de YouTube** ([`src/youtube.jsx`](src/youtube.jsx), en [`youtube.html`](youtube.html))
presenta la familia y después a cada agente, con Rostrum al final: el rol que dirige la función,
las dos cifras de terceros del costo del problema, lo que hace cada función y con qué se integra,
cada agente con lo que hace, lo que detecta y sus señales con más casos probados, Rostrum, el piso
de la prueba con sus entidades y países, y los tres pasos de la instalación. Solo los rótulos y los
tiempos se escriben ahí: los textos y las cifras son los que el portal publica del repositorio
—`nivel_c` de cada `familia.json`, las rondas, la hoja de ruta, la impresora y la instalación—, y
`grabar.mjs` trae esos archivos del portal, igual que el componente de la impresora. Se dibuja
cuadro por cuadro (30 por segundo): la página pone cada animación, también los gestos de los
robots, en el segundo exacto de cada cuadro, así que sale parejo en cualquier máquina. La PMO
todavía no tiene el suyo: el portal no publica sus agentes en una tabla como las de las demás.

Si cambia el texto de la impresora, se cambia en `familia.json`, el portal lo vuelve a publicar y se vuelve a grabar. No
se edita ni el GIF ni el video a mano, y [`graficos.py`](../img/graficos.py) no dibuja
la impresora: dos guiones de la misma escena terminan diciendo cosas distintas. (Sí dibuja la
tarjeta animada de cada agente, con los mismos gestos de `robots.py`.)

La tarjeta final de cada video lleva las cifras de la evidencia publicada: la PMO, de
[`tests/evidencias/rondas/`](../../tests/evidencias/rondas); la CFO, de
[`tests/evidencias/familias/cfo/`](../../tests/evidencias/familias/cfo) y de su material. Están en
`src/main.jsx`; si cambian, se cambian ahí.

Pide ffmpeg en el `PATH`. `CHROMIUM` apunta a otro navegador si no se usa el de
Playwright. Los cuadros intermedios quedan en `cuadros/`, que no se versiona.
