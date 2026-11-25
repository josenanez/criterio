# /criterio-campaigns:campaigns-wake 

Hoy solo tocaba la revisión semanal (`campaigns-scan`). No había peticiones abiertas y los términos ya estaban aceptados. Desde la corrida anterior no llegó ningún documento nuevo ni cambió ninguno, y la ficha del periodo ya tenía los resultados del informe. Siguen abiertas tres señales.

# Qué cambió en las campañas · Banco Altiplano Sintético · periodo 2026-10

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `campaigns-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política (`campaign_over_budget`) | C-01 · Temporada de fin de año: la pauta facturada suma 108,000,000 y el presupuesto es 100,000,000; la política tolera un 5 % más | 8,000,000.00 | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 2 |
| 2 | Una factura de pauta no tiene campaña del plan ni orden de compra (`media_invoice_unmatched`) | F-105 · Radio Sintética: no dice a qué campaña pertenece y no tiene orden de compra | 7,000,000.00 | — | — | `50-campanas/facturas_de_pauta.xlsx` fila 6 |
| 3 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-01 · Ventas atribuidas: el informe reporta 4,600 y la plataforma 4,100 al 2026-10-31; la política tolera un 2 % | 500.00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 2 |

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

---

Quedaron registradas dos corridas: `2026-11-25-campaigns-scan-2` y `2026-11-25-campaigns-wake-1`.