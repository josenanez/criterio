# /criterio-revenue:deal-scan 

Llevé las 5 cotizaciones de `40-cotizaciones/` a la ficha del periodo 2026-10. El motor encontró 9 señales y la corrida quedó registrada como `2026-11-05-deal-scan-1`.

Ninguna cotización era nueva en el inventario, pero la ficha de ingresos del periodo no existía, así que la creé con las 5. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-11-05, y no hubo preguntas.

La COT-2301 no trae aprobación escrita, así que su aprobador quedó vacío. Su descuento del 10 % está dentro del nivel que no pide aprobación.

Las 9 señales son:
- **Ganadas sin contrato (3):** OPP-2308, OPP-2329 y OPP-2330 no tienen contrato firmado en las fichas de Fidel.
- **Firmados sin factura (3):** CTR-2330, CTR-2331 y CTR-2332 no tienen factura emitida en las fichas de Clara dentro del plazo.
- **Descuento fuera de política (3):** COT-2303, COT-2304 y COT-2305 tienen un descuento del 35 %, que ningún nivel de la matriz cubre. Los tres traen aprobación escrita de Ricardo Paz, gerente general, pero el motor las marca igual.

Los archivos están en `estado-comercial/76543210-3-tiendas-del-maipo/`:
- `ingresos/2026-10/ficha.json`
- `corridas/salida-deal-scan.md`, que contiene el reporte completo con las cifras y las citas
- `ingresos/2026-10/reporte-deal-scan.md`: el comando dice que el motor lo deja ahí, pero no lo abrí ni comprobé que exista