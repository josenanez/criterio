# /criterio-assistant:ea-setup direccion/gerencia-general

La instalación quedó hecha, pero todavía no hay fichas: ninguna sesión, correo ni viaje se ha procesado. Eso lo hace `/criterio-assistant:ea-scan`, que no corrí en este comando. Por eso el reporte no muestra cruces, sesiones sin material ni compromisos vencidos. La agenda y la tabla de sesiones sí salieron.

- **Configuración:** `.criterio/direccion/gerencia-general/config.json`. Los datos salen de `00-referencia/` y los umbrales son los de `config.example.json`. El motor la validó sin problemas.
- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez con fecha 2026-10-26. El comprobante está en `.criterio/terminos/aceptacion-criterio-assistant-0.12.1-2026-10-26.md` y `.pdf`.
- **Agenda:** el reporte cubre del 2026-10-26 al 2026-11-09 e incluye la sesión de la junta del 2026-10-29.
- **Sin procesar:** el reporte lista 7 elementos. Son 3 sesiones, 3 correos y `90-borradores/LEEME.txt`, que no lleva «BORRADOR» en el nombre.
- **Marca de la raíz:** no dejé `_CRITERIO_DIRECCION.txt`, porque nadie podía autorizarla en esta prueba. Es opcional.
- **Corrida:** quedó registrada como `2026-10-26-ea-setup-1`, con lo que te mostré en `estado-direccion/gerencia-general/corridas/salida-ea-setup.md`. El reporte completo está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`.

El siguiente paso es correr `/criterio-assistant:ea-scan`.