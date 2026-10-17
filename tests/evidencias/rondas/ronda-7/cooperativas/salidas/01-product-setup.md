# /criterio-product:product-setup documentos/productos/PRD-305

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

## Listo — Microcrédito (PRD-305)

**Lo que miré:** 5 documentos, todos legibles. Solo 1 es material de descubrimiento: una entrevista del 2025-09-06 con una sola cita. La definición y el caso de negocio son del 2026-04-03. Lo más reciente es el acta del comité, del 2026-10-17.

**Las cuatro preguntas.** Nadie contesta en esta sesión, así que tomé la respuesta sugerida en cada una:
1. **Producto y gerente:** PRD-305 · Microcrédito · María Restrepo, como dice la definición.
2. **Quién decide qué se construye:** ningún documento lo dice. Lo dejé sin dato.
3. **Dónde guardo lo que encuentre:** `estado-producto/PRD-305`. No usé `estado/`, que es de otro agente.
4. **Términos:** el texto que sigue se mostró tal cual. José Francisco Ñáñez los aceptó para esta prueba el 2026-10-17, y así quedó registrado.

> Criterio produce borradores de trabajo, no decisiones ni asesoría. Procesa los documentos que usted le indique y dice lo que muestran; no sabe lo que se habló fuera de ellos. Puede equivocarse, y por eso cada dato viene con la cita del documento de donde salió: la verificación es suya. Sus documentos se procesan en la infraestructura de la plataforma de IA, no solo en su equipo. Cada versión se certifica antes de publicarse; garantía y responsabilidad: licencia Apache 2.0. Cada versión se acepta de nuevo y deja un comprobante en Markdown y PDF con su huella SHA-256. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

**Términos:** aceptados para la versión 0.3.13 (texto 1.1). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`. SHA-256: d85e8bd2335ac89a…

**Lo que levanté con lo escrito:** `producto.json`, la serie `volumen_mensual` y 17 requerimientos, 9 aceptados y 8 propuestos. No creé ninguno que el acta no nombre. Lo que no está escrito quedó en `not_found`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Microempresarios no tiene microcrédito» | **Parcialmente.** Una entrevista con un cliente: «Lo necesito y hoy no lo tengo.» No dice que sea microempresario ni que hable de microcrédito, aunque lleva ese título | 2025-09-06 (13 meses) |
| «La demanda se sostiene sin campaña» | **Un supuesto.** Dice «verificado con el documento técnico del proveedor del 2026-06-14», pero ese documento no está en la carpeta. Aunque estuviera, no es evidencia de demanda | declarado 2026-04-06 · 194 días sin verificar |
| Volumen mensual esperado: 216.930 | **Contrastada con una serie.** El tablero mide 207.028. La diferencia es 4,6 %, bajo el umbral del 20 %: es imprecisión, no contradicción | caso de negocio 2026-04-03 · tablero 2026-10-09 |
| Los 9 aceptados, pedidos por un «cliente entrevistado» | **Una sola entrevista, con una sola cita, que no nombra ninguno de los 17 requerimientos.** Las 14 evidencias que pude citar tienen 13 meses (umbral: 12) | 2025-09-06 |

### Lo que no está dicho en ninguna parte
- **Quién decide qué se construye.** Sin eso no hay acta de constitución posible.
- **El criterio de éxito.** El caso de negocio dice «Retorno esperado en 24 meses» sin cifra ni base.
- **La propuesta.** La definición dice solo «Propuesta principal».
- **Qué mide `volumen_mensual`.** Ningún documento define la métrica. Y la definición dice que el segmento «no tiene microcrédito», mientras el tablero ya mide 207.028 al mes.
- **El problema como hecho de mercado.** Ningún documento afirma ni niega que ningún microempresario tenga microcrédito, ni siquiera en otras entidades.
- **Qué plan se «mantiene».** La única decisión del acta es «Se mantiene el plan», y no hay ningún plan en la carpeta.
- **Quién decidió cada aceptación.** El único asistente al comité es la gerente.
- **Qué proyecto construye algo.** De los 9 aceptados, 0 tiene proyecto (0,0 %). Existe PRY-207 «Microcrédito rural», pero sus documentos no nombran PRD-305, así que no los enlacé.

### Supuestos sobre los que está escrita
Hay uno declarado: «La demanda se sostiene sin campaña». Hay otros dos que la definición no declara: que la entrevista de 2025 sigue vigente y que el segmento está desatendido.

### Lo que el registro de requerimientos ya muestra
Son hallazgos de lectura. La revisión completa es `/product-requirements`.
- **Aceptados sin proyecto:** 9 de 9.
- **Aceptados sin criterio de aceptación:** 3 (REQ-2037, REQ-4501, REQ-4514). En los demás el criterio es «se verifica en producción», que no se puede comprobar.
- **Sin doliente:** REQ-4503 y REQ-4514 (aceptados), REQ-4513 (propuesto).
- **Aceptado sin ninguna evidencia:** REQ-4504.
- **Propuestos sin decidir:** 8, entre 72 días (REQ-4512) y 206 días (REQ-4509). El umbral es 60.
- **REQ-2037** sale de la numeración 45xx y se aceptó el 2026-10-04.

### Qué le falta a tu carpeta
- Las **transcripciones de las entrevistas.** Hoy hay una sola cita.
- La **serie de la métrica**, con su definición. Hoy hay un solo punto.
- El **documento técnico del proveedor** del 2026-06-14.
- **Quién decide**, el criterio de éxito y las decisiones del comité con quién las tomó.

**No pude sellar la lectura.** `sellar` exige una corrida abierta con `corrida-inicio`, y este comando dice que aquí no se usa. No escribí el sello a mano. La próxima corrida releerá los 5 documentos.

**Después:** `/product-discovery` sobre el material de entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién lo pidió.

La corrida quedó registrada como `2026-10-17-product-setup-1`. Lo anterior, entero, está en `estado-producto/PRD-305/corridas/salida-product-setup.md`.