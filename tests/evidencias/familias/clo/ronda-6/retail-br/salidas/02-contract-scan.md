# /criterio-legal:contract-scan 

Las fichas de los seis contratos con documentos ya estaban extraídas, y las de CTR-1701 y CTR-1702 coinciden con lo que dicen los documentos. No revisé las otras cuatro fichas una por una: el motor no reportó `record_issues` al calcular. Los términos 1.3 ya estaban aceptados a nombre de José Francisco Ñáñez el 2026-10-06, así que no hubo que registrarlos de nuevo.

# Qué cambió en los contratos · Lojas Paulistas · al 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `signed_without_authority` | CTR-1702 · OT-1: Marcelo Tavares firmó el otrosí que lleva el contrato a 605.000,00 sin facultad para ese monto | 385.000,00 | — | `contratos/CTR-1702-embalagens-do-vale-ltda/10-contrato/aditivo-1.md` |
| 2 | `contract_expiring` | CTR-1703: vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar | 330.000,00 | 50 | `contratos/CTR-1703-shopping-centro-sul-s-a/10-contrato/contrato.md` |
| 3 | `payment_after_termination` | CTR-1706: 1 pago después de la terminación del 2026-07-31 | 13.750,00 | — | `10-registro/pagamentos-2026-09-30.csv` fila 20 |
| 4 | `guarantee_expires_early` | CTR-1701: la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 | — | 61 | `contratos/CTR-1701-logistica-paulista-ltda/20-garantias/apolice-cumprimento.md` |
| 5 | `register_mismatch` | CTR-1709: está en el registro y no hay documento en `contratos/CTR-1709…/10-contrato/` | — | — | `10-registro/registro-contratos.csv` fila 8 |

Todo lo que llegó se procesó, y el agente no hizo preguntas en esta corrida.

La salida quedó en `estado-legal/31452078000170-lojas-paulistas/corridas/salida-contract-scan.md`. La corrida quedó registrada como `2026-10-06-contract-scan-1`, con cinco hallazgos. El reporte completo del motor está en `contratos/reporte-contract-scan.md`, en la misma carpeta de estado.