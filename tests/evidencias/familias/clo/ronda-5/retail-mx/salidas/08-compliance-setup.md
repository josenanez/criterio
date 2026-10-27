# /criterio-compliance:compliance-setup legal/TBA180912Q37-tiendas-del-bajio

Constanza quedó instalada sobre Tiendas del Bajío (TBA180912Q37). Revisé las 10 obligaciones de la matriz contra su evidencia del periodo 2026-09, y el motor levantó 5 señales.

**Lo que dejé escrito**
- **Configuración:** `.criterio/cumplimiento/TBA180912Q37/config.json`. La valida el motor y no marcó problemas.
- **Términos:** la versión 1.2 queda aceptada por José Francisco Ñáñez con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-compliance-0.11.0-2026-10-06.md` y en su PDF.
- **Ficha del periodo:** el informe declara el estado "con observaciones", firmado por Sofía Elizondo el 2026-10-05. La ficha está en `estado-legal/TBA180912Q37-tiendas-del-bajio/cumplimiento/2026-09/ficha.json`.
- **Reporte y corrida:** el reporte `compliance-status` y la corrida de hoy quedaron guardados en la carpeta de estado.

**Lo que hay que atender**
- **OB-10:** la matriz la da por cumplida, pero no hay ninguna evidencia que empiece por OB-10.
- **OB-13:** no cita la norma, el contrato o la política de la que sale.
- **Otras 3 señales:** un caso del canal de denuncias vencido, una norma que aplica y ninguna obligación la cita, y una política con la revisión vencida. El reporte de estado no las detalla; para eso hay que correr `reports-cases`, `regulatory-watch` y `policy-review`.

**Respuestas sugeridas que tomé**
- **Periodo:** 2026-09, el último que tiene informe de cumplimiento.
- **Plazos:** 15 días para el canal de denuncias y 30 para evaluar una norma nueva, los mismos que ya usa la configuración de Fidel.
- **Fichas de Fidel:** `estado-legal/TBA180912Q37-tiendas-del-bajio/contratos`. Comprobé que la ruta existe.

**Lo que no hice**
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé en la carpeta de documentos, porque nadie autorizó escribir ahí. Queda como pregunta sin respuesta en la ficha.
- **Festivos:** `holidays` está vacío, como en la configuración de Fidel. No tengo la lista de festivos de México para cargarla.
- **Glob:** la herramienta no estaba disponible en esta sesión, así que usé `find` por Bash para ver la carpeta de estado.