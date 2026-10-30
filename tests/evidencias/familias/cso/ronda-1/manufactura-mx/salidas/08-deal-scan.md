# /criterio-revenue:deal-scan 

Se llevaron a la ficha de 2026-10 las 5 cotizaciones de `40-cotizaciones/`. El inventario no traía archivos nuevos. Los términos ya estaban vigentes (versión 1.3, aceptados por José Francisco Ñáñez el 2026-11-05).

# Qué cambió en lo vendido · Manufacturas del Bajío · periodo 2026-10

**Entidad:** Manufacturas del Bajío (MBA120315KT4) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.1.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1405: firmado con el cliente CMA150606F55 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 960,000.00 | — | 26 | `contratos/CTR-1405.json` |
| 2 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1432: firmado con el cliente CMA210312L114 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 600,000.00 | — | 26 | `contratos/CTR-1432.json` |
| 3 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1431 · Venta directa 31: ganada el 2026-10-07 por 480,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CMA180909I81 | 480,000.00 | — | 29 | `10-crm/oportunidades-2026-11-03.csv` fila 20 |
| 4 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1431: firmado con el cliente CMA200211K103 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 480,000.00 | — | 27 | `contratos/CTR-1431.json` |
| 5 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1430 · Venta directa 30: ganada el 2026-10-06 por 360,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CMA170808H70 | 360,000.00 | — | 30 | `10-crm/oportunidades-2026-11-03.csv` fila 19 |
| 6 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1430: firmado con el cliente CMA190110J92 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 360,000.00 | — | 28 | `contratos/CTR-1430.json` |
| 7 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1403 · OPP-1403: ningún nivel de la matriz cubre un descuento de 35 % | 1,218,000.00 | — | — | `40-cotizaciones/COT-1403_cotizacion.pdf` |
| 8 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1405 · OPP-1429: ningún nivel de la matriz cubre un descuento de 35 % | 462,000.00 | — | — | `40-cotizaciones/COT-1405_cotizacion.pdf` |
| 9 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1404 · OPP-1428: ningún nivel de la matriz cubre un descuento de 35 % | 420,000.00 | — | — | `40-cotizaciones/COT-1404_cotizacion.pdf` |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/oportunidades-2026-11-03.csv`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-crm/oportunidades-2026-11-03.csv`
- `40-cotizaciones/COT-1403_cotizacion.pdf`
- `40-cotizaciones/COT-1404_cotizacion.pdf`
- `40-cotizaciones/COT-1405_cotizacion.pdf`
- `contratos/CTR-1405.json`
- `contratos/CTR-1430.json`
- `contratos/CTR-1431.json`
- `contratos/CTR-1432.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1`, con 9 hallazgos. El reporte está en `ingresos/2026-10/reporte-deal-scan.md` y lo mostrado, en `corridas/salida-deal-scan.md`.

Dos detalles de la corrida:
- **Nota de la corrida:** el texto que dejé en `--nota` quedó impreciso: dice "4 contratos sin factura", pero el reporte trae 4 contratos sin factura, 2 ganadas sin contrato y 3 descuentos fuera de política.
- **COT-1401:** no trae aprobación escrita y su 10 % está "dentro del nivel sin aprobación". Quedó con los campos de aprobación vacíos y el motor no la señaló.