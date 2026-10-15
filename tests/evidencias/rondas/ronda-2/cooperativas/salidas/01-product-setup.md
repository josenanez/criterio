# /criterio-product:product-setup documentos/productos/PRD-300

## Listo — Crédito de libranza (PRD-300)

**Lo que miré:** 5 documentos, y se pudieron leer todos.
- Descubrimiento: una sola entrevista, del 2025-09-20.
- Definición y caso de negocio: ambos del 2026-04-09.
- Comité de producto: acta del 2026-10-10.
- Métricas: tablero del 2026-10-15.

**Términos:** aceptados por José Francisco Ñáñez el 2026-10-15, para la versión 0.3.8 (términos 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.8-2026-10-15.md` y `.pdf`. Los dos primeros 16 caracteres del SHA-256 son d532cc0636d081a9… (md) y 2198986eb2e729d5… (pdf).

Las respuestas por defecto que tomé:
- **Gerente de producto:** Gustavo Neira, porque la definición lo dice.
- **Quien decide:** "Comité de producto". Ningún documento lo dice; es una propuesta mía.
- **Estado:** `estado-producto/PRD-300`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Asociados rurales no tiene crédito de libranza | Una entrevista a un "cliente entrevistado": "Lo necesito y hoy no lo tengo". No dice si es de Asociados rurales. | 2025-09-20 (12 meses) |
| Volumen mensual de 156.447 | Solo el propio caso de negocio, que se cita a sí mismo como fuente. El tablero mide 121.498: la cifra declarada está 22,3 % por encima. | Declarada 2026-04-09, medida 2026-10-15 |
| El proveedor cumple el tiempo pactado | Un supuesto marcado "verificado", sin documento que muestre la verificación. | Declarado 2026-05-14 |
| Hay 4 requerimientos aceptados (REQ-1000 a REQ-1003) | La misma frase de la misma entrevista en los cuatro. La entrevista no nombra ninguno. | 2025-09-20 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** no aparece en la definición ni en el caso de negocio.
- **Fuente de los 156.447:** no hay estudio, base ni supuesto detrás.
- **Retorno esperado:** dice "en 24 meses", sin monto, sin tasa y sin base de cálculo.
- **Propuesta:** el título "Propuesta principal" está en la definición, pero sin contenido.
- **Qué pidió cada requerimiento:** los cuatro se llaman "Requerimiento REQ-100x" y "quién lo pidió" es "Cliente entrevistado" en todos.
- **Proyecto que los ejecuta:** la columna está vacía en los cuatro y la definición dice "Ninguno declarado". El comité decidió "Se mantiene el plan" y ningún documento muestra cuál es.
- **Decisión por requerimiento:** hay una decisión general del comité, no una para cada uno.
- **Quién decide qué se construye:** ningún documento lo dice. El comité del 2026-10-10 tiene un solo asistente, Gustavo Neira, que además es doliente de REQ-1001.

### Supuestos sobre los que está escrita
Hay uno: "El proveedor cumple el tiempo pactado", declarado el 2026-05-14, después de la fecha de la definición. La definición no declara ningún otro supuesto, así que la demanda de Asociados rurales y el volumen están escritos como hechos.

### Contraste con lo medido
- **volumen_mensual:** declarado 156.447 (2026-04-09), medido 121.498 (2026-10-15). La diferencia es de 22,3 %, sobre el umbral de 20 %.
- **Sin tendencia:** hay un solo punto medido, así que no se puede decir si sube o baja.
- **Sin producto en venta confirmado:** el tablero no dice si el crédito de libranza ya se vende, y por eso no sé si ese volumen es del producto.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- **Transcripciones de las entrevistas:** hay una sola, de una línea y de hace 12 meses. Por eso la evidencia de los cuatro requerimientos figura vencida.
- **Serie de la métrica principal con su fuente:** hoy hay un solo punto.
- **Decisiones del comité requerimiento por requerimiento,** y con más de una persona en la sala.
- **Proyecto para cada requerimiento aceptado:** los cuatro llevan entre 47 y 214 días sin uno.

Siguiente paso: `/product-discovery` sobre el material de entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién los pidió.

## Notas de la corrida
- **Preguntas:** no hubo ninguna a la persona. En total tomé 3 respuestas por defecto, y los términos salieron del argumento. Hasta el primer resultado pasaron unos 25 segundos medidos.
- **`sellar` pidió una corrida abierta:** el comando dice que aquí no va `corrida-inicio`, pero `sellar` lo exige. Abrí la corrida y reescribí la ficha dentro de ella (mismo contenido) para poder sellar. Conviene ajustar el texto del comando.
- **Dónde quedó todo:** la ficha y los 4 requerimientos están en `estado-producto/PRD-300/`. La corrida quedó registrada como `2026-10-15-product-setup-1` y la salida literal está en `estado-producto/PRD-300/corridas/salida-product-setup.md`.
- **Rutas:** la configuración está en `.criterio/producto/PRD-300/config.json`. Dejé vacíos `paths.fichas` y `committee_next`, porque no existen ni el repositorio de fichas ni una próxima fecha de comité.