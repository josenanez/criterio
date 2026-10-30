# /criterio-assistant:ea-setup direccion/presidencia

La instalación de Presidencia quedó lista y la corrida de hoy (2026-10-26) está registrada. No hubo preguntas a nadie, como pedía la prueba. Las fichas de sesiones y correos todavía no existen: falta correr `/criterio-assistant:ea-scan`.

**Qué se hizo**
- **Carpeta raíz:** `direccion/presidencia` era la única candidata. No la marqué con `_CRITERIO_DIRECCION.txt` porque nadie lo autorizó.
- **Qué hay en la oficina:** una agenda exportada el 2026-10-25, 5 sesiones (3 del comité de presidencia y 2 de la junta directiva) y 9 correos.
- **Configuración:** la escribí en `.criterio/direccion/presidencia/config.json` con los datos de `00-referencia/` (Banco Andino, CO; asiste Laura Gómez; `America/Bogota`) y los umbrales de `config.example.json`. El motor la validó sin problemas.
- **Términos:** mostré los de la versión 1.3 y registré la aceptación de José Francisco Ñáñez con fecha 2026-10-26. Los comprobantes en Markdown y PDF quedaron en `.criterio/terminos/`.

**Qué encontró**
- **Cruces en la agenda:** hay 8. Dos de ellos:
  - 2026-10-29: «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30).
  - 2026-10-27: el vuelo AV 9217 (19:00–20:00) se cruza con «Llamada con la calificadora» (19:15–19:45).
- **Acta que falta:** el comité de presidencia del 2026-09-21 lleva 35 días y su acta firmada no está en `40-acta/`.
- **Material que falta:** la junta directiva del 2026-10-29 es en 3 días y no tiene nada en `20-material/`.

**Qué quedó sin procesar**
- 13 elementos: 4 sesiones, los 8 correos de octubre (la fuente los lista así) y `90-borradores/LEEME.txt`, que no lleva «BORRADOR» en el nombre. De esos, los 12 primeros esperan a `ea-scan`; el archivo de `90-borradores/` es solo un aviso.

El reporte completo está en `estado-direccion/presidencia/reporte-ea-agenda.md`. Lo que te mostré en esta sesión quedó en `estado-direccion/presidencia/corridas/salida-ea-setup.md`.