# /criterio-product:product-spec 

El borrador de especificación de Recaudos (PRD-306) quedó sin secciones de comportamiento, porque el registro no dice qué pide ninguno de los 14 requerimientos aceptados. Cada uno tiene solo su identificador, sin título ni necesidad ni prioridad. Escribir qué hace cada uno habría sido inventarlo, así que los dejé a la vista en vez de rellenarlos.

Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré otra vez. La corrida tardó 39 segundos y registró 37 hallazgos.

- **Cobertura:** 0 de 14 aceptados con comportamiento especificado. Los 14 están en la tabla de no cubiertos, cada uno con su motivo.
- **Fuera del alcance:** REQ-4602 y REQ-4607 siguen en `propuesto`, así que no los especifiqué.
- **Criterios de aceptación:**
  - Nueve dicen solo «se verifica en producción», que indica dónde verificar pero no qué medir, y por eso no es verificable ni medible hoy.
  - Cinco no tienen criterio: REQ-4601, 4603, 4610, 4611 y 4613.
  - No redacté criterios sustitutos, porque eso exigiría saber qué pide cada requerimiento.
- **Vacíos con dueño:**
  - No hay criterio de éxito del producto, ni casos borde definidos.
  - El acta no dice quién aceptó cada requerimiento.
  - Ningún requerimiento tiene proyecto que lo construya, y el acta dice «Se mantiene el plan» sin que haya plan en los documentos.
  - La única evidencia de demanda es una entrevista de 2025-09-23, ya vencida, que no nombra ningún requerimiento. REQ-4604, 4606, 4608 y 4614 no tienen ninguna.
  - Hay dependencias con otros equipos sin acordar.
- **Supuestos:**
  - El del proveedor figura como verificado el 2026-10-01. Pero el documento técnico del proveedor que lo sustenta no está en la carpeta, y la fecha de declaración del supuesto es posterior a la fecha de la definición.
  - La cifra de volumen mensual (214.523) es declarada, sin medición.
- **Sin hacer:** no corrí el barrido normativo (`regulatory-sweep`). Lo dejé escrito como vacío sin resolver, no como ausencia de obligaciones.
- **Después:** no ofrezco `/product-charter`, porque los vacíos no están cerrados y el producto no tiene criterio de éxito.

La salida completa quedó en `estado-producto/PRD-306/corridas/salida-product-spec.md`, y la corrida registrada es `2026-10-23-product-spec-1`.