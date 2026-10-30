# /criterio-revenue:deal-scan 

Las cotizaciones de `40-cotizaciones/` pasaron a la ficha del periodo; el inventario no trajo documentos nuevos ni cambiados.
Las tres señales de descuento son nuevas con esta ficha; las demás vienen de las fichas de contratos, facturas y la liquidación.

# Qué cambió en lo vendido · Consultores Asociados de Lima · periodo 2026-10

**Entidad:** Consultores Asociados de Lima (20210046021) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.2.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2105: firmado con el cliente 20210001051 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 240,000.00 | — | 26 | `contratos/CTR-2105.json` |
| 2 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2132 · Venta directa 32: ganada el 2026-10-07 por 120,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 20210001086 | 120,000.00 | — | 29 | `10-crm/oportunidades-2026-11-03.xlsx` fila 21 |
| 3 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2131: firmado con el cliente 20210001108 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 120,000.00 | — | 27 | `contratos/CTR-2131.json` |
| 4 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2131 · Venta directa 31: ganada el 2026-10-06 por 90,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente 20210001078 | 90,000.00 | — | 30 | `10-crm/oportunidades-2026-11-03.xlsx` fila 20 |
| 5 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-2130: firmado con el cliente 20210001094 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 90,000.00 | — | 28 | `contratos/CTR-2130.json` |
| 6 | La comisión liquidada no es la que da el plan sobre lo cerrado y facturado (`commission_differs_from_plan`) | 2026-10 · Milagros Torres: se liquidaron 18,000.00 y el plan da 16,200.00 sobre lo ganado y facturado (OPP-2102) | 1,800.00 | — | — | `50-comisiones/liquidacion-2026-10.csv` fila 3 |
| 7 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2103 · OPP-2103: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 191,400.00 | — | — | `40-cotizaciones/COT-2103_cotizacion.pdf, «Aprobó el descuento»` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2105 · OPP-2130: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 79,200.00 | — | — | `40-cotizaciones/COT-2105_cotizacion.pdf, «Aprobó el descuento»` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 9 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-2104 · OPP-2129: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 72,600.00 | — | — | `40-cotizaciones/COT-2104_cotizacion.pdf, «Aprobó el descuento»` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/oportunidades-2026-11-03.xlsx`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- COT-2101 no trae aprobación escrita: ¿se deja vacía? → Sí; el documento dice que el descuento cae dentro del nivel sin aprobación (respuesta sugerida, prueba sin interfaz)

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `10-crm/oportunidades-2026-11-03.xlsx`
- `40-cotizaciones/COT-2103_cotizacion.pdf, «Aprobó el descuento»`
- `40-cotizaciones/COT-2104_cotizacion.pdf, «Aprobó el descuento»`
- `40-cotizaciones/COT-2105_cotizacion.pdf, «Aprobó el descuento»`
- `50-comisiones/liquidacion-2026-10.csv`
- `contratos/CTR-2105.json`
- `contratos/CTR-2130.json`
- `contratos/CTR-2131.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1`. La salida completa está en `estado-comercial/20210046021-consultores-asociados-de-lima/corridas/salida-deal-scan.md`.