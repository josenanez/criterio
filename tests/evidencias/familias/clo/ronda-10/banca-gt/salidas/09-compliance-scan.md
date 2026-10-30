# /criterio-compliance:compliance-scan 

El inventario no trajo archivos nuevos, cambiados ni borrados frente a la corrida anterior. Las señales salen de recalcular el periodo 2026-09. La sección «El resultado» llegó vacía del motor y la dejo tal cual.

# Qué cambió en el cumplimiento · Banco del Altiplano Sintético · periodo 2026-09

**Entidad:** Banco del Altiplano Sintético (48712035) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.1.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | María Fernanda Barrios | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | José Pablo Cifuentes | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-3301 · OBL-3 · Reporte de operaciones al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-3301-sistemas-financieros-de-guatemala-s-a/10-contrato/contrato.md, cláusula 7` |
| 5 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | María Fernanda Barrios | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Qué periodo se evalúa? → 2026-09, el del informe de cumplimiento más reciente (respuesta sugerida por los documentos; sesión sin interfaz)
- ¿Dónde están las fichas de Fidel? → estado-legal/48712035-banco-del-altiplano-sintetico/contratos (carpeta comprobada en disco)

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `contratos/CTR-3301-sistemas-financieros-de-guatemala-s-a/10-contrato/contrato.md, cláusula 7`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`

La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con 5 hallazgos. Dos cosas que debe saber:

- **Aceptación de términos:** los términos ya figuraban como vigentes (aceptada la versión 1.1.0). No registré una aceptación nueva a nombre de José Francisco Ñáñez, porque el agente no volvió a mostrarlos.
- **Texto guardado:** el archivo `salida-compliance-scan.md` lleva esas dos líneas iniciales más el reporte, es decir, lo mismo que se ve arriba.