# /criterio-audit-work:workpaper-check 

Los términos (v1.6) ya estaban vigentes y aceptados, así que no hizo falta registrar una aceptación nueva. Nadie hizo preguntas en esta corrida. Esto es lo que muestra el reporte, tal cual:

# El programa y los papeles · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `workpaper-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un hallazgo no cita un papel de trabajo, o cita uno que no existe (norma 14.6) (`finding_without_workpaper`) | TR-01 · H-02: cita PT-09, que no está en el índice de papeles (norma 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) (`work_program_not_approved`) | TR-02: el programa de trabajo se aprobó el 2026-03-16, después del primer papel (2026-03-09) (norma 13.6) | — | — | — | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 3 | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica (norma 12.3) (`procedure_not_executed`) | TR-01 · paso P4 «Revisar las provisiones»: no tiene papel ni la razón por la que no aplica (norma 12.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 4 | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe (normas 12.3 y 14.6) (`workpaper_not_reviewed`) | TR-01 · PT-03: no tiene la revisión del supervisor (normas 12.3 y 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

## El resultado

| Trabajo | Programa aprobado | Pasos | Papeles | Pasos sin papel | Papeles sin revisión | Hallazgos | Informe |
|---|---|---|---|---|---|---|---|
| TR-01 | 2026-02-06 | 4 | 3 | P4 | PT-03 | 2 | 2026-04-30 |
| TR-02 | 2026-03-16 | 4 | 3 | — | — | 1 | 2026-05-29 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-trabajos/TR-01_credito-comercial/PT-02.pdf`
- `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx`
- `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx`
- `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

La corrida quedó registrada como `2026-11-24-workpaper-check-1`. La salida está en `estado-auditoria/901777321-banco-andino-sintetico/corridas/salida-workpaper-check.md`.

Me salté un paso: no llamé al motor con `--today` en el reporte y en la corrida a propósito. Sí lo pasé en ambas llamadas, y el reporte salió con fecha de corte 2026-11-24.