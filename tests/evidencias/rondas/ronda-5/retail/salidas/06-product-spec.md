# /criterio-product:product-spec 

Escribí el borrador de especificación de PRD-306 (App de clientes), pero sin ninguna sección de comportamiento. Los 15 requerimientos aceptados no declaran qué necesidad cubren, así que cualquier comportamiento habría sido inventado. Gerente de producto: Felipe Arango. La corrida quedó registrada como `2026-10-16-product-spec-1`.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-16. No volví a registrarlos.

**Qué tiene el borrador**
- **Alcance:** entran REQ-2028, REQ-2036 y REQ-4601 a REQ-4613, solo como están registrados. REQ-4600 queda fuera porque sigue en `propuesto`.
- **Criterios de aceptación:**
  - Diez requerimientos traen solo «se verifica en producción». Eso no es verificable: dos personas no llegarían a la misma respuesta, y no hay métricas registradas.
  - Cinco no traen criterio: REQ-4603, 4604, 4608, 4609 y 4613.
- **Supuestos:**
  - «La demanda se sostiene sin descuento» lleva 196 días sin verificar, y el umbral es 30.
  - La cifra de 67.794 de volumen mensual no tiene ninguna serie medida con la que contrastarla.
- **Vacíos señalados, cada uno con quién lo cierra:**
  - REQ-4607 no tiene doliente.
  - El registro no dice quién decidió cada aceptación, y el acta solo dice «Se mantiene el plan».
  - Una sola cita genérica de cliente está asignada a 13 requerimientos y no nombra ninguno; REQ-2028 y REQ-4608 no tienen ni esa.
  - No hay criterio de éxito del producto ni prioridad.
  - Ningún proyecto construye el producto.
  - La definición no dice qué datos maneja la app, así que no pude hacer el barrido normativo.
- **Requerimientos sin cobertura:** los 15 aparecen en esa tabla, cada uno con su motivo.

No ofrecí `/product-charter` todavía, porque faltan necesidades, criterios de aceptación y criterio de éxito.

El borrador está en `/home/claude/banco/ronda-5/retail/espacio/estado-producto/PRD-306/corridas/salida-product-spec.md`.