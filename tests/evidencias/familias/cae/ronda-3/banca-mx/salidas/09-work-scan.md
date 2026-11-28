# /criterio-audit-work:work-scan 

Los términos están vigentes. El inventario no trae documentos nuevos, cambiados ni borrados, y la ficha del periodo ya coincidía con los papeles y los informes, así que no hubo que agregar nada. El motor no reporta problemas en la ficha.

La decisión sobre cada señal es del auditor.

# Qué cambió en los trabajos · Banco del Anáhuac Sintético · periodo 2026-11

**Entidad:** Banco del Anáhuac Sintético (BAS0811207K3) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 1.0.0 · **Comando:** `work-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles (`report_differs_from_workpapers`) | TR-01 · H-02: el informe trae 540,000,000 y los papeles 450,000,000 | — | — | — | `20-trabajos/TR-01_credito-comercial/informe.pdf` · `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | Un auditor asignado a un trabajo de aseguramiento tuvo a su cargo la actividad auditada en los doce meses anteriores (norma 2.2) (`auditor_reviews_own_work`) | TR-02: Luis Peña está asignado a un trabajo de aseguramiento sobre Tecnología, que tuvo a su cargo hasta el 2026-06-30, dentro de los doce meses anteriores al 2026-03-02 (norma 2.2) | — | — | — | `20-trabajos/asignaciones.xlsx` fila 3 · `00-referencia/cargos_anteriores.xlsx` fila 2 |
| 3 | Un hallazgo no tiene su criterio, su condición, su efecto o su prioridad, o no tiene su causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) (`finding_element_missing`) | TR-01 · H-01: le falta la causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |
| 4 | Un hallazgo no cita un papel de trabajo, o cita uno que no existe (norma 14.6) (`finding_without_workpaper`) | TR-01 · H-02: cita PT-09, que no está en el índice de papeles (norma 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 5 | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) (`work_program_not_approved`) | TR-02: el programa de trabajo se aprobó el 2026-03-16, después del primer papel (2026-03-09) (norma 13.6) | — | — | — | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 6 | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica (norma 12.3) (`procedure_not_executed`) | TR-01 · paso P4 «Revisar las provisiones»: no tiene papel ni la razón por la que no aplica (norma 12.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 7 | La prioridad de un hallazgo no es la que da la metodología para su impacto y su probabilidad (norma 14.3) (`rating_inconsistent`) | TR-01 · H-01: prioridad «Media»; con impacto 4 y probabilidad 4 la metodología da «alta» (norma 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |
| 8 | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe (normas 12.3 y 14.6) (`workpaper_not_reviewed`) | TR-01 · PT-03: no tiene la revisión del supervisor (normas 12.3 y 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

## El resultado

**Trabajos en `20-trabajos/`:** 2 · **Hallazgos en la ficha:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/cargos_anteriores.xlsx`
- `20-trabajos/TR-01_credito-comercial/PT-02.pdf`
- `20-trabajos/TR-01_credito-comercial/PT-03.pdf`
- `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx`
- `20-trabajos/TR-01_credito-comercial/informe.pdf`
- `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx`
- `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf`
- `20-trabajos/asignaciones.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)