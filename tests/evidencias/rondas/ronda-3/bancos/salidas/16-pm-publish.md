# /criterio-project:pm-publish confirmar

Publiqué la ficha en `/home/claude/banco/ronda-3/bancos/espacio/documentos/proyectos/PRY-207-onboarding-pyme/00-gobierno/ficha-pm.json`, con corte al 2026-10-15.

**Lleva:** 11 campos con dato y 3 sin decir en ninguna parte (`identity.authority`, `plan.milestones`, `declared.status`). **No declara estado**, porque en tu ficha no hay declaración tuya. Vera no verá `declared.status` ni `declared.as_of`, dos de los ocho campos que contrasta.

**Lo más viejo que va ahí:** los 11 campos con dato salen del acta de constitución del 2026-03-09, con unos 7 meses de antigüedad. Ninguno pasa de un año.

**Alertas del recálculo:**
- **"Cerrar la prueba 2" (Laura Vélez):** se ha reprogramado 6 veces. Era para el 2026-09-23 y ahora está en el 2026-12-07.
- **"Enviar el ajuste del presupuesto" (Laura Vélez):** no tiene fecha ("la otra semana").

La ficha tampoco lleva línea base ni hitos.

**Cómo quedó el resto:**
- **Términos:** ya estaban vigentes (versión 0.3.9, aceptados el 2026-10-15 por José Francisco Ñáñez), así que no los registré otra vez.
- **Copia de la ficha:** `ficha-pm.json` es copia exacta de `records/PRY-207.json`. La carpeta de gobierno ya existía.
- **Corrida:** quedó registrada como `2026-10-15-pm-publish-1`, con la salida guardada en `estado/PRY-207-onboarding-pyme/corridas/salida-pm-publish.md`.