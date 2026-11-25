# /criterio-campaigns:campaigns-scan 

Los términos están vigentes; los aceptó José Francisco Ñáñez. No llegaron documentos nuevos ni cambiados desde la corrida anterior. La ficha de 2026-10 ya tenía los tres resultados del informe tal como él los trae, así que no le agregué nada. Debajo va el reporte del motor tal cual.

# Qué cambió en las campañas · Consumo Maya Sintético · periodo 2026-10

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `campaigns-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay pauta facturada después de la fecha de fin de la campaña (`campaign_ran_past_end`) | C-03 · Lanzamiento de la colección: terminaba el 2026-10-15 y hay pauta facturada hasta el 2026-10-31 (F-104) | 25,000,000.00 | — | 16 | `50-campanas/plan_de_mercadeo.xlsx` fila 4 · `50-campanas/facturas_de_pauta.xlsx` fila 5 |
| 2 | Una campaña no tiene meta ni indicador de medición (`campaign_without_goal`) | C-02 · Clientes recurrentes: el plan no le fija meta ni indicador | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 |

## El resultado

**Campañas en el plan:** 4 · **Facturas de pauta:** 5 · **Resultados reportados en la ficha:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/facturas_de_pauta.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-campaigns-scan-1` con 2 hallazgos. Lo que se mostró arriba quedó guardado en `estado-mercadeo/cms210415xy3-consumo-maya-sintetico/corridas/salida-campaigns-scan.md`.