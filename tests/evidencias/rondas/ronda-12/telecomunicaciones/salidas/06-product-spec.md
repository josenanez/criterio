# /criterio-product:product-spec 

Escribí el borrador de especificación de Televisión IP (PRD-306), pero sin secciones de comportamiento. Los 12 requerimientos no dicen qué piden: el título es el propio código (por ejemplo «Requerimiento REQ-4600») y el campo `need` está vacío en todos. Describirlos habría sido inventar, así que el borrador solo fija el alcance y deja los vacíos a la vista.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-28, así que no los registré otra vez. La corrida quedó registrada con el id `2026-10-28-product-spec-1`.

- **Alcance:** entran los 11 requerimientos aceptados. Cada uno cita el acta del comité del 2026-10-25, pero ese documento tampoco dice qué pide cada uno. Quedó fuera REQ-4605: está propuesto desde hace 204 días y no tiene doliente.
- **Criterios de aceptación:** nueve dicen solo «se verifica en producción», que no se puede verificar sin discutir. Ninguno se puede medir hoy: no hay umbral ni observable, y ningún requerimiento tiene un proyecto que lo construya. REQ-4603 y REQ-4608 no tienen criterio. No inventé cifras.
- **Supuesto del proveedor:** figura como verificado el 2026-09-19. Pero no está el documento técnico del proveedor, no consta cuál es el tiempo pactado, y el supuesto aparece declarado en agosto dentro de una definición fechada en marzo. Además, la entrevista de 2025-09-25 que respalda a ocho requerimientos no nombra ninguno y tiene 13 meses.
- **Vacíos con dueño:**
  - Qué pide cada requerimiento: cada doliente.
  - Criterio de aceptación de los nueve vagos, y de REQ-4603 y REQ-4608: los dolientes, con Gustavo Neira.
  - Quién pidió REQ-4600, 4602 y 4609 (aceptados sin ninguna demanda citada): sus tres dolientes.
  - Criterio de éxito del producto, quién tiene autoridad para decidir, dependencias de otros equipos y obligaciones normativas: Gustavo Neira.
  - El volumen mensual de 100.016 del caso de negocio no tiene más fuente que el propio caso.
- **Cobertura:** ninguno de los 11 queda cubierto en contenido, solo en trazabilidad. La sección de lo no cubierto lo dice así.
- **Siguiente paso:** no ofrecí `/criterio-product:product-charter`, porque los vacíos siguen abiertos y no hay criterio de éxito.

Archivos en `estado-producto/PRD-306/corridas/`:
- salida-product-spec.md