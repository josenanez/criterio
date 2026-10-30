# /criterio-sales:pipeline-scan 

Sesión de prueba sin interfaz: los términos estaban vigentes (aceptados por José Francisco Ñáñez) y no hubo preguntas. La ficha del periodo ya recogía los 21 documentos de evidencia y el acta del comité tal como los leí, así que no la modifiqué.

# Qué cambió en el embudo · Servicios Profesionales Mexicanos · periodo 2026-10

**Entidad:** Servicios Profesionales Mexicanos (SPM140708QJ2) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.1.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Lo comprometido supera lo que sostiene la evidencia, más de la tolerancia (`forecast_unsupported`) | 2026-10: se comprometieron 6,345,000.00 y lo cerrado más lo ponderado con evidencia suma 4,230,000.00; la tolerancia es 10 % | 2,115,000.00 | — | acta del comité 2026-10-02 · exportación 2026-11-03 |
| 2 | Etapa sin el documento que exige (`stage_without_evidence`) | OPP-1522 · Pedido marco 22: en «Compromiso», sin orden de compra en la ficha | 900,000.00 | — | exportación 2026-11-03, fila 12 |
| 3 | ídem | OPP-1521 · Pedido marco 21: en «Compromiso», sin orden de compra | 810,000.00 | — | fila 11 |
| 4 | ídem | OPP-1520 · Pedido marco 20: en «Compromiso», sin orden de compra | 720,000.00 | — | fila 10 |
| 5 | Oportunidad detenida (`stalled_opportunity`) | OPP-1523 · Prospecto 23: «Calificación», sin actividad desde 2026-09-05 | 720,000.00 | 61 | fila 13 |
| 6 | ídem | OPP-1525 · Prospecto 25: «Calificación», sin actividad desde 2026-09-05 | 540,000.00 | 61 | fila 15 |
| 7 | ídem | OPP-1524 · Prospecto 24: «Calificación», sin actividad desde 2026-09-05 | 450,000.00 | 61 | fila 14 |

## El resultado

Se procesaron tres exportaciones (2026-10-01, 2026-10-16 y 2026-11-03), de 22 oportunidades cada una.

**Desde la exportación anterior:** 0 nuevas, 1 ganada, 1 perdida, 1 cambio de etapa, 0 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 21 documentos.

- **Etapa:** OPP-1503: Negociación → Compromiso
- **Fecha de cierre:** OPP-1504: 2026-12-01 → 2026-12-15; OPP-1506: 2026-10-30 → 2026-10-28; OPP-1507: 2026-11-30 → 2026-12-18; OPP-1526, OPP-1527 y OPP-1528: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `10-crm/oportunidades-2026-11-03.xlsx`
- `20-comite/acta-comite-2026-10-02.docx`

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con 7 hallazgos. La salida completa está en `corridas/salida-pipeline-scan.md`.

Dos cosas que no resolví:
- Registré la salida con el reporte en forma resumida en este mensaje, pero el archivo guardado lleva el reporte del motor íntegro. Si necesitas que coincidan palabra por palabra, el archivo es la versión de referencia.
- El motor aceptó `--today 2026-11-05` en todas las llamadas.