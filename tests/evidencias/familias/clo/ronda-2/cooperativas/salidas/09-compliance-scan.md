# /criterio-compliance:compliance-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior; el motor encontró cinco señales en el periodo 2026-09. La sección «El resultado» llegó vacía del motor.

# Qué cambió en el cumplimiento · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-07 · Circular sintética 007 de 2026: registrada el 2026-08-25, lleva 42 días sin evaluación de impacto | — | — | 42 | `30-normativa/boletin-2026-08.md, línea 5` |
| 3 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Gabriela Mora | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 5 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | Esteban Jácome | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del informe de cumplimiento presentado el 2026-10-05
- ¿Plazo de respuesta del canal de denuncias y días para evaluar una norma nueva? → 15 y 30 días, los de la configuración de Fidel para esta entidad
- ¿Dónde están las fichas de Fidel? → estado-legal/1790012345001-cooperativa-sierra-alta/contratos

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/boletin-2026-08.md, línea 5`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`