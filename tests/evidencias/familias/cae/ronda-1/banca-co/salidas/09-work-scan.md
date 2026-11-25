# /criterio-audit-work:work-scan 

No hay documentos nuevos ni cambiados en el inventario, y la ficha del periodo ya tenía todo lo que traen los documentos. Los papeles de trabajo no describen ningún hallazgo, así que los hallazgos del informe aparecen sin un papel que los respalde.
El inventario también marca dos archivos de `30-seguimiento/` que no están en su carpeta: `informe_revisor_fiscal_2026.pdf` corresponde a `20-trabajos/` y `riesgos_aceptados.xlsx` a `10-plan/`.

# Qué cambió en los trabajos · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `work-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles (`report_differs_from_workpapers`) | TR-01 · H-01: está en el informe y no en los papeles | — | — | — | `20-trabajos/TR-01_credito-comercial/informe.pdf` |
| 2 | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles (`report_differs_from_workpapers`) | TR-01 · H-02: está en el informe y no en los papeles | — | — | — | `20-trabajos/TR-01_credito-comercial/informe.pdf` |
| 3 | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles (`report_differs_from_workpapers`) | TR-02 · H-03: está en el informe y no en los papeles | — | — | — | `20-trabajos/TR-02_ciberseguridad/informe.pdf` |
| 4 | Un auditor asignado a un trabajo de aseguramiento tuvo a su cargo la actividad auditada en los doce meses anteriores (norma 2.2) (`auditor_reviews_own_work`) | TR-02: Luis Peña está asignado a un trabajo de aseguramiento sobre Tecnología, que tuvo a su cargo hasta el 2026-06-30, dentro de los doce meses anteriores al 2026-03-02 (norma 2.2) | — | — | — | `20-trabajos/asignaciones.xlsx` fila 3 · `00-referencia/cargos_anteriores.xlsx` fila 2 |
| 5 | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) (`work_program_not_approved`) | TR-02: el programa de trabajo se aprobó el 2026-03-16, después del primer papel (2026-03-09) (norma 13.6) | — | — | — | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 6 | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica (norma 12.3) (`procedure_not_executed`) | TR-01 · paso P4 «Revisar las provisiones»: no tiene papel ni la razón por la que no aplica (norma 12.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 7 | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe (normas 12.3 y 14.6) (`workpaper_not_reviewed`) | TR-01 · PT-03: no tiene la revisión del supervisor (normas 12.3 y 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

## El resultado

**Trabajos en `20-trabajos/`:** 2 · **Hallazgos en la ficha:** 0.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/cargos_anteriores.xlsx`
- `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx`
- `20-trabajos/TR-01_credito-comercial/informe.pdf`
- `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx`
- `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf`
- `20-trabajos/TR-02_ciberseguridad/informe.pdf`
- `20-trabajos/asignaciones.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-24-work-scan-1`. Lo que se mostró está guardado entero en `estado-auditoria/901777321-banco-andino-sintetico/corridas/salida-work-scan.md`.