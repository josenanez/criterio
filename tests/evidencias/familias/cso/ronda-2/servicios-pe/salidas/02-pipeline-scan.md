# /criterio-sales:pipeline-scan 

Los términos de esta versión ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-11-05). Los 17 documentos de evidencia y el acta del comité ya estaban en la ficha del periodo y coinciden con los textos, así que no cambié nada. Estas son las señales de esta corrida.

# Qué cambió en el embudo · Consultores Asociados de Lima · periodo 2026-10

**Entidad:** Consultores Asociados de Lima (20210046021) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo cerrado al corte se aparta de la meta del periodo, prorrateada por los días transcurridos, más del umbral (`target_vs_closed`) | 2026-10: cerrado 1,110,000.00 contra 1,554,000.00 esperado al corte (100 % del periodo de una meta de 1,554,000.00): -28.6 % | -444,000.00 | — | — | `00-referencia/metas.csv` fila 3 |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2122 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 300,000.00 | — | — | `10-crm/oportunidades-2026-11-03.xlsx` fila 11 |
| 3 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2121 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 270,000.00 | — | — | `10-crm/oportunidades-2026-11-03.xlsx` fila 10 |
| 4 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2120 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 240,000.00 | — | — | `10-crm/oportunidades-2026-11-03.xlsx` fila 9 |
| 5 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2104 · Servicio de soporte: la fecha de cierre se corrió 2 veces, de 2026-11-15 a 2026-12-15 | 270,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 5 · `10-crm/oportunidades-2026-11-03.xlsx` fila 5 |
| 6 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2123 · Prospecto 23: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 240,000.00 | — | 35 | `10-crm/oportunidades-2026-11-03.xlsx` fila 12 |
| 7 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2126 · Licencias adicionales 26: la fecha de cierre se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 240,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 15 · `10-crm/oportunidades-2026-11-03.xlsx` fila 15 |
| 8 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2128 · Licencias adicionales 28: la fecha de cierre se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 210,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 17 · `10-crm/oportunidades-2026-11-03.xlsx` fila 17 |
| 9 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2125 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 180,000.00 | — | 35 | `10-crm/oportunidades-2026-11-03.xlsx` fila 14 |
| 10 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2127 · Licencias adicionales 27: la fecha de cierre se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 180,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 16 · `10-crm/oportunidades-2026-11-03.xlsx` fila 16 |
| 11 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2124 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 150,000.00 | — | 35 | `10-crm/oportunidades-2026-11-03.xlsx` fila 13 |

## El resultado

| Exportación | Fecha | Formato | Oportunidades |
|---|---|---|---|
| `10-crm/oportunidades-2026-10-01.xlsx` | 2026-10-01 | dynamics | 20 |
| `10-crm/oportunidades-2026-10-16.xlsx` | 2026-10-16 | dynamics | 20 |
| `10-crm/oportunidades-2026-11-03.xlsx` | 2026-11-03 | dynamics | 20 |

**Desde la exportación anterior:** 0 nuevas, 1 ganadas, 1 perdidas, 1 cambios de etapa, 1 de monto y 6 de fecha de cierre. **Evidencia en la ficha:** 17 documentos.

- **Etapa:** OPP-2103: Negociación → Compromiso
- **Monto:** OPP-2105: 225,000.00 → 240,000.00
- **Fecha de cierre:** OPP-2104: 2026-12-01 → 2026-12-15; OPP-2106: 2026-10-30 → 2026-10-28; OPP-2107: 2026-11-30 → 2026-12-18; OPP-2126: 2026-12-04 → 2026-12-18; OPP-2127: 2026-12-04 → 2026-12-18; OPP-2128: 2026-12-04 → 2026-12-18

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dónde guardo lo que encuentro? → estado-comercial/20210046021-consultores-asociados-de-lima (respuesta sugerida, prueba sin interfaz)
- ¿Dejo la marca _CRITERIO_COMERCIAL.txt en la carpeta? → No (no se creó nada en la carpeta de documentos)

## Fuentes

- `00-referencia/metas.csv`
- `10-crm/oportunidades-2026-10-16.xlsx`
- `10-crm/oportunidades-2026-11-03.xlsx`
- Fuentes técnicas: F-06 (families/criterio-cso/FUENTES.es.md)

La corrida quedó registrada como `2026-11-05-pipeline-scan-1` con 11 hallazgos.