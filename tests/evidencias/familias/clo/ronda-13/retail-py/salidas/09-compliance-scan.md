# /criterio-compliance:compliance-scan 

Términos vigentes (versión 1.3). El inventario no trae archivos nuevos, cambiados ni borrados frente a la corrida anterior. Calculé el periodo 2026-09 con `--today 2026-10-06`.

# Qué cambió en el cumplimiento · Distribuidora del Ybytyruzú Sintética · periodo 2026-09

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.3.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Osvaldo Ramírez | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Celeste Villalba | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 5 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`

La corrida quedó registrada como `2026-10-06-compliance-scan-1` con 5 hallazgos.

Dos aclaraciones sobre cómo salió esta corrida:
- Los términos ya figuraban como aceptados en la versión 1.3.0. No hubo nada que registrar a nombre de José Francisco Ñáñez.
- En el archivo `salida-compliance-scan.md` escribí la línea "(El motor dejó esta sección vacía.)" solo en esta respuesta. El archivo conserva la sección "El resultado" vacía, tal como la dejó el motor.