# /criterio-assistant:ea-setup direccion/gerencia-general

La instalación quedó hecha, pero no hay fichas de las sesiones ni de los correos todavía. Por eso el reporte no dice qué sesión está sin material o sin acta, ni qué compromiso venció. Esas fichas las escribe `/criterio-assistant:ea-scan`, y este comando no lo corre. `compute` dio 0 señales y 7 elementos sin procesar.

- **Carpeta raíz:** `direccion/gerencia-general`, la única candidata. No dejé la marca `_CRITERIO_DIRECCION.txt` porque nadie autorizó escribirla en esa carpeta.
- **Preguntas:** nadie contestó. Tomé las 9 respuestas de `oficina.md`, `organos.csv` y `config.example.json`, y dejé dicho cuáles son.
- **Configuración:** `.criterio/direccion/gerencia-general/config.json`. Pasó la validación sin problemas.
- **Términos:** la versión 1.2 se mostró tal cual y quedó aceptada a nombre de José Francisco Ñáñez, fecha 2026-10-26. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-assistant-0.11.0-2026-10-26.md` y `.pdf`.
- **Agenda:** el reporte del motor lista seis eventos entre el 2026-10-26 y el 2026-11-09, entre ellos la sesión de la junta el 2026-10-29. Está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`. La tabla de sesiones solo marca como sin acta las del 2026-10-19 (comité de gerencia) y el 2026-10-29 (junta).
- **Archivo sin «BORRADOR»:** el motor marcó `90-borradores/LEEME.txt` porque no lleva «BORRADOR» en el nombre. No lo toqué.
- **Corrida registrada:** `2026-10-26-ea-setup-1`, con 0 hallazgos.

Siguiente paso: correr `/criterio-assistant:ea-scan` y luego volver a pedir el reporte de agenda.