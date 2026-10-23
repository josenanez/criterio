# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-201 en `documentos/proyectos/PRY-201-edificio-de-oficinas-torre-norte/00-gobierno/ficha-pm.json`, con corte al 2026-10-22.

**Lleva:** 220 campos con dato · 9 sin decir en ninguna parte · declara **verde** al 2026-10-21

- **Estado declarado:** el verde es una declaración del gerente, no de la PMO. Cuatro señales lo contradicen:
  - compromisos vencidos;
  - compromisos reprogramados;
  - dos hitos dados por cumplidos sin evidencia (licencias y cimentación);
  - dos entregables atrasados del proveedor (acero de refuerzo y bolsa de horas de ingeniería).
- **Lo más viejo que va ahí:** `vendors[0].contract_ref`, del 2026-04-14 (contrato CT-521). Tiene unos 6 meses, así que no pasa de un año.
- **Fecha de cierre:** `plan.end_date` es 2026-12-15 y sale del único cronograma que hay (v1). Coincide con la línea base y no hay nada que corregir.
- **Términos:** ya estaban vigentes (versión 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-22), así que no los registré de nuevo.

El comando no tiene un subcomando de publicación en `portafolio.py`. Copié el registro recalculado a `ficha-pm.json`, que es lo que el diseño pide. Este comando no avisa a nadie: Vera la encontrará en su próximo barrido.

La corrida quedó registrada como `2026-10-22-pm-publish-1` (19 hallazgos, 24 segundos), con la salida en `estado/PRY-201-edificio-de-oficinas-torre-norte/corridas/salida-pm-publish.md`.