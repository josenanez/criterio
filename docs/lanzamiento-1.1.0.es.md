# Criterio · catálogo 1.1.0 · 29 de octubre de 2026

La familia PMO abre su 1.0.0: está lanzada desde la semana del 19 de octubre y es estable, y una familia lanzada y estable sube a la 1.0.0 en su versión siguiente (decisión 0021). Rostrum, el servidor de todas las familias, sube con ella a su 1.0.0. Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** Pasa a la 1.1.0 porque es la entrada siguiente a la 1.0.0. La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **PMO 1.0.0** | Dos industrias nuevas, telecomunicaciones y logística, probadas con los 38 comandos de Vera, Samuel, Alba y Rostrum: 38 de 38 contratos cumplidos en cada una, Vera 119 de 119 señales y ninguna de más, Samuel 52 de 52 compromisos, Alba 61 de 61 alertas. La familia queda probada en ocho industrias |
| **La PMO se mide como las demás familias** | Su calidad sale de la corrida más reciente de cada industria, sea de la ronda que sea: las seis industrias anteriores con su corrida de la ronda 11 y las dos nuevas con la de la ronda 12. Sobre 500 señales, el piso del margen del 95 % de Vera es 99,2 % en precisión y en cobertura; Samuel, 98,2 %; Alba, 98,5 % |
| **Rostrum 1.0.0 · el cronograma** | En la página de cada proyecto, el Gantt de cada línea base aprobada contra el plan vigente, cada hito con su fecha de línea base, su fecha vigente y su estado en palabras, y la curva de avance por hitos con el avance declarado como un punto aparte. El motor calcula el cronograma y el informe solo lo dibuja, con la misma información en una tabla |
| **El cronograma, probado en las ocho industrias** | `tests/cronograma.py` dibuja cada proyecto con las fichas que escribieron los agentes en la corrida más reciente de cada industria, sin correr ningún agente: 104 proyectos, 130 líneas base y 365 hitos, y ninguna diferencia entre lo dibujado y lo calculado. Es una puerta de `scripts/verificar.py`. Rostrum pasó 1.072 de 1.072 comprobaciones en la ronda 12 |

## Las versiones en la 1.1.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | **1.0.0** | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | 0.12.1 | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | 0.12.1 | Estable | Sin lanzar |
| EA · Ofelia | 0.12.1 | Laboratorio | Semana del 26 de octubre |
| CSO · Augusto y Valeria | 0.1.0 | Laboratorio | Sin lanzar |
| Rostrum | **1.0.0** | — | — |

En esta entrada se liberan la PMO y Rostrum.

## Si ya la tienes instalada

Actualiza `criterio-portfolio`, `criterio-project`, `criterio-product` y `criterio-server`. Cada agente te pide aceptar los términos de su versión nueva y deja su comprobante en `.criterio/terminos/`. Las fichas que ya tienes sirven como están: el cronograma se calcula de ellas.
