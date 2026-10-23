# /criterio-compliance:compliance-scan 

Nada nuevo ni cambiado en la carpeta desde la corrida anterior (59 archivos, sin ilegibles). El motor recalculó el periodo 2026-09 y salieron 5 señales.

# Qué cambió en el cumplimiento · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Verónica Paz | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Verónica Paz | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-401 · OBL-3 · Reporte de operaciones al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md, cláusula 7` |
| 5 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | Mauricio León | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el último con informe de cumplimiento (propuesta tomada de los documentos)
- ¿Dónde están las fichas de Fidel? → estado-legal/0990054321001-minera-condor/contratos (comprobado en disco)

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`
- `contratos/CTR-401-perforaciones-del-sur-s-a/10-contrato/contrato.md, cláusula 7`

La sección «El resultado» salió vacía en el reporte del motor. No la completé, porque no puedo escribir cifras que el motor no dio.

Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-06, así que no hizo falta registrarlos de nuevo. La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con la salida en `estado-legal/0990054321001-minera-condor/corridas/salida-compliance-scan.md`.