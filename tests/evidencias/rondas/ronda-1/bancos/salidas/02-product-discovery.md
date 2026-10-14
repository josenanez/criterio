# /criterio-product:product-discovery 

Leí las cuatro piezas de PRD-306 (Microseguros) y salió un solo tema, con una sola cita. No creé ningún requerimiento y no pude sellar la lectura. La corrida quedó registrada con id `2026-10-14-product-discovery-1`.

- **Términos:** la versión 1.0 ya estaba aceptada en la configuración y coincide con `TERMS.md`.
- **Material:** solo una pieza es de descubrimiento, la entrevista del 2025-08-22. Las otras tres son la definición, el caso de negocio y el acta del comité del 2026-10-09.
- **Tema:** «Necesidad principal», 1 de 1 piezas. La cita es *«Lo necesito y hoy no lo tengo.»*, de un cliente sin nombre ni segmento. Cuenta como dicho una sola vez y no dice qué es lo que necesita.
- **Registro:** `estado/requirements` está vacío, así que ningún requerimiento recoge el tema. El comité lista cinco (REQ-1060, 1061, 1062, 1063 y 2025) con «Cliente entrevistado» como origen, pero la entrevista no contiene nada que permita atribuírselos. Cuatro están aceptados y ninguno tiene proyecto que lo ejecute.
- **Sin sellar:** el script `sellar` se negó porque `estado/producto.json` sigue siendo la plantilla vacía y no se escribió en esta corrida. La próxima corrida volverá a ver estos documentos como nuevos.
- **Sin contradicciones:** no hay nada contra qué contradecir porque el registro está vacío. Tampoco entraron fuentes públicas ni cifras de entrevistados.
- **Sin requerimiento propuesto:** para crear uno en `propuesto` hace falta alguien que lo asuma y nadie respondió en esta sesión.

Sugiero `/criterio-product:product-requirements` para ver el registro con sus vacíos. Si quieres llenar la ficha antes de volver a sellar, `/criterio-product:product-setup`.

Archivos en `estado/corridas/`:
- `salida-product-discovery.md`