import React from 'react';
import './youtube.css';
import './hoja.css';
import { Eyebrow, avance, cursor, escribe, montar, sube } from './tiempo';
import { ROBOTS, ROSTRUM } from './lib/criterioImpresora';
import { CRITERIO_PAISES } from './lib/criterioPaises';
import { CRITERIO_MAPA_GEO } from './lib/criterioMapaGeo';
import { CRITERIO_HOJA_DE_RUTA } from './lib/criterioHojaDeRuta';
import DESCARGAS from './lib/descargas.json';
import HOJA from './lib/una-pagina.json';
import { PAISES_PROBADOS, SECTORES_PROBADOS } from './portal/agentsMapa';
import { Robot } from './portal/CriterioFamily';
import { CriterioLogo } from './portal/CriterioLogo';

/* La hoja para la dirección, animada: vertical 4:5, 1080×1350, para LinkedIn. Cuenta lo mismo que la
   hoja y en su orden: el título; cada área con lo que hacen sus agentes en la operación, en la gerencia
   y lo que le llevan al nivel C, con lo que encontraron en las pruebas; los países y las industrias de
   las pruebas, que se cuentan y se nombran; los estándares; la efectividad mínima y las descargas; y la
   invitación.

   Los textos de la hoja salen de su archivo de datos en el portal (difusion/criterio-2-7-0/
   una-pagina.json, el mismo que escribe la hoja); los agentes, de ROSTRUM; los países, las industrias y
   el mapa, de agentsMapa.ts y de las tablas del portal; el piso de cada familia, de la hoja de ruta; las
   descargas, de scripts/descargas.py. Solo los rótulos y los tiempos se escriben aquí. Va en español,
   como la hoja. */

const TEXTO = {
  donde: 'Dónde se probó',
  paises: 'países',
  industrias: 'industrias',
  efectividad: 'o más de efectividad mínima en cada familia, con 95 % de confianza',
  descargas: 'descargas diarias en promedio, desde el lanzamiento',
  fuente: 'Pruebas sobre material sintético, contra una clave que los agentes no ven; la evidencia está publicada. Descargas: clonaciones en GitHub.',
  instala: 'Instala Criterio.',
  licencia: 'Código abierto · Apache 2.0',
};

const fmt = (n) => new Intl.NumberFormat('es-CO', { maximumFractionDigits: 0 }).format(n);
const agentesDe = (s) => ROSTRUM.familias.find((f) => f.sigla === s).agentes;
const nombres = (xs) => (xs.length === 1 ? xs[0] : `${xs.slice(0, -1).join(', ')}${/^[IÍ]/.test(xs.at(-1)) ? ' e ' : ' y '}${xs.at(-1)}`);

// La efectividad mínima que dice la hoja es el umbral de estable: el video no se graba si alguna
// familia queda por debajo de él.
const calidad = HOJA.areas.map((a) => CRITERIO_HOJA_DE_RUTA[a.sigla].calidad);
const UMBRAL = calidad[0].umbral;
const bajo = HOJA.areas.filter((a, i) => Math.min(...Object.values(calidad[i].pisos)) < UMBRAL);
if (bajo.length) throw new Error(`Por debajo del ${UMBRAL} %: ${bajo.map((a) => a.sigla).join(', ')}`);

