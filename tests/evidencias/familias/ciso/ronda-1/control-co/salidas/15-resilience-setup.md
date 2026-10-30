# /criterio-resilience:resilience-setup seguridad/900777888-cooperativa-control-sintetica

Amparo quedó instalada sobre Cooperativa Control Sintética (900777888, CO). El motor no levantó ninguna señal.

**Qué no abrí.** Excluí tres archivos por su nombre o extensión: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.

**Cómo quedó la configuración.** Todas las respuestas las tomé de los documentos, porque nadie las contestó:
- **Plazos:** contención de 4, 24, 72 y 168 horas según la severidad, y revisión posterior a 15 días. Salen de las secciones 5 y 7 de la política de respuesta a incidentes v2.
- **Periodo:** 2026-10, igual que la ficha hermana de seguridad.
- **Matriz y calendario:** la matriz tiene 4 destinatarios y el calendario 5 pruebas, y el motor los lee de `00-referencia/`.
- **Términos v1.3:** los registré a nombre de José Francisco Ñáñez, con fecha 2026-10-15. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-resilience-0.1.0-2026-10-15.md` y `.pdf`.
- **Marca de la raíz:** no dejé `_CRITERIO_SEGURIDAD.txt`, porque nadie lo autorizó.

**Primera ficha** (`estado-seguridad/…/resiliencia/2026-10/ficha.json`):
- **Incidente:** INC-CTL-101, crítico. Lo contuvieron en 3,50 horas, con 4,00 de plazo. Lo cerraron el 2026-09-08 y su revisión es del 2026-09-12.
- **Pruebas:** registré las cinco del calendario. La del core de la cooperativa (2026-08-01) salió "con observaciones"; las otras cuatro, exitosas.
- **Notificaciones:** hay constancia de la Superintendencia Financiera y del Comité de riesgos.

**Para que una persona lo confirme:**
- El archivo de la revisión (`80-revisiones/INC-CTL-101_revision.md`) trae la fecha, pero ninguna lección ni acción escrita. Está en `80-revisiones/`, no en `70-incidentes/`; no lo moví.
- Las respuestas a esas dudas las escribí yo y quedaron en la ficha, que mostró el reporte.

**Registro de la corrida:**
- El reporte `incident-timeline` quedó en `estado-seguridad/…/resiliencia/2026-10/reporte-incident-timeline.md`.
- Lo que te mostré está en `estado-seguridad/…/corridas/salida-resilience-setup.md`.
- La corrida quedó registrada como `2026-10-15-resilience-setup-1`.