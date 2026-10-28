[English](DISENO.md) · [← La familia](README.es.md)

# criterio-cso · el diseño de la familia

**Estado: en construcción.** Los doce comandos, los ocho skills y el motor de cálculo se construyen
sobre el núcleo común; el motor pasa su prueba determinista contra el material de Colombia y México
(`tests/criterio-cso/`), y la ronda con los agentes es el siguiente paso. Alcance en
[ADR 0019](../../docs/decisions/0019-scope-comercial-cso.md).

**Esta es la hoja de diseño de la familia**: los documentos que procesa, las señales que calcula el código, cada comando con su entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, sus fichas y sus invariantes, la estructura de carpetas, Rostrum, la cadencia, las pruebas y la hoja de ruta están en su [página](README.es.md).

Dos agentes que extienden la capacidad de la función comercial: procesan las exportaciones del CRM,
la evidencia de cada oportunidad, las cotizaciones y la liquidación de comisiones, y las contrastan
contra la tabla de etapas, la matriz de descuentos, el plan de comisiones y las fichas de Fidel y
de Clara. El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —el pronóstico que se
compromete, el descuento que se aprueba, la meta— la toma siempre una persona.

Primera versión: Colombia y México. **No califica personas**: dice qué oportunidad no tiene
evidencia y qué comisión no es la del plan, nunca quién vende mejor.

**Cómo trabajan.** Automatizados: procesan los documentos, calculan las señales y preparan cada
entregable sin intervención. Semiautomatizados cuando falta un dato que ningún documento trae —de
qué CRM sale la exportación, qué columna trae cada dato, en cuántos días se factura—: entonces le
preguntan a la persona, dicen qué preguntaron y siguen con la respuesta.

**Fuentes.** Toda fuente que se usa para procesar —el marco del rol, el formato de cada
exportación, las cifras de terceros— está en [`FUENTES.es.md`](FUENTES.es.md) con su versión, su
enlace, la fecha de consulta y su estado. El diseño, la documentación y las pruebas citan esas
fuentes por su identificador.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se
escriben aquí: salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y
[`fuentes.json`](fuentes.json), que `scripts/familias.py` escribe en este diseño, en
`FUENTES.es.md`, en la página de la familia, en los README de los plugins y, con `scripts/criterio-familias.mjs`, en el portal.

**Lo que más se pregunta**, en [`PREGUNTAS.es.md`](PREGUNTAS.es.md) ([English](PREGUNTAS.md)), y **hacia dónde va**, en la [hoja de ruta](README.es.md#hoja-de-ruta).

## Un agente por rol

<!-- cso:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| El pronóstico | **Augusto** — del latín *augur*, el que lee las señales antes de que pasen: el pronóstico contra lo que lo sostiene | `criterio-sales` | El embudo contra su evidencia y el pronóstico contra lo que lo sostiene: cada oportunidad contra el documento que exige su etapa, las detenidas, los cierres que se corren, lo comprometido contra lo ponderado con evidencia y la meta contra lo cerrado |
| De la venta a la factura | **Valeria** — del latín *valere*, valer: lo que vale lo vendido cuando está firmado y facturado | `criterio-revenue` | El precio y el descuento contra su política, y lo ganado contra lo firmado y lo facturado: cada descuento contra el nivel que lo aprueba, cada venta ganada contra su contrato en las fichas de Fidel, cada contrato firmado contra su factura en las de Clara, y cada comisión contra el plan |
<!-- /cso:agentes -->

## Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| La exportación de oportunidades del CRM | CSV o Excel, con la fecha de la exportación en el nombre: Salesforce (F-02), HubSpot (F-04, F-05) o cualquier otro con su mapeo de columnas | Augusto, Valeria |
| El historial de la fecha de cierre | CSV o Excel de Salesforce (F-03), si el CRM lo exporta | Augusto |
| La tabla de etapas: el documento que exige cada una, su probabilidad y si es abierta, ganada o perdida | Excel o CSV | Augusto |
| Las metas del periodo, por línea si las hay | Excel o CSV | Augusto |
| El acta o el paquete del comité comercial con el pronóstico comprometido | Word, PDF o correo | Augusto |
| La propuesta, la orden de compra y el acta de aceptación de cada oportunidad | Cualquier formato, con el id de la oportunidad al inicio del nombre | Augusto |
| La matriz de descuentos: el tope de cada nivel y quién lo aprueba | Excel o CSV | Valeria |
| Cada cotización o pedido, con su descuento y su aprobación | Word, PDF o correo, con el id de la cotización al inicio del nombre | Valeria |
| La tabla de cuentas: cada cuenta del CRM con la identificación del cliente | Excel o CSV | Valeria |
| El plan de comisiones y la liquidación de cada periodo | Excel o CSV | Valeria |
| Las fichas de los contratos de Fidel y las de la facturación de Clara | Las que ellos escriben en su estado | Valeria |

Las columnas que necesita cada tabla, y sus variantes, en el skill `sales-intake`; cómo se procesa
cada exportación, en el skill `crm-exports`. Dónde va cada documento, en la
[estructura de carpetas recomendada](README.es.md#la-estructura-de-carpetas-recomendada).

### Lo que procesa el motor y lo que extrae el agente

Como en las familias CFO y CLO ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)),
el motor procesa las tablas directamente —las exportaciones del CRM, el historial, las etapas, las
metas, la matriz de descuentos, la tabla de cuentas, el plan y la liquidación de comisiones—, y el
agente extrae a la ficha lo que solo trae un documento escrito: **cada documento de evidencia** de
una oportunidad con su tipo, su monto y su fecha; **el pronóstico comprometido** del acta del
comité; **cada cotización** con su precio de lista, su descuento y su aprobación. Cada dato con su
cita.

