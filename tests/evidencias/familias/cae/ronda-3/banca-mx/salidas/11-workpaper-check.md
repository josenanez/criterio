# /criterio-audit-work:workpaper-check 

Los términos (versión 1.6) están vigentes, así que no hizo falta registrar una aceptación nueva. Hay cuatro señales abiertas, dos en TR-01 y dos en TR-02. La fecha de corte es 2026-11-24.

# El programa y los papeles · Banco del Anáhuac Sintético · periodo 2026-11

**Entidad:** Banco del Anáhuac Sintético (BAS0811207K3) · **Fecha de corte:** 2026-11-24 · **Agente:** Justo, versión 1.0.0 · **Comando:** `workpaper-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Un hallazgo cita un papel que no está en el índice (norma 14.6) | TR-01 · H-02 cita PT-09, que no está en el índice de papeles | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | El programa se aprobó después del primer papel (norma 13.6) | TR-02: el programa se aprobó el 2026-03-16 y el primer papel es del 2026-03-09 | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 3 | Un paso no tiene papel ni razón por la que no aplica (norma 12.3) | TR-01 · paso P4 «Revisar las provisiones» | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 4 | Un papel no tiene la revisión del supervisor (normas 12.3 y 14.6) | TR-01 · PT-03 | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

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

La corrida quedó registrada como `2026-11-24-workpaper-check-1`. La salida está en `estado-auditoria/BAS0811207K3-banco-del-anahuac-sintetico/corridas/salida-workpaper-check.md`.

Si las cuatro señales son correctas, la decisión sobre cada una es del auditor.