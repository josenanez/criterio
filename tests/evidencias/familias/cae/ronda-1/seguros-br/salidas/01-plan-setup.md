# /criterio-audit-plan:plan-setup auditoria/31452078000190-seguradora-atlantica-sintetica

Prudencia quedó configurada para Seguradora Atlântica Sintética (CNPJ 31452078000190), y la primera revisión del plan encontró 3 puntos por atender.

Encontré dos archivos fuera de lugar; no los moví:
- `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/`.
- `30-seguimiento/riesgos_aceptados.xlsx` iría en `10-plan/`.

**Lo que tomé de los documentos.** No hubo nadie para responder, así que en cada pregunta tomé la respuesta sugerida por los documentos:
- **Ciclos de rotación:** Crítico y Alto cada 12 meses, Medio cada 24 y Bajo cada 36. Un riesgo es alto si está calificado Alto o Crítico.
- **Quién aprueba el plan y sus cambios:** el comité de auditoría, según el estatuto. En Brasil, la regulación (F-12) también exige al consejo de administración. Dejé lo que dice el estatuto; el responsable de auditoría tiene que revisar esa diferencia.
- **Evaluaciones:** la última evaluación de riesgos es del 2025-09-15 y la última evaluación externa de calidad, del 2021-03-31. Las dos fechas salen de la metodología.
- **Rostrum:** lo que encuentro no se publica ahí.
- **Estado:** lo guardo en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica`.
- **Términos:** José Francisco Ñáñez aceptó la versión 1.6 el 2026-11-24. Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-audit-plan-0.1.0-2026-11-24.md` y `.pdf`.
- **Archivos creados:** la configuración está en `.criterio/plan/31452078000190/config.json`. También dejé la marca `_CRITERIO_AUDITORIA.txt` en la carpeta de la entidad.

**Primera ficha.** Pasé a la ficha las dos actas del comité de auditoría:
- **TR-05 (Tesorería):** se cancela, según el acta del 2026-07-15.
- **TR-06 (Nómina):** se agrega, según el acta del 2026-10-20.

El motor encontró además dos señales que este reporte no muestra. Una es sobre la evaluación externa de calidad y se ve con `/criterio-audit-plan:quality-status`. La otra compara las horas del plan con la capacidad del equipo y se ve con `/criterio-audit-plan:plan-capacity`.

# El plan contra los riesgos · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 2 | La evaluación de riesgos que sostiene el plan tiene más de un año (norma 9.4) (`risk_assessment_outdated`) | la evaluación de riesgos que sostiene el plan es del 2025-09-15: tiene 435 días, y la norma 9.4 la pide al menos una vez al año | — | — | 70 | `00-referencia/metodologia-de-auditoria.pdf` |
| 3 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera los programas de cumplimiento y ética ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |

## El resultado

| Riesgo | Calificación | Unidad | Alto | Trabajos que lo cubren |
|---|---|---|---|---|
| R-01 · Pérdida por riesgo de crédito | Alto | U-01 | sí | TR-01 |
| R-02 · Ataque a los canales digitales | Crítico | U-02 | sí | TR-02 |
| R-03 · Fraude en pagos a proveedores | Alto | U-06 | sí | TR-04 |
| R-04 · Lavado de activos | Crítico | U-05 | sí | TR-03 |
| R-05 · Error en la liquidación de nómina | Medio | U-04 | no | TR-06 |

| Unidad | Nivel | Último trabajo | Ciclo | Vence | En el plan |
|---|---|---|---|---|---|
| U-01 · Crédito | Alto | 2025-10-15 | 12 meses | 2026-10-15 | TR-01 |
| U-02 · Tecnología | Alto | 2025-10-01 | 12 meses | 2026-10-01 | TR-02 |
| U-03 · Tesorería | Medio | 2023-03-10 | 24 meses | 2025-03-10 | — |
| U-04 · Nómina | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | TR-06 |
| U-05 · Cumplimiento | Alto | 2025-12-01 | 12 meses | 2026-12-01 | TR-03 |
| U-06 · Proveedores | Medio | 2025-01-15 | 24 meses | 2027-01-15 | TR-04 |
| U-10 · Canales físicos | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | — |

| Lo que el plan tiene que considerar (norma 9.4) | Considerado | Por qué no |
|---|---|---|
| el gobierno de TI | sí | — |
| el riesgo de fraude | sí | — |
| los programas de cumplimiento y ética | no | — |

**Última evaluación de riesgos:** 2025-09-15.

Qué se audita lo decide el responsable de auditoría con el consejo: aquí se dice qué queda sin cubrir.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/metodologia-de-auditoria.pdf`
- `10-plan/plan_anual_2026.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

**Revisión diaria automática:** no creé la tarea porque requiere un sí explícito y en esta prueba nadie lo dio. Para revisar a mano: `/criterio-audit-plan:plan-wake`.

**Cuándo vuelvo:** sin revisión automática.

La corrida quedó registrada como `2026-11-24-plan-setup-1`. Lo que se mostró está completo en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-plan-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.