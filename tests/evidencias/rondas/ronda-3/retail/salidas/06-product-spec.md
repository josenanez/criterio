# /criterio-product:product-spec 

El borrador de especificación de Marketplace (PRD-308) está escrito, pero no tiene comportamiento: ningún requerimiento aceptado dice qué debe hacer el producto. Los 13 aceptados se llaman «Requerimiento REQ-xxxx» y el acta del comité del 2026-10-12 no los describe. Dejé esa sección vacía a propósito, en vez de inventar lo que un marketplace suele hacer.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

- **Alcance:** entran los 13 aceptados. Los 4 en `propuesto` (REQ-4803, 4804, 4808 y 4810) quedan fuera porque nadie los ha decidido.
- **Criterios de aceptación:** nueve dicen solo «se verifica en producción», que no se puede verificar sin discusión. Cuatro no tienen criterio (REQ-4806, 4807, 4813 y 4814). No hay ninguno escrito contra una métrica.
- **Vacíos:** la lista llega a 10, cada uno con quién lo cierra. Los más pesados:
  - REQ-4815 está aceptado sin doliente.
  - La definición no trae criterio de éxito del producto.
  - Ningún requerimiento tiene proyecto que lo ejecute.
  - No hay plan que respalde la decisión «Se mantiene el plan».
- **Supuestos:** «La regulación de datos lo permite» figura como verificado, pero no cita quién ni con qué, así que lo traté como no verificado. Tampoco se hizo un barrido normativo con cita, porque nada indica qué datos trata cada requerimiento.
- **Cifra del caso de negocio:** declara un volumen mensual de 209.097 y el tablero mide 131.628. Es 37 % menos, y el umbral configurado es 20 %.
- **Requerimientos aceptados sin cubrir:** ninguno quedó fuera por omisión, pero el borrador no cubre el comportamiento de ninguno de los 13. La tabla final los lista con la causa de cada uno.

No ofrecí `/product-charter`, porque faltan los vacíos cerrados y el criterio de éxito.

La corrida quedó registrada como `2026-10-15-product-space-1`… concretamente `2026-10-15-product-spec-1`, con 17 requerimientos leídos, 28 hallazgos y 52 segundos.

Archivos están en `/home/claude/banco/ronda-3/retail/espacio/estado-producto/PRD-308/corridas/`:
- `salida-product-spec.md`