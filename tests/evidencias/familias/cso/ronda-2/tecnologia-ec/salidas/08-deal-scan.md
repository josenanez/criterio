# /criterio-revenue:deal-scan 

Corrida de prueba sin interfaz: los términos vigentes (v1.3) ya estaban aceptados por José Francisco Ñáñez. Las 5 cotizaciones de `40-cotizaciones` pasaron a la ficha del periodo. COT-1801 quedó sin aprobación porque el documento dice que está dentro del nivel sin aprobación.

# Qué cambió en lo vendido · Sistemas Integrados del Guayas · periodo 2026-10

**Entidad:** Sistemas Integrados del Guayas (0990234566001) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 0.2.0 · **Comando:** `deal-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Contrato firmado sin factura en la ficha de Clara dentro del plazo (`signed_without_invoice`) | CTR-1805: firmado con el cliente 1791800060001 el 2026-09-10; no hay factura emitida a ese cliente hasta el 2026-10-10 | 96,000.00 | — | 26 | `contratos/CTR-1805.json` |
| 2 | Ídem (`signed_without_invoice`) | CTR-1832: cliente 1791800117001, firmado el 2026-09-10; sin factura hasta el 2026-10-10 | 60,000.00 | — | 26 | `contratos/CTR-1832.json` |
| 3 | Ídem (`signed_without_invoice`) | CTR-1831: cliente 1791800109001, firmado el 2026-09-09; sin factura hasta el 2026-10-09 | 48,000.00 | — | 27 | `contratos/CTR-1831.json` |
| 4 | Oportunidad ganada sin contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1831 · Venta directa 31: ganada el 2026-10-06 por 36,000.00; sin contrato firmado con el cliente 1791800087001 | 36,000.00 | — | 30 | `10-crm/Deals_2026_11_03.csv` fila 20 |
| 5 | Contrato firmado sin factura (`signed_without_invoice`) | CTR-1830: cliente 1791800095001, firmado el 2026-09-08; sin factura hasta el 2026-10-08 | 36,000.00 | — | 28 | `contratos/CTR-1830.json` |
| 6 | Comisión liquidada distinta de la del plan (`commission_differs_from_plan`) | 2026-10 · Valeria Zambrano: se liquidaron 7,200.00 y el plan da 6,480.00 sobre lo ganado y facturado (OPP-1802) | 720.00 | — | — | `50-comisiones/liquidacion-2026-10.csv` fila 3 |
| 7 | Descuento fuera de la matriz (`discount_outside_policy`) | COT-1805 · OPP-1830: el 22 % cae en el nivel 3, que pide aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 31,680.00 | — | — | `40-cotizaciones/COT-1805_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |
| 8 | Descuento fuera de la matriz (`discount_outside_policy`) | COT-1804 · OPP-1829: el 22 % cae en el nivel 3, que pide aprobación de gerente general, y lo aprobó Marta Gil como gerente comercial | 29,040.00 | — | — | `40-cotizaciones/COT-1804_cotizacion.pdf` · `00-referencia/matriz-descuentos.csv` fila 4 |

## El resultado

**Cotizaciones en la ficha:** 5 · **Exportación:** `10-crm/Deals_2026_11_03.csv`

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-descuentos.csv`
- `10-crm/Deals_2026_11_03.csv`
- `40-cotizaciones/COT-1804_cotizacion.pdf`
- `40-cotizaciones/COT-1805_cotizacion.pdf`
- `50-comisiones/liquidacion-2026-10.csv`
- `contratos/CTR-1805.json`
- `contratos/CTR-1830.json`
- `contratos/CTR-1831.json`
- `contratos/CTR-1832.json`

La corrida quedó registrada como `2026-11-05-deal-scan-1` con 8 hallazgos. Lo mostrado está en `estado-comercial/0990234566001-sistemas-integrados-del-guayas/corridas/salida-deal-scan.md`.