# /criterio-product:product-spec 

Terminé: el borrador de especificación de Microseguros (PRD-309) está escrito y la corrida quedó registrada, pero la especificación casi no se pudo redactar. Ninguno de los 16 requerimientos dice qué problema resuelve; el acta del 2026-10-12 solo trae sus códigos. Por eso cubre 0 de los 12 aceptados con comportamiento, y dejé los vacíos a la vista en vez de rellenarlos.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-16), así que no los volví a registrar.

Lo que encontré:
- **Criterios de aceptación:** 11 de los 12 aceptados dicen solo «se verifica en producción», que no se puede verificar. REQ-4905 no tiene criterio.
- **Evidencia de demanda:** cinco aceptados no tienen evidencia. Los demás citan la misma entrevista del 2025-08-16, que no nombra ningún requerimiento y tiene 14 meses.
- **Proyecto:** ninguno de los 12 tiene proyecto que lo ejecute, y la definición dice «Ninguno declarado».
- **Doliente:** REQ-4909 y REQ-4913 están aceptados con el doliente «sin asignar».
- **Fecha:** REQ-2036 figura «desde 2026-10-15», posterior al acta.
- **Supuesto:** «El proveedor cumple el tiempo pactado» dice «verificado» sin citar con qué.
- **Volumen mensual:** el caso de negocio declara 276.481 y el tablero mide 194.582, un 29,6 % menos, sobre el umbral de 20 %.
- **Barrido normativo:** la documentación no dice el país, así que no cité ninguna norma. Los puntos que toca el producto quedaron en «no tengo la norma a la vista».

No ofrecí `/product-charter`: faltan el problema de cada requerimiento, el criterio de éxito, criterios verificables y un proyecto. El primer paso sugerido es que cada doliente escriba en una frase qué necesita quien lo pidió.

La corrida quedó como `2026-10-16-product-spec-1`: 16 requerimientos, 36 hallazgos, 58 segundos.

Archivo en `estado-producto/PRD-309/corridas/`:
- `salida-product-spec.md`