# /criterio-product:product-setup documentos/productos/PRD-304

Soy Alba. Terminé la instalación de PRD-304 «Trazabilidad». Nadie respondió preguntas, así que en cada una tomé la respuesta sugerida.

**Lo que miré:** 5 documentos, y solo 1 es de descubrimiento: una ronda de entrevistas del 2025-08-15 con una sola cita. Hay caso de negocio y definición (2026-02-26), un tablero de métricas (2026-10-14) y el acta del comité (2026-10-13). Pude leer todos los formatos.

**Respuestas sugeridas que tomé:**
- **Producto y gerente:** Gustavo Neira, PRD-304 «Trazabilidad», segmento Mantenimiento.
- **Quién decide:** «Comité de producto». Es una propuesta mía: ningún documento lo dice, y la ficha la marca así.
- **Dónde guardo el estado:** `estado-producto/PRD-304`, separada de `estado/`.
- **Términos:** versión 1.1, mostrados tal cual y registrados a nombre de José Francisco Ñáñez, 2026-10-16, por la instrucción de esta sesión. Los comprobantes `.md` y `.pdf` están en `.criterio/terminos/`. El SHA-256 del Markdown empieza por f969d4f658630df3….

**Lo que tu definición afirma, y qué lo sostiene**

| Afirmación | Sostenida por |
|---|---|
| Mantenimiento no tiene trazabilidad | Solo una cita genérica de un cliente («Lo necesito y hoy no lo tengo»), que no nombra trazabilidad ni Mantenimiento. Tiene 14 meses. |
| Volumen mensual de 151.914 | El caso de negocio. La medición del 2026-10-14 da 116.821, así que el negocio declaró 23,1 % por encima. |
| «La red de la mina soporta el volumen» | Solo el propio documento, que dice «verificado» sin decir con qué. Lo fecha el 2026-03-27, después del documento (2026-02-26). |
| Retorno esperado en 24 meses | Nada: sin cifra ni fuente. |

**Lo que no está dicho en ninguna parte**
- No hay criterio de éxito, y la «Propuesta principal» está vacía.
- Ningún documento dice quién decide qué se construye.
- El acta no dice quién aceptó los requerimientos aceptados.
- De los 14 aceptados, ninguno tiene proyecto que lo ejecute (0 %).
- 3 aceptados no tienen quién los pidió (REQ-4407, REQ-4410, REQ-2036), 3 no tienen doliente (REQ-4401, REQ-4402, REQ-4405) y 4 no tienen criterio de aceptación (REQ-4402, REQ-4412, REQ-2028, REQ-2036). En los demás, «se verifica en producción» está escrito, pero no se puede verificar.
- REQ-4400 lleva 155 días propuesto y REQ-4411 lleva 176 sin decidirse. El acta solo dice «Se mantiene el plan».

**Supuestos:** hay uno declarado, el de la red. La definición no declara ninguno sobre la demanda.

**Qué le falta a tu carpeta:**
- Las transcripciones de las entrevistas, con quién habló y de qué segmento. Hoy los 12 requerimientos con evidencia se apoyan en esa misma entrevista de hace 14 meses.
- Una serie de la métrica. Hay un solo punto.
- Las decisiones del comité, con quién decidió y por qué.

**Para el siguiente paso**, te sugiero `/product-discovery` sobre las entrevistas.

**Qué dejé escrito:**
- **Ficha y registro:** `producto.json`, 16 requerimientos (14 aceptados y 2 propuestos) y la serie de métricas, en `estado-producto/PRD-304`.
- **Corrida registrada:** la salida está en `estado-producto/PRD-304/corridas/salida-product-setup.md` y la corrida como `2026-10-16-product-setup-1`.
- **Verificación:** `config` pasó sin faltantes.

Dos cosas del proceso:
- `sellar` exigió una corrida abierta, así que corrí `corrida-inicio` antes de sellar, aunque el comando dice que ahí no va.
- La fuente de la autoridad tuvo que quedar como nota, porque el sellado rechaza una fuente que no sea un documento.