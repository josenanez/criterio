# /criterio-product:product-requirements 

## Registro — Marketplace (PRD-308) · al 2026-10-15

Hay 17 requerimientos y 13 están decididos. De esos 13, el 61.5% (8) tiene evidencia y ninguno tiene un proyecto que lo ejecute. La carpeta de fichas de proyecto (`estado/`) está vacía, así que ninguna traza se pudo confirmar. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-15), por eso no los registré de nuevo.

Todas las cifras salen de `compute`.

**Se va a construir y nadie lo pidió.** Cinco aceptados no tienen quién lo pidió:
- REQ-4800 (Carlos Peña).
- REQ-4801 (Ricardo Salas).
- REQ-4806 (Gustavo Neira).
- REQ-4813 (Liliana Torres).
- REQ-4815 (sin doliente).

REQ-4806 y REQ-4813 tampoco tienen criterio de aceptación, y REQ-4815 tampoco tiene doliente.

**Decidido y nadie lo construye.** Los 13 aceptados no tienen proyecto. Doce llevan entre 109 y 214 días aceptados, y solo REQ-2030 es reciente (20 días).

**Sin doliente.** REQ-4808 y REQ-4815 dicen «sin asignar». Quien lo cierra es el Comité de producto.

**Sin criterio de aceptación.** Cuatro decididos: REQ-4806, REQ-4807, REQ-4813 y REQ-4814. Cada doliente lo cierra. REQ-4808 también carece de criterio, pero está propuesto y no se le exige.

**Decidido sin documento que lo respalde.** El acta del comité del 12 de octubre solo dice «Se mantiene el plan». Diana Molina aparece como única asistente. No dice quién decidió cada requerimiento ni cuándo. Las fechas de decisión vienen de la columna «Desde» de la tabla.

**Lleva meses y nadie lo decide.** El umbral es de 60 días:
- REQ-4808: 144 días.
- REQ-4803: 103 días.
- REQ-4804: 101 días.

REQ-4810 lleva 45 días y no es hallazgo. La configuración dice que decide el Comité de producto, pero `compute` devuelve `authority: null`. Conviene confirmar quién decide de verdad.

**Evidencia vieja.** Ninguna. Lo más nuevo es del 2026-02-08, y el umbral es de 12 meses.

**Por estado.** 4 propuestos, 13 aceptados y 0 en cualquiera de los demás estados. No hay ninguno descartado.

**Aparte.** El caso de negocio declara un volumen mensual de 209,097 y la bodega mide 131,628. Es un 37% por encima de lo medido, con el umbral en 20%. Eso corresponde a `/product-definition`.

**Siguiente paso.** Ofrezco `/product-trace` para los 13 decididos sin proyecto. REQ-2030, REQ-4802, REQ-4805, REQ-4809, REQ-4811 y REQ-4812 tienen doliente, criterio y evidencia, y son candidatos a `/product-charter`.

La corrida quedó registrada como `2026-10-15-product-requirements-1`: 28 hallazgos en 42 segundos. La salida completa está en `/home/claude/banco/ronda-3/retail/espacio/estado-producto/PRD-308/corridas/salida-product-requirements.md`.