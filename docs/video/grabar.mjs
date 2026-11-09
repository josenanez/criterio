// Graba la impresora de cada familia desde el componente del portal, que es el dueño de la
// animación: components/criterio/CriterioFamily.tsx, con la hoja que el portal publica en
// lib/criterioImpresora.ts desde families/*/familia.json. Y el video de cada familia para YouTube
// (src/youtube.jsx), con lo que el portal publica de ella. Nada se copia a mano. Salen:
//
//   docs/video/criterio-{pmo,cfo}-familia-{es,en}.mp4   vertical 4:5, 1080×1350, para LinkedIn
//   docs/img/{es,en}/robots.gif                   la PMO, apaisado, 1120 px, para los README
//   docs/img/{es,en}/robots-{cfo,clo,ea}.gif       la CFO, la CLO y la EA, igual
//   docs/video/youtube/criterio-<familia>-youtube-{es,en}.mp4   1920×1080, para YouTube (no se versiona)
//   docs/video/youtube/criterio-youtube-{es,en}.mp4               el de Criterio completo (src/criterio.jsx), igual
//
// Uso (desde docs/video):  npm ci && PORTAL=<carpeta del portal> npm run grabar
// FAMILIAS=cfo,clo graba solo esas (y `criterio`, el video de Criterio); PIEZAS=youtube (o video, gif,
// criterio) solo esas piezas; IDIOMAS=es solo ese. El video de Criterio cita las descargas: las lee de
// la rama `descargas` del repositorio, o del CSV que diga DESCARGAS, con scripts/descargas.py.
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
// Lo que se trae del portal: los componentes que se dibujan tal cual y las tablas que el portal
// genera del repositorio. Van a src/portal y src/lib, que no se versionan.
const TRAER = {
  portal: [...['CriterioFamily.tsx', 'CriterioLogo.tsx', 'criterioPrueba.ts', 'criterioSetupFamilias.ts', 'criterioAgentTabsFamilias.ts', 'criterioCalculatorFamilias.ts']
    .map((f) => path.join('components', 'criterio', f)),
  ...['agentsMapa.ts', 'agentsTextos.ts'].map((f) => path.join('components', 'agents', f))],
  lib: ['criterioImpresora', 'criterioNivelC', 'criterioRondas', 'criterioHojaDeRuta', 'criterioIndustrias', 'criterioRegistro',
    'criterioPaises', 'criterioSectores', 'criterioMapaGeo', 'criterioCfo', 'criterioClo', 'criterioEa', 'criterioCco', 'criterioCiso'].map((f) => path.join('lib', `${f}.ts`)),
};
for (const [destino, archivos] of Object.entries(TRAER)) {
  fs.mkdirSync(path.join(AQUI, 'src', destino), { recursive: true });
  for (const f of archivos) {
    const origen = path.resolve(process.env.PORTAL, f);
    if (!fs.existsSync(origen)) {
      console.error(`No está ${origen}; en el portal, node scripts/criterio-familias.mjs`);
      process.exit(1);
    }
    fs.copyFileSync(origen, path.join(AQUI, 'src', destino, path.basename(f)));
  }
}
if (spawnSync('ffmpeg', ['-version']).status !== 0) {
  console.error('Falta ffmpeg en el PATH');
  process.exit(1);
}

// El video se dibuja a 783 px de ancho y se amplía 1,38: así el texto se lee en un
// teléfono y el componente cae en su diseño de dos columnas. El GIF va sin subtítulo
// ni encabezado, solo el piso y la hoja: el README ya tiene su propio título.
// El video es de la PMO y de la CFO: su tarjeta final lleva las cifras de sus rondas. Las familias
// CFO, CLO y EA salen en GIF. FAMILIAS=cfo,clo graba solo esas.
const FAMILIAS = (process.env.FAMILIAS || 'pmo,cfo,clo,ea,cco,ciso,criterio').split(',');
const PIEZAS = (process.env.PIEZAS || 'video,gif,youtube,criterio').split(',');
const IDIOMAS = (process.env.IDIOMAS || 'es,en').split(',');
// Las familias con video, cada una con su tarjeta final en src/main.jsx.
const VIDEOS = ['pmo', 'cfo'];
// Las familias con video de YouTube: las que el portal publica con sus agentes (lib/criterio<Sigla>.ts).
const YOUTUBE = ['cfo', 'clo', 'ea', 'cco', 'ciso'];
const TOMAS = [
  ...VIDEOS.flatMap((familia) => IDIOMAS.map((idioma) =>
    ({ familia, idioma, tipo: 'video', ancho: 1080, alto: 1350, zoom: 1.38 }))),
  ...['pmo', 'cfo', 'clo', 'ea'].flatMap((familia) => IDIOMAS.map((idioma) =>
    ({ familia, idioma, tipo: 'gif', ancho: 1280, alto: 568, zoom: 1 }))),
  ...YOUTUBE.flatMap((familia) => IDIOMAS.map((idioma) =>
    ({ familia, idioma, tipo: 'youtube', pagina: 'youtube.html', ancho: 1920, alto: 1080 }))),
  ...IDIOMAS.map((idioma) => ({ familia: 'criterio', idioma, tipo: 'criterio', pagina: 'criterio.html', ancho: 1920, alto: 1080 })),
].filter((t) => FAMILIAS.includes(t.familia) && PIEZAS.includes(t.tipo));

