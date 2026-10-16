# /criterio-project:pm-plan 

Armé el borrador de plan de PRY-200 desde el acta y el contrato CT-235, sin fechas y con las duraciones vacías. La corrida quedó registrada como `2026-10-15-pm-plan-1`.

Los términos ya estaban vigentes (v0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

**Lo que le falta al acta**
- El alcance dice solo «Componente 1, 2 y 3» y el fuera de alcance dice «lo que otro proyecto cubre». No hay nada que descomponer ahí, así que esos nodos van como «sin definir».
- El criterio de éxito («en producción y medido») no dice qué se mide ni con qué umbral.
- No hay autoridad declarada ni quién acepta los entregables. El patrocinador sí está (Rubén Cárdenas).
- Las dependencias dicen «Ninguna declarada».

**WBS: 8 nodos**
- Tres salen del contrato CT-235 (licenciamiento, bolsa de horas, calibración de sensores). Van como supuesto, porque el acta no menciona el contrato.
- Tres son los componentes del acta, sin definir.
- Dos salen del criterio de éxito: producción y medición.

**Presupuesto:** los tres entregables del contrato suman 614.564.511 COP de los 2.400.000.000 aprobados. En qué se gasta el resto no está en ningún documento.

**Proyectos análogos:** ninguno a la vista. La configuración no apunta a una carpeta de fichas de la PMO, y no busqué por mi cuenta.

**Contexto que importa:** el proyecto ya tiene cronograma v1 y v2, y el cierre del acta (2026-05-13) ya pasó. Si lo que necesitas es revisar el plan vigente, el modo es `/pm-plan revisar`.

**Discrepancia que no resolví:** el contrato marca «Licenciamiento del software» como pendiente, con fecha comprometida 2025-12-08. El cronograma v2 marca todos los hitos como cerrados. Está anotada al final de la salida para `/pm-report` o `/pm-commitments`.

Además, el registro de la corrida arrastró 18 señales abiertas de corridas anteriores de PRY-200, por ejemplo 7 compromisos vencidos. Esas no las produjo este plan.

El texto completo está en `estado/PRY-200-mantenimiento-predictivo-de-camiones/corridas/salida-pm-plan.md`.