# /criterio-assistant:ea-setup direccion/gerencia-general

Ofelia quedó instalada sobre la oficina de Gerencia general (Cooperativa Sierra Alta, Ecuador), pero no escribí las fichas de las sesiones ni de los correos. Por eso la corrida solo vio una señal: el acta firmada del comité de gerencia del 2026-09-21 no está en `40-acta/`. Han pasado 35 días, y lo que hay allí es un borrador.

**Qué quedó hecho**
- **Carpeta raíz:** `direccion/gerencia-general`, la única candidata. No dejé `_CRITERIO_DIRECCION.txt`, porque nadie lo autorizó.
- **Configuración:** la escribí en `.criterio/direccion/gerencia-general/config.json` con los datos de `oficina.md`, `organos.csv` y los correos, y el motor la validó sin problemas. Las demás respuestas las tomé de los documentos y las dije en la salida guardada de la corrida. Los umbrales son los de `config.example.json`.
- **Términos:** mostré el texto de la versión 1.2 y registré la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-10-26. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.

**Qué no se pudo calcular**
- **Cruces de agenda:** la exportación es del 2026-10-12, de hace 14 días, y el límite configurado es de 7. El motor no calcula cruces hasta que llegue una más reciente.
- **Fichas:** faltan las de los órganos comite-de-gerencia (sesiones 2026-09-21 y 2026-10-19) y consejo-de-administracion (2026-09-24), y las de tres correos (supervisor, cliente y boletín). Hay que correr `/criterio-assistant:ea-scan`. Sin ellas no hay lectura de compromisos ni de correspondencia, así que el reporte no dice nada sobre eso.
- **Archivo mal ubicado:** `90-borradores/LEEME.txt` no lleva «BORRADOR» en el nombre. No lo toqué.

El reporte completo está en `estado-direccion/gerencia-general/reporte-ea-agenda.md`, y la corrida quedó registrada como `2026-10-26-ea-setup-1`. No hice preguntas a ninguna persona.