# /criterio-project:pm-publish confirmar

Publiqué la ficha en `/home/claude/banco/ronda-10/cooperativas/espacio/documentos/proyectos/PRY-201-apertura-de-ahorro-en-línea/00-gobierno/ficha-pm.json`, con corte al 2026-10-18.

**Lleva:** 17 campos con dato · 2 sin decir en ninguna parte (`identity.authority`, `identity.phase`) · declara **verde** al 2026-10-17, con 91 % de avance. El verde es una declaración de la gerente y la ficha la marca así.

**Lo más viejo que va ahí:** los datos de identidad, plan y presupuesto aprobado, todos del acta y el cronograma del 2025-06-01. Tienen 16 meses, así que pasan de un año.

- **Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no los registré de nuevo.
- **Recálculo:** corrí `compute` antes de publicar.
- **Fecha de cierre:** `plan.end_date` es 2026-10-04, el último hito del único cronograma que hay (v1). No hay uno más nuevo, así que la fecha vigente y la de la línea base coinciden.
- **Alertas:** el recálculo da 14, y el verde declarado no las explica.
  - El hito «Integración con el core cooperativo» lleva 14 días vencido.
  - Dos hitos se declaran cumplidos sin evidencia.
  - Hay 5 compromisos vencidos, 3 reprogramados entre 4 y 6 veces y 2 sin fecha.
- **Cómo la publiqué:** `portafolio.py` no tiene un subcomando que publique, así que copié el registro del estado a la carpeta de gobierno con `cp`.
- **Corrida:** quedó registrada como `2026-10-18-pm-publish-1`, con la salida guardada en `estado/PRY-201-apertura-de-ahorro-en-línea/corridas/salida-pm-publish.md`.