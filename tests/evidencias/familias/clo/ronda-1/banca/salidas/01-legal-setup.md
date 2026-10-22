# /criterio-legal:legal-setup legal/900123456-banco-andino

Fidel quedó instalado sobre Banco Andino (NIT 900123456): leí los 6 contratos, armé su ficha y el cálculo dio 5 señales. Nadie respondió las preguntas, así que tomé las respuestas sugeridas por los documentos.

**Lo que hay que atender hoy (2026-10-06):**
- **CTR-104, informe mensual atrasado:** el informe mensual venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`. Lleva 31 días.
- **CTR-104, preaviso cerca:** tiene renovación automática y el preaviso de no renovación vence el 2026-11-01, en 26 días. Nadie ha decidido.
- **Firma sin facultad:** 1 contrato.
- **Garantía faltante:** 1 contrato.
- **Registro distinto del contrato:** 1 contrato.

El calendario solo detalla las dos primeras. Las otras tres están contadas, pero no vi cuáles contratos son. Las detallan `/authority-check`, `/contract-execution` y `/contract-register`.

**Configuración:**
- **Entidad:** Banco Andino, NIT 900123456, Colombia (COP).
- **Plazos:** aviso a 60 días para vencimientos y 30 para preavisos; certificado de la contraparte de máximo 30 días.
- **Matriz de atribuciones:** ya existía, con 3 firmantes, así que el chequeo de facultades quedó activo.
- **Términos:** versión 1.2, aceptada a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante quedó en `.criterio/terminos/` en Markdown y PDF.
- **No dejé la marca `_CRITERIO_LEGAL.txt`:** es lo único que un agente escribe dentro de los documentos y nadie la autorizó.

**Dos datos que registré tal como están escritos y que una persona debería mirar:**
- La cláusula 5 dice «el de agosto, a más tardar el 2026-09-05», y en CTR-106 dice «el de agosto, a más tardar el 2026-07-06». Usé la fecha escrita como fecha de la obligación.
- Los documentos no numeran la obligación de liquidación de la cláusula 6. La llamé OBL-2, con vencimiento en la terminación del contrato. Es una deducción mía; el contrato solo dice «a la terminación».

**Archivos** (en `estado-legal/900123456-banco-andino/`):
- Las 6 fichas están en `contratos/` y el cálculo en `contratos/resultados.json`.
- El calendario está en `contratos/reporte-obligations-calendar.md`.
- Lo que te mostré quedó en `corridas/salida-legal-setup.md`, y la corrida está registrada como `2026-10-06-legal-setup-1`.
- La configuración está en `.criterio/legal/900123456/config.json`.