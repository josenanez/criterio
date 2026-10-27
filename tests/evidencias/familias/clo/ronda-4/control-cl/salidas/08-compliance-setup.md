# /criterio-compliance:compliance-setup legal/76097001-8-comercial-control-andes

Constanza quedó instalada sobre Comercial Control Andes (76097001-8), y el primer estado del periodo 2026-09 ya está calculado.

**Qué dejé hecho**
- **Carpeta:** usé `legal/76097001-8-comercial-control-andes`, que venía en el argumento. Ya tenía la marca `_CRITERIO_LEGAL.txt`, así que no escribí nada en ella. El inventario encontró 57 documentos, 8 obligaciones en la matriz, 6 contratos y 3 periodos de cumplimiento.
- **Configuración:** `.criterio/cumplimiento/76097001-8-comercial-control-andes/config.json`, validada sin problemas. Los umbrales los tomé de la configuración que Fidel ya tenía para esta entidad (canal de denuncias 15 días, evaluación de normas 30 días), y las fichas de Fidel están en `estado-legal/76097001-8-comercial-control-andes/contratos`.
- **Términos 1.2:** José Francisco Ñáñez los aceptó con fecha 2026-10-06, y el comprobante en Markdown y PDF quedó en `.criterio/terminos/`.
- **Ficha del periodo:** el informe de septiembre declara «cumplido» (fecha 2026-10-05). El boletín de septiembre trae la norma N-2026-09 (Circular sintética 009 de 2026), que sigue por evaluar si aplica y aún no está en el registro normativo.

**Lo que muestra el motor para 2026-09**
- **Avance con evidencia:** 83,33 %, ponderado por criticidad.
- **Cumplidas con evidencia:** OB-01, OB-02, OB-03, OB-06, OB-07 y OB-08.
- **En plazo y sin evidencia todavía:** OB-04 (vence 2026-12-31) y OB-05 (vence 2026-10-20).
- **Señales abiertas:** ninguna en lo que procesa `compliance-status`. Ese comando no mira el registro normativo ni el canal de denuncias. Para N-2026-09 y el caso C-002, que sigue en investigación, hay que correr `regulatory-watch` y `reports-cases`.

**Preguntas.** No hubo nadie que contestara. Hice 4 y tomé la respuesta sugerida de los documentos en cada una: la carpeta, el periodo, los plazos y las fichas de Fidel. Todas quedaron registradas en la ficha con su fuente.

El reporte completo, tal como lo escribió el motor, está en `estado-legal/76097001-8-comercial-control-andes/cumplimiento/2026-09/reporte-compliance-status.md`. Lo que te mostré quedó guardado en `estado-legal/76097001-8-comercial-control-andes/corridas/salida-compliance-setup.md`, y la corrida está registrada como `2026-10-06-compliance-setup-1`.