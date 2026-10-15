# /criterio-product:product-business-case 

Armé el caso de negocio de Marketplace (PRD-308) y dejé la corrida registrada. Es una estructura con vacíos señalados: no calcula retorno ni recomienda aprobar o rechazar.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-15, así que no los registré de nuevo.

- **Cifra que no coincide:** el caso declara un volumen mensual de 209.097 (2025-10-14) y el tablero mide 131.628 (corte 2026-10-01). La declarada queda 37 % por encima de la medida, con el umbral en 20 %. La serie medida tiene un solo punto.
- **Retorno sin cifra:** «Retorno esperado en 24 meses» no trae valor ni base, así que entra como supuesto.
- **Costos:** ningún documento trae el costo de construir ni el de operar. Ese es el primer vacío y, sin él, esto es una propuesta y no un caso evaluable.
- **Criterio de éxito:** no está declarado en ninguna parte, así que no se sabe cómo se verificaría que funcionó.
- **Demanda:** 13 de los 17 requerimientos están aceptados, pero ninguno tiene proyecto que lo ejecute. Cinco de ellos no tienen quién los pidió, y los otros ocho citan la misma entrevista de 2026-02-08.
- **Otros productos:** no hay fichas publicadas, así que el cruce de `/product-overlap` no se pudo hacer. Los casos de PRD-299 a PRD-309 declaran el mismo tipo de volumen, pero ninguno repite el valor 209.097.

No ofrecí `/product-charter`, porque al caso le faltan costo y criterio de éxito. Sí propuse pasar los cuatro supuestos a `assumption-tracking`. El regulatorio es el más débil: figura como verificado sin decir quién ni con qué.

Archivos en `estado-producto/PRD-308/corridas/`:
- `salida-product-business-case.md`
- `2026-10-15-product-business-case-1.md`