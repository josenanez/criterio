# /criterio-legal:legal-setup legal/88457812-7-banco-del-tebicuary-sintetico

Fidel quedó instalado sobre Banco del Tebicuary Sintético (RUC 88457812-7, Paraguay, PYG) y procesó sus 6 contratos. El motor encontró 5 señales; el calendario muestra 2.

- **Preguntas:** nadie respondió, así que tomé las respuestas sugeridas de los documentos. Quedó con avisos de 60 días para un vencimiento y 30 para un preaviso. El certificado de la contraparte puede tener 30 días de antigüedad al firmar. La entidad no es pública, porque es un banco privado. No dejé la marca `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarla.
- **Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 (versión 1.3), como pediste para esta prueba. El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Configuración:** `.criterio/legal/88457812-7/config.json`, validada sin problemas.
- **Fichas:** convertí 28 documentos, 0 ilegibles. Las 6 fichas quedaron en `estado-legal/88457812-7-banco-del-tebicuary-sintetico/contratos/`, sin `record_issues`.
- **Las 5 señales del motor:** facultad de firma, pagos sobre el valor, obligación vencida, preaviso cercano y garantía faltante. Del calendario, lo que hay que atender es:
  - **CTR-4404, informe mensual:** el informe de agosto venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`.
  - **CTR-4404, preaviso:** vence el 2026-11-01, en 26 días, y nadie decidió.
  - **Otros vencimientos:** el calendario también lista las terminaciones de CTR-4405 (2026-11-20), CTR-4403 y CTR-4404 (2026-12-31).
- **Para que lo revise una persona:**
  - CTR-4405 y CTR-4406 traen el mismo RUC de contraparte, 88440006-9, aunque son empresas distintas.
  - El informe mensual «de agosto» de CTR-4406 tiene fecha límite 2026-07-06, anterior a agosto.
  - Registré ambos tal cual.
- **Corrida registrada:** `2026-10-06-legal-setup-1`, con 5 hallazgos.

El calendario completo está en `estado-legal/88457812-7-banco-del-tebicuary-sintetico/contratos/reporte-obligations-calendar.md`, y lo que te mostré en `corridas/salida-legal-setup.md`.