// Rostrum en dos pantallas: un teléfono (390 px) y un escritorio (1280 px).
// Recibe la base del servidor y un JSON con las rutas; devuelve, por ancho, las rutas
// cuya página se sale de la pantalla: la página entera más ancha que la ventana, o un
// elemento que la rebasa sin una caja que lo deje desplazarse dentro de ella.
// Lo llama `ronda.py` si encuentra Playwright (PLAYWRIGHT_NODE_PATH o el `require` normal);
// sin él, la prueba de Rostrum lo dice y no inventa el resultado.
import fs from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const [base, archivo] = process.argv.slice(2);
const rutas = JSON.parse(fs.readFileSync(archivo, 'utf8'));
const navegador = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const fuera = {};
for (const ancho of [390, 1280]) {
    const pagina = await navegador.newPage({ viewport: { width: ancho, height: 900 } });
    fuera[ancho] = [];
    for (const ruta of rutas) {
        await pagina.goto(base + ruta, { waitUntil: 'load' });
        const sale = await pagina.evaluate(() => {
            const W = document.documentElement.clientWidth;
            if (document.documentElement.scrollWidth > W + 1) return true;
            return [...document.querySelectorAll('body *')].some((e) => {
                const r = e.getBoundingClientRect();
                if (r.width === 0 || r.right <= W + 1) return false;
                for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) {
                    if (['auto', 'scroll', 'hidden'].includes(getComputedStyle(a).overflowX)) return false;
                }
                return true;
            });
        });
        if (sale) fuera[ancho].push(ruta);
    }
    await pagina.close();
}
await navegador.close();
console.log(JSON.stringify(fuera));
