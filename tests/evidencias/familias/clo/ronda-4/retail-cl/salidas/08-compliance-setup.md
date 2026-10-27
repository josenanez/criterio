# /criterio-compliance:compliance-setup legal/76083001-1-tiendas-pacifico

Constanza quedó instalada sobre Tiendas Pacífico (76083001-1) y revisó las 10 obligaciones de la matriz contra su evidencia en el periodo 2026-09. El informe de septiembre declara el periodo «cumplido», pero el motor encontró 4 señales abiertas.

- **Carpeta raíz:** usé `legal/76083001-1-tiendas-pacifico`, que venía en el argumento. Ya tenía la marca `_CRITERIO_LEGAL.txt`, así que no la pregunté de nuevo.
- **Inventario:** 61 documentos, sin cambios ni archivos fuera de lugar. Hay 6 contratos y 3 periodos de cumplimiento.
- **Configuración:** quedó en `.criterio/cumplimiento/76083001-1-tiendas-pacifico/config.json` y el motor la validó sin problemas.
  - Parte de la configuración de Fidel para la misma entidad.
  - Apunta a las 6 fichas de contratos de `estado-legal/76083001-1-tiendas-pacifico/contratos`, que comprobé con `find`.
- **Términos:** mostré el `en_corto` tal cual y registré la aceptación de José Francisco Ñáñez con fecha 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/` (Markdown y PDF).
- **Ficha del periodo:** `estado-legal/76083001-1-tiendas-pacifico/cumplimiento/2026-09/ficha.json` registra lo que declara el informe (cumplido, 2026-10-05). El informe no trae normas nuevas.
- **Avance con evidencia:** 72,73 % ponderado por criticidad.

Las señales abiertas son estas:
1. **OB-09, reporte mensual de quejas (Javiera Soto):** venció el 2026-10-05 y no tiene evidencia.
2. **Declarado contra evidenciado:** el informe dice «cumplido», pero hay 3 señales abiertas que ese estado no explica.
3. **OB-13, reporte de regalos e invitaciones:** la matriz no cita la norma, el contrato o la política de la que sale.
4. **Una política con la revisión vencida:** el reporte no la detalla; se ve con `/policy-review`.

Las demás obligaciones están cumplidas con evidencia, salvo OB-04 y OB-05, que están en plazo sin evidencia todavía.

No hice preguntas, porque nadie podía responderlas en esta sesión. Todo lo que llegó se procesó.

La corrida quedó registrada como `2026-10-06-compliance-setup-1`. El reporte completo está en `estado-legal/76083001-1-tiendas-pacifico/cumplimiento/2026-09/reporte-compliance-status.md`.