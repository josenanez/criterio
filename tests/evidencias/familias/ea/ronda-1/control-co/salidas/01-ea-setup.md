# /criterio-assistant:ea-setup direccion/gerencia-general

La instalación quedó hecha, pero todavía no hay fichas. Por eso el reporte no muestra qué se cruza, qué sesión no tiene acta ni qué compromiso venció. Eso lo da `/criterio-assistant:ea-scan`.

- **Carpeta:** `direccion/gerencia-general` fue la única candidata. No dejé `_CRITERIO_DIRECCION.txt`, porque en esta sesión nadie podía autorizarlo.
- **Inventario:** hay una agenda exportada el 2026-10-25. Hay cuatro sesiones: comité de gerencia el 2026-09-21 y el 2026-10-19, y junta directiva el 2026-09-24 y el 2026-10-29. Hay 5 correos.
- **Respuestas tomadas de los documentos (sin interfaz):**
  - Entidad: Distribuidora Control (CO).
  - Ejecutivo: Gerencia general. Asiste: Sara León.
  - Zona horaria: America/Bogota.
  - Correo de la oficina: presidencia@control.test.
  - Umbrales: los de `config.example.json`.
  - Carpetas excluidas: ninguna.
  - Rostrum: no se publica.
- **Configuración:** `.criterio/direccion/gerencia-general/config.json`, validada (ok). El estado está en `estado-direccion/gerencia-general`.
- **Términos:** José Francisco Ñáñez aceptó la versión 1.2 el 2026-10-26. El comprobante en Markdown y PDF quedó en `.criterio/terminos/` (`aceptacion-criterio-assistant-0.11.0-2026-10-26`).
- **Fichas:** no las escribí en este paso. `compute` dio 0 señales. En «Lo que no se pudo procesar», el reporte `estado-direccion/gerencia-general/reporte-ea-agenda.md` lista 7 elementos:
  - 3 sesiones sin ficha: comité de gerencia 2026-09-21 y 2026-10-19, y junta 2026-09-24.
  - 3 correos sin ficha: los de 2026-10-08, 2026-10-12 y 2026-10-21.
  - `90-borradores/LEEME.txt`, que no lleva «BORRADOR» en el nombre.
- **Agenda:** según el reporte, la próxima sesión de la junta es el 2026-10-29, en 3 días, y todavía no tiene acta.
- **Corrida:** quedó registrada como `2026-10-26-ea-setup-1`, con lo que mostré en `corridas/salida-ea-setup.md`.