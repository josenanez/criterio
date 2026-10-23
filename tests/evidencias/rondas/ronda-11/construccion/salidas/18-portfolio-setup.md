# /criterio-portfolio:portfolio-setup documentos/proyectos

Quedó la instalación y probé con tres proyectos (PRY-201, PRY-209 y PRY-210). El portafolio tiene 13 proyectos (PRY-199 a PRY-211) y 74 documentos, y el más reciente es del 2026-10-22.

**Qué quedó escrito**
- La configuración está en `.criterio/portafolio/config.json` y `config` la verificó sin problemas. El estado va en `estado/` y los informes irán en `reportes/`.
- Los términos (versión 1.2) quedaron aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-22. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-portfolio-0.8.0-2026-10-22.md` y `.pdf`.
- Con las respuestas sugeridas, el perfil es PMO, con informe semanal en presentación. Las preguntas de la prueba tuvieron respuesta sugerida y no hice ninguna a la persona. No dejé el archivo `_CRITERIO_PORTAFOLIO.txt` en la carpeta.
- Las tres fichas están en `estado/records/` y selladas. Lo que se le mostró a la persona quedó en `estado/corridas/salida-portfolio-setup.md`, y la corrida se registró como `2026-10-22-portfolio-setup-1`.

**Qué encontró `compute`** (25 señales; no devolvió `record_issues`)
- **PRY-201 (19 señales):**
  - Declara verde y 51 %, pero tiene 9 compromisos vencidos y dos hitos cerrados sin acta (licencias y cimentación).
  - Dos compromisos se han movido 5 y 6 veces. «Enviar el documento 1» se prometió para el 2026-10-02 y va para el 2026-12-25.
  - Dos entregables del proveedor van tarde, con 116 y 51 días.
  - La ficha del gerente quedó aparte en `pm_record` y no salió ninguna discrepancia con mi lectura.
- **PRY-209 (4 señales):** declara verde, con un compromiso vencido (24 días) y dos hitos cerrados sin acta.
- **PRY-210 (2 señales):** declara 82 %, y el cronograma sustenta entre 33 % y 67 %. Además, un hito está cerrado sin acta.
- Los tres proyectos no tienen autoridad del gerente declarada en ningún documento.

**Límites de esta lectura**
- Cuatro cronogramas .xml no se pueden leer sin instalar algo: PRY-200 v2, PRY-203 v1 y v3, y PRY-211 v1.
- Los .docx y .xlsx no los abre el lector estándar. Usé un extractor mínimo de solo lectura, que dejé en el scratchpad y no toca los documentos.
- Quedan 10 proyectos por leer (PRY-199, 200, 202 a 208), en dos lotes, uno tras otro.
- El comando pedía contar los minutos hasta el primer resultado. La corrida registró 152 segundos, pero ese tiempo no incluye lo que tardó la conversación.