# /criterio-product:product-spec 

No pude redactar la especificación de PRD-300 (Monitoreo de flota). Cubre 0 de los 11 requerimientos aceptados, porque ninguno dice qué se necesita. Todos tienen el título genérico «Requerimiento REQ-40xx» y el campo de necesidad vacío, y escribir comportamiento sobre eso habría sido inventarlo. El borrador es entonces la lista de lo que falta.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo. El resto de las preguntas no hizo falta contestarlas.

Lo que encontré:
- **Alcance:** los 11 aceptados son candidatos, pero ninguno se puede describir. REQ-4008, REQ-4012 y REQ-4013 siguen como propuestos y quedaron fuera. Los tres llevan más de 60 días sin decisión.
- **Criterios de aceptación:** 7 tienen «se verifica en producción», que no se puede verificar, y 4 no tienen criterio.
- **Evidencia:** REQ-4002 y REQ-4006 no tienen ninguna. Los otros 9 se apoyan en una sola entrevista del 2025-08-18, de hace unos 14 meses. Esa entrevista tampoco nombra ningún requerimiento.
- **Dolientes:** REQ-4000, REQ-4003 y REQ-4011 aparecen «sin asignar».
- **Proyecto:** ningún requerimiento tiene proyecto que lo ejecute. El acta no dice quién decidió la aceptación.
- **Supuesto:** «El ahorro se sostiene sin inversión adicional» lleva 113 días sin verificar y no se puede desmentir como está escrito. Figura declarado el 2026-06-24 dentro de una definición fechada 2025-11-14, y no se sabe cuál de las dos fechas es la correcta.
- **Normativa:** los documentos no dicen el país, los datos que recoge el monitoreo ni dónde se guardan. No cité ninguna norma; las tres obligaciones posibles quedaron como «no tengo la norma a la vista» para la revisión jurídica.
- **Sin respuesta en ningún documento:** criterio de éxito del producto, casos borde y lo que otros equipos tendrían que hacer.

Cada vacío tiene dueño. Casi todos los cierra Beatriz Cuéllar; el Comité de producto confirma los dolientes y las trazas a proyecto.

No ofrecí `/product-charter`: con estos vacíos abiertos no hay base para un acta. Lo primero es que Beatriz Cuéllar escriba la necesidad de cada requerimiento aceptado y se vuelva a correr este comando.

La corrida quedó registrada como `2026-10-15-product-spec-1`: 54 segundos, 14 requerimientos y 37 hallazgos.

Archivos en `/home/claude/banco/ronda-4/mineria/espacio/estado-producto/PRD-300/corridas/`:
- `salida-product-spec.md`