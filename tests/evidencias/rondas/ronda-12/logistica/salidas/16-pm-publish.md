# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-204 en `/home/claude/r12/logistica/espacio/documentos/proyectos/PRY-204-cross-docking-en-el-puerto/00-gobierno/ficha-pm.json`, con corte al 2026-10-28.

- **Contenido:** lleva 15 campos con dato y 2 sin decir en ninguna parte (`identity.authority` e `identity.phase`). Declara **verde** al 2026-10-28.
- **Lo más viejo:** 13 campos de identidad, plan y `money.approved` vienen del acta de constitución y del cronograma v1, ambos del 2025-10-13. Ya pasan de un año.
- **Fecha de cierre:** `plan.end_date` es 2027-01-14. Es el único cronograma que hay y coincide con la línea base, así que no hay diferencia que corregir.
- **Lo que la PMO va a ver primero:** el verde no lo sostienen las señales.
  - El avance declarado es 53 % y el plan sostiene entre 75 % y 100 %.
  - El hito «Diseño de la operación aprobado» figura cumplido sin evidencia.
  - Hay 5 compromisos vencidos sin evidencia, 2 sin fecha y 3 reprogramados, uno de ellos 6 veces.
- **Términos:** ya estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no los registré de nuevo.
- **Cómo se publicó:** `portafolio.py` no tiene un subcomando de publicación, así que copié tal cual la ficha ya recalculada (`records/PRY-204.json`) a esa ruta. Tomé el argumento «confirmar» como el sí a la publicación.
- **Corrida:** la registré como `2026-10-28-pm-publish-1`, con la salida completa en `estado/PRY-204-cross-docking-en-el-puerto/corridas/salida-pm-publish.md`.