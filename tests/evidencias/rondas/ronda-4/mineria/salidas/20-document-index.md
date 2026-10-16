# /criterio-portfolio:document-index 

## Carpeta al 2026-10-15

Los términos ya estaban vigentes (v0.3.10, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo nada que registrar.

**Documentos:** 73 · **Sin cambio:** 50 · **Hay que releer:** 23

- **Cambió el contenido:** ninguno.
- **Solo se reguardó, renombrado o movido, ya no está:** ninguno.
- **Nuevos para el índice (23):** todos son de PRY-200. Son el contrato CT-235, el acta de constitución, los cronogramas v1 y v2, las actas de recibo, la factura, la solicitud de cambio, el informe de avance, 6 comités semanales y las notas del 15 de oct. Los otros 12 proyectos no tienen nada nuevo.
  - La ficha de PRY-200 ya cita estos documentos, pero el índice no los tenía registrados. Por eso salen como nuevos y no como cambiados.
- **Citas que dejaron de resolver:** el índice marca 250 de PRY-200, pero probablemente es un falso positivo y no lo verifiqué a fondo.
  - Las 14 fuentes distintas existen dentro de la carpeta de PRY-200. Son rutas relativas al proyecto, y el chequeo parece resolverlas contra la raíz de documentos.
  - Tres de esas rutas comparten nombre con archivos de otros proyectos. Conviene confirmar que apunten al de PRY-200: el PDF de licencias y permisos, el informe de avance y la solicitud de cambio CC-01.
- **Formatos que no se pudieron leer:** el índice no reporta ninguno. Solo compara hashes. Entre los nuevos hay un .docx, un .xlsx y un .pdf, y su lectura le toca al barrido.

**Siguiente paso:** correr `/portfolio-scan` limitado a PRY-200 (23 documentos). `projects_to_recompute` vino vacío, así que no hay otros proyectos por recomputar.

La corrida quedó registrada como `2026-10-15-document-index-1` y la salida está en `estado/corridas/salida-document-index.md`. La corrida midió el tiempo (30 s) pero no la cantidad de documentos.