# /criterio-project:pm-publish confirmar

Publiqué la ficha en `documentos/proyectos/PRY-202-planta-de-tratamiento-de-agua/00-gobierno/ficha-pm.json`, con corte al 2026-10-17.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré otra vez.

**Lleva:** 165 campos con dato · 12 sin decir en ninguna parte · declara **verde** al 2026-10-16.

**Fecha de cierre:** `plan.end_date` es 2027-09-20, tomada del cronograma v2 del 2026-10-16. La del acta, 2027-05-28, queda en `plan.baseline`. La línea base vigente es la v2 (CC-01, +115 días).

**Lo más viejo que va ahí:** `vendors[0].contract_ref` y los importes y fechas de los entregables del contrato CT-812, del 2026-02-21. Tiene menos de un año, así que no pasa el umbral de 12 meses.

**Lo que la PMO va a ver:** el «verde» va marcado como declarado, y el cálculo lo contradice con 7 señales:
- La variación de tiempo es del 25,8 % contra la línea base original.
- La proyección de costo queda 28,9 % por encima de lo aprobado.
- El avance declarado es 89 %, y el plan sostiene entre 40 % y 60 %.
- Dos hitos figuran como cumplidos sin evidencia.
- Hay compromisos vencidos y reprogramados.
- Un entregable del proveedor lleva 124 días de atraso.

Quedan sin dato el producto, la autoridad y la fase. Los 5 hitos y los 4 entregables del proveedor no tienen evidencia documental.

**Dónde escribí:** solo ese archivo, más el registro de la corrida. La salida está en `estado/PRY-202-planta-de-tratamiento-de-agua/corridas/salida-pm-publish.md` y la corrida quedó como `2026-10-17-pm-publish-1`. No avisé a nadie; Vera lo encontrará en su próximo barrido.

El script `portafolio.py` no tiene un comando para publicar, así que copié la ficha tal cual de `records/PRY-202.json`, sin quitarle ni agregarle campos.