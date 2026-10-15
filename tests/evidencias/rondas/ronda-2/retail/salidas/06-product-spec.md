# /criterio-product:product-spec 

Escribí el borrador de especificación de Pago con QR (PRD-303), pero no pude cubrir con comportamiento ninguno de los 5 requerimientos aceptados. El registro no trae la necesidad de ninguno, y los títulos son marcadores como «Requerimiento REQ-1030». Escribir cómo funciona el pago habría sido inventarlo, así que lo dejé como vacío.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.
- **Criterios de aceptación:** ninguno de los 5 se puede verificar. Tres dicen «se verifica en producción», sin métrica ni umbral. REQ-2017 y REQ-2025 no tienen criterio. No redacté criterios de reemplazo, porque un umbral inventado quedaría como decidido. Tampoco hay métricas medidas del producto.
- **Vacíos:** son 9, cada uno con quién lo cerraría o con «sin dueño» cuando ningún documento lo nombra. Incluyen qué queda fuera del alcance, los casos borde, lo que debe hacer otro equipo y las obligaciones normativas. Tampoco consta quién aceptó cada requerimiento.
- **Normativa:** no hice el barrido de obligaciones normativas, porque sin definición de comportamiento no hay sobre qué hacerlo.
- **Supuestos:** «La demanda se sostiene sin descuento» lleva 212 días sin verificar. El volumen mensual de 243.100 del caso de negocio no tiene medición con la cual contrastarlo.
- **Siguiente paso:** no ofrezco `/product-charter`. Lo útil es que los dolientes cierren primero qué pide cada requerimiento y su criterio de aceptación.
- **Corrida:** quedó registrada con 8 hallazgos y 32 segundos medidos.

Archivos en `estado-producto/PRD-303/corridas/`:
- `salida-product-spec.md`
- `2026-10-15-product-spec-1.md`