# Criterio · catálogo 1.5.0 · 30 de octubre de 2026

La familia CLO sube a su 1.1.0 con los contratos públicos. Cuando la entidad es pública, Fidel revisa cada contrato contra la ley de contratación pública de su país: si se publicó a tiempo y si la garantía de cumplimiento cumple lo que la ley fija. Código abierto bajo Apache 2.0.

**El número del catálogo solo ordena las entradas del registro de versiones.** La versión de cada familia es la suya.

## Qué trae

| | |
|---|---|
| **La ley, no una opinión** | Cada regla sale del registro de países y tiene su fuente verificada, de la F-03 a la F-10 de la familia. El motor compara la ficha del contrato con la regla; no opina sobre el contrato |
| **La publicación** | Colombia: en el SECOP, dentro de 3 días hábiles. Chile: el trato directo, dentro de 24 horas. Brasil: en el PNCP, dentro de 20 días hábiles si hubo licitación o de 10 si fue contratación directa |
| **La garantía de cumplimiento** | Colombia: al menos el 10 % del valor. Ecuador: el 5 %, desde el umbral. Perú: el 10 % del monto original. Chile: el 5 %, desde el umbral. Brasil: hasta el 5 %, o hasta el 10 % si está justificada. México: entregada dentro de los 10 días naturales siguientes a la firma |
| **CLO 1.1.0 · Fidel** | La ronda 7, sobre una entidad pública por país: 19 de 19 señales, ninguna de más, y 909 de 912 datos. Encontró dos defectos: la clave (CLO-13) y una instrucción del skill (CLO-14). Los dos quedaron corregidos y verificados. Con todas sus rondas, el piso del margen del 95 % es 97,0 % en señales y 99,7 % en datos |

## Las versiones en la 1.5.0

| Familia | Versión | Calidad | Lanzamiento |
|---|---|---|---|
| PMO · Vera, Samuel y Alba | 1.0.0 | Estable | Semana del 19 de octubre |
| CFO · Clara, Tomás y Áurea | 1.0.0 | Estable | Semana del 26 de octubre |
| CLO · Fidel y Constanza | **1.1.0** | Estable | Sin lanzar |
| EA · Ofelia | 1.0.0 | Estable | Semana del 26 de octubre |
| CCO · Augusto y Valeria | 0.3.0 | Estable | Sin lanzar |
| Rostrum | 1.0.0 | — | — |

En esta entrada se libera la CLO.

## Si ya la tienes instalada

Actualiza `criterio-legal` y `criterio-compliance`. Cada agente te pide aceptar los términos de su versión nueva y deja su comprobante en `.criterio/terminos/`. Si tu entidad es pública, vuelve a correr `/criterio-legal:legal-setup`: te pregunta si lo es y, en Ecuador y en Chile, el umbral de la garantía.
