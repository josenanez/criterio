// Recorre un Rostrum que ya está corriendo, página por página, y dice qué no cumple.
//
//   cd tests/criterio-server/accesibilidad && npm ci
//   BASE=http://127.0.0.1:8765 npm run auditar          # CAPTURAS=1 guarda una captura por vista
//
// Sale con 1 si algo falla. Lo que mide:
//   · axe-core con las reglas WCAG 2.0, 2.1 y 2.2 de nivel A y AA, y las buenas prácticas, a 1280 y 390 px
//   · enlaces rotos y errores de consola
//   · que ninguna página se salga del ancho a 1280, 768, 390 y 320 px (WCAG 1.4.10)
//   · que ninguna letra baje de 12 px y que cada página tenga un solo h1
//   · el teclado: el primer Tab es el salto al contenido, el foco se ve, el menú del teléfono se abre
//   · que los robots se paren solos antes de cinco segundos (WCAG 2.2.2) y que el formulario no se
//     envíe sin texto
// El navegador es el de Playwright; CHROMIUM apunta a otro.
import { chromium } from 'playwright';
import fs from 'node:fs';

const BASE = process.env.BASE || 'http://127.0.0.1:8765';
const AXE = fs.readFileSync(new URL('./node_modules/axe-core/axe.min.js', import.meta.url), 'utf8');
// Antes de abrir el navegador: que haya un Rostrum escuchando. Si no, se dice en una línea.
try {
  const r = await fetch(BASE + '/estado.json');
  if (!r.ok) throw new Error(`respondió ${r.status}`);
} catch (e) {
  console.error(`No hay un Rostrum respondiendo en ${BASE} (${e.cause?.code || e.message}).`);
  console.error('Levántalo en otra ventana de la terminal y déjalo corriendo mientras se audita:');
  console.error('  python3 <repo>/plugins/criterio-server/scripts/servidor.py --mapa .criterio/rostrum/config.json');
  process.exit(2);
}
const b = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
const fallas = [];
p.on('pageerror', (e) => fallas.push(`error de página en ${p.url()}: ${e.message}`));
p.on('console', (m) => { if (m.type() === 'error') fallas.push(`consola en ${p.url()}: ${m.text()}`); });

// 1 · todas las páginas enlazadas desde la portada
const vistas = new Map(); const cola = ['/'];
while (cola.length && vistas.size < 500) {
  const u = cola.shift(); if (vistas.has(u)) continue;
  const r = await p.goto(BASE + u, { waitUntil: 'load' }).catch(() => null);
  const st = r ? r.status() : 0; vistas.set(u, st);
  if (st !== 200) { fallas.push(`enlace roto: ${u} (${st})`); continue; }
  if (!(r.headers()['content-type'] || '').includes('html')) continue;
  for (const h of await p.$$eval('a[href]', (as) => as.map((a) => a.getAttribute('href')))) {
    if (!h || h.startsWith('#') || /^(mailto:|https?:)/.test(h)) continue;
    const abs = new URL(h, p.url()); if (abs.origin !== new URL(BASE).origin) continue;
    const k = abs.pathname + abs.search; if (!vistas.has(k) && !cola.includes(k)) cola.push(k);
  }
}
const paginas = [...vistas].filter(([u, s]) => s === 200 && !u.endsWith('.json')).map(([u]) => u);

// 2 · cada página a cuatro anchos
for (const ancho of [1280, 768, 390, 320]) {
  await p.setViewportSize({ width: ancho, height: 900 });
  for (const u of paginas) {
    await p.goto(BASE + u, { waitUntil: 'load' });
    const m = await p.evaluate(() => {
      const d = document.documentElement; let min = 99;
      const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      while (w.nextNode()) {
        const el = w.currentNode.parentElement; if (!w.currentNode.textContent.trim() || el.closest('svg,.saltar')) continue;
        const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
        min = Math.min(min, parseFloat(cs.fontSize));
      }
      return { desborde: d.scrollWidth - d.clientWidth, min, h1: document.querySelectorAll('h1').length };
    });
    if (m.desborde > 0) fallas.push(`${u} a ${ancho} px se sale ${m.desborde} px del ancho`);
    if (m.min < 12) fallas.push(`${u} a ${ancho} px tiene letra de ${m.min} px`);
    if (m.h1 !== 1) fallas.push(`${u} tiene ${m.h1} h1`);
    if (ancho === 1280 || ancho === 390) {
      await p.addScriptTag({ content: AXE });
      const v = await p.evaluate(async () => (await axe.run(document, { runOnly: { type: 'tag',
        values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] } })).violations
        .map((x) => `${x.id} (${x.impact}): ${x.nodes.slice(0, 2).map((n) => n.target.join(' ')).join(' · ')}`));
      for (const x of v) fallas.push(`${u} a ${ancho} px · ${x}`);
    }
    if (process.env.CAPTURAS && (ancho === 1280 || ancho === 390)) {
      fs.mkdirSync(new URL('./capturas/', import.meta.url), { recursive: true });
      await p.screenshot({ path: new URL(`./capturas/${ancho}-${(u.replace(/[^a-z0-9]+/gi, '_') || 'portada').slice(0, 70)}.png`, import.meta.url).pathname, fullPage: true });
    }
  }
}

// 3 · lo que no se ve en una captura
await p.setViewportSize({ width: 1280, height: 900 });
await p.goto(BASE + (paginas.find((u) => u !== '/') || '/')); await p.keyboard.press('Tab');
if ((await p.evaluate(() => document.activeElement.className)) !== 'saltar') fallas.push('el primer Tab no es el salto al contenido');
await p.keyboard.press('Enter');
if ((await p.evaluate(() => document.activeElement.id)) !== 'contenido') fallas.push('el salto no lleva al contenido');
await p.keyboard.press('Tab');
if ((await p.evaluate(() => getComputedStyle(document.activeElement).outlineStyle)) === 'none') fallas.push('el foco no se ve');
await p.goto(BASE + '/'); await p.waitForTimeout(5300);
const vivas = await p.evaluate(() => document.getAnimations().filter((a) => a.playState === 'running').length);
if (vivas) fallas.push(`${vivas} animaciones siguen solas después de cinco segundos`);
if (await p.$('form.pide')) {
  await p.click('form.pide button[type=submit]');
  if (new URL(p.url()).pathname !== '/') fallas.push('el formulario se envía sin texto');
}
const t = await b.newPage({ viewport: { width: 390, height: 800 } });
await t.goto(BASE + '/');
let alcanzado = false;
for (let i = 0; i < 4 && !alcanzado; i++) {   // el salto al contenido y la marca van antes
  await t.keyboard.press('Tab');
  alcanzado = (await t.evaluate(() => document.activeElement.className)) === 'menu-caja';
}
if (!alcanzado) fallas.push('el menú del teléfono no se alcanza con el teclado en los primeros cuatro Tab');
await t.keyboard.press('Space');
if ((await t.evaluate(() => getComputedStyle(document.querySelector('.arbol')).display)) === 'none') fallas.push('el menú del teléfono no se abre con el teclado');

await b.close();
console.log(`${paginas.length} páginas, a 1280, 768, 390 y 320 px`);
for (const f of fallas) console.log(`  ✗ ${f}`);
console.log(fallas.length ? `${fallas.length} fallas` : 'todo cumple');
process.exit(fallas.length ? 1 : 0);
