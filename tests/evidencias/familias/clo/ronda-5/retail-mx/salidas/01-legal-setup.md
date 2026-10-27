# /criterio-legal:legal-setup legal/TBA180912Q37-tiendas-del-bajio

Fidel quedó instalado para Tiendas del Bajío (TBA180912Q37). Procesé los 6 contratos, y el cálculo dejó 5 señales; el calendario solo muestra una.

- **Carpeta:** usé la ruta que venía en el argumento. Había 61 documentos: 6 contratos, 3 periodos de cumplimiento, el registro de contratos y la matriz de atribuciones. Nada estaba fuera de lugar.
- **Configuración:** `.criterio/legal/TBA180912Q37/config.json`, validada sin problemas. Entidad Tiendas del Bajío, MX, MXN. Avisos de 60 días para vencimientos y 30 para preavisos. Certificado de la contraparte con 30 días de antigüedad máxima. El estado quedó en `estado-legal/TBA180912Q37-tiendas-del-bajio`. Esos valores salen de `config.example.json`.
- **Preguntas:** no le hice ninguna a nadie; las 6 respuestas salen de los documentos y del ejemplo de configuración. Dejé la lista de festivos vacía porque el único festivo del ejemplo era de otro país.
- **Términos:** mostré los términos 1.2 tal cual y los registré a nombre de José Francisco Ñáñez, fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-legal-0.11.0-2026-10-06.md` (y `.pdf`).
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Nadie lo autorizó en esta sesión y es lo único que se escribiría ahí.
- **Fichas:** 6, una por contrato, sin `record_issues`.
- **Señales:** `signed_without_authority`, `renewal_notice_missed`, `unsigned_contract`, `payment_after_termination` y `register_mismatch`, una de cada una.

Del calendario de obligaciones, que es lo único que este comando muestra, lo que hay que atender es CTR-1401. Su preaviso de no renovación venció el 2026-10-01 sin una decisión registrada, y el contrato se prorroga en sus términos el 2026-10-31. Las otras cuatro señales se revisan con `/authority-check`, `/contract-execution` y `/contract-register`.

El reporte está en `estado-legal/TBA180912Q37-tiendas-del-bajio/contratos/reporte-obligations-calendar.md`. La salida completa y la corrida `2026-10-06-legal-setup-1` quedaron registradas en `estado-legal/TBA180912Q37-tiendas-del-bajio/corridas/`.