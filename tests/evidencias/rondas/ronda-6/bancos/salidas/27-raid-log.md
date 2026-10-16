# /criterio-portfolio:raid-log portafolio

Levanté el RAID del portafolio (13 proyectos, PRY-199 a PRY-211). Ningún ítem tiene doliente ni fecha, y el único riesgo hablado en reunión y no registrado es de PRY-207.

Los términos ya estaban vigentes (v1.1, José Francisco Ñáñez, 2026-10-16), así que no los registré de nuevo. Leí las 13 fichas, los 13 informes de avance, la sección de dependencias de las 13 actas, 15 minutas, las notas de PRY-207 del 2026-10-16 y 4 solicitudes de cambio.

**Cifras tras reclasificar:** 9 riesgos, 9 dependencias, 12 incidencias y 0 supuestos. Las fichas traían 18 riesgos y ninguna dependencia.

- **Reclasificaciones:** pasé de riesgo a dependencia nueve ítems, porque dependen de alguien fuera del proyecto:
  - el calendario de liberaciones del core (PRY-199, 201, 203, 206);
  - la disponibilidad del equipo de seguridad (PRY-200, 202, 206, 210);
  - la fecha de entrega del proveedor (PRY-208).
- **Doliente y fecha:** faltan en los 30 ítems. No los rellené.
- **Para llevar a comité:** las tres dependencias de arriba afectan a varios proyectos a la vez. El core, además, ya se materializó como incidencia en PRY-202, 210 y 211, así que toca a 7 proyectos.
- **No registrado formalmente:** en las notas de PRY-207 del 2026-10-16 se dijo que el proveedor podría no llegar con el equipo completo a la siguiente fase. Es el único hallazgo de reuniones; las otras 14 minutas solo traen tablas de compromisos.

**Lo que no pude saber:**
- **Quién es "el core":** ningún documento lo dice. Si fuera PRY-201, su fecha de cierre no se ha movido, pero es solo una hipótesis mía. Las 13 actas declaran "ninguna" dependencia, así que no hay cruce posible por código de proyecto.
- **Movimiento y mitigaciones vencidas:** no existe un RAID anterior ni mitigaciones con fecha, así que no pude evaluarlos.
- **Reuniones de PRY-201, 210 y 211:** esos tres proyectos no tienen minutas, así que ahí no había dónde buscar riesgos dichos al pasar.
- **Valoración:** no hay escala ni probabilidad o impacto en ningún documento, y no los inventé.

**Siguiente paso:** puedo preparar para comité las tres dependencias con la decisión formulada, o proponer doliente a cada ítem. En el informe va la propuesta de nombres, que son los gerentes de cada proyecto; para el core y el equipo de seguridad no hay un nombre que se desprenda de los documentos.

La corrida quedó registrada como `2026-10-16-raid-log-1` (107 segundos). El texto completo está en `/home/claude/banco/ronda-6/bancos/espacio/estado/corridas/salida-raid-log.md`.