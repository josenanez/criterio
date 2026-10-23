# /criterio-product:product-business-case 

El caso de negocio de Locales comerciales (PRD-305) quedó armado como estructura, pero no se puede evaluar: es una propuesta, no un caso. Falta el costo de construir, el criterio de éxito y el retorno.

Los términos v1.2 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-22, así que no los registré de nuevo.

- **Cifras:** hay una sola, `volumen_mensual = 214.841`. Es declarada, viene del caso de negocio del 2025-09-25 y no tiene ninguna serie medida; lleva 13 meses sin contrastarse. No hay cifras medidas ni supuestas. «Retorno esperado en 24 meses» no trae cifra, base ni supuestos, así que no entró como cifra.
- **Costos:** el costo de construir no está en ningún documento. Es el primer vacío.
- **Qué se construye:** hay 13 requerimientos aceptados el 2026-10-16. Solo 7 tienen evidencia de demanda, y es una sola frase de un cliente anónimo del 2026-02-03. Los otros 6 se aceptaron sin cita de quién los pidió.
- **Supuestos:** «La licencia se expide sin objeciones» lleva 46 días sin verificar (umbral 30). Tampoco está dicho que el cliente entrevistado sea una entidad pública.
- **Otros vacíos:** el criterio de éxito, la propuesta (la sección está vacía), el tamaño del problema y el precio. Tampoco se dice qué pasa si no se hace ni qué alternativas se consideraron.
- **Cruce con otros productos:** no se pudo hacer, porque no hay ningún producto publicado.
- **Lo que no hice:** no produje ni completé ninguna cifra, ni recomiendo aprobar o rechazar. No ofrezco `/product-charter` porque la definición no está cerrada y faltan los costos.

No leí el `.docx` de la definición. Tomé de la ficha `producto.json`, creada en una corrida anterior, lo que ese documento dice: el problema, el segmento y el supuesto de la licencia.

La corrida quedó registrada: 34 segundos, 15 requerimientos y 26 hallazgos.

Archivos, bajo `estado-producto/PRD-305/corridas/`:
- `salida-product-business-case.md`
- `2026-10-22-product-business-case-1.md` (el registro de la corrida, escrito por `producto.py corrida`; no lo abrí, así que su nombre sale del id que devolvió el script)