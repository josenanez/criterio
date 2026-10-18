# /criterio-product:product-setup documentos/productos/PRD-307

La instalación de PRD-307 quedó lista. Los términos, la configuración, la ficha, los 16 requerimientos y la corrida quedaron registrados.

## Listo — Auxilios de solidaridad (PRD-307)

**Lo que miré:** 5 documentos, uno de descubrimiento (entrevistas del 2026-01-15). Hay una definición del 2026-04-29 y la fecha más reciente es el acta del comité del 2026-10-06. Pude leer todos los formatos.

**Términos:** aceptados para la versión 0.4.0 (términos 1.1) a nombre de José Francisco Ñáñez, 2026-10-17. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.4.0-2026-10-17.md` y `.pdf`, SHA-256 38ea1d146bbd84f3…

**Las cuatro preguntas:** nadie respondió, así que tomé la respuesta sugerida en cada una.
- Gerente: Óscar Ramírez, según la definición.
- Quién decide: Comité de producto, según el acta. La definición no nombra a nadie.
- Estado: `estado-producto/PRD-307`.
- Términos: el sí viene de tu instrucción.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Hay quien necesita auxilios y hoy no los tiene | Sostenida (media): una entrevista de un cliente sin nombre y sin segmento | 2026-01-15 |
| Ese segmento es *Asociados urbanos* | No está dicha en ninguna parte | — |
| El volumen mensual es 68.516 | No está dicha en ninguna parte: la fuente es el propio caso de negocio y no hay serie medida | 2026-04-29 |
| Retorno esperado en 24 meses | No está dicha en ninguna parte: no trae cifra ni base | 2026-04-29 |
| El reglamento vigente lo permite | Sostenida por un supuesto, declarado verificado | supuesto 2026-06-01, verificación 2026-08-22 |

### Lo que no está dicho en ninguna parte
- El criterio de éxito.
- La propuesta: la sección dice solo «Propuesta principal».
- De dónde sale el 68.516. Nadie está midiendo lo que el negocio afirmó, y por eso no pude contrastarlo.
- Que el problema sea de Asociados urbanos.
- Qué proyecto lo construye.

### Lo que dice el registro
- **Requerimientos:** 16, de los cuales 13 están aceptados y 3 propuestos.
- **Sin proyecto:** los 13 aceptados no tienen proyecto que los ejecute (0.0% con traza).
- **Evidencia:** 7 de 16 tienen evidencia de demanda (53.8%). Las 7 descansan en la misma entrevista de un cliente sin nombre, que no nombra ninguno de ellos.
- **Aceptados sin evidencia:** REQ-4701, 4704, 4706, 4707, 4713 y 4714.
- **Aceptados sin criterio de aceptación:** REQ-4706 y REQ-4713.
- **Aceptado sin doliente:** REQ-4702.
- **Propuestos sin decidir** (más de 60 días): REQ-4708 (106 días), REQ-4710 (154) y REQ-4715 (180).
- **El acta:** tiene un solo asistente, Óscar Ramírez, que también es el gerente. Su única decisión escrita es «Se mantiene el plan», y no hay ningún plan en la carpeta.

### Supuestos
Hay uno: «El reglamento vigente lo permite». La verificación se apoya en «el documento técnico del proveedor», que no está en la carpeta.

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas.
- La serie de `volumen_mensual` con su fuente.
- Las decisiones del comité requerimiento por requerimiento.
- El documento técnico del proveedor.
- Un criterio de éxito y un proyecto.

**Siguiente:** `/product-discovery` sobre el material de entrevistas.

## Notas de la corrida
- `sellar` exigió una corrida abierta, así que tuve que correr `corrida-inicio`, que el comando dice que no va. Reescribí las fichas dentro de esa corrida y las sellé.
- El script midió 38 segundos para la corrida. Los "~2 minutos" de la nota son una estimación mía y no una medición.
- El documento completo de esta salida está en `estado-producto/PRD-307/corridas/salida-product-setup.md`.