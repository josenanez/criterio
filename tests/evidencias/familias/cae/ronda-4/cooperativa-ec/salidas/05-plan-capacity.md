# /criterio-audit-plan:plan-capacity 

Los términos están vigentes (versión 1.6), así que el reporte salió. En esta corrida de prueba no se registró ninguna aceptación nueva. Corrí `terminos` y no pidió aceptar, así que no volví a registrar a José Francisco Ñáñez. Dos señales quedan abiertas.

---

# Las horas del plan · Cooperativa de Ahorro Chimborazo Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Chimborazo Sintética (1791234567001) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 1.1.0 · **Comando:** `plan-capacity`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Un trabajo de aseguramiento sobre ciberseguridad o terceros no lleva en su programa el requisito temático vigente (`topical_requirement_missing`) | TR-02 · Ciberseguridad de canales: empieza el 2026-03-02, y el requisito temático de Ciberseguridad rige desde el 2026-02-05; su programa no lo lleva | `10-plan/plan_anual_2026.xlsx` fila 3 |
| 2 | Las horas del plan superan las horas disponibles del equipo en el periodo (`plan_hours_exceed_capacity`) | el plan suma 2200 horas y el equipo tiene 2000 disponibles: faltan 200 | `10-plan/plan_anual_2026.xlsx` · `00-referencia/equipo.xlsx` |

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

---

La corrida quedó registrada como `2026-11-24-plan-capacity-1`. La salida completa está en `corridas/salida-plan-capacity.md`, con una línea de presentación antes del reporte. Esa línea no estaba en lo que te mostré arriba.