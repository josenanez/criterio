# /criterio-sales:pipeline-scan 

Procesé las tres exportaciones del CRM y los 15 documentos de evidencia que ya estaban en la ficha, más el pronóstico comprometido del acta del comité. No había nada nuevo que llevar a la ficha. Las señales de abajo salen del motor.

# Qué cambió en el embudo · Soluciones Digitales Andinas · periodo 2026-10

**Entidad:** Soluciones Digitales Andinas (900876543) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `target_vs_closed` | 2026-10: cerrado 264.000.000,00 contra 369.600.000,00 esperado al corte (100 % del periodo de una meta de 369.600.000,00): -28,6 % | -105.600.000,00 | — | `00-referencia/metas.csv` fila 3 |
| 2 | `stage_without_evidence` | OPP-1222 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 80.000.000,00 | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 11 |
| 3 | `stage_without_evidence` | OPP-1221 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 72.000.000,00 | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 10 |
| 4 | `stage_without_evidence` | OPP-1220 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 64.000.000,00 | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 9 |
| 5 | `stalled_opportunity` | OPP-1223 · Prospecto 23: abierta en «Calificación», sin actividad desde el 2026-09-05 | 64.000.000,00 | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 12 |
| 6 | `stalled_opportunity` | OPP-1205 · Ampliación de contrato: abierta en «Calificación», sin actividad desde el 2026-09-12 | 56.000.000,00 | 54 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 6 |
| 7 | `stalled_opportunity` | OPP-1225 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-09-05 | 48.000.000,00 | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 14 |
| 8 | `stalled_opportunity` | OPP-1224 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-09-05 | 40.000.000,00 | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 13 |

## El resultado

Las tres exportaciones HubSpot (2026-10-01, 2026-10-16 y 2026-11-03) traen 19 oportunidades cada una.

**Desde la exportación anterior:** 0 nuevas, 1 ganada, 1 perdida, 1 cambio de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 15 documentos.

- **Etapa:** OPP-1203: Negociación → Compromiso
- **Fecha de cierre:** OPP-1204: 2026-12-01 → 2026-12-15; OPP-1206: 2026-10-30 → 2026-10-28; OPP-1207: 2026-11-30 → 2026-12-18; OPP-1226, OPP-1227 y OPP-1228: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Las seis respuestas sugeridas se tomaron de los documentos: HubSpot como CRM, la columna `Associated Company`, el periodo 2026-10, los umbrales por omisión de 30 días y 2 corridas de cierre, y la carpeta de estado. No se creó la marca `_CRITERIO_COMERCIAL.txt`.

## Fuentes

`00-referencia/metas.csv` y `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`.

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`. Los términos ya estaban vigentes (versión 1.3, aceptados por José Francisco Ñáñez el 2026-11-05), así que no hubo que mostrarlos otra vez.

Este texto abrevia el reporte completo en las columnas «Responsable» y «Días», en la lista de exportaciones y en las preguntas. El reporte íntegro está en `estado-comercial/900876543-soluciones-digitales-andinas/comercial/2026-10/reporte-pipeline-scan.md`. El archivo `corridas/salida-pipeline-scan.md` guarda el reporte entero precedido de las dos líneas de introducción, no este texto abreviado.