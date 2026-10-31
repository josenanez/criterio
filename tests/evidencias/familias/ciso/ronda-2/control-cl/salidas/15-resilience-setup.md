# /criterio-resilience:resilience-setup seguridad/966778890-aseguradora-control-sintetica

Amparo quedó instalada sobre Aseguradora Control Sintética (966778890, CL), pero la marca de la carpeta raíz no se pudo crear. `marcar-raiz` falló con un error del motor (`KeyError: 'ciso'` en `raiz.py`: no conoce la familia CISO). No inventé el archivo `_CRITERIO_SEGURIDAD.txt`. Hay que corregir el motor para que el comando funcione.

- **Excluido sin abrir:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`.
- **Fuera de lugar:** `80-revisiones/INC-ACS-101_revision.md`. El motor sugiere `70-incidentes/`; la leí donde está y no la moví.
- **Plazos:** los tomé de la política de respuesta a incidentes, versión 2, §5 y §7. Contención: crítica 6 h, alta 24 h, media 72 h, baja 168 h. Revisión posterior a 15 días. La matriz de notificaciones y el calendario traían columnas que el motor reconoce, así que no hizo falta mapearlas.
- **Términos:** la versión 1.3 queda aceptada por José Francisco Ñáñez el 2026-10-15. El comprobante está en `.criterio/terminos/`.
- **Resultado:** `INC-ACS-101` (ransomware, crítica) se contuvo en 5,50 h con plazo de 6,00 h. Tiene su revisión posterior el 2026-09-12, dentro de los 15 días. Las 5 pruebas de continuidad están al día y el motor no detectó ninguna señal.
- **Notificación límite:** a la Comisión para el mercado financiero se notificó el 2026-09-04 09:10, justo 24 h después de la detección (2026-09-03 09:10). El motor no marca esa notificación como tardía.

Quedaron escritos:
- La configuración en `.criterio/resiliencia/966778890/config.json`.
- La ficha del periodo en `estado-seguridad/966778890-aseguradora-control-sintetica/resiliencia/2026-10/ficha.json`.
- El reporte en `estado-seguridad/966778890-aseguradora-control-sintetica/resiliencia/2026-10/reporte-incident-timeline.md`.
- Lo que te mostré, en `corridas/salida-resilience-setup.md`; la corrida quedó registrada como `2026-10-15-resilience-setup-1`.