**Lo que cruza familias va por las fichas.** El contrato lo dice la ficha de Fidel y la factura la
de Clara: Valeria las toma de su estado y no vuelve a procesar un contrato ni una factura
electrónica. El cruce es por la identificación del cliente, que la tabla de cuentas pone al lado de
cada cuenta del CRM.

## Las señales: lo que calcula el código

<!-- cso:senales · generado por scripts/familias.py; no se edita a mano -->
**Augusto · El pronóstico**

| Señal | Se levanta cuando |
|---|---|
| `stage_without_evidence` | Una oportunidad está en una etapa y no tiene el documento que esa etapa exige: la propuesta enviada, la orden de compra |
| `stalled_opportunity` | Una oportunidad abierta no tiene actividad registrada en los días configurados |
| `close_date_slipped` | La fecha de cierre de una oportunidad se movió más veces de las configuradas |
| `forecast_unsupported` | Lo comprometido supera lo que suman las oportunidades con evidencia, ponderadas por su etapa, más de la tolerancia configurada |
| `target_vs_closed` | Lo cerrado al corte se aparta de la meta del periodo, prorrateada por los días transcurridos, más del umbral |

**Valeria · De la venta a la factura**

| Señal | Se levanta cuando |
|---|---|
| `discount_outside_policy` | Un descuento supera el tope de su nivel y no tiene la aprobación que pide la matriz, o ningún nivel lo cubre |
| `won_without_contract` | Una oportunidad ganada no tiene su contrato firmado en la ficha de Fidel |
| `signed_without_invoice` | Un contrato firmado no tiene su factura en la ficha de Clara dentro del plazo de facturación |
| `commission_differs_from_plan` | La comisión liquidada no es la que da el plan sobre lo cerrado y facturado |
<!-- /cso:senales -->

Los días sin actividad, las veces que se puede correr un cierre, la tolerancia del pronóstico, el
umbral de la meta, el plazo de facturación y la tolerancia de la comisión son configuración de cada
organización, con un valor por defecto declarado; ninguno es una norma.

## Las tres clases, como en la familia PMO

**A · Lo que hace, y hoy consume tiempo de alguien:** preparar el comité comercial con el embudo
limpio, revisar qué oportunidad no tiene su propuesta o su orden de compra, armar el pronóstico
ponderado, revisar los descuentos contra la matriz, conciliar lo ganado con lo facturado y revisar la
liquidación de comisiones.

**B · Lo que hace, y hoy no se hace:** revisar todas las oportunidades, no una muestra, contra la
evidencia de su etapa; contar cuántas veces se corrió cada cierre; separar lo comprometido que tiene
evidencia de lo que no; cruzar cada venta ganada con su contrato y cada contrato con su factura;
recalcular cada comisión con el plan.

**C · Lo que no hace:** no escribe ni cambia nada en el CRM; no contacta a un cliente; no aprueba
un descuento ni una excepción de precio; no fija ni cambia una meta; no liquida ni corrige una
comisión; no califica ni compara a las personas del equipo.

