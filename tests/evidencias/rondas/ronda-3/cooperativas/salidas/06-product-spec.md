# /criterio-product:product-spec 

**Borrador de especificación de PRD-303 (Tarjeta débito)**, cerrado por Sandra Gil. Quedó sin sección de comportamiento, porque ningún requerimiento dice qué debe hacer.

Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez (v1.1, 2026-10-15), así que no hubo nada que registrar.

- **Alcance:** entran los 11 requerimientos aceptados (REQ-4300, 4301, 4303, 4304, 4305, 4307, 4309, 4311, 4313, 4314 y 4315). Quedan fuera los 5 propuestos. REQ-4306 lleva 175 días sin decidirse y REQ-4312 lleva 154, ambos por encima del umbral de 60.
- **Sin comportamiento:** los títulos son «Requerimiento REQ-43xx» y el único criterio escrito es «se verifica en producción». Redactar comportamiento habría sido inventarlo.
- **Criterios:** ninguno es verificable, y REQ-4303 y REQ-4305 no tienen criterio.
- **Dolientes y demanda:** REQ-4303, 4309, 4313 y 4314 no tienen doliente. La entrevista de 2025 que cita el acta no nombra ningún requerimiento.
- **Vacíos con dueño:**
  - Falta el criterio de éxito del producto.
  - Los casos borde no están definidos.
  - No hay proyecto asociado a ningún requerimiento.
  - El supuesto «el proveedor cumple el tiempo pactado» lleva 158 días sin verificar.
  - No hice el barrido normativo. Un producto de tarjeta débito roza pagos, consumidor financiero y datos personales, así que conviene correr `regulatory-sweep` antes de cerrar.
- **Siguiente paso:** no ofrezco `/product-charter`, porque los vacíos siguen abiertos y el producto no tiene criterio de éxito.

Dejé la corrida registrada como `2026-10-15-product-spec-1`: 16 requerimientos, 39 hallazgos y 32 s. La salida completa está en `estado-producto/PRD-303/corridas/salida-product-spec.md`.