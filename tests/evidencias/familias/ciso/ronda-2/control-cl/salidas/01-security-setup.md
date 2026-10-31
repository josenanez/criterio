# /criterio-security:security-setup seguridad/966778890-aseguradora-control-sintetica

Alexis quedó instalado sobre Aseguradora Control Sintética (966778890). El reporte del periodo 2026-10 está hecho y la corrida quedó registrada. Falló una cosa: `marcar-raiz` no dejó la marca `_CRITERIO_SEGURIDAD.txt` en la carpeta raíz.

**Error de `marcar-raiz`:** el motor terminó con `KeyError: 'ciso'` en `raiz.py`. No creé la marca a mano, así que la carpeta queda sin ella.

**Lo que se hizo**
- **Carpeta raíz:** tomé la del argumento, `seguridad/966778890-aseguradora-control-sintetica`.
- **Excluido, sin abrir:**
  - `00-referencia/credenciales-vpn.txt`
  - `10-controles/A.8.24_certificados/servidor-web.pem`
  - `90-continuidad/respaldo-correo-2026-06-20.zip`
- **Fuera de lugar:** `80-revisiones/INC-ACS-101_revision.md` iría en `70-incidentes/`. No lo moví.
- **No soportados por el motor:** los tres `escaneo-*.json.gz`. Quedan para el trabajo de vulnerabilidades.
- **Términos 1.3:** quedaron aceptados a nombre de José Francisco Ñáñez, fecha 2026-10-15. El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Configuración:** la escribí en `.criterio/seguridad/966778890/config.json`. Las columnas de la declaración de aplicabilidad (Control, Nombre, Aplicable, Estado, Responsable, Periodicidad, Justificación) y de las tablas de sistemas, terceros y riesgos son las estándar, así que `columns` quedó vacío. `config` la validó sin problemas.
- **Ficha del periodo 2026-10:** lleva 13 evidencias de controles, 4 revisiones de accesos y 3 evaluaciones de terceros. Dejé `A.8.28_borrador-guia-codificacion.docx` fuera por ser un borrador sin aprobar.

**Qué dice el reporte**
- "Lo que hay que atender" sale vacío: nada abierto en lo que procesa este comando.
- A.8.28 (Codificación segura) figura "En implementación", sin evidencia.
- Al 2026-10-15, A.8.16 (Actividades de seguimiento) vence el 2026-10-16. A.8.7, A.8.8, A.8.13 y A.8.15 vencen el 2026-10-31.
- La sección "Fuentes" del reporte dice "Sin documentos citados", aunque la ficha sí cita cada documento.

Hice 6 preguntas, todas con la respuesta sugerida por los documentos.

Archivos en `estado-seguridad/966778890-aseguradora-control-sintetica/`:
- `seguridad/2026-10/reporte-control-evidence.md`
- `seguridad/2026-10/ficha.json`
- `corridas/salida-security-setup.md`