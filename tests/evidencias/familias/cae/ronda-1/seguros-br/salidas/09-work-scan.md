# /criterio-audit-work:work-scan 

El inventario no encontró documentos nuevos, cambiados ni borrados. La ficha del periodo ya tenía cada hallazgo tal como lo escriben los papeles y los informes, así que no la cambié. El inventario también marca dos archivos de `30-seguimiento/` que están en otra carpeta de la que les toca: `informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/` y `riesgos_aceptados.xlsx` iría en `10-plan/`. Moverlos o no lo decide el auditor.

# Qué cambió en los trabajos · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Justo, versión 0.1.0 · **Comando:** `work-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un auditor asignado a un trabajo de aseguramiento tuvo a su cargo la actividad auditada en los doce meses anteriores (norma 2.2) (`auditor_reviews_own_work`) | TR-02: Luis Peña está asignado a un trabajo de aseguramiento sobre Tecnología, que tuvo a su cargo hasta el 2026-06-30, dentro de los doce meses anteriores al 2026-01-20 (norma 2.2) | — | — | — | `20-trabajos/asignaciones.xlsx` fila 3 · `00-referencia/cargos_anteriores.xlsx` fila 2 |
| 2 | Un hallazgo no cita un papel de trabajo, o cita uno que no existe (norma 14.6) (`finding_without_workpaper`) | TR-01 · H-02: cita PT-09, que no está en el índice de papeles (norma 14.6) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-02.pdf` |
| 3 | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) (`work_program_not_approved`) | TR-02: el programa de trabajo se aprobó el 2026-03-16, después del primer papel (2026-03-09) (norma 13.6) | — | — | — | `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf` |
| 4 | La prioridad de un hallazgo no es la que da la metodología para su impacto y su probabilidad (norma 14.3) (`rating_inconsistent`) | TR-01 · H-01: prioridad «Media»; con impacto 4 y probabilidad 4 la metodología da «alta» (norma 14.3) | — | — | — | `20-trabajos/TR-01_credito-comercial/PT-03.pdf` |

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
- `20-trabajos/TR-02_ciberseguridad/aprobacion-del-programa.pdf`
- `20-trabajos/asignaciones.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-24-work-scan-1`. Lo mostrado está guardado en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-work-scan.md`.