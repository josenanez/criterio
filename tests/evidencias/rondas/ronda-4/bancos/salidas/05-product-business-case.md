# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-309 (Crédito de libre inversión) y registré la corrida. Es una estructura con los vacíos nombrados, no una evaluación del caso.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-15, así que no los registré de nuevo.

- **Cifras:** el caso de 2025-12-13 declara un volumen mensual de 117.145. El tablero con corte 2026-10-11 mide 85.140, una brecha de 27,3 % (umbral 20 %), con la cifra declarada por encima. Eso va dentro del caso. La serie medida tiene un solo punto, así que no muestra tendencia.
- **Retorno:** el caso solo dice «en 24 meses», sin monto ni método. No lo traté como cifra.
- **Costos:** no hay ninguno en ningún documento. El costo de construir es el primer vacío; sin él lo que hay es una propuesta.
- **Éxito:** no hay criterio de éxito declarado, ni fecha de corte, ni alternativas, ni qué pasa si no se hace.
- **Requerimientos:** hay 11 decididos. Su evidencia de demanda es «Cliente entrevistado», sin cita, y ninguno dice quién decidió. Ninguno tiene proyecto que lo construya. Solo REQ-4909 y REQ-4912 tienen doliente, criterio y evidencia.
- **Supuestos:** «El canal actual soporta el volumen» figura como verificado, pero no hay documento de verificación. Lo anoté como supuesto con apariencia de declarado.
- **Tabla de requerimientos:** cuatro filas (REQ-4904, 4906, 4910 y 4911) salen de la corrida anterior de requerimientos, no de una relectura de cada ficha. Las marqué como «no revisadas en esta corrida».
- **Cruce con otros productos:** no hay ningún producto publicado a la vista, así que no se pudo hacer. No sabemos si otro producto cuenta las mismas transacciones.

La corrida tardó 39 segundos y quedó con 31 hallazgos abiertos (los de los requerimientos más la brecha entre lo declarado y lo medido).

El documento no recomienda aprobar ni rechazar; eso es del Comité de producto. Como siguiente paso ofrece pasar los tres supuestos a `assumption-tracking` y, si el caso se aprueba, `/product-charter` con REQ-4909 y REQ-4912.

Archivos en `/home/claude/banco/ronda-4/bancos/espacio/estado-producto/PRD-309/corridas/`:
- `salida-product-business-case.md`
- `2026-10-15-product-business-case-1.md`