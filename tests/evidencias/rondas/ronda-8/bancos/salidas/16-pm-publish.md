# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-202 en `documentos/proyectos/PRY-202-migración-a-la-nube/00-gobierno/ficha-pm.json`, con corte al 2026-10-17. Es una copia de la ficha que Samuel ya tenía en su estado. No escribí en ningún otro archivo de la carpeta de documentación.

**Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hizo falta pedirlos de nuevo.

**Fecha de cierre:** la vigente es 2027-06-29, tomada del cronograma v2. La original del acta, 2027-04-14, queda en `plan.baseline`. El desvío contra la original es de 76 días (14,7 %).

**Lleva:** 16 campos con dato y 3 sin decir en ninguna parte: `identity.product`, `identity.authority` e `identity.phase`. Declara **rojo** al 2026-10-17, con 77 % de avance declarado.

**Lo más viejo que va ahí:** `identity.code`, `identity.name`, `identity.business_area`, `identity.sponsor`, `identity.committee` y `plan.start_date`, del acta de constitución del 2025-11-03. Tienen 348 días, así que no pasan de un año.

Quedaron registradas 17 señales en la corrida `2026-10-17-pm-publish-1`.

Un aviso sobre cómo lo hice: `portafolio.py` no tiene un subcomando para publicar. Copié la ficha calculada a la carpeta de gobierno con `cp`, sin cambiarle ningún campo.

La salida completa está en `estado/PRY-202-migración-a-la-nube/corridas/salida-pm-publish.md`. No avisé a nadie: Vera la leerá en su próximo barrido.