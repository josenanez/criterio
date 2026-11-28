# /criterio-audit-plan:plan-coverage 

Corrí `plan-coverage` para el periodo 2026-11, con fecha de corte 2026-11-24. Los términos ya estaban vigentes (aceptada la versión 1.1.0), así que no registré ninguna aceptación nueva. Dejé el reporte completo y la corrida registrada. El reporte señala seis cosas, entre riesgos sin trabajo, unidades fuera de ciclo y áreas que el plan no considera.

# El plan contra los riesgos · Cooperativa de Ahorro Chimborazo Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Chimborazo Sintética (1791234567001) · **Fecha de corte:** 2026-11-24 · **Agente:** Prudencia, versión 1.1.0 · **Comando:** `plan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Riesgo alto o crítico sin trabajo en el plan (`high_risk_not_covered`) | R-06 · Pérdida de información de clientes: calificado Crítico y ningún trabajo del plan lo cubre (norma 9.4) | — | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Unidad pasada de su ciclo (`auditable_unit_overdue`) | U-03 · Tesorería: último trabajo 2023-03-10, ciclo de 24 meses vencido el 2025-03-10, no está en el plan | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Unidad pasada de su ciclo (`auditable_unit_overdue`) | U-10 · Canales físicos: sin trabajo registrado y fuera del plan; ciclo de 36 meses | — | `10-plan/universo_auditable.xlsx` fila 8 |
| 4 | Evaluación de riesgos con más de un año (`risk_assessment_outdated`) | La evaluación que sostiene el plan es del 2025-09-15: tiene 435 días y la norma 9.4 la pide al menos una vez al año | 70 | `00-referencia/metodologia-de-auditoria.pdf` |
| 5 | Área no considerada (`plan_area_not_considered`) | El plan no considera los programas de cumplimiento y ética ni dice por qué (norma 9.4) | — | `10-plan/plan_anual_2026.xlsx` |
| 6 | Área no considerada (`plan_area_not_considered`) | El plan no considera el riesgo de fraude ni dice por qué (norma 9.4) | — | `10-plan/plan_anual_2026.xlsx` |

## El resultado

| Riesgo | Calificación | Unidad | Alto | Trabajos que lo cubren |
|---|---|---|---|---|
| R-01 · Pérdida por riesgo de crédito | Alto | U-01 | sí | TR-01 |
| R-02 · Ataque a los canales digitales | Crítico | U-02 | sí | TR-02 |
| R-03 · Fraude en pagos a proveedores | Alto | U-06 | sí | TR-04 |
| R-04 · Lavado de activos | Crítico | U-05 | sí | TR-03 |
| R-05 · Error en la liquidación de nómina | Medio | U-04 | no | TR-06 |
| R-06 · Pérdida de información de clientes | Crítico | U-09 | sí | — |

| Unidad | Nivel | Último trabajo | Ciclo | Vence | En el plan |
|---|---|---|---|---|---|
| U-01 · Crédito | Alto | 2025-10-15 | 12 meses | 2026-10-15 | TR-01 |
| U-02 · Tecnología | Alto | 2025-10-01 | 12 meses | 2026-10-01 | TR-02 |
| U-03 · Tesorería | Medio | 2023-03-10 | 24 meses | 2025-03-10 | — |
| U-04 · Nómina | Bajo | 2024-05-01 | 36 meses | 2027-05-01 | TR-06 |
| U-05 · Cumplimiento | Alto | 2025-12-01 | 12 meses | 2026-12-01 | TR-03 |
| U-06 · Proveedores | Medio | 2025-01-15 | 24 meses | 2027-01-15 | TR-04 |
| U-10 · Canales físicos | Bajo | — | 36 meses | — | — |

| Lo que el plan tiene que considerar (norma 9.4) | Considerado | Por qué no |
|---|---|---|
| el gobierno de TI | sí | — |
| el riesgo de fraude | no | — |
| los programas de cumplimiento y ética | no | — |

**Última evaluación de riesgos:** 2025-09-15.

Qué se audita lo decide el responsable de auditoría con el consejo: aquí se dice qué queda sin cubrir.

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `00-referencia/metodologia-de-auditoria.pdf`
- `10-plan/matriz_de_riesgos.xlsx`
- `10-plan/plan_anual_2026.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

**Registro de la corrida:** `2026-11-24-plan-coverage-1` (11 hallazgos). La salida está en `corridas/salida-plan-coverage.md` y el reporte en `plan/2026-11/reporte-plan-coverage.md`, ambos dentro de la carpeta de estado.