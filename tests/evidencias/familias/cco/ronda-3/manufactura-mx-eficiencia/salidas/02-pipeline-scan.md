# /criterio-sales:pipeline-scan 

La ficha de 2026-10 ya tenía las 17 evidencias de `30-evidencia/` y el pronóstico comprometido del acta del comité. Los dos coinciden con los documentos, así que no se agregó nada.
Los correos y teléfonos de contacto que traen las propuestas no se pasaron a la ficha.

# Qué cambió en el embudo · Manufacturas del Bajío · periodo 2026-10

**Entidad:** Manufacturas del Bajío (MBA120315KT4) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 1.2.3 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1403 · Suministro anual: está en «Compromiso» y la ficha no tiene la orden de compra | 3,000,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 4 |
| 2 | Lo cerrado al corte se aparta de la meta del periodo, prorrateada por los días transcurridos, más del umbral (`target_vs_closed`) | 2026-10: cerrado 4,440,000.00 contra 6,216,000.00 esperado al corte (100 % del periodo de una meta de 6,216,000.00): -28.6 % | -1,776,000.00 | — | — | `00-referencia/metas.csv` fila 3 |
| 3 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1423 · Pedido marco 23: está en «Compromiso» y la ficha no tiene la orden de compra | 1,320,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 12 |
| 4 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1422 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 1,200,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 11 |
| 5 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1421 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 1,080,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 10 |
| 6 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-1420 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 960,000.00 | — | — | `10-crm/oportunidades-2026-11-03.csv` fila 9 |
| 7 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1427 · Prospecto 27: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 960,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 16 |
| 8 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1426 · Prospecto 26: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 840,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 15 |
| 9 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1405 · Ampliación de contrato: abierta en «Calificación», sin actividad desde el 2026-09-12 (54 días) | 840,000.00 | — | 54 | `10-crm/oportunidades-2026-11-03.csv` fila 6 |
| 10 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1425 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 720,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 14 |
| 11 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-1424 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-09-05 (61 días) | 600,000.00 | — | 61 | `10-crm/oportunidades-2026-11-03.csv` fila 13 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/oportunidades-2026-10-01.csv` | 2026-10-01 | salesforce | 19 |
| `10-crm/oportunidades-2026-10-16.csv` | 2026-10-16 | salesforce | 19 |
| `10-crm/oportunidades-2026-11-03.csv` | 2026-11-03 | salesforce | 19 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 0 de monto y 3 de fecha de cierre. **Evidencia en la ficha:** 17 documentos.

- **Etapa:** OPP-1403: Negociación → Compromiso
- **Fecha de cierre:** OPP-1404: 2026-12-10 → 2026-12-15; OPP-1406: 2026-10-30 → 2026-10-28; OPP-1407: 2026-11-30 → 2026-12-18

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

- `00-referencia/metas.csv`
- `10-crm/oportunidades-2026-11-03.csv`
- Fuentes técnicas: F-02 (families/criterio-cco/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-05-pipeline-scan-1`. Lo que se mostró está guardado en `<espacio>/estado-comercial/MBA120315KT4-manufacturas-del-bajio/corridas/salida-pipeline-scan.md`.