## Los comandos de Augusto, en orden de importancia

<!-- cso:comandos-augusto · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `sales-setup` | La carpeta raíz. Preguntas: entidad y NIT o RFC, país, el periodo, de qué CRM sale la exportación de `10-crm/` —Salesforce, HubSpot u otro, en CSV o Excel— y, si es otro, qué columna trae cada dato, la tabla de etapas de `00-referencia/` con el documento que exige cada una y su probabilidad, cuántos días sin actividad detienen una oportunidad y cuántas veces puede correrse un cierre | Inventario de lo que hay; reconoce el formato de cada exportación por sus columnas (F-02, F-04); compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; cada exportación con su formato, su fecha y sus oportunidades; las columnas que faltan; la primera ficha del periodo |
| 1 | `pipeline-scan` | `10-crm/` completo, `20-comite/` y `30-evidencia/` | El código procesa cada exportación con su fecha y compara cada oportunidad con la exportación anterior: etapa, monto y fecha de cierre; el agente lleva a la ficha del periodo cada documento de `30-evidencia/` —la propuesta, la orden de compra, el acta de aceptación— con su oportunidad, su tipo, su monto y su fecha, y el pronóstico comprometido del acta del comité, cada dato con su cita; el motor valida la ficha | Qué cambió entre la exportación anterior y la última; las oportunidades nuevas, ganadas y perdidas; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `pipeline-check` | La última exportación de `10-crm/`, las anteriores, la tabla de etapas de `00-referencia/` y la ficha del periodo | Cada oportunidad abierta contra el documento que exige su etapa; los días desde su última actividad; las veces que su fecha de cierre se corrió entre una exportación y otra, o en el historial de campos si llega | Las oportunidades sin el documento de su etapa, las detenidas y las que corrieron su cierre, cada una con su cita; sin calificar a quien la lleva |
| 3 | `forecast-check` | El pronóstico comprometido de la ficha, la última exportación de `10-crm/` y la tabla de etapas de `00-referencia/` | Lo cerrado del periodo más las oportunidades abiertas que cierran en él con la evidencia de su etapa, cada una por su monto y la probabilidad de su etapa, contra lo comprometido; la diferencia contra la tolerancia configurada | Lo comprometido, lo cerrado, lo ponderado con evidencia y lo ponderado sin ella; la diferencia; las oportunidades que lo sostienen y las que no |
| 4 | `target-check` | Las metas de `00-referencia/` y la última exportación de `10-crm/` | Lo ganado con cierre en el periodo hasta la fecha de corte contra la meta del periodo prorrateada por los días transcurridos, por línea si la meta la trae; la diferencia contra el umbral configurado | La meta, lo esperado al corte, lo cerrado y la diferencia por línea; nunca por persona |
| 5 | `sales-wake` | La configuración y la ficha | Decide qué toca: una exportación nueva en `10-crm/`, un acta nueva del comité, el cierre del periodo que se acerca y una revisión semanal | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /cso:comandos-augusto -->

## Los comandos de Valeria, en orden de importancia

