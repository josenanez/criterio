# /criterio-campaigns:campaigns-scan 

El inventario no trae documentos nuevos, cambiados ni borrados. La ficha del periodo ya tenía los tres resultados del informe de octubre tal como él los declara, así que no cambié nada en ella.

# Qué cambió en las campañas · Seguros Cordillera Sintéticos · periodo 2026-10

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 1.0.0 · **Comando:** `campaigns-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-32 · Día de la familia: la pauta facturada suma 23,000,000 y el presupuesto es 20,000,000; la política tolera un 5 % más | 3.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 8 |
| 3 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25.000.000,00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 4 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-42 · Verano: terminaba el 2026-09-30 y hay pauta facturada hasta el 2026-10-20 (F-42) | 9.000.000,00 | — | 20 | `50-campanas/plan_de_mercadeo.xlsx` fila 9 · `50-campanas/facturas_de_pauta.xlsx` fila 9 |
| 5 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 6 |
| 6 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-22 · Prensa Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 4.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 10 |
| 7 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-01 · Ventas atribuidas: el informe reporta 4,600 y la plataforma 4,100 al 2026-10-31; la política tolera un 2 % | 500,00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 2 |
| 8 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-03 · Visitas a la tienda: el informe reporta 3,100 y la plataforma 2,850 al 2026-10-31; la política tolera un 2 % | 250,00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 3 |
| 9 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |
| 10 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-22 · Aniversario: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 7 |

## El resultado

**Campañas en el plan:** 8 · **Facturas de pauta:** 9 · **Resultados reportados en la ficha:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/informe_de_resultados_2026-10.pdf`
- `50-campanas/plan_de_mercadeo.xlsx`
- `50-campanas/resultados_plataforma.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)