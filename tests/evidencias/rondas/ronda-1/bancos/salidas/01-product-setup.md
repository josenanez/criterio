# /criterio-product:product-setup documentos/productos/PRD-306

## Listo — Microseguros (PRD-306)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

Nadie podía responder, así que tomé la respuesta sugerida en las cuatro preguntas:
- **Producto y gerente:** Microseguros, Camilo Beltrán (sale del caso de negocio).
- **Quién decide:** Comité de producto.
- **Dónde guardo lo que encuentre:** la carpeta hermana `estado/`, fuera de la documentación.
- **Términos:** versión 1.0, aceptados por José Francisco Ñáñez el 2026-10-14.

También puse el próximo comité el 2026-11-09. Esa fecha la inventé yo, así que cámbiala si no es.

**Lo que miré:** 4 documentos, y los pude leer todos. Solo uno es de descubrimiento: las entrevistas del 2025-08-22. Hay una definición y un caso de negocio, ambos del 2026-01-08, y el acta del comité del 2026-10-09. No hay ninguna serie de métricas.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| El segmento Base de la pirámide no tiene microseguros | Una sola cita de un cliente: «Lo necesito y hoy no lo tengo». No dice de qué segmento es, ni quién, ni da cifra. | 2025-08-22 |
| El canal actual soporta el volumen | Un supuesto marcado «verificado» el 2026-08-25, sin decir quién lo verificó ni con qué. | 2026-08-25 |
| Volumen mensual de 139.663 | Solo el propio caso de negocio, que se cita a sí mismo como fuente. | 2026-01-08 |

### Lo que no está dicho en ninguna parte
- **Cliente:** la definición nombra un segmento, pero no quién es el cliente ni cuántos son.
- **Producto:** la propuesta es una línea, «Propuesta principal», sin contenido.
- **Éxito:** no hay criterio para saber si funcionó.
- **El 139.663 mensual:** ninguna serie, estudio ni entrevista lo respalda.
- **El retorno «en 24 meses»:** no trae monto, inversión ni cálculo.
- **El supuesto del canal:** no hay evidencia a la vista de que se verificó.
- **Los cinco requerimientos del comité:** todos dicen «Cliente entrevistado» como quién los pidió. La única entrevista tiene una cita y ningún tema que los nombre.
- **Proyecto:** la definición dice «Ninguno declarado», y los cinco requerimientos tienen «—» en el proyecto que los ejecuta.
- **La decisión del comité del 2026-10-09:** solo dice «Se mantiene el plan». Asistió una persona, el gerente. REQ-1062 sigue «propuesto» sin que se decida nada sobre él.

### Supuestos sobre los que está escrita
Declara uno solo: «El canal actual soporta el volumen», con fecha 2026-08-25. Esa fecha es posterior a la de la definición (2026-01-08). No declara supuestos sobre demanda, precio ni regulación de seguros.

### Cifras
La definición trae una cifra, 139.663 al mes, y no hay serie medida con qué contrastarla. Nadie está midiendo lo que el negocio afirmó. No calculé desviación porque faltan los datos. El script tampoco dio cifras derivadas, porque el registro de requerimientos todavía está vacío. Por eso tampoco escribo edades ni porcentajes.

### Qué le falta a tu carpeta
Esto es un hallazgo, no un requisito:
- Las transcripciones completas de las entrevistas, y entrevistas más recientes que la del 2025-08-22.
- La serie del volumen mensual, con su fuente y fecha.
- El detalle de las decisiones del comité. Sin él, un requerimiento descartado se ve igual que uno que nadie miró.
- Una definición que diga quién es el cliente, qué es el producto y cómo se mide el éxito.

Lo siguiente es `/product-discovery` sobre las entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién los pidió.

Esto es un borrador de trabajo, no certificado. Verifica cada punto contra los documentos antes de decidir.

**Lo que quedó escrito:**
- **Configuración:** `.criterio/producto/PRD-306/config.json`. El script la validó sin campos faltantes.
- **Estado:** `estado/` inicializado.
- **Salida de esta corrida:** `estado/corridas/salida-product-setup.md`.
- **Registro de la corrida:** `2026-10-14-product-setup-1`. Salió con el producto como «?» y 0 requerimientos en el registro, porque aún no se ha corrido el descubrimiento. En ese registro el tiempo hasta el primer resultado quedó sin medir.