# /criterio-sales:pipeline-scan 

Los términos ya estaban vigentes (versión 1.3, aceptada el 2026-11-05 por José Francisco Ñáñez). La ficha ya tenía los 19 documentos de evidencia y el pronóstico del acta, y coinciden con los originales. No hubo preguntas.

# Qué cambió en el embudo · Tiendas del Maipo · periodo 2026-10

**Entidad:** Tiendas del Maipo (76543210-3) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `forecast_unsupported` | Se comprometieron 756.000.000 y lo cerrado más lo ponderado con evidencia suma 504.000.000; la tolerancia es 10 % | 252.000.000 | — | acta 2026-10-02, sección Pronóstico de octubre · `Deals_2026_11_03.xlsx` |
| 2 | `stage_without_evidence` | OPP-2303 · Suministro anual: en «Compromiso», sin orden de compra en la ficha | 300.000.000 | — | `Deals_2026_11_03.xlsx` fila 4 |
| 3 | `stage_without_evidence` | OPP-2323 · Pedido marco 23: en «Compromiso», sin orden de compra | 132.000.000 | — | fila 13 |
| 4 | `stage_without_evidence` | OPP-2322 · Pedido marco 22: en «Compromiso», sin orden de compra | 120.000.000 | — | fila 12 |
| 5 | `stage_without_evidence` | OPP-2321 · Pedido marco 21: en «Compromiso», sin orden de compra | 108.000.000 | — | fila 11 |
| 6 | `stage_without_evidence` | OPP-2320 · Pedido marco 20: en «Compromiso», sin orden de compra | 96.000.000 | — | fila 10 |
| 7 | `stalled_opportunity` | OPP-2305 · Ampliación de contrato: en «Calificación», sin actividad desde 2026-10-01 | 84.000.000 | 35 | fila 6 |
| 8 | `stalled_opportunity` | OPP-2326 · Prospecto 26: en «Calificación», sin actividad desde 2026-10-01 | 84.000.000 | 35 | fila 16 |
| 9 | `stalled_opportunity` | OPP-2325 · Prospecto 25: en «Calificación», sin actividad desde 2026-10-01 | 72.000.000 | 35 | fila 15 |
| 10 | `stalled_opportunity` | OPP-2324 · Prospecto 24: en «Calificación», sin actividad desde 2026-10-01 | 60.000.000 | 35 | fila 14 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/Deals_2026_10_01.xlsx` | 2026-10-01 | zoho | 19 |
| `10-crm/Deals_2026_10_16.xlsx` | 2026-10-16 | zoho | 19 |
| `10-crm/Deals_2026_11_03.xlsx` | 2026-11-03 | zoho | 19 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 19 documentos.

- **Etapa:** OPP-2303: Negociación → Compromiso
- **Fecha de cierre:** OPP-2304: 2026-12-10 → 2026-12-15; OPP-2306: 2026-10-30 → 2026-10-28; OPP-2307: 2026-11-30 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-crm/Deals_2026_11_03.xlsx`
- `20-comite/acta-comite-2026-10-02.docx, sección Pronóstico de octubre`
- Fuentes técnicas: F-08 (families/criterio-cso/FUENTES.es.md)

La salida quedó en `estado-comercial/76543210-3-tiendas-del-maipo/corridas/salida-pipeline-scan.md`. La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 10 hallazgos.