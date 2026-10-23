# /criterio-product:product-spec 

Escribí el borrador de la especificación de PRD-302, pero no pude redactar el comportamiento de ningún requerimiento. Los 13 requerimientos aceptados tienen el título genérico «Requerimiento REQ-42xx» y ninguno dice qué problema resuelve. Describir lo que hace el producto habría sido inventarlo.

Los términos ya estaban vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no hubo que registrarlos de nuevo. No hubo preguntas que responder. El borrador está en `estado-producto/PRD-302/corridas/salida-product-spec.md` y la corrida quedó registrada como `2026-10-23-product-spec-1`.

- **Alcance:** entran los 13 aceptados, solo como lista. Quedan fuera REQ-4207, 4208 y 4214, que siguen propuestos y llevan entre 92 y 208 días sin decisión.
- **Criterios de aceptación:** 10 dicen solo «se verifica en producción», que no se puede verificar ni medir hoy. REQ-4203, 4204 y 4209 no tienen criterio. Lo único que la organización mide de este producto es el volumen mensual.
- **Supuesto «El segmento paga por esto»:** figura como verificado, pero el anexo del 2026-09-04 no trae ningún dato. Remite a un documento del proveedor que no está en la carpeta. Los otros dos supuestos que dejé a la vista:
  - **Entrevista de 2025-10-15:** la sostiene a los 13 aceptados, pero es una sola, de hace 12 meses, y no nombra ningún requerimiento.
  - **Volumen mensual:** el caso de negocio declara 289.875 y el tablero mide 235.072, una brecha de 18,9 % (el umbral es 20 %).
- **Vacíos con dueño:**
  - REQ-4202 y REQ-4213 están aceptados sin ninguna evidencia.
  - La decisión de aceptación no tiene documento propio ni dice quién la tomó.
  - No hay criterio de éxito del producto, ni proyecto o ficha, ni equipos externos nombrados.
  - Los casos borde no se pueden enumerar sin saber qué hace cada requerimiento.
- **Normativa:** ningún documento dice el país, así que no cité ninguna norma. Los cinco temas que toca el producto quedan como «no tengo la norma a la vista». Dueño: Elena Duarte con Jurídico.
- **Requerimientos sin cubrir:** los 13, todos por la misma razón (no tienen necesidad dicha). La tabla da el detalle de cada uno.

No ofrezco `/product-charter` todavía. Antes, cada doliente tiene que escribir su necesidad y su criterio, y luego se vuelve a correr este comando.