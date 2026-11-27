import React from 'react';
import './youtube.css';
import './hoja.css';
import './mapa.css';
import { avance, montar, sube } from './tiempo';
import { ROSTRUM } from './lib/criterioImpresora';
import { CRITERIO_RONDAS } from './lib/criterioRondas';
import { CRITERIO_HOJA_DE_RUTA } from './lib/criterioHojaDeRuta';
import { CRITERIO_PAISES } from './lib/criterioPaises';
import { CRITERIO_SECTORES } from './lib/criterioSectores';
import { dondeSeProbo, ordenDe } from './portal/agentsMapa';
import { CriterioLogo } from './portal/CriterioLogo';
import MAPA from './mapa-contornos.json';

/* «Dónde se probó Criterio»: vertical 4:5, 1080×1350, para LinkedIn. Al centro, el mapa de México a la
   Patagonia; a la izquierda, las industrias; a la derecha, las familias. Los países se encienden uno a uno,
   y cada línea une una industria, un país y una familia: **cada línea es una entidad de una ronda
   publicada** (CRITERIO_RONDAS), con su país y su industria, controles incluidos. Nada se dibuja que no
   esté probado. La PMO se prueba por industria, sin país: sus líneas pasan por encima del mapa, al final.
   Una familia sin ronda con los agentes —la CTO— queda en la lista, apagada, con su estado.

   Abajo, una franja con lo que hace igual a todas: sus agentes, la regla de estable, lo que procesan, los
   marcos, las políticas y la decisión. Sin totales ni cifras con fecha. Los contornos, de Natural Earth
   (mapa-contornos.mjs). */

const TEXTO = {
  es: {
    eyebrow: 'Las rondas de prueba',
    titulo: 'Dónde se probaron sus agentes',
    industrias: 'Industrias',
    familias: 'Familias',
    lab: 'laboratorio',
    pmo: ['PMO', 'Probada por industria'],
    final: 'Cada línea es una prueba publicada.',
    puntos: [
      ['Agentes', 'Cada familia trae sus agentes, uno por cada parte del área, y procesan toda su documentación.'],
      ['Efectividad', 'Una familia es estable cuando su evidencia sostiene 95 % de efectividad mínima con 95 % de confianza.'],
      ['Sistemas', 'Las exportaciones de cualquier sistema —ERP, CRM, gestión de riesgos— en Excel o CSV, y los documentos en Word o PDF.'],
      ['Marcos', 'Sobre los marcos de cada área: PMI, ISO 37301, ISO 31000, las Normas Globales del IIA, DAMA-DMBOK, BCBS 239, el Código ICC.'],
      ['Políticas', 'Los plazos, los umbrales y los niveles los fija la política de cada organización, no el agente.'],
      ['Decisión', 'El modelo de lenguaje (LLM) extrae con su cita y el código calcula. La decisión sigue siendo de la persona.'],
    ],
    instala: 'Instala Criterio.',
    lema: 'El nivel C, soportado por familias de agentes de IA.',
    url: 'josenanez.com/es/agents',
    licencia: 'Código abierto · Apache 2.0',
  },
  en: {
    eyebrow: 'The test rounds',
    titulo: 'Where its agents were tested',
    industrias: 'Industries',
    familias: 'Families',
    lab: 'lab',
    pmo: ['PMO', 'Tested by industry'],
    final: 'Every line is a published test.',
    puntos: [
      ['Agents', 'Each family brings its agents, one for each part of the area, and they process all its documentation.'],
      ['Effectiveness', 'A family is stable when its evidence supports 95% minimum effectiveness at 95% confidence.'],
      ['Systems', 'Exports from any system —ERP, CRM, risk management— in Excel or CSV, and documents in Word or PDF.'],
      ['Frameworks', 'Built on each area’s frameworks: PMI, ISO 37301, ISO 31000, the IIA’s Global Standards, DAMA-DMBOK, BCBS 239, the ICC Code.'],
      ['Policies', 'Deadlines, thresholds and levels are set by each organisation’s policy, not by the agent.'],
      ['Decision', 'The language model (LLM) extracts with its citation and the code calculates. The decision stays with the person.'],
    ],
    instala: 'Install Criterio.',
    lema: 'The C-level, supported by families of AI agents.',
    url: 'josenanez.com/agents',
    licencia: 'Open source · Apache 2.0',
  },
};