// Las descargas que cita el video de Criterio, con la regla de scripts/descargas.py: el CSV de la rama
// `descargas` del repositorio (la llena el flujo diario), o el que diga DESCARGAS. Sin él, no se graba.
if (TOMAS.some((t) => t.tipo === 'criterio')) {
  let csv = process.env.DESCARGAS;
  if (!csv) {
    for (const ref of ['origin/descargas', 'descargas']) {
      const r = spawnSync('git', ['-C', RAIZ, 'show', `${ref}:descargas.csv`], { encoding: 'utf8' });
      if (r.status === 0) {
        csv = path.join(AQUI, 'src', 'lib', 'descargas.csv');
        fs.writeFileSync(csv, r.stdout);
        break;
      }
    }
  }
  const r = csv ? spawnSync('python3', [path.join(RAIZ, 'scripts', 'descargas.py'), 'resumen', '--csv', csv], { encoding: 'utf8' }) : null;
  if (!r || r.status !== 0) {
    console.error('El video de Criterio cita las descargas: falta la rama `descargas` (git fetch origin descargas) o DESCARGAS=<csv>');
    process.exit(1);
  }
  fs.writeFileSync(path.join(AQUI, 'src', 'lib', 'descargas.json'), r.stdout);
}
const CUADROS = 30;
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
  const salida = path.join(AQUI, `criterio-${toma.familia}-familia-${toma.idioma}.mp4`);
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

// El video de YouTube se dibuja cuadro por cuadro: la página pone cada animación en el segundo exacto
// (window.__ir) y se toma la foto. Sale parejo aunque la máquina sea lenta.
async function youtube(navegador, url, toma) {
  const nombre = toma.familia === 'criterio' ? 'criterio-youtube' : `criterio-${toma.familia}-youtube`;
  const carpeta = path.join(AQUI, 'cuadros', `${nombre}-${toma.idioma}`);
  fs.rmSync(carpeta, { recursive: true, force: true });
  fs.mkdirSync(carpeta, { recursive: true });
  const pagina = await navegador.newPage({ viewport: { width: toma.ancho, height: toma.alto } });
  await pagina.goto(`${url}${toma.pagina}?l=${toma.idioma}&f=${toma.familia}`, { waitUntil: 'networkidle' });
  await pagina.evaluate(() => document.fonts.ready);
  const total = await pagina.evaluate(() => window.__duracion);
  const n = Math.round(total * CUADROS);
  for (let i = 0; i < n; i++) {
    await pagina.evaluate((s) => window.__ir(s), i / CUADROS);
    await pagina.screenshot({ path: path.join(carpeta, `${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
  }
  await pagina.close();
  fs.mkdirSync(path.join(AQUI, 'youtube'), { recursive: true });
  const salida = path.join(AQUI, 'youtube', `${nombre}-${toma.idioma}.mp4`);
  ffmpeg(['-framerate', String(CUADROS), '-i', path.join(carpeta, '%05d.jpg'),
    '-vf', 'format=yuv420p', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-movflags', '+faststart', salida]);
  return { salida, cuadros: n, segundos: total };
}

// Sin recarga ni vigilancia de archivos: una grabación que corre al lado copia de nuevo src/portal y
// src/lib, y una recarga a mitad de un video lo rompe.
const servidor = await createServer({ root: AQUI, configFile: path.join(AQUI, 'vite.config.js'), server: { port: 0, strictPort: false, hmr: false, watch: null } });
await servidor.listen();
const url = servidor.resolvedUrls.local[0];
const navegador = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
try {
  for (const toma of TOMAS) {
    if (toma.tipo === 'youtube' || toma.tipo === 'criterio') {
      const r = await youtube(navegador, url, toma);
      console.log(`${path.relative(RAIZ, r.salida)}  ${r.cuadros} cuadros, ${r.segundos} s, ${Math.round(fs.statSync(r.salida).size / 1024)} KB`);
      continue;
    }
    const cuadros = await grabar(navegador, url, toma);
    const salida = toma.tipo === 'video' ? video(toma, cuadros) : gif(toma, cuadros);
    const seg = (cuadros.tiempos.at(-1) - cuadros.tiempos[0]).toFixed(1);
    console.log(`${path.relative(RAIZ, salida)}  ${cuadros.tiempos.length} cuadros, ${seg} s, ${Math.round(fs.statSync(salida).size / 1024)} KB`);
  }
} finally {
  await navegador.close();
  await servidor.close();
}
