# /criterio-product:product-trace 

**Trazabilidad de Recaudos (PRD-306), al 2026-10-23.** Los 14 requerimientos decididos no tienen proyecto, y ninguna traza se pudo confirmar.

- **Términos:** ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-23, así que no hubo nada que registrar.
- **Fichas:** usé las 13 de `estado/records` (PRY-199 a PRY-211).
- **Decididos sin proyecto:** de los 16 requerimientos del registro, 14 están aceptados y ninguno declara proyecto. El acta del comité dice «Ninguno declarado» y no registra quién decidió cada uno. Los más antiguos, REQ-4604 y REQ-4610, llevan 212 días decididos sin proyecto. Los otros 2 requerimientos siguen en «propuesto».
- **Fichas que no coinciden con el registro:** no hay ninguna que contradiga al registro, porque el registro no declara proyecto alguno que comparar.
- **Proyecto que construye algo que el registro no tiene:** PRY-211 «Cobranza digital» dice en su ficha que ejecuta «recaudos», y ningún requerimiento lo nombra. El cruce es por nombre, no por el código PRD-306, y hay que confirmarlo con su gerente de proyecto. Si es este producto, PRY-211 podría ser el proyecto de varios de los 14.
- **Otras fichas:**
  - PRY-199 declara el producto PRD-299.
  - PRY-200, 201, 203, 204, 206 y 207 declaran productos distintos.
  - PRY-202, 205, 208, 209 y 210 no dicen qué producto ejecutan. Es un hallazgo de esas fichas, no de este registro.

Me equivoqué en una línea de la salida guardada, la de «Otras fichas». Dice «4 declaran otro producto» y debería decir 7. El resto del archivo es correcto, y no volví a correr el registro para no duplicar la corrida. Si prefiere el archivo corregido, se arregla y se vuelve a registrar.

En el cálculo, 10 de los 14 decididos tienen evidencia de demanda. Los otros 4 (REQ-4604, 4606, 4608 y 4614) están aceptados sin ella.

El siguiente paso con PRY-211 es una conversación con su gerente de proyecto. Para los decididos que ya estén listos, se puede usar `/criterio-product:product-charter`.

La corrida quedó registrada como `2026-10-23-product-trace-1` y encontró 37 hallazgos. La salida completa está en `estado-producto/PRD-306/corridas/salida-product-trace.md`.