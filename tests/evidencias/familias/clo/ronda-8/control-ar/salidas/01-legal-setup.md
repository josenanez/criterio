# /criterio-legal:legal-setup legal/30702173554-comercial-control-del-plata

La instalación de Fidel quedó lista para Comercial Control del Plata (CUIT 30702173554). Los seis contratos están procesados y no hay nada abierto en el calendario.

**Lo que hice en esta sesión sin interfaz** (nadie respondió, así que tomé las respuestas de los documentos):
- **Configuración:** `.criterio/legal/30702173554/config.json`, con país AR y moneda ARS. El motor la validó sin problemas.
- **Avisos y certificado:** usé los valores de `config.example.json` (60 días de aviso por vencimiento, 30 por preaviso, certificado de máximo 30 días). Los puse por defecto porque nadie contestó.
- **Entidad pública:** puse que no, porque ningún documento dice lo contrario.
- **Términos:** aceptados a nombre de José Francisco Ñáñez el 2026-10-06 (versión 1.3). Los comprobantes están en `.criterio/terminos/` en Markdown y PDF.
- **Marca de la raíz:** no escribí `_CRITERIO_LEGAL.txt`, porque nadie la autorizó.
- **Fichas:** las seis están en `estado-legal/30702173554-comercial-control-del-plata/contratos/` y no tienen `record_issues`.

**Calendario al 2026-10-06** (cifras del motor):
- **Vencido:** el reporte de operaciones del contrato CTR-2701 (OBL-3) vencía el 2026-09-30 y está a 6 días atrás. Hay evidencia entregada.
- **Terminación del CTR-2705:** 2026-11-20, a 45 días. El acta del comité del 2026-09-18 decidió renovarlo.
- **Terminación del CTR-2703:** 2026-12-31, a 86 días.
- **Informe final y acta de liquidación:** vencen ese mismo día en ambos contratos y no tienen evidencia todavía.

**Para que una persona verifique:** los contratos CTR-2704 (Software Control S.R.L.) y CTR-2705 (Asesores Control S.R.L.) traen el mismo CUIT, 30702700058. Lo registré tal como está en cada documento.

La corrida quedó registrada como `2026-10-06-legal-setup-1`. La salida completa está en `estado-legal/30702173554-comercial-control-del-plata/corridas/salida-legal-setup.md` y el calendario en `estado-legal/30702173554-comercial-control-del-plata/contratos/reporte-obligations-calendar.md`.