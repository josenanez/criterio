# /criterio-product:product-spec 

Dejé el borrador de especificación de PRD-304, pero sin la sección de comportamiento. El registro no dice qué pide ningún requerimiento: los 16 títulos son solo «Requerimiento REQ-xxxx». Escribir esa sección habría sido inventarla.

Los términos ya estaban vigentes y aceptados (v1.1, 2026-10-16, José Francisco Ñáñez), así que no los registré de nuevo.

- **Alcance:** entran como candidatos los 14 requerimientos aceptados, por su estado y no por su contenido. Quedan fuera REQ-4400 y REQ-4411, que siguen propuestos desde hace 155 y 176 días.
- **Criterios de aceptación:**
  - Diez requerimientos tienen «se verifica en producción», que no es verificable: no dice qué se mide ni quién lo mira.
  - Cuatro no tienen criterio: REQ-2028, 2036, 4402 y 4412.
  - Hoy solo se mide `volumen_mensual`, y ningún criterio lo usa.
- **Supuestos:**
  - «La red de la mina soporta el volumen» está declarado como verificado sin citar qué lo verificó.
  - El volumen declarado (151.914) es 23,1 % mayor que el medido (116.821).
  - La única demanda registrada es una entrevista de hace 14 meses que no nombra ningún requerimiento.
- **Vacíos:** cada uno lleva su dueño. Entre ellos están el doliente de REQ-4401, 4402 y 4405, quién aceptó los 14 (el acta no lo dice), el criterio de éxito del producto y el proyecto que ejecute cada requerimiento.
- **Normativa y otros equipos:** no se hizo barrido normativo porque la definición no dice qué se traza. Ningún documento menciona otros equipos, y no consta si no hay o si nadie los miró.
- **Requerimientos sin cubrir:** los 14 quedan listados, cada uno con su razón.
- **Siguiente paso:** no ofrezco `/product-charter`, porque los vacíos siguen abiertos y no hay criterio de éxito.

La corrida quedó registrada (`2026-10-16-product-spec-1`, 69 s, 16 requerimientos, 39 hallazgos).

Archivos en `/home/claude/banco/ronda-5/mineria/espacio/estado-producto/PRD-304/corridas/`:
- `salida-product-spec.md`