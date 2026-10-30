# /criterio-assistant:ea-setup direccion/presidencia

Ofelia quedó instalada sobre la oficina de Presidencia de Banco Andino, con la configuración validada y los términos aceptados. La primera corrida de la agenda encontró 10 hallazgos, y la corrida quedó registrada como `2026-10-26-ea-setup-1`.

- **Configuración:** está en `.criterio/direccion/presidencia/config.json` y el estado en `estado-direccion/presidencia`. Los datos salieron de `00-referencia/` y de los umbrales de ejemplo.
- **Términos:** los de la versión 1.3 quedaron registrados a nombre de José Francisco Ñáñez, con fecha 2026-10-26. El comprobante está en `.criterio/terminos/`, en Markdown y PDF.
- **Marca de la carpeta raíz:** no dejé `_CRITERIO_DIRECCION.txt`, porque nadie autorizó escribir en la carpeta de documentos.

**Lo que encontró la agenda (al 2026-10-26)**
- **Cruces:** hay 8 en la agenda exportada el 2026-10-25. El más cercano es el del 2026-10-29, entre la sesión de la junta (14:00–17:00) y la visita del supervisor (15:30–16:30).
- **Sin acta:** el comité de presidencia del 2026-09-21 no tiene acta firmada en `40-acta/`, y han pasado 35 días.
- **Sin material:** la junta directiva del 2026-10-29 no tiene material en `20-material/`, y faltan 3 días.

**Pendiente**
- Las 4 sesiones pasadas y los 8 correos de `20-correspondencia/` todavía no tienen ficha. Falta correr `/criterio-assistant:ea-scan`.
- `90-borradores/LEEME.txt` no lleva «BORRADOR» en el nombre. No lo toqué.

El reporte completo está en `estado-direccion/presidencia/reporte-ea-agenda.md`, y lo que te mostré en esta corrida quedó en `estado-direccion/presidencia/corridas/salida-ea-setup.md`.