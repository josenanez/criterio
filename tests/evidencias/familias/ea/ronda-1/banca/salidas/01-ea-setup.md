# /criterio-assistant:ea-setup direccion/presidencia

La instalación de la oficina de presidencia quedó lista, con los términos aceptados y la corrida registrada. No hay fichas todavía: falta correr `/criterio-assistant:ea-scan`.

Nadie respondió preguntas, así que tomé las respuestas sugeridas por los documentos y las dije en una línea cada una. Los términos (versión 1.2) quedaron aceptados a nombre de José Francisco Ñáñez, fecha 2026-10-26. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.

La configuración está en `.criterio/direccion/presidencia/config.json` y el motor la validó sin problemas. El estado quedó en `estado-direccion/presidencia`. No dejé la marca `_CRITERIO_DIRECCION.txt`, porque ningún documento la autoriza.

El motor encontró cuatro cosas que atender:
- **Cruce el 2026-10-29:** «Sesión de la junta» (14:00–17:00) se cruza con «Visita del supervisor» (15:30–16:30).
- **Cruce el 2026-11-03:** «Llamada con la casa matriz» (09:00–10:00) se cruza con «Revisión con tesorería» (09:00–09:30).
- **Acta ausente:** el comité de presidencia del 2026-09-21 lleva 35 días sin acta firmada en `40-acta/`.
- **Material ausente:** a la junta del 2026-10-29 le faltan 3 días y su `20-material/` está vacío.

Siete elementos quedaron sin procesar:
- **Sesiones sin ficha:** comité 09-21, comité 10-19 y junta 09-24.
- **Correos sin ficha:** supervisor, cliente y boletín.
- **`90-borradores/LEEME.txt`:** no lleva «BORRADOR» en el nombre.

Un detalle del reporte: muestra el país de la entidad como «None» aunque la configuración dice CO. Lo dejé tal cual lo escribió el motor.

La salida completa quedó en `estado-direccion/presidencia/corridas/salida-ea-setup.md`. El reporte de la agenda está en `reporte-ea-agenda.md`, en la misma carpeta de estado.