# /criterio-campaigns:budget-check 

Términos vigentes (versión 1.6, aceptada). Este es el reporte de presupuesto del periodo 2026-11. Si se amplía un presupuesto o se cierra una campaña, lo decide el área de mercadeo.

# Cada campaña contra su presupuesto · Banco Altiplano Sintético · periodo 2026-11

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.2.0 · **Comando:** `budget-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Pauta facturada por encima del presupuesto más la tolerancia (`campaign_over_budget`) | C-01 · Temporada de fin de año: facturado 108,000,000, presupuesto 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | `plan_de_mercadeo.xlsx` fila 2 |
| 2 | Ídem | C-33 · Hogar: facturado 54,000,000, presupuesto 50,000,000 | 4,000,000.00 | — | `plan_de_mercadeo.xlsx` fila 11 |
| 3 | Ídem | C-32 · Día de la familia: facturado 23,000,000, presupuesto 20,000,000 | 3,000,000.00 | — | `plan_de_mercadeo.xlsx` fila 10 |
| 4 | Pauta facturada después del fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta hasta el 2026-10-31 (F-104) | 25,000,000.00 | 16 | `plan_de_mercadeo.xlsx` fila 4 · `facturas_de_pauta.xlsx` fila 5 |
| 5 | Ídem | C-43 · Feria escolar: terminaba el 2026-10-10 y hay pauta hasta el 2026-10-25 (F-43) | 11,000,000.00 | 15 | `plan_de_mercadeo.xlsx` fila 13 · `facturas_de_pauta.xlsx` fila 12 |
| 6 | Ídem | C-42 · Verano: terminaba el 2026-09-30 y hay pauta hasta el 2026-10-20 (F-42) | 9,000,000.00 | 20 | `plan_de_mercadeo.xlsx` fila 12 · `facturas_de_pauta.xlsx` fila 11 |
| 7 | Campaña sin meta ni indicador (`campaign_without_goal`) | C-02 · Clientes recurrentes | — | — | `plan_de_mercadeo.xlsx` fila 3 |
| 8 | Ídem | C-22 · Aniversario | — | — | `plan_de_mercadeo.xlsx` fila 8 |
| 9 | Ídem | C-23 · Gran venta de noviembre | — | — | `plan_de_mercadeo.xlsx` fila 9 |

## El resultado

**Tolerancia de la política sobre el presupuesto:** 5 %.

| Campaña | Presupuesto | Facturado | Inicio | Fin | Meta | Indicador |
|---|---|---|---|---|---|---|
| C-01 · Temporada de fin de año | 100,000,000 | 108,000,000 | 2026-09-01 | 2026-10-31 | 5000 ventas | Ventas atribuidas |
| C-02 · Clientes recurrentes | 40,000,000 | 18,000,000 | 2026-09-15 | 2026-11-30 | — | — |
| C-03 · Lanzamiento de la colección | 60,000,000 | 25,000,000 | 2026-09-01 | 2026-10-15 | 3000 visitas a la tienda | Visitas a la tienda |
| C-04 · Marca | 30,000,000 | 0 | 2026-08-01 | 2026-12-31 | 2 millones de impresiones | Impresiones |
| C-12 · Reactivación | 15,000,000 | 0 | 2026-10-01 | 2026-11-30 | 800 clientes reactivados | Clientes reactivados |
| C-13 · Referidos | 12,000,000 | 0 | 2026-10-01 | 2026-12-15 | 500 referidos | Referidos |
| C-22 · Aniversario | 25,000,000 | 0 | 2026-10-01 | 2026-11-15 | — | — |
| C-23 · Gran venta de noviembre | 35,000,000 | 0 | 2026-10-15 | 2026-11-30 | — | — |
| C-32 · Día de la familia | 20,000,000 | 23,000,000 | 2026-09-01 | 2026-10-31 | 900 ventas | Ventas atribuidas |
| C-33 · Hogar | 50,000,000 | 54,000,000 | 2026-09-01 | 2026-10-31 | 1500 ventas | Ventas atribuidas |
| C-42 · Verano | 18,000,000 | 9,000,000 | 2026-08-01 | 2026-09-30 | 1000 visitas a la tienda | Visitas a la tienda |
| C-43 · Feria escolar | 22,000,000 | 11,000,000 | 2026-09-01 | 2026-10-10 | 1200 visitas a la tienda | Visitas a la tienda |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-budget-check-1` con 15 hallazgos.

Dos aclaraciones:
- El archivo de salida que guardé lleva el reporte del motor completo. Aquí condensé algunas celdas repetidas, como los textos de señal "Ídem" y la columna Responsable, que estaba vacía.
- Nadie respondió preguntas. La aceptación de términos no hizo falta registrarla de nuevo, porque ya figuraba aceptada con la versión 0.2.0.