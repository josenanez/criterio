# /criterio-sales:sales-wake 

Tocaba el barrido de la revisión semanal del embudo de Manufatcuras del Bajío. No llegó nada nuevo ni cambió nada: 33 archivos, ninguno fuera de lugar. No había peticiones abiertas y los términos están vigentes.

Mostré el reporte del periodo de la configuración, 2026-10, porque la ficha con la evidencia está ahí. Antes lo corrí sobre 2026-11, que no tiene ficha, y ese reporte da como faltantes todas las propuestas aunque sí existen. Quedó guardado en `estado-comercial/MBA120315KT4-manufacturas-del-bajio/comercial/2026-11/reporte-pipeline-check.md`, así que no lo tomes en cuenta.

# El embudo contra su evidencia · Manufacturas del Bajío · periodo 2026-10

**Entidad:** Manufacturas del Bajío (MBA120315KT4) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 1.2.3 · **Comando:** `pipeline-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1403 · Suministro anual: está en «Compromiso» y la ficha no tiene la orden de compra | 3,000,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 4 |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1423 · Pedido marco 23: está en «Compromiso» y la ficha no tiene la orden de compra | 1,320,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 12 |
| 3 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1422 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 1,200,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 11 |
| 4 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1421 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 1,080,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 10 |
| 5 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1420 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 960,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 9 |
| 6 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1427 · Prospecto 27: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 960,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 16 |
| 7 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1426 · Prospecto 26: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 840,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 15 |
| 8 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1405 · Ampliación de contrato: abierta en «Calificación», sin actividad desde el 2026-09-12 (54 días) | 840,000.00 | — | 54 | `10-crm/oportunidades-2026-11-03.csv` fila 6 |
| 9 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1425 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 720,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 14 |
| 10 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1424 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 600,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 13 |

## El resultado

| Oportunidad | Etapa | Monto | Cierre | Falta | Días sin actividad | Veces corrido |
|---|---|---|---|---|---|---|
| OPP-1401 · Renovación de licencias | Ganada | 1,440,000.00 | 2026-10-10 | — | 26 | 0 |
| OPP-1402 · Proyecto de expansión | Ganada | 2,160,000.00 | 2026-10-22 | — | 14 | 0 |
| OPP-1403 · Suministro anual | Compromiso | 3,000,000.00 | 2026-11-20 | orden compra | 6 | 0 |
| OPP-1404 · Servicio de soporte | Propuesta | 1,080,000.00 | 2026-12-15 | — | 7 | 1 |
| OPP-1405 · Ampliación de contrato | Calificación | 840,000.00 | 2026-12-20 | — | 54 | 0 |
| OPP-1407 · Implementación por fases | Negociación | 1,320,000.00 | 2026-12-18 | — | 5 | 1 |
| OPP-1420 · Pedido marco 20 | Compromiso | 960,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-1421 · Pedido marco 21 | Compromiso | 1,080,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-1422 · Pedido marco 22 | Compromiso | 1,200,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-1423 · Pedido marco 23 | Compromiso | 1,320,000.00 | 2026-12-12 | orden compra | 6 | 0 |
| OPP-1424 · Prospecto 24 | Calificación | 600,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-1425 · Prospecto 25 | Calificación | 720,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-1426 · Prospecto 26 | Calificación | 840,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-1427 · Prospecto 27 | Calificación | 960,000.00 | 2026-12-18 | — | 61 | 0 |
| OPP-1428 · Cotización especial 28 | Negociación | 1,080,000.00 | 2026-12-10 | — | 7 | 0 |
| OPP-1429 · Cotización especial 29 | Negociación | 1,200,000.00 | 2026-12-10 | — | 7 | 0 |
| OPP-1430 · Venta directa 30 | Ganada | 360,000.00 | 2026-10-06 | — | 30 | 0 |
| OPP-1431 · Venta directa 31 | Ganada | 480,000.00 | 2026-10-07 | — | 29 | 0 |

Sin calificar a quien lleva cada oportunidad: la señal es de la oportunidad, no de la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿La entidad es Manufacturas del Bajío, RFC MBA120315KT4, en México y en MXN? → Sí (respuesta sugerida, sesión de prueba)
- ¿El periodo es 2026-10? → Sí (respuesta sugerida, sesión de prueba)
- ¿Las exportaciones de 10-crm/ son informes de Salesforce con fechas mes/día? → Sí (respuesta sugerida, sesión de prueba)
- ¿Se usa la tabla de etapas de 00-referencia/etapas.csv tal como está? → Sí (respuesta sugerida, sesión de prueba)
- ¿30 días sin actividad detienen una oportunidad y un cierre puede correrse hasta 2 veces? → Sí (respuesta sugerida, sesión de prueba)
- ¿Lo que encuentre se guarda en estado-comercial/MBA120315KT4-manufacturas-del-bajio? → Sí (respuesta sugerida, sesión de prueba)
- ¿Dejo el archivo _CRITERIO_COMERCIAL.txt en la carpeta raíz? → No: nadie lo autorizó en la sesión de prueba

## Fuentes

- `10-crm/oportunidades-2026-11-03.csv`
- Fuentes técnicas: F-02 (families/criterio-cco/FUENTES.es.md)

---

Quedaron registradas las corridas `2026-11-05-sales-wake-1`, `2026-11-05-pipeline-scan-2` y `2026-11-05-pipeline-check-2`, todas con el caso 2026-10. Lo que te mostré quedó guardado en `estado-comercial/MBA120315KT4-manufacturas-del-bajio/corridas/salida-sales-wake.md`.