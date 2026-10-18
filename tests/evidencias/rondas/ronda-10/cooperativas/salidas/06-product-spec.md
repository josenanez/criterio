# /criterio-product:product-spec 

Dejé el borrador de especificación de Microcrédito (PRD-305), pero sin sección de comportamiento: ninguno de los 12 requerimientos aceptados trae escrito el problema que resuelve, y redactarla habría sido inventarla. Lo cierra Ricardo Salas, y el agente no aprueba ni decide el alcance.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-18, así que no los registré de nuevo.

- **Alcance:** entran los 12 requerimientos aceptados. No entran los 4 que siguen propuestos (REQ-4502, 4503, 4504 y 4510) ni la propuesta de valor, que está vacía en la definición.
- **Criterios de aceptación:** 10 dicen solo «se verifica en producción», que no se puede verificar, y 2 (REQ-4500 y REQ-4511) no tienen ninguno. No propuse umbrales nuevos porque habría sido rellenar.
- **Supuesto:** «El proveedor cumple el tiempo pactado» lleva 146 días sin verificar, y el umbral configurado es 30. No tiene dueño y ningún documento identifica al proveedor.
- **Vacíos con dueño propuesto:**
  - Dos aceptados no tienen doliente (REQ-4505 y 4506).
  - No se sabe quién decidió aceptarlos.
  - Tres no tienen evidencia de demanda (REQ-4507, 4511 y 4514).
  - Ninguno tiene proyecto que lo construya.
  - Faltan los casos borde y la prioridad.
  - No se hizo el barrido normativo: lo señalé como vacío, sin opinar sobre cumplimiento.
- **Lo que no cubre:** los 12 aceptados quedan sin sección, cada uno con su razón.

No ofrecí `/product-charter`, porque los vacíos siguen abiertos y el producto no tiene criterio de éxito.

La corrida quedó registrada como `2026-10-18-product-spec-1`: 42 segundos, 16 requerimientos leídos y 27 hallazgos.

Archivos en `/home/claude/banco/ronda-10/cooperativas/espacio/estado-producto/PRD-305/corridas/`:
- `salida-product-spec.md`