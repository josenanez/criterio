# /criterio-audit-plan:plan-capacity 

Los términos están vigentes (versión 1.6). El reporte señala dos cosas: un trabajo de ciberseguridad sin el requisito temático en su programa y horas del plan por encima de las disponibles.

# Las horas del plan · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.2.2 · **Comando:** `plan-capacity`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un trabajo de aseguramiento sobre ciberseguridad o terceros no lleva en su programa el requisito temático vigente (`topical_requirement_missing`) | TR-02 · Ciberseguridad de canales: trabajo de aseguramiento sobre ciberseguridad que empieza el 2026-03-02, y el requisito temático de Ciberseguridad rige desde el 2026-02-05; su programa no lo lleva | — | — | — | `10-plan/plan_anual_2026.xlsx` fila 3 |
| 2 | Las horas del plan superan las horas disponibles del equipo en el periodo (`plan_hours_exceed_capacity`) | el plan suma 2200 horas y el equipo tiene 2000 disponibles en el periodo: faltan 200 | — | — | — | `10-plan/plan_anual_2026.xlsx` · `00-referencia/equipo.xlsx` |

## El resultado

**Horas del plan:** 2200 · **Horas disponibles del equipo:** 2000.

| Trabajo | Temas | Horas |
|---|---|---|
| TR-01 · Crédito comercial | credito | 500.0 |
| TR-02 · Ciberseguridad de canales | ciberseguridad, ti | 400.0 |
| TR-03 · Prevención de lavado | lavado_de_activos | 300.0 |
| TR-04 · Pagos a proveedores | proveedores, terceros | 300.0 |
| TR-06 · Nómina | nomina | 200.0 |
| TR-07 · Gobierno corporativo | gobierno | 500.0 |

Requisitos temáticos de The IIA y desde cuándo rigen: Ciberseguridad, 2026-02-05; Terceros, 2026-09-15; Comportamiento Organizacional, 2026-12-15; Resiliencia Organizacional, 2027-04-30; Anticorrupción, 2027-11-23.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/equipo.xlsx`
- `10-plan/plan_anual_2026.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cae/FUENTES.es.md)

La corrida quedó registrada como `2026-11-24-plan-capacity-1`. El reporte está en `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica/plan/2026-11/reporte-plan-capacity.md`.