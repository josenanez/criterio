[English](DISENO.md) · [← La familia](README.es.md)

# criterio-cro · el diseño de la familia

**Estado: estable, lanzada en su versión 1.0.0.** Los comandos, los skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista contra el material de
`tests/criterio-cro/`. En la 0.2.0, los dos agentes corrieron sobre todas las entidades del material, con una clave que no ven; en la 1.0.0, la ronda 2 en Colombia, Perú y Brasil: 80 señales y 91 datos, con un piso del 95,4 % en las señales y del 95,9 % en los datos, y ningún control con una señal: [las rondas](../../tests/evidencias/familias/cro/RONDAS.md). Alcance en [ADR 0035](../../docs/decisions/0035-la-familia-cro.md).

**Esta es la hoja de diseño de la familia**: las señales que calcula el código, cada comando con su
entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, la
estructura de carpetas y la hoja de ruta están en su [página](README.es.md).

El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —aprobar un exceso, fijar un límite,
calificar un riesgo— es siempre de la junta, del comité de riesgos y de las áreas. **Los agentes procesan
exportaciones**: nunca se conectan a un sistema ni calculan capital, valor en riesgo ni pérdida esperada.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json).

## Un agente por rol

<!-- cro:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| El apetito por riesgo | **Severo** — del latín *severus*, el que no hace concesiones: cada exposición contra su límite | `criterio-risk-appetite` | La declaración de apetito contra sus límites y cada límite contra la exposición que reportan las áreas: el límite excedido sin plan ni aprobación, el reporte fuera de plazo, el límite sin dueño o con la revisión vencida, el riesgo alto de la matriz sin límite ni indicador y la declaración que la junta no ha revisado en el plazo del marco |
| Los indicadores y los eventos | **Casandra** — la que anunciaba lo que venía: cada indicador que avisa antes | `criterio-risk-events` | Los indicadores clave de riesgo contra sus umbrales y la base de eventos de pérdida contra sus registros: el indicador en alerta sin acción, el que no se reportó, el evento sin causa, sin monto o sin proceso, el que se registró fuera de plazo, el que se repite en el mismo proceso y el que no está en la matriz de riesgos |
<!-- /cro:agentes -->

## Las señales: lo que calcula el código

<!-- cro:senales · generado por scripts/familias.py; no se edita a mano -->
**Severo · El apetito por riesgo**

| Señal | Se levanta cuando |
|---|---|
| `limit_breached_without_plan` | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso |
| `limit_without_owner` | Un límite del marco no tiene dueño |
| `limit_review_overdue` | Un límite pasó su fecha de revisión |
| `exposure_report_late` | Un área reportó su exposición después del plazo que fija el marco |
| `risk_without_limit` | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave |
| `appetite_statement_outdated` | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco |

**Casandra · Los indicadores y los eventos**

| Señal | Se levanta cuando |
|---|---|
| `kri_alert_without_action` | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada |
| `kri_not_reported` | Un indicador clave no tiene valor en el periodo |
| `loss_event_incomplete` | Un evento de pérdida no tiene causa, monto o proceso |
| `loss_event_registered_late` | Un evento se registró después del plazo de la política desde que se descubrió |
| `loss_event_repeated` | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política |
| `loss_event_risk_unmapped` | Un evento no corresponde a ningún riesgo de la matriz |
<!-- /cro:senales -->

## Los comandos de Severo, en orden de importancia

