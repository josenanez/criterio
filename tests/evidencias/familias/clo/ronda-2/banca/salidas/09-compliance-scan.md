# /criterio-compliance:compliance-scan 

Desde la corrida anterior no hay archivos nuevos, cambiados ni borrados; el registro normativo se reconvirtió sin cambios. Las cinco señales que siguen salen del cálculo del periodo 2026-09.

# Qué cambió en el cumplimiento · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Diana Cruz | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Andrés Vela | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-101 · OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md, cláusula 7` |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés: no tiene responsable | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el último con informe de cumplimiento
- ¿Dónde están las fichas de Fidel? → estado-legal/900123456-banco-andino/contratos, comprobado en disco
- ¿Dejo el archivo _CRITERIO_LEGAL.txt en la carpeta raíz? → Sí

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md, cláusula 7`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`

La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con 5 hallazgos.