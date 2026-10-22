# /criterio-compliance:compliance-setup legal/900000001-distribuidora-control

Constanza quedó instalada sobre Distribuidora Control (900000001), y el estado de septiembre salió sin señales abiertas.

**Instalación**
- **Carpeta:** `legal/900000001-distribuidora-control` venía en el argumento. El inventario encontró 57 documentos, todos en su lugar.
- **Configuración:** la escribí en `.criterio/cumplimiento/900000001/config.json` y el motor la validó. El comando `config` solo lee, así que la escribí a mano.
  - Periodo 2026-09.
  - Plazo del canal de denuncias: 15 días.
  - Días para evaluar una norma: 30. Los dos plazos son los valores por defecto del motor, porque ningún documento fija otros.
  - Fichas de Fidel en `estado-legal/900000001-distribuidora-control/contratos`, que comprobé en disco: 6 fichas, de CTR-501 a CTR-506.
- **Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 (versión 1.2) y quedó el comprobante en Markdown y PDF.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`. Sin interfaz nadie autorizó escribir dentro de los documentos.

**Primer estado (periodo 2026-09, corte 2026-09-30)**
- El informe declara «cumplido».
- El avance con evidencia es 83,33 %, ponderado por criticidad.
- De las 8 obligaciones, 6 tienen evidencia.
- OB-04 (certificación anual de la junta, vence 2026-12-31) y OB-05 (capacitación mensual, vence 2026-10-20) siguen en plazo y aún no tienen evidencia.
- El motor no encontró señales, y todo lo que llegó se procesó.

El reporte completo quedó en `estado-legal/900000001-distribuidora-control/cumplimiento/2026-09/reporte-compliance-status.md`. Lo mostrado en esta sesión quedó guardado en `estado-legal/900000001-distribuidora-control/corridas/salida-compliance-setup.md`, y la corrida se registró como `2026-10-06-compliance-setup-2`.

Dos cosas sobre el estado que ya estaba en disco:
- **Ficha del periodo:** `cumplimiento/2026-09/ficha.json` ya traía el estado declarado y una norma por evaluar (`N-2026-09`). Los dejé como estaban y solo agregué las preguntas de esta sesión.
- **Aceptaciones anteriores:** la carpeta `.criterio/terminos` ya tenía aceptaciones de `criterio-compliance` 0.7.0 (2026-10-06 y 2026-10-22). Esta quedó con sufijo `-2` y no pisó ninguna.