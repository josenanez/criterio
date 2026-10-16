# /criterio-portfolio:change-control PRY-200 mover la salida a producción 30 días

No se puede aprobar ni registrar el cambio de PRY-200: faltan el solicitante, el motivo y quién tiene autoridad para aprobarlo. La solicitud es mover la salida a producción de 2027-02-27 a 2027-03-29, y eso también mueve el cierre del proyecto. Los términos (v1.1) ya estaban vigentes a nombre de José Francisco Ñáñez, fecha 2026-10-16, así que no los registré de nuevo.

- **Alcance y costo:** no hay impacto declarado. Alguien absorbe ese mes sin presupuesto adicional o recortando calidad. La proyección al 2026-10-15 deja 534.097.619 COP de holgura sobre los 6.800.000.000 aprobados, pero no incluye el mes extra. No hay un costo mensual en los documentos, así que no lo calculé.
- **Portafolio:** el cálculo no encuentra proyectos afectados (0 directos y 0 indirectos). Eso se debe a que el acta declara «Ninguna declarada» en dependencias, no a que no existan. El acta tampoco dice qué proyecto cubre lo que queda fuera de alcance. Hay que preguntarle a Ricardo Salas, gerente del proyecto, si algo espera esta salida.
- **Piloto con usuarios internos:** está en el camino del cambio (2026-12-03). No calculé cuántos días se mueve, porque eso requiere holgura por actividad y la ficha no la tiene.
- **Quién decide:** el acta no declara autoridad para aprobar cambios, y ese es el hallazgo de fondo. Por defecto va al Comité de Arquitectura. El comité del 2026-10-16 no registra esta solicitud.
- **Si se aprueba:** quedaría la línea base 2 con cierre 2027-03-29 y la v1 intacta. Ese registro lleva el motivo en blanco hasta que alguien lo dé. La desviación contra la original sería de +30 días en tiempo y sin variación de costo declarada.
- **Hallazgo aparte:** el hito «Integración con el core» figura cumplido sin evidencia de recibo. Los entregables de los contratos CT-936 y CT-107 figuran pendientes sin evidencia, aunque ambos contratos están facturados por el monto de un entregable. Lo dejé anotado sin revisarlo a fondo; le corresponde a `vendor-tracking`.

No generé el paquete de comité, y los contratos no traen cláusula de vigencia que permita decir si cubren hasta 2027-03-29. Como no hay interfaz, la oferta final de llevarlo a comité queda como siguiente paso para quien reciba esto.

La corrida quedó registrada como `2026-10-16-change-control-1` (42 segundos, caso PRY-200). El texto completo está en `estado/corridas/salida-change-control.md`.