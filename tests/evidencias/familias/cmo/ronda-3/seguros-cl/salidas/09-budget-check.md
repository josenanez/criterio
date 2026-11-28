# /criterio-campaigns:budget-check 

Términos vigentes (versión 1.6, ya aceptados en la instalación). Este es el reporte del motor tal cual:

# Cada campaña contra su presupuesto · Seguros Cordillera Sintéticos · periodo 2026-11

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 1.0.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Pauta facturada sobre presupuesto + tolerancia (`campaign_over_budget`) | C-01 · Temporada de fin de año: facturado 108,000,000 vs presupuesto 100,000,000; tolerancia 5 % | 8.000.000,00 | — | `plan_de_mercadeo.xlsx` fila 2 |
| 2 | `campaign_over_budget` | C-32 · Día de la familia: facturado 23,000,000 vs 20,000,000; tolerancia 5 % | 3.000.000,00 | — | `plan_de_mercadeo.xlsx` fila 8 |
| 3 | Pauta después del fin (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba 2026-10-15, pauta hasta 2026-10-31 (F-104) | 25.000.000,00 | 16 | plan fila 4 · `facturas_de_pauta.xlsx` fila 5 |
| 4 | `campaign_ran_past_end` | C-42 · Verano: terminaba 2026-09-30, pauta hasta 2026-10-20 (F-42) | 9.000.000,00 | 20 | plan fila 9 · facturas fila 9 |
| 5 | Sin meta ni indicador (`campaign_without_goal`) | C-02 · Clientes recurrentes | — | — | plan fila 3 |
| 6 | `campaign_without_goal` | C-22 · Aniversario | — | — | plan fila 7 |

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

**No se pudo procesar:** nada; todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.
**Fuentes:** `50-campanas/facturas_de_pauta.xlsx`, `50-campanas/plan_de_mercadeo.xlsx`, F-02 (families/criterio-cmo/FUENTES.es.md).

Corrida registrada (`2026-11-25-budget-check-1`, 10 hallazgos). El archivo de salida (`salida-budget-check.md`) es una copia del reporte completo del motor. La tabla de arriba omite la columna «Responsable», que venía vacía en las seis filas.