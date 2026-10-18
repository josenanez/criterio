# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de PRD-309, Tarjeta de la tienda, y registré la corrida (39 segundos, 15 requerimientos, 36 señales abiertas). Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo.

El caso no se sostiene todavía. Esto es lo que dice:

- **Cifras:** el volumen mensual declarado es 278.242 (caso de negocio, 2026-02-23) y el medido es 214.637 (tablero, corte 2026-10-09). La diferencia es de 22,9 %, sobre el umbral de 20 %. Hay un solo punto medido, y ni el caso ni el tablero explican qué cuenta como volumen. Por eso no se sabe si las dos cifras miden lo mismo.
- **Retorno:** dice «en 24 meses» y no trae monto, así que no hay nada que medir.
- **Costos:** no hay ninguno en ningún documento, y el costo de construir es el primer vacío.
- **Demanda:** de los 15 requerimientos, 13 están aceptados y 2 propuestos. Los aceptados se apoyan en una sola entrevista de 12 meses, que no nombra ningún requerimiento. REQ-4901 y REQ-4912 no tienen ninguna evidencia.
- **Supuesto:** que el cliente paga por la entrega rápida lleva 31 días sin verificar. Quedó listado en el caso como supuesto, con quién lo verificaría sin nombrar.
- **Otros vacíos:**
  - No hay criterio de éxito, así que la sección «Cómo se sabrá si funcionó» queda declarada como vacía.
  - La propuesta es solo un rótulo.
  - Nadie nombra quién decide.
  - No hay país ni proyecto asignado.
- **Cruce con otros productos:** no se hizo, porque en `estado-producto/` solo está PRD-309. Varias carpetas de documentos (PRD-299 a PRD-308) traen una métrica también llamada `volumen_mensual`, pero no las leí y no afirmo que se solapen.

El borrador no calcula rentabilidad, no rellena vacíos con cifras de referencia ni recomienda aprobar o rechazar. Sugiere pasar el supuesto de la entrega rápida a seguimiento y no pasar a `/product-charter` mientras la definición esté abierta.

Archivos en `/home/claude/banco/ronda-9/retail/espacio/estado-producto/PRD-309/corridas/`:
- `salida-product-business-case.md`
- `2026-10-17-product-business-case-1.md`