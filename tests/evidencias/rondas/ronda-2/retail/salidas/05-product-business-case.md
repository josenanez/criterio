# /criterio-product:product-business-case 

Armé el caso de negocio de Pago con QR (PRD-303) y registré la corrida. El documento no se sostiene todavía: tiene una sola cifra y falta el costo de construir.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (versión 1.1, 2026-10-15), así que no hubo que volver a aceptarlos.

- **Cifras:** hay una sola, `volumen_mensual` de 243.100, que es una cifra declarada. Su fuente es el propio caso de negocio del 2025-10-19, es decir, se cita a sí misma. Ningún documento dice qué cuenta (transacciones, pagos o clientes) ni cómo se llegó a ese número.
- **Retorno esperado:** el documento dice "Retorno esperado en 24 meses" sin ninguna cifra. Lo dejé como vacío y no lo calculé.
- **Cifra medida:** no hay serie medida (la carpeta `metrics` está vacía), así que no se pudo contrastar el 243.100 con nada.
- **Costos:** el costo de construir y el de operar no están en ningún documento. Es el primer vacío: sin él hay una propuesta, no un caso de negocio.
- **Supuesto:** "La demanda se sostiene sin descuento" lleva sin verificar desde el 2026-03-17. Ofrezco pasarlo, junto con el supuesto implícito de que el segmento alcanza ese volumen, al seguimiento con assumption-tracking.
- **Requerimientos:** los cinco están aceptados, pero ninguno tiene proyecto. Dos no tienen criterio de aceptación (REQ-2017 y REQ-2025). Como evidencia de demanda solo hay una cita anónima de entrevista, de 2025-09-29.
- **Otros vacíos:** no hay criterio de éxito con fecha de corte, ni alternativas, ni qué pasa si no se hace, ni propuesta concreta, ni autoridad de aprobación.
- **Cruce con otros productos:** no hay fichas publicadas, así que el cruce de `/product-overlap` no se pudo completar. Solo busqué la cifra y el código en los documentos a la vista y nadie más los usa. Existe el proyecto PRY-205 "pago con QR en caja", pero ningún documento lo vincula a PRD-303 y no usé sus datos.

La corrida registró 8 hallazgos (cinco requerimientos sin proyecto, dos sin criterio de aceptación y un supuesto sin verificar) y tardó 37 segundos.

Archivos en `estado-producto/PRD-303/corridas/`:
- `salida-product-business-case.md`
- `2026-10-15-product-business-case-1.md`