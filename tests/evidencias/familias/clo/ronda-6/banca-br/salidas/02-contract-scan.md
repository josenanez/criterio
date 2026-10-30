# /criterio-legal:contract-scan 

Las seis fichas ya existían de la configuración inicial y coinciden con sus documentos, así que no corregí nada. El motor no devolvió `record_issues`. Los términos (versión 1.3) ya estaban aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06, así que no hizo falta registrarlos de nuevo. Todo se corrió con `--today 2026-10-06`.

# Qué cambió en los contratos · Banco Serra Verde · al 2026-10-06

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días |
|---|---|---|---|---|---|
| 1 | `signed_without_authority` | CTR-1601: Paulo Nogueira firmó por 560.000,00 y la matriz de atribuciones no le da facultad para ese tipo y monto | 560.000,00 | — | — |
| 2 | `contract_obligation_overdue` | CTR-1604 · OBL-1, relatório mensal de agosto: venció el 2026-09-05 y no hay evidencia en 40-ejecucion/ | — | Licenças Digitais Ltda. | 31 |
| 3 | `notice_deadline_near` | CTR-1604: el preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie decidió | — | — | 26 |
| 4 | `guarantee_missing` | CTR-1603: exige garantía de calidad y no hay póliza aportada en 20-garantias/ | — | — | — |
| 5 | `register_differs_from_contract` | CTR-1602: valor 420.000,00 en el registro y 350.000,00 en el documento | — | — | — |

La sección «El resultado» del reporte salió vacía. Todo lo que llegó se procesó y no hubo preguntas en esta corrida.

## Registro

- **Reporte:** `<estado>/contratos/reporte-contract-scan.md` (el motor lo escribe ahí).
- **Salida:** `<espacio>/estado-legal/52817460000100-banco-serra-verde/corridas/salida-contract-scan.md`.
- **Corrida:** `2026-10-06-contract-scan-1`, con 5 hallazgos.

Sin opinión jurídica: lo que implica cada señal para la firma, la garantía o el preaviso queda para la persona.