# /criterio-resilience:resilience-setup seguridad/ccm090101ab3-comercial-control-sintetica

La instalación quedó lista para Comercial Control Sintética (CCM090101AB3, MX, periodo 2026-10). La ficha y el reporte salieron sin ninguna señal.

- **Archivos excluidos:** no los abrí.
  - `00-referencia/credenciales-vpn.txt`
  - `10-controles/A.8.24_certificados/servidor-web.pem`
  - `90-continuidad/respaldo-correo-2026-06-20.zip`
- **Plazos de la política:** salen de `politica-respuesta-incidentes.docx`, versión 2.
  - Contención: crítica 6 h, alta 24 h, media 72 h, baja 168 h.
  - Revisión posterior: 15 días calendario tras el cierre.
  - La configuración de ejemplo traía 4 h para crítica; usé las 6 h de la política.
- **Matriz y calendario:** la matriz tiene 4 destinatarios y el calendario 5 pruebas. Las columnas de ambos se reconocieron.
- **Términos:** versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-15. Quedó el comprobante en `.criterio/terminos/` en Markdown y PDF.
- **Ficha:** contiene 1 incidente (INC-CCM-101), 1 revisión y 5 pruebas.
  - INC-CCM-101 se contuvo en 5,5 h, dentro del plazo de 6 h.
  - Su revisión se hizo el 2026-09-12, 4 días después del cierre (2026-09-08).
  - La restauración del ERP comercial (2026-08-01) quedó "con observaciones" en su informe.
- **Corrida:** quedó registrada como `2026-10-15-resilience-setup-1`.

**Decisiones mías:**
- **Marca de la raíz:** no puse `_CRITERIO_SEGURIDAD.txt` en la carpeta de documentos, porque nadie lo autorizó. No lo volví a pedir.
- **Revisión fuera de lugar:** `80-revisiones/INC-CCM-101_revision.md` el motor dice que iría en `70-incidentes/`. No lo moví.
- **Preguntas:** las respuestas salieron de los documentos, así que no hubo preguntas a la persona.

**Por revisar:**
- **Notificaciones:** `compute` no marcó nada, pero no revisé a mano la notificación a la Comisión supervisora. Se envió a las 24 h 0 min de la detección, justo en el plazo de 24 h de la matriz. Conviene mirarla en `notifications`.
- **Reporte:** dice "Sin documentos citados" en Fuentes, aunque la ficha sí trae citas.

Los archivos están en `.criterio/resiliencia/ccm090101ab3/config.json` y `estado-seguridad/ccm090101ab3-comercial-control-sintetica/`:
- `resiliencia/2026-10/reporte-incident-timeline.md`
- `corridas/salida-resilience-setup.md`