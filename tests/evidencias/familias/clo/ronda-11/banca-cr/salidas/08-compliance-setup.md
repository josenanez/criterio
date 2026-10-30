# /criterio-compliance:compliance-setup legal/3101457812-banco-del-valle-central-sintetico

Constanza quedó lista sobre Banco del Valle Central Sintético (NIT 3101457812). Revisó las 10 obligaciones de la matriz contra su evidencia en el periodo 2026-09, y el informe declara el periodo cumplido mientras el motor encuentra 5 señales abiertas.

**Qué quedó hecho**
- **Carpeta:** usé la que venía en el argumento (60 documentos, 6 contratos, 3 periodos). Le dejé la marca `_CRITERIO_LEGAL.txt`, con autorización de José Francisco Ñáñez.
- **Configuración:** está en `.criterio/cumplimiento/3101457812/config.json` y el motor la validó sin problemas.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-06. El comprobante está en `terminos/` en Markdown y PDF.
- **Ficha del periodo:** registré lo que declara el informe: "cumplido", con fecha 2026-10-05.
- **Corrida:** `2026-10-06-compliance-setup-1`.

**Qué muestra el estado de 2026-09** (avance con evidencia 72,73 %, ponderado por criticidad)
1. OB-09, reporte mensual de quejas (Gabriela Quesada), venció el 2026-10-05 sin evidencia.
2. El informe declara el periodo cumplido, pero hay 4 señales abiertas que ese estado no explica.
3. La obligación OBL-3 del contrato CTR-3601 (cláusula 7) no está en la matriz.
4. OB-12, registro de conflictos de interés, no tiene responsable.
5. La norma N-2026-05 sigue "por evaluar". El motor la cuenta como señal, pero el reporte no la lista en "Lo que hay que atender". Lo anoté en la salida guardada.

**Lo que tomé como respuesta sugerida, sin preguntar** (nadie podía contestar): marcar la carpeta, el periodo 2026-09 y los umbrales por defecto. Las rutas de las fichas de Fidel las comprobé antes de proponerlas.

El reporte completo está en `estado-legal/3101457812-banco-del-valle-central-sintetico/cumplimiento/2026-09/reporte-compliance-status.md`. Lo que le mostré a la persona quedó en `corridas/salida-compliance-setup.md`.