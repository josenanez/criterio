# /criterio-portfolio:raid-log portafolio

Armé el RAID del portafolio al 2026-10-16: 36 ítems en 13 proyectos, ninguno con doliente ni fecha. Los términos v1.1 ya estaban aceptados a nombre de José Francisco Ñáñez (2026-10-16), así que no hubo que registrarlos de nuevo.

El registro tiene 9 riesgos, 15 incidencias, 12 dependencias y 0 supuestos. Salió de las 13 fichas, los informes de avance, las actas, las minutas y las notas de reunión de PRY-211.

- **Reclasificados:** pasé 9 ítems de riesgo a dependencia, con la prueba rápida del skill ("depende de alguien fuera del proyecto"): seguridad (5 casos), proveedor sin fecha (3) y calendario del core en PRY-203 (1). Es juicio mío, no lo dicen los documentos.
- **Sin dolientes ni valoración:** no relleno doliente, fecha, probabilidad ni impacto. Tampoco puedo medir el tiempo sin movimiento: cada proyecto tiene un solo informe y las fichas no guardan la fecha del último movimiento.
- **No registrado formalmente:** solo uno. En las notas de PRY-211 del 2026-10-16, "el proveedor podría no llegar con el equipo completo para la siguiente fase" (PRY-211-R1), y nadie lo anotó. En las demás minutas busqué lenguaje de riesgo en todo el texto y no encontré nada.
- **Core sin nombrar:** 4 proyectos (PRY-200, 201, 203, 210) dependen del "core" sin nombrar el proyecto, y ninguna de las 12 dependencias trae código ni confirmación de la contraparte. PRY-201, que es el Core de depósitos, aparece dependiendo del core sobre sí mismo. Si "el core" fuera PRY-201, su CC-01 figura aprobado sin acta y su piloto ya se movió; eso es una hipótesis mía.
- **Para decidir ahora:** las dependencias del core, el riesgo de proveedor de PRY-211, y los proveedores sin fecha en PRY-208 y PRY-209.
- **Informes viejos:** los de PRY-203, 206 y 207 superan los 15 días de silencio configurados.

No subí nada a comité ni propuse dolientes. Eso queda a su decisión.

La corrida quedó registrada en `estado/corridas/2026-10-16-raid-log-1.md`. Lo que le mostré, completo, está en `estado/corridas/salida-raid-log.md`.