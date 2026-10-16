# /criterio-project:pm-plan 

Dejé el borrador del plan de PRY-209 (Migración del ERP) sin ninguna fecha ni duración comprometida, y la corrida quedó registrada. El archivo está en `estado/PRY-209-migración-del-erp/corridas/salida-pm-plan.md`.

**Términos:** ya estaban aceptados para esta versión (0.3.11) a nombre de José Francisco Ñáñez, fecha 2026-10-16. No hubo que volver a registrarlos.

**Antes de empezar:** el proyecto ya está en ejecución (inició el 2026-04-27, 71 % declarado el 2026-10-12). Por eso el borrador es una descomposición retroactiva y no toca la línea base v1.

**Lo que le falta al acta:**
- **Alcance:** dice «Componente 1, 2, 3» sin describirlos, así que no hay entregables del acta que descomponer.
- **Criterio de éxito:** «en producción y medido» no dice qué se mide ni contra qué umbral.
- **Autoridad:** no dice qué decide el gerente y qué sube al comité.
- **Dependencias:** «Ninguna declarada», lo cual es poco creíble para un ERP.
- **Proveedor:** el acta no lo menciona, aunque los riesgos sí hablan de uno.

El patrocinador sí está declarado (Gustavo Neira).

**WBS (7 nodos):** los cuatro hitos del cronograma v1, el entregable final «en producción y medido», los componentes 1 a 3 (sin descomponer) y el hallazgo de seguridad en medios de pago. Este último es un supuesto mío: aparece como incidencia pero no tiene hito. Ningún nodo tiene quién lo acepta, y todas las duraciones están vacías.

**Orden:** diseño → ambiente de pruebas → integración → piloto → producción. Sale del orden del cronograma v1 y lo marqué como supuesto, porque el acta no declara dependencias.

**Proyectos análogos:** la configuración no apunta a ninguna carpeta de fichas de la PMO, así que no hay referencia y no estimé por analogía.

**Para comprometer una fecha falta:** la disponibilidad del equipo, la fecha del proveedor (que no la ha confirmado), la ventana de tiendas para el piloto y las respuestas a nueve preguntas para el equipo. Además, que alguien con autoridad apruebe el plan.

La corrida quedó como `2026-10-16-pm-plan-1`, con 13 señales abiertas (compromisos vencidos, sin fecha o reprogramados, avance contra plan, y declaración contra evidencia).