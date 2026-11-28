# /criterio-sales:sales-wake 

Hoy tocaba la revisión semanal del embudo de Almacenes del Istmo. No había peticiones abiertas y los términos están vigentes. El inventario no trae documentos nuevos ni cambiados, así que no hubo nada que llevar a la ficha. Abajo van los dos reportes tal como los escribió el motor.

# Qué cambió en el embudo · Almacenes del Istmo · periodo 2026-10

**Entidad:** Almacenes del Istmo (155622222-2-2017) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 1.4.2 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo comprometido supera lo que suman las oportunidades con evidencia, ponderadas por su etapa, más de la tolerancia configurada (`forecast_unsupported`) | 2026-10: se comprometieron 945,000.00 y lo cerrado más lo ponderado con evidencia suma 630,000.00; la tolerancia es 10 % | 315,000.00 | — | — | `20-comite/acta-comite-2026-10-02.docx, «Pronóstico de octubre»` · `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2603 · Suministro anual: está en «Compromiso» y la ficha no tiene la orden de compra | 375,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 4 |
| 3 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2623 · Pedido marco 23: está en «Compromiso» y la ficha no tiene la orden de compra | 165,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 13 |
| 4 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2622 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 150,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 12 |
| 5 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2621 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 135,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 11 |
| 6 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2620 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 120,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 10 |
| 7 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2626 · Prospecto 26: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 105,000.00 | — | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 16 |
| 8 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2605 · Ampliación de contrato: abierta en «Calificación», sin actividad desde el 2026-09-12 (54 días) | 105,000.00 | — | 54 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 6 |
| 9 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2625 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 90,000.00 | — | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 15 |
| 10 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2624 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 75,000.00 | — | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 14 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/hubspot-crm-exports-deals-2026-10-01.csv` | 2026-10-01 | hubspot | 19 |
| `10-crm/hubspot-crm-exports-deals-2026-10-16.csv` | 2026-10-16 | hubspot | 19 |
| `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` | 2026-11-03 | hubspot | 19 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 19 documentos.

- **Etapa:** OPP-2603: Negociación → Compromiso
- **Fecha de cierre:** OPP-2604: 2026-12-10 → 2026-12-15; OPP-2606: 2026-10-30 → 2026-10-28; OPP-2607: 2026-11-30 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿De qué CRM salen las exportaciones de 10-crm/? → HubSpot (reconocido por el motor en los tres cortes); respuesta sugerida, sesión de prueba
- ¿Qué columna trae la empresa asociada? → Associated Company; respuesta sugerida, sesión de prueba
- ¿Cuántos días sin actividad detienen una oportunidad y cuántas veces puede correrse un cierre? → 30 días y 2 veces, según 00-referencia/politica-comercial.md; respuesta sugerida, sesión de prueba
- ¿Qué periodo se revisa? → 2026-10, el del acta del comité y la liquidación; respuesta sugerida, sesión de prueba

## Fuentes

- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- `20-comite/acta-comite-2026-10-02.docx, «Pronóstico de octubre»`
- Fuentes técnicas: F-04 (families/criterio-cco/FUENTES.es.md)

---

# El embudo contra su evidencia · Almacenes del Istmo · periodo 2026-10

