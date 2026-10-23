# /criterio-portfolio:raid-log portafolio

Hice el registro RAID del portafolio sobre las 13 fichas, sus actas de constitución, los informes de avance y las minutas de comité. Lo que aparece abajo es el resumen. La salida completa, con el registro de los 41 ítems, está en `estado/corridas/salida-raid-log.md`.

Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-23, así que no los registré de nuevo.

## RAID — Portafolio al 2026-10-23
Quedaron 41 ítems: 7 riesgos, 0 supuestos, 21 incidencias y 13 dependencias. Ninguno tiene doliente ni fecha, y uno no estaba registrado formalmente. El movimiento no se puede medir, porque solo hay una corrida.

**Cambios respecto a las fichas**
- **Reclasificación:** 13 ítems que las fichas llamaban riesgo pasan a dependencia, porque dependen de alguien fuera del proyecto.
  - Calendario del core: PRY-203, 207 y 209.
  - Fecha de entrega del proveedor: PRY-200, 202, 204, 205, 206 y 208.
  - Equipo de seguridad: PRY-199, 200, 201 y 209. Este grupo también podría ser un supuesto.
- **Fuera del registro:** un hecho de PRY-210 («se ajustó el plan de pruebas con el área de seguridad») no es riesgo ni incidencia.
- **Dependencias:** las 13 actas dicen «Ninguna declarada», así que esas dependencias salen de informes de avance.

**Necesitan decisión ahora**
- **Calendario del core:** tres proyectos lo dependen de él y en otros tres ya costó historias fuera del sprint. No hay forma de saber quién es la contraparte.
- **PRY-202:** el cronograma v2 mueve el piloto 69 días, pero el cambio CC-01 sigue sin pasar por el comité. El mismo cronograma declara los hitos cerrados al 100 %, y el informe del mismo día dice rojo y 41 %.
- **PRY-205:** el cronograma da la salida a producción por cerrada, pero el informe del 2026-10-21 reporta rojo y 56 %.
- **Hallazgo de seguridad:** aparece en cuatro proyectos (202, 203, 205 y 208). No sé si es el mismo.

**No registrado formalmente:** en las notas de PRY-206 del 2026-10-23 se dijo que el proveedor podría no llegar con el equipo completo a la siguiente fase, y nadie lo anotó como riesgo.

**Lo que no sé:**
- **Dolientes y fechas:** ningún documento dice quién es el doliente de un ítem ni desde cuándo está abierto.
- **Contrapartes repetidas:** no sé si «el core», «el proveedor» y el hallazgo de seguridad son un solo hecho o varios. Las frases se repiten palabra por palabra entre proyectos.
- **Minutas:** PRY-203, 207, 208, 209 y 211 no tienen minuta en la carpeta.
- **Cruce con PRY-201:** no pude cruzar la dependencia del core con ningún proyecto. PRY-201 Core de depósitos está en rojo, con salida el 2026-10-30, pero eso es una hipótesis mía.
- **Supuestos:** no hay ninguno, y no inventé ninguno.

Los identificadores (`202-I3`, etc.) son rótulos míos, porque las fichas no traen id. Probabilidad e impacto no están en ningún ítem y no los inferí.

La corrida quedó registrada como `2026-10-23-raid-log-1`. Los 71 hallazgos que muestra el registro de la corrida vienen de otras señales del portafolio, no de este RAID.

¿Subo a comité los cuatro grupos de decisión, o propongo primero un doliente para cada ítem? Propongo, no asigno.