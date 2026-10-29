# 0021 · Se publica desde la primera versión, se lanza en una fecha, y el lanzamiento abre la 1.0

**Fecha:** 2026-10-28 · **Estado:** aceptada el 2026-10-28 · **Modifica:** 0020

## Contexto

Hasta esta decisión, publicar y lanzar eran lo mismo. Una familia que no estaba liberada no salía ni
en el marketplace ni en el portal, y una que salía quedaba marcada en el mapa de agentes como «Corre
hoy». Dos problemas salían de ahí:

- **El trabajo esperaba al anuncio.** El diseño, el desarrollo, las pruebas y la documentación de una
  familia no se podían subir al portal hasta el día de su lanzamiento.
- **El mapa decía más de lo que había pasado.** Cuatro familias marcaban «Corre hoy», y solo la PMO
  se había lanzado: la semana del 19 de octubre.

Además, una familia en construcción no se podía instalar con `claude plugin install …@criterio`, que
es como se instala la ronda con los agentes.

Y la regla de diez versiones por entero (decisión 0020) haría que una familia nueva, como la CSO,
necesitara nueve versiones, cada una con su ronda completa con los agentes, antes de llegar a su
1.0.

## Decisión

### 1. Tres datos de cada familia, y cada uno lo dice alguien distinto

| Dato | Quién lo dice | Valores |
|---|---|---|
| La etapa | El código | Construida, probada, ampliando |
| La calidad | La evidencia, con `scripts/calidad.py` (decisión 0020) | Laboratorio o estable |
| **El lanzamiento** | **Quien lanza la familia: es el único dato que se escribe a mano** | La semana del lanzamiento, en `lanzamiento` de su `familia.json` |

### 2. Se publica desde la primera versión

Una familia entra al marketplace y al portal con su primera liberación en el registro, aunque sea de
laboratorio y no se haya lanzado. Quien la encuentra la puede instalar, la ve marcada como laboratorio
y acepta sus términos, como con cualquier versión.

### 3. Se lanza en una fecha

`lanzamiento` lleva la semana del lanzamiento, como una fecha AAAA-MM-DD. Mientras no la tenga, la
familia aparece en el mapa de agentes como «Siguiente». Desde esa semana, como «Corre hoy». El
titular de la página de agents cuenta las familias lanzadas, no las publicadas.

Solo se lanza lo que está publicado: `scripts/registro.py verificar` falla con una familia que tenga
fecha de lanzamiento y ninguna versión liberada.

### 4. El lanzamiento abre la 1.0

**Una familia lanzada sube a la 1.0.0 en su primera versión estable, venga de la 0.y que venga.**

- Antes de su lanzamiento, una familia recorre su década como dice la decisión 0020: 0.1, 0.2… Si
  llega a la 0.9 sin lanzarse, la siguiente es la 1.0.
- La semana de su lanzamiento, si es estable, su versión es la 1.0.0. Si es de laboratorio, se lanza
  con su 0.y, y su primera versión estable después del lanzamiento es la 1.0.0.
- Una corrección, el tercer número, sí puede salir antes de abrir la 1.0.
- `scripts/registro.py liberar` falla si una familia lanzada y estable que está en una 0.y no sube a
  la 1.0.0.

El número del catálogo solo ordena las entradas del registro: sigue la regla de diez versiones por
entero, sin relación con el lanzamiento de ninguna familia.

### 5. La PMO se mide como las demás familias

La calidad de la PMO sale de la corrida más reciente de cada industria, sea de la ronda que sea, y
no solo de su ronda más reciente: es la regla de la decisión 0020 para las demás familias. Una ronda
que agrega industrias corre en ellas los 38 comandos y no obliga a repetir las que ya pasaron. La
ronda 12, la de la 1.0.0, corre telecomunicaciones y logística; las seis anteriores siguen con su
corrida de la ronda 11, y el motor se prueba sobre todo el material con cada cambio.

## Las familias hoy

| Familia | Lanzamiento | Calidad | La versión siguiente |
|---|---|---|---|
| PMO | Semana del 2026-10-19 | Estable | 1.0.0 |
| CFO | Semana del 2026-10-26 | Estable | 1.0.0 |
| CLO | Sin lanzar | Estable | 1.0.0, por la excepción de la 0.12 |
| EA | Semana del 2026-10-26 | Laboratorio | Se lanza con su 0.12.1; su primera versión estable, la 1.0.0 |
| CSO | Sin lanzar | Laboratorio | Se publica en la 0.1.0; la 0.2.0 trae su ronda |

## Consecuencias

- La CSO sale al marketplace y al portal con su versión 0.1.0: el motor probado, como laboratorio y
  sin lanzar. Su ronda con los agentes se instala igual que la de las demás familias, y pasa a la
  0.2.0, junto con un material que siembra al menos 73 señales.
- La CLO deja de marcar «Corre hoy» hasta la semana de su lanzamiento. Sigue publicada y se puede
  instalar. La EA se lanza la semana del 2026-10-26 con su versión de laboratorio.
- La decisión 0020 queda modificada en un punto: la CSO no tiene que recorrer su década completa para
  llegar a la 1.0; la abre su lanzamiento, si es estable.
