import React from 'react';
import './youtube.css';
import { Eyebrow, avance, montar, sube } from './tiempo';
import { CRITERIO_NIVEL_C } from './lib/criterioNivelC';
import { ROBOTS, ROSTRUM } from './lib/criterioImpresora';
import { CRITERIO_PAISES } from './lib/criterioPaises';
import { CRITERIO_MAPA_GEO } from './lib/criterioMapaGeo';
import DESCARGAS from './lib/descargas.json';
import { MAPA, PAISES_PROBADOS, SECTORES_PROBADOS, AGENTES_QUE_CORREN, VIVAS, corre, ordenDe } from './portal/agentsMapa';
import { TITULAR, LABORATORIO, DESPLIEGUE } from './portal/agentsTextos';
import { pisoDe } from './portal/criterioPrueba';
import { SETUP_FAMILIAS } from './portal/criterioSetupFamilias';
import { CriterioLogo } from './portal/CriterioLogo';

/* El video de Criterio completo, 1920×1080, en el orden de la página de agentes: qué es; la pirámide de
   hoy y la de ahora; las familias que corren hoy; dónde se probó y cuántos lo descargan; la evidencia;
   cómo se despliega cada familia; hacia dónde va —el mapa de la empresa por capas—; la invitación a
   instalar y el cierre.

   Solo se escriben aquí los rótulos y los tiempos: el titular, la pirámide y las etapas son los de la
   página de agentes (agentsTextos.ts), las familias, los países y el mapa salen de agentsMapa.ts y de
   las tablas que el portal genera del repositorio, y las descargas, de scripts/descargas.py sobre la
   rama `descargas` (grabar.mjs las trae). El reloj, en tiempo.jsx. */

const TEXTO = {
  es: {
    corren: 'Corre hoy',
    familias: 'familias',
    agentes: 'agentes',
    yRostrum: 'y Rostrum, el portal de todas',
    donde: 'Dónde se probó',
    paises: 'países',
    industrias: 'industrias',
    adopcion: 'Desde el lanzamiento',
    porDia: 'descargas al día, en promedio',
    fuente: 'Clonaciones del repositorio en GitHub: cada instalación o actualización descarga Criterio.',
    evidencia: 'La evidencia',
    piso: 'detectado como mínimo, con 95 % de confianza',
    rumbo: 'Hacia dónde vamos',
    instala: 'Instala Criterio.',
    instalaSub: 'Empieza por el área que más te cuesta hoy.',
    licencia: 'Código abierto · Apache 2.0',
  },
  en: {
    corren: 'Running today',
    familias: 'families',
    agentes: 'agents',
    yRostrum: 'and Rostrum, the portal for all of them',
    donde: 'Where it was tested',
    paises: 'countries',
    industrias: 'industries',
    adopcion: 'Since launch',
    porDia: 'downloads a day, on average',
    fuente: 'Repository clones on GitHub: every install or update downloads Criterio.',
    evidencia: 'The evidence',
    piso: 'caught at least, with 95% confidence',
    rumbo: 'Where we are going',
    instala: 'Install Criterio.',
    instalaSub: 'Start with the area that costs you most today.',
    licencia: 'Open source · Apache 2.0',
  },
};

