# /criterio-compliance:compliance-scan 

Desde la corrida anterior no hay archivos nuevos, cambiados ni borrados. Las señales salen de las tablas y de la ficha del periodo, que ya traía el informe y el boletín de agosto. La pregunta sobre el responsable de OB-12 sigue sin respuesta.

# Qué cambió en el cumplimiento · Banco Valle de Anáhuac · periodo 2026-09

**Entidad:** Banco Valle de Anáhuac (BVA150301K21) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.11.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Mónica Garza | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-07 · Circular sintética 007 de 2026: registrada el 2026-08-25, lleva 42 días sin evaluación de impacto | — | — | 42 | `30-normativa/boletin-2026-08.md, punto 1` |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-1301 · OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-1301-sistemas-financieros-s-a-de-c-v/10-contrato/contrato.md, cláusula 7` |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés: no tiene responsable | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el más reciente con informe de cumplimiento (propuesta tomada de los documentos)
- ¿Plazo de respuesta del canal de denuncias y días para evaluar una norma nueva? → 15 y 30 días, los valores por defecto de la configuración
- ¿Dónde están las fichas de Fidel? → estado-legal/BVA150301K21-banco-valle-de-anahuac/contratos (carpeta comprobada)
- ¿Quién responde por OB-12, que no tiene responsable en la matriz? → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/boletin-2026-08.md, punto 1`
- `contratos/CTR-1301-sistemas-financieros-s-a-de-c-v/10-contrato/contrato.md, cláusula 7`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`

La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con 5 hallazgos.