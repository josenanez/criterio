# /criterio-resilience:resilience-setup seguridad/20599887766-distribuidora-control-sintetica

Amparo quedó instalada sobre Distribuidora Control Sintética (20599887766). La ficha de 2026-10 tiene 1 incidente, 1 revisión posterior y 5 pruebas de continuidad. El reporte `incident-timeline` no marca nada abierto.

**Qué hice**
- **Preguntas:** no hubo quién respondiera. Tomé las respuestas de los documentos.
- **Plazos de contención:** crítica 6 h, alta 24 h, media 72 h, baja 168 h. La revisión posterior es a 15 días. Salen de la política de respuesta a incidentes v2, secciones 5 y 7.
- **Matriz de notificaciones:**
  - Organismo supervisor de energía: incidentes críticos, 24 h.
  - Autoridad de protección de datos: datos personales, 72 h.
  - Clientes afectados: 72 h.
  - Comité de riesgos: todos los incidentes, 48 h.
- **Calendario de continuidad:** 5 pruebas.
- **Términos:** versión 1.3, registrados a nombre de José Francisco Ñáñez con fecha 2026-10-15. Los comprobantes quedaron en `.criterio/terminos/`, en Markdown y PDF.
- **Marca de la raíz:** no puse `_CRITERIO_SEGURIDAD.txt`, porque nadie pudo autorizarla.
- **Configuración:** `.criterio/resiliencia/20599887766/config.json`, y el motor la validó sin problemas.

**Lo que no abrí**
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

**Resultado**
- **INC-DCS-101:** ransomware, severidad crítica. Se contuvo en 5.50 h contra un plazo de 6.00 h. Se cerró el 2026-09-08 y tuvo revisión posterior el 2026-09-12.
- **Pruebas:** cuatro exitosas y la restauración del sistema comercial (2026-08-01) con observaciones.
- **Notificaciones:** las dejé en la ficha: el Comité de riesgos el 2026-09-03 a las 15:10 y el supervisor de energía el 2026-09-04 a las 09:10. Este comando no las compara con la matriz, así que no sé si llegaron a tiempo. Eso lo mira `notifications`.
- **Calendario:** `continuity-tests` es el comando que lo cruza con las fechas de las pruebas. No lo corrí.
- **Archivo fuera de lugar:** el motor marca `80-revisiones/INC-DCS-101_revision.md` como si debiera estar en `70-incidentes/`. No lo moví. La revisión sí quedó en la ficha, con su fecha.
- **Sin cita:** el reporte dice "Sin documentos citados", aunque la ficha trae las fuentes.

**Dónde quedó cada cosa**
- Reporte: `estado-seguridad/20599887766-distribuidora-control-sintetica/resiliencia/2026-10/reporte-incident-timeline.md`
- Salida de esta corrida: `estado-seguridad/20599887766-distribuidora-control-sintetica/corridas/salida-resilience-setup.md`
- Ficha: `estado-seguridad/20599887766-distribuidora-control-sintetica/resiliencia/2026-10/ficha.json`

Para leer el `.docx` de la política y el `.xlsx` de la matriz usé un script de apoyo en el directorio temporal de la sesión, porque `Read` no abre esos formatos.