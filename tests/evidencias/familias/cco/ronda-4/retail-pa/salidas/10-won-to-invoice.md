# /criterio-revenue:won-to-invoice 

Hay 3 oportunidades ganadas sin contrato y 2 contratos firmados con la factura vencida. Los términos ya estaban vigentes, así que no registré ninguna aceptación.

# De lo ganado a la factura · Almacenes del Istmo · periodo 2026-11

**Entidad:** Almacenes del Istmo (155622222-2-2017) · **Fecha de corte:** 2026-11-05 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 1.4.2 · **Comando:** `won-to-invoice`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Oportunidad ganada sin contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-2608 · Venta de equipos: ganada el 2026-10-05 por 75,000.00; las fichas de Fidel no tienen un contrato firmado con el cliente 830026002 | 75,000.00 | — | 31 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 9 |
| 2 | Oportunidad ganada sin contrato firmado (`won_without_contract`) | OPP-2630 · Venta directa 30: ganada el 2026-10-07 por 60,000.00; sin contrato firmado con el cliente 830026008 | 60,000.00 | — | 29 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 20 |
| 3 | Contrato firmado sin factura en la ficha de Clara dentro del plazo (`signed_without_invoice`) | CTR-2631: firmado con el cliente 830026010 el 2026-09-09; no hay factura emitida a ese cliente hasta el 2026-10-09 | 60,000.00 | — | 27 | `contratos/CTR-2631.json` |
| 4 | Oportunidad ganada sin contrato firmado (`won_without_contract`) | OPP-2629 · Venta directa 29: ganada el 2026-10-06 por 45,000.00; sin contrato firmado con el cliente 830026007 | 45,000.00 | — | 30 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 19 |
| 5 | Contrato firmado sin factura dentro del plazo (`signed_without_invoice`) | CTR-2630: firmado con el cliente 830026009 el 2026-09-08; no hay factura emitida a ese cliente hasta el 2026-10-08 | 45,000.00 | — | 28 | `contratos/CTR-2630.json` |

## El resultado

| Oportunidad ganada | Cuenta | Monto | Ganada | Contrato (Fidel) | Factura (Clara) |
|---|---|---|---|---|---|
| OPP-2601 · Renovación de licencias | Supermercados Bahía S.A. | 180,000.00 | 2026-10-10 | CTR-2601 | FE-2601 |
| OPP-2602 · Proyecto de expansión | Distribuidora Colón S.A. | 270,000.00 | 2026-10-22 | CTR-2602 | FE-2602 |
| OPP-2608 · Venta de equipos | Farmacias Chiriquí S.A. | 75,000.00 | 2026-10-05 | — | — |
| OPP-2629 · Venta directa 29 | Cliente Comercial 2650 S.A. | 45,000.00 | 2026-10-06 | — | — |
| OPP-2630 · Venta directa 30 | Cliente Comercial 2651 S.A. | 60,000.00 | 2026-10-07 | — | — |

| Contrato | Cliente | Firmado | Plazo de facturación | Factura | Estado |
|---|---|---|---|---|---|
| CTR-2601 | 830026000 | 2026-10-13 | 2026-11-12 | FE-2601 | facturado |
| CTR-2602 | 830026001 | 2026-10-24 | 2026-11-23 | FE-2602 | facturado |
| CTR-2603 | 830026004 | 2026-10-20 | 2026-11-19 | — | en plazo |
| CTR-2630 | 830026009 | 2026-09-08 | 2026-10-08 | — | vencido |
| CTR-2631 | 830026010 | 2026-09-09 | 2026-10-09 | — | vencido |

Plazo de facturación configurado: 30 días. Los contratos y las facturas son los de las fichas de Fidel y de Clara: no se vuelven a procesar.

## Lo que no se pudo procesar

- `50-comisiones/`: no está la liquidación de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- `contratos/CTR-2630.json`
- `contratos/CTR-2631.json`

La corrida quedó registrada como `2026-11-05-won-to-invoice-1`. Su salida está en `estado-comercial/155622222-2-2017-almacenes-del-istmo/corridas/salida-won-to-invoice.md`.

Pasé el reporte a este mensaje con el encabezado y las señales en abreviado, por lo que no es copia literal del archivo que registré. En la salida registrada, la nota inicial va antes del encabezado, y el reporte del motor va completo, con sus filas de señales sin recortar.