function escenas(l) {
  const t = TEXTO[l];
  const L = LABORATORIO[l];
  const D = DESPLIEGUE[l];
  const fmt = (n, d = 0) => new Intl.NumberFormat(l === 'es' ? 'es-CO' : 'en-US', { maximumFractionDigits: d, minimumFractionDigits: d }).format(n);
  const pct = (v) => (l === 'es' ? `${fmt(v, 1)} %` : `${fmt(v, 1)}%`);
  // Las familias que corren hoy, en el orden en que la página las presenta.
  const vivas = MAPA.flatMap((c) => c.familias).filter(corre).map((f) => f.sigla).sort((a, b) => ordenDe(a) - ordenDe(b));
  const deRostrum = (s) => ROSTRUM.familias.find((f) => f.sigla === s);
  const lista = [];

  // 1 · Qué es: el titular de la página de agentes y la promesa.
  lista.push({
    dura: 8,
    sinMarca: true,
    render: (lt) => (
      <div className="yt-centro">
        <div className="yt-rolfila" style={sube(lt, 0.1)}><CriterioLogo locale={l} /></div>
        <h1 className="yt-titular" style={sube(lt, 0.6, 0.7)}>
          {TITULAR[l][0]}<br /><span style={{ opacity: avance(lt, 1.6, 0.7) }}>{TITULAR[l][1]}</span>
        </h1>
        <Eyebrow style={sube(lt, 3)}>{ROBOTS.promesa[l]}</Eyebrow>
      </div>
    ),
  });

  // 2 · La pirámide de hoy y la de ahora: el nivel C en la punta, y después parado sobre sus familias.
  lista.push({
    dura: 11,
    render: (lt) => (
      <div>
        <h2 className="yt-h2 corto" style={sube(lt, 0.1)}>{L.titulo}</h2>
        <div className="yt-piramides">
          <div style={sube(lt, 0.6)}>
            <svg viewBox="0 0 600 420" className="yt-piramide">
              <polygon points="300,10 590,410 10,410" className="cuerpo" />
              <polygon points="300,10 372,110 228,110" className="nivelc" />
              <line x1="155" y1="210" x2="445" y2="210" /><line x1="82" y1="310" x2="518" y2="310" />
              <text x="300" y="150" className="rotulo">{L.nivelC}</text>
            </svg>
            <p className="n">{L.hoy[0]}</p>
            <p className="r">{L.hoy[1]}</p>
          </div>
          <div style={sube(lt, 3)}>
            <svg viewBox="0 0 600 420" className="yt-piramide">
              <rect x="10" y="40" width="580" height="90" className="nivelc" />
              <text x="300" y="98" className="rotulo claro">{L.nivelC}</text>
              {vivas.map((s, i) => {
                const w = 580 / vivas.length;
                const p = avance(lt, 4 + i * 0.35, 0.5);
                return (
                  <g key={s} style={{ opacity: p }}>
                    <rect x={10 + i * w + 6} y={150 + (1 - p) * 40} width={w - 12} height={260} className="columna" />
                    <text x={10 + i * w + w / 2} y={300} className="sigla">{s.toUpperCase()}</text>
                  </g>
                );
              })}
            </svg>
            <p className="n">{L.ahora[0]}</p>
            <p className="r">{L.ahora[1]}</p>
          </div>
        </div>
      </div>
    ),
  });

  // 3 · Lo que corre hoy: cada familia con su rol y sus agentes.
  lista.push({
    dura: 13,
    render: (lt) => (
      <div>
        <div className="yt-cuentas chico" style={sube(lt, 0.1)}>
          <div><p className="v">{fmt(Math.round(VIVAS * avance(lt, 0.3, 1.5)))}</p><p className="k">{t.familias}</p></div>
          <div><p className="v">{fmt(Math.round(AGENTES_QUE_CORREN * avance(lt, 0.3, 1.5)))}</p><p className="k">{t.agentes}</p></div>
          <p className="y">{t.yRostrum}</p>
        </div>
        <div className="yt-tarjetas">
          {vivas.map((s, i) => (
            <div key={s} style={sube(lt, 1.6 + i * 0.6)}>
              <p className="s">{s.toUpperCase()}</p>
              <p className="r">{CRITERIO_NIVEL_C[s].portada.rol}</p>
              <p className="a">{deRostrum(s).agentes.map((a) => a.nombre).join(' · ')}</p>
            </div>
          ))}
        </div>
      </div>
    ),
  });

  // 4 · Dónde se probó: los países de todas las familias, encendidos en el mapa, y sus industrias.
  const orden = (c) => CRITERIO_PAISES.findIndex((p) => p.codigo === c);
  const codigos = [...PAISES_PROBADOS].sort((a, b) => orden(a) - orden(b));
  const enciende = (k) => 0.6 + k * 0.25;
  const fin = enciende(codigos.length);
  const mapa = (lt, tenue) => (
    <svg viewBox={CRITERIO_MAPA_GEO.viewBox} className="yt-mapa" aria-hidden="true" style={{ opacity: tenue ? 0.35 : 1 }}>
      {CRITERIO_MAPA_GEO.paises.map((g) => {
        const k = codigos.indexOf(g.codigo);
        return (
          <g key={g.codigo}>
            <path d={g.d} className="base" />
            {k >= 0 ? <path d={g.d} className="probado" style={{ opacity: tenue ? 1 : avance(lt, enciende(k), 0.4) }} /> : null}
          </g>
        );
      })}
    </svg>
  );
  lista.push({
    dura: 10,
    render: (lt) => (
      <div className="yt-donde">
        {mapa(lt, false)}
        <div>
          <Eyebrow>{t.donde}</Eyebrow>
          <div className="yt-cuentas">
            <div><p className="v">{fmt(Math.round(codigos.length * avance(lt, 0.6, fin - 0.6)))}</p><p className="k">{t.paises}</p></div>
            <div><p className="v">{fmt(Math.round(SECTORES_PROBADOS.length * avance(lt, 0.6, fin - 0.6)))}</p><p className="k">{t.industrias}</p></div>
          </div>
          <p className="yt-paises">
            {codigos.map((c, k) => <span key={c} style={{ opacity: avance(lt, enciende(k), 0.3) }}>{CRITERIO_PAISES.find((p) => p.codigo === c)?.nombre[l] ?? c}</span>)}
          </p>
          <div className="yt-sectores chico" style={sube(lt, fin + 0.3)}>
            {SECTORES_PROBADOS.map((x) => (
              <span key={x.id}><svg viewBox="0 0 48 48" aria-hidden="true"><path d={x.icono} /></svg>{x.nombre[l]}</span>
            ))}
          </div>
        </div>
      </div>
    ),
  });

  // 5 · Las descargas: solo el promedio diario desde el lanzamiento. Un total o una fecha envejecen al día
  // siguiente; el promedio se sostiene.
  const R = DESCARGAS;
  lista.push({
    dura: 5,
    render: (lt) => (
      <div className="yt-donde">
        {mapa(lt, true)}
        <div>
          <Eyebrow>{t.adopcion}</Eyebrow>
          <p className="yt-grande">{fmt(R.promedio_diario * avance(lt, 0.3, 1.4), 1)}</p>
          <p className="yt-grande-k" style={sube(lt, 0.8)}>{t.porDia}</p>
          <p className="yt-fuente" style={sube(lt, 2)}>{t.fuente}</p>
        </div>
      </div>
    ),
  });

  // 6 · La evidencia: el piso de cada familia y la regla de estable.
  const estable = D.etapas.organizacion;
  lista.push({
    dura: 10,
    oscuro: true,
    render: (lt) => (
      <div>
        <Eyebrow oscuro>{t.evidencia}</Eyebrow>
        <div className="yt-pisos">
          {vivas.map((s, i) => {
            const p = pisoDe(s);
            return (
              <div key={s} style={sube(lt, 0.5 + i * 0.4)}>
                <p className="s">{s.toUpperCase()}</p>
                <p className="v">{p ? pct(p.piso * avance(lt, 0.5 + i * 0.4, 1.2)) : '—'}</p>
              </div>
            );
          })}
        </div>
        <p className="yt-corto" style={sube(lt, 3.4)}>{t.piso}</p>
        <p className="yt-regla" style={sube(lt, 4.4)}><b>{estable[0]}.</b> {estable[1].split('. ')[0]}.</p>
      </div>
    ),
  });

  // 7 · Cómo se despliega: las cinco etapas, las mismas para todas.
  const etapas = ['diseno', 'construida', 'probada', 'ampliando', 'organizacion'];
  lista.push({
    dura: 10,
    render: (lt) => (
      <div>
        <h2 className="yt-h2 corto" style={sube(lt, 0.1)}>{D.title}</h2>
        <ol className="yt-etapas">
          {etapas.map((e, i) => (
            <li key={e} style={sube(lt, 0.9 + i * 0.7)}>
              <span className="i">{i + 1}</span>
              <p>{D.etapas[e][0]}</p>
            </li>
          ))}
        </ol>
        <p className="yt-lead" style={sube(lt, 4.8)}>{D.lead.split('. ')[0]}.</p>
      </div>
    ),
  });

  // 8 · Hacia dónde vamos: el mapa de la empresa por capas, con lo que corre y la dirección. Sin
  // prioridades ni conteo de lo que falta: el mapa es dirección, no un compromiso (decisión del 9 de
  // noviembre de 2026).
  const nombreDe = (f) => (f.sigla ? f.sigla.toUpperCase() : typeof f.clave === 'string' ? f.clave : f.clave[l]);
  lista.push({
    dura: 10,
    render: (lt) => (
      <div>
        <Eyebrow>{t.rumbo}</Eyebrow>
        <div className="yt-capas">
          {MAPA.map((c, i) => (
            <div key={c.id} style={sube(lt, 0.4 + i * 0.5)}>
              <p className="c">{c.nombre[l]}</p>
              <div className="fs">
                {c.familias.map((f) => (
                  <span key={nombreDe(f)} className={corre(f) ? 'corre' : 'dir'}>
                    {nombreDe(f)}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    ),
  });

  // 9 · La invitación.
  lista.push({
    dura: 4,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="yt-centro">
        <p className="yt-instala" style={sube(lt, 0.1, 0.6)}>{t.instala}</p>
        <p className="yt-detecto" style={sube(lt, 0.9)}>{t.instalaSub}</p>
      </div>
    ),
  });

  // 10 · El cierre: el marketplace —el mismo comando de cada familia—, la página y la licencia. Sin
  // versión: envejece con la siguiente liberación.
  lista.push({
    dura: 8,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="yt-centro">
        <div className="yt-rolfila" style={sube(lt, 0.1)}><CriterioLogo locale={l} oscuro /></div>
        <code className="yt-comando" style={sube(lt, 0.6)}>{SETUP_FAMILIAS.cfo[l].code[0][0]}</code>
        <p className="yt-url" style={sube(lt, 1.2)}>josenanez.com/agents</p>
        <p className="yt-pie-version" style={sube(lt, 1.8)}>{t.licencia}</p>
      </div>
    ),
  });
  return lista;
}

const idioma = new URLSearchParams(location.search).get('l') === 'en' ? 'en' : 'es';
montar(escenas(idioma), 'Criterio');
