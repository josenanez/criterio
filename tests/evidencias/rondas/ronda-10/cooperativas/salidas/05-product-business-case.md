# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-305 (Microcrédito). Es un borrador sin cifras mías: el caso casi no tiene cifras con sustento.

Los términos ya estaban vigentes y registrados a nombre de José Francisco Ñáñez, así que no hubo que aceptarlos de nuevo. No hubo preguntas que contestar.

- **Cifras:** hay una sola. Es `volumen_mensual` = 166.254, declarada el 2025-12-01. Su fuente es el propio caso de negocio y no dice la unidad. No hay ninguna cifra medida, porque la carpeta `metrics/` está vacía. El «retorno esperado en 24 meses» no trae número.
- **Costos:** no hay ninguno en los documentos. Es el primer vacío: sin el costo de construir esto es una propuesta, no un caso de negocio.
- **Requerimientos:** 12 están aceptados y 4 propuestos. Ninguno tiene proyecto que lo ejecute. La única entrevista del 2025-12-30 respalda 9 de los 12 y no nombra ninguno. REQ-4507, 4511 y 4514 no tienen evidencia de demanda.
- **Supuestos:** el del proveedor está sin verificar desde el 2026-05-25, y la definición no nombra proveedor ni contrato. Marqué dos supuestos implícitos: que el volumen declarado es alcanzable y que una sola entrevista basta como demanda.
- **Criterio de éxito:** ningún documento lo define, y el caso lo dice así.
- **Otros productos:** busqué la cifra 166.254 en los demás productos (PRD-299 a PRD-309) y solo aparece en PRD-305. No hay fichas de otros productos publicadas, así que ese cruce es limitado.

Dejé la salida y la corrida registradas (`2026-10-18-product-business-case-1`, 27 hallazgos). Puedo pasar los supuestos a seguimiento (assumption-tracking). `/product-charter` no tiene sentido hasta que exista el costo.

Archivos están en `estado-producto/PRD-305/corridas/`:
- `salida-product-business-case.md`