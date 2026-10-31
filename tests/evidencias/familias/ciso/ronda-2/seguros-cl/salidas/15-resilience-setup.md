# /criterio-resilience:resilience-setup seguridad/965123456-seguros-del-sur-sinteticos

Amparo quedó instalada sobre Seguros del Sur (965123456). Como nadie respondió, usé como respuesta suya lo que dicen los documentos. Un comando falló con la primera ficha, y lo corregí y volví a correr.

- **Configuración:** `.criterio/resiliencia/965123456/config.json`. Los plazos salen de `politica-respuesta-incidentes.docx` (versión 2), secciones 5 y 7:

  | Severidad | Horas para contener |
  |---|---|
  | crítica | 4 |
  | alta | 12 |
  | media | 48 |
  | baja | 120 |

  La revisión posterior es a 14 días calendario tras el cierre.
- **Excluidos, no abiertos:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`. Conviene sacarlos de la carpeta de evidencia.
- **Fuera de lugar:** las tres revisiones de `80-revisiones/` irían en `70-incidentes/`. No moví nada. Los tres `.gz` de `50-escaneos/` son del escáner de vulnerabilidades, no de Amparo.
- **Marca de la raíz:** no la creé, porque nadie autorizó crear `_CRITERIO_SEGURIDAD.txt`.
- **Términos 1.3:** los mostré tal cual y los registré a nombre de José Francisco Ñáñez, con fecha 2026-10-15. El comprobante está en `.criterio/terminos/` (`.md` y `.pdf`).
- **Primera ficha:** `estado-seguridad/965123456-seguros-del-sur-sinteticos/resiliencia/2026-10/ficha.json`, con 6 incidentes, 3 revisiones y 4 pruebas. Calculé con `--today 2026-10-15`.

El motor marcó 8 señales:

| Señal | Cantidad |
|---|---|
| Incidentes con respuesta tardía | 2 |
| Notificaciones tardías | 2 |
| Pruebas de restauración vencidas | 2 |
| Prueba de continuidad vencida | 1 |
| Incidente sin revisión | 1 |

El reporte `incident-timeline` detalla tres:

- **INC-SEG-102:** se contuvo en 18 horas y la política da 12.
- **INC-SEG-106:** sigue sin contención registrada y la política da 12 horas.
- **INC-SEG-105:** se cerró el 2026-08-25 y no tiene revisión posterior; van 37 días con 14 de plazo.

Las notificaciones tardías y las pruebas vencidas no salen en ese reporte; salen con `/notifications` y `/continuity-tests`. En la ficha dejé una cosa sin cerrar: INC-SEG-104 tiene clientes afectados y la matriz pide notificarles, pero no hay constancia de esa notificación en `70-incidentes/`.

La salida de esta corrida está en `estado-seguridad/965123456-seguros-del-sur-sinteticos/corridas/salida-resilience-setup.md`, y la corrida quedó registrada como `2026-10-15-resilience-setup-1`.