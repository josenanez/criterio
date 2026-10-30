# /criterio-legal:legal-setup legal/08010006129040-almacenes-del-valle-de-sula

Fidel quedó instalado sobre Almacenes del Valle de Sula (RTN 08010006129040, Honduras). Procesé los 7 contratos y el motor encontró 5 señales.

**Lo que hice**
- **Configuración:** la dejé en `.criterio/legal/08010006129040/config.json` y el motor la validó sin problemas. Usé los valores de ejemplo: avisos de 60 y 30 días, certificado de 30 días como máximo. La entidad no es pública, así que no apliqué la revisión de contratación pública.
- **Términos:** quedaron aceptados (versión 1.3) a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes están en `.criterio/terminos/`.
- **Fichas:** escribí una ficha por contrato (CTR-4101 a CTR-4107) en `estado-legal/08010006129040-almacenes-del-valle-de-sula/contratos/`, sin observaciones del motor. Cada dato lleva la cita de su documento. En CTR-4105 registré la decisión de renovar, que sale del acta del 2026-09-18.
- **Raíz de documentos:** no la marqué con `_CRITERIO_LEGAL.txt`, porque nadie lo autorizó. No escribí nada dentro de los documentos.

**Calendario de vencimientos**
- **CTR-4103 (arrendamiento de la sede principal):** vence el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar. Esa decisión es de una persona.
- **CTR-4105:** termina el 2026-11-20 (45 días) y su informe final y acta de liquidación vencen ese mismo día.
- **CTR-4101:** el reporte de operaciones al oficial de cumplimiento vencía el 2026-09-30 y ya está entregado.

**Las otras 4 señales**
- Una es de firma sin facultad.
- Una es de garantía faltante.
- Dos son de registro: una no cuadra y otra difiere del contrato.

El calendario no las detalla. Las mostrarán `/authority-check`, `/contract-execution` y `/contract-register`.

La corrida quedó registrada como `2026-10-06-legal-setup-1`. Lo que te mostré, completo, está en `estado-legal/08010006129040-almacenes-del-valle-de-sula/corridas/salida-legal-setup.md` y el reporte del calendario en `contratos/reporte-obligations-calendar.md`.