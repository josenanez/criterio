# /criterio-product:product-discovery 

Leí los 5 documentos de PRD-309 (Crédito de libre inversión), pero de descubrimiento hay una sola entrevista, así que no hay síntesis que hacer. No se creó ningún requerimiento.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.
- **El único tema:** «Necesidad principal», 1 de 1 piezas. La cita es *«Lo necesito y hoy no lo tengo.»*, de un cliente entrevistado sin nombre ni segmento, el 2025-09-06. Esa pieza tiene 13 meses, más que el umbral de 12 de la configuración.
- **Sin vínculo con el registro:** ninguno de los 15 requerimientos tiene la necesidad escrita, y el acta del 2026-10-09 atribuye 11 a «Cliente entrevistado» sin citar qué dijo. No pude atar la cita a ninguno y no lo inventé.
- **Sin promover:** una sola voz no vale como «dicho muchas veces». Quedó registrada como dicha una vez, ni promovida ni descartada.
- **Otras secciones:** no hay afirmaciones numéricas de entrevistados, ni fuentes públicas, ni evidencia que contradiga el registro.
- **Recálculo (`compute`):** 15 requerimientos, 11 aceptados y 4 propuestos, con 31 señales abiertas. La más llamativa no es de descubrimiento: el caso de negocio declara `volumen_mensual` en 117.145 y el tablero mide 85.140, un 27,3 % menos. Eso toca `/product-definition`.
- **Sin sellar:** `sellar` se negó porque la ficha `producto.json` no se escribió en esta corrida, y este comando no la escribe. No lo forcé, así que la próxima corrida volverá a tratar estos 5 documentos como nuevos.

La corrida quedó registrada con `corrida`: 32 s, 31 hallazgos. La salida completa está en `estado-producto/PRD-309/corridas/salida-product-discovery.md`.