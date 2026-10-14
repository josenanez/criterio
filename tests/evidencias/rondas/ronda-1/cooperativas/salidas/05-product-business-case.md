# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de PRD-300 (Crédito de libranza). Todavía no es evaluable: la definición y el caso son de 2026-05-09, y de las 2 cifras del caso ninguna tiene fuente propia. No recomiendo aprobar ni rechazar.

Los términos 1.0 ya constaban en la configuración a nombre de José Francisco Ñáñez. En las preguntas que quedaron abiertas tomé la respuesta sugerida y seguí.

- **Costo de construir:** no está en ningún documento de PRD-300, así que ese es el primer vacío. Listé los proyectos PRY-200 y PRY-209 como candidatos, sin sumarlos. El acta de PRY-200 dice «Producto asociado: crédito de libranza», sin código, y la definición de PRD-300 dice «Ninguno declarado». PRY-209 dice «No aplica».
- **Volumen mensual 211.347:** es una cifra declarada que se cita a sí misma como fuente. No hay serie medida (`metrics/` está vacío) ni otra cifra con la que contrastarla.
- **Retorno esperado «en 24 meses»:** no trae valor ni base. No estimé nada.
- **Criterio de éxito:** no está declarado ni hay fecha de corte. Sin él el producto no se puede cerrar meses después.
- **Demanda:** una sola frase de una entrevista del 2025-10-11, que ya pasó el umbral de 12 meses.
- **Requerimientos:** REQ-2023 está aceptado sin criterio de aceptación. Los tres REQ del acta del comité no tienen proyecto asignado.
- **Supuestos:** el del proveedor figura como «verificado», pero ningún documento muestra la verificación. Hay otros dos supuestos implícitos que nadie ha declarado: que el volumen es alcanzable y que el segmento no tiene oferta de libranza.
- **Otros productos:** no hay ninguno publicado. Busqué el 211.347 en toda la carpeta de documentos y solo aparece en PRD-300, pero eso no prueba que no haya solape.

La salida completa, con la tabla de vacíos y la normativa sin fijar, está en `estado/PRD-300/corridas/salida-product-business-case.md`. La corrida quedó registrada como `2026-10-14-product-business-case-1` y tardó 48 segundos. El registro muestra `producto: "?"`, probablemente porque `producto.json` sigue vacío.

Ofrezco pasar los tres supuestos a `assumption-tracking`. No ofrezco `/product-charter`: faltan el costo y el criterio de éxito, y ningún proyecto está vinculado.