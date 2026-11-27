// Los contornos del mapa de «Dónde se probó Criterio» (src/mapa.jsx): de México a la Patagonia, con el
// Caribe, proyectados una sola vez desde Natural Earth 1:50m (dominio público, por world-atlas) y
// guardados en src/mapa-contornos.json. El video no proyecta nada al grabar: dibuja estos trazos.
//
//   node mapa-contornos.mjs
//
// Cada país lleva su código ISO de dos letras cuando es uno de los que nombra lib/criterioPaises.ts, y
// su ancla: el centro de su parte más grande, donde llegan las líneas. Los Estados Unidos no se dibujan
// —el mapa empieza en la frontera de México—, y de un país con territorios lejos —Francia, los Países
// Bajos, el Reino Unido— solo entra lo que cae en el recuadro: la Guayana Francesa, las Antillas, las
// Malvinas.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { feature } from 'topojson-client';
import { geoMercator, geoPath, geoCentroid, geoArea } from 'd3-geo';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const mundo = JSON.parse(fs.readFileSync(path.join(AQUI, 'node_modules', 'world-atlas', 'countries-50m.json'), 'utf8'));

// ISO 3166-1 numérico → alfa-2, para los países de las rondas.
const ISO = { 170: 'CO', 218: 'EC', 604: 'PE', 152: 'CL', 484: 'MX', 76: 'BR', 32: 'AR', 591: 'PA', 320: 'GT', 188: 'CR', 340: 'HN', 600: 'PY' };
const RECUADRO = { oeste: -119, este: -30, norte: 33.5, sur: -56.5 };
const dentro = ([lon, lat]) => lon >= RECUADRO.oeste && lon <= RECUADRO.este && lat >= RECUADRO.sur && lat <= RECUADRO.norte;

const partes = [];
for (const f of feature(mundo, mundo.objects.countries).features) {
  if (Number(f.id) === 840) continue;
  const poligonos = f.geometry.type === 'Polygon' ? [f.geometry.coordinates] : f.geometry.type === 'MultiPolygon' ? f.geometry.coordinates : [];
  const quedan = poligonos.filter((p) => dentro(geoCentroid({ type: 'Polygon', coordinates: p })));
  if (!quedan.length) continue;
  partes.push({ id: Number(f.id), nombre: f.properties.name, geometry: { type: 'MultiPolygon', coordinates: quedan } });
}

const ANCHO = 1000;
const coleccion = { type: 'FeatureCollection', features: partes.map((p) => ({ type: 'Feature', geometry: p.geometry })) };
const proyeccion = geoMercator().fitWidth(ANCHO, coleccion);
const trazo = geoPath(proyeccion).digits(1);
const [[, y0], [, y1]] = trazo.bounds(coleccion);
proyeccion.translate([proyeccion.translate()[0], proyeccion.translate()[1] - y0]);
const alto = Math.ceil(y1 - y0);

const paises = partes.map((p) => {
  const mayor = p.geometry.coordinates.map((c) => ({ type: 'Polygon', coordinates: c })).sort((a, b) => geoArea(b) - geoArea(a))[0];
  const [x, y] = proyeccion(geoCentroid(mayor));
  return { iso: ISO[p.id] ?? null, nombre: p.nombre, d: trazo({ type: 'Feature', geometry: p.geometry }), ancla: [Math.round(x), Math.round(y)] };
});
const faltan = Object.values(ISO).filter((c) => !paises.some((p) => p.iso === c));
if (faltan.length) throw new Error(`Faltan en el mapa: ${faltan.join(', ')}`);

const salida = { fuente: 'Natural Earth 1:50m, dominio público, por world-atlas 2.0.2', ancho: ANCHO, alto, paises };
fs.writeFileSync(path.join(AQUI, 'src', 'mapa-contornos.json'), JSON.stringify(salida) + '\n');
console.log(`src/mapa-contornos.json · ${paises.length} países · ${ANCHO}×${alto} · ${Math.round(JSON.stringify(salida).length / 1024)} KB`);
