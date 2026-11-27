# /criterio-audit-plan:plan-coverage 

Prudencia cruzó la matriz, el universo y el plan de Banco Andino Sintético. Abajo está lo que el plan deja sin cubrir; qué se audita lo decide el responsable de auditoría con el consejo.

Los términos ya estaban vigentes (versión 1.6) y no pedían nueva aceptación. Por eso no registré aceptación a nombre de José Francisco Ñáñez.

# El plan contra los riesgos · Banco Andino Sintético · periodo 2026-11

**Fecha de corte:** 2026-11-24 · **Agente:** Prudencia, versión 0.2.2 · **Comando:** `plan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Riesgo alto o crítico sin trabajo en el plan | R-06 · Pérdida de información de clientes: calificado Crítico y ningún trabajo del plan lo cubre (norma 9.4) | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Unidad que pasó su ciclo de rotación sin trabajo | U-03 · Tesorería: último trabajo el 2023-03-10; su ciclo de 24 meses venció el 2025-03-10 y no está en el plan (624 días) | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Unidad que pasó su ciclo de rotación sin trabajo | U-10 · Canales físicos: sin trabajo registrado y fuera del plan; su ciclo es de 36 meses | `10-plan/universo_auditable.xlsx` fila 8 |
| 4 | Evaluación de riesgos con más de un año (norma 9.4) | La evaluación que sostiene el plan es del 2025-09-15: tiene 435 días y la norma pide una al menos cada año (70 días de atraso) | `00-referencia/metodologia-de-auditoria.pdf` |
| 5 | El plan no considera un área de la norma 9.4 ni dice por qué | No considera el riesgo de fraude ni explica la omisión | `10-plan/plan_anual_2026.xlsx` |

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
| los programas de cumplimiento y ética | sí | — |

**Última evaluación de riesgos:** 2025-09-15.

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

---

La corrida quedó registrada como `2026-11-24-plan-coverage-1`. Lo mostrado está en `corridas/salida-plan-coverage.md`, y el reporte completo en `plan/2026-11/reporte-plan-coverage.md`, ambos dentro de la carpeta de estado.