# /criterio-product:product-spec 

Con el registro actual no se puede escribir ninguna sección de comportamiento para PRD-309, así que el borrador salió como esqueleto con los vacíos a la vista. Los 13 requerimientos aceptados llegan al acta del comité solo con su número. Ninguno dice qué pide, y los 15 tienen la necesidad sin encontrar. Rellenarlo con algo razonable habría sido decidir por el comité.

**Términos y cuestiones.** Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-17), así que no registré nada nuevo. Nadie respondió preguntas en esta sesión, y no hubo ninguna que contestar.

**Alcance**
- **Entran:** los 13 aceptados, solo por número y sin descripción.
- **No entran:** REQ-4905 y REQ-4908, que siguen en `propuesto`. Tampoco entra ninguna función de la tarjeta, porque ningún documento las dice.

**Criterios de aceptación**
- 9 requerimientos tienen solo «se verifica en producción». Eso no es verificable, porque dos personas no llegarían a la misma respuesta.
- 4 no tienen criterio: REQ-4901, 4907, 4909 y 4913.
- No propuse criterios propios.

**Supuestos y cifras**
- «El cliente paga por la entrega rápida» lleva 31 días sin verificar, contra un umbral de 30. Su fecha (2026-09-16) tampoco cuadra con la de la definición (2026-02-23), y no se ve qué relación tiene con una tarjeta de la tienda.
- El caso de negocio declara 278.242 de volumen mensual y lo medido es 214.637, una brecha de 22,9 % (umbral configurado: 20 %).

**Vacíos**
- Qué pide cada requerimiento y los casos borde.
- Quién aceptó cada requerimiento: el acta da la fecha pero no la persona.
- Un criterio de éxito del producto, que no existe.
- Un proyecto que lo construya: la definición dice «Ninguno declarado».
- Evidencia de demanda: la única es una cita de entrevista de hace 12 meses que no nombra ningún requerimiento, y REQ-4901 y REQ-4912 no tienen ninguna.
- Obligaciones normativas: no hice el barrido, porque ningún documento dice el país, el tipo de tarjeta ni quién la emite.

Cada vacío lleva su dueño en el documento. La autoridad «Comité de producto» viene de la respuesta sugerida del setup, no de un documento.

**Qué no cubre.** Ninguno de los 13 queda cubierto por una sección de comportamiento. El documento lo detalla requerimiento por requerimiento. No ofrezco `/product-charter`, porque los vacíos siguen abiertos.

La corrida quedó registrada como `2026-10-17-product-spec-1`: 15 requerimientos, 47 s y 36 señales abiertas.

Archivos en `/home/claude/banco/ronda-9/retail/espacio/estado-producto/PRD-309/corridas/`:
- `salida-product-spec.md`