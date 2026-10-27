# /criterio-assistant:ea-setup direccion/presidencia

La instalación quedó hecha, pero todavía no hay fichas. La agenda sí salió, y el motor lo avisa en el reporte: las sesiones y los correos aún no tienen ficha. Eso lo hace `/criterio-assistant:ea-scan`, que no corrí porque el flujo de este comando no lo incluye.

- **Configuración:** `.criterio/direccion/presidencia/config.json`, validada sin problemas. Las respuestas salieron de `oficina.md` y de `organos.csv`: entidad Comercial Control (EC), asiste Mónica Ruiz, zona `America/Guayaquil`, correo `presidencia@controlec.test`, umbrales del ejemplo, sin Rostrum.
- **Estado:** `estado-direccion/presidencia`, fuera de la carpeta de documentos.
- **Términos:** versión 1.2, aceptados por José Francisco Ñáñez con fecha 2026-10-26. El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_DIRECCION.txt`, porque nadie la autorizó.
- **Qué se cruza en la agenda:** el reporte no marcó nada que atender. Muestra la sesión de la junta del 2026-10-29 a 3 días, con 1 material y sin acta. Para el comité-ejecutivo del 2026-10-19 muestra 1 material y ningún acta, a -7 días.
- **Compromisos vencidos:** el motor no los calculó, porque ninguna ficha existe aún.
- **Archivo fuera de norma:** `90-borradores/LEEME.txt` no lleva «BORRADOR» en el nombre. No lo toqué.
- **Corrida:** registrada como `2026-10-26-ea-setup-1`, con 0 hallazgos. Lo mostrado en esta sesión está en `estado-direccion/presidencia/corridas/salida-ea-setup.md`, y el reporte en `estado-direccion/presidencia/reporte-ea-agenda.md`.