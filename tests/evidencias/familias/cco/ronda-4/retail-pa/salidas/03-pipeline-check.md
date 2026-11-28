# /criterio-sales:pipeline-check 

Los términos ya estaban vigentes (aceptados en la versión 1.4.2), así que no hubo que registrar la aceptación. Corrí el reporte de 2026-11 con `--today 2026-11-05` y dejé la corrida registrada. El motor la registró con 10 hallazgos, aunque el reporte lista 13 señales. No averigüé por qué difieren.

El reporte es el de Almacenes del Istmo, con corte de la exportación al 2026-11-03.

# El embudo contra su evidencia · Almacenes del Istmo · periodo 2026-11

**Lo que hay que atender (13 señales, ordenadas por monto):**

**Sin el documento que exige su etapa (9):**

| Oportunidad | Etapa | Monto | Falta |
|---|---|---|---|
| OPP-2603 · Suministro anual | Compromiso | 375,000.00 | propuesta, orden de compra |
| OPP-2627 · Cotización especial 27 | Negociación | 180,000.00 | propuesta |
| OPP-2607 · Implementación por fases | Negociación | 165,000.00 | propuesta |
| OPP-2623 · Pedido marco 23 | Compromiso | 165,000.00 | propuesta, orden de compra |
| OPP-2622 · Pedido marco 22 | Compromiso | 150,000.00 | propuesta, orden de compra |
| OPP-2604 · Servicio de soporte | Propuesta | 135,000.00 | propuesta |
| OPP-2621 · Pedido marco 21 | Compromiso | 135,000.00 | propuesta, orden de compra |
| OPP-2628 · Cotización especial 28 | Negociación | 135,000.00 | propuesta |
| OPP-2620 · Pedido marco 20 | Compromiso | 120,000.00 | propuesta, orden de compra |

**Detenidas, sin actividad (4):**

| Oportunidad | Etapa | Monto | Días sin actividad |
|---|---|---|---|
| OPP-2626 · Prospecto 26 | Calificación | 105,000.00 | 61 |
| OPP-2605 · Ampliación de contrato | Calificación | 105,000.00 | 54 |
| OPP-2625 · Prospecto 25 | Calificación | 90,000.00 | 61 |
| OPP-2624 · Prospecto 24 | Calificación | 75,000.00 | 61 |

**El resultado:**
- La tabla completa tiene 18 oportunidades.
- En la tabla, OPP-2604 y OPP-2607 son las únicas con el cierre corrido, una vez cada una.
- Cinco oportunidades en «Ganada» tampoco tienen propuesta ni orden de compra: OPP-2601, 2602, 2608, 2629 y 2630. El reporte las muestra en la tabla, pero no las lista entre las señales.

**Lo que no se pudo procesar:** la ficha no trae el pronóstico comprometido de 2026-11 en `20-comite/`, así que no se compara.

**Preguntas que hizo:** ninguna.

**Fuentes:** `10-crm/hubspot-crm-exports-deals-2026-11-03.csv`.

La señal es de la oportunidad, no de quien la lleva.

El reporte completo está en `estado-comercial/155622222-2-2017-almacenes-del-istmo/comercial/2026-11/reporte-pipeline-check.md`. Lo mostrado quedó en `corridas/salida-pipeline-check.md`, en esa misma carpeta de estado, y la corrida quedó registrada como `2026-11-05-pipeline-check-1`.