# /criterio-product:product-requirements 

## Registro — Alerta de taludes (PRD-301) · al 2026-10-17

El registro tiene 17 requerimientos: 12 aceptados y 5 propuestos. De los 12 decididos, el 83,3 % (10) tiene evidencia y ninguno tiene un proyecto que lo ejecute.

Los términos ya estaban vigentes (versión 0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

No hay carpeta de fichas de proyecto. El 0 % de proyecto sale de que el acta del comité del 2026-10-09 pone «—» en los 17 requerimientos, y ninguna ficha lo confirma ni lo desmiente. Todos los títulos son el genérico «Requerimiento REQ-xxxx», porque el acta no los describe.

En el orden de lectura de product-health:

1. **Se va a construir y nadie lo pidió:** REQ-2030 y REQ-4108, ambos aceptados y sin una sola cita de quien los pidió.
2. **Decidido y nadie lo construye:** los 12 aceptados. El más viejo es REQ-4105, aceptado desde el 2026-03-30, hace 201 días.
3. **Sin doliente:** REQ-4100 dice «sin asignar».
4. **Sin criterio de aceptación:** REQ-4101, 4104, 4105, 4107, 4109 y 4114. Los demás traen «se verifica en producción», que el cálculo cuenta como criterio aunque no sea medible.
5. **Decidido sin documento que lo respalde:** el cálculo no emite esta señal. El acta solo lista estados y una decisión, «Se mantiene el plan», con una sola asistente, Natalia Ospina. No dice quién aceptó cada requerimiento. Esto es una lectura mía de la forma del acta, no un hallazgo calculado.
6. **Lleva meses y nadie lo decide:** REQ-4103 (203 días), REQ-4102 (166) y REQ-4112 (130), contra un umbral de 60. La facultad de decidir es del Comité de producto, que los revisó el 2026-10-09 y no decidió ninguno.
7. **Evidencia vieja:** 14 requerimientos (10 aceptados y 4 propuestos) descansan en la misma entrevista del 2025-08-30, de hace 13 meses. Esa entrevista habla de un «Cliente entrevistado» y no nombra ninguno de ellos.

Fuera de los requerimientos:
- El supuesto «La red de la mina soporta el volumen» lleva 58 días sin verificar (umbral 30).
- La definición no declara criterio de éxito.
- El volumen mensual declarado (191.637) no tiene medición contra la que contrastarlo.

No hay requerimientos descartados, en construcción ni entregados. El registro solo ha crecido.

Como hay 12 decididos que nadie construye, el siguiente paso sería `/product-trace`. No ofrezco `/product-charter`: ningún aceptado cumple a la vez evidencia, criterio medible y doliente.

La corrida quedó registrada como `2026-10-17-product-requirements-1` (39 hallazgos, 31 segundos). La salida completa está en `estado-producto/PRD-301/corridas/salida-product-requirements.md`.