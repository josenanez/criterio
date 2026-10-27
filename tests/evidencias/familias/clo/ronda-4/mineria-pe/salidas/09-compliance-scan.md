# /criterio-compliance:compliance-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior; la ficha del periodo ya recogía el informe y la norma del boletín. Salieron cinco señales.

# Qué cambió en el cumplimiento · Minera Puna Alta · periodo 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.10.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-07 · Circular sintética 007 de 2026: registrada el 2026-08-25, lleva 42 días sin evaluación de impacto | — | — | 42 | `30-normativa/boletin-2026-08.md, punto 1` |
| 3 | Una norma que aplica no tiene ninguna obligación en la matriz (`applicable_norm_not_in_matrix`) | N-2026-04 · Resolución sintética 004 de 2026: aplica y ninguna obligación de la matriz la cita | — | — | — | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Carmen Rojas | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 5 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | Óscar Mendoza | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y país? → Minera Puna Alta, RUC 20730000015, Perú (PEN), según la marca de la carpeta y la configuración de Fidel
- ¿Qué periodo se evalúa? → 2026-09, el último con informe de cumplimiento
- ¿Plazo de respuesta del canal de denuncias y días para evaluar una norma? → 15 y 30 días, los valores que ya usa la configuración de Fidel
- ¿Dónde están las fichas de Fidel? → estado-legal/20730000015-minera-puna-alta/contratos/, comprobada: tiene 7 fichas CTR-801 a CTR-807
- ¿Dónde guardo lo que encuentro? → estado-legal/20730000015-minera-puna-alta, fuera de los documentos
- ¿Dejo la marca _CRITERIO_LEGAL.txt en la carpeta? → No hace falta: ya está marcada desde el 2026-10-27

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/boletin-2026-08.md, punto 1`
- `30-normativa/registro-normativo.csv`
- `40-canal/casos.csv`

La corrida quedó registrada como `2026-10-06-compliance-scan-1` con 5 hallazgos.