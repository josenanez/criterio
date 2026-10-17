# /criterio-product:product-spec 

Escribí el borrador de la especificación de Microcrédito (PRD-305). No redacté ninguna sección de comportamiento, porque el registro no lo permite. La corrida quedó registrada como `2026-10-17-product-spec-1`.

- **Alcance:** entran los 9 requerimientos aceptados: REQ-2037, 4500, 4501, 4502, 4503, 4504, 4505, 4511 y 4514. Los 8 propuestos quedan fuera.
- **Por qué no hay comportamiento:** ninguno de los 9 aceptados tiene una necesidad descrita, y su título es solo el código.
- **Criterios de aceptación:**
  - Seis dicen «se verifica en producción». Eso no es verificable y hoy no se puede medir.
  - Tres no tienen criterio: REQ-2037, 4501 y 4514.
- **Dueños y evidencia:** REQ-4503 y REQ-4514 no tienen dueño, y REQ-4504 no tiene evidencia de demanda. El acta no dice quién decidió aceptar ningún requerimiento.
- **Supuesto sin verificar:** «La demanda se sostiene sin campaña» se dice verificado con un documento del proveedor del 2026-06-14. Ese documento no está en la carpeta y es posterior a la definición, que es del 2026-04-03.
- **Cifra de volumen:** el caso de negocio declara 216.930 y el tablero mide 207.028, un 4,6 % menos. La métrica no tiene definición y la serie tiene un solo punto.
- **Obligaciones normativas:** un microcrédito toca consumidor financiero y datos personales, pero ningún documento del producto cita una obligación. Lo dejé como vacío para jurídico, sin opinar sobre cumplimiento.
- **Sin autoridad ni firma:** el producto no tiene autoridad registrada, así que el borrador lo cierra María Restrepo y falta quién firme. No ofrecí `/product-charter` porque los vacíos siguen abiertos y no hay criterio de éxito.

Aplicando la regla de los vacíos con dueño, la tabla de vacíos del borrador cierra con el criterio de éxito del producto y con los casos borde.

**Dos omisiones mías:**
- **Evidencia desactualizada:** la entrevista del 2025-09-06 tiene más de 12 meses, y el cálculo la marca como evidencia desactualizada en 14 casos. El borrador la llama «genérica» pero no menciona su antigüedad.
- **Requerimientos sin dueño:** el cálculo cuenta 3, no 2, porque REQ-4513 (propuesto) tampoco tiene dueño. El borrador solo menciona los dos aceptados.

Los términos ya estaban vigentes, aceptados a nombre de José Francisco Ñáñez el 2026-10-17 (v0.3.13), así que no los registré de nuevo.

El borrador está en `estado-producto/PRD-305/corridas/salida-product-spec.md`.