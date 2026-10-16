# /criterio-product:product-business-case 

Armé el caso de negocio de Trazabilidad (PRD-304). Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-16, así que no los registré otra vez. Sin interfaz, tomé las respuestas sugeridas.

- **Cifra que no coincide:** el caso de negocio declara un volumen mensual de 151.914 (2026-02-26). La bodega de datos mide 116.821 (2026-10-14). Es 23,1 % por encima de lo medido, sobre el umbral de 20 %. La serie medida tiene un solo punto.
- **Costos:** no consta ninguno en los documentos, ni de construir ni de operar. Es el primer vacío: sin él lo que hay es una propuesta, no un caso que evaluar.
- **Retorno:** el caso solo dice «en 24 meses», sin cifra.
- **Supuesto de la red:** «La red de la mina soporta el volumen» está marcado «verificado» sin citar qué lo verificó. Su fecha de declaración (2026-03-27) es posterior a la del documento (2026-02-26). Lo clasifiqué como supuesto y lo ofrezco para assumption-tracking.
- **Demanda:** el caso incluye los 14 requerimientos aceptados, no los 2 propuestos. Once se apoyan en una sola cita de un cliente, de hace 14 meses. Tres (REQ-4407, 4410 y 2036) no tienen cita de quien los pidió.
- **Otros vacíos:** no hay criterio de éxito, alternativas consideradas, qué pasa si no se hace, propuesta (el rótulo está vacío) ni proyecto que lo construya.
- **Cruce con otros productos:** no se pudo hacer porque no hay otro producto publicado a la vista.

Todas las cifras vienen de los documentos de la carpeta; no produje ninguna, y no recomiendo aprobar ni rechazar. No ofrezco `/product-charter`, porque faltan el costo y el criterio de éxito.

La corrida quedó registrada (`2026-10-16-product-business-case-1`, 38 segundos, 39 hallazgos).

Archivos en `estado-producto/PRD-304/corridas/`:
- `salida-product-business-case.md`