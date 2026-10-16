# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-207 en `/home/claude/banco/ronda-6/bancos/espacio/documentos/proyectos/PRY-207-onboarding-pyme/00-gobierno/ficha-pm.json`, con corte al 2026-10-16.

**Lleva:** 15 campos con dato · 2 sin decir en ninguna parte (`identity.authority`, `identity.phase`; tampoco hay proveedores) · declara **verde** al 2026-10-13.

**Lo más viejo que va ahí:** los campos de identidad, alcance y fecha de inicio, del acta de constitución del 2026-01-20. Tienen unos 9 meses, así que no pasan de un año.

- **Fecha de cierre:** `plan.end_date` es 2027-06-07, tomada del cronograma v2 (2026-10-13), que es el vigente. La del acta, 2027-03-22, va en `plan.baseline`. La diferencia son los 77 días de la solicitud de cambio CC-01.
- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.
- **Estado declarado:** es verde, y lo primero que verá la PMO es que el cálculo lo contradice con 5 señales:
  - compromisos vencidos;
  - compromisos reprogramados;
  - hitos dados por cumplidos sin evidencia;
  - avance declarado de 30 %, frente a 50–75 % que sustenta el plan;
  - 77 días de atraso contra la línea base original.
- **Corrida:** quedó registrada como `2026-10-16-pm-publish-1`, con 21 hallazgos. La salida completa está en `estado/PRY-207-onboarding-pyme/corridas/salida-pm-publish.md`.

No toqué ningún otro archivo de la documentación y no avisé a nadie. Vera encontrará la ficha en su próximo barrido.