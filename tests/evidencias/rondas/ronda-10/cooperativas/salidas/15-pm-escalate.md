# /criterio-project:pm-escalate 

Armé el paquete de escalamiento de PRY-201 con un solo punto formulado como decisión: el acta no declara la autoridad de la gerente, y ese es el primer punto que escala.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no registré nada nuevo. No había tema en el argumento, por lo que usé lo que la ficha ya marca como escalable.

**La decisión:** ¿confirma el Comité de Crédito, por escrito, qué puede decidir sola Natalia Ospina en alcance, fechas y presupuesto?
- **Recomiendo** una adenda al acta que lo declare (opción A). Cuesta una sesión del comité.
- **Costos:** las opciones no llevan cifras en pesos ni días, porque ningún documento las da.
- **Fecha:** no hay vencimiento en los documentos. Puse como fecha límite el comité del 2026-11-01, que sale de la configuración.

Cumplen el criterio de escalamiento pero no quedaron como paquete, porque todavía no tienen una pregunta cerrada:
- **Presupuesto:** la proyección es 18.779.394.290 COP contra 18.000.000.000 aprobados, 4,33 % por encima. El informe sigue declarando verde. Sin autoridad declarada no se puede decir si esto escala.
- **Hito vencido:** la integración con el core cooperativo, que es también la fecha de cierre, venció el 2026-10-04 y sigue pendiente, sin nueva fecha.
- **Compromisos reprogramados:** Beatriz Cuéllar lleva 5 reprogramaciones (89 días), Paula Céspedes 5 (61 días) y Diana Molina 4 (54 días). Conviene llamarlos antes de escalar.
- **Riesgo sin registrar:** que el proveedor no llegue con el equipo completo. Se comentó en la reunión y nadie lo anotó.

No calculé a quién alcanza el cambio, porque ningún documento propone cuántos días se mueve algo. Cuando exista una fecha nueva para la integración con el core, corre `/pm-escalate cambio <fecha>`. Sospecho que PRY-202 (Core cooperativo) queda alcanzado, pero no lo verifiqué.

La salida quedó en `salida-pm-escalate.md` y la corrida se registró como `2026-10-18-pm-escalate-1`, con 37 segundos medidos y 14 señales abiertas.

Archivos en `/home/claude/banco/ronda-10/cooperativas/espacio/estado/PRY-201-apertura-de-ahorro-en-línea/corridas/`:
- `salida-pm-escalate.md`