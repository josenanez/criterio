# El video y los GIF de las familias

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
el componente y esa hoja, los monta en una página propia y graba:

| Pieza | Formato | Para qué |
|---|---|---|
| [`criterio-pmo-familia-es.mp4`](criterio-pmo-familia-es.mp4) · [`criterio-pmo-familia-en.mp4`](criterio-pmo-familia-en.mp4) | Vertical 4:5, 1080×1350, H.264, con la tarjeta final de cifras | El post de LinkedIn |
| [`../img/es/robots.gif`](../img/es/robots.gif) · [`../img/en/robots.gif`](../img/en/robots.gif) | Apaisado, 1120 px, la impresión completa de la PMO | El README de la familia PMO |
| [`../img/es/robots-cfo.gif`](../img/es/robots-cfo.gif) · [`../img/en/robots-cfo.gif`](../img/en/robots-cfo.gif) | Igual, la CFO | El diseño de la familia CFO |
| [`../img/es/robots-clo.gif`](../img/es/robots-clo.gif) · [`../img/en/robots-clo.gif`](../img/en/robots-clo.gif) | Igual, la CLO | El diseño de la familia CLO |
| [`../img/es/robots-ea.gif`](../img/es/robots-ea.gif) · [`../img/en/robots-ea.gif`](../img/en/robots-ea.gif) | Igual, la EA | La página de la familia EA |

`FAMILIAS=cfo,clo` graba solo esas.

Si cambia el texto de la impresora, se cambia en `familia.json`, el portal lo vuelve a publicar y se vuelve a grabar. No
se edita ni el GIF ni el video a mano, y [`graficos.py`](../img/graficos.py) no dibuja
la impresora: dos guiones de la misma escena terminan diciendo cosas distintas. (Sí dibuja la
tarjeta animada de cada agente, con los mismos gestos de `robots.py`.)

La tarjeta final del video lleva las cifras de la evidencia publicada en
[`tests/evidencias/rondas/`](../../tests/evidencias/rondas). Están en `src/main.jsx`; si
cambian, se cambian ahí.

Pide ffmpeg en el `PATH`. `CHROMIUM` apunta a otro navegador si no se usa el de
Playwright. Los cuadros intermedios quedan en `cuadros/`, que no se versiona.
