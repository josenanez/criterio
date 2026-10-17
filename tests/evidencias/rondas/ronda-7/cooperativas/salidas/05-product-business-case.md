# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de Microcrédito (PRD-305) y quedó registrado en la corrida `2026-10-17-product-business-case-1`.

Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez el 2026-10-17), así que no pedí aceptación de nuevo. Como nadie podía responder preguntas, tomé la respuesta sugerida en cada una.

- **Cifras:** hay una sola declarada, `volumen_mensual` de 216.930 (caso de negocio, 2026-04-03). La medida es 207.028 (tablero de métricas, corte 2026-10-09). La diferencia es del 4,6 %, bajo el umbral de 20 %, pero la dejé dentro del caso. La serie tiene un solo punto y nadie define qué cuenta ese volumen, así que no se sabe si las dos cifras miden lo mismo.
- **Supuestas:** el «retorno esperado en 24 meses» no trae monto ni base. «La demanda se sostiene sin campaña» lleva 194 días sin verificar, y el documento del proveedor que la respaldaría no está en la carpeta.
- **Qué se construye:** los 9 requerimientos aceptados, ninguno con proyecto. REQ-4503 y REQ-4514 no tienen doliente, y REQ-4504 no tiene ninguna evidencia de demanda. Los otros 8 solo tienen la entrevista del 2025-09-06, que ya pasó el umbral de 12 meses.
- **Vacíos:** el primero es el costo de construir, que no está en ningún documento, así que hoy esto es una propuesta y no un caso evaluable. Tampoco están dichos el criterio de éxito, quién decide, qué pasa si no se hace, las alternativas consideradas, el país (y con él la norma aplicable) ni la «Propuesta principal».
- **Otros productos:** no hay fichas publicadas. Los otros 11 productos (PRD-299 a PRD-309) declaran un `volumen_mensual` distinto. Sin una definición de la métrica no puedo decir si cuentan las mismas transacciones.

No proyecté ingresos ni retorno, y no recomiendo aprobar ni rechazar. Como todavía faltan el costo y el criterio de éxito, tampoco corresponde `/product-charter`. Conviene pasar los supuestos a `assumption-tracking`.

El documento completo está en `estado-producto/PRD-305/corridas/salida-product-business-case.md`.