# /criterio-product:product-business-case 

El caso de negocio de Microseguros (PRD-306) quedó armado, y no se sostiene: ninguna de sus 2 cifras tiene fuente y no hay costo de construir en ningún documento. Por eso es una propuesta, no un caso que se pueda evaluar.

Los términos ya estaban aceptados (versión 1.0, José Francisco Ñáñez, 2026-10-14). La corrida quedó registrada con el id `2026-10-14-product-business-case-1`.

- **Cifras:**
  - El volumen mensual de 139.663 es una cifra supuesta que se presenta como declarada. El caso se cita a sí mismo como fuente.
  - El «retorno esperado en 24 meses» no tiene monto, inversión ni cálculo.
  - No hay serie medida con la que contrastarlas, así que no hay diferencia declarada contra medida que mostrar.
- **Requerimientos:**
  - Entran 4 aceptados: REQ-1060, REQ-1061, REQ-1063 y REQ-2025.
  - REQ-1062 queda fuera porque sigue propuesto desde 2026-05-29.
  - Ninguno de los 4 tiene proyecto que lo ejecute.
  - Todos citan solo a «Cliente entrevistado», y la única entrevista tiene 418 días y no los nombra.
- **Vacíos principales:**
  - No hay costo de construir.
  - Falta el origen del 139.663.
  - Falta el criterio de éxito con su métrica y su fecha de corte.
  - Faltan las alternativas y qué pasa si no se hace.
  - Faltan los obligaciones normativas, porque no hay país declarado.
- **Supuestos:** el volumen, el canal («verificado» pero sin evidencia a la vista), la demanda del segmento y el retorno. Quedan como candidatos para `assumption-tracking`.
- **Otros productos:** no hay fichas publicadas, así que el cruce de `/product-overlap` no se pudo hacer. Ningún otro documento de `documentos/productos/` afirma el 139.663.

No produje ninguna cifra y no recomiendo aprobar ni rechazar; esa decisión es del Comité de producto. No pasa a `/product-charter`.

La salida completa está en `estado/corridas/salida-product-business-case.md`.