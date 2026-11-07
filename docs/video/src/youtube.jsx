import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { flushSync } from 'react-dom';
import './youtube.css';
import { CRITERIO_NIVEL_C } from './lib/criterioNivelC';
import { IMPRESORA, ROBOTS, ROSTRUM } from './lib/criterioImpresora';
import { CRITERIO_CFO } from './lib/criterioCfo';
import { CRITERIO_CLO } from './lib/criterioClo';
import { CRITERIO_EA } from './lib/criterioEa';
import { CRITERIO_CCO } from './lib/criterioCco';
import { CRITERIO_CISO } from './lib/criterioCiso';
import { casosDe, pisoDe, resumenPrueba } from './portal/criterioPrueba';
import { PASOS_INSTALAR, SETUP_FAMILIAS, versionDe } from './portal/criterioSetupFamilias';
import { Robot } from './portal/CriterioFamily';
import { CriterioLogo, CriterioSimbolo } from './portal/CriterioLogo';

/* El video de cada familia para YouTube, 1920×1080: la familia —su rol, el costo del problema y lo
   que hace cada función—, cada agente con lo que hace y lo que detecta, Rostrum, la prueba y cómo
   se instala. Solo se escriben aquí los rótulos y los tiempos: cada texto y cada cifra salen de lo
   que el portal publica desde el repositorio (grabar.mjs trae esos archivos), así que una cifra que
   cambia en el repositorio cambia en el video la próxima vez que se graba.

   El tiempo no corre solo: grabar.mjs llama a window.__ir(segundo) cuadro por cuadro, y cada
   animación —también los gestos de los robots— se dibuja en ese segundo exacto. */

const AGENTES = { cfo: CRITERIO_CFO, clo: CRITERIO_CLO, ea: CRITERIO_EA, cco: CRITERIO_CCO, ciso: CRITERIO_CISO };

const TEXTO = {
  es: {
    problema: 'El costo del problema',
    funciones: 'Lo que hace',
    columnas: ['Función', 'Qué hace', 'Con qué se integra'],
    familia: (n) => `${['', 'Una agente', 'Dos agentes', 'Tres agentes', 'Cuatro agentes'][n] || `${n} agentes`} y un portal`,
    hace: 'Lo que hace',
    detecta: 'Lo que detecta antes de la decisión',
    senales: (n) => `${n} señales`,
    casos: (n) => `${n} casos probados`,
    prueba: 'La prueba',
    piso: 'de lo que debía detectarse, detectado como mínimo, con 95 % de confianza',
    entidades: 'entidades de prueba',
    paises: 'países',
    controles: (k, n) => `${k} de ${n} entidades de control sin una sola alarma falsa`,
    version: (v) => `Versión ${v}`,
    licencia: 'Código abierto · Apache 2.0',
  },
  en: {
    problema: 'The cost of the problem',
    funciones: 'What it does',
    columnas: ['Function', 'What it does', 'Works with'],
    familia: (n) => `${['', 'One agent', 'Two agents', 'Three agents', 'Four agents'][n] || `${n} agents`} and a portal`,
    hace: 'What it does',
    detecta: 'What it catches before the decision',
    senales: (n) => `${n} signals`,
    casos: (n) => `${n} cases tested`,
    prueba: 'The proof',
    piso: 'of what had to be caught, caught at least, with 95% confidence',
    entidades: 'test entities',
    paises: 'countries',
    controles: (k, n) => `${k} of ${n} control entities without a single false alarm`,
    version: (v) => `Version ${v}`,
    licencia: 'Open source · Apache 2.0',
  },
};

// Lo que aparece, aparece así: sube y se enciende en medio segundo.
const entre = (x) => Math.min(1, Math.max(0, x));
const suave = (x) => 1 - (1 - x) ** 3;
const sube = (lt, desde, dura = 0.6) => {
  const p = suave(entre((lt - desde) / dura));
  return { opacity: p, transform: `translateY(${(1 - p) * 28}px)` };
};

function Eyebrow({ children, oscuro }) {
  return <p className={`yt-eyebrow ${oscuro ? 'oscuro' : ''}`}>{children}</p>;
}

