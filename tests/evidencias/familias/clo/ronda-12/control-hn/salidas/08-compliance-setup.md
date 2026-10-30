# /criterio-compliance:compliance-setup legal/08010007330150-comercial-control-de-honduras

Constanza quedó instalada sobre Comercial Control de Honduras (RTN 08010007330150). El primer estado del periodo 2026-09 muestra 6 de 8 obligaciones con evidencia. El motor da un avance con evidencia de 83,33 % (ponderado por criticidad).

- **Carpeta:** usé la del argumento. Ya tenía la marca `_CRITERIO_LEGAL.txt`, así que no la pedí de nuevo. El inventario trae 57 documentos, 6 contratos y 3 periodos, sin nada fuera de lugar ni ilegible.
- **Configuración:** la escribí en `.criterio/cumplimiento/08010007330150/config.json` y el motor la validó sin problemas. Había otra de Fidel (rol jurídico) y la dejé como estaba. Las fichas de contratos de Fidel están en `estado-legal/08010007330150-comercial-control-de-honduras/contratos`.
- **Términos:** mostré el resumen de la versión 1.3 y los registré a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes en `.md` y `.pdf` quedaron en `.criterio/terminos/`.
- **Preguntas:** hice 2 y las respondí con la propuesta de los documentos. Son el periodo (2026-09) y la ruta de las fichas de Fidel.
- **Informe del periodo:** declara «cumplido» (Mario Aguilar, 2026-10-05).
- **Obligaciones:**
  - Con evidencia: OB-01, OB-02, OB-03, OB-06, OB-07 y OB-08.
  - En plazo y sin evidencia todavía: OB-04, que vence el 2026-12-31, y OB-05, que vence el 2026-10-20.
  - OB-07 está cumplida con una evidencia de julio de 2026 (`cumplimiento-2026-07`).
- **Norma nueva:** el boletín de septiembre trae N-2026-09 (Circular sintética 009 de 2026), por evaluar. El registro normativo todavía no la tiene.
- **Señales:** el motor no levantó ninguna. Eso incluye la comparación entre lo declarado y lo evidenciado.

Dejé la ficha del periodo en `estado-legal/08010007330150-comercial-control-de-honduras/cumplimiento/2026-09/ficha.json`, el reporte en `cumplimiento/2026-09/reporte-compliance-status.md` y la salida en `corridas/salida-compliance-setup.md`. La corrida quedó registrada como `2026-10-06-compliance-setup-1`.

Un detalle de fechas: la sesión tiene fecha de hoy 2026-10-30, pero todo el motor corrió con `--today 2026-10-06`, como pediste. La marca de la carpeta dice 2026-10-30.