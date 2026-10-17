# /criterio-product:product-wake 

Revisé el registro de Microcrédito (PRD-305). Es la primera revisión, así que no había corte anterior. Todo lo que sigue es nuevo, y lo que toca es `review`. Volveré el 2026-11-16.

Los términos ya estaban vigentes: la versión 0.3.13, aceptada por José Francisco Ñáñez el 2026-10-17.

El registro tiene 17 requerimientos: 9 aceptados y 8 propuestos. Estos son los hallazgos:

- **Sin decidir:** los 8 propuestos llevan entre 72 y 206 días (el umbral es 60). Falta saber quién tiene la facultad de decidirlos, porque `authority` está en `not_found`. El comité de hoy solo anotó «Se mantiene el plan» y no resolvió ninguno.
- **Supuesto sin verificar:** «La demanda se sostiene sin campaña» lleva 194 días sin verificarse. Haría falta una serie de volumen mensual de un periodo sin campaña, con fecha y fuente.
- **Evidencia vencida:** toda la evidencia de demanda es una entrevista del 2025-09-06, con 13 meses. Esa entrevista no nombra ninguno de los 14 requerimientos que la citan.
- **Aceptado sin sustento:** REQ-4504 no tiene evidencia. REQ-2037, REQ-4501 y REQ-4514 no tienen criterio de aceptación. REQ-4503, REQ-4513 y REQ-4514 no tienen doliente.
- **Nadie lo construye:** los 9 aceptados no tienen proyecto, y la traza está en 0 %. No confirmé ninguna traza, porque no hay carpeta de fichas configurada.
- **Lo que no sé:** el criterio de éxito de la definición y la autoridad de decisión.

No hay documentos de descubrimiento nuevos. Dejé registrados la revisión (`ran`), el corte `snapshots/2026-10-17.json` y la corrida `2026-10-17-product-wake-1`.

Todo está en `estado-producto/PRD-305/`. El informe completo, con la tabla de los 8 requerimientos, está en `corridas/salida-product-wake.md`.