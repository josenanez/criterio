[English](DISENO.md) · [← La familia](README.es.md)

# criterio-cmo · el diseño de la familia

**Estado: construida y probada, en laboratorio (versión 0.2.0).** Los comandos, los skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista contra el material de
`tests/criterio-cmo/`. En la 0.2.0, los dos agentes corrieron sobre todas las entidades del material, con una clave que no ven: [las rondas](../../tests/evidencias/familias/cmo/RONDAS.md). Alcance en [ADR 0036](../../docs/decisions/0036-la-familia-cmo.md).

**Esta es la hoja de diseño de la familia**: las señales que calcula el código, cada comando con su
entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, la
estructura de carpetas y la hoja de ruta están en su [página](README.es.md).

El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —aprobar una pieza, ampliar un
presupuesto, decidir cuál cifra es la correcta— es siempre de legal, del área de mercadeo y de quien firma el
informe. **Los agentes procesan documentos y exportaciones**: nunca se conectan a una plataforma ni procesan
los datos de una persona.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json).

## Un agente por rol

<!-- cmo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| Lo que se anuncia | **Lucía** — del latín *lux*, la luz: cada afirmación, a la luz de su soporte | `criterio-claims` | Cada pieza aprobada contra su soporte, cada promoción contra sus condiciones publicadas y cada base de contactos contra su autorización: la afirmación sin soporte, la comparativa sin fuente, la promoción sin vigencia o sin condiciones, la pieza pagada a un influenciador sin identificarse como publicidad, la pieza publicada sin la aprobación de legal y la base usada sin autorización para mercadeo |
| Lo que se invierte | **Próspero** — del latín *prosperus*, el que hace que algo rinda: cada peso de la pauta contra lo que produjo | `criterio-campaigns` | El presupuesto de cada campaña contra la pauta facturada y contra su resultado medido: la campaña que pasó su presupuesto, la factura de pauta sin campaña ni orden, la campaña sin meta ni indicador, el resultado reportado que no coincide con la plataforma y la pauta facturada después de la fecha de fin |
<!-- /cmo:agentes -->

## Las señales: lo que calcula el código

<!-- cmo:senales · generado por scripts/familias.py; no se edita a mano -->
**Lucía · Lo que se anuncia**

| Señal | Se levanta cuando |
|---|---|
| `claim_without_substantiation` | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes |
| `comparative_claim_without_source` | Una afirmación comparativa no cita su fuente ni su fecha |
| `promotion_terms_missing` | Una promoción no publica su vigencia o sus condiciones de modo y lugar |
| `sponsored_content_unidentified` | Una pieza pagada a un influenciador no se identifica como publicidad |
| `piece_published_unapproved` | Una pieza se publicó sin la aprobación que pide la política, o antes de ella |
| `contact_base_without_consent` | Una base de contactos usada en una campaña no tiene autorización para mercadeo |

**Próspero · Lo que se invierte**

| Señal | Se levanta cuando |
|---|---|
| `campaign_over_budget` | La pauta facturada de una campaña supera su presupuesto más la tolerancia de la política |
| `media_invoice_unmatched` | Una factura de pauta no tiene campaña del plan ni orden de compra |
| `campaign_without_goal` | Una campaña no tiene meta ni indicador de medición |
| `result_differs_from_platform` | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia |
| `campaign_ran_past_end` | Hay pauta facturada después de la fecha de fin de la campaña |
<!-- /cmo:senales -->

## Los comandos de Lucía, en orden de importancia

