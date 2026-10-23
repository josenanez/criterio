# /criterio-legal:contract-execution 

Los términos de la versión 1.2 ya estaban vigentes, aceptados el 2026-10-06, así que no hizo falta registrar la aceptación. El reporte solo marca un contrato con pagos por encima del valor: CTR-202. No trae ninguna fila de garantías ni de pagos después de la terminación. El motor registró la corrida con 4 hallazgos, pero el reporte solo detalla uno, y no sé a qué corresponden los otros tres.

# Pagos y garantías · Cooperativa Sierra Alta · al 2026-10-06

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.8.0 · **Comando:** `contract-execution`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo pagado supera el valor del contrato más sus otrosíes (`payments_over_value`) | CTR-202: pagado 105,999.99 contra un valor de 100,000.00 con sus otrosíes | 5,999.99 | — | — | `10-registro/pagos-2026-09-30.csv` fila 6 · `10-registro/pagos-2026-09-30.csv` fila 7 · `contratos/CTR-202-suministros-quito-s-a/10-contrato/contrato.md` |

## El resultado

| Contrato | Valor con otrosíes | Pagado | Saldo | Último pago |
|---|---|---|---|---|
| CTR-201 | 160,000.00 | 48,000.00 | 112,000.00 | 2026-09-10 |
| CTR-202 | 100,000.00 | 105,999.99 | -5,999.99 | 2026-09-10 |
| CTR-203 | 120,000.00 | 36,000.00 | 84,000.00 | 2026-08-10 |
| CTR-204 | 60,000.00 | 18,000.00 | 42,000.00 | 2026-09-10 |
| CTR-205 | 40,000.00 | 12,000.00 | 28,000.00 | 2026-09-10 |
| CTR-206 | 100,000.00 | 30,000.00 | 70,000.00 | 2026-07-10 |
| CTR-207 | 60,000.00 | 18,000.00 | 42,000.00 | 2026-09-10 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-registro/pagos-2026-09-30.csv`
- `contratos/CTR-202-suministros-quito-s-a/10-contrato/contrato.md`

La salida quedó en `estado-legal/1790012345001-cooperativa-sierra-alta/corridas/salida-contract-execution.md`. La corrida quedó registrada como `2026-10-06-contract-execution-1`.