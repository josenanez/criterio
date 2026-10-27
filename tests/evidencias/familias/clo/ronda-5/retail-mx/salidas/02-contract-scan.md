# /criterio-legal:contract-scan 

Primera corrida: se extrajeron las fichas de los 6 contratos con documento (CTR-1401 a CTR-1406). El motor marcó 5 señales; las cifras y fechas son las del reporte.

# Qué cambió en los contratos · Tiendas del Bajío · al 2026-10-06

**Entidad:** Tiendas del Bajío (TBA180912Q37) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.11.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `signed_without_authority` | CTR-1402 · OT-1: Sofía Elizondo firmó el otrosí que lleva el contrato a 2,420,000.00 sin facultad para ese monto | 1,540,000.00 | — | `contratos/CTR-1402-…/10-contrato/otrosi-1.md` |
| 2 | `renewal_notice_missed` | CTR-1401: el preaviso venció el 2026-10-01 sin decisión; el contrato se prorroga en sus términos el 2026-10-31 | — | 5 | `contratos/CTR-1401-…/10-contrato/contrato.md` |
| 3 | `unsigned_contract` | CTR-1405: el documento no tiene la firma de las dos partes y el contrato empezó el 2026-02-01 | 440,000.00 | — | `contratos/CTR-1405-…/10-contrato/contrato.md` |
| 4 | `payment_after_termination` | CTR-1406: 1 pago después de la terminación del 2026-07-31, por 55,000.00 | 55,000.00 | — | `10-registro/pagos-2026-09-30.csv` fila 20 |
| 5 | `register_mismatch` | CTR-1409: está en el registro y no hay documento en `contratos/CTR-1409…/10-contrato/` | — | — | `10-registro/registro-contratos.csv` fila 8 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

La corrida quedó registrada con el id `2026-10-06-contract-scan-1` (5 hallazgos). El reporte está en `estado-legal/TBA180912Q37-tiendas-del-bajio/contratos/reporte-contract-scan.md` y lo que se mostró aquí, en `corridas/salida-contract-scan.md`.