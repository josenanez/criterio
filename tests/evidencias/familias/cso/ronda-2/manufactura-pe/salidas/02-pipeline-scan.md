# /criterio-sales:pipeline-scan 

Corrida registrada (`2026-11-05-pipeline-scan-1`). Los términos estaban vigentes, aceptados por José Francisco Ñáñez el 2026-11-05. La ficha ya tenía los 18 documentos de evidencia y el acta del comité, así que no agregué nada. Las dos preguntas que quedaban las tomé de los documentos: el periodo es octubre 2026.

Un error mío sin consecuencias: un comando suelto contra `<temporal>` falló porque esa ruta es un directorio, y no se tocó nada.

---

# Qué cambió en el embudo · Industrias del Rímac · periodo 2026-10

**Entidad:** Industrias del Rímac (20210045016) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | `forecast_unsupported` | 2026-10: se comprometieron 2,520,000.00 y lo cerrado más lo ponderado con evidencia suma 1,680,000.00; la tolerancia es 10 % | 840,000.00 | — | acta del comité 2026-10-02 · `10-crm/oportunidades-2026-11-03.csv` |
| 2 | `stage_without_evidence` | OPP-2003 · Suministro anual: en «Compromiso», sin orden de compra en la ficha | 1,000,000.00 | — | `oportunidades-2026-11-03.csv` fila 4 |
| 3 | `stage_without_evidence` | OPP-2022 · Pedido marco 22: en «Compromiso», sin orden de compra | 400,000.00 | — | fila 12 |
| 4 | `stage_without_evidence` | OPP-2021 · Pedido marco 21: en «Compromiso», sin orden de compra | 360,000.00 | — | fila 11 |
| 5 | `stage_without_evidence` | OPP-2020 · Pedido marco 20: en «Compromiso», sin orden de compra | 320,000.00 | — | fila 10 |
| 6 | `close_date_slipped` | OPP-2007 · Implementación por fases: fecha de cierre corrida 3 veces, de 2026-10-31 a 2026-12-18 | 440,000.00 | — | `historial-2026-11-03.csv` filas 2–4 |
| 7 | `stalled_opportunity` | OPP-2023 · Prospecto 23: en «Calificación», sin actividad desde el 2026-09-05 | 320,000.00 | 61 | `oportunidades-2026-11-03.csv` fila 13 |
| 8 | `close_date_slipped` | OPP-2026 · Renovación anual 26: corrida 3 veces, de 2026-11-08 a 2026-12-20 | 320,000.00 | — | `historial-2026-11-03.csv` filas 5–7 |
| 9 | `close_date_slipped` | OPP-2028 · Renovación anual 28: corrida 3 veces, de 2026-11-08 a 2026-12-20 | 280,000.00 | — | filas 11–13 |
| 10 | `stalled_opportunity` | OPP-2025 · Prospecto 25: en «Calificación», sin actividad desde el 2026-09-05 | 240,000.00 | 61 | `oportunidades-2026-11-03.csv` fila 15 |
| 11 | `close_date_slipped` | OPP-2027 · Renovación anual 27: corrida 3 veces, de 2026-11-08 a 2026-12-20 | 240,000.00 | — | filas 8–10 |
| 12 | `stalled_opportunity` | OPP-2024 · Prospecto 24: en «Calificación», sin actividad desde el 2026-09-05 | 200,000.00 | 61 | fila 14 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/oportunidades-2026-10-01.csv` | 2026-10-01 | salesforce | 21 |
| `10-crm/oportunidades-2026-10-16.csv` | 2026-10-16 | salesforce | 21 |
| `10-crm/oportunidades-2026-11-03.csv` | 2026-11-03 | salesforce | 21 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 18 documentos.

- **Etapa:** OPP-2003: Negociación → Compromiso
- **Fecha de cierre:** OPP-2004: 2026-12-10 → 2026-12-15; OPP-2006: 2026-10-30 → 2026-10-28; OPP-2007: 2026-11-30 → 2026-12-18; OPP-2026, OPP-2027 y OPP-2028: 2026-12-01 → 2026-12-20

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Periodo de la primera ficha: octubre o noviembre? → Octubre 2026 (2026-10), por el acta del comité del 2026-10-02 y la liquidación 2026-10; respuesta sugerida tomada de los documentos en la prueba sin interfaz.

## Fuentes

- `10-crm/historial-2026-11-03.csv`, `10-crm/oportunidades-2026-11-03.csv`
- `20-comite/acta-comite-2026-10-02.docx, «El comité compromete para octubre un pronóstico de ventas de S/ 2,520,000»`
- Fuentes técnicas: F-02 (families/criterio-cso/FUENTES.es.md)

---

El reporte está en `estado-comercial/20210045016-industrias-del-rimac/comercial/2026-10/reporte-pipeline-scan.md`. La salida de la corrida quedó en `corridas/salida-pipeline-scan.md`.