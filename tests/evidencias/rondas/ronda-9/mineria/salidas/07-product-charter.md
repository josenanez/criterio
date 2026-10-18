# /criterio-product:product-charter REQ-4000

Dejé el borrador del acta de REQ-4000 (producto PRD-300, Monitoreo de flota), pero no creé la ficha del proyecto. Falta la firma, y la ficha se crea solo después de ella.

**Términos:** ya estaban vigentes (v1.1), aceptados por José Francisco Ñáñez el 2026-10-17, así que no hubo que registrarlos otra vez.

**REQ-4000 está aceptado, pero el acta tiene vacíos.** En cada pregunta tomé la respuesta sugerida: seguir y marcar el faltante como vacío, sin rellenarlo. Estos son los vacíos:
- **Quién lo aceptó:** el comité del 2026-10-15 solo registra como asistente a Camilo Beltrán, y el campo de quién decidió está vacío.
- **Necesidad y criterio de éxito:** REQ-4000 no dice qué pide. Su único criterio de aceptación, «se verifica en producción», no tiene métrica ni umbral. La definición del producto tampoco declara criterio de éxito.
- **Evidencia de demanda:** es una sola entrevista del 2025-10-08, de un cliente sin nombre que no menciona este requerimiento, y ya pasó el umbral de 12 meses.
- **Gobierno:** la definición no declara la autoridad. Tampoco hay patrocinador, gerente del proyecto, hitos ni presupuesto en ningún documento.
- **Normativa:** no se barrió, porque ningún documento dice qué datos recoge el monitoreo (por ejemplo, ubicación de vehículos o conductores) ni en qué país. Queda para revisión jurídica.

**Supuestos:** el único (el proveedor cumple el tiempo pactado) está verificado desde el 2026-07-13, así que no pasa como riesgo al proyecto.

**Alcance excluido:** el acta cubre solo REQ-4000. Ningún documento dice por qué los otros 15 quedan fuera, y no inventé una razón. Cinco de ellos están propuestos, sin decisión del gerente de producto.

**Lo que sigue:** el Comité de producto firma el acta. Después se crea la ficha, con el estado declarado vacío por diseño. Luego el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada: tardó 37 s y el mismo texto de arriba está guardado como evidencia. El borrador completo está en `/home/claude/banco/ronda-9/mineria/espacio/estado-producto/PRD-300/corridas/salida-product-charter.md`.