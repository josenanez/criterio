# /criterio-legal:legal-setup legal/08010004578120-banco-de-occidente-sintetico

Fidel quedó instalado sobre Banco de Occidente Sintético (RTN 08010004578120). Las 6 fichas de contrato están hechas y no tienen incidencias de validación. El motor encontró 5 señales y registró la corrida (`2026-10-06-legal-setup-1`).

- **Carpeta y estado:** la carpeta de documentos es `legal/08010004578120-banco-de-occidente-sintetico`, con los 6 contratos, el registro y la matriz de atribuciones. La configuración quedó en `.criterio/legal/08010004578120/config.json` y las fichas en `estado-legal/08010004578120-banco-de-occidente-sintetico/contratos/`.
- **Datos de la entidad:** quedó como Honduras (HN), moneda HNL y entidad privada, sin garantía mínima por ley de contratación pública. Los avisos son a 60 días para vencimientos y 30 para preavisos, y el certificado de la contraparte puede tener hasta 30 días. Son los valores de `config.example.json`, porque nadie los contradijo.
- **Términos:** aceptó José Francisco Ñáñez, versión 1.3, el 2026-10-06. El comprobante, en Markdown y PDF, está en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos, porque en una sesión sin interfaz nadie lo autorizó.

El calendario de obligaciones, con corte al 2026-10-06, muestra dos cosas que atender:

1. **CTR-4001 (Sistemas Financieros de Occidente):** el plazo para avisar la no renovación venció el 2026-10-01 sin decisión registrada. El contrato se prorroga en sus términos el 2026-10-31.
2. **CTR-4004 (Licencias Digitales del Norte):** el informe mensual de agosto vencía el 2026-09-05 y no hay evidencia en `40-ejecucion/`. Lleva 31 días vencido.

Lo próximo en el calendario:
- **CTR-4001:** el informe final y el acta de liquidación, junto con la terminación, el 2026-10-31.
- **CTR-4005:** terminación e informe final el 2026-11-20. El comité de contratos decidió renovarlo el 2026-09-18.
- **CTR-4003:** terminación e informe final el 2026-12-31.

El motor también marcó tres señales que este comando no detalla: una firma sin facultad, pagos por encima del valor pactado y una garantía que vence antes de lo exigido. Salen con `authority-check` y `contract-execution`.

El texto completo de lo que te mostré, con el reporte del motor, está en `estado-legal/08010004578120-banco-de-occidente-sintetico/corridas/salida-legal-setup.md`.