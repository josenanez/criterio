# /criterio-product:product-spec 

**Borrador de especificación — Cuenta PyME (PRD-303), 2026-10-15.** Lo cierra Beatriz Cuéllar; yo no apruebo.

No pude redactar el comportamiento de ninguno de los cinco requerimientos, y no lo inventé. Los cinco están aceptados (acta del 2026-10-13), pero ninguno trae necesidad escrita: el acta los titula solo «Requerimiento REQ-xxxx». La cobertura de la especificación es 0 de 5.

- **Términos:** ya estaban aceptados para esta versión (1.1, por José Francisco Ñáñez, 2026-10-15). No hizo falta pedirlos de nuevo.
- **Alcance:** en "Entra" van los cinco requerimientos. "No entra" deja todo comportamiento de la cuenta sin decidir, porque ninguna fuente lo dice.
- **Criterios de aceptación:** ninguno es verificable hoy. REQ-1030 a 1033 dicen «se verifica en producción», que no dice qué se verifica. REQ-2018 no tiene criterio.
- **Supuestos:** son tres, todos sin verificar.
  - «El segmento paga por esto».
  - Que la única entrevista, del 2025-08-11, sostiene cada requerimiento. Tiene 14 meses (el umbral es 12) y no nombra ningún requerimiento.
  - Que el volumen declarado (276.747) se sostiene. El medido es 246.553, una diferencia de 10,9%, bajo el umbral de 20%.
- **Vacíos, cada uno con dueño:**
  - La necesidad de cada requerimiento, que cierran los cinco dolientes.
  - Quién decidió el 2026-10-13: el acta solo dice «Se mantiene el plan».
  - La facultad de decidir (`authority`, vacía en la configuración).
  - Los casos borde.
  - Lo que deban hacer otros equipos.
  - El proyecto que ejecute cada requerimiento: hay 0 de 5.
  - El criterio de éxito del producto.

  Los que no son de un doliente los cierra Beatriz Cuéllar.
- **Normativa:** no corrí el barrido de obligaciones. La definición no dice qué hace la cuenta, así que no hay con qué acotar qué normas toca. Queda como vacío, sin dictamen de cumplimiento.
- **Siguiente paso:** no ofrezco `/product-charter` todavía. Primero deben escribir la necesidad de cada requerimiento y volver a correr `/product-spec`.

La corrida quedó registrada: 32 segundos, 5 requerimientos y 16 señales (`evidence_stale`, `decision_without_source` y `requirement_untraced` en los cinco, y `requirement_without_acceptance` en REQ-2018).

Archivos en `/home/claude/banco/ronda-2/bancos/espacio/estado-producto/PRD-303/corridas/`:
- `salida-product-spec.md`