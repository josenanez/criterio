# /criterio-sales:sales-setup comercial/20210046021-consultores-asociados-de-lima

Soy Augusto. Pongo el embudo al lado de su evidencia y el pronóstico al lado de lo que lo sostiene; no califico a quien vende.

La instalación quedó lista. Las tres exportaciones de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) son de Dynamics 365 Sales y no les falta ninguna columna. Dejé el periodo en 2026-10, el del acta del comité, con 30 días de actividad y un solo corrimiento de cierre, como dice la política comercial. José Francisco Ñáñez aceptó los términos de la versión 1.3. Hice dos preguntas, con respuesta sugerida. La marca `_CRITERIO_COMERCIAL.txt` no se dejó en la carpeta.

**Términos aceptados (tal cual):** Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se prueba antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

# El embudo contra su evidencia · Consultores Asociados de Lima · periodo 2026-10

**Entidad:** Consultores Asociados de Lima (20210046021) · **Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0 · **Comando:** `pipeline-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2122 · Pedido marco 22: está en «Compromiso» y la ficha no tiene la orden de compra | 300,000.00 | — | — | `10-crm/oportunidades-2026-11-03.xlsx` fila 11 |
| 2 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2121 · Pedido marco 21: está en «Compromiso» y la ficha no tiene la orden de compra | 270,000.00 | — | — | `10-crm/oportunidades-2026-11-03.xlsx` fila 10 |
| 3 | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra (`stage_without_evidence`) | OPP-2120 · Pedido marco 20: está en «Compromiso» y la ficha no tiene la orden de compra | 240,000.00 | — | — | `10-crm/oportunidades-2026-11-03.xlsx` fila 9 |
| 4 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2104 · Servicio de soporte: la fecha de cierre se corrió 2 veces, de 2026-11-15 a 2026-12-15 | 270,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 5 · `10-crm/oportunidades-2026-11-03.xlsx` fila 5 |
| 5 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2123 · Prospecto 23: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 240,000.00 | — | 35 | `10-crm/oportunidades-2026-11-03.xlsx` fila 12 |
| 6 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2126 · Licencias adicionales 26: la fecha de cierre se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 240,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 15 · `10-crm/oportunidades-2026-11-03.xlsx` fila 15 |
| 7 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2128 · Licencias adicionales 28: la fecha de cierre se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 210,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 17 · `10-crm/oportunidades-2026-11-03.xlsx` fila 17 |
| 8 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2125 · Prospecto 25: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 180,000.00 | — | 35 | `10-crm/oportunidades-2026-11-03.xlsx` fila 14 |
| 9 | La fecha de cierre de una oportunidad se movió más veces de las configuradas (`close_date_slipped`) | OPP-2127 · Licencias adicionales 27: la fecha de cierre se corrió 2 veces, de 2026-11-20 a 2026-12-18 | 180,000.00 | — | — | `10-crm/oportunidades-2026-10-16.xlsx` fila 16 · `10-crm/oportunidades-2026-11-03.xlsx` fila 16 |
| 10 | Una oportunidad abierta no tiene actividad registrada en los días configurados (`stalled_opportunity`) | OPP-2124 · Prospecto 24: abierta en «Calificación», sin actividad desde el 2026-10-01 (35 días) | 150,000.00 | — | 35 | `10-crm/oportunidades-2026-11-03.xlsx` fila 13 |

## El resultado

| Oportunidad | Etapa | Monto | Cierre | Falta | Días sin actividad | Veces corrido |
|---|---|---|---|---|---|---|
| OPP-2101 · Renovación de licencias | Ganada | 360,000.00 | 2026-10-10 | — | 20 | 0 |
| OPP-2102 · Proyecto de expansión | Ganada | 540,000.00 | 2026-10-22 | — | 2 | 0 |
| OPP-2103 · Suministro anual | Compromiso | 750,000.00 | 2026-11-20 | — | 2 | 0 |
| OPP-2104 · Servicio de soporte | Propuesta | 270,000.00 | 2026-12-15 | — | 2 | 2 |
| OPP-2105 · Ampliación de contrato | Calificación | 240,000.00 | 2026-12-20 | — | 2 | 0 |
| OPP-2107 · Implementación por fases | Negociación | 330,000.00 | 2026-12-18 | — | 2 | 1 |
| OPP-2120 · Pedido marco 20 | Compromiso | 240,000.00 | 2026-12-12 | orden compra | 20 | 0 |
| OPP-2121 · Pedido marco 21 | Compromiso | 270,000.00 | 2026-12-12 | orden compra | 20 | 0 |
| OPP-2122 · Pedido marco 22 | Compromiso | 300,000.00 | 2026-12-12 | orden compra | 20 | 0 |
| OPP-2123 · Prospecto 23 | Calificación | 240,000.00 | 2026-12-18 | — | 35 | 0 |
| OPP-2124 · Prospecto 24 | Calificación | 150,000.00 | 2026-12-18 | — | 35 | 0 |
| OPP-2125 · Prospecto 25 | Calificación | 180,000.00 | 2026-12-18 | — | 35 | 0 |
| OPP-2126 · Licencias adicionales 26 | Calificación | 240,000.00 | 2026-12-18 | — | 2 | 2 |
| OPP-2127 · Licencias adicionales 27 | Calificación | 180,000.00 | 2026-12-18 | — | 2 | 2 |
| OPP-2128 · Licencias adicionales 28 | Calificación | 210,000.00 | 2026-12-18 | — | 2 | 2 |
| OPP-2129 · Cotización especial 29 | Negociación | 300,000.00 | 2026-12-10 | — | 20 | 0 |
| OPP-2130 · Cotización especial 30 | Negociación | 330,000.00 | 2026-12-10 | — | 20 | 0 |
| OPP-2131 · Venta directa 31 | Ganada | 90,000.00 | 2026-10-06 | — | 20 | 0 |
| OPP-2132 · Venta directa 32 | Ganada | 120,000.00 | 2026-10-07 | — | 20 | 0 |

Sin calificar a quien lleva cada oportunidad: la señal es de la oportunidad, no de la persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Dónde guardo lo que encuentro? → estado-comercial/20210046021-consultores-asociados-de-lima (respuesta sugerida, prueba sin interfaz)
- ¿Dejo la marca _CRITERIO_COMERCIAL.txt en la carpeta? → No (no se creó nada en la carpeta de documentos)

## Fuentes

- `10-crm/oportunidades-2026-10-16.xlsx`
- `10-crm/oportunidades-2026-11-03.xlsx`
- Fuentes técnicas: F-06 (families/criterio-cso/FUENTES.es.md)

Dos cosas que aclarar sobre lo que escribí en el archivo de la corrida y lo que mostré aquí:
- El archivo `salida-sales-setup.md` lleva mi introducción y el reporte, pero no el bloque de términos. Lo mostré aquí tal cual, pero no quedó escrito allí.
- Puse `max_close_moves` en 1 porque la política comercial permite correr el cierre una sola vez. Este plugin trae 2 por defecto.

La corrida quedó registrada como `2026-11-05-sales-setup-1`.