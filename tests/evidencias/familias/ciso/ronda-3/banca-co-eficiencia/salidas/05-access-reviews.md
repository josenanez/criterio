# /criterio-security:access-reviews 

Dos de los cuatro sistemas tienen la revisión de accesos vencida o sin hacer. Los términos estaban vigentes (versión 1.5), así que pude generar el reporte.

- **Directorio activo:** la última revisión es del 2026-06-30 y tocaba el 2026-09-28, con 17 días de atraso.
- **Portal de clientes:** no tiene ninguna revisión registrada. La tabla pide una cada 180 días.
- **Core bancario y correo corporativo:** siguen dentro de plazo. Les toca el 2026-11-08 y el 2026-10-29.

Ambos sistemas vencidos tienen como responsable al Jefe de seguridad de la información. Quedan fuera tres archivos que el motor excluye por omisión porque son credenciales, llaves o respaldos: `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`. No los abrí.

- **Marca de la carpeta raíz:** el reporte dice que el motor falló al escribir `_CRITERIO_SEGURIDAD.txt` y que no quedó.
- **Aceptación de términos:** no la registré porque ya constaba aceptada en la versión 1.2.3.
- **Tarea programada:** no se creó.

El reporte completo está en `estado-seguridad/901555123-banco-cordillera-sintetico/seguridad/2026-10/reporte-access-reviews.md`. Guardé lo que te mostré en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-access-reviews.md`. La corrida quedó registrada como `2026-10-15-access-reviews-1`, con 8 hallazgos en el registro.