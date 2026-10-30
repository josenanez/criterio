# /criterio-resilience:resilience-setup seguridad/tba110315k21-tiendas-del-bajio-sinteticas

Amparo quedó instalada para Tiendas del Bajío Sintéticas (TBA110315K21), con la fecha de prueba 2026-10-15 y el periodo 2026-10. La primera ficha tiene 6 incidentes, 3 revisiones y 4 pruebas, y el motor encontró 8 señales.

**Configuración.** Quedó en `.criterio/resiliencia/tba110315k21/config.json`. No hubo preguntas: tomé las respuestas de los documentos.
- **Contención:** crítica 6 h, alta 24 h, media 72 h y baja 168 h, según la política de respuesta a incidentes (versión 2, sección 5).
- **Revisión posterior:** 15 días (sección 7 de la política).
- **Notificaciones y calendario:** la matriz y el calendario de continuidad los lee el motor directo de `00-referencia/`.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez el 2026-10-15, con comprobante en `.criterio/terminos/`.

**No abrí tres archivos:**
- `credenciales-vpn.txt` es una credencial.
- `servidor-web.pem` es una llave.
- `respaldo-correo-2026-06-20.zip` es un respaldo.

No dejé la marca `_CRITERIO_SEGURIDAD.txt` en la carpeta, porque nadie la autorizó. Las tres revisiones de `80-revisiones/` están fuera de lugar (irían en `70-incidentes/`); no las moví.

**Señales del motor:**
- **Contención tardía (2):** INC-TDA-102 se contuvo en 30 horas y la política da 24. INC-TDA-106 sigue sin contención registrada y su plazo es de 24 horas.
- **Sin revisión posterior (1):** INC-TDA-105 se cerró el 2026-08-25 y no tiene revisión; la política da 15 días.
- **Notificaciones tardías (2), pruebas de continuidad vencidas (1) y pruebas de restauración vencidas (2):** el motor las cuenta, pero el reporte de línea de tiempo no las detalla. Se ven en los reportes de notificaciones y de pruebas de continuidad, que no corrí.

Quién notifica, quién contiene o quién hace una prueba lo decide una persona. Amparo no ejecuta nada de eso.

La corrida quedó registrada como `2026-10-15-resilience-setup-1`.

Archivos están en `estado-seguridad/tba110315k21-tiendas-del-bajio-sinteticas/`:
- `resiliencia/2026-10/ficha.json`
- `resiliencia/2026-10/reporte-incident-timeline.md`
- `corridas/salida-resilience-setup.md`