# /criterio-product:product-spec 

Escribí el borrador de especificación de PRD-300, pero no tiene secciones de comportamiento: no cubre ninguno de los 4 requerimientos aceptados (REQ-1000, REQ-1001, REQ-1002 y REQ-2017).

Escribirlas habría obligado a inventar la necesidad de cada requerimiento. Ningún documento la dice, y los títulos son genéricos («Requerimiento REQ-xxxx»). Los cuatro traen el mismo criterio de aceptación, «se verifica en producción», que dice dónde se verifica, no qué se mide. Por eso los marqué como no verificables hoy y no redacté un criterio propio.

Los vacíos quedaron en una tabla, cada uno con quién lo cerraría:
- **Necesidad y criterio medible:** los cuatro dolientes (Andrés Lozano, Javier Hoyos, Mauricio Pérez y Natalia Ospina), cada uno en su requerimiento.
- **Quién aceptó los requerimientos y quién tiene la facultad de decidir:** el acta del 2026-10-11 solo dice «Se mantiene el plan», y `authority` está en `null`.
- **Supuesto de ahorro sin inversión adicional:** lleva 131 días sin verificar (el umbral es 30).
- **Volumen del caso de negocio:** declara 164.808 al mes y el tablero mide 102.629, un 37,7% menos. Beatriz Cuéllar, gerente de producto, aparece como propuesta para cerrar estos dos, porque nada lo asigna.
- **Evidencia:** REQ-1000, REQ-1001 y REQ-1002 se apoyan en una sola cita genérica de hace 12 meses. REQ-2017 no tiene ninguna.

No sé qué datos maneja el producto, así que dejé el barrido normativo como pregunta abierta y no lo hice. Tampoco consta si hay dependencias de otros equipos.

No ofrezco `/product-charter` porque los vacíos siguen abiertos. Conviene correr antes `/product-trace`, porque los cuatro están aceptados y sin proyecto.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo. La corrida quedó registrada como `2026-10-15-product-spec-1`.

Archivos en `/home/claude/banco/ronda-2/mineria/espacio/estado-producto/PRD-300/corridas/`:
- salida-product-spec.md