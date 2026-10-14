# /criterio-portfolio:raid-log portafolio

Terminé el RAID del portafolio al 2026-10-14. Sale de las 13 fichas, sus informes de avance y las minutas y notas de reunión. Nadie respondió preguntas en esta sesión: los términos v1.0 ya estaban aceptados en la configuración y no hubo ninguna otra decisión que tomar.

**Cifras**
- Las fichas traen 35 ítems: 11 riesgos, 11 incidencias y 13 dependencias. No hay supuestos.
- Las 13 dependencias estaban registradas como riesgos. Las reclasifiqué porque dependen de alguien fuera del proyecto: el calendario de liberaciones del core (4 proyectos), la fecha de entrega del proveedor (3) y la disponibilidad del equipo de seguridad (6).
- Los 35 están sin doliente y sin fecha, y ninguno tiene probabilidad ni impacto. Lo reporto como hallazgo y no lo rellené.

**Necesitan decisión ahora**
- **Calendario del core:** afecta a PRY-202, 204, 205 y 211. Ningún documento dice de qué proyecto o equipo depende. PRY-201 (Core de depósitos) es candidato por el nombre, pero no lo asumí.
- **Proveedor de PRY-202:** en las notas del 2026-10-13 se dijo que podría no llegar con el equipo completo, y nadie lo anotó como riesgo. Es el único riesgo de reunión que encontré. PRY-202 está en rojo y la revisión con el proveedor es el 2026-10-24.
- **Hallazgo de seguridad:** incidencia sin doliente en PRY-201, 205 y 207. PRY-201 y 207 se declaran en verde con ella abierta.
- **Prueba de carga:** incidencia sin doliente en PRY-201, 202, 206 y 210, sin fecha de la nueva prueba.

**Lo que no pude evaluar**
- Los ítems sin movimiento en dos períodos y las mitigaciones vencidas: solo hay un corte (2026-10-14) y ningún ítem trae mitigación.
- Supuestos: ningún documento declara uno y no inventé ninguno.
- Los ids son provisionales (`código-n`), porque las fichas no traen id de ítem RAID.

No subí nada a comité ni propuse dolientes. Puedo hacerlo para el comité del 2026-10-20 si me lo pides.

La corrida quedó registrada como `2026-10-14-raid-log-1`. El registro completo, con la tabla de los 35 ítems, está en `/home/claude/banco/ronda-1/bancos/espacio/estado/corridas/salida-raid-log.md`.