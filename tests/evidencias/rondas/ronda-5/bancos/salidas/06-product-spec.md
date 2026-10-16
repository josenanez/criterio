# /criterio-product:product-spec 

Escribí el borrador de especificación de Cuenta PyME (PRD-303), pero sin la sección de comportamiento. El registro no dice qué debe hacer ninguno de los 12 requerimientos aceptados, y rellenarlo habría sido inventarlo.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no hubo que registrarlos de nuevo.

**Por qué no hay comportamiento**
- Los 17 requerimientos se llaman «Requerimiento REQ-xxxx» y ninguno describe el problema que resuelve.
- El criterio de aceptación de los 12 aceptados es la misma frase, «se verifica en producción», que no se puede medir. Lo marqué como no verificable hoy.
- Ninguno de los 12 queda cubierto en comportamiento. Solo aparecen en el alcance, y la tabla de no cubiertos los lista a todos.

**Vacíos que dejé a la vista, cada uno con su dueño** (la mayoría de Javier Hoyos, gerente de producto):
- **Sin respaldo:** REQ-4305 y REQ-4309 están aceptados sin cita de quien los pidió. REQ-4306 está aceptado sin doliente.
- **Decisión sin responsable:** el acta del comité del 2026-10-15 no nombra a quien decidió y cierra con «Se mantiene el plan».
- **Sin constructor:** ningún documento vincula los 12 a un proyecto.
- **Evidencia vieja:** 10 de los 12 se apoyan en una sola entrevista de hace 12 meses.
- **Supuestos sin verificar:** «El segmento paga por esto» lleva 90 días sin verificarse, y el volumen mensual del caso de negocio no tiene medición contra la cual contrastarlo.
- **Segmento:** el producto se llama Cuenta PyME pero el segmento declarado es «Personas».
- **Criterio de éxito:** el producto no tiene criterio de éxito.
- **Otros equipos:** ningún documento menciona qué necesita de ellos.
- **Normativa:** no hice el barrido normativo ni cito ninguna norma. Lo dejé como vacío para Cumplimiento y Jurídico.

Los 5 requerimientos propuestos quedan fuera del alcance. Llevan entre 124 y 213 días sin decidirse (umbral de 60) y le tocan al Comité de producto.

No ofrezco `/product-charter`, porque los vacíos no están cerrados. Lo útil ahora es `/product-trace` y que cada doliente escriba qué problema es el suyo.

La corrida quedó registrada como `2026-10-16-product-spec-1`: 47 segundos medidos, 17 requerimientos y 36 hallazgos.

Archivos en `estado-producto/PRD-303/corridas/`:
- `salida-product-spec.md`