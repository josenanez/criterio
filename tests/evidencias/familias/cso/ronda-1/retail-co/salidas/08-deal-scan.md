# /criterio-revenue:deal-scan 

Llevé las 5 cotizaciones de `40-cotizaciones/` a la ficha del periodo 2026-10. El inventario no trajo documentos nuevos ni cambiados, y los términos ya estaban aceptados en esta versión a nombre de José Francisco Ñáñez. El motor encontró 8 señales.

# Qué cambió en lo vendido · Almacenes del Valle · periodo 2026-10

**Entidad:** Almacenes del Valle (901234567) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.1.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1108 · Venta de equipos: ganada el 2026-10-05 por 50.000.000,00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830011002 | 50.000.000,00 | — | 31 | `10-crm/oportunidades-2026-11-03.csv` fila 9 |
| 2 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1133 · Venta directa 33: ganada el 2026-10-07 por 40.000.000,00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830011008 | 40.000.000,00 | — | 29 | `10-crm/oportunidades-2026-11-03.csv` fila 23 |
| 3 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1131: firmado con el cliente 830011010 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 40.000.000,00 | — | 27 | `contratos/CTR-1131.json` |
| 4 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1132 · Venta directa 32: ganada el 2026-10-06 por 30.000.000,00 y las fichas de Fidel no tienen un contrato firmado con el cliente 830011007 | 30.000.000,00 | — | 30 | `10-crm/oportunidades-2026-11-03.csv` fila 22 |
| 5 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1130: firmado con el cliente 830011009 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 30.000.000,00 | — | 28 | `contratos/CTR-1130.json` |
| 6 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1103 · OPP-1103: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 63.800.000,00 | — | — | `40-cotizaciones/COT-1103_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 7 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1105 · OPP-1131: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 28.600.000,00 | — | — | `40-cotizaciones/COT-1105_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1104 · OPP-1130: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 26.400.000,00 | — | — | `40-cotizaciones/COT-1104_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/oportunidades-2026-11-03.csv`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `10-crm/oportunidades-2026-11-03.csv`
- `40-cotizaciones/COT-1103_cotizacion.pdf`
- `40-cotizaciones/COT-1104_cotizacion.pdf`
- `40-cotizaciones/COT-1105_cotizacion.pdf`
- `contratos/CTR-1130.json`
- `contratos/CTR-1131.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1`, con la salida en `estado-comercial/901234567-almacenes-del-valle/corridas/salida-deal-scan.md`.