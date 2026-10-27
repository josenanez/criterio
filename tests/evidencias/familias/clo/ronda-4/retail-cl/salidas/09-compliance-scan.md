# /criterio-compliance:compliance-scan 

Los términos de la versión 1.2 están vigentes. El inventario no trae archivos nuevos, cambiados ni borrados desde la corrida anterior. El motor calculó el periodo 2026-09 y dejó cuatro señales abiertas.

# Qué cambió en el cumplimiento · Tiendas Pacífico · periodo 2026-09

**Entidad:** Tiendas Pacífico (76083001-1) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.10.0 · **Comando:** `compliance-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación de la matriz pasó su fecha límite sin evidencia (`compliance_obligation_overdue`) | OB-09 · Reporte mensual de quejas: venció el 2026-10-05 y no hay evidencia en la ventana de su periodicidad | — | Javiera Soto | 1 | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica (`declared_compliance_vs_evidence`) | el informe declara el periodo cumplido (cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5) y hay 3 señales abiertas que ese estado no explica | — | — | — | `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5` |
| 3 | Una política pasó su fecha de revisión (`policy_review_overdue`) | P-03 · Política de conflictos de interés: su revisión vencía el 2026-08-31 | — | Javiera Soto | 36 | `20-politicas/indice-politicas.csv` fila 4 |
| 4 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-obligaciones.csv`
- `20-politicas/indice-politicas.csv`
- `cumplimiento-2026-09/20-reportes/informe-cumplimiento-2026-09.md, línea 5`

La sección «El resultado» salió vacía del motor y la dejé así. La corrida quedó registrada como `2026-10-06-compliance-scan-1` con 4 hallazgos.