function escenas(sigla, l) {
  const t = TEXTO[l];
  const fmt = (n, d = 0) => new Intl.NumberFormat(l === 'es' ? 'es-CO' : 'en-US', { maximumFractionDigits: d, minimumFractionDigits: d }).format(n);
  const pct = (v) => (l === 'es' ? `${fmt(v, 1)} %` : `${fmt(v, 1)}%`);
  const N = CRITERIO_NIVEL_C[sigla];
  const P = N.portada;
  const imp = IMPRESORA[sigla][l];
  const agentes = AGENTES[sigla].agentes;
  const lista = [];

  // 1 · El rol. Esta escena y el cierre llevan el logotipo grande: sin la marca del pie.
  lista.push({
    dura: 6,
    sinMarca: true,
    render: (lt) => (
      <div className="yt-centro">
        <div style={sube(lt, 0.2)} className="yt-logo"><CriterioLogo locale={l} sigla={sigla} /></div>
        <Eyebrow><span style={sube(lt, 0.8)}>{ROBOTS.promesa[l]}</span></Eyebrow>
        <h1 className="yt-h1" style={sube(lt, 1.3, 0.9)}>{P.rol}</h1>
      </div>
    ),
  });

  // 2 · El costo del problema: las dos cifras de terceros de la portada.
  lista.push({
    dura: 12,
    render: (lt) => (
      <div>
        <Eyebrow>{t.problema}</Eyebrow>
        <div className="yt-cifras">
          {P.cifras.map((c, i) => (
            <div key={c.id} className="yt-cifra" style={sube(lt, 0.6 + i * 3.2, 0.8)}>
              <p className="yt-valor">{c.valor[l]}</p>
              <p className="yt-corto">{c.corto[l]}</p>
              <p className="yt-fuente">{c.fuente.split(',')[0]}, {c.anio}</p>
            </div>
          ))}
        </div>
      </div>
    ),
  });

  // 3 · Lo que hace: una fila por función, con qué se integra.
  const paso = 3.2;
  lista.push({
    dura: 3 + P.filas.length * paso + 2,
    render: (lt) => (
      <div>
        <Eyebrow>{t.funciones}</Eyebrow>
        <div className="yt-tabla">
          <div className="yt-fila yt-cabeza" style={sube(lt, 0.4)}>
            {t.columnas.map((c) => <span key={c}>{c}</span>)}
          </div>
          {P.filas.map((x, i) => (
            <div key={x.es[0]} className="yt-fila" style={sube(lt, 1.6 + i * paso)}>
              <span className="f">{x[l][0]}</span>
              <span className="q">{x[l][1]}</span>
              <span className="c">{x[l][2]}</span>
            </div>
          ))}
        </div>
      </div>
    ),
  });

  // 4 · La familia: sus agentes y Rostrum.
  const bots = [...agentes.map((a) => a.id), 'rostrum'];
  const nombre = (id) => (id === 'rostrum' ? 'Rostrum' : agentes.find((a) => a.id === id).nombre);
  lista.push({
    dura: 7,
    render: (lt) => (
      <div>
        <Eyebrow>{`Criterio ${sigla.toUpperCase()}`}</Eyebrow>
        <h2 className="yt-h2" style={sube(lt, 0.3)}>{t.familia(agentes.length)}</h2>
        <div className="yt-bots">
          {bots.map((id, i) => (
            <div key={id} className="yt-bot" style={sube(lt, 1 + i * 0.5)}>
              <Robot kind={id} vivo />
              <p className="n">{nombre(id)}</p>
              <p className="r">{imp.roles[id]}</p>
            </div>
          ))}
        </div>
      </div>
    ),
  });

  // 5 · Cada agente: quién es, lo que hace y lo que detecta, con las señales que más casos tienen.
  for (const a of agentes) {
    const ids = a.senales.map((s) => s.id);
    const casos = casosDe(sigla, ids);
    const top = [...a.senales].sort((x, y) => casosDe(sigla, [y.id]) - casosDe(sigla, [x.id])).slice(0, 3);
    lista.push({
      dura: 22,
      render: (lt) => (
        <div className="yt-agente">
          <div className="yt-quien" style={sube(lt, 0.2)}>
            <div className="yt-bot grande"><Robot kind={a.id} vivo /></div>
            <p className="yt-nombre">{a.nombre}</p>
            <p className="yt-rol">{a.rol[l]} · {imp.roles[a.id]}</p>
            <p className="yt-origen" style={sube(lt, 1.2)}>{a.origen[l]}</p>
          </div>
          <div className="yt-que">
            <Eyebrow><span style={sube(lt, 1.6)}>{t.hace}</span></Eyebrow>
            <p className="yt-hace" style={sube(lt, 2)}>{a.hace[l]}</p>
            <div style={sube(lt, 7)}>
              <Eyebrow>{t.detecta}</Eyebrow>
              <p className="yt-conteo">{t.senales(a.senales.length)} · {t.casos(fmt(casos))}</p>
            </div>
            <ul className="yt-senales">
              {top.map((s, i) => (
                <li key={s.id} style={sube(lt, 9 + i * 2.6)}>
                  <span>{s[l]}</span>
                  <b>{fmt(casosDe(sigla, [s.id]))}</b>
                </li>
              ))}
            </ul>
          </div>
        </div>
      ),
    });
  }

  // 6 · Rostrum, al final: lo mismo que dice en la impresora de la familia.
  const rostrum = imp.guion.find((g) => g.quien === 'rostrum');
  lista.push({
    dura: 13,
    render: (lt) => (
      <div className="yt-agente">
        <div className="yt-quien" style={sube(lt, 0.2)}>
          <div className="yt-bot grande"><Robot kind="rostrum" vivo /></div>
          <p className="yt-nombre">Rostrum</p>
          <p className="yt-rol">{imp.roles.rostrum}</p>
          <p className="yt-origen" style={sube(lt, 1.2)}>{ROSTRUM.origen[l]}</p>
        </div>
        <div className="yt-que">
          <Eyebrow><span style={sube(lt, 1.6)}>{t.hace}</span></Eyebrow>
          <p className="yt-hace" style={sube(lt, 2)}>{rostrum.texto}</p>
        </div>
      </div>
    ),
  });

  // 7 · La prueba: el piso que cita la portada y dónde se probó.
  const piso = pisoDe(sigla);
  const r = resumenPrueba(sigla);
  if (piso) {
    lista.push({
      dura: 12,
      oscuro: true,
      render: (lt) => (
        <div>
          <Eyebrow oscuro>{t.prueba}</Eyebrow>
          <div className="yt-piso" style={sube(lt, 0.4, 0.9)}>
            <p className="yt-valor grande">{pct(piso.piso)}</p>
            <p className="yt-corto">{t.piso}</p>
          </div>
          <div className="yt-tres">
            {[[fmt(r.senales[1]), t.casos('').trim()], [fmt(r.entidades), t.entidades], [fmt(r.paises), t.paises]].map(([v, k], i) => (
              <div key={k} style={sube(lt, 2.4 + i * 0.8)}>
                <p className="v">{v}</p>
                <p className="k">{k}</p>
              </div>
            ))}
          </div>
          {r.controles[1] ? <p className="yt-nota" style={sube(lt, 5.5)}>{t.controles(r.controles[0], r.controles[1])}</p> : null}
        </div>
      ),
    });
  }

  // 8 · Cómo se instala: los mismos tres pasos y comandos de la página de la familia.
  const pasos = PASOS_INSTALAR[l];
  const code = SETUP_FAMILIAS[sigla][l].code;
  lista.push({
    dura: 13,
    render: (lt) => (
      <div>
        <Eyebrow>{pasos.eyebrow}</Eyebrow>
        <ol className="yt-pasos">
          {[pasos.marketplace, pasos.familia, pasos.configurar].map((p, i) => (
            <li key={p} style={sube(lt, 0.6 + i * 2.4)}>
              <span className="i">{i + 1}</span>
              <div>
                <p className="p">{p}</p>
                <code>{code[i][0]}</code>
              </div>
            </li>
          ))}
        </ol>
      </div>
    ),
  });

  // 9 · El cierre.
  lista.push({
    dura: 7,
    oscuro: true,
    sinMarca: true,
    render: (lt) => (
      <div className="yt-centro">
        <div className="yt-logo" style={sube(lt, 0.2)}><CriterioLogo locale={l} sigla={sigla} oscuro /></div>
        <p className="yt-url" style={sube(lt, 0.9)}>josenanez.com/agents/criterio-{sigla}</p>
        <p className="yt-pie" style={sube(lt, 1.4)}>{t.version(versionDe(sigla))} · {t.licencia}</p>
      </div>
    ),
  });
  return lista;
}