<!-- cro:comandos-severo · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `appetite-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el último periodo cerrado y los plazos del marco: los días para reportar la exposición y cada cuántos meses revisa la junta la declaración | Inventario de lo que hay; procesa la matriz de riesgos, los límites y los indicadores de `00-marco/` y la exposición de `10-exposicion/`, y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `appetite-scan` | La declaración y el marco de `00-marco/`, las actas de `40-actas/`, la exposición de `10-exposicion/` y la ficha del periodo | Lleva a la ficha la fecha en que la junta revisó la declaración de apetito y cada exceso que aprobó el comité, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `limit-check` | Los límites de `00-marco/`, la exposición del periodo y los planes de acción de `10-exposicion/`, y los excesos aprobados de la ficha | Cada exposición reportada contra su límite máximo o mínimo; el exceso, contra su plan de acción o su aprobación; cada reporte, contra el plazo del marco | Los límites excedidos sin plan ni aprobación y los reportes fuera de plazo, con la diferencia y los días |
| 3 | `framework-check` | Los límites de `00-marco/` y la ficha —la declaración de apetito con su última revisión por la junta— | Cada límite contra su dueño y su fecha de revisión, y la declaración contra el plazo en que la junta la revisa | Los límites sin dueño o con la revisión vencida, y la declaración vencida, con los días |
| 4 | `coverage-check` | La matriz de riesgos, los límites y los indicadores de `00-marco/` | Cada riesgo calificado alto o crítico en la matriz contra los límites y los indicadores clave que lo miden | Los riesgos altos sin límite ni indicador, con su fila |
| 5 | `appetite-wake` | La configuración y el registro de corridas | Decide si toca procesar el apetito —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cro:comandos-severo -->

## Los comandos de Casandra, en orden de importancia

<!-- cro:comandos-casandra · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `events-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el último periodo cerrado y los plazos de la política: los días para registrar un evento y la ventana en que dos eventos cuentan como repetidos | Inventario de lo que hay; procesa los indicadores de `00-marco/`, sus valores de `20-indicadores/` y la base de eventos de `30-eventos/`, y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `events-scan` | Las actas de `40-actas/`, los valores y las acciones de `20-indicadores/`, la base de eventos de `30-eventos/` y la ficha del periodo | Lleva a la ficha cada acción sobre un indicador que quedó en un acta, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `kri-check` | Los indicadores de `00-marco/`, sus valores y sus acciones de `20-indicadores/`, y las acciones de la ficha | Cada indicador clave con su valor del periodo, contra su umbral de alerta y de límite en el sentido que fija el marco; el que está en alerta, contra su acción | Los indicadores en alerta sin acción y los que no tienen valor en el periodo |
| 3 | `event-check` | La base de eventos de pérdida de `30-eventos/` | Cada evento contra su causa, su monto y su proceso, y su fecha de registro contra el plazo de la política desde que se descubrió | Los eventos incompletos y los registrados fuera de plazo, con los días |
| 4 | `pattern-check` | La base de eventos de `30-eventos/` y la matriz de riesgos de `00-marco/` | Los eventos del mismo tipo en el mismo proceso dentro de la ventana de la política, y cada evento contra el riesgo de la matriz al que corresponde | Los eventos repetidos, con su monto, y los que no están en la matriz |
| 5 | `events-wake` | La configuración y el registro de corridas | Decide si toca procesar los eventos —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cro:comandos-casandra -->

## Cifras de terceros

<!-- cro:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte), C-02 (AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte), C-03 (AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte).
<!-- /cro:cifras -->

## Decisiones cerradas

- Los nombres, Severo y Casandra, y la estructura: dos agentes, sus doce señales y sus comandos (decisión 0035).
- Aquí CRO es Chief Risk Officer, la segunda línea; la función comercial es la familia CCO (decisión 0022).
- Procesa exportaciones y nunca se conecta a un sistema; no calcula capital, valor en riesgo ni pérdida esperada: procesa las cifras que reportan las áreas y los modelos de la organización.
- El sentido de cada límite —máximo o mínimo— y de cada indicador —mayor o menor es peor— lo dice la tabla del marco: un indicador de liquidez se excede por debajo.
- La norma de supervisión se cita solo en la entidad vigilada de su país: la Superintendencia Financiera en Colombia (F-10), la SBS en el Perú (F-11) y el Consejo Monetario Nacional en Brasil (F-12).
- COSO ERM 2017 queda fuera de la 0.1.0 hasta verificarse en su texto.
