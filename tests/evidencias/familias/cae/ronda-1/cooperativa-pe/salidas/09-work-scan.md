# /criterio-audit-work:work-scan 

Desde la corrida anterior no llegó ningún documento nuevo ni cambió ninguno en `20-trabajos/`. La ficha del periodo ya tenía todos los hallazgos y coincide con los papeles, así que no la toqué.
El inventario encontró dos archivos que parecen estar en otra carpeta: `30-seguimiento/informe_revisor_fiscal_2026.pdf`, que iría en `20-trabajos/`, y `30-seguimiento/riesgos_aceptados.xlsx`, que iría en `10-plan/`. Los dejé donde están.

# Qué cambió en los trabajos · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `work-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles (`report_differs_from_workpapers`) | TR-01 · H-02: el informe trae 540,000,000 y los papeles 450,000,000 | — | — | — | `20-trabajos/TR-01_credito-comercial/informe.pdf` · `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 2 | Un hallazgo no tiene su criterio, su condición, su efecto o su prioridad, o no tiene su causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) (`finding_element_missing`) | TR-01 · H-01: le falta la causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |
| 3 | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica (norma 12.3) (`procedure_not_executed`) | TR-01 · paso P4 «Revisar las provisiones»: no tiene papel ni la razón por la que no aplica (norma 12.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx` fila 5 |
| 4 | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe (normas 12.3 y 14.6) (`workpaper_not_reviewed`) | TR-01 · PT-03: no tiene la revisión del supervisor (normas 12.3 y 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx` fila 4 |

## El resultado

**Trabajos en `20-trabajos/`:** 2 · **Hallazgos en la ficha:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-trabajos/TR-01_credito-comercial/PT-02.pdf`
- `20-trabajos/TR-01_credito-comercial/PT-03.pdf`
- `20-trabajos/TR-01_credito-comercial/indice_de_papeles.xlsx`
- `20-trabajos/TR-01_credito-comercial/informe.pdf`
- `20-trabajos/TR-01_credito-comercial/programa_de_trabajo.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)