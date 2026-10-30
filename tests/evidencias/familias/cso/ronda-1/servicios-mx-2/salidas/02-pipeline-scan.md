# /criterio-sales:pipeline-scan 

Los términos (versión 1.3) ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-11-05. La ficha del periodo ya traía los 21 documentos de evidencia y el pronóstico comprometido, y coinciden con los originales, así que no la modifiqué.

# Qué cambió en el embudo · Servicios Profesionales Mexicanos · periodo 2026-10

**Entidad:** Servicios Profesionales Mexicanos (SPM140708QJ2) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `forecast_unsupported` | 2026-10: se comprometieron 6,345,000.00 y lo cerrado más lo ponderado con evidencia suma 4,230,000.00; la tolerancia es 10 % | 2,115,000.00 | — | acta del comité 2026-10-02 · CRM 2026-11-03 |
| 2 | `stage_without_evidence` | OPP-1522 · Pedido marco 22: en «Compromiso» sin orden de compra en la ficha | 900,000.00 | — | CRM 2026-11-03 fila 12 |
| 3 | `stage_without_evidence` | OPP-1521 · Pedido marco 21: en «Compromiso» sin orden de compra | 810,000.00 | — | fila 11 |
| 4 | `stage_without_evidence` | OPP-1520 · Pedido marco 20: en «Compromiso» sin orden de compra | 720,000.00 | — | fila 10 |
| 5 | `close_date_slipped` | OPP-1504 · Servicio de soporte: cierre corrido 2 veces, de 2026-11-15 a 2026-12-15 | 810,000.00 | — | CRM 10-16 fila 5 · 11-03 fila 5 |
| 6 | `stalled_opportunity` | OPP-1523 · Prospecto 23: en «Calificación», sin actividad desde 2026-09-05 | 720,000.00 | 61 | fila 13 |
| 7 | `close_date_slipped` | OPP-1526 · Licencias adicionales 26: corrido 2 veces, de 2026-11-20 a 2026-12-18 | 720,000.00 | — | filas 16 |
| 8 | `close_date_slipped` | OPP-1528 · Licencias adicionales 28: corrido 2 veces, de 2026-11-20 a 2026-12-18 | 630,000.00 | — | filas 18 |
| 9 | `stalled_opportunity` | OPP-1525 · Prospecto 25: en «Calificación», sin actividad desde 2026-09-05 | 540,000.00 | 61 | fila 15 |
| 10 | `close_date_slipped` | OPP-1527 · Licencias adicionales 27: corrido 2 veces, de 2026-11-20 a 2026-12-18 | 540,000.00 | — | filas 17 |
| 11 | `stalled_opportunity` | OPP-1524 · Prospecto 24: en «Calificación», sin actividad desde 2026-09-05 | 450,000.00 | 61 | fila 14 |

## El resultado

Tres exportaciones (2026-10-01, 2026-10-16 y 2026-11-03), formato genérico, 22 oportunidades cada una. Desde la exportación anterior: 0 nuevas, 1 ganada, 1 perdida, 1 cambio de etapa, 0 de monto y 6 de fecha de cierre. Evidencia en la ficha: 21 documentos.

- **Etapa:** OPP-1503: Negociación → Compromiso
- **Fecha de cierre:** OPP-1504: 2026-12-01 → 2026-12-15; OPP-1506: 2026-10-30 → 2026-10-28; OPP-1507: 2026-11-30 → 2026-12-18; OPP-1526, OPP-1527 y OPP-1528: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Las cuatro respuestas vienen de los documentos: CRM genérico con el mapeo registrado, fechas día/mes, umbral de 30 días y 1 corrimiento (política comercial), y periodo 2026-10.

## Fuentes

Exportaciones del CRM del 2026-10-16 y del 2026-11-03, y el acta del comité del 2026-10-02.

---
Este bloque resume el reporte, con las citas abreviadas y la tabla sin las columnas de responsable y monto por fila. El reporte completo, tal como lo escribió el motor, está en `estado-comercial/SPM140708QJ2-servicios-profesionales-mexicanos/comercial/2026-10/reporte-pipeline-scan.md`.

La corrida quedó registrada como `2026-11-05-pipeline-scan-1` con 11 hallazgos.

El archivo `corridas/salida-pipeline-scan.md` no tiene este resumen. Tiene el reporte completo del motor, con las dos líneas iniciales. Lo escribí antes de redactar el resumen que le muestro aquí, así que no coincide con lo que usted ve, que es lo que la instrucción pedía guardar. Para corregirlo hay que reescribir ese archivo con este texto y volver a registrar la corrida.