**Entidad:** Almacenes del Istmo (155622222-2-2017) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 1.4.2 · **Comando:** `pipeline-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2603 · Suministro anual: está en «Compromiso» y la ficha no tiene la orden de compra | 375,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 4 |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2623 · Pedido marco 23: está en «Compromiso» y la ficha no tiene la orden de compra | 165,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 13 |
| 3 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2622 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 150,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 12 |
| 4 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2621 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 135,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 11 |
| 5 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2620 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 120,000.00 | — | — | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 10 |
| 6 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2626 · Prospecto 26: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 105,000.00 | — | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 16 |
| 7 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2605 · Ampliación de contrato: abierta en «Calificación», sin actividad desde el 2026-09-12 (54 días) | 105,000.00 | — | 54 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 6 |
| 8 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2625 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 90,000.00 | — | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 15 |
| 9 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2624 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 75,000.00 | — | 61 | `10-crm/hubspot-crm-exports-deals-2026-11-03.csv` fila 14 |

## El resultado

| Oportunidad | Etapa | Monto | Cierre | Falta | Días sin actividad | Veces corrido |
|---|---|---|---|---|---|---|
| OPP-2601 · Renovación de licencias | Ganada | 180,000.00 | 2026-10-10 | — | 26 | 0 |
| OPP-2602 · Proyecto de expansión | Ganada | 270,000.00 | 2026-10-22 | — | 14 | 0 |
| OPP-2603 · Suministro anual | Compromiso | 375,000.00 | 2026-11-20 | orden compra | 6 | 0 |
| OPP-2604 · Servicio de soporte | Propuesta | 135,000.00 | 2026-12-15 | — | 7 | 1 |
| OPP-2605 · Ampliación de contrato | Calificación | 105,000.00 | 2026-12-20 | — | 54 | 0 |
| OPP-2607 · Implementación por fases | Negociación | 165,000.00 | 2026-12-18 | — | 5 | 1 |
| OPP-2608 · Venta de equipos | Ganada | 75,000.00 | 2026-10-05 | — | 31 | 0 |
| OPP-2620 · Pedido marco 20 | Compromiso | 120,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-2621 · Pedido marco 21 | Compromiso | 135,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-2622 · Pedido marco 22 | Compromiso | 150,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-2623 · Pedido marco 23 | Compromiso | 165,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-2624 · Prospecto 24 | Calificación | 75,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-2625 · Prospecto 25 | Calificación | 90,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-2626 · Prospecto 26 | Calificación | 105,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-2627 · Cotización especial 27 | Negociación | 180,000.00 | 2026-12-10 | — | 7 | 0 |
| OPP-2628 · Cotización especial 28 | Negociación | 135,000.00 | 2026-12-10 | — | 7 | 0 |
| OPP-2629 · Venta directa 29 | Ganada | 45,000.00 | 2026-10-06 | — | 30 | 0 |
| OPP-2630 · Venta directa 30 | Ganada | 60,000.00 | 2026-10-07 | — | 29 | 0 |

Sin calificar a quien lleva cada oportunidad: la señal es de la oportunidad, no de la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿De qué CRM salen las exportaciones de 10-crm/? → HubSpot (reconocido por el motor en los tres cortes); respuesta sugerida, sesión de prueba
- ¿Qué columna trae la empresa asociada? → Associated Company; respuesta sugerida, sesión de prueba
- ¿Cuántos días sin actividad detienen una oportunidad y cuántas veces puede correrse un cierre? → 30 días y 2 veces, según 00-referencia/politica-comercial.md; respuesta sugerida, sesión de prueba
- ¿Qué periodo se revisa? → 2026-10, el del acta del comité y la liquidación; respuesta sugerida, sesión de prueba

## Fuentes

- `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`
- `20-comite/acta-comite-2026-10-02.docx, «Pronóstico de octubre»`
- Fuentes técnicas: F-04 (families/criterio-cco/FUENTES.es.md)

---

Quedaron registradas tres corridas, todas con el periodo 2026-10 como caso: `2026-11-05-sales-wake-1`, `2026-11-05-pipeline-scan-2` y `2026-11-05-pipeline-check-2`. Lo que se mostró quedó en `estado-comercial/155622222-2-2017-almacenes-del-istmo/corridas/salida-sales-wake.md`.

Una cosa a revisar: el registro de `pipeline-check` dice 10 hallazgos, pero su reporte trae 9 señales. La diferencia sería la del pronóstico, que aparece en `pipeline-scan` y no en este reporte. Eso es lo que más probablemente pasa, pero no lo comprobé en el motor.