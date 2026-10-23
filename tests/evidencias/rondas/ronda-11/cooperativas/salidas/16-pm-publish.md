# /criterio-project:pm-publish confirmar

Publiqué la ficha en `documentos/proyectos/PRY-206-pagos-con-qr/00-gobierno/ficha-pm.json`, con corte al 2026-10-23.

Los términos ya estaban vigentes (versión 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23), así que no hubo que registrarlos de nuevo.

**Lleva:** 114 campos con dato · 5 sin decir en ninguna parte (autoridad, fase y la evidencia de los 3 hitos) · declara **amarillo** al 2026-10-19, con 79 % de avance.

**Lo más viejo que va ahí:** identidad, plan y presupuesto aprobado, todos del acta de constitución y el cronograma del 2025-06-06. Tienen 16 meses, más de un año.

**Fecha de cierre:** `plan.end_date` es 2025-12-31. No hay un cronograma más nuevo que el v1, así que la fecha vigente y la de la línea base coinciden. Esa fecha ya pasó hace casi 10 meses.

**Lo que la PMO va a ver:**
- Los 3 hitos figuran como cumplidos en el cronograma v1 sin ninguna evidencia de recibo.
- El 79 % declarado queda 21 puntos por debajo de lo que ese plan sostiene (100 %).
- Hay 4 compromisos vencidos, 5 sin fecha y 4 reprogramados 3 o más veces.

Patrocinador, gerente y comité vienen del acta de 2025. Si alguno cambió en una reunión, conviene corregirlo antes de que Vera lo contraste.

No hay un comando de publicación en el script, así que copié a mano `records/PRY-206.json` a la carpeta de gobierno. La carpeta ya existía.

Lo que mostré quedó en `estado/PRY-206-pagos-con-qr/corridas/salida-pm-publish.md`. La corrida quedó registrada como `2026-10-23-pm-publish-1`.