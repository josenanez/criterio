// Graba la impresora de cada familia desde el componente del portal, que es el dueño de la
// animación: components/criterio/CriterioFamily.tsx, con la hoja que el portal publica en
// lib/criterioImpresora.ts desde families/*/familia.json. Nada se copia a mano. Salen:
//
//   docs/video/criterio-pmo-familia-{es,en}.mp4   vertical 4:5, 1080×1350, para LinkedIn
//   docs/img/{es,en}/robots.gif                   la PMO, apaisado, 1120 px, para los README
//   docs/img/{es,en}/robots-{cfo,clo}.gif          la CFO y la CLO, igual
//
// Uso (desde docs/video):  npm ci && PORTAL=<carpeta del portal> npm run grabar
// Pide ffmpeg en el PATH. El navegador es el de Playwright (npx playwright install chromium);
// CHROMIUM apunta a otro ejecutable si se quiere.

import { createServer } from 'vite';
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '..', '..');

if (!process.env.PORTAL) {
  console.error('Falta PORTAL: la carpeta del portal, donde está components/criterio/CriterioFamily.tsx');
  process.exit(1);
}
const componente = path.resolve(process.env.PORTAL, 'components', 'criterio', 'CriterioFamily.tsx');
const hoja = path.resolve(process.env.PORTAL, 'lib', 'criterioImpresora.ts');
for (const f of [componente, hoja]) {
  if (!fs.existsSync(f)) {
    console.error(`No está ${f}; en el portal, node scripts/criterio-familias.mjs`);
    process.exit(1);
  }
}
fs.copyFileSync(componente, path.join(AQUI, 'src', 'CriterioFamily.tsx'));
fs.mkdirSync(path.join(AQUI, 'src', 'lib'), { recursive: true });
fs.copyFileSync(hoja, path.join(AQUI, 'src', 'lib', 'criterioImpresora.ts'));
if (spawnSync('ffmpeg', ['-version']).status !== 0) {
  console.error('Falta ffmpeg en el PATH');
  process.exit(1);
}

// El video se dibuja a 783 px de ancho y se amplía 1,38: así el texto se lee en un
// teléfono y el componente cae en su diseño de dos columnas. El GIF va sin subtítulo
// ni encabezado, solo el piso y la hoja: el README ya tiene su propio título.
// El video es solo de la PMO: su tarjeta final lleva las cifras de sus rondas. Las familias
// CFO y CLO salen en GIF. FAMILIAS=cfo,clo graba solo esas.
const FAMILIAS = (process.env.FAMILIAS || 'pmo,cfo,clo').split(',');
const TOMAS = [
  { familia: 'pmo', idioma: 'es', tipo: 'video', ancho: 1080, alto: 1350, zoom: 1.38 },
  { familia: 'pmo', idioma: 'en', tipo: 'video', ancho: 1080, alto: 1350, zoom: 1.38 },
  ...['pmo', 'cfo', 'clo'].flatMap((familia) => ['es', 'en'].map((idioma) =>
    ({ familia, idioma, tipo: 'gif', ancho: 1280, alto: 568, zoom: 1 }))),
].filter((t) => FAMILIAS.includes(t.familia));
const FIN = /FIN DE LA IMPRESIÓN|END OF PRINTOUT/;

function ffmpeg(args) {
  const r = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', ...args], { stdio: 'inherit' });
  if (r.status !== 0) throw new Error(`ffmpeg terminó con ${r.status}`);
}

// Cada cuadro dura lo que tardó en llegar el siguiente: el screencast no entrega a ritmo
// fijo, y repartirlo parejo aceleraría o frenaría la impresión.
function lista(carpeta, tiempos, ultimo) {
  const lineas = tiempos.map((t, i) => {
    const dura = i + 1 < tiempos.length ? tiempos[i + 1] - t : ultimo;
    return `file '${String(i).padStart(5, '0')}.jpg'\nduration ${Math.max(dura, 0.001).toFixed(4)}`;
  });
  lineas.push(`file '${String(tiempos.length - 1).padStart(5, '0')}.jpg'`);
  const ruta = path.join(carpeta, 'lista.txt');
  fs.writeFileSync(ruta, lineas.join('\n') + '\n');
  return ruta;
}

