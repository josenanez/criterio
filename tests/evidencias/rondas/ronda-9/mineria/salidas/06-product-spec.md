# /criterio-product:product-spec 

El borrador de especificación de Monitoreo de flota (PRD-300) quedó escrito y la corrida registrada. No dice qué debe hacer ninguno de los 11 requerimientos aceptados, porque el registro no lo trae. Los títulos son genéricos («Requerimiento REQ-40xx») y ninguno tiene la necesidad que resuelve, así que no rellené ese hueco.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-17, versión 1.1), así que no volví a registrarlos.

El borrador cubre los 11 aceptados de los 16 requerimientos. Quedan fuera los 5 propuestos, que llevan entre 95 y 214 días sin decidirse.

- **Criterios de aceptación:** 10 de los 11 dicen solo «se verifica en producción». Eso no pasa la prueba de que dos personas lleguen a la misma respuesta, y no nombra ninguna medida. REQ-4009 no tiene criterio.
- **Evidencia de demanda:** los 8 aceptados que citan evidencia usan la misma frase de la misma entrevista (2025-10-08), que no nombra ningún requerimiento. REQ-4003, 4004 y 4009 no tienen evidencia alguna.
- **Supuesto del proveedor:** se verificó con el documento técnico del propio proveedor. Ningún documento define qué es «el tiempo pactado».

Estos vacíos quedaron abiertos, cada uno con quién lo cierra:
- Qué hace cada requerimiento.
- Los casos borde: no hay ninguno documentado.
- El criterio de éxito del producto.
- Quién decidió la aceptación, que consta vacío en los 11. El acta solo registra a Camilo Beltrán como asistente y una decisión: «Se mantiene el plan», aunque no existe ningún plan.
- Lo que deben hacer otros equipos: ningún requerimiento tiene proyecto que lo ejecute.
- Las obligaciones normativas: el registro no dice qué datos trata el producto, así que no hice el barrido.

No ofrezco `/product-charter` todavía: con estos vacíos el acta heredaría la misma ausencia.

Archivos en `/home/claude/banco/ronda-9/mineria/espacio/estado-producto/PRD-300/corridas/`:
- salida-product-spec.md
- 2026-10-17-product-spec-1.md (la corrida registrada: 52 s, 16 requerimientos, 31 señales abiertas)