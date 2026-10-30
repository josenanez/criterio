# /criterio-legal:legal-setup legal/155731001-2-2016-banco-istmeno

La instalación para Banco Istmeño quedó lista y la corrida está registrada. Todo salió de los documentos y no hice preguntas a nadie.

**Lo que quedó escrito**
- La configuración está en `.criterio/legal/155731001-2-2016/config.json` y la validación no dio problemas.
- Los términos 1.3 los aceptó José Francisco Ñáñez para esta prueba, con fecha 2026-10-06. El comprobante quedó en `.criterio/terminos/`, en Markdown y en PDF.
- Se convirtieron 28 documentos y no hubo ilegibles. Se armaron las 6 fichas, de CTR-2901 a CTR-2906, y no quedó ningún `record_issues`.

**Respuestas que tomé de los documentos**
- La entidad es Banco Istmeño, RUC 155731001-2-2016, Panamá, en dólares.
- Los umbrales son los de `config.example.json`: 60 días para vencimientos, 30 para preavisos y 30 para la antigüedad del certificado.
- No la marqué como entidad pública, porque ningún documento la presenta bajo contratación pública.

**Lo que encontró el motor (5 señales)**
- **CTR-2901:** el plazo para avisar la no renovación venció el 2026-10-01 sin una decisión registrada. El contrato se prorroga el 2026-10-31 en sus términos.
- **CTR-2904:** el informe mensual de agosto venció el 2026-09-05 y no hay evidencia en la carpeta de ejecución.
- **Otras tres señales:** contrato sin firma de la contraparte, garantía faltante y pagos por encima del valor. El calendario no las detalla. Por el contenido de las fichas, el contrato sin firma sería CTR-2905, que está firmado solo por la entidad.
- **Pendiente de revisar:** no verifiqué cuáles contratos tienen la garantía faltante ni los pagos de más, y la nota de la corrida los menciona sin que el motor los haya confirmado aquí. Para eso están `/authority-check` y `/contract-execution`.

**Lo que no hice**
- No dejé el archivo `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Escribir ahí necesita un sí de la persona y en esta sesión no había quien lo diera.
- La carpeta también trae políticas, normativa, canal de denuncias y tres periodos de cumplimiento. Son de Constanza y no los toqué.

El reporte `obligations-calendar` lo generó el motor y quedó en `estado-legal/155731001-2-2016-banco-istmeno/contratos/reporte-obligations-calendar.md`. El texto completo de esta sesión está en `corridas/salida-legal-setup.md`, en la misma carpeta de estado.