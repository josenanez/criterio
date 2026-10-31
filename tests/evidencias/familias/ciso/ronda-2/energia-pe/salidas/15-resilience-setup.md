# /criterio-resilience:resilience-setup seguridad/20587654321-energia-andina-sintetica

Amparo quedó instalada sobre Energía Andina Sintética (20587654321). El motor encontró 8 señales en el periodo 2026-10. El reporte `incident-timeline` solo muestra 3; las otras 5 (notificaciones tardías y pruebas vencidas) aún no se han visto en detalle.

Nadie respondió preguntas en esta sesión, así que tomé las respuestas sugeridas por los documentos.

**Lo que no se abrió.** Quedaron excluidos por ser credenciales, llaves o respaldos:
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

**Configuración.**
- **Plazos de la política (v2):** contención de 4 h para críticos, 24 h para altos, 72 h para medios y 168 h para bajos. La revisión posterior es a los 15 días.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez, con fecha 2026-10-15. Los comprobantes están en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_SEGURIDAD.txt` en la carpeta porque nadie lo autorizó.
- **Matriz de notificaciones y calendario de continuidad:** el motor los leyó de `00-referencia/` sin necesidad de registrar columnas aparte.
- **Ficha:** cargué en la del periodo 2026-10 los 6 incidentes, 3 revisiones y 4 pruebas. El motor no reportó problemas en el registro.

**Lo que hay que atender (del reporte `incident-timeline`):**
- **INC-ENA-102** (alta): se contuvo en 30 horas y la política da 24.
- **INC-ENA-106** (alta): detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas.
- **INC-ENA-105** (baja): cerrado el 2026-08-25 y sin revisión posterior; la política da 15 días y van 36.

El detalle de las notificaciones tardías y de las pruebas vencidas se ve con `/notifications` y `/continuity-tests`.

En `inventario`, las tres revisiones de `80-revisiones/` aparecen como "fuera de lugar" (el motor sugiere `70-incidentes/`). No moví nada.

**Dónde quedó todo.** El reporte está en `estado-seguridad/20587654321-energia-andina-sintetica/resiliencia/2026-10/reporte-incident-timeline.md`. Lo que te mostré está en `corridas/salida-resilience-setup.md`, y la corrida quedó registrada como `2026-10-15-resilience-setup-1`.