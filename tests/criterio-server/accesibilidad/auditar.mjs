// Recorre un Rostrum que ya está corriendo, página por página, y dice qué no cumple.
//
//   cd tests/criterio-server/accesibilidad && npm ci
//   npm run auditar                                      # levanta la demostración y la recorre
//   BASE=http://127.0.0.1:8765 npm run auditar          # o un Rostrum que ya está corriendo
//                                                        # CAPTURAS=1 guarda una captura por vista
//
// Sale con 1 si algo falla. Lo que mide:
//   · axe-core con las reglas WCAG 2.0, 2.1 y 2.2 de nivel A y AA, y las buenas prácticas, a 1280 y 390 px
//   · enlaces rotos y errores de consola
//   · que ninguna página se salga del ancho a 1280, 768, 390 y 320 px (WCAG 1.4.10)
//   · que ninguna letra baje de 12 px y que cada página tenga un solo h1
//   · el teclado: el primer Tab es el salto al contenido, el foco se ve, el menú del teléfono se abre
//   · que los robots se paren solos antes de cinco segundos (WCAG 2.2.2) y que el formulario no se
//     envíe sin texto
//   · el HTML de cada página contra el validador del W3C (Nu Html Checker, `vnu-jar`, pide Java)
// El navegador es el de Playwright; CHROMIUM apunta a otro.
import { chromium } from 'playwright';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync, spawn } from 'node:child_process';
import vnuJar from 'vnu-jar';

// Sin BASE, la demostración del plugin: seis familias sobre material sintético, en una carpeta temporal.
let servidor = null;
let BASE = process.env.BASE;
if (!BASE) {
  const repo = new URL('../../../', import.meta.url).pathname;
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'rostrum-demo-'));
  execFileSync('python3', ['-c', 'import sys,zipfile;zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])',
    path.join(repo, 'plugins/criterio-server/demo/criterio-demo.zip'), tmp]);
  const puerto = String(18765 + Math.floor(Math.random() * 1000));
  servidor = spawn('python3', [path.join(repo, 'plugins/criterio-server/scripts/servidor.py'), '--mapa',
    path.join(tmp, 'criterio-demo/.criterio/rostrum/config.json'), '--puerto', puerto], { stdio: 'ignore' });
  BASE = `http://127.0.0.1:${puerto}`;
  for (let i = 0; i < 50; i++) {
    if (await fetch(BASE + '/estado.json').then((r) => r.ok, () => false)) break;
    await new Promise((ok) => setTimeout(ok, 200));
  }
}
const salir = (codigo) => { if (servidor) servidor.kill(); process.exit(codigo); };
const AXE = fs.readFileSync(new URL('./node_modules/axe-core/axe.min.js', import.meta.url), 'utf8');
// Antes de abrir el navegador: que haya un Rostrum escuchando. Si no, se dice en una línea.
try {
  const r = await fetch(BASE + '/estado.json');
  if (!r.ok) throw new Error(`respondió ${r.status}`);
} catch (e) {
  console.error(`No hay un Rostrum respondiendo en ${BASE} (${e.cause?.code || e.message}).`);
  console.error('Levántalo en otra ventana de la terminal y déjalo corriendo mientras se audita:');
  console.error('  python3 <repo>/plugins/criterio-server/scripts/servidor.py --mapa .criterio/rostrum/config.json');
  salir(2);
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
// 4 · el HTML de cada página, tal como lo sirve Rostrum, contra el validador del W3C
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'rostrum-w3c-'));
const archivo = new Map();
for (const [i, u] of paginas.entries()) {
  const f = path.join(dir, `${i}.html`); archivo.set(f, u);
  fs.writeFileSync(f, await (await fetch(BASE + u)).text());
}
let w3c;
try {
  w3c = execFileSync('java', ['-jar', vnuJar, '--format', 'json', '--stdout', '--exit-zero-always', ...archivo.keys()],
    { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], maxBuffer: 64 * 1024 * 1024 });
} catch (e) {
  // Sin Java no hay validación, y eso se dice como falla: no se da por bueno lo que no se revisó.
  w3c = '';
  fallas.push(`el validador del W3C no corrió: ${e.message.split('\n')[0]} (¿hay Java?)`);
}
const salida = (w3c.trim().startsWith('{') ? w3c : '') || '';
for (const m of salida ? JSON.parse(salida).messages : []) {
  if (m.type !== 'error') continue;
  const u = archivo.get(decodeURI(new URL(m.url).pathname)) || m.url;
  fallas.push(`${u} · W3C: ${m.message}${m.lastLine ? ` (línea ${m.lastLine})` : ''}`);
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
console.log(`${paginas.length} páginas, a 1280, 768, 390 y 320 px, y su HTML contra el validador del W3C`);
for (const f of fallas) console.log(`  ✗ ${f}`);
console.log(fallas.length ? `${fallas.length} fallas` : 'todo cumple');
salir(fallas.length ? 1 : 0);
