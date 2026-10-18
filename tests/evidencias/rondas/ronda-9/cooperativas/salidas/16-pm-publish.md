# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-209 en `documentos/proyectos/PRY-209-convenios-de-libranza-con-empresas/00-gobierno/ficha-pm.json`, con corte al 2026-10-17.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrar nada.
- **Fecha de cierre:** `plan.end_date` es 2027-04-17. Hay un solo cronograma (v1), así que esa fecha es la vigente y coincide con la línea base.
- **Carpeta de gobierno:** ya existía; no creé nada.
- **Contenido de la ficha:** no hay un comando de publicación en el script. Copié tal cual la ficha que `compute` acababa de recalcular en `estado/.../records/PRY-209.json`, sin campos fuera del esquema.
- **Campos:** lleva 13 con dato y 3 sin decir en ninguna parte (`identity.product`, `identity.authority` e `identity.phase`). En `identity.product` el acta dice «No aplica».
- **Estado declarado:** amarillo al 2026-10-09, con 24 % de avance, marcado como declaración.
- **Lo más viejo:** los campos del acta del 2026-06-20, con 119 días. Ninguno pasa de un año.
- **Lo que verá la PMO:** el estado amarillo no cuenta 5 compromisos vencidos ni 3 reprogramados. La corrida registró 12 hallazgos en total: los 5 vencidos, los 3 reprogramados y 4 compromisos sin fecha.
- **Registro de la corrida:** `corridas/2026-10-17-pm-publish-1.md`, con la salida en `salida-pm-publish.md`.