// El lienzo: 1080×1350. Las industrias a la izquierda, las familias a la derecha y el mapa entre ellas.
const CUERPO = { arriba: 276, abajo: 1070 };
const IZQ = { x: 44, borde: 286 };
const DER = { x: 800, borde: 790 };
const MAPA_ANCHO = 488;
const ESCALA = MAPA_ANCHO / MAPA.ancho;
const MAPA_ALTO = MAPA.alto * ESCALA;
const MAPA_X = 296;
const MAPA_Y = CUERPO.abajo - MAPA_ALTO - 4;

// Los tiempos: la entrada, cada país, la PMO y el cierre del mapa.
const ENTRA = 3.2;
const PASO = 2.6;
const DIBUJA = 0.9;

const sectorDe = (id) => CRITERIO_SECTORES.find((s) => s.id === id || s.alias.includes(id))?.id;

// Las familias que publica el portal, en el orden de la página, con su estado de su hoja de ruta.
const FAMILIAS = [...ROSTRUM.familias].sort((a, b) => ordenDe(a.sigla) - ordenDe(b.sigla)).map((f) => ({
  sigla: f.sigla,
  nombre: f.nombre,
  etiqueta: CRITERIO_HOJA_DE_RUTA[f.sigla]?.calidad?.etiqueta,
  rondas: Boolean(CRITERIO_RONDAS[f.sigla]?.rondas?.length),
}));

// Cada entidad de cada ronda: familia, país, industria. La PMO no tiene país: va aparte.
// Solo lo que corrió con los agentes (rondas), no el material que prueba el motor (entidades).
const PRUEBAS = Object.entries(CRITERIO_RONDAS).flatMap(([sigla, r]) =>
  (r.rondas ?? []).filter((e) => e.pais && sectorDe(e.industria)).map((e) => ({ sigla, pais: e.pais, sector: sectorDe(e.industria) })));
const PMO = dondeSeProbo('pmo').sectores;

// Los países, de norte a sur, como se recorre el mapa.
const ancla = (iso) => {
  const p = MAPA.paises.find((x) => x.iso === iso);
  if (!p) throw new Error(`El mapa no tiene ${iso}`);
  return [MAPA_X + p.ancla[0] * ESCALA, MAPA_Y + p.ancla[1] * ESCALA];
};
const PAISES = [...new Set(PRUEBAS.map((p) => p.pais))].sort((a, b) => ancla(a)[1] - ancla(b)[1]);
for (const c of PAISES) if (!CRITERIO_PAISES.some((p) => p.codigo === c)) throw new Error(`El país ${c} no está en lib/criterioPaises.ts`);

// Las industrias: las que tocan las rondas o la PMO, en el orden del portal.
const SECTORES = CRITERIO_SECTORES.filter((s) => PRUEBAS.some((p) => p.sector === s.id) || PMO.includes(s.id));

const fila = (n, k) => CUERPO.arriba + ((CUERPO.abajo - CUERPO.arriba) / n) * (k + 0.5);
const yIndustria = Object.fromEntries(SECTORES.map((s, k) => [s.id, fila(SECTORES.length, k)]));
const yFamilia = Object.fromEntries(FAMILIAS.map((f, k) => [f.sigla, fila(FAMILIAS.length, k)]));

const inicio = (k) => ENTRA + k * PASO;
const PMO_INICIA = inicio(PAISES.length);
const FINAL = PMO_INICIA + 3;
const DURA = FINAL + 4.4;

