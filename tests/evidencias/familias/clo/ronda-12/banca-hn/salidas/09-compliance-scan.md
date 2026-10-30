# /criterio-compliance:compliance-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior; el cálculo del periodo 2026-09 dejó 5 señales abiertas.

# Qué cambió en el cumplimiento · Banco de Occidente Sintético · periodo 2026-09

**Entidad:** Banco de Occidente Sintético (08010004578120) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.2.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Ana Lucía Pineda | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Óscar Zelaya | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-4001 · OBL-3 · Reporte de operaciones al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `legal/08010004578120-banco-de-occidente-sintetico/contratos/CTR-4001-sistemas-financieros-de-occidente-s-de-r/10-contrato/contrato.md, cláusula 7` |
| 5 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés: no tiene responsable | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dejo en la carpeta de documentos el archivo _CRITERIO_LEGAL.txt? → No. Sesión de prueba sin interfaz; nadie autorizó escribir en los documentos.

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`
- `legal/08010004578120-banco-de-occidente-sintetico/contratos/CTR-4001-sistemas-financieros-de-occidente-s-de-r/10-contrato/contrato.md, cláusula 7`

La corrida quedó registrada con el id `2026-10-06-compliance-scan-1` y 5 hallazgos. Dos cosas del procedimiento:

- **Términos:** el motor los dio por vigentes (versión 1.3), así que no hizo falta registrar la aceptación de José Francisco Ñáñez.
- **Sección "El resultado":** el motor la dejó vacía y la copié tal cual, sin rellenarla.