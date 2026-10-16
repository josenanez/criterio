# /criterio-product:product-spec 

Escribí el borrador de especificación de PRD-309, pero sin ninguna sección de comportamiento. Los 11 requerimientos aceptados no dicen qué necesidad cubren, y no quise inventarla. La corrida quedó registrada.

Los términos ya estaban aceptados por José Francisco Ñáñez el 2026-10-15 (versión 0.3.10), así que no los registré de nuevo. Nadie respondió preguntas; en esta corrida no hubo ninguna que tomar por defecto.

- **Alcance:** entran los 11 aceptados, solo como lista. No entran los 4 propuestos (REQ-4901, 4903, 4908 y 4913), que llevan entre 137 y 168 días sin decisión, ni ningún otro segmento distinto de Microcomercio.
- **Criterios de aceptación:** REQ-4902, 4909 y 4912 traen «se verifica en producción», que no es verificable porque no dice qué se mide ni con qué resultado. Los otros 8 no traen criterio, y no propuse cifras porque serían mías.
- **Supuestos:**
  - «El canal actual soporta el volumen» figura como verificado, pero no hay documento de verificación.
  - Ese supuesto se apoya en un volumen de 117.145 que el tablero no sostiene: mide 85.140, 27,3 % menos, sobre un umbral de 20 %.
  - Ningún documento dice quién decide, y ninguno de los 11 aceptados dice quién tomó la decisión.
- **Vacíos:** cada uno lleva su dueño, mayormente Mauricio Pérez, el gerente de producto, y los dolientes de cada requerimiento. REQ-4900 y 4905 no tienen doliente. Tampoco están dichos el criterio de éxito del producto, los casos borde ni lo que debe hacer otro equipo.
- **Obligaciones normativas:** ningún documento dice el país. Por eso no cito normas; el estado de las tres áreas que toca es «no tengo la norma a la vista». La revisión jurídica sigue pendiente.
- **Requerimientos sin cubrir:** los 11. REQ-4909 y 4912 son los más cercanos a estar listos.
- **Siguiente paso:** todavía no corresponde `/product-charter`. Primero hay que cerrar la necesidad y el criterio de esos dos.

Archivos en `estado-producto/PRD-309/corridas/`:
- `salida-product-spec.md`
- `2026-10-15-product-spec-1.md` (registro de la corrida)