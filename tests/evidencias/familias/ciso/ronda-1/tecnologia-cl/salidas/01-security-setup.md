# /criterio-security:security-setup seguridad/76543210k-nube-austral-software-sintetica

La instalación quedó lista para Nube Austral Software Sintética (76543210k, periodo 2026-10, corte 2026-10-15). `control-evidence` encontró dos señales y la corrida quedó registrada.

**Lo que dejé escrito**
- La configuración está en `.criterio/seguridad/76543210k/config.json` y `config` la validó sin problemas.
- José Francisco Ñáñez aceptó los términos 1.3 para esta prueba. Los comprobantes están en `.criterio/terminos/`.
- Cargué en la ficha 12 evidencias de control, 3 revisiones de accesos y 3 evaluaciones de terceros.
- Lo que te mostré quedó guardado en `corridas/salida-security-setup.md`.
- Sin interfaz, tomé la respuesta sugerida en cada pregunta. No dejé la marca `_CRITERIO_SEGURIDAD.txt`, porque la ruta vino en el argumento.

**Lo que no abrí**
- `credenciales-vpn.txt`, por su nombre.
- `servidor-web.pem`, por ser una llave.
- `respaldo-correo-2026-06-20.zip`, por ser un respaldo.

**Lo que muestra el reporte `control-evidence`**
1. **A.8.15, Registro de eventos:** figura como Implementado y la ficha no tiene ninguna evidencia de que operó.
2. **A.5.18, Derechos de acceso:** la evidencia más reciente es del 2026-06-30 y su periodicidad es de 92 días. Venció el 2026-09-30, hace 15 días.

El reporte no declara ningún control cumplido.

**Otras señales que `compute` contó**
- `compute` contó 8 señales en total. Las otras 6 son: 2 revisiones de accesos vencidas, 2 evaluaciones de terceros vencidas, 1 aceptación de riesgo vencida y 1 control aplicable sin responsable.
- No las miré una por una; entran en los reportes de los otros comandos.
- El control sin responsable es A.8.24: la declaración de aplicabilidad no trae responsable para él.

**Pendiente**
- El borrador de A.8.28 va a `reviewed` y no cuenta como evidencia.
- Las revisiones de `80-revisiones/` de INC-NUB-101, 102 y 103 están fuera de lugar (irían en `70-incidentes/`). No moví nada.

El reporte está en `estado-seguridad/76543210k-nube-austral-software-sintetica/seguridad/2026-10/reporte-control-evidence.md`.