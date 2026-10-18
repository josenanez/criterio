# /criterio-product:product-setup documentos/productos/PRD-300

## Listo — Monitoreo de flota (PRD-300)

La configuración, la ficha del producto, los 16 requerimientos y la corrida quedaron registrados. `config` verifica sin faltantes.

**Lo que miré:** 6 documentos. Solo uno es de descubrimiento: una ronda de entrevistas del 2025-10-08. Hay una definición y un caso de negocio, ambos del 2025-12-15. Lo más reciente es del 2026-10-15 (el acta del comité y el tablero de métricas). Los dos `.docx` se leyeron sin problema.

**Las cuatro preguntas** se respondieron con la propuesta por defecto:
- **Quién eres:** Camilo Beltrán, gerente de PRD-300.
- **Quién decide:** el Comité de producto. Ningún documento nombra a una persona que decida.
- **Dónde guardo:** `estado-producto/PRD-300`. No toqué `estado/`, que es de otro agente.
- **Términos:** versión 1.1, mostrados tal cual. El sí lo dio la instrucción de la prueba, así que registré a José Francisco Ñáñez con fecha 2026-10-17. Los comprobantes `.md` y `.pdf` están en `.criterio/terminos/`.

**Lo que tu definición afirma, y qué lo sostiene:**

| Afirmación | Sostenida por |
|---|---|
| El segmento Mantenimiento no tiene monitoreo de flota | Solo un supuesto: una frase de un «cliente entrevistado» (2025-10-08), sin nombre ni segmento. |
| Volumen mensual de 236.725 | El tablero mide 201.743 al 2026-10-15. La diferencia es de 14,8 %, bajo el umbral de 20 %, así que no es alerta. |
| El proveedor cumple el tiempo pactado | Un supuesto verificado, pero con el documento técnico del propio proveedor. |
| Retorno esperado en 24 meses | No está dicha en ninguna parte. |

**Lo que no está dicho en ninguna parte:**
- El criterio de éxito.
- De dónde sale el retorno en 24 meses.
- De dónde sale la cifra de 236.725.
- La propuesta: el título existe y no tiene nada debajo.
- El problema que pidió cada uno de los 16 requerimientos.
- Qué proyecto construye algo.
- Qué plan es el que «se mantiene».
- Quién decidió cada aceptación.

**Supuestos:** el supuesto del proveedor está fechado el 2026-03-19, tres meses después de la definición del 2025-12-15 donde aparece.

**Los 16 requerimientos del acta** son 11 aceptados y 5 propuestos:
- 11 aceptados no tienen proyecto que los ejecute.
- 11 tienen evidencia vencida (12 meses). Todos apuntan a la misma entrevista de un solo cliente.
- 3 aceptados no tienen evidencia de demanda (REQ-4003, REQ-4004 y REQ-4009). REQ-4009 tampoco tiene criterio de aceptación.
- 5 propuestos llevan entre 95 y 214 días sin decidirse.
- El criterio de aceptación escrito en 14 de los 16 es «se verifica en producción». Dice dónde, no qué.

**Qué le falta a tu carpeta:**
- Las transcripciones de las entrevistas.
- Una serie de más de un punto para `volumen_mensual`, con su definición.
- El plan que el comité «mantiene».
- Quién decide cada aceptación.

**Siguiente paso:** `/product-discovery` sobre las entrevistas.

**Una desviación del procedimiento:** `sellar` exige una corrida abierta, y este comando dice que aquí no va `corrida-inicio`. Abrí la corrida, reescribí la ficha (el script es idempotente) y sellé. Por eso el tiempo medido de la corrida es de 34 segundos, no el de toda la conversación.

La salida completa quedó en `estado-producto/PRD-300/corridas/salida-product-setup.md`. La corrida quedó registrada como `2026-10-17-product-setup-1`.