# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-301 (Alerta de taludes). Tiene una sola cifra, y el costo, el retorno y el criterio de éxito no tienen fuente, así que entran como vacíos y no como cifras.

**Términos:** ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17, así que no los volví a pedir.

- **Cifra única:** `volumen_mensual` = 191.637, declarada en el propio caso de negocio del 2026-06-09. No dice la unidad ni de dónde sale. No hay serie medida, así que no se puede contrastar y la brecha queda como ausencia, no como diferencia.
- **Costos:** no hay ninguno declarado en ningún documento. Es el primer vacío: sin costo de construir hay una propuesta, no un caso.
- **Retorno:** el caso solo dice «Retorno esperado en 24 meses», sin cifra, base ni método.
- **Criterio de éxito:** no está declarado, ni en la definición ni en el caso. Tampoco hay fecha de corte. La propuesta de la definición está vacía.
- **Qué se construye:** 12 requerimientos aceptados y ninguno tiene proyecto que lo ejecute. REQ-4108 y REQ-2030 se aceptaron sin que nadie conste como quien los pidió. La única evidencia de demanda es una entrevista de 2025-08-30, con 13 meses de antigüedad, que no nombra ninguno de los requerimientos.
- **Supuesto:** «La red de la mina soporta el volumen» lleva 58 días sin verificar, contra un umbral de 30. Lo dejé para pasarlo al seguimiento con assumption-tracking.
- **Otros productos:** no hay ninguno publicado, así que no hice el cruce de `/product-overlap`.

No proyecté ingresos ni calculé rentabilidad, y el documento no recomienda aprobar ni rechazar. La corrida quedó registrada como `2026-10-17-product-business-case-1`.

Archivos en `/home/claude/banco/ronda-7/mineria/espacio/estado-producto/PRD-301/corridas/`:
- `salida-product-business-case.md`
- `2026-10-17-product-business-case.md`