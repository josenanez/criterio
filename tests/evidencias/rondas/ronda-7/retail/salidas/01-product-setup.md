# /criterio-product:product-setup documentos/productos/PRD-309

## Listo — Tarjeta de la tienda (PRD-309)

La configuración, el estado y los 13 requerimientos quedaron escritos. Falló un paso: no pude sellar la lectura de los documentos.

**Qué miré:** 5 documentos. Uno es de descubrimiento: una ronda de entrevistas del 2025-08-24 con una sola cita. Los otros son la definición y el caso de negocio del 2026-07-12, el tablero de métricas del 2026-10-10 y el acta del comité del 2026-10-13. Pude leer todos.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.13 (términos 1.1), con fecha 2026-10-17. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`. Su huella SHA-256 empieza por `d85e8bd2335ac89a`.

**Preguntas:** nadie respondió, así que tomé la sugerida en cada una:
- **Producto:** Tarjeta de la tienda, PRD-309, con gerente Diana Molina.
- **Quién decide:** el comité de producto. Es una sugerencia mía: el acta no nombra a quien decide.
- **Dónde guardo:** `estado-producto/PRD-309`.
- **Términos:** aceptados con el nombre indicado.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por |
|---|---|
| Hogares no tiene tarjeta de la tienda | Nada propio. La única cita («Lo necesito y hoy no lo tengo») es de un cliente sin nombre, de hace 13 meses, y no menciona Hogares ni la tarjeta. |
| Volumen mensual de 272.424 | Solo el propio caso de negocio. El tablero mide 208.658 al 2026-10-10, así que el caso está 23,4 % por encima de lo medido. |
| Retorno esperado en 24 meses | Nada: no trae cifra, supuesto ni serie. |
| El proveedor cumple el tiempo pactado | Es un supuesto, sin verificar desde hace 70 días. |
| «Propuesta principal» | Nada: la definición no dice en qué consiste. |

### Lo que no está dicho en ninguna parte
- El criterio de éxito.
- La cifra del retorno.
- En qué consiste la propuesta principal.
- Que Hogares lo pida.
- Quién decide qué se construye.
- Qué proyecto lo ejecuta: ninguno está declarado.
- Qué cuenta como `volumen_mensual`: el tablero no define la métrica y tiene un solo punto.
- Qué necesita cada requerimiento: el acta solo trae el número y un nombre genérico.
- Quién es el proveedor y qué tiempo se pactó.

### Qué dice el cálculo sobre los 13 requerimientos
Son 9 aceptados y 4 propuestos, y el cálculo dio 32 hallazgos:
- **Evidencia vencida:** 9, porque la única entrevista tiene 13 meses y el umbral es 12.
- **Aceptados sin evidencia:** 4 (REQ-2026, REQ-4903, REQ-4904 y REQ-4907). Solo 5 de los 9 aceptados tienen evidencia (55,6 %).
- **Aceptados sin proyecto:** 9, es decir, ninguno tiene traza (0,0 %).
- **Propuestos sin decidir:** 4, entre 75 y 172 días.
- **Sin doliente:** 2 (REQ-4907 y REQ-4910).
- **Aceptados sin criterio de aceptación:** 2 (REQ-4907 y REQ-4911).

El comité tuvo un solo asistente, Diana Molina, que además es doliente de dos de esos requerimientos. Su única decisión fue «Se mantiene el plan».

Una salvedad: ligué la entrevista a los requerimientos porque el acta dice «Cliente entrevistado» y hay una sola ronda. La entrevista no nombra ningún requerimiento, así que es lectura del acta, no cita directa.

### Qué le falta a tu carpeta
- Transcripciones completas y entrevistas recientes que nombren a Hogares.
- La serie de `volumen_mensual`, con su definición y más de un punto.
- Un documento de decisión que diga quién decide y qué se decidió en cada requerimiento. Sin él, un requerimiento descartado se ve igual que uno que nadie miró.
- Una fuente para el 272.424 distinta del propio caso de negocio.

### Lo que falló
`sellar` respondió «no hay una corrida abierta: sellar va después de corrida-inicio». El comando dice que aquí no va `corrida-inicio`, así que no lo abrí por mi cuenta. La lectura quedó sin sellar y conviene revisar esa instrucción.

### Archivos y siguiente paso
La corrida quedó registrada como `2026-10-17-product-setup-1`. El texto completo está en `estado-producto/PRD-309/corridas/salida-product-setup.md`.

El siguiente paso es `/product-discovery` sobre las entrevistas. Con una sola cita hay poco que convertir en requerimientos, y las entrevistas nuevas son lo que más movería este resultado.