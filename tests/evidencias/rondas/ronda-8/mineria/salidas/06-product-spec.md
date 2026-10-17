# /criterio-product:product-spec 

Escribí el borrador de especificación de Trazabilidad (PRD-304), pero tiene solo el armazón y los huecos a la vista. El registro no permite escribir comportamiento, y no rellené nada con lo razonable. Ninguno de los 11 requerimientos aceptados tiene descrita su necesidad, y todos se llaman «Requerimiento REQ-44xx».

- **Términos:** ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-17, así que no hubo que registrar nada.
- **Alcance:** entran los 11 aceptados (REQ-4400, 4401, 4402, 4403, 4404, 4406, 4409, 4410, 4412, 4413 y 4414), solo por referencia. Los 5 que siguen propuestos quedan fuera, y también la arquitectura y las estimaciones.
- **Criterios de aceptación:** el único que existe es «se verifica en producción», en 6 requerimientos. No es verificable y no lo reescribí con una métrica inventada. Otros 5 (REQ-4400, 4402, 4404, 4410 y 4414) no tienen criterio.
- **Supuestos:** «Operaciones adopta la herramienta» figura como verificado, pero el anexo cita una medición del piloto que no está en la carpeta. Además, la fecha del supuesto (2026-07-24) es posterior a la de la definición (2025-09-15).
- **Vacíos con dueño:**
  - REQ-4400 y REQ-4414 están aceptados sin doliente.
  - El acta no dice quién decidió ninguna aceptación; solo registra a Andrés Lozano como asistente y la decisión «Se mantiene el plan».
  - REQ-4401 y REQ-4414 no tienen evidencia de demanda. Los otros 9 se apoyan en una cita anónima de hace más de 12 meses.
  - Faltan la prioridad, el criterio de éxito del producto y el proyecto que ejecuta cada requerimiento.
  - No hay barrido normativo, porque ningún documento describe qué datos trata el producto.
- **Requerimientos sin cubrir:** los 11 aparecen en la tabla final, porque ninguno tiene sección de comportamiento.
- **Charter:** no ofrecí `/criterio-product:product-charter`, porque faltan los vacíos cerrados y el criterio de éxito.

La corrida quedó registrada como `2026-10-17-product-spec-1`: 16 requerimientos leídos, 40 hallazgos y 40 segundos.

Archivos en `estado-producto/PRD-304/corridas/`:
- `salida-product-spec.md`