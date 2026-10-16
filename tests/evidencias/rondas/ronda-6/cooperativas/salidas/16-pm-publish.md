# /criterio-project:pm-publish confirmar

Publiqué la ficha en `/home/claude/banco/ronda-6/cooperativas/espacio/documentos/proyectos/PRY-210-corresponsales-rurales/00-gobierno/ficha-pm.json`, con corte al 2026-10-16.

**Lleva:** 18 campos con dato · 3 sin decir en ninguna parte (producto, autoridad, fase) · declara **verde** al 2026-10-13.

**Lo más viejo que va ahí:** identidad, alcance, presupuesto aprobado y fechas, del 2026-06-14 (acta de constitución y cronograma v1), cuatro meses. Nada pasa de un año.

**Lo que revisé antes de escribir:**
- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16). No los registré de nuevo.
- **Fecha de cierre:** `plan.end_date` es 2027-08-30. No hay un cronograma más nuevo que el v1, y su último hito cae en esa misma fecha, así que coincide con la línea base.
- **Carpeta de gobierno:** ya existía, no creé nada.

**Lo primero que verá la PMO:** el estado declarado es verde, con 47 % de avance. El recálculo lo contradice con cuatro señales:
- El avance declarado está 22 puntos por encima de lo que el plan sustenta (0 de 4 hitos cumplidos).
- El hito «Diseño funcional aprobado» venció hace 6 días (2026-10-10).
- Hay 3 compromisos vencidos.
- Hay 2 compromisos reprogramados 4 y 5 veces.

La ficha marca el estado como declaración tuya, no como evidencia.

**Dos cosas más:**
- **Ficha sin sellar:** se leyó el historial de reuniones, no el proyecto entero.
- **Copia sin cambios:** es idéntica a la de tu carpeta de estado, sin campos fuera del esquema.

El script no tiene un subcomando de publicación, así que copié el archivo con `cp`.

La salida quedó en `estado/PRY-210-corresponsales-rurales/corridas/salida-pm-publish.md`. La corrida quedó registrada como `2026-10-16-pm-publish-1`.