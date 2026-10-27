# /criterio-legal:legal-setup legal/CCM120615R59-comercial-control-centro

Dejé a Fidel instalado sobre Comercial Control Centro (RFC CCM120615R59, México, MXN), con fecha de corte 2026-10-06. Procesó los 6 contratos y no encontró vencimientos ni preavisos abiertos. El chequeo de facultades, los pagos y las garantías no corrieron: son los comandos `authority-check` y `contract-execution`.

**Lo que se hizo**
- **Configuración:** `.criterio/legal/CCM120615R59/config.json`. El motor la validó sin problemas. Usé los umbrales de `config.example.json`: 60 días para vencimientos, 30 para preavisos y 30 para la antigüedad del certificado. En esta prueba nadie respondió las preguntas, así que tomé las respuestas sugeridas.
- **Términos:** mostré el `en_corto` de la versión 1.2 y registré la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes están en `.criterio/terminos/`, en Markdown y PDF.
- **Fichas:** convertí 29 documentos, sin ilegibles, y escribí las 6 fichas (CTR-1501 a CTR-1506) en `estado-legal/CCM120615R59-comercial-control-centro/contratos/`. El motor no reportó `record_issues`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarla en esta prueba. No se movió ni se creó nada dentro de los documentos.

**Qué encontró el calendario**
- CTR-1501: el reporte de operaciones al oficial de cumplimiento (OBL-3) vencía el 2026-09-30 y está entregado, con evidencia.
- CTR-1505: termina el 2026-11-20, en 45 días, y su informe final y acta de liquidación (OBL-2) vence ese día, sin evidencia todavía. Hay un acta del comité del 2026-09-18 que decide renovarlo, y la registré como decisión con su cita.
- CTR-1503: termina el 2026-12-31, en 86 días, y su OBL-2 también está sin evidencia todavía.

La decisión de renovar o terminar es de una persona.

Todo quedó registrado en `salida-legal-setup.md` (carpeta `corridas/` del estado), y la corrida es la `2026-10-06-legal-setup-1`.