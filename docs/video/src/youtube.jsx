import React from 'react';
import './youtube.css';
import { Eyebrow, avance, cursor, escribe, montar, sube } from './tiempo';
import { CRITERIO_NIVEL_C } from './lib/criterioNivelC';
import { IMPRESORA } from './lib/criterioImpresora';
import { CRITERIO_CFO } from './lib/criterioCfo';
import { CRITERIO_CLO } from './lib/criterioClo';
import { CRITERIO_EA } from './lib/criterioEa';
import { CRITERIO_CCO } from './lib/criterioCco';
import { CRITERIO_CISO } from './lib/criterioCiso';
import { CRITERIO_RONDAS } from './lib/criterioRondas';
import { CRITERIO_PAISES } from './lib/criterioPaises';
import { CRITERIO_SECTORES } from './lib/criterioSectores';
import { CRITERIO_MAPA_GEO } from './lib/criterioMapaGeo';
import { casosDe, pisoDe, resumenPrueba } from './portal/criterioPrueba';
import { PASOS_INSTALAR, SETUP_FAMILIAS, codigoFamilia } from './portal/criterioSetupFamilias';
import { AGENT_TABS_FAMILIAS } from './portal/criterioAgentTabsFamilias';
import { CALC_FAMILIAS } from './portal/criterioCalculatorFamilias';
import { Robot } from './portal/CriterioFamily';
import { CriterioLogo } from './portal/CriterioLogo';

/* El video de cada familia para YouTube, 1920×1080, en unos noventa segundos y en el orden de su
   página: un hallazgo de entrada; el rol y lo que hace cada función, con qué se integra; dónde se
   probó; los agentes; la capacidad que hoy se va en el trabajo que preparan; la evidencia; cada
   agente con lo que encontró; Rostrum; la versión y la instalación. Una idea por pantalla.

   Solo se escriben aquí los rótulos, los tiempos y qué agente abre el video: cada texto y cada cifra
   salen de lo que el portal publica desde el repositorio (grabar.mjs trae esos archivos), así que lo
   que cambia en el repositorio cambia en el video la próxima vez que se graba. El reloj y cómo
   aparece cada cosa están en tiempo.jsx, que comparte con el video de Criterio. */

const AGENTES = { cfo: CRITERIO_CFO, clo: CRITERIO_CLO, ea: CRITERIO_EA, cco: CRITERIO_CCO, ciso: CRITERIO_CISO };
// La PMO no tiene una ficha de agentes como las demás: sus agentes son los de sus pestañas.
const agentesDe = (sigla, l) => AGENTES[sigla]?.agentes ?? AGENT_TABS_FAMILIAS[sigla][l].agents.map((a) => ({ id: a.id, nombre: a.name }));

// El agente cuyo hallazgo abre el video: el primero que dice su captura de Rostrum en la página.
const GANCHO = { pmo: 'vera', cfo: 'aurea', clo: 'fidel', ea: 'ofelia', cco: 'valeria', ciso: 'amparo' };

const TEXTO = {
  es: {
    prueba: 'Datos de prueba',
    detecto: (n) => `${n} lo detectó antes de la decisión.`,
    donde: 'Dónde se probó',
    paises: 'países',
    entidades: 'entidades de prueba',
    control: (n) => `y ${n} entidades de control`,
    familia: (n) => `${['', 'Una agente', 'Dos agentes', 'Tres agentes', 'Cuatro agentes'][n] || `${n} agentes`} y un portal`,
    capacidad: 'Lo que hoy hace tu equipo, a mano',
    calcula: '¿Cuánto le cuesta? Calcúlalo con tus números en la página.',
    evidencia: 'La evidencia',
    piso: 'detectado como mínimo, con 95 % de confianza',
    casos: 'casos probados',
    controles: (k, n) => `${k} de ${n} entidades de control sin una sola alarma falsa`,
    defectos: (n, r, k) => (k === n ? `${n} defectos encontrados en ${r} rondas: todos corregidos y verificados` : `${n} defectos encontrados en ${r} rondas: ${k} corregidos y verificados`),
    encontro: 'Lo que encontró',
    licencia: 'Código abierto · Apache 2.0',
  },
  en: {
    prueba: 'Test data',
    detecto: (n) => `${n} caught it before the decision.`,
    donde: 'Where it was tested',
    paises: 'countries',
    entidades: 'test entities',
    control: (n) => `and ${n} control entities`,
    familia: (n) => `${['', 'One agent', 'Two agents', 'Three agents', 'Four agents'][n] || `${n} agents`} and a portal`,
    capacidad: 'What your team does by hand today',
    calcula: 'What does it cost? Work it out with your numbers on the page.',
    evidencia: 'The evidence',
    piso: 'caught at least, with 95% confidence',
    casos: 'cases tested',
    controles: (k, n) => `${k} of ${n} control entities without a single false alarm`,
    defectos: (n, r, k) => (k === n ? `${n} defects found in ${r} rounds: all fixed and verified` : `${n} defects found in ${r} rounds: ${k} fixed and verified`),
    encontro: 'What it found',
    licencia: 'Open source · Apache 2.0',
  },
};

