# /criterio-security:security-setup seguridad/965123456-seguros-del-sur-sinteticos

Alexis quedó instalado sobre Seguros del Sur (sintéticos), 965123456, y la primera ficha del periodo 2026-10 está calculada con fecha de corte 2026-10-15. Quedó la configuración, la aceptación de términos, la ficha y el reporte, y la corrida está registrada.

**Lo que hay que atender, en el reporte de controles:**
1. **A.8.15 Registro de eventos** figura como «Implementado» y no tiene ninguna evidencia de que operó. El responsable es el Oficial de cumplimiento.
2. **A.5.18 Derechos de acceso** tiene su evidencia más reciente del 2026-06-30. Su periodicidad es de 92 días y venció el 2026-09-30, hace 15 días. El responsable es el Jefe de infraestructura.

El motor encontró 8 señales en total en el periodo. Las 6 de otros comandos quedan para sus reportes:
- Una aceptación de riesgo vencida.
- Dos revisiones de accesos vencidas.
- Dos evaluaciones de terceros vencidas.
- Un control sin responsable.

**Lo que no abrí:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`. Conviene sacarlos de la carpeta de evidencia. Tampoco moví nada. El inventario dice que las tres revisiones de `80-revisiones/` irían en `70-incidentes/`.

**Cómo resolví lo que no se podía preguntar:**
- La carpeta venía en el argumento.
- Acepté los términos versión 1.3 a nombre de José Francisco Ñáñez, 2026-10-15. Dejé el comprobante en `.criterio/terminos/`.
- No dejé la marca `_CRITERIO_SEGURIDAD.txt` porque nadie la autorizó.
- Puse Chile y CLP porque la carpeta es de una aseguradora chilena y las notificaciones van a la CMF. No lo confirmó nadie.
- El borrador de guía de codificación (A.8.28) lo dejé fuera de la evidencia por no estar aprobado.

**Archivos:**
- `.criterio/seguridad/965123456-seguros-del-sur-sinteticos/config.json`
- `estado-seguridad/965123456-seguros-del-sur-sinteticos/seguridad/2026-10/reporte-control-evidence.md`
- `estado-seguridad/965123456-seguros-del-sur-sinteticos/corridas/salida-security-setup.md`