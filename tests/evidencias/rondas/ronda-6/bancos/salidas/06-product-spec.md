# /criterio-product:product-spec 

Escribí el borrador de especificación de Microseguros (PRD-306), pero sin la sección de comportamiento. Los 12 requerimientos aceptados no dicen qué problema resuelven, y no quise inventarlo. Dejé la corrida registrada como `2026-10-16-product-spec-1`.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (fecha 2026-10-16), así que no hubo que volver a registrarlos. No hubo preguntas que responder.

- **Alcance:** entran los 12 requerimientos en estado `aceptado`. Quedan fuera los 4 `propuesto` (REQ-4601, 4607, 4609, 4611), porque nadie los ha decidido.
- **Criterios de aceptación:** en 8 requerimientos el criterio es «se verifica en producción», que no dice qué se mide ni quién verifica. Otros 4 no tienen criterio: REQ-4606, 4613, 4614 y 4615.
- **Supuestos:** hay uno, «el proveedor cumple el tiempo pactado», sin verificar desde el 2026-06-28. Su fecha no cuadra con el documento, que es de 2025-12-25.
- **Vacíos, cada uno con quién lo cierra:**
  - REQ-4602 no tiene doliente.
  - REQ-4603, 4614 y 4615 no tienen evidencia de demanda. Los otros 9 solo tienen una cita genérica de la entrevista de 2025-10-05, que no nombra ningún requerimiento.
  - Ningún requerimiento tiene proyecto que lo ejecute.
  - El acta no dice quién decidió cada aceptación.
  - Los casos borde, el éxito del producto y la prioridad no están definidos.
  - No hay acuerdo escrito con el proveedor.
  - Las obligaciones normativas no aparecen en ningún documento. No hice el barrido citado, y la tabla de vacíos lo dice.
- **Requerimientos aceptados sin cubrir:** los 12 quedan sin comportamiento. La tabla final dice qué le falta a cada uno.
- **Siguiente paso:** no ofrecí `/product-charter`, porque no hay vacíos cerrados ni un criterio de éxito verificable.

La corrida midió 40 segundos y 37 hallazgos, y su nota quedó en el registro.

Archivos en `/home/claude/banco/ronda-6/bancos/espacio/estado-producto/PRD-306/corridas/`:
- `salida-product-spec.md`