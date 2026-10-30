# /criterio-security:security-scan 

Los documentos nuevos ya estaban en la ficha del periodo, así que no llevé ninguno. El borrador de la guía de codificación quedó anotado como no evidencia. El motor encontró 8 señales. El reporte completo está en `estado-seguridad/901555123-banco-cordillera-sintetico/seguridad/2026-10/reporte-security-scan.md`.

**Lo que hay que atender:**
1. **A.8.15, Registro de eventos:** figura «Implementado» en la declaración de aplicabilidad y no tiene ninguna evidencia de que operó.
2. **Directorio activo:** la última revisión de accesos es del 2026-06-30 y tocaba el 2026-09-28 (17 días de retraso).
3. **R-03, respaldo fuera de sitio a más de 24 horas:** el Comité de riesgos lo aceptó hasta el 2026-09-30 y no se volvió a revisar (15 días).
4. **Mesa de Ayuda Externa:** la última evaluación es del 2025-09-30 y tocaba el 2026-09-30 (15 días).
5. **Portal de clientes:** no tiene ninguna revisión de accesos registrada.
6. **Centro de Datos Alterno:** es un tercero crítico y no tiene ninguna evaluación de seguridad registrada.
7. **A.5.18, Derechos de acceso:** la evidencia más reciente es del 2026-06-30 y venció el 2026-09-30 (15 días).
8. **A.8.24, Uso de la criptografía:** es aplicable y no tiene responsable en la declaración.

**Lo que no se abrió:** el motor excluyó `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip` por ser credenciales, llaves o respaldos.

**Otras notas:**
- **Términos:** estaban vigentes con la aceptación de José Francisco Ñáñez del 2026-10-15, así que no hubo que registrarlos de nuevo.
- **Marca de carpeta:** no dejé la marca `_CRITERIO_SEGURIDAD.txt` en la carpeta de la entidad, porque en esta sesión sin interfaz nadie la autorizó.
- **Corrida registrada:** quedó como `2026-10-15-security-scan-1`, con la salida en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-security-scan.md`.