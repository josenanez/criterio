# /criterio-legal:contract-scan 

Los seis contratos (CTR-3601 a CTR-3606) eran nuevos en el inventario. Sus fichas ya existían y coinciden con los documentos, y el motor no reportó `record_issues`. Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez, así que no hubo que registrar nada.

# Qué cambió en los contratos · Banco del Valle Central Sintético · al 2026-10-06

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Firma sin facultad según la matriz (`signed_without_authority`) | CTR-3601: Gabriela Quesada firmó por 240.000.000,00 y la matriz no le da facultad para ese tipo y monto | 240.000.000,00 | — | — | `contratos/CTR-3601-…/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | Lo pagado supera el valor más otrosíes (`payments_over_value`) | CTR-3602: pagado 159.000.000,00 contra un valor de 150.000.000,00 con sus otrosíes | 9.000.000,00 | — | — | `10-registro/pagos-2026-09-30.csv` filas 6 y 7 · contrato CTR-3602 |
| 3 | Preaviso vencido sin decisión registrada (`renewal_notice_missed`) | CTR-3601: el preaviso venció el 2026-10-01 sin decisión; el contrato se prorroga en sus términos el 2026-10-31 | — | — | 5 | contrato CTR-3601 |
| 4 | Póliza vence antes de lo exigido (`guarantee_expires_early`) | CTR-3601: la póliza vence el 2026-12-31 y el contrato la exige hasta el 2027-02-28 | — | — | 59 | `contratos/CTR-3601-…/20-garantias/poliza-cumplimiento.md` |
| 5 | Obligación vencida sin evidencia (`contract_obligation_overdue`) | CTR-3604 · OBL-1, informe mensual de agosto: venció el 2026-09-05 y no hay evidencia en `40-ejecucion/` | — | Licencias Digitales S.A. | 31 | contrato CTR-3604, cláusula 5 |

- **Sin procesar:** nada, todo lo que llegó se procesó.
- **Preguntas hechas:** ninguna.
- **Registro de la corrida:** `2026-10-06-contract-scan-1`, con 5 hallazgos. La salida completa está en `estado-legal/3101457812-banco-del-valle-central-sintetico/corridas/salida-contract-scan.md`.

Ninguna de las señales es una opinión jurídica: son lo que muestran los documentos y las tablas.