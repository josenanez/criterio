# /criterio-product:product-business-case 

Armé el borrador del caso de negocio de Autopago en tienda (PRD-302) y dejé la corrida registrada. El caso no se sostiene todavía: no hay costos, ni criterio de éxito, ni una cifra de retorno.

Los términos ya estaban vigentes con la aceptación de José Francisco Ñáñez del 2026-10-16, así que no los registré de nuevo.

Las cifras que sí tienen fuente:

- **Volumen mensual declarado:** 107.018, del caso de negocio del 2025-10-25.
- **Volumen mensual medido:** 107.348, del tablero de métricas con corte 2026-10-11. La brecha es del 0,3 %, bajo el umbral del 20 %. La serie tiene un solo punto y el indicador no tiene definición escrita.
- **Retorno esperado «en 24 meses»:** no trae monto, base ni supuestos. Quedó como supuesto sin cifra.

Los vacíos más importantes, todos en el documento:

- **Costos:** no consta el costo de construir ni de operar. Es el primer vacío; sin él hay una propuesta, no un caso.
- **Criterio de éxito y quién decide:** no están declarados. La autoridad es un comité y ningún documento nombra a una persona.
- **Supuesto regulatorio:** «La regulación de datos lo permite» dice «verificado», pero no cita con qué. Lleva 57 días sin verificarse.
- **Requerimientos:**
  - Los 12 aceptados no tienen proyecto que los construya.
  - 4 se aceptaron sin evidencia de demanda (REQ-2028, 4203, 4207 y 4209).
  - 2 no tienen doliente (REQ-4207 y 4209).
  - La única evidencia es un cliente entrevistado que no nombra ninguno de ellos ni dice si es de Pequeños negocios.
- **Otros productos:** no hay ninguno publicado, así que no se pudo hacer el cruce de métricas. No asumo que no haya solape.

Solo ofrecí pasar los supuestos a assumption-tracking. No ofrecí `/product-charter` porque la definición no está cerrada y el costo no consta.

La salida está en `/home/claude/banco/ronda-6/retail/espacio/estado-producto/PRD-302/corridas/salida-product-business-case.md`. La corrida `2026-10-16-product-business-case-1` midió 32 segundos y 25 hallazgos.