// Las líneas, de la industria al país y del país a la familia: curvas suaves, de borde a borde.
const curva = ([x1, y1], [x2, y2]) => {
  const d = Math.max(60, Math.abs(x2 - x1) * 0.45);
  return `M${x1},${y1} C${x1 + d},${y1} ${x2 - d},${y2} ${x2},${y2}`;
};
const LINEAS = PAISES.flatMap((pais, k) => {
  const de = PRUEBAS.filter((p) => p.pais === pais);
  const [mx, my] = ancla(pais);
  const sectores = [...new Set(de.map((p) => p.sector))];
  const familias = [...new Set(de.map((p) => p.sigla))];
  return [
    ...sectores.map((s) => ({ k, pais, d: curva([IZQ.borde, yIndustria[s]], [mx, my]) })),
    ...familias.map((s) => ({ k, pais, d: curva([mx, my], [DER.borde, yFamilia[s]]) })),
  ];
});
// La PMO: de cada industria a la PMO, por encima del mapa.
const LINEAS_PMO = PMO.map((s) => {
  const [x1, y1] = [IZQ.borde, yIndustria[s]];
  const [x2, y2] = [DER.borde, yFamilia.pmo];
  return `M${x1},${y1} C${x1 + 180},${y1} ${x1 + 120},${CUERPO.arriba - 8} 540,${CUERPO.arriba - 8} S${x2 - 180},${y2} ${x2},${y2}`;
});

