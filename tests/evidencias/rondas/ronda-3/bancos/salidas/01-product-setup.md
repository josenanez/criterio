# /criterio-product:product-setup documentos/productos/PRD-301

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

Nadie podía responder, así que tomé la respuesta sugerida en cada pregunta. Tú eres Paula Céspedes, gerente de Nómina empresarial (PRD-301), según el caso de negocio. Quien decide es «Comité de producto», el único nombre escrito. El estado quedó en `estado-producto/PRD-301`, aparte de `estado/`, que es del portafolio.

## Listo — Nómina empresarial (PRD-301)

**Lo que miré:** 5 documentos, y 1 de descubrimiento (entrevistas del 2025-09-20, una sola cita). Hay una definición y un caso de negocio, ambos del 2025-09-03. Lo más reciente es el tablero de métricas del 2026-09-29. No quedó ningún formato sin leer.

Levanté 18 requerimientos del acta del comité del 2026-10-10 (17 aceptados y 1 propuesto), la serie de la métrica y la ficha del producto, y sellé la lectura.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-15 para la versión 0.3.9 (términos 1.1). Lo registré con el sí que dejaste en el argumento.
- Comprobante: `.criterio/terminos/aceptacion-criterio-product-0.3.9-2026-10-15.md` y `.pdf`.
- SHA-256: eff52306622e7cd2…

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| El segmento Base de la pirámide no tiene nómina empresarial | Una cita: «Lo necesito y hoy no lo tengo» (cliente entrevistado, sin nombre ni empresa) | 2025-09-20 |
| Volumen mensual de 267.895 | Solo el caso de negocio. El tablero mide 201.716 al 2026-09-29, así que el caso está **24,7 % por encima** de lo medido | 2025-09-03 / 2026-09-29 |
| La regulación vigente lo permite | Un supuesto marcado «verificado» sin decir con qué. Figura «declarado el 2026-05-30» en un documento fechado 2025-09-03 | 2025-09-03 |
| Retorno esperado en 24 meses | Nada: sin cifra y sin base | 2025-09-03 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito del producto.** La definición no lo trae.
- **De dónde salen el retorno de 24 meses y el 267.895.**
- **Qué cuenta como `volumen_mensual`.** El tablero no lo define, así que no sé si las dos cifras miden lo mismo.
- **Con qué se verificó la regulación, y cuál es.**
- **Quién decide.** El acta solo registra a Paula Céspedes como asistente.
- **Qué pidió cada requerimiento.** La única entrevista no nombra ninguno. El acta se los atribuye a «Cliente entrevistado» en 15 de 18.
- **Proyecto que ejecute alguno:** 0 de 18 (0,0 %). La definición dice «Ninguno declarado».
- **Quién pidió REQ-4100 y REQ-4108.** Están aceptados sin evidencia.
- **Doliente de REQ-4109.** El acta dice «sin asignar».
- **Criterio de aceptación en 6 aceptados:** REQ-2030, 4103, 4108, 4112, 4113 y 4115. En los demás dice «se verifica en producción», que no dice qué se mide.
- **Por qué sigue propuesto REQ-4104.** Lleva 71 días sin decidirse.
- **Quién decidió cada aceptación.** El acta solo dice «Se mantiene el plan».

### Supuestos sobre los que está escrita
Declara uno: «La regulación vigente lo permite», marcado verificado sin fuente. No declara ningún supuesto sobre demanda ni sobre volumen.

### Qué le falta a tu carpeta
- **Las transcripciones de las entrevistas.** Hay una cita del 2025-09-20 y 16 requerimientos se apoyan en ella. Tiene 12 meses, justo el límite.
- **La serie de `volumen_mensual`.** Hay un solo punto (201.716, 2026-09-29), sin historia ni definición.
- **Las decisiones del comité, requerimiento por requerimiento.** REQ-2030 y REQ-2038 tienen otra numeración (2xxx) y se aceptaron el 2026-10-02 y el 2026-10-03. Puede que sean de otro producto; los dejé en el registro porque el acta los trae.

Para sellar tuve que abrir una corrida con `corrida-inicio`. El comando dice que aquí no va, pero `sellar` exige una corrida abierta.

Te ofrezco `/product-discovery` sobre las entrevistas: ahí los temas se vuelven requerimientos con la cita de quién los pidió.

La corrida quedó registrada como `2026-10-15-product-setup-1`, con el texto completo en `estado-producto/PRD-301/corridas/salida-product-setup.md`.