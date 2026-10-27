# /criterio-compliance:compliance-scan 

Términos vigentes, sin archivos nuevos, cambiados ni borrados desde la corrida anterior. El motor calculó cinco señales abiertas para el periodo 2026-09.

# Qué cambió en el cumplimiento · Banco Ribera · periodo 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.10.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Claudia Salinas | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Martín Paredes | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-701 · OBL-3 · Reporte de operaciones al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-701-tecnologia-limena-s-a-c/10-contrato/contrato.md, cláusula 7` |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés: no tiene responsable | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el último con informe de cumplimiento (propuesta tomada de los documentos)
- ¿Dónde están las fichas de Fidel? → estado-legal/20710000019-banco-ribera/contratos (ruta comprobada)
- ¿Dejo el archivo _CRITERIO_LEGAL.txt en la carpeta de documentos? → None

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `contratos/CTR-701-tecnologia-limena-s-a-c/10-contrato/contrato.md, cláusula 7`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`

La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con 5 hallazgos. Lo mostrado está guardado en `estado-legal/20710000019-banco-ribera/corridas/salida-compliance-scan.md`.

Dos cosas que debe saber:
- La sección "El resultado" salió vacía en el reporte del motor. La dejé tal cual, sin rellenarla.
- Los términos ya figuraban como vigentes (aceptados en la versión 0.10.0). Por eso no registré ninguna aceptación nueva a nombre de José Francisco Ñáñez; este comando no tiene cómo hacerlo.