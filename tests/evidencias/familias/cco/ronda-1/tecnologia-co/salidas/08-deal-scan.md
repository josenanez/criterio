# /criterio-revenue:deal-scan 

Las cinco cotizaciones de `40-cotizaciones/` no eran nuevas para el inventario, pero no estaban en la ficha de ingresos del periodo. Las llevé ahí. COT-1201 no trae aprobación escrita; su descuento es del 10 % y el documento dice que está dentro del nivel sin aprobación.

# Qué cambió en lo vendido · Soluciones Digitales Andinas · periodo 2026-10

**Entidad:** Soluciones Digitales Andinas (900876543) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.1.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Contrato firmado sin factura dentro del plazo (`signed_without_invoice`) | CTR-1205: firmado con el cliente 830012005 el 2026-09-10; las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 64.000.000,00 | 26 | `contratos/CTR-1205.json` |
| 2 | Ídem | CTR-1232: firmado con el cliente 830012010 el 2026-09-10; sin factura hasta el 2026-10-10 | 40.000.000,00 | 26 | `contratos/CTR-1232.json` |
| 3 | Ídem | CTR-1231: firmado con el cliente 830012009 el 2026-09-09; sin factura hasta el 2026-10-09 | 32.000.000,00 | 27 | `contratos/CTR-1231.json` |
| 4 | Oportunidad ganada sin contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1231 · Venta directa 31: ganada el 2026-10-06 por 24.000.000,00; no hay contrato firmado con el cliente 830012007 | 24.000.000,00 | 30 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 20 |
| 5 | Contrato firmado sin factura dentro del plazo (`signed_without_invoice`) | CTR-1230: firmado con el cliente 830012008 el 2026-09-08; sin factura hasta el 2026-10-08 | 24.000.000,00 | 28 | `contratos/CTR-1230.json` |
| 6 | Comisión liquidada distinta de la que da el plan (`commission_differs_from_plan`) | 2026-10 · Paula Vega: se liquidaron 4.800.000,00 y el plan da 4.320.000,00 sobre lo ganado y facturado (OPP-1202) | 480.000,00 | — | `50-comisiones/liquidacion-2026-10.csv` fila 3 |
| 7 | Descuento sin la aprobación que pide la matriz (`discount_outside_policy`) | COT-1205 · OPP-1230: el 22 % cae en el nivel 3, que pide gerente general, y lo aprobó Marta Gil como gerente comercial | 21.120.000,00 | — | `40-cotizaciones/COT-1205_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Ídem | COT-1204 · OPP-1229: el 22 % cae en el nivel 3, que pide gerente general, y lo aprobó Marta Gil como gerente comercial | 19.360.000,00 | — | `40-cotizaciones/COT-1204_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- `40-cotizaciones/COT-1204_cotizacion.pdf`
- `40-cotizaciones/COT-1205_cotizacion.pdf`
- `50-comisiones/liquidacion-2026-10.csv`
- `contratos/CTR-1205.json`, `CTR-1230.json`, `CTR-1231.json`, `CTR-1232.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1`, con 8 hallazgos. En la tabla de arriba quité la columna «Responsable», que salió vacía en las ocho filas. El archivo `corridas/salida-deal-scan.md` guarda el reporte tal como lo escribió el motor.