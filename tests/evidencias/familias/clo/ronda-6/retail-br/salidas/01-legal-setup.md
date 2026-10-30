# /criterio-legal:legal-setup legal/31452078000170-lojas-paulistas

Fidel quedó instalado sobre Lojas Paulistas (CNPJ 31452078000170, Brasil, BRL). Procesó los 6 contratos y la corrida quedó registrada como `2026-10-06-legal-setup-1`.

- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Preguntas:** no hice ninguna a la persona. Tomé las respuestas sugeridas de los documentos y las dije en una línea cada una:
  - Avisos con 60 días de anticipación para vencimientos y 30 para preavisos.
  - Certificado de la contraparte con 30 días de antigüedad máxima.
  - Estado guardado en `estado-legal/31452078000170-lojas-paulistas`.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarlo.
- **Fichas:** las 6 fichas están en `estado-legal/31452078000170-lojas-paulistas/contratos/` y no salió ningún `record_issues`.
- **Señales:** el motor marcó 5:
  - una firma sin facultad;
  - un contrato por vencer;
  - un pago posterior a la terminación;
  - una garantía que vence antes de lo exigido;
  - un registro que no cuadra.

El calendario solo muestra la del vencimiento: CTR-1703 vence el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar. Las otras cuatro salen con `/authority-check`, `/contract-execution` y `/contract-register`, que no corrí.

Cuando corrí el calendario, la obligación de compliance de CTR-1701 vencía el 2026-09-30 y estaba 6 días atrás, con su evidencia.

**Para que lo revise una persona:**
- La cláusula 5 de CTR-1706 dice «o de agosto, até 2026-07-06». Registré la fecha tal cual (2026-07-06), sin interpretarla.
- En CTR-1702 el otrosí OT-1 movió la terminación a 2027-12-31, y el informe final quedó con esa fecha.

El reporte está en `estado-legal/31452078000170-lojas-paulistas/contratos/reporte-obligations-calendar.md` y lo que mostré, en `corridas/salida-legal-setup.md`, en la misma carpeta de estado.