# /criterio-sales:sales-setup comercial/MBA120315KT4-manufacturas-del-bajio

Soy Augusto. Dejé instalada la entidad Manufacturas del Bajío (MBA120315KT4, México, MXN) con periodo 2026-10, y la corrida quedó registrada.

- **Exportaciones:** las tres del CRM (1 y 16 de octubre, 3 de noviembre) son Salesforce, completas, con 19 filas cada una. Las fechas van mes/día, porque `10/22/2026` no admite otra lectura.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez el 2026-11-05. Los comprobantes están en `.criterio/terminos/` (Markdown y PDF).
- **Preguntas:** no le hice ninguna a nadie. Las respuestas salieron de los documentos, así que **confírmalas**:
  - El periodo es 2026-10.
  - Una oportunidad se detiene a los 30 días sin actividad.
  - Un cierre puede correrse hasta 2 veces.
  - Los demás umbrales (tolerancia del pronóstico 10 %, umbral de la meta 15 %) son los de `config.example.json`. Ningún documento los fija.
  - La tabla de etapas es la de `etapas.csv`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie lo autorizó.

El motor encontró 11 señales:

- **Etapa sin su documento:** 5 oportunidades están en «Compromiso» sin orden de compra: OPP-1403, 1420, 1421, 1422 y 1423.
- **Detenidas:** 5 oportunidades abiertas llevan entre 54 y 61 días sin actividad: OPP-1405 y 1424 a 1427.
- **Meta:** 1 señal de meta contra lo cerrado.

El reporte completo está en `estado-comercial/MBA120315KT4-manufacturas-del-bajio/comercial/2026-10/reporte-pipeline-check.md`. Lo que te mostré quedó en `corridas/salida-sales-setup.md`.

La ficha del periodo tiene las 13 propuestas y las 4 órdenes de compra (OPP-1401, 1402, 1430 y 1431). Los correos y teléfonos de los clientes no entraron. Como pronóstico comprometido registré $4,662,000, del acta del 2 de octubre. El mejor escenario de $7,104,000 no va, porque el acta dice que no se compromete.