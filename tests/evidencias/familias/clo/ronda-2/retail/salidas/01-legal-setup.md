# /criterio-legal:legal-setup legal/900765432-almacenes-caribe

Fidel quedó instalado sobre Almacenes Caribe (NIT 900765432). Procesó los 6 contratos, CTR-301 a CTR-306, y el motor encontró 5 señales. La corrida quedó registrada como `2026-10-06-legal-setup-1`.

**Lo que hay que atender hoy (2026-10-06)**
- **CTR-303 (arrendamiento de la sede, 240.000.000):** vence el 2026-11-25, en 50 días, y no hay decisión registrada de renovar o terminar. Esa decisión es de una persona.

**Las otras 4 señales**
Solo tengo el conteo, porque el calendario no las detalla. Son: una firma sin facultad, un pago después de la terminación, una garantía que vence antes de lo exigido y un registro que no coincide con los documentos. El detalle sale con `/authority-check`, `/contract-execution` y `/contract-register`, que no corrí en esta sesión. El registro trae además CTR-309 (Publicidad Exterior), que no tiene carpeta de documentos. El motor marcó una señal de registro que no coincide, pero no sé si es esa.

**Qué se hizo**
- **Respuestas sugeridas:** como nadie podía contestar, tomé las respuestas sugeridas de los documentos. La entidad es Almacenes Caribe, NIT 900765432, Colombia. El aviso es de 60 días para vencimientos y 30 para preavisos, y el certificado puede tener hasta 30 días de antigüedad. El estado está en `estado-legal/900765432-almacenes-caribe`, fuera de los documentos.
- **Términos:** los mostré tal cual y registré la aceptación de José Francisco Ñáñez, versión 1.2, fecha 2026-10-06. El comprobante está en `.criterio/terminos/` (Markdown y PDF).
- **Marca de la carpeta:** dejé `_CRITERIO_LEGAL.txt` en `legal/900765432-almacenes-caribe`, autorizado a nombre de José Francisco Ñáñez. Fue la respuesta sugerida y nadie la confirmó, así que conviene que confirme si la quiere ahí.
- **Configuración:** `.criterio/legal/900765432/config.json`, validada sin problemas.
- **Fichas:** convertí los 29 documentos, sin ninguno ilegible. Escribí las 6 fichas a mano desde los contratos, con su cita. No hubo `record_issues`.
- **Salida y reporte:** lo que mostré está en `estado-legal/900765432-almacenes-caribe/corridas/salida-legal-setup.md`. El reporte del motor es `contratos/reporte-obligations-calendar.md`, en esa misma carpeta.

**Notas sobre las fichas**
- **CTR-302:** la ficha lleva el valor original (160.000.000) y el otrosí OT-1 por separado. El registro dice 440.000.000, que ya incluye el otrosí.
- **Informe final y acta de liquidación (OBL-2):** el contrato dice "a la terminación" sin fecha propia. Le puse la fecha de terminación vigente de cada contrato; en CTR-302 es la del otrosí, 2027-12-31.
- **Firmas de la contraparte:** los documentos traen "Representante de [empresa]" y no un nombre propio, y así quedaron en las fichas.