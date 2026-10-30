# /criterio-vulnerability:vuln-setup seguridad/tba110315k21-tiendas-del-bajio-sinteticas

La instalación quedó lista para Tiendas del Bajío Sintéticas (TBA110315K21): la configuración está validada, los términos están aceptados y la corrida quedó registrada. El motor encontró 9 señales abiertas, que están en el reporte.

- **Configuración:** `.criterio/vulnerabilidades/tba110315k21/config.json`. Los plazos salen de la sección 4 de la política (versión 3): crítica 15, alta 30, media 90 y baja 180 días. Las demás respuestas las tomé de los documentos; no hubo preguntas a la persona.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez con fecha 2026-10-15. Los comprobantes están en `.criterio/terminos/`.
- **Exportaciones:** las tres del escáner se reconocieron completas, sin columnas faltantes. El catálogo KEV no es una exportación y el motor lo procesa aparte.
- **Marca de la raíz:** no dejé `_CRITERIO_SEGURIDAD.txt`, porque nadie lo autorizó en esta sesión.
- **Señales del periodo 2026-10:**
  - 3 vulnerabilidades pasadas de plazo.
  - 1 del catálogo KEV vencida.
  - 1 excepción vencida (CVE-2099-12003 en tda-db-01).
  - 2 cierres sin reescaneo.
  - 2 activos sin escanear.
- **Reporte:** `estado-seguridad/tba110315k21-tiendas-del-bajio-sinteticas/vulnerabilidades/2026-10/reporte-vuln-sla.md`. No se publica en Rostrum.
- **Archivos excluidos:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`. Los tres siguen sin abrirse.
- **Falla del motor:** `convertir` generó un caché `.md` de `credenciales-vpn.txt`, aunque estaba excluido. Yo no lo leí. Conviene revisar `00-referencia/credenciales-vpn.txt.md` y borrarlo.
- **Archivos fuera de lugar:** las 3 revisiones de `80-revisiones/` irían en `70-incidentes/`. Es solo una sugerencia; no moví nada.

Todo lo mostrado quedó guardado en `estado-seguridad/tba110315k21-tiendas-del-bajio-sinteticas/corridas/salida-vuln-setup.md`.