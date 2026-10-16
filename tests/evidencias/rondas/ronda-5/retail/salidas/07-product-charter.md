# /criterio-product:product-charter REQ-4601

Dejé el borrador del acta de REQ-4601 (producto PRD-306, App de clientes). Quedó sin firma y no creé la ficha del proyecto. Faltan tres de los cuatro puntos que el comando exige comprobar antes de redactar. Como nadie podía responder, tomé la respuesta sugerida: seguí y los marqué como vacíos del acta, sin rellenarlos.

Los términos ya estaban vigentes (v0.3.11, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Los cuatro puntos de la verificación:**
- **Aceptado:** el estado es «aceptado» desde 2026-08-21, pero el registro no dice quién lo aceptó.
- **Criterio de aceptación:** el único es «se verifica en producción». No dice qué se mide, con qué umbral ni cuándo, así que cuenta como vacío.
- **Evidencia de demanda:** es una sola entrevista, del 2025-09-29, con la frase «Lo necesito y hoy no lo tengo.» No nombra el requerimiento, sirve de única evidencia a 14 de los 16 y tiene más de 12 meses.
- **Autoridad del gerente:** no está declarada. «Comité de producto» es una inferencia, porque ningún documento dice quién decide.

**Otros vacíos del acta:**
- No se sabe qué es REQ-4601. Su título es solo «Requerimiento REQ-4601» y su necesidad no aparece en ningún documento.
- El producto no tiene criterio de éxito.
- Nadie nombra al patrocinador ni al gerente del proyecto. El acta lo firma el patrocinador, que no está nombrado en ningún documento.
- Falta la revisión normativa: los documentos no dicen el país ni qué datos recoge la app.

**Qué entra y qué no:** solo entra REQ-4601. REQ-4600 queda fuera por estar «propuesto». Los otros 14 requerimientos aceptados quedan fuera porque no se pidieron para esta acta; el acta deja a quien la arme decidir si alguno entra.

**Supuestos:** el supuesto «La demanda se sostiene sin descuento» sigue sin verificar y quedó marcado como riesgo del proyecto sin doliente. Hay otros dos supuestos implícitos, también sin doliente.

**Lo que sigue:** cuando alguien firme el acta, el gerente del proyecto instala `criterio-project` y corre `/pm-setup`. La corrida quedó registrada con id `2026-10-16-product-charter-1`.

Archivos en `/home/claude/banco/ronda-5/retail/espacio/estado-producto/PRD-306/corridas/`:
- salida-product-charter.md