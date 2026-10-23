# /criterio-portfolio:raid-log portafolio

Armé el registro RAID del portafolio (13 proyectos) y lo guardé como salida de la corrida. Los 49 ítems registrados llegan sin doliente y sin fecha.

Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez). Cuando el comando preguntaba si escalar o proponer dolientes, tomé la respuesta sugerida: no escalé ni asigné a nadie, queda como oferta.

**Lo que hay hoy:**
- **Conteo:** 23 riesgos, 26 incidencias, 0 supuestos y 0 dependencias.
- **Dolientes y fechas:** ninguno de los 49 ítems tiene doliente ni fecha. Los 23 riesgos tampoco traen probabilidad, impacto ni mitigación.
- **Detectado en reunión y no registrado formalmente (1):** en las notas del 2026-10-22 de PRY-200 se dijo que el proveedor podría no llegar con el equipo completo a la siguiente fase, y nadie lo anotó como riesgo.
- **Reclasificaciones que propongo:**
  - 5 "riesgos" de la forma "el proveedor no ha confirmado la fecha" pasan a dependencias. Son PRY-199, 200, 205, 206 y 210.
  - 2 incidencias de PRY-210 y PRY-211 se dan por resueltas según su propio texto ("se recibió la aprobación de la consulta previa"). No encontré el documento de esa aprobación.
- **Para mirar primero:**
  - El hallazgo de seguridad en espacios confinados, que aparece sin doliente en PRY-206, 207 y 209.
  - La reprogramación del taladro en PRY-208, que coincide en tema con el contrato CT-751. Ahí "Alquiler del taladro" (vencido desde 2026-01-05) sigue pendiente. Esa relación es mía, no está en los documentos.

**Lo que no pude hacer:**
- **Dependencias entre proyectos:** no hay ninguna declarada, así que no hay nada que cruzar.
- **Movimiento de las incidencias:** no traen fecha. Los riesgos son de octubre, así que por fecha ninguno lleva dos períodos sin moverse.
- **Reuniones de PRY-201, 203, 206, 207 y 210:** no existen en la carpeta. De esos cinco no puedo decir que no haya riesgos dichos y no anotados.

La salida está en `estado/corridas/salida-raid-log.md` y la corrida quedó registrada como `2026-10-23-raid-log-1`. No toqué las fichas.