# /criterio-product:product-requirements 

El registro de PRD-303 (Tarjeta débito) tiene 16 requerimientos: 11 aceptados, 5 propuestos y ninguno en otro estado. Salieron 39 hallazgos, y los 16 tienen al menos uno. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.

Lo leí en el orden de lectura de product-health:

- **Se va a construir y nadie lo pidió:** REQ-4300, 4307, 4309 y 4314 están aceptados sin ninguna cita de quien los pidió.
- **Decidido y nadie lo construye:** los 11 aceptados no tienen proyecto que los ejecute, es decir 0 %. El más viejo, REQ-4307, se aceptó el 2026-04-28.
- **Sin doliente:** REQ-4303, 4309, 4313 y 4314 figuran como «sin asignar».
- **Sin criterio de aceptación:** REQ-4303 y REQ-4305. REQ-4310 tampoco tiene, pero está propuesto y no se le exige.
- **Lleva meses y nadie lo decide:** los 5 propuestos pasan el umbral de 60 días. REQ-4306 lleva 175 días, 4312 lleva 154, 4310 lleva 116, 4308 lleva 104 y 4302 lleva 82. La facultad de decidir es del Comité de producto, según la configuración. El acta del 2026-10-05 solo dice «Se mantiene el plan».
- **Evidencia vieja:** 12 requerimientos se apoyan en la misma entrevista, del 2025-09-12, de hace 13 meses; el umbral es 12. Esa entrevista no nombra ninguno de ellos. Por eso el 63,6 % con evidencia sobreestima lo que los documentos sostienen.

Dos cosas más que conviene saber:

- **Decisiones sin documento propio:** las 11 aceptaciones citan la misma acta, con un solo asistente (Sandra Gil), y el acta no dice quién aceptó cada una. El cálculo no lo marca como señal; es una observación mía.
- **Supuesto sin verificar:** «El proveedor cumple el tiempo pactado» lleva 158 días sin verificarse.

No son hallazgo: la brecha del volumen mensual (2,5 %, bajo el umbral de 20 %) y las diferencias de forma en los propuestos.

Los 16 requerimientos se llaman «Requerimiento REQ-43xx» en el acta, sin título real, así que las tablas no dicen de qué trata cada uno.

Ofrezco `/product-trace` por los 11 aceptados sin proyecto. `/product-charter` no aplica todavía: ningún aceptado tiene a la vez evidencia, criterio y doliente confirmados.

La salida y la corrida quedaron en `estado-producto/PRD-303/corridas/` (`salida-product-requirements.md` y `2026-10-15-product-requirements-1`).