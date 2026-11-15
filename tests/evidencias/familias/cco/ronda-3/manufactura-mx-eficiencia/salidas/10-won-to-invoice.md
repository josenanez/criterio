# /criterio-revenue:won-to-invoice 

# De lo ganado a la factura · Manufacturas del Bajío · periodo 2026-10

**Entidad:** Manufacturas del Bajío (MBA120315KT4) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-11-05 · **Agente:** Valeria, versión 1.2.3 · **Comando:** `won-to-invoice`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1405: firmado con el cliente CMA150606F55 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 960,000.00 | — | 26 | `contratos/CTR-1405.json` |
| 2 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1432: firmado con el cliente CMA210312L114 el 2026-09-10 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-10 | 600,000.00 | — | 26 | `contratos/CTR-1432.json` |
| 3 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1431 · Venta directa 31: ganada el 2026-10-07 por 480,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CMA180909I81 | 480,000.00 | — | 29 | `10-crm/oportunidades-2026-11-03.csv` fila 20 |
| 4 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1431: firmado con el cliente CMA200211K103 el 2026-09-09 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-09 | 480,000.00 | — | 27 | `contratos/CTR-1431.json` |
| 5 | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel (`won_without_contract`) | OPP-1430 · Venta directa 30: ganada el 2026-10-06 por 360,000.00 y las fichas de Fidel no tienen un contrato firmado con el cliente CMA170808H70 | 360,000.00 | — | 30 | `10-crm/oportunidades-2026-11-03.csv` fila 19 |
| 6 | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación (`signed_without_invoice`) | CTR-1430: firmado con el cliente CMA190110J92 el 2026-09-08 y las fichas de Clara no tienen una factura emitida a ese cliente hasta el 2026-10-08 | 360,000.00 | — | 28 | `contratos/CTR-1430.json` |

## El resultado

| Oportunidad ganada | Cuenta | Monto | Ganada | Contrato (Fidel) | Factura (Clara) |
|---|---|---|---|---|---|
| OPP-1401 · Renovación de licencias | 001A0000140000AaQZ | 1,440,000.00 | 2026-10-10 | CTR-1401 | FE-1401 |
| OPP-1402 · Proyecto de expansión | 001A0000140001AaQZ | 2,160,000.00 | 2026-10-22 | CTR-1402 | FE-1402 |
| OPP-1430 · Venta directa 30 | 001A0000140007AaQZ | 360,000.00 | 2026-10-06 | — | — |
| OPP-1431 · Venta directa 31 | 001A0000140008AaQZ | 480,000.00 | 2026-10-07 | — | — |

| Contrato | Cliente | Firmado | Plazo de facturación | Factura | Estado |
|---|---|---|---|---|---|
| CTR-1401 | CMA100101A00 | 2026-10-13 | 2026-11-12 | FE-1401 | facturado |
| CTR-1402 | CMA110202B11 | 2026-10-24 | 2026-11-23 | FE-1402 | facturado |
| CTR-1403 | CMA140505E44 | 2026-10-20 | 2026-11-19 | — | en plazo |
| CTR-1405 | CMA150606F55 | 2026-09-10 | 2026-10-10 | — | vencido |
| CTR-1430 | CMA190110J92 | 2026-09-08 | 2026-10-08 | — | vencido |
| CTR-1431 | CMA200211K103 | 2026-09-09 | 2026-10-09 | — | vencido |
| CTR-1432 | CMA210312L114 | 2026-09-10 | 2026-10-10 | — | vencido |

Plazo de facturación configurado: 30 días. Los contratos y las facturas son los de las fichas de Fidel y de Clara: no se vuelven a procesar.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-crm/oportunidades-2026-11-03.csv`
- `contratos/CTR-1405.json`
- `contratos/CTR-1430.json`
- `contratos/CTR-1431.json`
- `contratos/CTR-1432.json`

---
Notas de la corrida:
- Los términos (versión 1.5) ya estaban vigentes y aceptados, así que no hizo falta registrar de nuevo la aceptación de José Francisco Ñáñez.
- Usé el periodo 2026-10, que es el de la configuración, porque el comando no indicaba otro.
- El reporte quedó en `estado-comercial/MBA120315KT4-manufacturas-del-bajio/corridas/salida-won-to-invoice.md` y la corrida se registró como `2026-11-05-won-to-invoice-1` (9 hallazgos).