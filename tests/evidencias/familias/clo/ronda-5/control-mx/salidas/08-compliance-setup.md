# /criterio-compliance:compliance-setup legal/CCM120615R59-comercial-control-centro

Constanza quedó instalada sobre Comercial Control Centro (CCM120615R59, México, MXN). Revisé las 8 obligaciones del periodo 2026-09 contra su evidencia. El motor no levantó ninguna señal abierta.

**Lo que dejé hecho**
- **Configuración:** la escribí en `.criterio/cumplimiento/CCM120615R59/config.json` y el motor la validó sin problemas. Las rutas de documentos y estado son las de la entidad, y las fichas de contratos de Fidel están en `estado-legal/CCM120615R59-comercial-control-centro/contratos`, que comprobé que existe.
- **Términos:** los mostré tal cual y registré la aceptación de José Francisco Ñáñez para la versión 1.2, con fecha 2026-10-06. Los comprobantes en Markdown y PDF quedaron en `.criterio/terminos/`.
- **Marca de la raíz:** la carpeta ya tenía `_CRITERIO_LEGAL.txt`, así que no volví a preguntar ni a escribir nada en los documentos.
- **Ficha del periodo:** `estado-legal/CCM120615R59-comercial-control-centro/cumplimiento/2026-09/ficha.json` recoge dos cosas:
  - El informe del 2026-10-05 declara el estado como «cumplido».
  - El boletín de septiembre trae la Circular sintética 009 de 2026 (N-2026-09), que queda como «por evaluar». Está en el boletín pero no en el registro normativo, y no decidí si aplica.
- **Reporte:** `compliance-status` lo generó el motor. Está en `cumplimiento/2026-09/reporte-compliance-status.md` y su texto, con una nota mía antes del encabezado, en `corridas/salida-compliance-setup.md`.
- **Corrida:** quedó registrada como `2026-10-06-compliance-setup-1`, con 1 pregunta (la de los términos), 8 obligaciones revisadas y 0 hallazgos.

**Estado de las 8 obligaciones, según el motor**
- **Avance con evidencia:** 83.33 % ponderado por criticidad, contra el estado declarado «cumplido».
- **Con evidencia (6):** OB-01, OB-02, OB-03, OB-06, OB-07 y OB-08.
- **En plazo, sin evidencia todavía (2):** OB-04, que vence el 2026-12-31, y OB-05, que vence el 2026-10-20.
- **OB-07:** su evidencia es la de la carpeta `cumplimiento-2026-07`, porque es una revisión semestral.

Por ser una prueba sin interfaz, no hice más preguntas. La matriz de obligaciones salió tal cual del CSV y no completé ninguna fila. Tampoco calculé cifras ni fechas por mi cuenta: todas vienen del motor.