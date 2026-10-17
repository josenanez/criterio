# /criterio-product:product-charter REQ-4600

Dejé el borrador del acta de REQ-4600 con sus vacíos marcados, pero no creé la ficha del proyecto porque el acta no está firmada. No corrí `portafolio.py init` y el campo `declared` queda sin escribir.

Los términos ya estaban vigentes: José Francisco Ñáñez los aceptó el 2026-10-17 (v1.1), así que no los registré otra vez. Como nadie respondía preguntas, a cada falta le apliqué la respuesta sugerida: seguir y marcarla como vacío, sin rellenarla.

REQ-4600 está aceptado, pero incumple tres de las cuatro condiciones para tener con qué:
- **Criterio de aceptación:** el único es «se verifica en producción». No dice qué se mide, con qué umbral ni quién lo verifica, así que no es verificable.
- **Evidencia de demanda:** el requerimiento no trae ninguna y el acta de comité no dice el problema. La única evidencia del producto es una entrevista del 2025-09-27, de una sola voz y 385 días de antigüedad.
- **Autoridad:** «Comité de producto» es la propuesta por defecto de la instalación. Ningún documento la declara, y el acta de comité del 2026-10-15 lista como único asistente a Gustavo Neira.

En el borrador también quedan como vacíos el patrocinador, el presupuesto, los hitos y la propuesta (la definición solo dice «Propuesta principal»). El acta de comité tampoco dice quién decidió aceptar REQ-4600.

El supuesto «el reglamento vigente lo permite» pasa al proyecto como riesgo sin doliente: lleva 154 días sin verificar. No consta ni el país ni la norma, y eso queda para revisión jurídica.

En la tabla «No entra» no listé razones por requerimiento. No leí los otros requerimientos (REQ-2030 y REQ-4601 a REQ-4615), porque el acta cubre solo REQ-4600 y no quise inventar motivos.

Lo que sigue es cerrar esos vacíos, empezando por criterio de éxito, autoridad y problema. Después de la firma se crea la ficha, y el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-17-product-charter-1`: 29 segundos y 43 señales abiertas en el producto, la mayoría de requerimientos sin trazar (16) y con evidencia envejecida (11).

Archivos en `estado-producto/PRD-306/corridas/`:
- `salida-product-charter.md`