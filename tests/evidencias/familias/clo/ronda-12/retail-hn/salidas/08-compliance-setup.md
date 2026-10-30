# /criterio-compliance:compliance-setup legal/08010006129040-almacenes-del-valle-de-sula

La instalación quedó hecha sobre Almacenes del Valle de Sula. El motor calcula 5 señales abiertas, pero el reporte de estado solo detalla 3 de ellas.

Qué dejé hecho:
- **Carpeta:** sigue la estructura. No moví ni creé nada en los documentos.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé, porque nadie autorizó escribir en los documentos. Esa pregunta quedó sin respuesta en la ficha.
- **Configuración:** `.criterio/cumplimiento/08010006129040/config.json`, validada por el motor.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Respuestas sugeridas:**
  - Periodo 2026-09.
  - 15 días de plazo para el canal de denuncias.
  - 30 días para evaluar una norma nueva.
  - Fichas de Fidel en `estado-legal/08010006129040-almacenes-del-valle-de-sula/contratos`, que comprobé que existe.
  - Los 15 y 30 días son los valores por defecto, no algo que digan los documentos.
- **Ficha del periodo:** `estado-legal/08010006129040-almacenes-del-valle-de-sula/cumplimiento/2026-09/ficha.json`. Registra el estado declarado por el informe del 2026-10-05, «con observaciones», con su cita.

Lo que muestra el reporte de estado (11 obligaciones, con avance con evidencia de 69.57 % ponderado por criticidad):
- **OB-10, Declaración mensual de origen de fondos:** la matriz la da por cumplida y no hay evidencia que empiece por OB-10.
- **OB-11, Monitoreo mensual de listas restrictivas:** la última evidencia es de 2026-07 y el ciclo anterior no tiene.
- **OB-13, Reporte de regalos e invitaciones:** no cita la norma, el contrato o la política de la que sale.

Las otras dos señales que cuenta el motor son un caso del canal de denuncias vencido y una política con la revisión vencida. No las detallé; salen en `reports-cases` y `policy-review`.

La salida completa está en `estado-legal/08010006129040-almacenes-del-valle-de-sula/corridas/salida-compliance-setup.md`, y la corrida quedó registrada con 5 hallazgos. El reporte está en `estado-legal/08010006129040-almacenes-del-valle-de-sula/cumplimiento/2026-09/reporte-compliance-status.md`.