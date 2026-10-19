# El video y el GIF de la familia

```
cd docs/video
npm ci
npx playwright install chromium
PORTAL=<carpeta del portal> npm run grabar
```

La animación de la impresora tiene un solo dueño: el componente del portal
`components/criterio/CriterioFamily.tsx`. Ahí vive el guion —qué dice la hoja de cada
agente— y de ahí sale todo. [`grabar.mjs`](grabar.mjs) trae el componente, lo monta en
una página propia y graba la misma animación de dos formas:

| Pieza | Formato | Para qué |
|---|---|---|
| [`criterio-pmo-familia-es.mp4`](criterio-pmo-familia-es.mp4) · [`criterio-pmo-familia-en.mp4`](criterio-pmo-familia-en.mp4) | Vertical 4:5, 1080×1350, H.264, con la tarjeta final de cifras | El post de LinkedIn |
| [`../img/es/robots.gif`](../img/es/robots.gif) · [`../img/en/robots.gif`](../img/en/robots.gif) | Apaisado, 1120 px, la impresión completa | Los README de la familia |

Si cambia el texto de la impresora, se cambia en el componente y se vuelve a grabar. No
se edita ni el GIF ni el video a mano, y [`graficos.py`](../img/graficos.py) ya no dibuja
la animación: dos guiones de la misma escena terminan diciendo cosas distintas.

La tarjeta final del video lleva las cifras de la evidencia publicada en
[`tests/evidencias/rondas/`](../../tests/evidencias/rondas). Están en `src/main.jsx`; si
cambian, se cambian ahí.

Pide ffmpeg en el `PATH`. `CHROMIUM` apunta a otro navegador si no se usa el de
Playwright. Los cuadros intermedios quedan en `cuadros/`, que no se versiona.
