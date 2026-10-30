# /criterio-legal:legal-setup legal/3101612904-almacenes-de-la-meseta

Fidel quedó instalado sobre Almacenes de la Meseta (3101612904, CR, colones). Procesé los 7 contratos con la fecha de prueba 2026-10-06.

**Lo que hay que atender hoy**
- **CTR-3703** (Centro Comercial del Oeste, arrendamiento de la sede principal) vence el 2026-11-25, en 50 días, y no tiene una decisión de renovar o terminar. El contrato dice que no se prorroga solo. La decisión es de una persona.
- **CTR-3705** termina el 2026-11-20, en 45 días. Hay un acta del comité del 2026-09-18 que decidió renovarlo.
- **CTR-3701**: el reporte de operaciones al oficial de cumplimiento vencía el 2026-09-30. Está entregado ese mismo día.

**Otras señales.** El cálculo dio 5 señales en total. Las otras 4 son una firma sin facultad, una garantía faltante y dos diferencias entre el registro y los contratos. Todavía no sé cuáles son. Salen al correr `authority-check`, `contract-register` y `contract-execution`.

**Qué dejé hecho**
- **Configuración:** `.criterio/legal/3101612904/config.json`, validada sin problemas.
- **Términos:** aceptados a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Fichas:** las 7 fichas están en `estado-legal/3101612904-almacenes-de-la-meseta/contratos/` y el motor no reportó observaciones sobre ellas. Cada dato lleva su cita al contrato o a la póliza.
- **Registro de la corrida:** `estado-legal/3101612904-almacenes-de-la-meseta/corridas/salida-legal-setup.md`.

**Qué decidí por mi cuenta, porque nadie respondió**
- **Umbrales:** usé los de `config.example.json` (aviso de vencimiento a 60 días, de preaviso a 30, certificado de la contraparte hasta 30 días).
- **Tipo de entidad:** la marqué como privada, sin contratación pública.
- **Feriados:** la lista quedó vacía, porque no tenía los de Costa Rica.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie lo autorizó.
- **Fichas:** dejé vacíos el monto y la fecha de entrega de las pólizas, porque no aparecen en los documentos.

**Sin hacer:** no dejé el reporte `obligations-calendar` copiado entero en este mensaje. Está en `estado-legal/3101612904-almacenes-de-la-meseta/contratos/reporte-obligations-calendar.md`. Tampoco hice preguntas sobre las matrices ni sobre carpetas fuera de estructura, porque el inventario no encontró ninguna.