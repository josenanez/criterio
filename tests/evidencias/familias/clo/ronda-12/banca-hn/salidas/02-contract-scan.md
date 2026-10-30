# /criterio-legal:contract-scan 

Primera corrida: los seis contratos (CTR-4001 a CTR-4006) eran nuevos y los llevé a su ficha con la cita de cada documento. El motor no reportó `record_issues` ni nada sin procesar. Salieron cinco señales, y su revisión es de la persona.

Los términos ya estaban vigentes (versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-06), así que no hubo que registrar nada. Cuando la carpeta de estado `estado-legal/08010004578120-banco-de-occidente-sintetico/` fue un caso nuevo, la ficha de cada contrato quedó en `contratos/<código>.json`.

# Qué cambió en los contratos · Banco de Occidente Sintético · al 2026-10-06

**Entidad:** Banco de Occidente Sintético (08010004578120) · **Fecha de corte:** 2026-10-06 · **Agente:** Fidel, versión 1.2.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días |
|---|---|---|---|---|
| 1 | `signed_without_authority` | CTR-4001: Ana Lucía Pineda firmó por 12,000,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto (matriz, fila 2) | 12,000,000.00 | — |
| 2 | `payments_over_value` | CTR-4002: pagado 7,950,000.00 contra un valor de 7,500,000.00 con sus otrosíes (pagos, filas 6 y 7) | 450,000.00 | — |
| 3 | `renewal_notice_missed` | CTR-4001: el preaviso venció el 2026-10-01 sin decisión; el contrato se prorroga en sus términos el 2026-10-31 | — | 5 |
| 4 | `guarantee_expires_early` | CTR-4001: la póliza de cumplimiento vence el 2026-12-31 y el contrato la exige hasta el 2027-02-28 | — | 59 |
| 5 | `contract_obligation_overdue` | CTR-4004 · OBL-1 · Informe mensual de ejecución (agosto): venció el 2026-09-05 y no hay evidencia en `40-ejecucion/` (responsable: Licencias Digitales del Norte, S. de R.L.) | — | 31 |

**Lo que no se pudo procesar:** todo se procesó. **Preguntas que hice:** ninguna.

**Fuentes:** matriz de atribuciones, exportación de pagos 2026-09-30 y los contratos y la póliza de CTR-4001, CTR-4002 y CTR-4004 (con la cláusula 5 de este último).

Dos datos no los dice ningún documento y quedaron vacíos en las fichas: el monto asegurado y la fecha de entrega de cada póliza.

La salida completa quedó en `corridas/salida-contract-scan.md` y la corrida se registró como `2026-10-06-contract-scan-1`.