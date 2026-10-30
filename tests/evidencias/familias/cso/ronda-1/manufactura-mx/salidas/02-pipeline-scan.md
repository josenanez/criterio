# /criterio-sales:pipeline-scan 

Términos vigentes (versión 1.3, aceptados por José Francisco Ñáñez el 2026-11-05). Los 17 documentos de evidencia y el pronóstico comprometido del acta ya estaban en la ficha del periodo, con los mismos montos y fechas que los originales. No hubo que cambiarla.

# Qué cambió en el embudo · Manufacturas del Bajío · periodo 2026-10

**Entidad:** Manufacturas del Bajío (MBA120315KT4) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Etapa sin documento (`stage_without_evidence`) | OPP-1403 · Suministro anual: está en «Compromiso» y la ficha no tiene la orden de compra | 3,000,000.00 | — | `10-crm/oportunidades-2026-11-03.csv` fila 4 |
| 2 | Meta vs. cerrado (`target_vs_closed`) | 2026-10: cerrado 4,440,000.00 contra 6,216,000.00 esperado al corte (100 % del periodo de una meta de 6,216,000.00): -28.6 % | -1,776,000.00 | — | `00-referencia/metas.csv` fila 3 |
| 3 | Etapa sin documento | OPP-1423 · Pedido marco 23: en «Compromiso», sin orden de compra | 1,320,000.00 | — | `10-crm/oportunidades-2026-11-03.csv` fila 12 |
| 4 | Etapa sin documento | OPP-1422 · Pedido marco 22: en «Compromiso», sin orden de compra | 1,200,000.00 | — | `10-crm/oportunidades-2026-11-03.csv` fila 11 |
| 5 | Etapa sin documento | OPP-1421 · Pedido marco 21: en «Compromiso», sin orden de compra | 1,080,000.00 | — | `10-crm/oportunidades-2026-11-03.csv` fila 10 |
| 6 | Etapa sin documento | OPP-1420 · Pedido marco 20: en «Compromiso», sin orden de compra | 960,000.00 | — | `10-crm/oportunidades-2026-11-03.csv` fila 9 |
| 7 | Detenida (`stalled_opportunity`) | OPP-1427 · Prospecto 27: en «Calificación», sin actividad desde el 2026-09-05 | 960,000.00 | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 16 |
| 8 | Detenida | OPP-1426 · Prospecto 26: en «Calificación», sin actividad desde el 2026-09-05 | 840,000.00 | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 15 |
| 9 | Detenida | OPP-1405 · Ampliación de contrato: en «Calificación», sin actividad desde el 2026-09-12 | 840,000.00 | 54 | `10-crm/oportunidades-2026-11-03.csv` fila 6 |
| 10 | Detenida | OPP-1425 · Prospecto 25: en «Calificación», sin actividad desde el 2026-09-05 | 720,000.00 | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 14 |
| 11 | Detenida | OPP-1424 · Prospecto 24: en «Calificación», sin actividad desde el 2026-09-05 | 600,000.00 | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 13 |

## El resultado

Hay 3 exportaciones (2026-10-01, 2026-10-16 y 2026-11-03), de 19 oportunidades cada una.

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 17 documentos.

- **Etapa:** OPP-1403: Negociación → Compromiso
- **Fecha de cierre:** OPP-1404: 2026-12-10 → 2026-12-15; OPP-1406: 2026-10-30 → 2026-10-28; OPP-1407: 2026-11-30 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

`00-referencia/metas.csv`, `10-crm/oportunidades-2026-11-03.csv` y las fuentes técnicas F-02.

---

El reporte completo del motor está en `estado-comercial/MBA120315KT4-manufacturas-del-bajio/comercial/2026-10/reporte-pipeline-scan.md`. La corrida quedó registrada como `2026-11-05-pipeline-scan-1` con 11 hallazgos.

Para no recargar esta respuesta, dejé las columnas "Responsable" (vacía en todas las filas) y los nombres completos de las señales fuera de la tabla. El archivo que guardé en `corridas/salida-pipeline-scan.md` lleva el reporte tal como lo escribió el motor, con la tabla completa.