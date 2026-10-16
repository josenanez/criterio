# /criterio-product:product-trace 

## Trazabilidad — App de clientes (PRD-306) · al 2026-10-16

15 requerimientos decididos. Ninguno tiene proyecto, ninguno está confirmado contra una ficha y ninguno está entregado.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez para la versión 0.3.11), así que no volví a registrarlos. Como nadie podía responder, usé `estado/records` como carpeta de fichas. Es la única con fichas de proyectos en este espacio.

### Decidido y nadie lo está construyendo
- **Qué dice el acta:** en el comité del 2026-10-16 los 15 requerimientos aceptados tienen «Proyecto que lo ejecuta: —». La decisión del acta es «Se mantiene el plan», y no nombra ningún proyecto. El único asistente es Felipe Arango.
- **Los más antiguos:**
  - REQ-4605 (Paula Céspedes), desde 2026-03-26.
  - REQ-4602 (Jorge Medina), desde 2026-04-20.
  - REQ-4611 (Liliana Torres), desde 2026-05-18.
- **Los más recientes:** REQ-2028 (2026-09-19) y REQ-2036 (2026-10-04).
- **Sin doliente:** REQ-4607 aparece como «sin asignar».
- **No cuenta como decidido:** REQ-4600 sigue «propuesto», con 120 días sin decidir.

La tabla completa con los 15 está en el archivo de salida.

### La traza no se confirma
Ninguna. Como ningún requerimiento declara un proyecto, no hay traza que confirmar ni desmentir.

### Lo que un proyecto construye y el registro no tiene
Ninguna ficha dice ejecutar PRD-306, pero tampoco se puede descartar que alguno lo haga. Las 13 fichas leídas se reparten así:
- **PRY-199:** declara PRD-299, que es otro producto.
- **PRY-200, 201, 204, 205, 207 y 208:** el campo de producto es texto libre («venta en línea», «puntos de fidelización», «pago con QR», etc.), no un código.
- **PRY-202, 203, 206, 209, 210 y 211:** el campo de producto está vacío. Es un hallazgo del lado de esas fichas, y alguno de esos proyectos podría estar construyendo la app.

### La cadena completa
La cadena se rompe en el segundo eslabón: no hay cita de decisión a proyecto en ninguno de los casos. El detalle por requerimiento está en el archivo de salida.

### Después
- **Para `/product-charter`:** REQ-4602, 4605, 4606, 4610, 4611 y 4612 tienen doliente, criterio de aceptación y evidencia. REQ-2036 también tiene los tres, pero su evidencia es del 2025-09-29.
- **Fichas con producto vacío:** es una conversación con sus gerentes de proyecto, no un comando.

La corrida quedó registrada como `2026-10-16-product-trace-1`: 39 hallazgos, 44 segundos. La salida completa está en `estado-producto/PRD-306/corridas/salida-product-trace.md`.