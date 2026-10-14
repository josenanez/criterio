# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-202 en `/home/claude/banco/ronda-1/bancos/espacio/documentos/proyectos/PRY-202-migración-a-la-nube/00-gobierno/ficha-pm.json`, con corte al 2026-10-14.

Los términos 1.0 ya estaban aceptados en la configuración, así que no pedí nada. La carpeta de gobierno ya existía y no creé nada más. Es una copia tal cual de `records/PRY-202.json`, y la ficha sigue sin sellar.

**Lleva:** 10 campos con dato · 7 sin decir en ninguna parte · **no declara estado**

- **Sin decir en ninguna parte:** `identity.authority`, `identity.phase`, `declared`, `plan.milestones`, `money.committed`, `money.executed` y `money.projection`. Además `identity.product` no está en la ficha.
- **Estado:** no hay `declared.status` ni `declared.as_of`, así que la PMO verá vacío justo lo primero que mira.
- **Conflicto abierto:** la fecha del compromiso de Paula Céspedes. El acta del comité dice 2026-11-02 y las notas de la reunión dicen 2026-10-28.

**Lo más viejo que va ahí:** los campos de identidad, plan y dinero salen del acta de constitución del 2026-02-19, unos ocho meses atrás. No pasa de un año.

Dejé registrada la corrida como `2026-10-14-pm-publish-1`. El archivo de salida es `estado/PRY-202-migración-a-la-nube/corridas/salida-pm-publish.md`.