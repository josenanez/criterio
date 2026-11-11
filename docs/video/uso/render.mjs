// El video de uso: la toma montada, cuadro por cuadro. La terminal es la de la sesión real (xterm.js, con lo
// que Claude Code escribió en la toma); a la izquierda, el capítulo del guion.
//
//   PORTAL=<repo del portal> node uso/render.mjs <toma> <guion.json> <salida.mp4>
//   PORTAL=… node uso/render.mjs <toma> <guion.json> <cuadro.png> --cuadro <segundo de la toma> [intro|cierre]
//
// Los robots salen de las figuras de difusión del portal. Lo único que se quita de la toma son los avisos del
// entorno donde se grabó, no de Criterio ni de Claude Code al usarlo («ocultar» en el guion): se cambian por
// espacios del mismo ancho.
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { chromium } from 'playwright';

const [tomaDir, guionP, salida, modo, segundo, tarjetaFija] = process.argv.slice(2);
const FPS = 30, INTRO = 5, CIERRE = 7;
const AQUI = path.dirname(new URL(import.meta.url).pathname);
const g = JSON.parse(fs.readFileSync(guionP, 'utf8'));
const FIGURAS = path.resolve(process.env.PORTAL ?? '../jf-amplify-portal', 'difusion', 'criterio-2-0-0', 'figuras');
const robot = (n) => n && `file://${path.join(FIGURAS, `robot-${n}.svg`)}`;

const ANSI = '(?:\\x1b\\[[0-9;]*m)*';
const ocultar = (g.ocultar ?? []).map((s) => new RegExp([...s].map((c) => c.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join(ANSI), 'g'));
const ev = fs.readFileSync(path.join(tomaDir, 'toma.cast'), 'utf8').trim().split('\n').slice(1).map((l) => {
  const e = JSON.parse(l);
  for (const re of ocultar) e[2] = e[2].replace(re, (m) => ' '.repeat(m.replace(/\x1b\[[0-9;]*m/g, '').length));
  return e;
});
const m = modo === '--cuadro' ? null : JSON.parse(fs.readFileSync(path.join(tomaDir, 'montaje.json'), 'utf8'));

function castEn(v) {
  const A = m.anclas;
  for (let i = 0; i < A.length - 1; i++) {
    const [c0, v0] = A[i], [c1, v1] = A[i + 1];
    if (v >= v0 && v < v1) return c0 + ((v - v0) / (v1 - v0)) * (c1 - c0);
  }
  return A[A.length - 1][0];
}

const navegador = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
const pagina = await navegador.newPage({ viewport: { width: 1920, height: 1080 } });
await pagina.goto(`file://${path.join(AQUI, 'pagina.html')}`);
await pagina.evaluate(([gg, robots]) => window.__preparar(gg, robots), [g, g.intro.robots.map(robot)]);
await pagina.evaluate(() => document.fonts.ready);
const capitulo = (c) => pagina.evaluate(([x, b]) => window.__capitulo(x, b), [c, robot(c.agente)]);

if (modo === '--cuadro') {
  let d = '';
  for (const e of ev) { if (e[0] > +segundo) break; d += e[2]; }
  await pagina.evaluate((x) => window.__escribir(x), d);
  const c = [...g.capitulos].reverse().find((x) => x.desde <= +segundo) ?? g.capitulos[0];
  await capitulo(c);
  if (tarjetaFija) await pagina.evaluate((q) => window.__tarjeta(q), tarjetaFija);
  await pagina.screenshot({ path: salida });
  await navegador.close();
  process.exit(0);
}

const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '18', '-movflags', '+faststart', salida], { stdio: ['pipe', 'inherit', 'inherit'] });
const cuadro = async () => {
  const b = await pagina.screenshot({ type: 'jpeg', quality: 94 });
  if (!ff.stdin.write(b)) await new Promise((ok) => ff.stdin.once('drain', ok));
};

const total = INTRO + m.duracion + CIERRE;
let k = 0, cap = -1, tarjeta;
// La terminal arranca con lo que había en pantalla al empezar el montaje.
let inicio = '';
while (k < ev.length && ev[k][0] <= m.anclas[0][0]) inicio += ev[k++][2];
await pagina.evaluate((d) => window.__escribir(d), inicio);
for (let f = 0; f < Math.round(total * FPS); f++) {
  const T = f / FPS;
  const quiere = T < INTRO ? 'intro' : T >= INTRO + m.duracion ? 'cierre' : null;
  if (quiere !== tarjeta) { await pagina.evaluate((q) => window.__tarjeta(q), quiere); tarjeta = quiere; }
  if (!quiere) {
    const v = T - INTRO;
    const c = castEn(v);
    let datos = '';
    while (k < ev.length && ev[k][0] <= c) datos += ev[k++][2];
    if (datos) await pagina.evaluate((d) => window.__escribir(d), datos);
    let i = -1;
    m.capitulos.forEach((cc, j) => { if (cc.video <= v + 1e-6) i = j; });
    if (i !== cap && i >= 0) { cap = i; await capitulo(m.capitulos[i]); }
  }
  await cuadro();
  if (f % (FPS * 30) === 0) console.log(`${Math.round(T)} s de ${Math.round(total)}`);
}
ff.stdin.end();
await new Promise((ok) => ff.on('close', ok));
await navegador.close();
console.log(`${salida} · ${total.toFixed(1)} s`);
