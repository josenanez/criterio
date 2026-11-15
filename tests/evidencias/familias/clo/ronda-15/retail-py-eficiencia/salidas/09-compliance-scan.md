# /criterio-compliance:compliance-scan 

Desde la corrida anterior no llegó ningún archivo nuevo, ni cambió ni se borró ninguno. En 30-normativa solo está el registro normativo, que procesa el motor, así que no hay boletín que extraer. Las señales del periodo siguen abiertas, y la fuente de OB-13 sigue esperando la respuesta de la persona.

# Qué cambió en el cumplimiento · Distribuidora del Ybytyruzú Sintética · periodo 2026-09

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.6.3 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 3 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Osvaldo Ramírez | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Celeste Villalba | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 5 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09 (respuesta sugerida por los documentos: es el único periodo con informe en 20-reportes; sesión de prueba sin interfaz)
- ¿Cuál es el plazo de respuesta del canal de denuncias? → 15 días (respuesta sugerida: la fijada en el setup de Fidel; sesión de prueba sin interfaz)
- ¿Cuántos días hay para evaluar una norma nueva? → 30 días (respuesta sugerida: la fijada en el setup de Fidel; sesión de prueba sin interfaz)
- ¿De qué norma, contrato o política sale la obligación OB-13 (Reporte de regalos e invitaciones)? La matriz no trae fuente. → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`

---

La corrida quedó registrada como `2026-10-06-compliance-scan-1`. Lo de arriba está guardado en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-compliance-scan.md`. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06, así que no hubo que volver a mostrarlos.

El motor dejó vacía la sección «El resultado». También escribió `None` donde falta la respuesta sobre OB-13, cuando debería decir que no hay respuesta. Así viene del motor y no lo cambié.