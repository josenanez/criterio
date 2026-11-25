# /criterio-audit-work:workpaper-check 

Los términos de la versión 1.6 ya estaban vigentes (aceptados en la 0.1.0), así que no hubo que registrar ninguna aceptación. El motor encontró tres señales en el programa y los papeles de Banco Andino Sintético. Los dos trabajos tienen hallazgos en 0, así que ninguno depende de un papel que falte.

# El programa y los papeles · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `workpaper-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) (`work_program_not_approved`) | TR-02: el programa de trabajo se aprobó el 2026-03-16, después del primer papel (2026-03-09) (norma 13.6) | — | — | — | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 2 | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica (norma 12.3) (`procedure_not_executed`) | TR-01 · paso P4 «Revisar las provisiones»: no tiene papel ni la razón por la que no aplica (norma 12.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 3 | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe (normas 12.3 y 14.6) (`workpaper_not_reviewed`) | TR-01 · PT-03: no tiene la revisión del supervisor (normas 12.3 y 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

## El resultado

| Trabajo | Programa aprobado | Pasos | Papeles | Pasos sin papel | Papeles sin revisión | Hallazgos | Informe |
|---|---|---|---|---|---|---|---|
| TR-01 | 2026-02-06 | 4 | 3 | P4 | PT-03 | 0 | 2026-04-30 |
| TR-02 | 2026-03-16 | 4 | 3 | — | — | 0 | 2026-05-29 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx`
- `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx`
- `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

El reporte quedó en `trabajos/2026-11/reporte-workpaper-check.md`, dentro de la carpeta de estado. La salida mostrada quedó en `corridas/salida-workpaper-check.md`. La corrida quedó registrada con el id `2026-11-24-workpaper-check-1`. La decisión sobre estas señales es del auditor.