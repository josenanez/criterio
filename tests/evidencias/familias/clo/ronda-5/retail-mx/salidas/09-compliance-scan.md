# /criterio-compliance:compliance-scan 

No hubo archivos nuevos, cambiados ni borrados desde la corrida anterior. Procesé el periodo 2026-09, el último con informe de cumplimiento. El informe declara "con observaciones" y el motor encontró 5 señales abiertas.

# Qué cambió en el cumplimiento · Tiendas del Bajío · periodo 2026-09

**Entidad:** Tiendas del Bajío (TBA180912Q37) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.11.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Sofía Elizondo | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Jorge Salgado | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 5 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el último con informe de cumplimiento (respuesta sugerida a partir de los documentos)
- ¿Dejo el archivo _CRITERIO_LEGAL.txt en la carpeta de documentos? → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`

La corrida quedó registrada como `2026-10-06-compliance-scan-1` con 5 hallazgos. Lo que mostré está en `estado-legal/TBA180912Q37-tiendas-del-bajio/corridas/salida-compliance-scan.md`.

Dos cosas que debes saber:
- La sección "El resultado" salió vacía en el reporte del motor. La mostré tal cual y no la rellené.
- Cuando generé el reporte la primera vez, lo redirigí a un archivo temporal en `corridas/` con `>` y `&&`. El comando pedía llamadas simples, sin esos operadores. Borré ese archivo y el registro final salió de la salida escrita con Write.