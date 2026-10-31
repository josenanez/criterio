# /criterio-security:security-scan 

La ficha de 2026-10 ya traía todos los documentos de controles, accesos y terceros. Los revisé contra su texto y no había nada que agregar. El motor calculó 8 señales con fecha de corte 2026-10-15.

El reporte completo está en `estado-seguridad/965123456-seguros-del-sur-sinteticos/seguridad/2026-10/reporte-security-scan.md`. Las 8 señales:

1. **A.8.15, Registro de eventos:** figura «Implementado» y no tiene ninguna evidencia de que operó.
2. **Directorio activo:** la última revisión de accesos es del 2026-06-30 y tocaba el 2026-09-28 (17 días).
3. **R-03, Respaldo fuera de sitio a más de 24 horas:** el Comité de riesgos lo aceptó hasta el 2026-09-30 y no se volvió a revisar (15 días).
4. **Mesa de Ayuda Externa:** la última evaluación es del 2025-09-30 y tocaba el 2026-09-30 (15 días).
5. **Portal de clientes:** no hay ninguna revisión de accesos registrada.
6. **Centro de Datos Alterno:** tercero crítico sin ninguna evaluación de seguridad registrada.
7. **A.5.18, Derechos de acceso:** la evidencia más reciente es del 2026-06-30 y venció el 2026-09-30 (15 días).
8. **A.8.24, Uso de la criptografía:** aplicable y sin responsable en la declaración.

- **Excluidos sin abrir:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`.
- **Fuera de la ficha:** el borrador A.8.28 de la guía de codificación, porque está sin aprobar y no prueba que el control operó.
- **Términos:** la versión 1.3 ya estaba vigente, registrada a nombre de José Francisco Ñáñez el 2026-10-15.
- **Corrida registrada:** `2026-10-15-security-scan-1`, con la salida en `estado-seguridad/965123456-seguros-del-sur-sinteticos/corridas/salida-security-scan.md`.