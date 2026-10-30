# /criterio-assistant:ea-setup direccion/gerencia-general

La oficina de Gerencia general quedó instalada, pero las fichas de sesiones y correos todavía no están escritas. Eso lo hace `/criterio-assistant:ea-scan`. Por eso el reporte no calcula decisiones ni compromisos y deja 17 elementos sin ficha.

- **Respuestas:** nadie contestó. Las nueve salieron de `00-referencia/oficina.md` y `organos.csv`, o de los umbrales sugeridos en `config.example.json`. Se excluyó `20-correspondencia/personal`.
- **Términos (v1.3):** quedaron aceptados por José Francisco Ñáñez para esta prueba, con fecha 2026-10-26. El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Marca de la carpeta raíz:** no dejé `_CRITERIO_DIRECCION.txt`, porque nadie podía autorizarlo.
- **Configuración:** está en `.criterio/direccion/gerencia-general/config.json` y el motor la validó sin problemas.
- **Actas pendientes:** faltan las actas firmadas del comité de gerencia del 21, 25, 27 y 29 de septiembre, con 35, 31, 29 y 27 días. El 21 de septiembre solo tiene un borrador en `40-acta/`.
- **Agenda:** la exportación es del 2026-10-12, de hace 14 días. El motor no calcula cruces hasta que llegue una de los últimos 7 días.
- **Corrida y reporte:** la corrida quedó registrada como `2026-10-26-ea-setup-1`. El reporte está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`. Lo que te mostré, entero, está en `estado-direccion/gerencia-general/corridas/salida-ea-setup.md`.

El motor no marcó el borrador `acta-BORRADOR.md` en `40-acta/` como acta firmada. Tampoco reconoció `90-borradores/LEEME.txt`, que no tiene «BORRADOR» en el nombre. No moví ni cambié nada en los documentos.