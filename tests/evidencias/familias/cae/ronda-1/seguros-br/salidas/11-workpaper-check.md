# /criterio-audit-work:workpaper-check 

Dos señales abiertas en el programa y los papeles; el motor las calculó con fecha de corte 2026-11-24.

Los términos ya estaban vigentes (versión 1.6, aceptada con la instalación 0.1.0), así que no hizo falta registrar la aceptación de nuevo.

# El programa y los papeles · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `workpaper-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Un hallazgo cita un papel que no existe (norma 14.6) | TR-01 · H-02 cita PT-09, que no está en el índice de papeles | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | El programa no tiene la aprobación antes de su primer papel (norma 13.6) | TR-02: el programa se aprobó el 2026-03-16, después del primer papel (2026-03-09) | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |

## El resultado

| Trabajo | Programa aprobado | Pasos | Papeles | Pasos sin papel | Papeles sin revisión | Hallazgos | Informe |
|---|---|---|---|---|---|---|---|
| TR-01 | 2026-02-06 | 4 | 3 | — | — | 2 | 2026-04-30 |
| TR-02 | 2026-03-16 | 4 | 3 | — | — | 1 | 2026-05-29 |

Todo lo que llegó se procesó, y en esta corrida no hice ninguna pregunta.

La corrida quedó registrada como `2026-11-24-workpaper-check-1`. La salida mostrada está en `corridas/salida-workpaper-check.md`.