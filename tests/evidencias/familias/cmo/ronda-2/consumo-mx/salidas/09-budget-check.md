# /criterio-campaigns:budget-check 

Términos vigentes. Aquí está el reporte de las campañas contra su presupuesto del periodo 2026-11, tal como lo escribió el motor.

# Cada campaña contra su presupuesto · Consumo Maya Sintético · periodo 2026-11

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.2.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-32 · Día de la familia: la pauta facturada suma 23,000,000 y el presupuesto es 20,000,000; la política tolera un 5 % más | 3,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 8 |
| 3 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25,000,000.00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 4 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-42 · Verano: terminaba el 2026-09-30 y hay pauta facturada hasta el 2026-10-20 (F-42) | 9,000,000.00 | — | 20 | `50-campanas/plan_de_mercadeo.xlsx` fila 9 · `50-campanas/facturas_de_pauta.xlsx` fila 9 |
| 5 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |
| 6 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-22 · Aniversario: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 7 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | — | — |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |
| C-12 · Reactivación | 15,000,000 | 0 | 2026-10-01 | 2026-11-30 | 800 clientes reactivados | Clientes reactivados |
| C-22 · Aniversario | 25,000,000 | 0 | 2026-10-01 | 2026-11-15 | — | — |
| C-32 · Día de la familia | 20,000,000 | 23,000,000 | 2026-09-01 | 2026-10-31 | 900 ventas | Ventas atribuidas |
| C-42 · Verano | 18,000,000 | 9,000,000 | 2026-08-01 | 2026-09-30 | 1000 visitas a la tienda | Visitas a la tienda |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-budget-check-1`.