async function grabar(navegador, url, toma) {
  const carpeta = path.join(AQUI, 'cuadros', `${toma.familia}-${toma.tipo}-${toma.idioma}`);
  fs.rmSync(carpeta, { recursive: true, force: true });
  fs.mkdirSync(carpeta, { recursive: true });
  const pagina = await navegador.newPage({ viewport: { width: toma.ancho, height: toma.alto } });

  // La animación arranca cuando el componente entra en pantalla. Aquí arranca cuando el
  // escenario está listo, para que el primer cuadro no la encuentre a medias.
  await pagina.addInitScript(() => {
    window.__espera = true;
    window.IntersectionObserver = class {
      constructor(cb) { this.cb = cb; }
      observe(el) {
        const t = setInterval(() => {
          if (!window.__espera) { clearInterval(t); this.cb([{ isIntersecting: true, target: el }]); }
        }, 20);
      }
      disconnect() {}
      unobserve() {}
    };
  });
  await pagina.goto(`${url}?l=${toma.idioma}&f=${toma.familia}`, { waitUntil: 'networkidle' });
  await pagina.evaluate(({ tipo, zoom }) => {
    const s = document.querySelector('section');
    s.querySelectorAll('button').forEach((b) => b.parentElement && b.parentElement.remove());
    const nota = [...s.querySelectorAll('p')].find((p) => /Estado de la familia|Where the family stands/.test(p.textContent));
    if (nota) nota.remove();
    const cuerpo = s.querySelector('.max-w-6xl');
    if (tipo === 'video') {
      document.body.classList.add('video');
      document.documentElement.style.zoom = String(zoom);
      const marco = document.getElementById('frame');
      marco.style.minHeight = `${window.innerHeight / zoom}px`;
      marco.style.alignItems = 'flex-start';
      cuerpo.children[2].style.display = 'none';   // el subtítulo: lo dice el texto del post
    } else {
      [...cuerpo.children].slice(0, 3).forEach((x) => x.remove());   // antetítulo, título y subtítulo
      cuerpo.firstElementChild.style.marginTop = '0';
      s.style.paddingTop = '24px';
      s.style.paddingBottom = '24px';
    }
  }, toma);
  await pagina.evaluate(() => document.fonts.ready);

  const cdp = await pagina.context().newCDPSession(pagina);
  const tiempos = [];
  cdp.on('Page.screencastFrame', (f) => {
    fs.writeFileSync(path.join(carpeta, `${String(tiempos.length).padStart(5, '0')}.jpg`), Buffer.from(f.data, 'base64'));
    tiempos.push(f.metadata.timestamp);
    cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(() => {});
  });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 95, maxWidth: toma.ancho, maxHeight: toma.alto, everyNthFrame: 1 });
  await pagina.waitForTimeout(1200);
  await pagina.evaluate(() => { window.__espera = false; });
  await pagina.waitForFunction((fin) => new RegExp(fin).test(document.body.innerText), FIN.source, { timeout: 300000, polling: 200 });
  await pagina.waitForTimeout(2500);
  if (toma.tipo === 'video') {
    await pagina.evaluate(() => document.getElementById('end').classList.add('on'));
    await pagina.waitForTimeout(6000);
  }
  await cdp.send('Page.stopScreencast');
  await pagina.close();
  return { carpeta, tiempos };
}

function video(toma, { carpeta, tiempos }) {
  const salida = path.join(AQUI, `criterio-pmo-familia-${toma.idioma}.mp4`);
  ffmpeg(['-f', 'concat', '-safe', '0', '-i', lista(carpeta, tiempos, 0.5),
    '-vf', 'fps=30,crop=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-movflags', '+faststart', salida]);
  return salida;
}

// Una paleta para todo el GIF, sin tramado, y solo se reescribe lo que cambia: así pesa
// lo que se mueve y no la escena entera. El último cuadro, la impresión completa, se
// queda cuatro segundos antes de volver a empezar.
function gif(toma, { carpeta, tiempos }) {
  const salida = path.join(RAIZ, 'docs', 'img', toma.idioma, toma.familia === 'pmo' ? 'robots.gif' : `robots-${toma.familia}.gif`);
  const filtro = 'fps=8,scale=1120:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle';
  ffmpeg(['-f', 'concat', '-safe', '0', '-i', lista(carpeta, tiempos, 4.0), '-vf', filtro, '-loop', '0', salida]);
  return salida;
}

const servidor = await createServer({ root: AQUI, configFile: path.join(AQUI, 'vite.config.js'), server: { port: 0, strictPort: false } });
await servidor.listen();
const url = servidor.resolvedUrls.local[0];
const navegador = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
try {
  for (const toma of TOMAS) {
    const cuadros = await grabar(navegador, url, toma);
    const salida = toma.tipo === 'video' ? video(toma, cuadros) : gif(toma, cuadros);
    const seg = (cuadros.tiempos.at(-1) - cuadros.tiempos[0]).toFixed(1);
    console.log(`${path.relative(RAIZ, salida)}  ${cuadros.tiempos.length} cuadros, ${seg} s, ${Math.round(fs.statSync(salida).size / 1024)} KB`);
  }
} finally {
  await navegador.close();
  await servidor.close();
}
