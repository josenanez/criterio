# /criterio-compliance:compliance-scan 

La corrida quedó registrada. No hubo archivos nuevos, cambiados ni borrados desde la corrida anterior, y el motor recalculó el periodo 2026-09 con cinco señales. Los términos ya estaban vigentes, así que no se mostraron ni registré la aceptación a nombre de José Francisco Ñáñez.

# Qué cambió en el cumplimiento · Almacenes del Canal · periodo 2026-09

**Entidad:** Almacenes del Canal (155791002-2-2017) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.1.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Abdiel Moreno | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Yamileth Castillo | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-3001 · OBL-3 · Reporte de operaciones al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-3001-logistica-colon-s-a/10-contrato/contrato.md, cláusula 7` |
| 4 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Abdiel Moreno | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés: no tiene responsable | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del informe más reciente
- ¿Plazo de respuesta del canal de denuncias y días para evaluar una norma nueva? → 15 y 30 días, los de config.example.json
- ¿Dónde están las fichas de Fidel? → estado-legal/155791002-2-2017-almacenes-del-canal/contratos
- ¿Dejo la marca _CRITERIO_LEGAL.txt en la carpeta de documentos? → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `30-normativa/registro-normativo.csv`
- `contratos/CTR-3001-logistica-colon-s-a/10-contrato/contrato.md, cláusula 7`

Lo que queda guardado:
- **Salida:** `<espacio>/estado-legal/155791002-2-2017-almacenes-del-canal/corridas/salida-compliance-scan.md`.
- **Corrida:** `2026-10-06-compliance-scan-1`, con 5 hallazgos.