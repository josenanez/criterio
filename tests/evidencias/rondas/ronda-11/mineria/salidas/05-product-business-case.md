# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-309 (Inspección con drones). Tiene un solo costo, ninguno, y una sola cifra, que no tiene respaldo. La corrida quedó registrada y duró 33 segundos.

Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-22), así que no los registré de nuevo.

- **Problema y para quién:** «Los Supervisores no tienen inspección con drones». Lo sostiene una sola entrevista del 2025-08-21 («Lo necesito y hoy no lo tengo»). Es débil: la entrevista no dice que el cliente sea Supervisor y tiene 14 meses.
- **Qué se construye:** son 13 requerimientos aceptados y ninguno tiene proyecto que lo ejecute. REQ-4900 y REQ-4907 no tienen cita de quién los pidió. Los otros 11 se apoyan en la misma entrevista, que no nombra ninguno.
- **Cifras:** la única es el volumen mensual de 270.035, declarada por el negocio. No tiene serie medida ni base de cálculo. El «retorno esperado en 24 meses» es una frase sin número, así que lo traté como supuesto.
- **Costos:** no hay ninguno en los documentos. Ese es el primer vacío: sin el costo de construir no hay caso que evaluar, hay una propuesta.
- **Supuestos:** son tres.
  - La licencia ambiental lo permite: lleva 161 días sin verificar y no tiene a quién asignarlo.
  - El volumen de 270.035 es alcanzable.
  - Los Supervisores son quienes lo piden.
- **Otros vacíos:** faltan el criterio de éxito con su fecha de corte, la propuesta principal (no tiene contenido), la autoridad que decide, qué pasa si no se hace y las alternativas.
- **Otros productos:** no hay ninguno publicado a la vista. La cifra 270.035 no aparece en las carpetas de documentos de PRD-299 a PRD-308 (búsqueda textual). No es un cruce completo.

No produje ninguna cifra ni recomendé aprobar o rechazar.

Lo siguiente es pasar los tres supuestos a assumption-tracking. `/product-charter` todavía no corresponde, porque el caso no tiene costo ni criterio de éxito.

Archivos en `estado-producto/PRD-309/corridas/`:
- `salida-product-business-case.md`
- `2026-10-23-product-business-case-1.md`