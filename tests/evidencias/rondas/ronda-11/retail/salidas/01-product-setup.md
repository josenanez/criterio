# /criterio-product:product-setup documentos/productos/PRD-301

## Listo — Puntos de fidelización (PRD-301)

La instalación quedó hecha y la corrida registrada. La definición de PRD-301 casi no tiene nada que la sostenga. No hay criterio de éxito escrito, ningún documento dice quién decide, y toda la demanda sale de una sola entrevista de 2025.

**Lo que miré:** 5 documentos, de los que solo 1 es de descubrimiento. Es una entrevista del 2025-08-29 con una frase: «Lo necesito y hoy no lo tengo». Leí también la definición y el caso de negocio del 2025-12-18, el tablero de métricas del 2026-10-11 y el acta del comité del 2026-10-20. Los 5 se pudieron leer.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.8.0 (términos 1.2), el 2026-10-23. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.8.0-2026-10-23.md` y `.pdf`. La huella SHA-256 de los términos empieza por 97ef3d7200b125fa.

**Preguntas:** 0. En la sesión sin interfaz tomé las respuestas sugeridas:
- **Carpeta raíz:** la del argumento.
- **Gerente de producto:** Beatriz Cuéllar, según la definición.
- **Estado:** `estado-producto/PRD-301`.
- **Quién decide:** «Comité de producto». Es mi propuesta, no un dato de los documentos.

No dejé `_CRITERIO_PRODUCTO.txt` en la carpeta de documentos, porque esa pregunta no traía respuesta sugerida y no escribo ahí sin un sí.

### Lo que la definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «Jóvenes no tiene puntos de fidelización» | Solo la entrevista, que no dice quién es el entrevistado ni de qué producto habla | 2025-08-29 |
| Volumen mensual de 297.074 | La medición: 310.136. Diferencia de 4,4 %, bajo el umbral de 20 % | declarado 2025-12-18, medido 2026-10-11 |
| «Retorno esperado en 24 meses» | Nada: no hay cifra | 2025-12-18 |
| «Propuesta principal» | Nada: está sin contenido | 2025-12-18 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** ningún documento dice cómo se sabrá que el producto funcionó.
- **Quién decide:** el acta solo lista como asistente a Beatriz Cuéllar, que además es doliente de dos requerimientos aceptados.
- **Origen de la cifra 297.074:** el caso de negocio se cita a sí mismo como fuente.
- **Retorno esperado:** solo dice «en 24 meses», sin monto.
- **Qué es la propuesta.**
- **Qué le pasa al joven:** el problema describe la ausencia de la solución.
- **Qué pide cada requerimiento:** los 17 se titulan «Requerimiento REQ-xxxx» y ninguno tiene el problema escrito.

### Lo que dice el registro (17 requerimientos: 12 aceptados, 5 propuestos)
- **Sin proyecto:** los 12 aceptados no tienen proyecto que los ejecute.
- **Aceptados sin evidencia:** REQ-4115 y REQ-2030, que nadie pidió.
- **Aceptados sin criterio de aceptación:** REQ-4101, 4103, 4106, 4109 y 4110. En los demás el criterio es siempre «se verifica en producción», que no dice qué se mide.
- **Sin doliente:** REQ-4103 y REQ-4105.
- **Evidencia envejecida:** 14 requerimientos. Toda la demanda sale de la misma entrevista, de hace 13 meses (el umbral es 12), y esa entrevista no nombra ningún requerimiento.
- **Propuestos sin decidir hace más de 60 días:** REQ-4104 (186 días), REQ-4108 (117), REQ-4105 (113) y REQ-4113 (75).
- **Acta:** termina con «Se mantiene el plan» y no decide nada sobre estos puntos.

### Supuestos sobre los que está escrita
- **«Las tiendas soportan el volumen»:** declarado el 2026-06-26 y sin verificar desde hace 119 días. El volumen medido ya está 4,4 % por encima del declarado.
- **Fecha del supuesto:** la definición es del 2025-12-18 pero el supuesto lleva fecha de junio de 2026, así que alguien editó el documento sin cambiarle la fecha.
- No hay más supuestos declarados.

### Qué le falta a tu carpeta
- Más transcripciones de entrevistas: hay una sola.
- Una serie de la métrica: el tablero trae un único punto.
- Las decisiones del comité con quién decidió.
- Un criterio de éxito escrito.

**Nota de proceso:** el comando dice que aquí no va `corrida-inicio`, pero `sellar` se negó a correr sin una corrida abierta. La abrí, así que el tiempo medido (29 segundos) cubre solo el tramo final.

**Siguiente paso:** `/product-discovery` sobre las entrevistas. Con una sola frase no va a sacar mucho, así que lo útil sería conseguir más entrevistas.

La salida completa está en `estado-producto/PRD-301/corridas/salida-product-setup.md`, y la corrida quedó registrada con el id `2026-10-23-product-setup-1`.