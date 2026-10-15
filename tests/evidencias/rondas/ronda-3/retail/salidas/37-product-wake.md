# /criterio-product:product-wake 

## Marketplace (PRD-308) · 2026-10-15

Esta es la primera revisión del registro y no hay corte anterior. Lo que sigue es la línea base, no novedades. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez, así que no hubo que aceptarlos de nuevo.

El registro tiene 17 requerimientos: 13 aceptados y 4 propuestos. Ocho tienen evidencia de demanda (61,5 %) y ninguno tiene proyecto asociado.

- **Sin decidir (umbral de 60 días):**
  - REQ-4808 lleva 144 días. Además no tiene doliente ni criterio de aceptación, así que primero hay que nombrarle dueño.
  - REQ-4803 lleva 103 días.
  - REQ-4804 lleva 101 días y tampoco tiene evidencia.
  - Los tres deben ir al Comité de producto.
- **Aceptados sin evidencia de demanda:** REQ-4800, 4801, 4806, 4813 y 4815.
- **Aceptados sin doliente:** REQ-4815.
- **Aceptados sin criterio de aceptación:** REQ-4806, 4807, 4813 y 4814.
- **Declarado contra medido:** el caso de negocio declara 209.097 de `volumen_mensual` y el tablero mide 131.628 al 2026-10-01. La diferencia es de 37 %, por encima del umbral de 20 %.
- **Trazas:** los 13 aceptados no los construye ningún proyecto, porque ninguna ficha nombra PRD-308.

**Lo que no sé:**
- El criterio de éxito de la definición no está dicho en ningún documento.
- La autoridad del producto: la configuración dice "Comité de producto", pero el cálculo la devuelve vacía.
- Los supuestos: no hay ninguno registrado, así que no puedo decir cuáles faltan por verificar.
- La configuración no indica carpeta de fichas, así que usé `estado/records`. Si esa carpeta no es la de las fichas, la conclusión sobre las trazas no vale.

El corte quedó guardado en `snapshots/2026-10-15.json`. El texto completo de esta salida está en `estado-producto/PRD-308/corridas/salida-product-wake.md`. La corrida quedó registrada como `2026-10-15-product-wake-1`.

**Vuelvo el 2026-11-14.**