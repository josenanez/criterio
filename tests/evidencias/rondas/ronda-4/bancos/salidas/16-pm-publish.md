# /criterio-project:pm-publish confirmar

Publiqué la ficha en `documentos/proyectos/PRY-210-portal-de-proveedores/00-gobierno/ficha-pm.json`, con corte al 2026-10-15. Los términos ya estaban vigentes (versión 0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Lleva:** 39 campos con dato · 3 sin decir en ninguna parte (producto, autoridad, fase) · declara **verde** al 2026-10-13.

**Lo más viejo que va ahí:** el acta de constitución, del 2025-09-01. Aporta 10 campos de identidad y plan (patrocinador, gerente, comité, fecha de fin y otros). Tiene 13 meses, así que pasa de un año.

**Antes de que la PMO la lea:**
- El recálculo contradice el estado verde con cuatro señales:
  - El avance declarado es 34 %, y el plan sostiene entre 60 y 80 %.
  - Dos hitos figuran como cumplidos sin acta de recibo.
  - Hay 5 compromisos vencidos.
  - Hay 4 compromisos reprogramados varias veces.
- De los ocho campos que Vera contrasta, solo `identity.product` no está en ninguna parte (el acta dice «No aplica»). Los otros siete llevan dato.

`portafolio.py` no tiene un subcomando para publicar. Copié la ficha de `records/PRY-210.json` tal cual, sin campos fuera del esquema. La carpeta de gobierno ya existía.

La corrida quedó registrada como `2026-10-15-pm-publish-1`, con la salida completa en `estado/PRY-210-portal-de-proveedores/corridas/salida-pm-publish.md`.