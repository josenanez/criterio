# /criterio-product:product-wake 

Revisé PRD-302 (Crédito hipotecario digital). Es la primera corrida del reloj y no había corte anterior, así que lo que sigue es lo que está abierto hoy, no novedades. Los términos ya estaban vigentes (v0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los pedí de nuevo.

**Qué toca hoy:** la revisión mensual. El comité no toca todavía. Ninguno de los 4 documentos de la carpeta cambió, así que no releí nada.

**Lo que ya pasó un umbral:**
- **Requerimientos sin decidir (más de 60 días):**
  - REQ-4212 lleva 115 días. Tiene doliente (Jorge Medina) pero ninguna cita de demanda.
  - REQ-4200 lleva 85 días y REQ-4207 lleva 83. Ninguno tiene doliente ni criterio de aceptación.
  - REQ-4201 lleva 71 días y tampoco tiene doliente.
- **Supuesto sin verificar:** «La demanda declarada se sostiene sin campaña» lleva 113 días, contra un umbral de 30. Ya corresponde tratarlo como riesgo registrado. Falta una medición de demanda sin campaña que lo sostenga o lo desmienta.
- **Evidencia vencida:** 10 requerimientos se apoyan en una sola entrevista del 2025-09-12, que ya tiene 13 meses. La afirmación de demanda de la definición se queda sin sustento vigente.
- **Aceptados sin sustento:**
  - REQ-4206, REQ-4210 y REQ-4213 no tienen ninguna cita de demanda.
  - REQ-4203 no tiene criterio de aceptación.
  - Ninguno de los 9 requerimientos aceptados tiene un proyecto que lo construya.

**Lo que no sé:**
- **Trazas:** no confirmé ninguna. La configuración no trae carpeta de fichas de proyectos, y sin ella ninguna traza se da por confirmada.
- **Quién decide qué se construye:** ningún documento lo declara. «Comité de producto» es solo lo que propone el acta del comité.
- **Criterio de éxito:** no está en ningún documento de la definición.

**Una anomalía menor:** el índice marca 8 campos del registro cuyo documento fuente no se encuentra con la ruta guardada (`documentos/productos/PRD-302/...`). No hay documentos renombrados ni borrados; parece un problema de la ruta registrada y conviene corregirla.

Dejé registrados la revisión, el corte (`snapshots/2026-10-17.json`) y la corrida (`2026-10-17-product-wake-1`). El informe completo está en `estado-producto/PRD-302/corridas/salida-product-wake.md`.

**Vuelvo el 2026-11-16.**