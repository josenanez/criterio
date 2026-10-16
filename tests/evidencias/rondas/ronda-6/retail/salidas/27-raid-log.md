# /criterio-portfolio:raid-log portafolio

## RAID — portafolio (13 proyectos, PRY-199 a PRY-211) al 2026-10-16

El registro sale de las fichas del portafolio y de las actas, las minutas y las notas de reunión. Los códigos de ítem (p. ej. PRY-206-R2) los puse yo para poder citar, porque las fichas no traen ids.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los volví a registrar.

**Cifras:** 12 riesgos, 6 supuestos, 15 incidencias y 3 dependencias, 36 ítems en total. Los 36 están sin doliente y sin fecha de revisión o resolución. Hay 1 no registrado formalmente. No pude medir cuántos llevan tiempo sin movimiento, porque ninguna ficha guarda esa fecha.

Estos conteos son después de reclasificar 9 ítems. Tal como venían en los informes había 20 riesgos registrados, 15 incidencias, 0 supuestos y 0 dependencias.

### Necesitan decisión ahora
| Id | Qué | Doliente | Por qué sube |
|---|---|---|---|
| PRY-199-I1, PRY-206-I1, PRY-207-I1, PRY-210-I1 | Hallazgo de seguridad en los medios de pago, con casi la misma frase en cuatro proyectos | Ninguno | Afecta a varios proyectos. Hay que nombrar un doliente y confirmar si es un solo hallazgo o cuatro; con los documentos no puedo saberlo. |
| PRY-202-I1, PRY-203-I1, PRY-204-I1, PRY-211-I1 | Despliegue reprogramado por el congelamiento de fin de año | Ninguno | En 203, 204 y 211 el cronograma sigue en v1 con la misma fecha; en 202 el informe no da la nueva fecha. Hay que abrir solicitud de cambio o decir que no se mueve. |
| PRY-200-I1, PRY-203-I2, PRY-208-I1 | El equipo perdió dos semanas por rotación de un desarrollador clave | Ninguno | Si es la misma persona o el mismo equipo, afecta a tres proyectos. Hay que confirmarlo. |
| PRY-201-I1, PRY-205-I1 | La prueba de carga de temporada no alcanzó el umbral y se repite | Ninguno | Ninguno de los dos informes da la fecha de la nueva prueba. |
| PRY-206-R2 | El proveedor podría no llegar con el equipo completo para la siguiente fase | Ninguno | Se dijo en reunión y no está en el informe. |

### Detectados en reuniones, no registrados
Hay uno: el riesgo de PRY-206 de arriba. Sale de las notas del 2026-10-16 (`PRY-206-precios-dinámicos/2026-10-16-notas-reunion.txt`, línea 7), que dicen «nadie lo anotó como riesgo». No encontré otro y no inventé ninguno. Los proyectos 202, 203, 208, 210 y 211 no tienen carpeta de reuniones, así que de ellos no hay nada que revisar.

### Sin doliente o sin fecha
- **Doliente:** ninguno de los 36 ítems lo tiene.
- **Riesgos, supuestos y dependencias (21):** ninguno trae probabilidad ni fecha de revisión. Solo los 6 riesgos de «regulación de datos personales» traen impacto («alcance»).
- **Incidencias (15):** traen «desde», pero ninguna trae fecha esperada de resolución.

Lo reporto como hallazgo y no rellené nada.

### Dependencias
Ninguna de las 13 actas declara una dependencia de otro proyecto («Ninguna declarada»). Por eso el cruce entre proyectos no tiene nada que cruzar, y eso es en sí un hallazgo.

Lo que sí hay son tres dependencias de un proveedor, que estaban escritas como riesgo. Ninguna está confirmada:
- **PRY-201-D1, PRY-209-D1 y PRY-211-D1:** el proveedor no ha confirmado la fecha de la última entrega.
- **PRY-209:** además, su solicitud de cambio CC-01 (+70 días) figura aprobada «por el comité» sin nombrar cuál ni la fecha.

Una pregunta, no un ítem: PRY-199 y PRY-207 tienen un hito «Integración con el ERP», y PRY-209 es la migración del ERP, que movió su fecha. Ninguna acta dice que dependan de PRY-209. Alguien debería confirmar si hay dependencia.

### Reclasificados y duplicados
- **Riesgo a dependencia (3):** el «proveedor no ha confirmado la fecha» en PRY-201, 209 y 211. Depende de un tercero y ya es un hecho, no una posibilidad.
- **Riesgo a supuesto (6):** «Disponibilidad de los jefes de tienda para el piloto» en PRY-199, 201, 202, 203, 208 y 211. Se está dando por cierta una disponibilidad que nadie verificó. Si el gerente prefiere mantenerlo como riesgo, es su decisión.
- **Riesgos que ya ocurrieron (no cambié el tipo, los marco):**
  - PRY-204-R1 (congelamiento de cambios) tiene su incidencia en PRY-204-I1.
  - PRY-200-R2 y PRY-203-R1 (concentración del conocimiento) conviven con la incidencia de rotación del desarrollador clave.

El registro completo de los 36 ítems está en `estado/corridas/salida-raid-log.md`.

### Después
Puedo subir a comité los cinco puntos de «Necesitan decisión ahora». También puedo proponer doliente para los ítems que no lo tienen; propongo, no asigno. Dime cuál y lo preparo.

### Pie de rigor
- **Lo que no sé:**
  - Si los hallazgos y las pérdidas de equipo con la misma frase son un mismo hecho o hechos distintos.
  - Quién es doliente de cada ítem.
  - Cuánto lleva cada ítem sin movimiento, así que el criterio «más de dos períodos sin movimiento» no se puede aplicar.
  - La escala de probabilidad e impacto de la organización: no está definida y no inventé una.
- **Lo que no revisé a fondo:** busqué riesgos dichos al pasar por palabras clave en las minutas y en el texto extraído. No leí línea por línea los comités de PRY-204, 205 y 206, así que un riesgo dicho con otras palabras podría no haber salido.
- **Mi lectura:** lo que clasifiqué como supuesto o dependencia es mi lectura del texto del informe, no algo que el gerente haya declarado así. Los informes de avance son declaración del gerente y no los contrasté aquí contra otra evidencia.
- Es un borrador de trabajo; la verificación es tuya.

La corrida quedó registrada como `2026-10-16-raid-log-1`, con una duración de 109 segundos. Dejé el texto entero de esta salida en `estado/corridas/salida-raid-log.md`.