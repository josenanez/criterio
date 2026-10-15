# /criterio-portfolio:raid-log portafolio

Terminé el registro RAID del portafolio y la corrida quedó registrada (`2026-10-15-raid-log-1`, 71 segundos, 13 proyectos). Salió de las 13 fichas, los informes de avance, las actas de constitución, las minutas de comité y las notas de PRY-203 del 2026-10-15. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

**Cifras:** 21 riesgos, 22 incidencias, 0 supuestos y 0 dependencias.
- Los 43 ítems no tienen doliente ni fecha. Lo reporto como hallazgo y no lo relleno.
- 42 de los 43 no traen fecha de último movimiento. Por eso no puedo medir "sin movimiento en dos períodos".
- Ninguno trae probabilidad ni impacto. La organización no define escala; usaría alta, media y baja, pero no inventé valores.

**Detectado en reuniones y no registrado:** solo uno.
- En las notas de PRY-203 del 2026-10-15 se comentó que "el proveedor podría no llegar con el equipo completo para la siguiente fase", y nadie lo anotó como riesgo. Queda marcado como no registrado formalmente, para que el gerente decida si lo formaliza.
- PRY-200, 204, 207 y 208 no tienen minutas en la carpeta. No sé qué se habló en esos proyectos.

**Necesitan decisión ahora:** ningún ítem cumple de forma demostrable un criterio formal de escalamiento. Subo dos por juicio, y los decide la PMO:
- **PRY-203:** el riesgo del proveedor, más "el proveedor no ha confirmado la fecha de la última entrega". El proyecto declara rojo, y el entregable "Licenciamiento del software" de CT-683 venció el 2026-03-19 sin evidencia de recibo.
- **Textos repetidos en varios proyectos:** licencia ambiental (6 proyectos), bloqueo de la vía de acceso (4) y parada de planta (riesgos en 4, incidencias en 6). Si es un mismo hecho, afecta a otros proyectos y cumple el criterio de escalamiento. Si cada informe copió la frase, es ruido. Los documentos no permiten distinguirlo.

**Reclasificaciones propuestas:**
- "El proveedor no ha confirmado la fecha de la última entrega" está como riesgo en PRY-200, 201, 203 y 208, pero depende de un tercero, así que es una dependencia.
- "Ventana de parada de planta definida por operaciones" (PRY-203, 206, 207 y 210) también es una dependencia.
- En ninguno de los dos casos hay un proyecto del portafolio al que atarla.
- "El proveedor entregó los equipos, pendientes de aceptación" (PRY-201) está como incidencia. No sé si lo es; queda para que el gerente lo confirme.

**Dependencias:** las 13 actas dicen "Ninguna declarada", así que no hubo cruce de fechas entre proyectos. Eso no equivale a que no existan, porque al menos ocho ítems de riesgo se leen como dependencias.

**Pendiente tuyo:** subir a comité los dos puntos de arriba y proponer doliente para los 43 sin él. Puedo hacer cualquiera de las dos cosas; proponer, no asignar.

El registro completo de los 43 ítems, con el pie de rigor, está en `/home/claude/banco/ronda-3/mineria/espacio/estado/corridas/salida-raid-log.md`.