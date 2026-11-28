# /criterio-audit-plan:plan-setup auditoria/BAS0811207K3-banco-del-anahuac-sintetico

Prudencia quedó lista para el Banco del Anáhuac Sintético (RFC BAS0811207K3). La configuración está en `.criterio/plan/BAS0811207K3/config.json`, los términos quedaron aceptados a nombre de José Francisco Ñáñez con fecha 2026-11-24 y la carpeta quedó marcada con `_CRITERIO_AUDITORIA.txt`. El comprobante de los términos está en `.criterio/terminos/aceptacion-criterio-audit-plan-1.0.0-2026-11-24.md` y en `.pdf`.

La primera ficha (2026-11) tiene una sola aprobación: el acta 07-2026 dice que el comité de auditoría aprobó cancelar TR-05 (Tesorería) el 2026-07-15. Ninguna acta trae la aprobación para agregar TR-06; el reporte `plan-status` muestra ese cambio que no tiene acta.

# El plan contra los riesgos · Banco del Anáhuac Sintético · periodo 2026-11

**Entidad:** Banco del Anáhuac Sintético (BAS0811207K3) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 1.0.0 · **Comando:** `plan-coverage`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo de la metodología (`high_risk_not_covered`) | R-06 · Pérdida de información de clientes: calificado Crítico en la matriz y ningún trabajo del plan lo cubre (norma 9.4) | — | — | — | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-10 · Canales físicos: no tiene un trabajo registrado y no está en el plan; su ciclo es de 36 meses | — | — | — | `10-plan/universo_auditable.xlsx` fila 8 |
| 4 | La evaluación de riesgos que sostiene el plan tiene más de un año (norma 9.4) (`risk_assessment_outdated`) | la evaluación de riesgos que sostiene el plan es del 2025-09-15: tiene 435 días, y la norma 9.4 la pide al menos una vez al año | — | — | 70 | `00-referencia/metodologia-de-auditoria.pdf` |
| 5 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera los programas de cumplimiento y ética ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |
| 6 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera el riesgo de fraude ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |

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

---

**Reloj:** no creé la tarea programada porque en esta sesión de prueba nadie dio el sí explícito que pide. Para correrlo a mano: `/criterio-audit-plan:plan-wake`.
**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-24-plan-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.