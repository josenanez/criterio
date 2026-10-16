# /criterio-product:product-charter REQ-4200

El borrador del acta de REQ-4200 está escrito, con cada dato citado al documento de origen. No está firmado y no creé la ficha del proyecto: eso va después de la firma, y no sé quién firma. Ningún documento nombra a una persona con autoridad sobre PRD-302, solo al Comité de producto.

**Términos.** Ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-16, así que no los registré otra vez.

**Producto.** `REQ-4200` es un requerimiento, no un código de producto. Usé PRD-302 «Autopago en tienda», que es el único configurado.

**Faltan cosas, y las dejé marcadas como vacíos en vez de rellenarlas.** Como nadie podía responder, tomé la respuesta sugerida y seguí. El 2026-10-16 la corrida de definición ya había dicho que la definición no está cerrada y no ofreció este comando; el borrador lo dice en sus vacíos.
- **Criterio de éxito:** el único que hay es «se verifica en producción», que no dice qué se mide ni contra qué umbral. El producto tampoco tiene criterio de éxito en ningún documento.
- **Autoridad:** solo figura el Comité de producto. El acta del comité no dice quién aceptó REQ-4200.
- **Evidencia de demanda:** es una sola frase de un cliente entrevistado el 2026-05-28. La entrevista no nombra el requerimiento ni dice si el cliente es de Pequeños negocios.
- **Supuesto regulatorio:** «La regulación de datos lo permite» dice «verificado» sin citar con qué, y lleva 57 días sin verificarse. Pasa al proyecto como riesgo sin doliente asignado.
- **Sin dato en ningún documento:** patrocinador, gerente del proyecto, presupuesto, hitos y una propuesta de producto escrita (la sección dice solo «Propuesta principal»).

**Alcance.** Solo entra REQ-4200. Los otros 14 quedan fuera: tres siguen propuestos y once están aceptados pero esta acta se pidió solo para REQ-4200.

**Lo que sigue.** Cuando alguien con autoridad firme, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`. Después, con `/pm-publish`, `/product-trace` podrá confirmar la traza.

**Corrida.** Quedó registrada como `2026-10-16-product-charter-1`.

Archivos en `/home/claude/banco/ronda-6/retail/espacio/estado-producto/PRD-302/corridas/`:
- `salida-product-charter.md`