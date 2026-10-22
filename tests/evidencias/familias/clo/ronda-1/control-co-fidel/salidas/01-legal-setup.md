# /criterio-legal:legal-setup legal/900000001-distribuidora-control

Fidel quedó instalado sobre Distribuidora Control (NIT 900000001, Colombia), con los 6 contratos procesados y la corrida registrada. El motor no encontró señales: ni vencimientos urgentes, ni firmas sin facultad, ni pagos por fuera de lo pactado.

- **Carpeta:** el argumento ya traía la ruta (`legal/900000001-distribuidora-control`), así que no busqué la raíz. Contiene los contratos CTR-501 a CTR-506, el registro y la matriz de atribuciones, y nada fuera de lugar.
- **Preguntas:** nadie respondió, así que tomé las respuestas sugeridas de los documentos. Quedaron avisos de 60 días para vencimientos y 30 para preavisos, certificado de la contraparte de 30 días como máximo y estado en `estado-legal/900000001-distribuidora-control`.
- **Marca de la carpeta:** la marqué con `_CRITERIO_LEGAL.txt`, también por la respuesta sugerida. Es lo único que escribí dentro de los documentos.
- **Términos:** los de la versión 1.2 quedaron aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Fichas:** escribí una por contrato a partir de los documentos. El motor no reportó `record_issues`.
- **Calendario** (al 2026-10-06, ventana de 30 días atrás a 90 adelante):
  - El reporte de operaciones al oficial de cumplimiento de CTR-501 vencía el 2026-09-30 y tiene evidencia entregada.
  - CTR-505 termina el 2026-11-20 (en 45 días); el comité decidió renovarlo el 2026-09-18.
  - CTR-503 termina el 2026-12-31 (en 86 días).
  - Para ambos falta el informe final y el acta de liquidación.

Dos datos de las fichas conviene que alguien los verifique:
- **CTR-502:** la fecha de su informe final y acta de liquidación quedó en 2027-12-31, la terminación que fija el otrosí OT-1. El contrato dice «a la terminación»; es una elección mía, no un dato del documento.
- **CTR-506:** la cláusula 5 dice «el de agosto» pero fija el 2026-07-06. Lo registré tal cual, sin corregirlo.

La salida completa quedó en `estado-legal/900000001-distribuidora-control/corridas/salida-legal-setup.md`. El reporte del motor está en `estado-legal/900000001-distribuidora-control/contratos/reporte-obligations-calendar.md`.