# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-302 (Crédito hipotecario digital) y registré la corrida. No tiene costos, beneficio ni criterio de éxito, así que hoy es una propuesta más que un caso evaluable.

Los términos v1.2 ya estaban aceptados por José Francisco Ñáñez el 2026-10-23, así que no hubo que registrarlos de nuevo.

- **Cifras:** el caso declara un `volumen_mensual` de 289.875 (2026-05-08) y el tablero mide 235.072 (corte 2026-10-13). La brecha es de 18,9 %, bajo el umbral de 20 %. Esa brecha quedó dentro del caso, con las dos cifras y las dos fechas. La serie medida tiene un solo punto.
- **Lo que se construye:** entran los 13 requerimientos aceptados. Los 3 propuestos quedaron fuera.
  - Ninguno tiene proyecto que lo ejecute.
  - Tres no tienen criterio de aceptación.
  - Dos no tienen evidencia de quién los pidió.
- **Costos:** no hay costo de construir ni de operar en ningún documento, y ese es el primer vacío.
- **Retorno y éxito:** el «retorno esperado en 24 meses» no tiene cifra. El criterio de éxito no está declarado.
- **Supuesto central:** «El segmento paga por esto» figura como confirmado, pero remite a un documento técnico del proveedor que no está en la carpeta. El anexo no recoge ningún dato.
- **Otros productos:** no hay otros publicados, así que el cruce de métricas quedó pendiente.

No calculé ingresos, retorno ni recuperación, y no recomiendo aprobar ni rechazar. Para la corrida, el script contó 35 hallazgos sobre los 16 requerimientos y midió 47 segundos.

Archivos en `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/bancos/espacio/estado-producto/PRD-302/corridas/`:
- salida-product-business-case.md
- 2026-10-23-product-business-case-1.md

Como siguiente paso, pasar los supuestos a assumption-tracking; si el caso se aprueba, correr `/criterio-product:product-charter`.