function escenas(sigla, l) {
  const t = TEXTO[l];
  const fmt = (n, d = 0) => new Intl.NumberFormat(l === 'es' ? 'es-CO' : 'en-US', { maximumFractionDigits: d, minimumFractionDigits: d }).format(n);
  const pct = (v, d = 1) => (l === 'es' ? `${fmt(v, d)} %` : `${fmt(v, d)}%`);
  const P = CRITERIO_NIVEL_C[sigla].portada;
  const imp = IMPRESORA[sigla][l];
  const agentes = agentesDe(sigla, l);
  const tabs = AGENT_TABS_FAMILIAS[sigla][l].agents;
  const D = CRITERIO_RONDAS[sigla];
  const lista = [];

  // 1 · El hallazgo que abre: el primero de la captura de Rostrum del agente elegido, en los datos de prueba.
  const quien = tabs.find((a) => a.id === GANCHO[sigla]) ?? tabs[0];
  // La captura de Vera cuenta el hallazgo en una oración entera; las demás lo dan antes de la primera coma.
  const tras = quien.caption.split(': ')[1];
  const hallazgo = sigla === 'pmo' ? tras.split('. ')[0].replace(/\.$/, '') : tras.split(', ')[0];
  const gancho = hallazgo.charAt(0).toUpperCase() + hallazgo.slice(1) + '.';
  lista.push({
    dura: 6,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="yt-centro">
        <Eyebrow oscuro style={sube(lt, 0.1)}>{t.prueba}</Eyebrow>
        <p className="yt-gancho">{escribe(gancho, lt, 0.4, 32)}{cursor(gancho, lt, 0.4, 32)}</p>
        <p className="yt-detecto" style={sube(lt, 0.6 + gancho.length / 32)}>{t.detecto(quien.name)}</p>
      </div>
    ),
  });

  // 2 · El rol y lo que hace cada función; abajo pasan los nombres con los que se integra.
  const marcas = [...new Set(P.filas.flatMap((x) => x[l][2].split(' · ')))];
  // El rol en una sola línea: un rol largo, como el del CISO, baja de tamaño para caber en el ancho.
  const tamRol = Math.min(132, Math.floor(1600 / (0.39 * P.rol.length)));
  const paso = 1.7;
  lista.push({
    dura: 2.2 + P.filas.length * paso + 2.4,
    render: (lt) => (
      <div>
        <div className="yt-rolfila" style={sube(lt, 0.1)}>
          <CriterioLogo locale={l} sigla={sigla} conFuncion={false} />
        </div>
        <h1 className="yt-h1" style={{ ...sube(lt, 0.3, 0.7), fontSize: `${tamRol}px` }}>{P.rol}</h1>
        <div className="yt-funciones">
          {P.filas.map((x, i) => (
            <div key={x.es[0]} style={sube(lt, 2.2 + i * paso)}>
              <b>{x[l][0]}</b>
              <span>{x[l][1]}</span>
            </div>
          ))}
        </div>
        <div className="yt-cinta" style={{ opacity: avance(lt, 2.2, 0.8) }}>
          <div style={{ transform: `translateX(${-lt * 90}px)` }}>
            {[...marcas, ...marcas, ...marcas].map((m, i) => <span key={i}>{m}</span>)}
          </div>
        </div>
      </div>
    ),
  });

  // 3 · Dónde se probó: los países se encienden en el mapa mientras suben las cuentas. La EA no lleva
  // mapa, como en su página: su prueba se cuenta en oficinas, no en países.
  const orden = (c) => CRITERIO_PAISES.findIndex((p) => p.codigo === c);
  // La PMO no se prueba por país: sus entidades no traen uno, y la cuenta de países no se muestra.
  const codigos = [...new Set(D.entidades.map((e) => e.pais).filter(Boolean))].sort((a, b) => orden(a) - orden(b));
  const nombrePais = (c) => CRITERIO_PAISES.find((p) => p.codigo === c)?.nombre[l] ?? c;
  const sectores = [...new Set(D.entidades.filter((e) => !e.control).map((e) => e.industria))].map((id) => {
    const x = CRITERIO_SECTORES.find((y) => y.id === id);
    if (!x) throw new Error(`La industria ${id} no está en lib/criterioSectores.ts`);
    return x;
  });
  const enControl = D.entidades.filter((e) => e.control).length;
  const conMapa = sigla !== 'ea' && codigos.length > 0;
  const enciende = (k) => 0.6 + k * 0.28;
  const finPaises = enciende(codigos.length || 3);
  lista.push({
    dura: 10,
    render: (lt) => (
      <div className={conMapa ? 'yt-donde' : ''}>
        {conMapa ? (
          <svg viewBox={CRITERIO_MAPA_GEO.viewBox} className="yt-mapa" aria-hidden="true">
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
        ) : null}
        <div>
          <Eyebrow>{t.donde}</Eyebrow>
          <div className="yt-cuentas">
            {codigos.length ? <div><p className="v">{fmt(Math.round(codigos.length * avance(lt, 0.6, finPaises - 0.6)))}</p><p className="k">{t.paises}</p></div> : null}
            <div><p className="v">{fmt(Math.round(D.entidades.length * avance(lt, 0.6, finPaises - 0.6)))}</p><p className="k">{t.entidades}</p></div>
          </div>
          <p className="yt-paises">
            {codigos.map((c, k) => <span key={c} style={{ opacity: avance(lt, enciende(k), 0.3) }}>{nombrePais(c)}</span>)}
          </p>
          <div className="yt-sectores" style={sube(lt, finPaises + 0.3)}>
            {sectores.map((x) => (
              <span key={x.id}>
                <svg viewBox="0 0 48 48" aria-hidden="true"><path d={x.icono} /></svg>
                {x.nombre[l]}
              </span>
            ))}
          </div>
          {enControl ? <p className="yt-control" style={sube(lt, finPaises + 0.8)}>{t.control(enControl)}</p> : null}
        </div>
      </div>
    ),
  });

  // 4 · Los agentes y Rostrum, que se encienden uno a uno.
  const bots = [...agentes.map((a) => a.id), 'rostrum'];
  const nombre = (id) => (id === 'rostrum' ? 'Rostrum' : agentes.find((a) => a.id === id).nombre);
  lista.push({
    dura: 6,
    render: (lt) => (
      <div>
        <h2 className="yt-h2" style={sube(lt, 0.2)}>{t.familia(agentes.length)}</h2>
        <div className="yt-bots">
          {bots.map((id, i) => (
            <div key={id} className="yt-bot" style={sube(lt, 0.8 + i * 0.6)}>
              <Robot kind={id} vivo />
              <p className="n">{nombre(id)}</p>
              <p className="r">{imp.roles[id]}</p>
            </div>
          ))}
        </div>
      </div>
    ),
  });

  // 5 · La capacidad: las tareas que hoy hace el equipo y que los agentes preparan, que se marcan una a
  // una; el costo lo pone cada quien en la calculadora de la página.
  const calc = CALC_FAMILIAS[sigla];
  const tareas = calc.ids.flatMap((id) => calc[l].agents[id].tasks.slice(0, 2));
  lista.push({
    dura: 8.5,
    render: (lt) => (
      <div>
        <Eyebrow>{t.capacidad}</Eyebrow>
        <ul className="yt-tareas">
          {tareas.map((x, i) => (
            <li key={x} style={sube(lt, 0.4 + i * 0.55)}>
              <span className="marca" style={{ opacity: avance(lt, 0.7 + i * 0.55, 0.3) }}>✓</span>
              {x}
            </li>
          ))}
        </ul>
        <p className="yt-calcula" style={sube(lt, 0.8 + tareas.length * 0.55)}>{t.calcula}</p>
      </div>
    ),
  });

  // 6 · La evidencia: el piso que cita la portada, lo que detecta cada función con sus casos, los controles
  // y los defectos.
  const piso = pisoDe(sigla);
  const r = resumenPrueba(sigla);
  const filas = (CRITERIO_NIVEL_C[sigla].alcance ?? []).map((x) => ({ f: x[l][0], n: casosDe(sigla, x.senales) }));
  const mayor = Math.max(1, ...filas.map((x) => x.n));
  const rondas = new Set(D.rondas.map((x) => x.ronda)).size;
  const verificados = D.defectos.filter((d) => d.estado === 'verificado').length;
  lista.push({
    dura: 14,
    oscuro: true,
    render: (lt) => (
      <div>
        <Eyebrow oscuro>{t.evidencia}</Eyebrow>
        <div className="yt-piso">
          <p className="yt-valor">{piso ? pct(piso.piso * avance(lt, 0.3, 1.6)) : null}</p>
          <div style={sube(lt, 1.2)}>
            <p className="yt-corto">{t.piso}</p>
            <p className="yt-sub">{fmt(r.senales[1])} {t.casos}</p>
          </div>
        </div>
        <div className="yt-barras">
          {filas.map((x, i) => {
            const p = avance(lt, 3 + i * 0.5, 1);
            return (
              <div key={x.f} style={{ opacity: avance(lt, 3 + i * 0.5, 0.3) }}>
                <span className="f">{x.f}</span>
                <span className="b"><i style={{ width: `${(100 * x.n * p) / mayor}%` }} /></span>
                <span className="n">{fmt(Math.round(x.n * p))}</span>
              </div>
            );
          })}
        </div>
        <div className="yt-sello" style={sube(lt, 3.8 + filas.length * 0.5)}>
          {r.controles[1] ? <p>{t.controles(r.controles[0], r.controles[1])}</p> : null}
          {D.defectos.length ? <p>{t.defectos(D.defectos.length, rondas, verificados)}</p> : null}
        </div>
      </div>
    ),
  });

  // 7 · Cada agente, con lo que encontró en los datos de prueba: la captura de Rostrum de su página.
  for (const a of tabs) {
    lista.push({
      dura: 7,
      render: (lt) => (
        <div className="yt-agente">
          <div className="yt-quien" style={sube(lt, 0.1)}>
            <div className="yt-bot grande"><Robot kind={a.id} vivo /></div>
            <p className="yt-nombre">{a.name}</p>
            <p className="yt-rol">{a.role}</p>
          </div>
          <div>
            <Eyebrow style={sube(lt, 0.3)}>{t.encontro}</Eyebrow>
            <p className="yt-hallazgo">{escribe(a.caption, lt, 0.6, 55)}{cursor(a.caption, lt, 0.6, 55)}</p>
          </div>
        </div>
      ),
    });
  }

  // 8 · Rostrum: lo mismo que dice en la impresora de la familia.
  const rostrum = imp.guion.find((g) => g.quien === 'rostrum');
  lista.push({
    dura: 5.5,
    render: (lt) => (
      <div className="yt-agente">
        <div className="yt-quien" style={sube(lt, 0.1)}>
          <div className="yt-bot grande"><Robot kind="rostrum" vivo /></div>
          <p className="yt-nombre">Rostrum</p>
          <p className="yt-rol">{imp.roles.rostrum}</p>
        </div>
        <p className="yt-hace" style={sube(lt, 0.5)}>{rostrum.texto}</p>
      </div>
    ),
  });

  // 9 · La instalación: los mismos tres pasos y comandos de la página. Sin la versión: envejece con la
  // siguiente liberación.
  const pasos = PASOS_INSTALAR[l];
  const code = SETUP_FAMILIAS[sigla]?.[l].code ?? codigoFamilia(sigla, agentes.map((a) => a.nombre), `/criterio-${sigla}:${sigla}-setup`, l);
  lista.push({
    dura: 11,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div>
        <div className="yt-rolfila" style={sube(lt, 0.1)}>
          <CriterioLogo locale={l} sigla={sigla} oscuro conFuncion={false} />
          <span className="yt-version">{t.licencia}</span>
        </div>
        <ol className="yt-pasos">
          {[pasos.marketplace, pasos.familia, pasos.configurar].map((p, i) => (
            <li key={p} style={sube(lt, 0.6 + i * 1.2)}>
              <span className="i">{i + 1}</span>
              <div>
                <p className="p">{p}</p>
                <code>{code[i][0]}</code>
              </div>
            </li>
          ))}
        </ol>
        <p className="yt-url" style={sube(lt, 4.6)}>josenanez.com/agents/criterio-{sigla}</p>
      </div>
    ),
  });
  return lista;
}

const q = new URLSearchParams(location.search);
const idioma = q.get('l') === 'en' ? 'en' : 'es';
const familia = q.get('f') in GANCHO ? q.get('f') : 'cfo';
montar(escenas(familia, idioma), `Criterio ${familia.toUpperCase()}`);
