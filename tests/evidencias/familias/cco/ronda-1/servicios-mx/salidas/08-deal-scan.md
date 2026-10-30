# /criterio-revenue:deal-scan 

No había documentos nuevos desde la corrida anterior. Llevé a la ficha las 5 cotizaciones de `40-cotizaciones/` que aún no estaban en ella. Los dos descuentos de abajo (filas 7 y 8) vienen de esas cotizaciones.

# Qué cambió en lo vendido · Servicios Profesionales Mexicanos · periodo 2026-10

**Entidad:** Servicios Profesionales Mexicanos (SPM140708QJ2) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.1.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1508 · Venta de equipos: ganada el 2026-10-05 por 450,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CSE120303C22 | 450,000.00 | — | 31 | `10-crm/oportunidades-2026-11-03.xlsx` fila 9 |
| 2 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1533 · Venta directa 33: ganada el 2026-10-08 por 450,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CSE190110J92 | 450,000.00 | — | 28 | `10-crm/oportunidades-2026-11-03.xlsx` fila 23 |
| 3 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1532 · Venta directa 32: ganada el 2026-10-07 por 360,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CSE180909I81 | 360,000.00 | — | 29 | `10-crm/oportunidades-2026-11-03.xlsx` fila 22 |
| 4 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1531 · Venta directa 31: ganada el 2026-10-06 por 270,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CSE170808H70 | 270,000.00 | — | 30 | `10-crm/oportunidades-2026-11-03.xlsx` fila 21 |
| 5 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1530: firmado con el cliente CSE200211K103 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 270,000.00 | — | 28 | `contratos/CTR-1530.json` |
| 6 | La comisión liquidada no es la que da el plan sobre lo cerrado y facturado (`commission_differs_from_plan`) | 2026-10 · Daniela Ochoa: se liquidaron 54,000.00 y el plan da 48,600.00 sobre lo ganado y facturado (OPP-1502) | 5,400.00 | — | — | `50-comisiones/liquidacion-2026-10.csv` fila 3 |
| 7 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1505 · OPP-1530: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 237,600.00 | — | — | `40-cotizaciones/COT-1505_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre (`discount_outside_policy`) | COT-1504 · OPP-1529: el 22 % cae en el nivel 3, que pide la aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 217,800.00 | — | — | `40-cotizaciones/COT-1504_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/oportunidades-2026-11-03.xlsx`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `10-crm/oportunidades-2026-11-03.xlsx`
- `40-cotizaciones/COT-1504_cotizacion.pdf`
- `40-cotizaciones/COT-1505_cotizacion.pdf`
- `50-comisiones/liquidacion-2026-10.csv`
- `contratos/CTR-1530.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1`, con 8 hallazgos.