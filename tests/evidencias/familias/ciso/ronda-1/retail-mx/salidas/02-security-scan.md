# /criterio-security:security-scan 

La ficha de 2026-10 ya traía los documentos nuevos, con fechas y citas que coinciden con los originales, así que no agregué nada. El motor encontró 8 señales. Los términos (versión 1.3) estaban vigentes y la aceptación de José Francisco Ñáñez del 2026-10-15 ya constaba en la configuración.

Corrí todo con `--today 2026-10-15`. El borrador `A.8.28` sigue anotado como revisado y no cuenta como evidencia.

| # | Señal | Qué |
|---|---|---|
| 1 | Control implementado sin evidencia | A.8.15 (Registro de eventos) figura «Implementado» y no tiene evidencia de que operó. |
| 2 | Revisión de accesos vencida | Directorio activo: la última fue el 2026-06-30 y tocaba el 2026-09-28 (17 días). |
| 3 | Aceptación de riesgo vencida | R-03 (respaldo fuera de sitio a más de 24 horas) estaba aceptada hasta el 2026-09-30 y no se volvió a revisar (15 días). |
| 4 | Evaluación de tercero vencida | Mesa de Ayuda Externa: la última fue el 2025-09-30 y tocaba el 2026-09-30 (15 días). |
| 5 | Revisión de accesos sin hacer | Portal de clientes no tiene ninguna revisión registrada. |
| 6 | Evaluación de tercero sin hacer | Centro de Datos Alterno, tercero crítico, no tiene ninguna evaluación registrada. |
| 7 | Evidencia vencida | A.5.18 (Derechos de acceso): la última evidencia es del 2026-06-30 y venció el 2026-09-30 (15 días). |
| 8 | Control sin responsable | A.8.24 (Uso de la criptografía) es aplicable y no tiene responsable. |

Tres archivos quedaron excluidos sin abrirse, por ser credenciales, llaves o respaldos: `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`.

Las preguntas que hizo la sesión (aceptar los términos y si se deja la marca `_CRITERIO_SEGURIDAD.txt`) ya estaban respondidas en la ficha. La corrida quedó registrada como `2026-10-15-security-scan-1`. El reporte está en `estado-seguridad/tba110315k21-tiendas-del-bajio-sinteticas/seguridad/2026-10/reporte-security-scan.md`.