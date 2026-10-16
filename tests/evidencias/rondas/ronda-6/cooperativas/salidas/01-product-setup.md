# /criterio-product:product-setup documentos/productos/PRD-305

## Listo: Microcrédito (PRD-305)

La instalación quedó hecha y la corrida registrada como `2026-10-16-product-setup-1`. Por la ruta de prueba sin interfaz, las cuatro preguntas las respondí yo con la respuesta sugerida.

**Lo que miré:** 4 documentos, y solo uno es de descubrimiento (una entrevista de 3 líneas). Están la definición y el caso de negocio, ambos del 2025-09-05, y el acta del comité del 2026-10-05. No hay métricas ni documentos de ningún proyecto. Pude leer todo, incluido el `.docx`.
**Configuración:** `.criterio/producto/PRD-305/config.json`; el comando `config` la verificó completa. El estado queda en `estado-producto/PRD-305`. Gerente: Óscar Ramírez. Decide el comité de producto; es un supuesto mío, porque ningún documento lo dice.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.1 (familia 0.3.12), fecha 2026-10-16. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.3.12-2026-10-16.md` y `.pdf`. SHA-256 del `.md`: bbc944aafa669a50…

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «Jóvenes no tiene microcrédito» | Un supuesto. La única cita es «Lo necesito y hoy no lo tengo», de un cliente que no se identifica como joven ni habla de microcrédito | 2025-10-03, 12 meses, en el umbral de envejecer |
| Volumen mensual 282.429 | Solo el propio caso de negocio, que se cita a sí mismo. No hay serie medida | 2025-09-05 |
| «Retorno esperado en 24 meses» | Nada: sin cifra y sin fuente | — |
| «El proveedor cumple el tiempo pactado» | Es un supuesto, sin verificar desde hace 73 días | declarado el 2026-08-04 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito.** No está escrito en ningún documento.
- **La propuesta.** La definición dice «Propuesta principal» y nada más.
- **El origen de 282.429 al mes.** Nadie lo está midiendo.
- **La cifra del retorno,** ni sobre qué inversión.
- **Que el segmento sea Jóvenes.** Ninguna entrevista lo dice.
- **Quién es el proveedor y cuál es el tiempo pactado.**
- **Quién decide.** El acta la firma como asistente solo Óscar Ramírez, que también escribió la definición y el caso de negocio.
- **Ningún proyecto ejecuta nada.** 0 de 13 requerimientos aceptados tienen proyecto (0,0 %). El acta dice «Se mantiene el plan», pero no hay plan escrito.

**Registro de 16 requerimientos** (13 aceptados, 3 propuestos). Las cifras salen del cálculo:
- **Sin evidencia de demanda:** 5 aceptados (REQ-4501, 4502, 4503, 4510, 4511). Los otros 8 aceptados sí tienen (61,5 %).
- **Evidencia en el límite de antigüedad:** 11, todos apoyados en la misma entrevista de 2025-10-03.
- **Sin doliente:** 4 (REQ-4505, 4509, 4510, 4511).
- **Aceptados sin criterio de aceptación:** 3 (REQ-4500, 4505, 4515). Los demás dicen todos «se verifica en producción», que no permite saber si algo quedó hecho antes de construirlo.
- **Propuestos sin decidir:** REQ-4508 (114 días) y REQ-4513 (168 días).
- **Sin descripción:** todos se llaman «Requerimiento REQ-45xx», así que ningún documento dice qué es cada uno.

### Supuestos sobre los que está escrita
Declara uno solo, el del proveedor. Aparece fechado el 2026-08-04 dentro de una definición del 2025-09-05. O se editó después sin cambiar la fecha o hay un error, y conviene aclararlo.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- **Entrevistas:** las transcripciones. Hoy una sola frase sostiene 11 requerimientos.
- **Métricas:** la serie de `volumen_mensual` con su fuente.
- **Decisiones del comité:** el motivo de cada una.
- **PRY-207 (microcrédito rural):** no sé si tiene relación con este producto. Ningún documento lo dice y no lo leí.

### Desvíos de lo que pedía el comando
- **Minutos hasta el primer resultado:** no los medí. El script midió 35 segundos de cálculo, y eso no equivale al tiempo de la conversación.
- **Corrida abierta:** el paso de sellar exige una corrida abierta y la ficha escrita después de abrirla. Por eso corrí `corrida-inicio`, a pesar de que el comando dice que aquí no va, y volví a escribir la ficha antes de sellar. El sello salió bien, con 4 documentos vistos.
- **Entrevista como evidencia:** la entrevista es genérica y no nombra ningún REQ. La usé como evidencia de los 11 que el acta atribuye a un «cliente entrevistado», y lo dejé anotado en cada registro.

La salida completa está en `estado-producto/PRD-305/corridas/salida-product-setup.md`. Lo siguiente sería `/product-discovery` sobre el material de entrevistas, para que los temas se vuelvan requerimientos con la cita de quién los pidió.