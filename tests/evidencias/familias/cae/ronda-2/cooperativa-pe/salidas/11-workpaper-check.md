# /criterio-audit-work:workpaper-check 

Los términos (versión 1.6) ya estaban vigentes y aceptados en la 0.2.2. No tuve que registrar una aceptación nueva a nombre de José Francisco Ñáñez. Pasé `--today 2026-11-24` en cada llamada. Nadie respondió preguntas y el motor no hizo ninguna.

# El programa y los papeles · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Agente:** Justo, versión 0.2.2 · **Comando:** `workpaper-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Un hallazgo cita un papel que no existe (norma 14.6) | TR-01 · H-02: cita PT-09, que no está en el índice de papeles | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | El programa no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) | TR-02: el programa se aprobó el 2026-03-16, después del primer papel (2026-03-09) | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 3 | Un paso del programa no tiene papel ni razón por la que no aplica (norma 12.3) | TR-01 · paso P4 «Revisar las provisiones» | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 4 | Un papel no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes del informe (normas 12.3 y 14.6) | TR-01 · PT-03: sin revisión del supervisor | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

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

La corrida quedó registrada como `2026-11-24-workpaper-check-1`. El texto de arriba es el reporte que escribió el motor, copiado entero a `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica/corridas/salida-workpaper-check.md`. Las decisiones sobre estos cuatro puntos son del auditor.