function Mapa({ l, lt }) {
  const t = TEXTO[l];
  // El país que está encendido ahora, y los que ya pasaron.
  const k = Math.floor((lt - ENTRA) / PASO);
  const actual = lt >= ENTRA && k < PAISES.length ? PAISES[k] : null;
  const vistos = new Set(PAISES.filter((_, i) => lt >= inicio(i)));
  const enPmo = lt >= PMO_INICIA && lt < FINAL;
  const alFinal = avance(lt, FINAL, 0.8);
  const deActual = actual ? PRUEBAS.filter((p) => p.pais === actual) : [];
  const vistosS = new Set(PRUEBAS.filter((p) => vistos.has(p.pais)).map((p) => p.sector));
  const vistosF = new Set(PRUEBAS.filter((p) => vistos.has(p.pais)).map((p) => p.sigla));
  if (lt >= PMO_INICIA) { PMO.forEach((s) => vistosS.add(s)); vistosF.add('pmo'); }
  const estado = (activo, visto) => (activo ? 'activo' : visto ? 'visto' : '');
  const nombrePais = (c) => CRITERIO_PAISES.find((p) => p.codigo === c)?.nombre[l] ?? c;
  const siglas = [...new Set(deActual.map((p) => p.sigla))].sort((a, b) => ordenDe(a) - ordenDe(b)).map((s) => s.toUpperCase());
  const punto = Math.min(t.puntos.length - 1, Math.floor(Math.max(0, lt - 2) / ((DURA - 2) / t.puntos.length)));
  const desdePunto = 2 + punto * ((DURA - 2) / t.puntos.length);

  return (
    <div className="mp">
      <div className="mp-logo" style={sube(lt, 0.05)}><CriterioLogo locale={l} oscuro conFuncion={false} /></div>
      <div className="mp-titulo" style={sube(lt, 0.35)}>
        <p className="yt-eyebrow oscuro">{t.eyebrow}</p>
        <h1>{t.titulo}</h1>
      </div>

      <p className="mp-col izq" style={{ top: CUERPO.arriba - 46, ...sube(lt, 0.7) }}>{t.industrias}</p>
      <p className="mp-col der" style={{ top: CUERPO.arriba - 46, ...sube(lt, 0.7) }}>{t.familias}</p>

      <svg className="mp-svg" viewBox="0 0 1080 1350" width="1080" height="1350">
        <g transform={`translate(${MAPA_X},${MAPA_Y}) scale(${ESCALA})`} style={{ opacity: avance(lt, 0.6, 1) }}>
          {MAPA.paises.map((p) => {
            const c = p.iso && vistos.has(p.iso) ? (p.iso === actual ? 'activo' : 'visto') : p.iso && PAISES.includes(p.iso) ? 'probado' : '';
            const brillo = p.iso === actual ? avance(lt, inicio(k), 0.4) : 1;
            return <path key={`${p.nombre}`} d={p.d} className={`mp-pais ${c}`} style={c === 'activo' ? { opacity: 0.5 + 0.5 * brillo } : undefined} />;
          })}
        </g>
        {LINEAS.map((x, i) => {
          if (!vistos.has(x.pais)) return null;
          const p = avance(lt, inicio(x.k) + 0.25, DIBUJA);
          const activa = x.pais === actual;
          const op = activa ? 1 : 0.16 + 0.22 * alFinal;
          return <path key={i} d={x.d} pathLength="1" className={`mp-linea ${activa ? 'activa' : ''}`} style={{ strokeDasharray: 1, strokeDashoffset: 1 - p, opacity: op }} />;
        })}
        {lt >= PMO_INICIA ? LINEAS_PMO.map((d, i) => (
          <path key={`pmo${i}`} d={d} pathLength="1" className={`mp-linea ${enPmo ? 'activa' : ''}`}
            style={{ strokeDasharray: 1, strokeDashoffset: 1 - avance(lt, PMO_INICIA + 0.2, DIBUJA), opacity: enPmo ? 1 : 0.16 + 0.22 * alFinal }} />
        )) : null}
        {PAISES.filter((c) => vistos.has(c)).map((c) => {
          const [x, y] = ancla(c);
          const activo = c === actual;
          return <circle key={c} cx={x} cy={y} r={activo ? 7 + 3 * avance(lt, inicio(k), 0.4) : 4.5} className={`mp-punto ${activo ? 'activo' : ''}`} />;
        })}
      </svg>

      {SECTORES.map((s, i) => {
        const activo = (actual && deActual.some((p) => p.sector === s.id)) || (enPmo && PMO.includes(s.id));
        return (
          <div key={s.id} className={`mp-ind ${estado(activo, vistosS.has(s.id))}`} style={{ top: yIndustria[s.id] - 22, ...sube(lt, 0.8 + i * 0.05, 0.4) }}>
            <svg viewBox="-4 -4 56 56" aria-hidden="true"><path d={s.icono} /></svg>
            <span>{s.nombre[l]}</span>
          </div>
        );
      })}
      {FAMILIAS.map((f, i) => {
        const activo = (actual && deActual.some((p) => p.sigla === f.sigla)) || (enPmo && f.sigla === 'pmo');
        return (
          <div key={f.sigla} className={`mp-fam ${estado(activo, vistosF.has(f.sigla))} ${f.rondas || f.sigla === 'pmo' ? '' : 'sin'}`} style={{ top: yFamilia[f.sigla] - 27, ...sube(lt, 0.8 + i * 0.05, 0.4) }}>
            <b>{f.sigla.toUpperCase()}</b>
            <span>{f.nombre[l]}{f.etiqueta === 'laboratorio' ? <em>{t.lab}</em> : null}</span>
          </div>
        );
      })}

      {/* El país encendido: su nombre y las familias que se probaron allí. */}
      <div className="mp-rotulo">
        {actual ? (
          <div key={actual} style={sube(lt, inicio(k), 0.35)}>
            <p className="n">{nombrePais(actual)}</p>
            <p className="s">{siglas.join(' · ')}</p>
          </div>
        ) : enPmo ? (
          <div style={sube(lt, PMO_INICIA, 0.35)}>
            <p className="n">{t.pmo[0]}</p>
            <p className="s">{t.pmo[1]}</p>
          </div>
        ) : lt >= FINAL ? (
          <div style={sube(lt, FINAL, 0.5)}>
            <p className="n fin">{t.final}</p>
          </div>
        ) : null}
      </div>

      {/* La franja: lo que hace igual a todas las familias. */}
      <div className="mp-franja" style={{ opacity: avance(lt, 1.6, 0.6) }}>
        <div key={punto} style={sube(lt, desdePunto, 0.45)}>
          <p className="k">{t.puntos[punto][0]}</p>
          <p className="v">{t.puntos[punto][1]}</p>
        </div>
      </div>
    </div>
  );
}

function escenas(l) {
  const t = TEXTO[l];
  return [
    { dura: DURA, oscuro: true, sinMarca: true, render: (lt) => <Mapa l={l} lt={lt} /> },
    {
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
    },
  ];
}

const l = new URLSearchParams(location.search).get('l') === 'en' ? 'en' : 'es';
montar(escenas(l), 'Criterio');
