# /criterio-product:product-spec 

Escribí el borrador de la especificación de Logística de frío (PRD-303), pero sin ninguna sección de comportamiento. Los 13 requerimientos aceptados no tienen título real ni necesidad en el registro, y redactar comportamiento habría sido inventarlo.

Los términos ya estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28). No hizo falta registrarlos de nuevo.

- **Alcance:** entran los 13 aceptados (REQ-4300 a 4307, 4310 a 4313 y REQ-2028). Quedan fuera REQ-4308 y REQ-4309 porque siguen como propuestos.
- **Criterios de aceptación:** siete requerimientos traen solo «se verifica en producción», que no es verificable ni medible hoy. Seis no traen criterio (REQ-4300, 4301, 4302, 4303, 4306 y 4310).
- **Evidencia de demanda:** REQ-4301, 4312 y 2028 no tienen ninguna. Los otros diez dependen de una entrevista anónima del 2025-10-13 que no nombra ningún requerimiento y ya pasa del umbral de 12 meses.
- **Supuestos:**
  - El del combustible figura como verificado, pero el anexo solo dice «se confirmó» y no trae la medición del piloto.
  - Ese supuesto es del 2026-08-30 y la definición está fechada 2026-05-27, así que alguno de los dos documentos tiene mal la fecha.
  - Las cifras del caso de negocio (70.118 de volumen mensual, retorno a 24 meses) no tienen fuente más allá del propio caso.
- **Vacíos con dueño:**
  - Ningún proyecto construye lo aceptado.
  - No hay criterio de éxito del producto.
  - Quien decidió está vacío en los 13.
  - El acta dice «Se mantiene el plan», pero ese plan no existe en la documentación.
  - No hice el barrido normativo. Por ser distribución farmacéutica, queda abierto a cargo de Ricardo Salas.
- **Cobertura:** la tabla final lista los 13 como sin sección de comportamiento, cada uno con su razón.

No ofrecí `/criterio-product:product-charter` porque los vacíos siguen abiertos y falta el criterio de éxito.

La corrida quedó registrada: 49 s, 15 requerimientos leídos y 35 hallazgos.

Archivos en `/home/claude/r12/logistica/espacio/estado-producto/PRD-303/corridas/`:
- `salida-product-spec.md`