function escenas() {
  const t = TEXTO;
  const lista = [];

  // 1 · El título, que se escribe, y lo que cambia.
  const [t0, t1] = HOJA.titulo;
  lista.push({
    dura: 7,
    sinMarca: true,
    render: (lt) => (
      <div className="hj-titulo">
        <div style={sube(lt, 0.1)}><CriterioLogo locale="es" /></div>
        <h1>{escribe(t0, lt, 0.5, 38)}{cursor(t0, lt, 0.5, 38)}<span style={sube(lt, 0.7 + t0.length / 38)}>{t1}</span></h1>
        <p className="hj-sub" style={sube(lt, 1.6 + t0.length / 38)}>{HOJA.sub}</p>
      </div>
    ),
  });

  // 2 · Cada área: el robot que la representa, sus agentes y lo que hacen en cada nivel; el nivel C, al
  // final y resaltado; y lo que encontraron en las pruebas, que se escribe.
  const [op, ge, nc] = HOJA.niveles;
  for (const a of HOJA.areas) {
    const agentes = agentesDe(a.sigla).map((x) => x.nombre);
    const hallazgo = `${HOJA.prueba}: ${a.hallazgo}`;
    lista.push({
      dura: 6,
      oscuro: true,
      render: (lt) => (
        <div className="hj-area">
          <Eyebrow oscuro style={sube(lt, 0.05)}>{HOJA.eyebrow}</Eyebrow>
          <div className="hj-cabeza" style={sube(lt, 0.2)}>
            <div className="yt-bot hj-bot"><Robot kind={a.robot} vivo /></div>
            <div>
              <p className="hj-sigla">{a.sigla.toUpperCase()}</p>
              <p className="hj-quien">{a.area} · {nombres(agentes)}</p>
            </div>
          </div>
          <div className="hj-niveles">
            {[[op, a.operacion, 0.9], [ge, a.gerencia, 1.6], [nc, a.nivel_c, 2.3]].map(([k, v, d], i) => (
              <div key={k} className={i === 2 ? 'c' : ''} style={sube(lt, d)}><b>{k}</b><span>{v}</span></div>
            ))}
          </div>
          <p className="hj-prueba">{escribe(hallazgo, lt, 3.1, 48)}{cursor(hallazgo, lt, 3.1, 48)}</p>
        </div>
      ),
    });
  }

  // 3 · Los países: se encienden en el mapa y se nombran uno a uno, y la cuenta sube con cada uno.
  const orden = (c) => CRITERIO_PAISES.findIndex((p) => p.codigo === c);
  const codigos = [...PAISES_PROBADOS].sort((x, y) => orden(x) - orden(y));
  const enciende = (k) => 0.7 + k * 0.32;
  lista.push({
    dura: 8,
    render: (lt) => (
      <div className="hj-paises">
        <Eyebrow style={sube(lt, 0.05)}>{t.donde}</Eyebrow>
        <div className="hj-cuenta"><span className="v">{fmt(codigos.filter((c, k) => lt >= enciende(k)).length)}</span><span className="k">{t.paises}</span></div>
        <div className="hj-mapa-fila">
          <svg viewBox={CRITERIO_MAPA_GEO.viewBox} className="yt-mapa hj-mapa" aria-hidden="true">
            {CRITERIO_MAPA_GEO.paises.map((g) => {
              const k = codigos.indexOf(g.codigo);
              return (
                <g key={g.codigo}>
                  <path d={g.d} className="base" />
                  {k >= 0 ? <path d={g.d} className="probado" style={{ opacity: avance(lt, enciende(k), 0.4) }} /> : null}
                </g>
              );
            })}
          </svg>
          <ul className="hj-nombres">
            {codigos.map((c, k) => <li key={c} style={sube(lt, enciende(k), 0.35)}>{CRITERIO_PAISES.find((p) => p.codigo === c)?.nombre.es ?? c}</li>)}
          </ul>
        </div>
      </div>
    ),
  });

  // 4 · Las industrias: aparecen con su ícono, y la cuenta sube con cada una.
  const aparece = (k) => 0.6 + k * 0.22;
  lista.push({
    dura: 6.5,
    render: (lt) => (
      <div>
        <Eyebrow style={sube(lt, 0.05)}>{t.donde}</Eyebrow>
        <div className="hj-cuenta"><span className="v">{fmt(SECTORES_PROBADOS.filter((x, k) => lt >= aparece(k)).length)}</span><span className="k">{t.industrias}</span></div>
        <div className="yt-sectores hj-sectores">
          {SECTORES_PROBADOS.map((x, k) => (
            <span key={x.id} style={sube(lt, aparece(k), 0.35)}><svg viewBox="0 0 48 48" aria-hidden="true"><path d={x.icono} /></svg>{x.nombre.es}</span>
          ))}
        </div>
      </div>
    ),
  });

  // 5 · Los estándares sobre los que se construye cada familia, uno a uno.
  const E = HOJA.estandares;
  lista.push({
    dura: 6,
    render: (lt) => (
      <div>
        <Eyebrow style={sube(lt, 0.05)}>{E.subtitulo}</Eyebrow>
        <h2 className="hj-h2" style={sube(lt, 0.2)}>{E.titulo}</h2>
        <ul className="hj-estandares">
          {E.lista.map((x, k) => <li key={x} style={sube(lt, 0.9 + k * 0.55)}>{x}</li>)}
        </ul>
      </div>
    ),
  });

  // 6 · La efectividad mínima y las descargas diarias, que cuentan hasta su cifra.
  const porDia = Math.round(DESCARGAS.promedio_diario);
  lista.push({
    dura: 6,
    render: (lt) => (
      <div className="hj-cifras">
        <div style={sube(lt, 0.1)}><p className="v">{fmt(UMBRAL * avance(lt, 0.3, 1.4))} %</p><p className="k">{t.efectividad}</p></div>
        <div style={sube(lt, 1.4)}><p className="v">{fmt(porDia * avance(lt, 1.6, 1.4))}</p><p className="k">{t.descargas}</p></div>
        <p className="hj-fuente" style={sube(lt, 3)}>{t.fuente}</p>
      </div>
    ),
  });

  // 7 · La invitación y la página.
  lista.push({
    dura: 6,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="hj-cierre">
        <div style={sube(lt, 0.1)}><CriterioLogo locale="es" oscuro /></div>
        <p className="yt-instala hj-instala" style={sube(lt, 0.5, 0.6)}>{t.instala}</p>
        <p className="hj-invita" style={sube(lt, 1.2)}>{HOJA.invitacion}</p>
        <p className="yt-url hj-url" style={sube(lt, 1.8)}>{HOJA.url}</p>
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
montar(escenas(), 'Criterio');