<!-- cmo:comandos-lucia · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `claims-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país y el periodo | Inventario de lo que hay; procesa el registro de piezas de `10-piezas/`, el registro de bases de contactos de `40-bases/` y el plan de `50-campanas/`, y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `claims-scan` | Las piezas de `10-piezas/`, los soportes de `20-soportes/`, las bases de `30-promociones/` y la ficha del periodo | Lleva a la ficha cada afirmación de cada pieza con su soporte, y cada promoción con su vigencia y sus condiciones, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `claim-check` | La ficha —las afirmaciones de cada pieza— y la carpeta de soportes de `20-soportes/` | Cada afirmación contra el soporte que está en la carpeta, y cada comparativa contra la fuente y la fecha que la pieza cita | Las afirmaciones sin soporte y las comparativas sin fuente, con la pieza |
| 3 | `promo-check` | La ficha —cada promoción con su vigencia y sus condiciones— y las bases de `30-promociones/` | Cada promoción contra su inicio, su fin y sus condiciones de modo y lugar, tal como las publican sus bases | Las promociones a las que les falta la vigencia o las condiciones, con sus bases |
| 4 | `approval-check` | El registro de piezas de `10-piezas/`, el registro de bases de `40-bases/` y el plan de `50-campanas/` | Cada pieza publicada contra su aprobación; cada pieza pagada a un influenciador contra su identificación como publicidad; cada base que usa una campaña contra su autorización para mercadeo | Las piezas publicadas sin aprobación o antes de ella, las pagadas sin identificar y las bases usadas sin autorización |
| 5 | `claims-wake` | La configuración y el registro de corridas | Decide si toca procesar las piezas —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cmo:comandos-lucia -->

## Los comandos de Próspero, en orden de importancia

<!-- cmo:comandos-prospero · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `campaigns-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo y las dos tolerancias de la política: sobre el presupuesto y entre un resultado y la plataforma | Inventario de lo que hay; procesa el plan de mercadeo, las facturas de pauta y la exportación de la plataforma de `50-campanas/`, y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `campaigns-scan` | El informe de resultados y las tablas de `50-campanas/`, y la ficha del periodo | Lleva a la ficha cada resultado que reporta el informe —su campaña, su indicador, su valor y su corte—, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `budget-check` | El plan de mercadeo y las facturas de pauta de `50-campanas/` | La pauta facturada de cada campaña contra su presupuesto y la tolerancia de la política; cada campaña contra su meta y su indicador; la pauta contra la fecha de fin | Las campañas que pasaron su presupuesto, las que no tienen meta y las que siguieron después de su fin, con la diferencia y los días |
| 3 | `invoice-check` | Las facturas de pauta y el plan de mercadeo de `50-campanas/` | Cada factura de pauta contra la campaña del plan a la que pertenece y su orden de compra | Las facturas sin campaña, con una campaña que no está en el plan o sin orden de compra |
| 4 | `result-check` | La ficha —los resultados del informe— y la exportación de la plataforma de `50-campanas/` | Cada resultado reportado contra el valor de la plataforma para la misma campaña, el mismo indicador y el mismo corte, con la tolerancia de la política | Los resultados que no coinciden con la plataforma, con la diferencia |
| 5 | `campaigns-wake` | La configuración y el registro de corridas | Decide si toca procesar las campañas —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cmo:comandos-prospero -->

## Cifras de terceros

<!-- cmo:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Gartner), C-02 (Gartner), C-03 (Association of National Advertisers (ANA)).
<!-- /cmo:cifras -->

## Decisiones cerradas

- Los nombres, Lucía y Próspero, y la estructura: dos agentes, sus once señales y sus comandos (decisión 0036).
- El mercadeo entra por lo que vive en documentos —lo que se anuncia y lo que se invierte—; las plataformas de pauta y de analítica, solo por sus exportaciones (decisión 0036, que sigue a la 0019).
- De una base de contactos se procesa solo su registro: cuántos registros, con qué autorización y desde cuándo; nunca los datos de una persona.
- Si el soporte de una afirmación basta lo decide legal: la agente dice si hay uno que trate de lo mismo.
- El Estatuto del Consumidor de Colombia (F-10) se cita solo en una entidad de Colombia; la Ley 2300 de 2023, lo que pide la Ley 1581 para el mercadeo y la ley de publicidad de los demás países quedan fuera de la 0.1.0 hasta verificarse.
