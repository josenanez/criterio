# /criterio-campaigns:budget-check 

Una campaña pasó su presupuesto más la tolerancia: C-01. El reporte completo sigue tal cual lo escribió el motor.

# Cada campaña contra su presupuesto · Banco Altiplano Sintético · periodo 2026-11

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | 1200 recompras | Recompras |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |

Si se amplía un presupuesto o se cierra una campaña lo decide el área: aquí se dice cuál se pasó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-budget-check-1`.