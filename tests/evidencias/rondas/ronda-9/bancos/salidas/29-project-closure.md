# /criterio-portfolio:project-closure PRY-207

PRY-207 (Onboarding PyME) no se puede cerrar contra su criterio de éxito. Ningún documento declara que terminó, y el último informe lo reporta en rojo con 76 % de avance.

Salí de la ficha y de cuatro documentos: el acta de constitución, el cronograma v1, el acta de recibo del piloto (2026-10-04) y el informe de avance (2026-10-06). Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo.

- **Criterio de éxito:** el acta dice "Onboarding PyME en producción y medido". Ningún documento menciona producción ni medición. El último hito del cronograma es un piloto con usuarios internos, que no equivale a producción.
- **Hitos:** el cronograma marca los cuatro como cerrados. Los tres primeros no tienen acta de recibo; el script los señala con 349, 249 y 149 días sin sustento. El piloto sí tiene acta, pero se recibió el 2026-10-04 y su fecha de línea base era 2026-08-29, sin replanificación registrada. No calculé esos días de diferencia porque el script no los da.
- **Presupuesto:** la proyección al cierre es 21.962.012.879 COP contra 18.000.000.000 aprobados, un sobrecosto de 22,0 %. Hay 0 replanificaciones y 0 solicitudes de cambio, así que no hay aprobación documentada. Lo ejecutado es 5.521.092.051 COP (30,7 %) y lo comprometido 14.120.349.319 COP (78,4 %).
- **Alcance:** dos historias quedaron fuera del sprint por dependencia con el core. No hay decisión registrada de quién las sacó ni cuándo.
- **RAID abierto:** dos riesgos (equipo de seguridad y calendario de liberaciones del core) y esa incidencia. Ninguno tiene doliente con nombre, así que no están cerrados.
- **Lecciones:** no entra ninguna, porque los documentos no sustentan un hecho con fecha y efecto. Los hallazgos de gobierno quedaron en el acta, sin convertirse en lección.
- **Archivo:** no moví la carpeta a `archivo/` ni congelé la ficha. Archivarlo sacaría del barrido diario un proyecto con tres señales abiertas: avance contra plan, hitos sin evidencia y sobrecosto.

Antes de cerrar, alguien con autoridad tiene que declarar el cierre, y el Comité de Arquitectura tiene que decidir sobre el alcance recortado y el sobrecosto.

La corrida quedó registrada como `2026-10-17-project-closure-1`. El acta de cierre completa está en `estado/corridas/salida-project-closure.md`, bajo `/home/claude/banco/ronda-9/bancos/espacio/`.