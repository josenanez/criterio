# /criterio-product:product-spec 

Terminé el borrador de especificación de Recaudos (PRD-306), pero sin comportamiento: ninguno de los 16 requerimientos aceptados quedó cubierto. Ninguno dice qué problema resuelve (los títulos son solo «Requerimiento REQ-xxxx»), y no quise inventarlo.

- **Criterios de aceptación:** 9 requerimientos dicen solo «se verifica en producción», que no se puede verificar sin discutir. Los otros 7 no tienen criterio. No propuse cifras propias.
- **Supuestos:** «El reglamento vigente lo permite» lleva 154 días sin verificar. El volumen mensual declarado (196.775) frente al medido (175.099) tiene una brecha del 11%, bajo el umbral del 20%.
- **Vacíos:**
  - El problema de cada requerimiento.
  - Los casos borde.
  - Los dueños de REQ-4611 y REQ-4614.
  - Los dueños de cada criterio faltante.
  - El proyecto que construiría los 16 (hoy ninguno).
  - Las dependencias con otros equipos: ningún documento las registra, así que no las inventé.
- **Obligaciones normativas:** ningún documento dice el país, así que todas quedaron como «no tengo la norma a la vista» o «sin resolver». No cité ninguna norma.
- **Fuera de la especificación:** REQ-4614, porque está propuesto y no aceptado.
- **Corrida:** los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-17), así que no los registré de nuevo. La corrida quedó registrada con `product-spec` (39 s, 17 requerimientos, 43 hallazgos).
- **Siguiente paso:** no ofrezco `/product-charter`, porque los vacíos siguen abiertos. Antes conviene volver a `/product-requirements` cuando los dueños hayan escrito el problema de cada requerimiento.

El borrador completo está en `estado-producto/PRD-306/corridas/salida-product-spec.md`. Lo tiene que cerrar Gustavo Neira.