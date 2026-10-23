# /criterio-product:product-spec 

El borrador de especificación de PRD-309 (Inspección con drones) no tiene comportamiento redactable. Ninguno de los 13 requerimientos aceptados dice qué necesidad cubre: todos tienen el título vacío («Requerimiento REQ-49xx») y la necesidad sin dato. Escribir comportamiento habría sido inventarlo.

Los términos ya estaban vigentes (versión 1.2, aceptada por José Francisco Ñáñez el 2026-10-22), así que no se pidió nada. Corrí `corrida-inicio` antes de leer. La corrida quedó registrada con 15 requerimientos leídos, 50 segundos y 35 hallazgos. El borrador completo está en `estado-producto/PRD-309/corridas/salida-product-spec.md`.

- **Cobertura:** 0 de 13 requerimientos aceptados. REQ-4904 y REQ-4912 están en `propuesto` y quedan fuera de alcance.
- **Criterios de aceptación:**
  - Diez requerimientos tienen «se verifica en producción», que no es verificable: dice dónde, no qué se mide.
  - REQ-4901, REQ-4903 y REQ-4913 no tienen ningún criterio.
  - No hay documento que diga qué se mide hoy en la organización.
- **Evidencia:** REQ-4900 y REQ-4907 no tienen ninguna. Los otros 11 se apoyan en la misma entrevista genérica de 2025-08-21, que tiene 14 meses y no nombra ningún requerimiento.
- **Proyecto:** ninguno de los 13 tiene un proyecto que lo ejecute.
- **Decisión:** el acta no dice quién decidió la aceptación; su única decisión es «Se mantiene el plan».
- **Supuesto de la definición:** «La licencia ambiental lo permite» sigue sin verificar y sin dueño. Su fecha (2026-05-15) es posterior a la de la definición (2026-03-17), y nada lo explica.
- **Propuesta y éxito:** la propuesta principal no tiene contenido y el criterio de éxito del producto no está dicho.
- **Caso de negocio:** el volumen de 270.035 no tiene serie ni fuente, y el retorno esperado no tiene cifra.
- **REQ-2028:** queda fuera de la serie REQ-49xx.
- **Normativa:** como no hay país declarado, no cité ninguna norma. Los cuatro puntos del barrido están en «no tengo la norma a la vista» o «sin resolver»: operación de drones, licencia ambiental, datos personales en las imágenes y retención.

No ofrezco `/product-charter`: los vacíos no están cerrados y ningún requerimiento tiene criterio verificable. Cada vacío de la tabla del borrador lleva su dueño propuesto, casi siempre el doliente del requerimiento o Laura Vélez.