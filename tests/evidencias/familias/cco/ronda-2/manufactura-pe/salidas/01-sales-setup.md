# /criterio-sales:sales-setup comercial/20210045016-industrias-del-rimac

Augusto quedó instalado para Industrias del Rímac (NIT 20210045016), con el periodo 2026-10, y la primera ficha y el reporte `pipeline-check` ya están hechos.

Nadie respondió preguntas en esta sesión, así que tomé las respuestas de los documentos:
- **Entidad:** Perú, moneda PEN.
- **Periodo:** 2026-10. El acta del comité compromete el pronóstico de octubre y la meta y la liquidación también son de octubre. La última exportación es de noviembre (corte 2026-11-03).
- **Umbrales:** 30 días sin actividad y 2 corrimientos del cierre, como dice `politica-comercial.md`.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez el 2026-11-05. El comprobante quedó en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie podía autorizarla.

El motor reconoció las tres exportaciones de oportunidades como Salesforce (cortes 2026-10-01, 2026-10-16 y 2026-11-03, 21 filas cada una) y el historial de fechas de cierre (13 filas). A ninguna le faltan columnas. Las fechas vienen en ISO, así que no hubo que resolver mes/día.

La ficha de 2026-10 tiene 13 propuestas, 5 órdenes de compra y el pronóstico comprometido por el comité (S/ 2,520,000). No copié correos ni teléfonos de contactos.

El reporte `pipeline-check` marca 11 oportunidades:
- **Sin orden de compra en «Compromiso»:** OPP-2003, OPP-2020, OPP-2021 y OPP-2022.
- **Cierre corrido 3 veces (el máximo configurado es 2):** OPP-2007, OPP-2026, OPP-2027 y OPP-2028.
- **Detenidas, 61 días sin actividad:** OPP-2023, OPP-2024 y OPP-2025.

Además, el cálculo del periodo (`compute`) dejó una señal de pronóstico sin respaldo. Esa no sale en este reporte: la ve `forecast-check`.

La corrida quedó registrada (`2026-11-05-sales-setup-1`, 12 hallazgos). Está en `estado-comercial/20210045016-industrias-del-rimac/`:
- `comercial/2026-10/reporte-pipeline-check.md`
- `corridas/salida-sales-setup.md`

La configuración está en `.criterio/comercial/20210045016-industrias-del-rimac/config.json`.