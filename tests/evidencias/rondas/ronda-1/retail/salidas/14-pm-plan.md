# /criterio-project:pm-plan 

Terminé el borrador del plan de PRY-211. No comprometí ninguna fecha, y la corrida quedó registrada.

El proyecto no es un caso de acta recién firmada. Arrancó el 2026-02-19 y ya tiene un `cronograma-v1.csv` con cuatro hitos, dos de ellos cerrados. Por eso el borrador contrasta la WBS con ese cronograma y no toca la línea base. Los términos (versión 1.0, 2026-10-14) ya constaban en la configuración, así que no pedí aceptación otra vez.

**Lo que le falta al acta:**
- El alcance dice solo «Componente 1, 2, 3» y el fuera de alcance dice «Lo que otro proyecto cubre». Los tres componentes quedan sin definir en la WBS.
- «Medido» en el criterio de éxito no tiene métrica ni línea de comparación.
- La autoridad del gerente no está declarada y el acta no dice quién acepta cada entregable. Las dos actas de recibo dicen «Recibido por: Camilo Beltrán», o sea el propio gerente.
- Las dependencias dicen «Ninguna declarada», pero el cronograma tiene un hito «Integración con el ERP». No sé si hay una dependencia.

**WBS (10 nodos):**
- Los 4 hitos del cronograma están marcados como supuesto: el acta no los nombra.
- Los componentes 1 a 3 y el cierre del hallazgo de seguridad de medios de pago están sin definir.
- Producción y medición salen del criterio de éxito. Ninguno tiene hito, ni aceptante.
- Todas las duraciones están vacías, con 6 preguntas para llevar al equipo.

**Orden:** solo sostengo que medir va después de producción. Que el ERP precede al piloto y el piloto a producción lo dejé como supuesto. El último hito es el piloto (2027-03-16) y el cierre del acta es 2027-05-04. Entre los dos no hay hito para «en producción y medido».

**Supuestos:** el más importante es que el proveedor llegue con el equipo completo. Se dijo en la reunión del 2026-10-14 y nadie lo registró como riesgo.

**Análogos:** ninguno a la vista, porque la configuración no apunta a fichas de la PMO. Como referencia del propio proyecto, el diseño se recibió 138 días después de su línea base y el ambiente de pruebas 33 días después. El cronograma no muestra replanificación.

**Para comprometer una fecha falta:** disponibilidad real del equipo, fecha y equipo del proveedor, ventana del piloto en tiendas, fecha del dueño del ERP y el ajuste de presupuesto de Laura Vélez, que no tiene fecha.

Dejé aparte una observación para `/pm-report`: el informe declara «Verde» con un ejecutado de 8,2 mil millones COP por encima de lo comprometido (6,1 mil millones). La proyección al cierre pasa de los 18.000 millones aprobados.

El primer intento de marcar el arranque falló por una ruta relativa. Lo repetí con ruta absoluta y la corrida midió 56 segundos.

Archivos en `/home/claude/banco/ronda-1/retail/espacio/estado/PRY-211-pronóstico-de-demanda/corridas/`:
- `salida-pm-plan.md`
- `2026-10-14-pm-plan-1.md`