# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-303 (Tarjeta débito) y registré la corrida. Todavía no es un caso evaluable: no tiene costos ni beneficio con cifra.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-15, así que no hubo que registrarlos de nuevo.

- **Cifras:** el caso tiene una sola, declarada. El volumen mensual esperado es 250.670 (Sandra Gil, 2026-04-05). El tablero mide 256.871 (2026-10-06), una diferencia de 2,5 %, por debajo del umbral de 20 %. La medida es un solo punto, y no se sabe si la tarjeta ya opera.
- **Retorno:** dice solo "retorno esperado en 24 meses", sin valor, así que no cuenta como cifra.
- **Alcance:** entran los 11 requerimientos aceptados. Ninguno tiene proyecto que lo ejecute. Cuatro no dicen quién los pidió y cuatro no tienen doliente. Los títulos son genéricos, así que el documento no dice qué se construye en concreto.
- **Vacíos principales:**
  - Costo de construir y operar.
  - Beneficio con valor.
  - Cómo se calculó 250.670.
  - Criterio de éxito.
  - Alternativas y qué pasa si no se hace.
  - Contrato del proveedor.
- **Supuestos:** hay tres. Uno es declarado y sin verificar (el proveedor cumple el tiempo pactado) y dos son implícitos. Los dejé listos para pasar a seguimiento, sin hacerlo.
- **Otros productos:** no hay fichas publicadas (`estado/` está vacío) y 250.670 no aparece en los documentos de PRD-299 a PRD-309, así que no hubo cruce. Conviene correr `/product-overlap` cuando se publiquen.

Tomé las respuestas sugeridas sin preguntar, como pedía la prueba. No calculé retorno ni recomendé aprobar o rechazar.

La salida completa está en `estado-producto/PRD-303/corridas/salida-product-business-case.md`, y la corrida quedó registrada como `2026-10-15-product-business-case-1`. Tardó 34 segundos y dejó 39 señales abiertas, la mayoría de evidencia vieja y requerimientos sin trazar.