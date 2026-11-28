# /criterio-revenue:deal-scan 

El inventario no trajo documentos nuevos ni cambiados. Las cinco cotizaciones de `40-cotizaciones/` ya estaban en la ficha del periodo, así que no hubo nada que extraer. Abajo va el reporte del motor sobre esa ficha.

# Qué cambió en lo vendido · Almacenes del Istmo · periodo 2026-10

**Entidad:** Almacenes del Istmo (155622222-2-2017) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 1.4.2 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2608 · Venta de equipos: ganada el 2026-10-05 por 75,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830026002 | 75,000.00 | — | 31 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 9 |
| 2 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2630 · Venta directa 30: ganada el 2026-10-07 por 60,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830026008 | 60,000.00 | — | 29 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 20 |
| 3 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2631: firmado con el cliente 830026010 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 60,000.00 | — | 27 | `contratos/CTR-2631.json` |
| 4 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2629 · Venta directa 29: ganada el 2026-10-06 por 45,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830026007 | 45,000.00 | — | 30 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 19 |
| 5 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2630: firmado con el cliente 830026009 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 45,000.00 | — | 28 | `contratos/CTR-2630.json` |
| 6 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2603 · OPP-2603: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 95,700.00 | — | — | `40-cotizaciones/COT-2603_cotizacion.pdf, p. 1` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 7 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2604 · OPP-2627: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 42,900.00 | — | — | `40-cotizaciones/COT-2604_cotizacion.pdf, p. 1` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2605 · OPP-2628: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 33,000.00 | — | — | `40-cotizaciones/COT-2605_cotizacion.pdf, p. 1` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- `40-cotizaciones/COT-2603_cotizacion.pdf, p. 1`
- `40-cotizaciones/COT-2604_cotizacion.pdf, p. 1`
- `40-cotizaciones/COT-2605_cotizacion.pdf, p. 1`
- `contratos/CTR-2630.json`
- `contratos/CTR-2631.json`