# /criterio-legal:contract-execution 

Los términos estaban vigentes (versión 1.5), así que no hizo falta registrar la aceptación. Esta es la revisión de pagos y garantías de Distribuidora del Ybytyruzú Sintética (88612904-4), con corte al 2026-10-06. Dejó dos señales por atender.

# Pagos y garantías · Distribuidora del Ybytyruzú Sintética · al 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Pago con fecha posterior a la terminación del contrato (`payment_after_termination`) | CTR-4506: 1 pago después de la terminación del 2026-07-31 | 82.500.000,00 | — | `10-registro/pagos-2026-09-30.csv` fila 20 |
| 2 | La póliza vence antes de lo que exige el contrato (`guarantee_expires_early`) | CTR-4501: la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 | — | 61 | `contratos/CTR-4501-logistica-del-chaco-sintetica-s-a/20-garantias/poliza-cumplimiento.md` |

## El resultado

| Contrato | Valor con otrosíes | Pagado | Saldo | Último pago |
|---|---|---|---|---|
| CTR-4501 | 2.640.000.000,00 | 792.000.000,00 | 1.848.000.000,00 | 2026-09-10 |
| CTR-4502 | 1.650.000.000,00 | 495.000.000,00 | 1.155.000.000,00 | 2026-09-10 |
| CTR-4503 | 1.980.000.000,00 | 594.000.000,00 | 1.386.000.000,00 | 2026-09-10 |
| CTR-4504 | 990.000.000,00 | 297.000.000,00 | 693.000.000,00 | 2026-09-10 |
| CTR-4505 | 660.000.000,00 | 198.000.000,00 | 462.000.000,00 | 2026-09-10 |
| CTR-4506 | 1.650.000.000,00 | 577.500.000,00 | 1.072.500.000,00 | 2026-09-10 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó.
**Las preguntas que hizo:** ninguna en esta corrida.
**Fuentes:** `10-registro/pagos-2026-09-30.csv` y la póliza de cumplimiento de CTR-4501.

Dejé la salida en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-contract-execution.md`. La corrida quedó registrada como `2026-10-06-contract-execution-1`, con 5 hallazgos.