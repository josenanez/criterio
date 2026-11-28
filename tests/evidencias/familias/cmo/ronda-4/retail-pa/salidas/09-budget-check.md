# /criterio-campaigns:budget-check 

Los términos (versión 1.6) ya estaban vigentes y aceptados, así que no hizo falta registrar nada. Corrí el reporte con fecha de corte 2026-11-25. Tiene 6 señales abiertas: 2 campañas pasadas de presupuesto, 2 con pauta facturada después de su fin y 2 sin meta.

# Cada campaña contra su presupuesto · Almacenes del Canal Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Canal Sintéticos (155634567-2-2020) · **Fecha de corte:** 2026-11-25 · **Agente:** Próspero, versión 1.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `campaign_over_budget` | C-01 · Temporada de fin de año: facturado 108,000,000 contra presupuesto de 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | `campaign_over_budget` | C-32 · Día de la familia: facturado 23,000,000 contra presupuesto de 20,000,000; la política tolera un 5 % más | 3,000,000.00 | — | `50-campanas/plan_de_mercadeo.xlsx` fila 8 |
| 3 | `campaign_ran_past_end` | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25,000,000.00 | 16 | `plan_de_mercadeo.xlsx` fila 4 · `facturas_de_pauta.xlsx` fila 5 |
| 4 | `campaign_ran_past_end` | C-42 · Verano: terminaba el 2026-09-30 y hay pauta facturada hasta el 2026-10-20 (F-42) | 9,000,000.00 | 20 | `plan_de_mercadeo.xlsx` fila 9 · `facturas_de_pauta.xlsx` fila 9 |
| 5 | `campaign_without_goal` | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | `plan_de_mercadeo.xlsx` fila 3 |
| 6 | `campaign_without_goal` | C-22 · Aniversario: el plan no le fija meta ni indicador | — | — | `plan_de_mercadeo.xlsx` fila 7 |

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

La corrida quedó registrada como `2026-11-25-budget-check-1` y lo mostrado está guardado en `corridas/salida-budget-check.md`.