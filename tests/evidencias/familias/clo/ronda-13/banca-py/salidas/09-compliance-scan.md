# /criterio-compliance:compliance-scan 

Sin archivos nuevos, cambiados ni borrados desde la corrida anterior. El motor levantó 5 señales para el periodo 2026-09.

# Qué cambió en el cumplimiento · Banco del Tebicuary Sintético · periodo 2026-09

**Entidad:** Banco del Tebicuary Sintético (88457812-7) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.3.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Rossana Giménez | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5 (presenta Hugo Duarte, oficial de cumplimiento)) y hay 4 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5 (presenta Hugo Duarte, oficial de cumplimiento)` |
| 3 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Hugo Duarte | 53 | `30-normativa/registro-normativo.csv` fila 4 |
| 4 | Una obligación de cumplimiento de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-4401 · OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento: obligación de cumplimiento del contrato que la matriz no tiene | — | — | — | `contratos/CTR-4401-sistemas-financieros-del-guaira-sintetic/10-contrato/contrato.md, cláusula 7` |
| 5 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | Rossana Giménez | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dejo en la carpeta de documentos el archivo _CRITERIO_LEGAL.txt para reconocerla la próxima vez? → Sí (respuesta sugerida, sesión de prueba sin interfaz)
- ¿Aceptas los términos vigentes (1.3)? → Sí, José Francisco Ñáñez (indicado en el argumento de la prueba)

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `30-normativa/registro-normativo.csv`
- `contratos/CTR-4401-sistemas-financieros-del-guaira-sintetic/10-contrato/contrato.md, cláusula 7`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5 (presenta Hugo Duarte, oficial de cumplimiento)`

La sección «El resultado» salió vacía del motor y la dejé así. La corrida quedó registrada como `2026-10-06-compliance-scan-1`, con 5 hallazgos, y lo mostrado está en `corridas/salida-compliance-scan.md`.