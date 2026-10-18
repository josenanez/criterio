# /criterio-portfolio:portfolio-scan 

El barrido terminó: leí 41 de los 67 documentos y escribí y sellé diez fichas. La corrida quedó registrada como `2026-10-17-portfolio-scan-1`, con 229 segundos medidos por el script.

- **Términos:** ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-17), así que no registré otra aceptación.
- **Lectura:** los 67 archivos se pudieron leer, sin ilegibles. Las fichas son de PRY-200, 201, 203, 204, 205, 206, 207, 208, 210 y 211. PRY-199, PRY-202 y PRY-209 no cambiaron y no se releyeron.
- **Sin dato:** `authority` y `phase` faltan en las diez fichas. `product` falta en PRY-205, 208 y 210, porque sus actas dicen «No aplica».

**Lo que más pide atención** (el detalle completo está en la salida que guardé):
- **PRY-208:** declara verde con 31% de avance, pero su cronograma marca los cinco hitos como cerrados, incluida la salida a producción, y ninguno tiene acta. La factura FV-1314 es de 909.461.374 COP y no hay ningún acta de recibo del contrato CT-314. También tiene un compromiso vencido (Ricardo Salas, punto 32, para el 2026-10-15).
- **PRY-204:** la solicitud de cambio CC-01 dice «autorizada por el comité», sin nombrar cuál ni citar el acta. Con ella registré una segunda línea base: el piloto pasa al 2027-01-23.
- **PRY-201:** la factura FV-1894 es de 561.870.991 COP, y solo dos de los tres entregables del contrato CT-894 tienen acta de recibo (222.267.112 COP cada uno). El script marca la factura como mayor que lo aceptado.
- **PRY-203, 205 y 206:** las fechas de cierre de sus actas ya pasaron y siguen declarando verde o amarillo.
- **PRY-210:** tiene un compromiso sin fecha (María Restrepo, punto 28, «por definir»).

**Pendientes que dejé sin resolver:**
- `2026-10-17-notas-reunion.txt` está suelto en la raíz de PRY-209. No lo leí ni lo moví, porque el plan no lo incluía. Alguien tiene que decir en qué carpeta va.
- La ficha de PRY-209 tiene 15 citas que no resuelven. Los archivos están en disco; la ficha cita rutas sin el prefijo de la carpeta del proyecto. No la reescribí, porque sus documentos no cambiaron.
- No existe una carpeta `entrada/`, así que no moví nada.

**Dos advertencias:**
- En la salida señalé a PRY-205 y PRY-206 como proyectos con cierre vencido, pero el script no emitió ninguna señal para ellos, ni para PRY-207. Es una observación mía sobre las fechas del acta, no una alerta calculada.
- El registro de la corrida cuenta 52 hallazgos, pero los 12 de PRY-209 salen de su ficha anterior, que este barrido no tocó.

El siguiente paso es `/criterio-portfolio:portfolio-report`. Ahí se calculan las desviaciones de costo y tiempo y las señales de proveedores.

Todo quedó en `estado/`: las fichas en `records/`, la salida en `corridas/salida-portfolio-scan.md` y el snapshot en `snapshots/2026-10-17.json`.

Versión 0.4.0. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.4.0