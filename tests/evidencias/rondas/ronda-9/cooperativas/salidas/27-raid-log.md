# /criterio-portfolio:raid-log portafolio

Armé el registro RAID del portafolio sobre las 13 fichas (PRY-199 a PRY-211) y lo guardé como evidencia de la corrida.

Salió con 15 riesgos, 16 incidencias, 0 supuestos y 0 dependencias, más 1 riesgo no registrado. Ningún ítem tiene doliente y ningún riesgo tiene fecha, así que los 31 aparecen como hallazgo y no relleno ninguno. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

- **Riesgo no registrado:** solo uno, en las notas de PRY-209 del 2026-10-17: "el proveedor podría no llegar con el equipo completo para la siguiente fase". Las otras minutas que leí solo traen tablas de compromisos.
- **Dependencias disfrazadas de riesgo:** las actas dicen "Ninguna declarada", pero 15 riesgos de la lista son dependencias externas: el proveedor del core, el proveedor que no confirma su última entrega y la aprobación del reglamento por el Consejo. Propongo reclasificarlos; no toqué las fichas. Ninguno trae el código del proyecto del que depende, por lo que no pude hacer el cruce de fechas entre proyectos.
- **Para comité del 2026-10-24:**
  - El reglamento del Consejo toca 10 proyectos, entre incidencias y riesgos.
  - El proveedor del core afecta a 3.
  - El proveedor sin fecha de entrega afecta a 6.
  - El hallazgo de seguridad en la revisión de arquitectura está en 4.
- **Lo que no sé:**
  - Las fichas no guardan historial de movimiento, así que no pude evaluar "sin movimiento en dos períodos".
  - No sé si las frases idénticas repetidas en varios proyectos son un mismo hecho o texto copiado entre informes.
  - No releí los informes de avance: trabajé sobre lo que las fichas ya habían extraído.
  - La minuta de PRY-204 del 2026-10-11 no la leí entera.

Puedo proponer doliente para los 31 ítems, sin asignarlo, si me dices quiénes son los gerentes de cada proyecto; las fichas no los traen en el RAID.

Archivos en `/home/claude/banco/ronda-9/cooperativas/espacio/estado/corridas/`:
- `salida-raid-log.md`
- `2026-10-17-raid-log-1.md`

La corrida quedó registrada como `2026-10-17-raid-log-1`, con 69 segundos medidos. Las señales abiertas que reporta (52) vienen del estado general del portafolio, no de este registro.