# /criterio-legal:legal-setup legal/30718174607-banco-del-rio-de-la-plata-sintetico

Fidel quedó instalado sobre la entidad: procesó 6 contratos, escribió las 6 fichas y no quedó ningún `record_issues`. Dejé la corrida registrada.

**Lo que hice**
- **Carpeta:** usé `legal/30718174607-banco-del-rio-de-la-plata-sintetico`, que venía en el argumento.
- **Inventario:** hay 6 contratos, el registro y la matriz de atribuciones. No hay nada fuera de la estructura.
- **Configuración:** la escribí en `.criterio/legal/30718174607/config.json` y el motor la validó sin problemas. La entidad es Banco del Río de la Plata (sintético), AR, ARS, no pública. Los avisos son de 60 y 30 días, y el certificado de la contraparte puede tener hasta 30 días de antigüedad.
- **Términos:** mostré el texto de la versión 1.3 y registré la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante quedó en `.criterio/terminos/` en Markdown y PDF.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`. Es lo único que se escribe dentro de los documentos y no había quien lo autorizara.

**Lo que muestra el calendario al 2026-10-06**
- **CTR-2504, informe mensual vencido:** el informe venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`. Lleva 31 días vencido.
- **CTR-2504, preaviso:** el contrato se renueva solo, y el preaviso de no renovación vence el 2026-11-01, en 26 días. Nadie ha decidido.
- **CTR-2501:** el reporte al oficial de cumplimiento se entregó el 2026-09-30, a tiempo.
- **Próximos vencimientos:** CTR-2505 termina el 2026-11-20, y CTR-2503 y CTR-2504 terminan el 2026-12-31. Cada uno trae su informe final y acta de liquidación a esa fecha.

El motor también contó otras tres señales que el reporte del calendario no detalla:
- una firma sin facultad suficiente,
- una garantía faltante,
- un registro que difiere del contrato.

Se ven con `authority-check`, `contract-execution` y `contract-register`.

**Una nota sobre CTR-2505.** El comité decidió renovarlo el 2026-09-18, pero el contrato dice que no se prorroga automáticamente. Lo dejé registrado como decisión y no lo interpreté.

El reporte completo está en `estado-legal/30718174607-banco-del-rio-de-la-plata-sintetico/contratos/reporte-obligations-calendar.md`, y lo mostrado quedó en `corridas/salida-legal-setup.md`.