# /criterio-product:product-spec 

El borrador de la especificación de Almacén de repuestos (PRD-306) quedó escrito, pero la sección de comportamiento está vacía a propósito. Ninguno de los 14 requerimientos dice qué pide: el título es solo «Requerimiento 46xx» y la necesidad aparece como `not_found`. Escribir comportamiento habría sido inventarlo.

Los términos ya estaban vigentes (José Francisco Ñáñez, 2026-10-15, versión 0.3.9), así que no los registré de nuevo.

- **Alcance:** entran los 10 aceptados: REQ-4600, 4601, 4602, 4603, 4604, 4605, 4607, 4609, 4610 y 4611. Quedan fuera los 4 propuestos (REQ-4606, 4608, 4612 y 4613), que llevan entre 176 y 195 días sin decisión.
- **Criterios de aceptación:** ninguno es verificable. Seis requerimientos dicen «se verifica en producción», que indica dónde se verifica pero no qué se observa. Cuatro no tienen criterio: REQ-4603, 4605, 4607 y 4611. Hoy el tablero solo mide `volumen_mensual`.
- **Supuestos:** el proveedor cumple el tiempo pactado sigue sin verificar desde hace 205 días. El volumen del caso de negocio (249.273) está 38,5% por encima del medido (153.324), con un umbral de 20%.
- **Vacíos:** son once, cada uno con quién lo cierra. Entre ellos están el doliente de REQ-4601, que figura «sin asignar», y que el acta no dice quién decidió ninguna aceptación. Tampoco hay criterio de éxito del producto, proyecto que construya nada, ni dependencias con otros equipos. No pude hacer el barrido normativo porque ningún documento dice qué datos maneja el producto, y no afirmo que no haya obligaciones.
- **Cobertura:** los 10 aceptados quedan sin cubrir, cada uno con su motivo.

No corresponde `/product-charter` todavía. Lo más corto de cerrar es que los dolientes describan qué pide su requerimiento y reescriban el criterio.

La corrida quedó registrada en `estado-producto/PRD-306/corridas/2026-10-15-product-spec-1.md`. Tardó 38 segundos sobre 14 requerimientos y registró 31 hallazgos.

Archivos:
- `/home/claude/banco/ronda-3/mineria/espacio/estado-producto/PRD-306/corridas/salida-product-spec.md`