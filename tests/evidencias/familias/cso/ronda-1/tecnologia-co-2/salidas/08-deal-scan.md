# /criterio-revenue:deal-scan 

Los términos de esta versión ya estaban aceptados (José Francisco Ñáñez, 2026-11-05), así que no hubo que registrarlos de nuevo. El inventario no trajo cotizaciones nuevas, pero llevé a la ficha las cinco de `40-cotizaciones/`. COT-1201 queda sin aprobación porque su documento dice que no la requiere.

# Qué cambió en lo vendido · Soluciones Digitales Andinas · periodo 2026-10

**Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Contrato firmado sin factura (`signed_without_invoice`) | CTR-1205, cliente 830012005, firmado el 2026-09-10 | 64.000.000,00 | 26 | `contratos/CTR-1205.json` |
| 2 | Contrato firmado sin factura | CTR-1232, cliente 830012010, firmado el 2026-09-10 | 40.000.000,00 | 26 | `contratos/CTR-1232.json` |
| 3 | Contrato firmado sin factura | CTR-1231, cliente 830012009, firmado el 2026-09-09 | 32.000.000,00 | 27 | `contratos/CTR-1231.json` |
| 4 | Oportunidad ganada sin contrato (`won_without_contract`) | OPP-1231, ganada el 2026-10-06, cliente 830012007 | 24.000.000,00 | 30 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 20 |
| 5 | Contrato firmado sin factura | CTR-1230, cliente 830012008, firmado el 2026-09-08 | 24.000.000,00 | 28 | `contratos/CTR-1230.json` |
| 6 | Comisión distinta del plan (`commission_differs_from_plan`) | Paula Vega: se liquidaron 4.800.000,00 y el plan da 4.320.000,00 (OPP-1202) | 480.000,00 | — | `50-comisiones/liquidacion-2026-10.csv` fila 3 |
| 7 | Descuento fuera de matriz (`discount_outside_policy`) | COT-1205 · OPP-1230: el 22 % cae en el nivel 3, que pide gerente general, y lo aprobó Marta Gil como gerente comercial | 21.120.000,00 | — | `40-cotizaciones/COT-1205_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Descuento fuera de matriz | COT-1204 · OPP-1229: el 22 % cae en el nivel 3, que pide gerente general, y lo aprobó Marta Gil como gerente comercial | 19.360.000,00 | — | `40-cotizaciones/COT-1204_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |

## Resultado

- Hay 5 cotizaciones en la ficha.
- Todo lo que llegó se procesó.
- El agente no hizo preguntas en esta corrida.

La corrida quedó registrada como `2026-11-05-deal-scan-1` con 8 hallazgos. Dejé la salida mostrada en `estado-comercial/900876543-soluciones-digitales-andinas/corridas/salida-deal-scan.md`. El reporte del motor está en `ingresos/2026-10/reporte-deal-scan.md`. Aquí resumí las columnas «Responsable» y «Fuentes», que están vacías o repiten las citas.