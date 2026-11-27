import React from 'react';
import './youtube.css';
import './hoja.css';
import './equipos.css';
import { Eyebrow, avance, montar, sube } from './tiempo';
import { IMPRESORA, ROBOTS, ROSTRUM } from './lib/criterioImpresora';
import { CRITERIO_NIVEL_C } from './lib/criterioNivelC';
import { CRITERIO_HOJA_DE_RUTA } from './lib/criterioHojaDeRuta';
import { CRITERIO_PAISES } from './lib/criterioPaises';
import { CRITERIO_SECTORES } from './lib/criterioSectores';
import { dondeSeProbo, ordenDe } from './portal/agentsMapa';
import { Robot } from './portal/CriterioFamily';
import { CriterioLogo } from './portal/CriterioLogo';

/* «Nuestros equipos de agentes»: vertical 4:5, 1080×1350, para LinkedIn. Cada familia sale como un
   equipo en su cancha: sus agentes entran con su nombre y su posición, y después, lo que hace la
   familia, en qué países y en qué industrias se probó. El fútbol se queda en la cancha: los textos
   son los que el portal publica de cada familia.

   Las familias y sus agentes salen de ROSTRUM, en el orden de la página de agentes (ordenDe); la
   posición de cada agente, de la impresora de su familia (roles); lo que hace, de su portada
   (CRITERIO_NIVEL_C); su estado, de la calidad de su hoja de ruta; los países y las industrias, de
   las entidades de sus rondas (dondeSeProbo, la misma cuenta del mapa del portal). Solo los rótulos y
   los tiempos se escriben aquí. */

const TEXTO = {
  es: {
    titulo: 'Nuestros equipos de agentes',
    sub: 'Una familia por cada rol del nivel C: sus agentes, lo que hacen y dónde se probaron.',
    familia: 'Familia',
    nuevos: { titulo: 'Los equipos nuevos', sub: 'Las familias que llegan: sus agentes, lo que hacen y dónde se probaron.' },
    estado: { estable: 'Estable', laboratorio: 'En laboratorio' },
    hace: 'Qué hace',
    paises: ['país en las pruebas', 'países en las pruebas'],
    industrias: ['industria', 'industrias'],
    instala: 'Instala Criterio.',
    lema: 'El nivel C, soportado por familias de agentes de IA.',
    url: 'josenanez.com/es/agents',
    licencia: 'Código abierto · Apache 2.0',
  },
  en: {
    titulo: 'Our agent teams',
    sub: 'One family for each C-level role: its agents, what they do and where they were tested.',
    familia: 'Family',
    nuevos: { titulo: 'Our new agent teams', sub: 'The families joining: their agents, what they do and where they were tested.' },
    estado: { estable: 'Stable', laboratorio: 'In the lab' },
    hace: 'What it does',
    paises: ['country in the tests', 'countries in the tests'],
    industrias: ['industry', 'industries'],
    instala: 'Install Criterio.',
    lema: 'The C-level, supported by families of AI agents.',
    url: 'josenanez.com/agents',
    licencia: 'Open source · Apache 2.0',
  },
};

// Dónde va cada jugador en la cancha, según cuántos tiene el equipo: en una fila, repartidos.
const POSICIONES = { 1: [50], 2: [30, 70], 3: [18, 50, 82], 4: [14, 38, 62, 86] };
const uno = (n, [s, p]) => (n === 1 ? s : p);

