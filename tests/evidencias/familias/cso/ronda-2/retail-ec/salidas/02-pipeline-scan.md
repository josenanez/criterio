# /criterio-sales:pipeline-scan 

Procesé tres exportaciones del CRM, 19 documentos de evidencia y el acta del comité. La ficha de octubre ya los traía, así que no la cambié. Los términos estaban vigentes (versión 1.3, aceptada por José Francisco Ñáñez el 2026-11-05). No hubo preguntas que responder.

# Qué cambió en el embudo · Comercial Andina del Pacífico · periodo 2026-10

**Fecha de corte:** 2026-11-03 · **Procesado:** 2026-11-05 · **Agente:** Augusto, versión 0.2.0

## Lo que hay que atender (10 señales)

1. **Pronóstico sin respaldo suficiente (`forecast_unsupported`).** El comité comprometió 945,000.00 y lo cerrado más lo ponderado con evidencia suma 630,000.00. La diferencia es 315,000.00 y la tolerancia es 10 %.
2. **Cinco oportunidades en «Compromiso» sin orden de compra en la ficha (`stage_without_evidence`).**
   - OPP-1703 · Suministro anual: 375,000.00
   - OPP-1723 · Pedido marco 23: 165,000.00
   - OPP-1722 · Pedido marco 22: 150,000.00
   - OPP-1721 · Pedido marco 21: 135,000.00
   - OPP-1720 · Pedido marco 20: 120,000.00
3. **Cuatro oportunidades en «Calificación» sin actividad desde el 2026-10-01, 35 días (`stalled_opportunity`).**
   - OPP-1705 · Ampliación de contrato: 105,000.00
   - OPP-1726 · Prospecto 26: 105,000.00
   - OPP-1725 · Prospecto 25: 90,000.00
   - OPP-1724 · Prospecto 24: 75,000.00

## El resultado

- **Exportaciones:** las de 2026-10-01, 2026-10-16 y 2026-11-03, todas en formato Dynamics y con 19 oportunidades cada una.
- **Desde la exportación anterior:** 0 nuevas, 1 ganada, 1 perdida, 1 cambio de etapa, 0 de monto y 3 de fecha de cierre.
- **Cambio de etapa:** OPP-1703 pasó de Negociación a Compromiso.
- **Cambios de fecha de cierre:**
  - OPP-1704: 2026-12-10 → 2026-12-15
  - OPP-1706: 2026-10-30 → 2026-10-28
  - OPP-1707: 2026-11-30 → 2026-12-18
- **Evidencia en la ficha:** 19 documentos.

Todo lo que llegó se procesó. No hay preguntas en esta corrida.

**Fuentes:** `10-crm/oportunidades-2026-11-03.xlsx` y `20-comite/acta-comite-2026-10-02.docx`.

El reporte completo está en `estado-comercial/1790123456001-comercial-andina-del-pacifico/comercial/2026-10/reporte-pipeline-scan.md`. La corrida quedó registrada como `2026-11-05-pipeline-scan-1`, con la salida guardada en `corridas/salida-pipeline-scan.md`.