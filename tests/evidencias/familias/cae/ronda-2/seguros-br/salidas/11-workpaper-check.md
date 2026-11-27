# /criterio-audit-work:workpaper-check 

Los términos vigentes (versión 1.6) ya estaban aceptados; el reporte señala cuatro puntos entre TR-01 y TR-02.

# El programa y los papeles · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `workpaper-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Un hallazgo no cita un papel que exista (norma 14.6) | TR-01 · H-02: cita PT-09, que no está en el índice de papeles | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | El programa no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) | TR-02: el programa se aprobó el 2026-03-16, después del primer papel (2026-03-09) | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 3 | Un paso del programa no tiene papel ni la razón por la que no aplica (norma 12.3) | TR-01 · paso P4 «Revisar las provisiones» | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 4 | Un papel no tiene la revisión del supervisor ni la aprobación del responsable de auditoría antes del informe (normas 12.3 y 14.6) | TR-01 · PT-03: sin revisión del supervisor | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

## El resultado

| Trabajo | Programa aprobado | Pasos | Papeles | Pasos sin papel | Papeles sin revisión | Hallazgos | Informe |
|---|---|---|---|---|---|---|---|
| TR-01 | 2026-02-06 | 4 | 3 | P4 | PT-03 | 2 | 2026-04-30 |
| TR-02 | 2026-03-16 | 4 | 3 | — | — | 1 | 2026-05-29 |

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** los cuatro documentos citados arriba, más F-01 (families/criterio-cae/FUENTES.es.md).

La corrida quedó registrada como `2026-11-24-workpaper-check-1`. La decisión sobre cada punto es del auditor.