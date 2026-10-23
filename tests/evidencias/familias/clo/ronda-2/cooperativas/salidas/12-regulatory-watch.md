# /criterio-compliance:regulatory-watch 

Los términos vigentes de esta versión ya estaban aceptados a nombre de José Francisco Ñáñez (2026-10-06). La norma N-2026-07 del boletín de agosto no estaba en el registro. Ya estaba en la ficha del periodo como "por evaluar", así que no la modifiqué.

# Normas nuevas · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `regulatory-watch`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-07 · Circular sintética 007 de 2026: registrada el 2026-08-25, lleva 42 días sin evaluación de impacto | — | — | 42 | `30-normativa/boletin-2026-08.md, línea 5` |
| 2 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |

## El resultado

| Id | Norma | Registrada | Aplica | Evaluada |
|---|---|---|---|---|
| N-2026-01 | Resolución sintética 001 de 2026 | 2026-03-10 | sí | sí |
| N-2026-02 | Circular sintética 002 de 2026 | 2026-05-02 | no | sí |
| N-2026-04 | Resolución sintética 004 de 2026 | 2026-06-01 | sí | sí |
| N-2026-07 | Circular sintética 007 de 2026 | 2026-08-25 | por evaluar | no |

Sin opinión sobre el alcance de ninguna norma: si aplica y qué exige lo decide la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del informe de cumplimiento presentado el 2026-10-05
- ¿Plazo de respuesta del canal de denuncias y días para evaluar una norma nueva? → 15 y 30 días, los de la configuración de Fidel para esta entidad
- ¿Dónde están las fichas de Fidel? → estado-legal/1790012345001-cooperativa-sierra-alta/contratos

## Fuentes

- `30-normativa/boletin-2026-08.md, línea 5`
- `30-normativa/registro-normativo.csv`

La corrida quedó registrada como `2026-10-06-regulatory-watch-1`. Dejé lo mostrado en `estado-legal/1790012345001-cooperativa-sierra-alta/corridas/salida-regulatory-watch.md`.