function Equipo({ f, l, lt }) {
  const t = TEXTO[l];
  const roles = IMPRESORA[f.sigla][l].roles;
  const etiqueta = CRITERIO_HOJA_DE_RUTA[f.sigla]?.calidad?.etiqueta;
  if (!t.estado[etiqueta]) throw new Error(`La familia ${f.sigla} no tiene un estado conocido: ${etiqueta}`);
  const filas = CRITERIO_NIVEL_C[f.sigla].portada.filas.map((x) => x[l]);
  const { paises, sectores } = dondeSeProbo(f.sigla);
  const nombrePais = (c) => CRITERIO_PAISES.find((p) => p.codigo === c)?.nombre[l] ?? c;
  const orden = (c) => CRITERIO_PAISES.findIndex((p) => p.codigo === c);
  const lugares = [...paises].sort((x, y) => orden(x) - orden(y)).map(nombrePais);
  const industrias = CRITERIO_SECTORES.filter((x) => sectores.includes(x.id)).map((x) => x.nombre[l]);
  const pos = POSICIONES[f.agentes.length];
  if (!pos) throw new Error(`La cancha no tiene posiciones para ${f.agentes.length} agentes`);
  const entra = (k) => 0.6 + k * 0.45;
  const hace = entra(f.agentes.length) + 0.4;
  const datos = hace + 0.3 + filas.length * 0.3 + 0.2;
  return (
    <div className="eq">
      <div className="eq-cabeza" style={sube(lt, 0.05)}>
        <Eyebrow oscuro>{`Criterio · ${t.familia} ${f.sigla.toUpperCase()}`}</Eyebrow>
        <span className={`eq-estado ${etiqueta}`}>{t.estado[etiqueta]}</span>
      </div>
      <div className="eq-nombre" style={sube(lt, 0.15)}>
        <p className="s">{f.sigla.toUpperCase()}</p>
        <p className="n">{f.nombre[l]}</p>
      </div>
      <div className="eq-cancha">
        <div className="eq-lineas" style={{ opacity: avance(lt, 0.2, 0.6) }}>
          <i className="medio" /><i className="circulo" /><i className="area izq" /><i className="area der" />
        </div>
        {f.agentes.map((a, k) => (
          <div key={a.id} className="eq-jugador" style={{ left: `${pos[k]}%`, ...sube(lt, entra(k), 0.5) }}>
            <div className="yt-bot"><Robot kind={a.id} vivo /></div>
            <p className="nom">{a.nombre}</p>
            <p className="rol">{roles[a.id]}</p>
          </div>
        ))}
      </div>
      <div className="eq-hace">
        <p className="eq-k" style={sube(lt, hace)}>{t.hace}</p>
        {filas.map(([que, como], k) => (
          <div key={que} className="eq-fila" style={sube(lt, hace + 0.3 + k * 0.3, 0.4)}><b>{que}</b><span>{como}</span></div>
        ))}
      </div>
      <div className={`eq-datos ${lugares.length ? '' : 'solo'}`} style={sube(lt, datos)}>
        {lugares.length ? (
          <div>
            <p className="v">{Math.round(lugares.length * avance(lt, datos, 1))}</p>
            <p className="eq-k">{uno(lugares.length, t.paises)}</p>
            <p className="lista">{lugares.join(' · ')}</p>
          </div>
        ) : null}
        <div>
          <p className="v">{Math.round(industrias.length * avance(lt, datos + 0.3, 1))}</p>
          <p className="eq-k">{uno(industrias.length, t.industrias)}</p>
          <p className="lista">{industrias.join(' · ')}</p>
        </div>
      </div>
    </div>
  );
}

// ?e=cae,cdo solo esos equipos, con la portada de los nuevos: la pieza de un anuncio.
const SOLO = (new URLSearchParams(location.search).get('e') || '').split(',').filter(Boolean);

function escenas(l) {
  const t = { ...TEXTO[l], ...(SOLO.length ? TEXTO[l].nuevos : {}) };
  for (const s of SOLO) if (!ROSTRUM.familias.some((f) => f.sigla === s)) throw new Error(`El portal no publica la familia ${s}`);
  const familias = [...ROSTRUM.familias].filter((f) => !SOLO.length || SOLO.includes(f.sigla))
    .sort((x, y) => ordenDe(x.sigla) - ordenDe(y.sigla));
  const lista = [{
    dura: 5,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="eq-portada">
        <div style={sube(lt, 0.1)}><CriterioLogo locale={l} oscuro /></div>
        <h1 style={sube(lt, 0.5, 0.6)}>{t.titulo}</h1>
        <p style={sube(lt, 1.2)}>{t.sub}</p>
      </div>
    ),
  }];
  for (const f of familias) {
    lista.push({ dura: 9, oscuro: true, render: (lt) => <Equipo f={f} l={l} lt={lt} /> });
  }
  lista.push({
    dura: 6,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="hj-cierre">
        <div style={sube(lt, 0.1)}><CriterioLogo locale={l} oscuro /></div>
        <p className="yt-instala hj-instala" style={sube(lt, 0.5, 0.6)}>{t.instala}</p>
        <p className="hj-invita" style={sube(lt, 1.2)}>{t.lema}</p>
        <p className="yt-url hj-url" style={sube(lt, 1.8)}>{t.url}</p>
        <p className="hj-licencia" style={sube(lt, 2.4)}>{t.licencia}</p>
      </div>
    ),
  });
  return lista;
}

// Los gestos de los robots: la misma hoja de estilo que usan el portal, Rostrum y los README.
const estilo = document.createElement('style');
estilo.textContent = ROBOTS.css;
document.head.appendChild(estilo);
const l = new URLSearchParams(location.search).get('l') === 'en' ? 'en' : 'es';
montar(escenas(l), 'Criterio');
