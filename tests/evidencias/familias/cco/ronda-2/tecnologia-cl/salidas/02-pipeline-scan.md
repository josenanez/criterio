# /criterio-sales:pipeline-scan 

Los términos vigentes (versión 1.3) ya estaban registrados a nombre de José Francisco Ñáñez. La ficha del periodo ya traía los documentos de evidencia y el pronóstico del acta, y coinciden con los originales; no hubo preguntas.

# Qué cambió en el embudo · Soluciones Digitales del Pacífico · periodo 2026-10

**Entidad:** Soluciones Digitales del Pacífico (77654321-7) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo cerrado al corte se aparta de la meta del periodo, prorrateada por los días transcurridos, más del umbral (`target_vs_closed`) | 2026-10: cerrado 333.000.000,00 contra 466.200.000,00 esperado al corte (100 % del periodo de una meta de 466.200.000,00): -28,6 % | -133.200.000,00 | — | — | `00-referencia/metas.csv` fila 3 |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige (`stage_without_evidence`) | OPP-2422 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 90.000.000,00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 11 |
| 3 | Ídem (`stage_without_evidence`) | OPP-2421 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 81.000.000,00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 10 |
| 4 | Ídem (`stage_without_evidence`) | OPP-2420 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 72.000.000,00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 9 |
| 5 | La fecha de cierre se movió más veces de las configuradas (`close_date_slipped`) | OPP-2404 · Servicio de soporte: se corrió 2 veces, de 2026-11-15 a 2026-12-15 | 81.000.000,00 | — | — | `10-crm/…-2026-10-16.csv` fila 5 · `10-crm/…-2026-11-03.csv` fila 5 |
| 6 | Oportunidad abierta sin actividad en los días configurados (`stalled_opportunity`) | OPP-2423 · Prospecto 23: «Calificación», sin actividad desde el 2026-09-05 (61 días) | 72.000.000,00 | — | 61 | `10-crm/…-2026-11-03.csv` fila 12 |
| 7 | `close_date_slipped` | OPP-2426 · Licencias adicionales 26: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 72.000.000,00 | — | — | `10-crm/…-2026-10-16.csv` fila 15 · `10-crm/…-2026-11-03.csv` fila 15 |
| 8 | `close_date_slipped` | OPP-2428 · Licencias adicionales 28: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 63.000.000,00 | — | — | `10-crm/…-2026-10-16.csv` fila 17 · `10-crm/…-2026-11-03.csv` fila 17 |
| 9 | `stalled_opportunity` | OPP-2425 · Prospecto 25: «Calificación», sin actividad desde el 2026-09-05 (61 días) | 54.000.000,00 | — | 61 | `10-crm/…-2026-11-03.csv` fila 14 |
| 10 | `close_date_slipped` | OPP-2427 · Licencias adicionales 27: se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 54.000.000,00 | — | — | `10-crm/…-2026-10-16.csv` fila 16 · `10-crm/…-2026-11-03.csv` fila 16 |
| 11 | `stalled_opportunity` | OPP-2424 · Prospecto 24: «Calificación», sin actividad desde el 2026-09-05 (61 días) | 45.000.000,00 | — | 61 | `10-crm/…-2026-11-03.csv` fila 13 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/hubspot-crm-exports-deals-2026-10-01.csv` | 2026-10-01 | hubspot | 20 |
| `10-crm/hubspot-crm-exports-deals-2026-10-16.csv` | 2026-10-16 | hubspot | 20 |
| `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` | 2026-11-03 | hubspot | 20 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 17 documentos.

- **Etapa:** OPP-2403: Negociación → Compromiso
- **Fecha de cierre:** OPP-2404: 2026-12-01 → 2026-12-15; OPP-2406: 2026-10-30 → 2026-10-28; OPP-2407: 2026-11-30 → 2026-12-18; OPP-2426: 2026-12-04 → 2026-12-18; OPP-2427: 2026-12-04 → 2026-12-18; OPP-2428: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/metas.csv`
- `10-crm/hubspot-crm-exports-deals-2026-10-16.csv`
- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- Fuentes técnicas: F-04 (families/criterio-cso/FUENTES.es.md)

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 11 hallazgos.

Dos aclaraciones sobre lo que escribí en la salida:
- **Tabla de señales:** abrevié las filas 3 a 11 (texto repetido de la señal y rutas de las citas con `…`). Lo que quedó guardado en `corridas/salida-pipeline-scan.md` es el reporte completo del motor, sin abreviar.
- **Ficha:** no la modifiqué.