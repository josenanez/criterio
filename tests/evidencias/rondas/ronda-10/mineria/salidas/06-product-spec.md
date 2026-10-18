# /criterio-product:product-spec 

Escribí el borrador de especificación de PRD-308 (Permisos de trabajo digitales), pero no tiene sección de comportamiento. Ninguno de los 9 requerimientos aceptados dice qué necesita ni cómo se verifica, y escribirla habría sido inventarla.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-18, así que no los volví a registrar.

- **Qué cubre:** los 9 requerimientos `aceptado` (REQ-4800, 4802, 4803, 4805, 4806, 4807, 4808, 4809 y 4811) entran al alcance solo como identificadores. Los 3 `propuesto` (REQ-4801, 4804 y 4810) quedan fuera porque nadie los ha decidido. Ninguno de los 9 queda cubierto por una sección de comportamiento.
- **Criterios de aceptación:** el único que existe, «se verifica en producción», no es verificable y está en 5 requerimientos. Otros 4 (REQ-4803, 4805, 4806 y 4808) no tienen ninguno.
- **Supuesto sin verificar:** «Operaciones adopta la herramienta» cita una entrevista con doce clientes que no está en `10-descubrimiento`. La única entrevista allí es de 2025-09-27 y es con un cliente.
- **Vacíos con dueño:**
  - REQ-4809 no tiene doliente.
  - No hay proyecto que construya el producto.
  - Falta el criterio de éxito.
  - Los casos borde no están definidos.
  - Solo asistió Javier Hoyos al comité.
- **Normativa:** no hice el barrido. La definición no dice qué contiene un permiso de trabajo ni qué datos de personas maneja. Lo dejé como «no se sabe», no como «no hay obligaciones».
- **Siguiente paso:** no ofrezco `/product-charter` todavía. Cuando cada aceptado tenga necesidad y criterio verificable, se vuelve a correr `/product-spec`.

La corrida quedó registrada como `2026-10-18-product-spec-1` (40 s, 12 requerimientos, 30 hallazgos).

Archivos en `/home/claude/banco/ronda-10/mineria/espacio/estado-producto/PRD-308/corridas/`:
- `salida-product-spec.md`