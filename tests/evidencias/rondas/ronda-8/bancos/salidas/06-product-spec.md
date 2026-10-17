# /criterio-product:product-spec 

Escribí el borrador de especificación de Microseguros (PRD-306), pero no pude describir qué debe hacer el producto. Los 14 requerimientos tienen como título «Requerimiento REQ-46xx» y ninguno tiene la necesidad escrita, así que el borrador es un índice de IDs más una lista de lo que falta decidir.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no hizo falta registrarlos de nuevo.

- **Alcance:** entran los 11 requerimientos aceptados. Quedan fuera REQ-4606, REQ-4608 y REQ-4610, que siguen en `propuesto`.
- **Criterios de aceptación:** ninguno es verificable. Ocho dicen «se verifica en producción», sin magnitud ni umbral. REQ-4602, 4609 y 4611 no tienen criterio. No propuse umbrales porque eso lo decide producto.
- **Supuestos:**
  - La demanda «sin campaña» lleva 166 días sin verificar; el umbral es 30.
  - El volumen mensual declarado (140.572) está 28,9 % por encima del medido (99.900); el umbral es 20 %.
  - La evidencia de demanda es una sola frase de una entrevista del 2025-09-25, que no nombra ningún requerimiento y tiene más de 12 meses.
- **Vacíos:**
  - REQ-4612 no tiene doliente.
  - Ninguna aceptación registra quién decidió.
  - La definición no trae criterio de éxito.
  - «Se mantiene el plan» no apunta a ningún plan.
  - Ningún requerimiento tiene proyecto que lo ejecute.
  - No hubo barrido normativo: ningún documento nombra normas y no cito ninguna de memoria. Propongo que Mauricio Pérez asigne a Legal o Cumplimiento.
- **Cobertura:** ninguno de los 11 aceptados queda cubierto en sustancia. REQ-4602, 4609 y 4611 entran solo como vacío.
- **Siguiente paso:** no ofrezco `/product-charter`, porque los vacíos siguen abiertos.

La corrida quedó registrada: 14 requerimientos, 44 segundos, 32 hallazgos.

Archivos en `/home/claude/banco/ronda-8/bancos/espacio/estado-producto/PRD-306/corridas/`:
- `salida-product-spec.md`
- `2026-10-17-product-spec-1.md`