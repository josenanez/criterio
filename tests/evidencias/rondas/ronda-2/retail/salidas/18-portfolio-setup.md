# /criterio-portfolio:portfolio-setup documentos/proyectos

## Listo — Retail

Dejé instalado el agente y probé con tres de los 13 proyectos. En dos de los tres, el informe dice verde y la evidencia lo contradice.

**Lo que miré:**
- Encontré 74 documentos en 13 proyectos (PRY-199 a PRY-211).
- Los formatos son .md, .pdf, .docx, .csv, .xlsx, .json y .txt.
- El documento más reciente es del 2026-10-15.

**Cómo quedó configurado:** nadie respondió, así que usé la respuesta sugerida en todo.
- **Rol:** PMO del portafolio.
- **Comité:** semanal, con próximo comité el 2026-10-22. Esa fecha la supuse, porque ningún documento la dice. Los archivos se llaman «comite-semanal», pero no traen fecha de la próxima reunión.
- **Formato del informe:** presentación. Quedó guardado como `html`, que es el formato del ejemplo.
- **Dónde guarda:** la configuración está en `.criterio/portafolio/config.json`, lo que Vera va encontrando en `estado/` y los informes en `reportes/`.

**Términos:** la versión 1.1 quedó registrada a nombre de José Francisco Ñáñez, con fecha 2026-10-15. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`. La verificación de la configuración dio `ok`.

**Hallazgos de los tres proyectos** (PRY-201, PRY-206 y PRY-211, desempatados por mí entre los cinco con documentos del 2026-10-15). El cálculo levantó 17 señales:
- **PRY-211:** declara verde con cinco señales en contra.
  - El despliegue se atrasó 77 días y el cronograma ya lo refleja, pero el cambio CC-01 sigue pendiente de comité.
  - Declara 31 % de avance cuando los hitos sostienen entre 60 y 80 %.
  - Hay un compromiso vencido hace 15 días (el punto 33, de Beatriz Cuéllar).
  - Un hito figura cerrado sin acta de recibo.
- **PRY-206:** declara verde.
  - Dos entregables del proveedor siguen pendientes, con 233 y 128 días de vencidos.
  - Hay una factura de 543.383.423 COP radicada contra un entregable sin acta de recibo.
  - Dos hitos figuran cerrados sin acta.
- **PRY-201:** declara amarillo, pero el atraso es de 91 días (28,6 %).
  - El cambio CC-01 figura autorizado sin fecha y sin línea base nueva.
  - Dos hitos figuran cerrados sin acta.
  - Aquí el gerente declara 59 % cuando los hitos sostienen entre 75 y 100 %.

En los tres proyectos falta la autoridad del gerente, es decir, hasta qué monto puede decidir sin subir a comité.

**Lo que sigue:** quedan 10 proyectos y 64 documentos. Calculo de 30 a 45 minutos en dos lotes, uno tras otro. Es una estimación mía, no una medida.

La corrida quedó registrada como `2026-10-15-portfolio-setup-1`, con la salida completa en `estado/corridas/salida-portfolio-setup.md`. El tiempo exacto hasta el primer resultado no se midió.