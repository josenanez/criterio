# /criterio-legal:legal-setup legal/45678912000155-empresa-publica-paulista

Fidel quedó instalado sobre Empresa Pública Paulista (CNPJ 45678912000155). Procesé los 6 contratos y no hubo `record_issues`. La corrida quedó registrada con 4 hallazgos.

**Hallazgos** (al 2026-10-06):
- **CTR-2402:** no hay constancia de publicación en el PNCP, y la ley pedía hacerlo a más tardar el 2025-07-24.
- **CTR-2404:** se publicó el 2026-03-13, y el plazo era el 2026-03-10.
- **CTR-2403:** la garantía es de 72.000,00 y el tope legal es 45.000,00, sin justificación en el contrato.
- **CTR-2406:** la garantía es de 60.000,00 y el tope legal es 37.500,00, sin justificación en el contrato.

**Calendario de obligaciones:**
- **CTR-2401:** el informe de compliance (OBL-3) venció el 2026-09-30 y su evidencia está entregada.
- **CTR-2405:** termina el 2026-11-20, en 45 días. El comité decidió renovarlo el 2026-09-18.
- **CTR-2403:** termina el 2026-12-31, en 86 días.

La decisión de renovar o terminar es de una persona.

**Qué hice, sin pregunta a la persona:**
- **Entidad:** Brasil, BRL, pública bajo la ley de licitaciones y publica en el PNCP.
- **Umbrales:** 60 y 30 días de aviso, y 30 días de antigüedad máxima del certificado.
- **Garantía:** sin umbral, porque no aplica a Brasil.
- **Términos 1.3:** aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes en Markdown y PDF quedaron en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie autorizó escribir en los documentos.
- **Estructura:** `00-referencia/politica-contratacao.md` iría en `20-politicas/`. No lo moví.

**Dónde quedó todo:**
- **Configuración:** `.criterio/legal/45678912000155/config.json`
- **Fichas:** `estado-legal/45678912000155-empresa-publica-paulista/contratos/`
- **Reporte:** `estado-legal/45678912000155-empresa-publica-paulista/contratos/reporte-obligations-calendar.md`
- **Salida de la corrida:** `estado-legal/45678912000155-empresa-publica-paulista/corridas/salida-legal-setup.md`