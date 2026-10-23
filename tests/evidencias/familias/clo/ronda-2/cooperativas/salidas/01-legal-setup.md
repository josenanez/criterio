# /criterio-legal:legal-setup legal/1790012345001-cooperativa-sierra-alta

Fidel quedó instalado sobre Cooperativa Sierra Alta (RUC 1790012345001, Ecuador, USD) y procesó los 7 contratos (CTR-201 a CTR-207). Quedan 7 fichas, sin problemas de validación.

**Qué encontró.** El motor marcó 4 señales, pero este comando no las detalla. Son pagos sobre el valor pactado, un contrato vencido que sigue activo, una diferencia con el registro y un certificado de la contraparte vencido. Cada una la revisan `contract-execution`, `contract-register` y `authority-check`.

**Calendario de obligaciones** (al 2026-10-06; ventana de 30 días atrás a 90 adelante):

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-201 | Reporte de operaciones al oficial de cumplimiento (OBL-3), con evidencia | -6 |
| 2026-11-20 | CTR-205 | Terminación | 45 |
| 2026-11-20 | CTR-205 | Informe final y acta de liquidación (OBL-2), sin evidencia todavía | 45 |

El calendario no marca nada urgente. El comité decidió renovar CTR-205 en el acta del 2026-09-18.

**Decisiones mías que conviene que verifiques:**
- **Fecha del informe final de CTR-202:** quedó en la terminación que fija el otrosí OT-1 (2027-12-31), no en la del contrato original.
- **Firmantes de la contraparte:** los anoté como «Representante de <razón social>», tal como aparecen en los documentos.
- **Entidad y umbrales:** tomé la entidad de los documentos (Ecuador, USD) y los umbrales de `config.example.json` (60 días para vencimientos, 30 para preavisos, 30 para el certificado).
- **Matriz de atribuciones:** usé la de la carpeta.

**Términos y marca.** Los términos 1.2 (versión 0.8.0) quedaron aceptados por José Francisco Ñáñez el 2026-10-06, con comprobante en `.criterio/terminos/`. Como respuesta sugerida, dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Es lo único que se escribió allí. No hice preguntas a nadie en esta prueba.

**Archivos:**
- Configuración: `.criterio/legal/1790012345001/config.json`
- Fichas: `estado-legal/1790012345001-cooperativa-sierra-alta/contratos/`
- Reporte del calendario: `estado-legal/1790012345001-cooperativa-sierra-alta/contratos/reporte-obligations-calendar.md`
- Salida de la corrida: `estado-legal/1790012345001-cooperativa-sierra-alta/corridas/salida-legal-setup.md`, registrada como `2026-10-06-legal-setup-1`