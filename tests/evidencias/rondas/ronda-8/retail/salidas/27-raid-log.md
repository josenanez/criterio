# /criterio-portfolio:raid-log portafolio

## RAID del portafolio retail al 2026-10-17

Armé el registro RAID de los 13 proyectos (PRY-199 a PRY-211). Salen 14 riesgos, 7 dependencias, 18 incidencias y 0 supuestos. Ninguno de los 39 ítems tiene doliente.

No existe un registro RAID formal en ningún proyecto. Lo que hay son menciones sueltas en los informes de avance, sin probabilidad, impacto, doliente ni fecha de vencimiento.

Los términos estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no hizo falta registrarlos de nuevo. Salieron de las fichas, las actas de constitución, los informes de avance, las minutas de comité y las notas de reunión.

- **Necesitan decisión ahora:**
  - El hallazgo de seguridad en los medios de pago aparece con el mismo texto en seis proyectos (PRY-199, 202, 203, 204, 209 y 211), sin doliente.
  - La prueba de carga de temporada que no alcanzó el umbral aparece en cinco (PRY-200, 201, 202, 206 y 210).
  - PRY-204 y PRY-209 reprogramaron el despliegue por el congelamiento de fin de año y ningún documento da la fecha nueva.
  - PRY-200 y PRY-206 declaran rojo con el plan ya vencido, y ambos tienen un proveedor sin fecha confirmada.
- **Detectado en reuniones y no registrado:** solo uno. En las notas de PRY-200 del 2026-10-17 se dijo que el proveedor podría no llegar con el equipo completo a la siguiente fase, y nadie lo anotó como riesgo. Revisé las otras minutas de comité y no encontré más.
- **Reclasificado:** "El proveedor no ha confirmado la fecha de la última entrega" estaba como riesgo en siete informes. Depende de alguien fuera del proyecto, así que lo pasé a dependencia.
- **Sin fecha:** en 6 de las 18 incidencias falta la fecha de inicio.

No pude evaluar tres cosas:
- **Movimiento y mitigaciones:** ningún ítem trae fecha de último movimiento ni mitigación, así que no puedo decir cuáles llevan dos períodos sin moverse.
- **Dependencias entre proyectos:** las 13 actas dicen "Ninguna declarada" y ningún documento cita el código de otro proyecto, así que no cruzamos fechas entre proyectos.
- **Textos repetidos:** no sé si los textos idénticos entre proyectos son un mismo hecho o texto copiado de una plantilla.

Ofrezco subir a comité (22 de octubre) los cuatro grupos de "Necesitan decisión ahora". También propongo que el gerente de cada proyecto asuma los ítems del suyo, y que la PMO nombre un solo doliente para el hallazgo de pagos si resulta ser común. Son propuestas; no subí ni asigné nada.

La corrida quedó registrada como `2026-10-17-raid-log-1`. La salida completa está en `estado/corridas/salida-raid-log.md`.