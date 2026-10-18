# /criterio-product:product-charter REQ-4900

El borrador del acta de REQ-4900 está listo, pero tiene vacíos y no se debe firmar tal cual. No creé la ficha del proyecto ni escribí el estado declarado, porque el acta no está firmada.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

Lo que dice el acta y lo que le falta:
- **Qué es REQ-4900:** el acta del comité del 2026-10-11 lo titula solo «Requerimiento REQ-4900». No hay descripción, y el problema que cito es el del producto: «el segmento Hogares no tiene tarjeta de la tienda».
- **Criterio de éxito:** el único que existe es «se verifica en producción», sin qué se mide, con qué umbral ni quién lo certifica. El producto tampoco tiene criterio de éxito ni cifra de retorno.
- **Evidencia de demanda:** la única cita es una entrevista del 2025-10-12 («Lo necesito y hoy no lo tengo»). No nombra el requerimiento y supera en 5 días el umbral de 12 meses.
- **Gobierno:** ningún documento nombra patrocinador, gerente del proyecto, autoridad ni quién aceptó el requerimiento. «Comité de producto» como autoridad sale de la respuesta sugerida de `product-setup`, no de un documento.
- **Supuestos que pasan al proyecto:** «El cliente paga por la entrega rápida» lleva 31 días sin verificar (umbral: 30). Sin doliente asignado.
- **Cifra del negocio:** `volumen_mensual` declarado 278.242 contra 214.637 medido, una brecha de 22,9 % sobre el umbral de 20 %.
- **Normativa:** una tarjeta de la tienda probablemente toca crédito al consumidor y datos personales, pero ningún documento cita una norma. Lo dejé abierto en vez de citar de memoria.
- **No entra:** los demás requerimientos (REQ-4901 a REQ-4913 y REQ-2035). REQ-4905 y REQ-4908 están solo propuestos.

Según la corrida registrada, el siguiente paso es nombrar a quien firma y cerrar los vacíos, empezando por la descripción de REQ-4900, el criterio verificable y la autoridad. Después, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

Archivos en `estado-producto/PRD-309/corridas/`:
- `salida-product-charter.md`
- `2026-10-17-product-charter-1.md`