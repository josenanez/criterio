# /criterio-portfolio:raid-log portafolio

Terminé el registro RAID del portafolio y dejé la corrida registrada.

Salió de las 13 fichas, los informes de avance, las minutas, las notas de PRY-203 del 15-oct y las solicitudes de cambio. Los términos ya estaban vigentes (v0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Resultado:**
- **Conteo:** 9 riesgos, 12 dependencias, 17 incidencias y 0 supuestos. Ninguna ficha ni documento declara un supuesto, y no inventé ninguno.
- **Sin doliente:** ninguno de los 38 ítems tiene doliente. Tampoco traen fecha, probabilidad ni impacto, y lo dejé como hallazgo en vez de rellenarlo. No apliqué la escala alta/media/baja, porque ningún proyecto define una.
- **Reclasificados:** las fichas traían 21 "riesgos", y 12 de ellos eran dependencias. "Proveedor del core", "aprobación del reglamento por el Consejo" y "el proveedor no ha confirmado la fecha" dependen de alguien fuera del proyecto.
- **No estaban registradas:** hay cuatro incidencias que aparecen en informes de avance y no en la ficha. En PRY-202 son el hallazgo de seguridad y el ajuste del reglamento; en PRY-203, la reprogramación de la salida; en PRY-204, el ajuste del reglamento.
- **Dicho en reunión:** hay un solo ítem, en las notas de PRY-203 del 15-oct: el proveedor podría no llegar con el equipo completo. Lo clasifiqué como dependencia no registrada formalmente. Las demás minutas solo traen compromisos.

**Para decidir ahora (escalan al comité del 22-oct):**
1. El Consejo de Administración pidió ajustar el reglamento antes del piloto (informes de PRY-202, 204, 208 y 211). Otros seis proyectos esperan esa misma aprobación. En total afecta a 9 proyectos.
2. El proveedor del core está declarado como dependencia en PRY-199, 201, 202 y 207, y ninguna ficha dice quién coordina con él.
3. Los tres proyectos en Rojo (201, 207, 209) tienen incidencias abiertas sin responsable.

**Lo que no pude determinar:**
- **Proveedor del core:** no sé si es el de PRY-202. PRY-202 movió su línea base (CC-01, +119 días), pero ninguna dependencia trae el código del proyecto del que depende. Lo dejé como hipótesis para que el gerente la confirme.
- **Sin movimiento en dos períodos:** no lo pude medir, porque hay un solo informe por proyecto.
- **Mitigaciones vencidas:** no hay ninguna registrada.
- **Plazo de PRY-202:** su cronograma v2 fija el fin vigente en 2026-07-06, anterior a hoy, con 76% de avance en Verde. No es un ítem RAID; conviene revisarlo con `/health-check`.

La corrida quedó registrada como `2026-10-15-raid-log-1`, con una nota que dice lo que no supe. Tardó 107 segundos.

Si quieres, preparo la decisión formulada de las dos primeras escaladas y propongo un doliente por ítem. Propongo, no asigno.

Archivos en `/home/claude/banco/ronda-3/cooperativas/espacio/estado/corridas/`:
- `salida-raid-log.md`