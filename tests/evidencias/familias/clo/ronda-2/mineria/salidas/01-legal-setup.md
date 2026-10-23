# /criterio-legal:legal-setup legal/0990054321001-minera-condor

Fidel quedó instalado sobre Minera Cóndor (RUC 0990054321001, Ecuador, USD) y las 6 fichas de contrato están hechas. El motor las procesó sin `record_issues` y encontró 4 señales.

Las 4 señales son:
- **Firma sin facultad:** 1.
- **Preaviso vencido:** 1.
- **Contrato sin la firma de la contraparte:** 1.
- **Garantía faltante:** 1.

El calendario solo detalla la del preaviso. Las otras tres se ven con `/authority-check` y `/contract-execution`, que no corrí.

**Qué vence.** El calendario trae una señal:
- **CTR-401:** el preaviso de no renovación venció el 2026-10-01 sin decisión registrada. El contrato se prorroga en sus términos el 2026-10-31.
- **Próximas terminaciones:**
  - CTR-401, 2026-10-31.
  - CTR-405, 2026-11-20.
  - CTR-403, 2026-12-31.
- **Al día:** el reporte de operaciones de CTR-401 (OBL-3), que vencía el 2026-09-30, tiene evidencia entregada.

La decisión de renovar o terminar es de una persona.

**Lo que decidí por mi cuenta, con el valor sugerido en cada pregunta:**
- **Países y avisos:** Ecuador y USD salen de los documentos. Dejé los avisos de `config.example.json`: 60 días para vencimientos, 30 para preavisos y 30 días de antigüedad máxima del certificado.
- **Dónde queda lo que se vaya encontrando:** `estado-legal/0990054321001-minera-condor`.
- **Marca en la carpeta:** dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos.
- **Matriz de atribuciones:** existe, así que el chequeo de facultades quedó activo.
- **Términos:** José Francisco Ñáñez aceptó los términos 1.2 el 2026-10-06, con comprobantes en Markdown y PDF.
- **Feriados:** no cargué ninguno. El ejemplo traía uno de otro país y los de Ecuador no están en los documentos.
- **Preguntas a la persona:** ninguna.

**Dónde quedó todo:**
- **Configuración:** `.criterio/legal/0990054321001/config.json`
- **Fichas:** `estado-legal/0990054321001-minera-condor/contratos/`
- **Calendario:** `estado-legal/0990054321001-minera-condor/contratos/reporte-obligations-calendar.md`
- **Salida de esta corrida:** `estado-legal/0990054321001-minera-condor/corridas/salida-legal-setup.md`

La corrida quedó registrada como `2026-10-06-legal-setup-1`.