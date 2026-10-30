# /criterio-legal:legal-setup legal/OPB150301AB9-organismo-publico-del-bajio

Fidel quedó instalado sobre Organismo Público del Bajío (OPB150301AB9). El motor lo validó y no devolvió problemas en las 6 fichas.

**Qué pasó**
- **Carpeta:** usé la ruta del argumento, con 6 contratos (CTR-2301 a CTR-2306), el registro y la matriz de atribuciones. `00-referencia/politica-contratacion.md` está fuera de lugar y debería ir en `20-politicas/`. No moví nada y no dejé la marca `_CRITERIO_LEGAL.txt`, porque nadie la autorizó.
- **Respuestas:** no hice preguntas. Entidad pública, país MX y moneda MXN salen de los documentos. Avisos de 60 y 30 días y certificado de 30 días son los de `config.example.json`. El umbral de garantía queda vacío, porque en México no aplica.
- **Términos:** José Francisco Ñáñez aceptó la versión 1.3 el 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-1.0.0-2026-10-06.md` y `.pdf`.
- **Fichas:** convertí los 35 documentos y escribí las 6 fichas en `estado-legal/OPB150301AB9-organismo-publico-del-bajio/contratos/`.

**Lo que encontró el motor**
- **Garantías tardías:** 3 señales `public_guarantee_late`.

  | Contrato | Entregada | Límite según el motor |
  |---|---|---|
  | CTR-2302 | 2025-07-12 | 2025-07-06 |
  | CTR-2304 | 2026-03-12 | 2026-03-06 |
  | CTR-2306 | 2025-10-12 | 2025-10-06 |

  El límite es 10 días naturales después de la firma.
- **Calendario** (30 días atrás a 90 adelante, al 2026-10-06):
  - CTR-2301: el reporte al oficial de cumplimiento vencía el 2026-09-30 y tiene evidencia de entrega.
  - CTR-2305: termina el 2026-11-20 (en 45 días), con el informe final y el acta de liquidación sin evidencia.
  - CTR-2303: termina el 2026-12-31 (en 86 días), también con el informe final y el acta de liquidación sin evidencia.
- **Decisión de renovar:** el acta del comité del 2026-09-18 registra que CTR-2305 se renueva. La decisión es de una persona; yo solo la registré.

**Pendiente:** no corrí `authority-check` ni `contract-execution`, porque este comando no los incluye. Las señales de facultades y de pagos aparecerán cuando los corras.

**Registro de la corrida:** la salida completa está en `estado-legal/OPB150301AB9-organismo-publico-del-bajio/corridas/salida-legal-setup.md`. La corrida quedó registrada como `2026-10-06-legal-setup-1`, con 3 hallazgos. El reporte del calendario está en `estado-legal/OPB150301AB9-organismo-publico-del-bajio/contratos/reporte-obligations-calendar.md`.