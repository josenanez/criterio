# /criterio-project:pm-publish confirmar

Publiqué la ficha en `/home/claude/banco/ronda-10/retail/espacio/documentos/proyectos/PRY-206-precios-dinámicos/00-gobierno/ficha-pm.json`, con corte al 2026-10-18. Es una copia tal cual del registro que `compute` acababa de recalcular, porque el script no tiene subcomando de publicación.

**Lleva:** 17 campos con dato · 3 sin decir en ninguna parte (`identity.product`, `identity.authority`, `identity.phase`) · declara **rojo** al 2026-10-15, con 47 % de avance.

**Lo más viejo que va ahí:** los campos de identidad, `plan.start_date`, `plan.scope_summary` y `money.approved`, todos del acta del 2026-04-05. Tienen 196 días, así que no pasan de un año.

**Fecha de cierre:** `plan.end_date` es 2027-01-05. Sale del cronograma v2 (2026-10-15), el más reciente, y coincide con la línea base v2 que aprobó CC-01. La fecha original (2026-11-13) va en `plan.baseline`.

**Para tener presente antes de que la PMO la lea:**
- **Hitos sin evidencia:** tres figuran como cumplidos sin acta de recibo: Diseño de la experiencia, Integración con el ERP y Piloto en tiendas.
- **CC-01:** dice «el comité» sin decir cuál ni quién firmó.
- **CT-980:** Tecnología para Tiendas Ltda. tiene 599.677.238 COP facturados sin ningún entregable aceptado.
- **Avance:** el 47 % declarado queda por debajo de lo que sustenta el plan (80–100 %).

**Términos:** ya estaban vigentes (v0.5.0), aceptados por José Francisco Ñáñez el 2026-10-18, así que no hizo falta registrarlos de nuevo.

**Corrida:** quedó registrada como `2026-10-18-pm-publish-1`, con 22 señales, y la salida está en `estado/PRY-206-precios-dinámicos/corridas/salida-pm-publish.md`.