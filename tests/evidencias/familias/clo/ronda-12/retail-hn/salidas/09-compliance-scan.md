# /criterio-compliance:compliance-scan 

Ya terminé; solo falta mostrarte el reporte. Los términos ya estaban vigentes, así que no registré ninguna aceptación.

Desde la corrida anterior no hay archivos nuevos, cambiados ni borrados en la carpeta. Las señales de abajo salen de las tablas ya cargadas, evaluadas a la fecha de la prueba.

# Qué cambió en el cumplimiento · Almacenes del Valle de Sula · periodo 2026-09

**Entidad:** Almacenes del Valle de Sula (08010006129040) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.2.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un caso del canal de denuncias pasó el plazo de respuesta configurado (`report_case_overdue`) | caso C-003: recibido el 2026-08-28, lleva 39 días sin respuesta y el plazo es de 15 | — | — | 39 | `40-canal/casos.csv` fila 4 |
| 2 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | María José Funes | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 3 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Ricardo Lagos Paz | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 4 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | Ricardo Lagos Paz | — | `00-referencia/matriz-obligaciones.csv` fila 11 |
| 5 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 12 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del último informe de cumplimiento
- ¿Plazo de respuesta del canal de denuncias? → 15 días (valor propuesto por defecto)
- ¿Días para evaluar una norma nueva? → 30 días (valor propuesto por defecto)
- ¿Dónde están las fichas de Fidel? → estado-legal/08010006129040-almacenes-del-valle-de-sula/contratos
- ¿Dejo el archivo _CRITERIO_LEGAL.txt en la carpeta de documentos? → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `40-canal/casos.csv`

La sección "El resultado" salió vacía en el reporte del motor y la dejé así. La corrida quedó registrada como `2026-10-06-compliance-scan-1` con 5 hallazgos. La salida completa está en `estado-legal/08010006129040-almacenes-del-valle-de-sula/corridas/salida-compliance-scan.md`.