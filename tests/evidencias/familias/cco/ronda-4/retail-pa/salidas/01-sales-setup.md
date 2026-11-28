# /criterio-sales:sales-setup comercial/155622222-2-2017-almacenes-del-istmo

Soy Augusto. Pongo el embudo al lado de su evidencia y el pronóstico al lado de lo que lo sostiene; no califico a quien vende.

**Carpeta:** encontré una sola candidata, `comercial/155622222-2-2017-almacenes-del-istmo`, que tiene 00-referencia/, 10-crm/, 20-comite/, 30-evidencia/, 40-cotizaciones/ y 50-comisiones/. Respuesta sugerida: sí, es esa.

**Preguntas, con la respuesta que tomé de los documentos** (es una sesión de prueba, así que nadie las respondió):
1. **Entidad y país:** Almacenes del Istmo, RUC 155622222-2-2017, Panamá, en USD.
2. **Periodo:** 2026-10, el del acta del comité y el de la liquidación.
3. **CRM:** HubSpot. El motor lo reconoció en los tres cortes (2026-10-01, 2026-10-16 y 2026-11-03), con 19 filas cada uno y sin columnas faltantes. No hizo ninguna pregunta.
4. **Empresa asociada:** la columna `Associated Company`, registrada en `crm.columns.cuenta`.
5. **Etapas:** salen de `00-referencia/etapas.csv`. Propuesta exige la propuesta; Compromiso exige la orden de compra.
6. **Umbrales:** 30 días sin actividad detienen una oportunidad y un cierre puede correrse 2 veces, según `00-referencia/politica-comercial.md`.
7. **Dónde guardo lo que encuentro:** `estado-comercial/155622222-2-2017-almacenes-del-istmo`.
8. **Marca:** sí. Quedó `_CRITERIO_COMERCIAL.txt` en la carpeta de la entidad.

**Términos (versión 1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los aceptó José Francisco Ñáñez el 2026-11-05. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-sales-1.4.2-2026-11-05.md` y `.pdf`.

**Configuración:** quedó escrita en `.criterio/comercial/155622222-2-2017-almacenes-del-istmo/config.json`.

---

Crucé cada documento de `30-evidencia/` y el pronóstico comprometido en el acta del 2 de octubre contra el último corte del CRM. Las oportunidades en Compromiso que no tienen orden de compra y las detenidas en Calificación son lo primero que hay que revisar en el comité.

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
- Fuentes técnicas: F-04 (families/criterio-cco/FUENTES.es.md)

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito, y en esta prueba no lo hubo. Para correrlo a mano: `/criterio-sales:sales-wake`.

La corrida quedó registrada como `2026-11-05-sales-setup-1`, con la salida en `estado-comercial/155622222-2-2017-almacenes-del-istmo/corridas/salida-sales-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.