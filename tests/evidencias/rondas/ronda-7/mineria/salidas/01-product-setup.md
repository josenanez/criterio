# /criterio-product:product-setup documentos/productos/PRD-301

## Listo: Alerta de taludes (PRD-301)

La configuración, los términos aceptados, la ficha del producto y los 17 requerimientos quedaron escritos. La corrida `2026-10-17-product-setup-2` guarda la salida completa, y `config` verifica la configuración sin faltantes.

**Lo que miré:** 4 documentos, uno solo de descubrimiento (una ronda de entrevistas del 2025-08-30). La definición y el caso de negocio son del 2026-06-09, y lo más reciente es el acta del comité del 2026-10-09. Los 4 se pudieron leer.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.1, fecha 2026-10-17, con el sí dado en la instrucción de la sesión. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`. El SHA-256 empieza por d85e8bd2335ac89a.

**Respuestas por defecto:** las cuatro preguntas se tomaron con la propuesta sugerida.
- **Quién eres:** Natalia Ospina, gerente de producto según la definición.
- **Quién decide:** "Comité de producto". Es una propuesta mía; ningún documento lo declara.
- **Dónde se guarda:** `estado-producto/PRD-301`.
- **Términos:** la instrucción de la sesión.

### Lo que la definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| El segmento Comunidad no tiene alerta de taludes | Una sola entrevista de un cliente sin nombre: «Lo necesito y hoy no lo tengo». No dice que sea de Comunidad | 2025-08-30 (13 meses) |
| La red de la mina soporta el volumen | Solo un supuesto, sin verificar desde hace 58 días | declarado el 2026-08-20 |
| Volumen mensual de 191.637 | Solo el propio caso de negocio; no hay serie medida | 2026-06-09 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** ningún documento lo escribe.
- **Propuesta:** la definición tiene el encabezado «Propuesta principal» y nada debajo.
- **Retorno:** el caso dice «Retorno esperado en 24 meses» sin cifra.
- **Origen del 191.637:** la cifra cita al propio caso de negocio y no hay serie medida, así que nadie está midiendo lo que el negocio afirmó.
- **Quién decide qué se construye:** al comité solo asistió la gerente.
- **Qué pide cada requerimiento:** los 17 se titulan «Requerimiento REQ-xxxx»; ninguno dice el problema.
- **Qué proyecto los construye:** ninguno. De 12 aceptados, 0 tienen traza (0,0 %). El acta decide «Se mantiene el plan» y en la carpeta no hay plan.
- **Qué entrevista respalda cuál:** 14 requerimientos citan al «cliente entrevistado» y la entrevista no nombra ninguno.

### Lo que se ve en el registro (12 aceptados y 5 propuestos)
- **Evidencia vieja:** los 14 requerimientos con evidencia se apoyan en la misma entrevista de hace 13 meses (el umbral es 12).
- **Aceptados sin evidencia:** REQ-4108 y REQ-2030.
- **Aceptados sin criterio de aceptación:** 6. En los demás el criterio es «se verifica en producción», que dice dónde, no qué.
- **Sin doliente:** REQ-4100.
- **Propuestos sin decidir:** REQ-4103 (203 días), REQ-4102 (166) y REQ-4112 (130).
- **Fecha del supuesto:** el supuesto de la red está fechado el 2026-08-20 dentro de una definición del 2026-06-09, y la cifra de 191.637 depende de él.

### Qué le falta a tu carpeta
- Las transcripciones completas de las entrevistas, y más de una.
- La serie medida del volumen mensual, con su fuente.
- Quién decide, y las decisiones del comité con quién las tomó.
- Un plan o proyecto al que cuelgue algo.

### Dos desvíos del comando
- **`sellar` exigió `corrida-inicio`:** el comando dice que aquí no va, pero `sellar` no corre sin una corrida abierta. La abrí y lo dejé anotado en la nota de la corrida.
- **La primera corrida quedó sin salida:** la carpeta `corridas/` no existía y la salida no se escribió. Repetí el registro y la segunda corrida sí la lleva. La primera, `2026-10-17-product-setup-1`, quedó duplicada y sin salida.

**Siguiente paso:** `/product-discovery` sobre las entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.