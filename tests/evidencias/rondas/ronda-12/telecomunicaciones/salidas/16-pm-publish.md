# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-211 en `documentos/proyectos/PRY-211-plataforma-de-internet-de-las-cosas/00-gobierno/ficha-pm.json`, con corte al 2026-10-28.

**Términos:** estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no hizo falta volver a registrarlos.

**Fecha de cierre:** `plan.end_date` es 2026-11-05 y sale del cronograma v2 del 2026-10-28, el más nuevo. La del acta (2026-07-26) quedó en `plan.baseline`.

**Lleva:**
- 3 campos sin decir en ninguna parte: `identity.authority`, `identity.phase` y `vendors[0].invoiced`.
- El estado declarado es **amarillo**, con 49 % de avance, al 2026-10-28.
- El resto de los campos va con dato. No los conté uno a uno.

**Lo más viejo que va ahí:** los datos del proveedor y del contrato CT-707, del 2025-12-29. No pasan de un año. Patrocinador, gerente y comité son del acta del 2026-01-05.

**Lo primero que verá la PMO:**
- La ficha declara amarillo, pero trae 102 días de atraso frente a la línea base original (53,1 %).
- Declara 49 % de avance con los 5 hitos marcados como cumplidos.
- Dos de esos hitos no tienen evidencia: "Diseño de red aprobado" e "Integración con la red".
- Hay 6 compromisos vencidos y 7 reprogramados.
- Los 2 entregables del proveedor siguen pendientes y vencidos, sin recibo.
- El cambio CC-01 sigue pendiente de decisión.

**Cómo se escribió:** `portafolio.py` no tiene subcomando para publicar. Copié la ficha de `estado/…/records/PRY-211.json` tal cual, sin agregar campos. No avisé a nadie; Vera la encontrará en su próximo barrido.

**Registro de la corrida:** `2026-10-28-pm-publish-1`, con 20 hallazgos y 21 segundos. La salida completa quedó en `estado/PRY-211-plataforma-de-internet-de-las-cosas/corridas/salida-pm-publish.md`.