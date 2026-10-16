# /criterio-project:pm-publish confirmar

Publiqué la ficha en `documentos/proyectos/PRY-211-cobranza-digital/00-gobierno/ficha-pm.json`, con corte al 2026-10-16. Es una copia exacta de `estado/PRY-211-cobranza-digital/records/PRY-211.json` y es JSON válido.

**Lleva:** 19 campos con dato · 2 sin decir en ninguna parte (`identity.authority` e `identity.phase`) · declara **verde** al 2026-10-13, con 89 % de avance.

**Lo más viejo que va ahí:** 12 campos del acta de constitución, del 2025-07-08, con 15 meses (pasa de un año). Entre ellos están patrocinador, gerente, comité, producto, fecha de fin y presupuesto aprobado, seis de los ocho campos que la PMO contrasta.

**El verde lo contradice el cálculo.** Dejó 16 alertas:
- Hay 2 hitos marcados como cumplidos sin evidencia.
- La proyección de costo supera lo aprobado en 15,5 %.
- Hay 7 compromisos vencidos y 3 sin fecha.
- Hay 2 compromisos reprogramados 4 y 6 veces.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo. La carpeta de gobierno ya existía, así que no hubo que crearla. No toqué ningún otro archivo ni avisé a nadie.

La ficha todavía lleva la nota "Sin sellar" de `pm-setup`; este comando no la sella.

La corrida quedó registrada como `2026-10-16-pm-publish-1`, con la salida completa en `estado/PRY-211-cobranza-digital/corridas/salida-pm-publish.md`.