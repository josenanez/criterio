# /criterio-compliance:compliance-scan 

Desde la corrida anterior no hay archivos nuevos, cambiados ni borrados. El reporte sale de la matriz y los registros que ya estaban en la carpeta. La sección "El resultado" salió vacía del motor y la dejé así.

# Qué cambió en el cumplimiento · Lojas Paulistas · periodo 2026-09

**Entidad:** Lojas Paulistas (31452078000170) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.12.1 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolução sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaração mensal de origem de recursos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Marcelo Tavares | — | `00-referencia/matriz-obrigacoes.csv` fila 10 |
| 4 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflitos de interesses: su revisión vencía el 2026-08-31 | — | Camila Duarte | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 5 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Relatório de brindes e convites: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obrigacoes.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del último informe de cumplimiento
- ¿Dónde están las fichas de Fidel? → estado-legal/31452078000170-lojas-paulistas/contratos
- ¿Dónde guardo lo que encuentro? → estado-legal/31452078000170-lojas-paulistas, el estado ya creado por Fidel
- ¿Dejo la marca _CRITERIO_LEGAL.txt en la carpeta? → None

## Fuentes

- `00-referencia/matriz-obrigacoes.csv`
- `20-politicas/indice-politicas.csv`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`

La salida quedó en `estado-legal/31452078000170-lojas-paulistas/corridas/salida-compliance-scan.md`. La corrida quedó registrada con el id `2026-10-06-compliance-scan-1` y 5 hallazgos.

Los términos ya estaban vigentes, así que no registré ninguna aceptación nueva a nombre de José Francisco Ñáñez.