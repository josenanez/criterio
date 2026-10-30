# /criterio-assistant:ea-setup direccion/gerencia-general

Ofelia quedó instalada sobre `direccion/gerencia-general`, con los términos aceptados y la configuración validada. Todavía no hay fichas, así que el reporte tiene solo lo que el motor saca de las carpetas.

- **Términos:** versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-26. El comprobante está en `.criterio/terminos/aceptacion-criterio-assistant-0.12.1-2026-10-26.md` y `.pdf`.
- **Configuración:** `.criterio/direccion/gerencia-general/config.json`. El motor la validó sin problemas.
  - Entidad: Cooperativa Sierra Alta (EC), asiste Rosa Quishpe.
  - Zona horaria America/Guayaquil y correo de la oficina presidencia@sierraalta.test.
  - Órganos: consejo-de-administracion y comite-de-gerencia.
  - Excluida: `20-correspondencia/personal`.
  - Umbrales de `config.example.json`, sin Rostrum.
  - El estado va en `estado-direccion/gerencia-general`.
- **Marca de la raíz:** no dejé `_CRITERIO_DIRECCION.txt`, porque nadie la autorizó.
- **Actas firmadas que faltan:** cuatro sesiones del comité de gerencia.

  | Sesión | Días sin acta firmada |
  |---|---|
  | 2026-09-21 (solo hay un borrador) | 35 |
  | 2026-09-25 | 31 |
  | 2026-09-27 | 29 |
  | 2026-09-29 | 27 |
- **Agenda:** la exportación es del 2026-10-12, de hace 14 días, y el límite es 7. El motor no calculó cruces. Hace falta una exportación nueva.
- **Fichas:** no se escribieron las de las 7 sesiones y los 7 correos, y el motor las marca como no procesadas. Para tenerlas hay que correr `/criterio-assistant:ea-scan`.
- **Aviso menor:** `90-borradores/LEEME.txt` no lleva «BORRADOR» en el nombre. No lo toqué.

El reporte completo está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`. La corrida quedó registrada como `2026-10-26-ea-setup-1`, con lo que mostré en `corridas/salida-ea-setup.md`.