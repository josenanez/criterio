# /criterio-product:product-charter REQ-4600

Dejé el borrador del acta de constitución del REQ-4600 (Microseguros, PRD-306), con sus vacíos marcados, pero **no creé la ficha del proyecto**. No hay firma, y la ficha va solo después de ella.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo. Los vacíos que se llevó el borrador, tomando la respuesta sugerida de seguir sin lo que falta y marcarlo:

- **Autoridad:** no está en la definición. «Comité de producto» es solo la propuesta por defecto de la configuración.
- **Criterio de éxito:** el único escrito es «se verifica en producción», sin métrica, umbral ni fecha. El del producto no está en ningún documento.
- **Necesidad:** el requerimiento no tiene necesidad escrita ni título descriptivo.
- **Quién lo aceptó:** el acta del comité (2026-10-05) lo lista como aceptado desde 2026-04-11, pero no dice quién.
- **Evidencia de demanda:** una sola entrevista de 2025-09-25, ya de 12 meses (umbral 12). No nombra el requerimiento ni dice que el cliente sea PyME.
- **Gobierno:** no hay patrocinador, gerente del proyecto ni presupuesto, y la norma y el país aplicables no constan.

**Supuesto de demanda:** el supuesto «la demanda declarada se sostiene sin campaña» (166 días sin verificar) pasa como riesgo del proyecto, sin doliente. El volumen declarado, 140.572, está 28,9 % por encima del medido, 99.900 (umbral 20 %).

**Alcance:** el acta cubre solo REQ-4600. Los otros 13 requerimientos quedan fuera porque no se pidieron aquí. La salida anota qué le falta a cada uno (sin criterio, sin doliente, sin quién lo pidió o solo propuesto).

**Siguiente paso:** cuando haya firma de quien tenga la autoridad, se crea la ficha con `portafolio.py init` y el estado declarado queda vacío. El gerente del proyecto, ya nombrado, instala `criterio-project` y corre `/pm-setup`.

Dejé la corrida registrada como `2026-10-17-product-charter-1`. Lo que te mostré está en `estado-producto/PRD-306/corridas/salida-product-charter.md`.