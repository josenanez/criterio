import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import { CriterioFamily } from './CriterioFamily';

// La tarjeta final del video. Las cifras son las de la evidencia publicada
// (tests/evidencias/rondas): si cambian, se cambian aquí y se vuelve a grabar.
const FINAL = {
  es: { k: 'Criterio PMO · versión 0.5.0', a: '10 rondas de prueba · 4 industrias', b: '520 proyectos · 5.137 documentos', c: '1.480 ejecuciones de 37 comandos', d: 'Código abierto · Apache 2.0', u: 'josenanez.com/agents/criterio-pmo' },
  en: { k: 'Criterio PMO · version 0.5.0', a: '10 test rounds · 4 industries', b: '520 projects · 5,137 documents', c: '1,480 runs of 37 commands', d: 'Open source · Apache 2.0', u: 'josenanez.com/agents/criterio-pmo' },
};

const idioma = new URLSearchParams(location.search).get('l') === 'en' ? 'en' : 'es';
const t = FINAL[idioma];

createRoot(document.getElementById('root')).render(
  <div id="frame">
    <CriterioFamily locale={idioma} />
    <div id="end"><div className="in">
      <p className="k">{t.k}</p>
      <p className="big">{t.a}</p><p className="big">{t.b}</p><p className="big">{t.c}</p>
      <p className="d">{t.d}</p><p className="u">{t.u}</p>
    </div></div>
  </div>,
);
