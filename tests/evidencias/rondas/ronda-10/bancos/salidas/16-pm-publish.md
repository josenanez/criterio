# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-201 en `documentos/proyectos/PRY-201-core-de-depósitos/00-gobierno/ficha-pm.json`, con corte al 2026-10-18.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo.
- **Recálculo:** corrí `compute` antes de publicar. La fecha de cierre es 2027-06-21. Coincide con el acta y con el único cronograma que existe (v1, 2026-03-19), así que no hay diferencia entre la fecha vigente y la original.
- **Qué lleva:** 87 campos con dato y 2 sin decir en ninguna parte (`identity.authority` e `identity.phase`). Declara **amarillo** al 2026-10-16.
- **Lo más viejo:** el acta y el cronograma, del 2026-03-19. Tienen unos 7 meses, dentro del umbral de un año.
- **Lo que la PMO verá:** el avance declarado es 70 %, pero el plan solo sustenta entre 25 % y 50 %: 1 de 4 hitos cumplidos. La ficha ya traía esa señal y este comando no la añade.
- **Otras señales:** la ficha trae 14 señales en total. Ocho son compromisos vencidos, tres reprogramados y dos sin fecha.
- **Registro de la corrida:** quedó como `2026-10-18-pm-publish-1`, y lo que te mostré está en `estado/PRY-201-core-de-depósitos/corridas/salida-pm-publish.md`.

La carpeta de gobierno ya existía, así que no hubo que crearla. Copié el registro de la ficha tal cual con `cp`, sin cambiar campos. No avisé a nadie: la PMO la verá en su próximo barrido.