const q = new URLSearchParams(location.search);
const idioma = q.get('l') === 'en' ? 'en' : 'es';
const familia = q.get('f') in AGENTES ? q.get('f') : 'cfo';
const ESCENAS = escenas(familia, idioma);
const INICIOS = ESCENAS.reduce((a, e) => [...a, a[a.length - 1] + e.dura], [0]);
const TOTAL = INICIOS[INICIOS.length - 1];
const FUNDIDO = 0.45;

function Video() {
  const [t, setT] = useState(0);
  window.__duracion = TOTAL;
  window.__ir = (s) => {
    flushSync(() => setT(s));
    // Los gestos de los robots, en ese mismo segundo.
    for (const a of document.getAnimations()) {
      a.pause();
      a.currentTime = s * 1000;
    }
  };
  const i = Math.max(0, INICIOS.findIndex((x, k) => t >= x && t < INICIOS[k + 1]));
  const e = ESCENAS[i];
  const lt = t - INICIOS[i];
  // Cada escena entra y sale fundida; la primera ya está al empezar.
  const opacidad = Math.min(i === 0 ? 1 : entre(lt / FUNDIDO), entre((e.dura - lt) / FUNDIDO));
  return (
    <div className={`yt ${e.oscuro ? 'oscuro' : ''}`}>
      <div className="yt-escena" style={{ opacity: opacidad }}>{e.render(lt)}</div>
      {e.sinMarca ? null : (
        <div className="yt-marca">
          <CriterioSimbolo size={30} color={e.oscuro ? '#d5a84b' : '#8a6327'} />
          <span>Criterio {familia.toUpperCase()}</span>
        </div>
      )}
      <div className="yt-avance" style={{ width: `${(100 * t) / TOTAL}%` }} />
    </div>
  );
}

createRoot(document.getElementById('root')).render(<Video />);
