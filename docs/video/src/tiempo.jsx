import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { flushSync } from 'react-dom';
import { CriterioSimbolo } from './portal/CriterioLogo';

/* Lo que comparten los videos de YouTube —el de cada familia (youtube.jsx) y el de Criterio
   (criterio.jsx)—: cómo aparece lo que aparece, el texto que se escribe solo y el reloj.

   El tiempo no corre solo: grabar.mjs llama a window.__ir(segundo) cuadro por cuadro, y cada
   animación —también los gestos de los robots— se dibuja en ese segundo exacto. */

export const entre = (x) => Math.min(1, Math.max(0, x));
export const suave = (x) => 1 - (1 - x) ** 3;
export const avance = (lt, desde, dura) => suave(entre((lt - desde) / dura));
// Lo que aparece, aparece así: sube y se enciende en medio segundo.
export const sube = (lt, desde, dura = 0.5) => {
  const p = avance(lt, desde, dura);
  return { opacity: p, transform: `translateY(${(1 - p) * 28}px)` };
};
// El texto que se escribe solo, a tantos caracteres por segundo, con su cursor.
export const escribe = (texto, lt, desde, cps = 40) => texto.slice(0, Math.max(0, Math.floor((lt - desde) * cps)));
export const cursor = (texto, lt, desde, cps = 40) => (lt >= desde && escribe(texto, lt, desde, cps).length < texto.length ? <span className="yt-cursor" /> : null);

export function Eyebrow({ children, oscuro, style }) {
  return <p className={`yt-eyebrow ${oscuro ? 'oscuro' : ''}`} style={style}>{children}</p>;
}

const FUNDIDO = 0.35;

// Monta el video: las escenas en orden, cada una con su duración, fundidas, con la marca del pie y la
// barra de avance.
export function montar(escenas, marca) {
  const inicios = escenas.reduce((a, e) => [...a, a[a.length - 1] + e.dura], [0]);
  const total = inicios[inicios.length - 1];
  function Video() {
    const [t, setT] = useState(0);
    window.__duracion = total;
    window.__inicios = inicios;
    window.__ir = (s) => {
      flushSync(() => setT(s));
      // Los gestos de los robots, en ese mismo segundo.
      for (const a of document.getAnimations()) {
        a.pause();
        a.currentTime = s * 1000;
      }
    };
    const i = Math.max(0, inicios.findIndex((x, k) => t >= x && t < inicios[k + 1]));
    const e = escenas[i];
    const lt = t - inicios[i];
    // Cada escena entra y sale fundida; la primera ya está al empezar.
    const opacidad = Math.min(i === 0 ? 1 : entre(lt / FUNDIDO), entre((e.dura - lt) / FUNDIDO));
    return (
      <div className={`yt ${e.oscuro ? 'oscuro' : ''}`}>
        <div className="yt-escena" style={{ opacity: opacidad }}>{e.render(lt)}</div>
        {e.sinMarca ? null : (
          <div className="yt-marca">
            <CriterioSimbolo size={30} color={e.oscuro ? '#d5a84b' : '#8a6327'} />
            <span>{marca}</span>
          </div>
        )}
        <div className="yt-avance" style={{ width: `${(100 * t) / total}%` }} />
      </div>
    );
  }
  createRoot(document.getElementById('root')).render(<Video />);
}
