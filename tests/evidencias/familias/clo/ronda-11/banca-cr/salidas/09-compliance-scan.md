# /criterio-compliance:compliance-scan 

Los términos quedaron aceptados a nombre de José Francisco Ñáñez para esta prueba. No hay archivos nuevos ni cambiados desde la corrida anterior; el escaneo calculó 5 señales para el periodo 2026-09.

# Qué cambió en el cumplimiento · Banco del Valle Central Sintético · periodo 2026-09

**Entidad:** Banco del Valle Central Sintético (3101457812) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.1.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Gabriela Quesada | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Esteban Vargas | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-3601 · OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-3601-sistemas-financieros-del-valle-s-a/10-contrato/contrato.md, cláusula 7` |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés: no tiene responsable | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dejo en la carpeta de documentos el archivo _CRITERIO_LEGAL.txt para reconocerla a primera vista? → Sí (respuesta sugerida tomada en la sesión de prueba, sin interfaz)

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `contratos/CTR-3601-sistemas-financieros-del-valle-s-a/10-contrato/contrato.md, cláusula 7`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`