# /criterio-product:product-business-case 

Armé el caso de negocio de PRD-300 (Monitoreo de flota) y quedó registrada la corrida. No hay un caso que evaluar todavía: el costo de construir no está en ningún documento, y sin él lo que hay es una propuesta.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.
- **La cifra no coincide con la medida:** el caso declara 164.808 de volumen mensual (2026-02-02) y la bodega mide 102.629 (corte 2026-09-28). La declarada está 37,7 % por encima, con un umbral de 20 %. La serie medida tiene un solo punto, así que no hay tendencia. Tampoco hay método de cálculo del 164.808.
- **Qué se construye:** cuatro requerimientos aceptados en el acta del 2026-10-11 (REQ-1000, REQ-1001, REQ-1002 y REQ-2017).
  - Ninguno tiene decisión documentada ni proyecto asignado.
  - REQ-2017 no tiene evidencia de demanda.
  - Los otros tres citan la misma entrevista anónima de hace 12 meses.
- **Retorno y ahorro:** «retorno en 24 meses» no trae monto, y el supuesto del ahorro lleva 131 días sin verificar (umbral 30).
- **Otros vacíos:** costo de construir, criterio de éxito, autoridad, qué pasa si no se hace, qué alternativas se consideraron, y país y datos que recoge (a revisión jurídica, sin citar norma).
- **Otros productos:** no hay ninguno publicado a la vista. Busqué 164.808 en los documentos de PRD-299 a PRD-309 y no aparece. Varios de esos productos también usan la métrica volumen_mensual, así que conviene correr `/product-overlap` cuando se publiquen.

El documento está en `/home/claude/banco/ronda-2/mineria/espacio/estado-producto/PRD-300/corridas/salida-product-business-case.md`. La corrida quedó como `2026-10-15-product-business-case-1`: 35 segundos, 14 hallazgos, sobre 4 requerimientos.

No ofrezco `/product-charter` todavía, porque faltan criterio de éxito, autoridad y costo.