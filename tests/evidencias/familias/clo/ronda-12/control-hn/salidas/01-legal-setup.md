# /criterio-legal:legal-setup legal/08010007330150-comercial-control-de-honduras

Fidel quedó instalado sobre Comercial Control de Honduras (RTN 08010007330150) y procesó los 6 contratos, CTR-4201 a CTR-4206. El motor no marcó ninguna señal.

Lo que muestra el calendario al 2026-10-06:
- **CTR-4201:** el reporte de operaciones al oficial de cumplimiento (OBL-3) vencía el 2026-09-30 y tiene evidencia entregada ese día.
- **CTR-4205:** termina el 2026-11-20, en 45 días, y tiene pendiente el informe final y el acta de liquidación. El acta del comité del 2026-09-18 decidió renovarlo. Esa decisión consta solo como registro de lo que dice el acta.
- **CTR-4203:** termina el 2026-12-31, en 86 días, con el informe final y el acta de liquidación pendientes.

El calendario no mostró vencimientos ni preavisos de los otros contratos dentro de la ventana de 30 días atrás y 90 adelante. No revisé las comparaciones de firma contra la matriz ni los pagos contra lo pactado, porque el motor no devolvió señales de esos puntos. Los pagos están en `10-registro/pagos-2026-09-30.csv` y esta instalación no los cruzó.

Nadie contestó preguntas, así que tomé estas respuestas de los documentos:
- **Entidad:** Honduras, en lempiras (HNL), no pública.
- **Avisos:** 60 días para vencimientos y 30 para preavisos, los valores de `config.example.json`.
- **Certificado de la contraparte:** 30 días de antigüedad máxima.
- **Términos:** versión 1.3, aceptada a nombre de José Francisco Ñáñez el 2026-10-06, con comprobante en `.criterio/terminos/`.
- **Marca de la carpeta:** dejé `_CRITERIO_LEGAL.txt` en la carpeta raíz, con la respuesta sugerida de la prueba, que era sí. Es lo único que escribí dentro de los documentos.

Los archivos quedaron en tres lugares:
- **Configuración:** `.criterio/legal/08010007330150/config.json`
- **Estado:** `estado-legal/08010007330150-comercial-control-de-honduras`. Allí están las 6 fichas, el reporte del calendario y la salida de esta corrida (`corridas/salida-legal-setup.md`).
- **Registro de la corrida:** `2026-10-06-legal-setup-1`, registrada con 0 hallazgos.