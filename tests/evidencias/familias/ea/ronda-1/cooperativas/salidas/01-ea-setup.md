# /criterio-assistant:ea-setup direccion/gerencia-general

La instalación quedó hecha para la oficina de Gerencia general. Las fichas de sesiones y correos todavía no existen: faltan `/criterio-assistant:ea-scan` y una agenda nueva.

- **Configuración:** está en `.criterio/direccion/gerencia-general/config.json` y el motor la validó. Los datos salen de `00-referencia/oficina.md` y `organos.csv`.
  - La entidad es Cooperativa Sierra Alta (EC) y asiste Rosa Quishpe.
  - La oficina usa el correo presidencia@sierraalta.test y la zona America/Guayaquil.
  - Se excluye `20-correspondencia/personal` y no se publica en Rostrum.
  - Los umbrales son los de `config.example.json`.
  - El estado queda en `estado-direccion/gerencia-general`.
- **Términos:** el motor mostró los términos 1.2 y registré la aceptación de José Francisco Ñáñez con fecha 2026-10-26. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_DIRECCION.txt`, porque nadie lo autorizó.
- **Qué encontró:** el comité de gerencia del 2026-09-21 lleva 35 días sin acta firmada. En `40-acta/` solo hay un borrador.
- **Agenda:** la exportación es del 2026-10-12, de hace 14 días, y el límite configurado es 7. Por eso no se calcularon cruces. Hace falta una exportación nueva.
- **Sin ficha:** tres sesiones (comité del 2026-09-21 y del 2026-10-19, consejo del 2026-09-24) y tres correos. El reporte lo marca como no procesado. La sesión del consejo del 2026-10-29 no aparece en esa lista.
- **90-borradores:** `LEEME.txt` no lleva «BORRADOR» en el nombre.

Nadie respondió preguntas, así que tomé cada respuesta de los documentos. El reporte está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`. Lo que te mostré quedó guardado en `corridas/salida-ea-setup.md` y la corrida quedó registrada como `2026-10-26-ea-setup-1`.