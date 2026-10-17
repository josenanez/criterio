# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de Tarjeta de la tienda (PRD-309). Con lo que hay en la carpeta todavía es una propuesta, no un caso de negocio. No hay ningún costo con fuente, no hay criterio de éxito y la única cifra no tiene serie que la mida.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré de nuevo.

- **Cifras:** hay una sola, `volumen_mensual = 106.991`. Es declarada (caso de negocio del 2025-11-12) y no hay serie medida con la que contrastarla. El retorno solo dice «en 24 meses», sin monto ni base, así que no cuenta como cifra.
- **Qué se construye:** entran los 11 requerimientos aceptados. REQ-4903 y REQ-4911 no tienen quién los pidiera, y ninguno de los 11 tiene proyecto que lo ejecute.
- **Costos:** no hay ninguno con fuente. Ese es el primer vacío, y no calculé retorno ni rentabilidad.
- **Supuestos:** el de regulación de datos figura como verificado, pero el concepto jurídico del 2026-08-21 no está en la carpeta. Los otros dos son implícitos: que los clientes frecuentes son quienes quieren la tarjeta, y que 106.991 al mes es alcanzable.
- **Vacíos:** nombré 13 (costo de construir, criterio de éxito, qué cuenta el 106.991, serie de medición, país, entre otros).
- **Otros productos:** no hay ninguno publicado, así que no pude cruzar si otro cuenta las mismas cifras.

La corrida quedó registrada con `producto.py corrida` (37 segundos) y el hallazgo `evidence_stale` figura en 11 requerimientos.

Archivos en `estado-producto/PRD-309/corridas/`:
- `salida-product-business-case.md`
- `2026-10-17-product-business-case-1.md`