<!-- cso:comandos-valeria · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `revenue-setup` | La carpeta raíz. Preguntas: entidad y NIT o RFC, país, el periodo, la matriz de descuentos, el plan de comisiones y la tabla de cuentas de `00-referencia/`, dónde están las fichas de los contratos de Fidel y las de la facturación de Clara, y en cuántos días se factura un contrato firmado | Inventario de lo que hay; compara la carpeta con la estructura recomendada; comprueba que cada cuenta ganada tenga su identificación en la tabla de cuentas; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las cuentas sin identificación; si encontró las fichas de Fidel y de Clara; la primera ficha del periodo |
| 1 | `deal-scan` | `40-cotizaciones/` completo y la última exportación de `10-crm/` | Reprocesa solo lo que cambió; el agente lleva a la ficha del periodo cada cotización o pedido con su oportunidad, su precio de lista, su descuento y quién lo aprobó con qué cargo y en qué fecha, cada dato con su cita; el motor valida la ficha | Qué cambió; qué cotizaciones son nuevas; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `discount-check` | La matriz de descuentos de `00-referencia/` y la ficha del periodo | Cada descuento contra el nivel de la matriz que lo cubre y la aprobación que ese nivel pide; un descuento que ningún nivel cubre siempre se señala | Cada cotización con su descuento, su nivel, la aprobación que pide y la que tiene; las que quedan fuera de la política, con su cita |
| 3 | `won-to-invoice` | La última exportación de `10-crm/`, la tabla de cuentas de `00-referencia/`, las fichas de los contratos de Fidel y las de la facturación de Clara | Cada oportunidad ganada contra un contrato firmado con su cliente en las fichas de Fidel; cada contrato firmado con un cliente contra una factura emitida a ese cliente en las fichas de Clara, dentro del plazo de facturación | Lo ganado sin contrato y lo firmado sin factura, cada uno con su cita en el CRM y en la ficha del otro agente; los contratos no se vuelven a procesar |
| 4 | `commission-check` | El plan de comisiones de `00-referencia/`, la liquidación del periodo de `50-comisiones/`, la última exportación de `10-crm/` y las fichas de la facturación de Clara | Lo que el plan da sobre lo ganado en el periodo y ya facturado, por responsable de la oportunidad y por línea, contra lo que se liquidó; la diferencia contra la tolerancia configurada | Por responsable: lo que da el plan, lo liquidado y la diferencia, con las oportunidades que forman la base; no se publica en Rostrum salvo que la configuración lo diga |
| 5 | `revenue-wake` | La configuración y la ficha | Decide qué toca: cotizaciones nuevas, una oportunidad ganada sin contrato ni factura cuando vence su plazo, la liquidación del periodo cuando llega y una revisión semanal | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /cso:comandos-valeria -->

## El formato común de los reportes

El mismo de las demás familias, y lo escribe el motor: encabezado, lo que hay que atender, el
resultado propio del comando, lo que no se pudo procesar, las preguntas que hizo y las fuentes.

## Lo que se reusa de las demás familias

- `texto.py` para Word, Excel, PowerPoint, PDF y correo, `terminos.py` para la aceptación de los
  términos, `rastro.py` para el rastro de cada corrida y `raiz.py` para la carpeta raíz, copiados
  de la familia PMO por `scripts/sincronizar.py`.
- `nucleo.py` —tablas, fechas, inventario, señales y reporte—, copiado de `criterio-finance`.
- La forma de la ficha: cita por dato, declarado contra evidenciado, «no encontrado» válido.
- Las fichas de los contratos de Fidel y la facturación emitida de Clara, que Valeria lee de su
  estado.
- Los términos por versión con su comprobante, el registro de versiones y las puertas de
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, para publicar los reportes del embudo y de la venta a la factura
  ([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

Lo nuevo es el motor propio, `ventas.py`, con librería estándar: procesa las exportaciones del CRM
directamente, y el agente extrae a la ficha solo lo que trae un documento escrito. Vive en
`criterio-sales` y se copia a `criterio-revenue`, con los skills `sales-intake` y `crm-exports`.

## Cómo se prueba

Material sintético en `tests/criterio-cso/`: dos industrias por país —Colombia y México—, con una
exportación de Salesforce, una de HubSpot y una de CSV con su mapeo, y un control por país, con una
clave que el motor no ve. Cada señal de la familia se siembra al menos una vez; qué se siembra y
dónde, en [`tests/criterio-cso/EVIDENCIA.md`](../../tests/criterio-cso/EVIDENCIA.md). La
extracción del agente se prueba en la ronda, sobre el mismo material. La familia se declara probada
con una ronda completa.

## Cifras de terceros

<!-- cso:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Xactly con Regina Corso Consulting), C-02 (Salesforce), C-03 (Gartner).
<!-- /cso:cifras -->

## Decisiones cerradas

- El alcance: la función comercial, con dos agentes, sus nueve señales y lo que nunca hacen (ADR
  0019). José, 2026-10-28.
- Los nombres, Augusto y Valeria. José, 2026-10-28.
- Las exportaciones: Salesforce y HubSpot con su lector, y cualquier CSV o Excel con su mapeo de
  columnas. José, 2026-10-28.
- La comisión entra en el primer incremento: las nueve señales desde el primero. José, 2026-10-28.
- Los países: Colombia y México primero. José, 2026-10-28.
- Los plugins: `criterio-sales` para Augusto y `criterio-revenue` para Valeria.

## Decisiones abiertas

1. Microsoft Dynamics y Zoho, cada uno con su fuente verificada, en el incremento 2.
2. La lista de precios contra el precio de cada cotización, como una señal más.
