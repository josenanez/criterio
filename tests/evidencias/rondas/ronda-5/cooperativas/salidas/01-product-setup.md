# /criterio-product:product-setup documentos/productos/PRD-309

## Listo — Microseguros (PRD-309)

**Lo que miré:** 5 documentos, de los que 1 es de descubrimiento (una entrevista del 2025-08-16). La definición y el caso de negocio son del 2026-01-25. Lo más reciente es el tablero del 2026-10-14. Pude leer todos los formatos.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.11 (términos 1.1) el 2026-10-16. Tomé ese sí de tu instrucción de la prueba. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.11-2026-10-16.md` y en el `.pdf` del mismo nombre. SHA-256 del `.md`: f969d4f658630df3…; del `.pdf`: 064270343bd7a374….

**Lo que tomé por defecto, sin preguntar:**
- Quién decide qué se construye: "Comité de producto". Ningún documento lo nombra. El acta solo lista como asistente a Beatriz Cuéllar.
- Dónde guardo el estado: `estado-producto/PRD-309`. No usé `estado/`, que es de otro agente.

**Lo que no pude hacer:** sellar la lectura. `sellar` exige una corrida abierta, y este comando no abre ninguna. La lectura queda sin sellar.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Pensionados no tiene microseguros | Una entrevista a un «Cliente entrevistado»: «Lo necesito y hoy no lo tengo.» No dice que sea pensionado, así que el sustento es parcial | 2025-08-16 |
| El volumen mensual será de 276.481 | Nada. El tablero mide 194.582 al 2026-10-14, 29.6 % por debajo de lo declarado | 2026-01-25 |
| El proveedor cumple el tiempo pactado | Un supuesto marcado «verificado» sin decir con qué | declarado 2026-03-30 |
| Retorno esperado en 24 meses | Nada. No hay cifra de retorno ni de dónde sale | 2026-01-25 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Ni la definición ni el caso de negocio dicen qué tiene que pasar para decir que funcionó.
- **La propuesta.** Dice «Propuesta principal» y no describe qué se ofrece.
- **Que los Pensionados lo pidan.** La única entrevista no dice quién es el entrevistado ni su segmento.
- **De dónde sale 276.481**, ni qué cuenta el «volumen». El tablero tampoco lo define.
- **Qué proyecto construye esto.** La definición dice «Ninguno declarado» y el acta no pone proyecto en ninguno de los 16 requerimientos.
- **El problema de cada requerimiento.** El acta solo trae códigos.
- **Quién aceptó cada requerimiento.** El acta no lo dice.
- **Con qué se verificó el supuesto del proveedor.** Su fecha (2026-03-30) es posterior a la de la definición (2026-01-25).

### Lo que muestra el registro (16 requerimientos: 12 aceptados, 4 propuestos)
- **12 aceptados sin proyecto** (0 % trazados).
- **5 aceptados sin evidencia de demanda:** REQ-4900, 4903, 4905, 4908 y 4911.
- **10 con evidencia vencida.** La única entrevista tiene 14 meses (el umbral es 12) y sostiene a todos los que citan «Cliente entrevistado». No nombra ninguno de los requerimientos.
- **4 propuestos sin decidir** (umbral: 60 días):
  - REQ-4901: 141 días.
  - REQ-4904: 69 días.
  - REQ-4910: 172 días.
  - REQ-4912: 110 días.
- **3 sin doliente** («sin asignar»): REQ-4909, 4912 y 4913.
- **1 aceptado sin criterio de aceptación:** REQ-4905, que además no tiene evidencia.
- **El comité del 2026-10-12 decidió «Se mantiene el plan»**, con los 12 aceptados sin proyecto.

### Supuestos sobre los que está escrita
Uno: «El proveedor cumple el tiempo pactado», declarado el 2026-03-30 y marcado «verificado». Lo registré como verificado porque el documento lo dice, pero no cita ninguna fuente de la verificación.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- Las transcripciones de las entrevistas. Hay una sola, de 14 meses, anónima y de una frase.
- El origen de 276.481 y la definición de «volumen mensual». El tablero trae un único punto, no una serie.
- El criterio de éxito y el retorno en cifras.
- Quién aceptó cada requerimiento y por qué, en el acta del comité de producto.

**Después:** `/product-discovery` sobre el material de entrevistas.

**Registro de la corrida:** `estado-producto/PRD-309/corridas/salida-product-setup.md`. La corrida quedó registrada como `2026-10-16-product-setup-1`. No hice preguntas (sesión sin interfaz) y el tiempo hasta el primer resultado no se midió. La configuración pasó la verificación (`config` devolvió `ok: true`).