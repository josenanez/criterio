import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import { CriterioFamily } from './CriterioFamily';
import { IMPRESORA } from './lib/criterioImpresora';

// La tarjeta final del video de cada familia que tiene video. Las cifras son las de la evidencia
// publicada —la PMO, de tests/evidencias/rondas; la CFO, de tests/evidencias/familias/cfo y de su
// material—: si cambian, se cambian aquí y se vuelve a grabar.
const FINALES = {
  pmo: {
    es: { k: 'Criterio PMO · versión 0.5.0', a: '10 rondas de prueba · 4 industrias', b: '520 proyectos · 5.137 documentos', c: '1.480 ejecuciones de 37 comandos', d: 'Código abierto · Apache 2.0', u: 'josenanez.com/agents/criterio-pmo' },
    en: { k: 'Criterio PMO · version 0.5.0', a: '10 test rounds · 4 industries', b: '520 projects · 5,137 documents', c: '1,480 runs of 37 commands', d: 'Open source · Apache 2.0', u: 'josenanez.com/agents/criterio-pmo' },
  },
  cfo: {
    es: { k: 'Criterio CFO · versión 0.12.0', a: '5 países · 4 industrias', b: '15 entidades · 991 documentos', c: 'Clara, Tomás y Áurea · 22 comandos', d: 'Código abierto · Apache 2.0', u: 'josenanez.com/agents/criterio-cfo' },
    en: { k: 'Criterio CFO · version 0.12.0', a: '5 countries · 4 industries', b: '15 entities · 991 documents', c: 'Clara, Tomás and Áurea · 22 commands', d: 'Open source · Apache 2.0', u: 'josenanez.com/agents/criterio-cfo' },
  },
};

const q = new URLSearchParams(location.search);
const idioma = q.get('l') === 'en' ? 'en' : 'es';
// Las familias son las que el portal publica en su impresora: una nueva se graba sin tocar esto.
const familia = q.get('f') in IMPRESORA ? q.get('f') : 'pmo';
const t = (FINALES[familia] || FINALES.pmo)[idioma];

createRoot(document.getElementById('root')).render(
  <div id="frame">
    <CriterioFamily locale={idioma} familia={familia} />
    <div id="end"><div className="in">
      <p className="k">{t.k}</p>
      <p className="big">{t.a}</p><p className="big">{t.b}</p><p className="big">{t.c}</p>
      <p className="d">{t.d}</p><p className="u">{t.u}</p>
    </div></div>
  </div>,
);
