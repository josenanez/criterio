# /criterio-campaigns:campaigns-scan 

El inventario no encontró documentos nuevos, modificados ni borrados. La ficha del periodo ya tenía los tres resultados del informe tal como el informe los declara, así que no hubo nada que agregar. Las cinco señales de abajo las decide el área de mercadeo, junto con quien firma el informe.

# Qué cambió en las campañas · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `campaigns-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8.000.000,00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25.000.000,00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 3 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7.000.000,00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 6 |
| 4 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-01 · Ventas atribuidas: el informe reporta 4,600 y la plataforma 4,100 al 2026-10-31; la política tolera un 2 % | 500,00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 2 |
| 5 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |

## El resultado

**Campañas en el plan:** 4 · **Facturas de pauta:** 5 · **Resultados reportados en la ficha:** 3.

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