# /criterio-portfolio:raid-log portafolio

Terminé: la corrida quedó registrada y falta solo entregarte el resultado, que está abajo.

## RAID — Portafolio Logística al 2026-10-28

El registro sale de las 13 fichas, las 13 actas de constitución, las minutas de comité de siete proyectos y las notas de PRY-204 del 28 de octubre. No releí los informes de avance: usé lo que las fichas ya habían extraído de ellos.

Tras reclasificar quedan **13 riesgos, 0 supuestos, 17 incidencias y 6 dependencias**, más 1 riesgo dicho en reunión que nadie registró.

- **Doliente y fecha:** los 36 ítems registrados no tienen doliente, fecha, probabilidad ni impacto. No los rellené: lo reporto como hallazgo.
- **Movimiento:** no se puede evaluar cuáles llevan dos períodos sin moverse, porque es la primera ficha de cada proyecto y no hay RAID anterior.
- **Supuestos y dependencias:** no hay ninguno registrado. Las 13 actas dicen «Ninguna declarada», así que no pude cruzar dependencias entre proyectos.

**Necesitan decisión ahora**
- **Hallazgo de seguridad en montacargas** (PRY-199 y PRY-206): sin doliente ni fecha. No cumple un criterio formal de escalamiento; sube por su naturaleza y la decisión es tuya.
- **Riesgo no registrado en PRY-204:** en las notas del 28 de octubre se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase. El proyecto es de 18.000 M COP, está declarado en verde, y su patrocinador y su gerente son la misma persona.
- **Paro de transportadores:** aparece en cinco proyectos, así que cumple «afecta a otro proyecto».
- **Retraso de las estanterías:** aparece en cuatro proyectos y también cumple ese criterio.
- **Proveedor sin confirmar fecha:** aparece en seis proyectos. Lo reclasifiqué de riesgo a dependencia declarada, pero no acordada.

**Dudas del registro**
- **Textos repetidos:** el mismo texto aparece en proyectos que no se parecen, por ejemplo estanterías en un proyecto de ruteo y montacargas en uno de pintura. No pude verificar si es un solo hecho o texto de plantilla. Si es plantilla, esas filas bajan de «decisión ahora» a «verificar».
- **PRY-209:** «Se ajustó el plan de arranque» parece un cambio de plan y no una incidencia. Lo dejé como incidencia dudosa.
- **Fuera del RAID:** PRY-207, 210, 202 y 211 tienen la fecha de fin del plan vencida y avance declarado menor al 100 %, sin incidencia registrada. Corresponde a `/health-check` y `/baseline-variance`.

**Límites:** busqué riesgos en reuniones, y solo apareció el de PRY-204. PRY-203 y PRY-207 a 211 no tienen minutas, así que ahí no se pudo buscar.

**Para tu decisión:** ¿subo a comité las filas de «Necesitan decisión ahora», con la decisión formulada para cada una? ¿Propongo un doliente por ítem? Solo propongo: el gerente de cada proyecto como candidato, para que confirme. El próximo comité es el 2026-10-31.

La corrida quedó en `estado/corridas/2026-10-28-raid-log-1.md` (161 s, 13 proyectos). El registro completo, ítem por ítem, está en `estado/corridas/salida-raid-log.md`. La medición no incluye el conteo de documentos, que sale como no medido. Los términos ya estaban vigentes (v1.3, José Francisco Ñáñez, 2026-10-28), así que no hubo que volver a aceptarlos. Esto es un borrador de un agente: la verificación contra las citas es tuya.