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
| `youtube/criterio-<familia>-youtube-{es,en}.mp4` | Horizontal 16:9, 1920×1080, H.264, unos noventa segundos | El canal de YouTube; no se versiona (pesa decenas de megas) |
| `youtube/criterio-youtube-{es,en}.mp4` | Igual, el de Criterio completo | El canal de YouTube; no se versiona |
| `linkedin/criterio-hoja-es.mp4` | Vertical 4:5, 1080×1350, H.264, poco más de un minuto | La hoja para la dirección, animada, para el post de LinkedIn; no se versiona |

`FAMILIAS=cfo,clo` graba solo esas (`criterio`, el de Criterio); `PIEZAS=youtube` solo el video de YouTube de cada familia (o `video`, `gif`, `criterio`, `hoja`);
`IDIOMAS=es` solo ese idioma.

**El video de YouTube** ([`src/youtube.jsx`](src/youtube.jsx), en [`youtube.html`](youtube.html))
dura unos noventa segundos, una idea por pantalla, en el orden de la página de la familia: un
hallazgo de los datos de prueba que se escribe solo; el rol, lo que hace cada función y con qué se
integra; dónde se probó —el mapa que se enciende país por país, con sus industrias—; los agentes;
las tareas que hoy hace el equipo y que los agentes preparan; la evidencia —el piso, lo que detecta
cada función, los controles y los defectos—; cada agente escribiendo lo que encontró; Rostrum; y los
tres pasos de la instalación, sin la versión, que cambia con cada liberación. Solo los rótulos, los tiempos y qué agente abre se
escriben ahí: los textos y las cifras son los que el portal publica del repositorio —`nivel_c` de
cada `familia.json`, las rondas, la hoja de ruta, la impresora, los países, las industrias, el
mapa, la calculadora, las capturas de Rostrum de cada agente y la instalación—, y `grabar.mjs`
trae esos archivos del portal, igual que el componente de la impresora. Se dibuja cuadro por cuadro
(30 por segundo): la página pone cada animación, también los gestos de los robots, en el segundo
exacto de cada cuadro, así que sale parejo en cualquier máquina. La PMO todavía no tiene el suyo:
el portal no publica sus agentes en una tabla como las de las demás.

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

**La hoja animada** ([`src/hoja.jsx`](src/hoja.jsx), en [`hoja.html`](hoja.html)) cuenta lo mismo que la
hoja para la dirección del portal y en su orden: el título; cada área con su robot, lo que hacen sus
agentes en la operación, en la gerencia y lo que le llevan al nivel C, y lo que encontraron en las
pruebas; los países y las industrias, que se cuentan y se nombran; los estándares; la efectividad mínima
y las descargas diarias; y la invitación. Sus textos salen del mismo JSON que escribe la hoja
(`difusion/criterio-2-7-0/una-pagina.json` del portal, que grabar.mjs trae); los países, las industrias,
el mapa, los pisos y las descargas, de sus dueños. Si alguna familia queda por debajo del umbral de
estable, el video no se graba. Va en español: `PIEZAS=hoja FAMILIAS=criterio IDIOMAS=es`.

**El video de Criterio** ([`src/criterio.jsx`](src/criterio.jsx), en [`criterio.html`](criterio.html))
sigue la página de agentes: qué es, la pirámide de hoy y la de ahora, las familias que corren hoy,
dónde se probó, las descargas, la evidencia de cada familia, cómo se despliega, hacia dónde va —el
mapa de la empresa por capas— y la invitación a instalar. Las descargas son solo el promedio diario
desde el lanzamiento: un total o una fecha envejecen al día siguiente. Las calcula
`scripts/descargas.py resumen` sobre la rama `descargas` (o el CSV de `DESCARGAS`); sin ellas, el
video no se graba. Tampoco lleva versión, cuántas familias faltan ni cuáles siguen: la versión cambia
con cada liberación, y el mapa es dirección, no un número cerrado ni un orden comprometido. Los textos que comparte con la página
(el titular, la pirámide y las etapas) están en `components/agents/agentsTextos.ts` del portal. El
reloj de los dos videos está en [`src/tiempo.jsx`](src/tiempo.jsx).
