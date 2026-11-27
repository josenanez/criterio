[English](DISENO.md) · [← La familia](README.es.md)

# criterio-cdo · el diseño de la familia

**Estado: estable, lanzada en su versión 1.0.0.** Los comandos, los skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista contra el material de
`tests/criterio-cdo/`. En la 0.2.0, las dos agentes corrieron sobre todas las entidades del material, con una clave que no ven; en la 1.0.0, la ronda 2 en Colombia, México y Perú: 94 señales y 348 datos, con un piso del 96,0 % en las señales y del 98,9 % en los datos, y ningún control con una señal: [las rondas](../../tests/evidencias/familias/cdo/RONDAS.md). Alcance en [ADR 0034](../../docs/decisions/0034-la-familia-cdo.md).

**Esta es la hoja de diseño de la familia**: las señales que calcula el código, cada comando con su
entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, la
estructura de carpetas y la hoja de ruta están en su [página](README.es.md).

El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —quién es el dueño de un dato, cuál
cifra es la correcta— es siempre del área de datos. **Las agentes procesan exportaciones y metadatos**:
nunca se conectan a una base ni procesan un dato personal.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json).

## Un agente por rol

<!-- cdo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| El gobierno de los datos | **Custodia** — del latín *custodia*, la guarda: cada dato con quien responde por él | `criterio-data-governance` | El catálogo de datos contra sus dueños, su clasificación, su conservación y sus políticas: el conjunto sin dueño o sin clasificar, la política con la revisión vencida, lo que se conserva más de lo que dice la política, el término del informe que no está en el glosario y la base con datos personales que no está en el registro de la organización |
| La calidad y el linaje | **Ariadna** — la del hilo que lleva de vuelta por el laberinto: cada cifra hasta su fuente | `criterio-data-quality` | Cada cifra de un informe de dirección contra su fuente, su corte y su linaje, y cada regla de calidad contra su umbral: la cifra sin fuente, la que no coincide con su fuente en el mismo corte, la que sale de otro corte, el linaje que se corta, la regla bajo su umbral, la que no corrió y el dato crítico sin regla |
<!-- /cdo:agentes -->

## Las señales: lo que calcula el código

<!-- cdo:senales · generado por scripts/familias.py; no se edita a mano -->
**Custodia · El gobierno de los datos**

| Señal | Se levanta cuando |
|---|---|
| `dataset_without_owner` | Un conjunto de datos del catálogo no tiene un dueño de negocio |
| `dataset_without_classification` | Un conjunto no tiene su clasificación de confidencialidad |
| `policy_review_overdue` | Una política de datos o de conservación pasó su fecha de revisión |
| `retention_exceeded` | Un conjunto conserva registros más tiempo del que fija la política para su tipo |
| `term_not_in_glossary` | Un término de un informe de dirección no tiene su definición en el glosario de negocio |
| `personal_data_unregistered` | Un conjunto con datos personales no está en el registro de bases de datos personales de la organización |

**Ariadna · La calidad y el linaje**

| Señal | Se levanta cuando |
|---|---|
| `figure_without_source` | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas |
| `figure_differs_from_source` | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización |
| `cutoff_mismatch` | La cifra del informe es la de la fuente en un corte distinto al que el informe declara |
| `lineage_broken` | Un paso del linaje de una cifra no tiene su sistema de origen |
| `quality_rule_below_threshold` | El resultado de una regla de calidad en el periodo está bajo su umbral |
| `quality_rule_not_run` | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo |
| `critical_data_without_rule` | Un dato marcado como crítico no tiene ninguna regla de calidad |
<!-- /cdo:senales -->

## Los comandos de Custodia, en orden de importancia

<!-- cdo:comandos-custodia · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `governance-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país y el periodo | Inventario de lo que hay; procesa la exportación del catálogo y el registro de bases de datos personales de `10-catalogo/` y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `governance-scan` | Las políticas y el glosario de `00-referencia/`, el catálogo de `10-catalogo/`, los informes de `20-informes/` y la ficha del periodo | Lleva a la ficha cada política con su fecha de revisión, cada plazo de conservación y cada término de los informes, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `catalog-check` | La exportación del catálogo de `10-catalogo/` | Cada conjunto del catálogo contra su dueño de negocio y su clasificación de confidencialidad | Los conjuntos sin dueño o sin clasificación, con su fila |
| 3 | `retention-check` | La ficha —las políticas y los plazos de conservación— y el catálogo | Cada política contra su fecha de revisión y cada conjunto contra el plazo de conservación de su tipo | Las políticas con la revisión vencida y los conjuntos que conservan registros más allá de su plazo, con los días |
| 4 | `glossary-check` | La ficha —los términos de los informes—, el glosario de `00-referencia/` y el registro de bases de datos personales | Cada término de los informes de dirección contra el glosario de negocio, y cada conjunto con datos personales contra el registro de bases de la organización | Los términos sin definición y las bases con datos personales fuera del registro, con su cita |
| 5 | `governance-wake` | La configuración y el registro de corridas | Decide si toca procesar el gobierno —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cdo:comandos-custodia -->

## Los comandos de Ariadna, en orden de importancia

<!-- cdo:comandos-ariadna · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `lineage-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo y la diferencia que tolera la política de datos entre una cifra y su fuente | Inventario de lo que hay; procesa el linaje, las cifras de la fuente y las reglas de calidad de `30-calidad/` y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `lineage-scan` | Los informes de `20-informes/`, el linaje y las reglas de `30-calidad/`, y la ficha del periodo | Lleva a la ficha cada cifra de los informes —su indicador, su valor y su corte—, con la cita; recalcula las señales | Lo que entró a la ficha; los informes que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `figure-check` | La ficha —las cifras de los informes— y las cifras de la fuente de `30-calidad/` | Cada cifra de un informe contra la de su fuente al mismo corte, con la tolerancia de la política; si coincide con la de otro corte, lo dice | Las cifras sin fuente, las que no coinciden y las que salen de otro corte, con las dos citas |
| 3 | `lineage-check` | La exportación del linaje de `30-calidad/` | Cada paso del linaje de cada indicador contra su sistema de origen | Los pasos sin sistema de origen, con su fila |
| 4 | `rule-check` | Las reglas, sus resultados y los datos críticos de `30-calidad/` | Cada regla contra su umbral y su resultado del periodo, y cada dato crítico contra las reglas que lo miden | Las reglas bajo su umbral, las que no corrieron sobre un dato crítico y los datos críticos sin regla |
| 5 | `lineage-wake` | La configuración y el registro de corridas | Decide si toca procesar la calidad —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cdo:comandos-ariadna -->

## Cifras de terceros

<!-- cdo:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Comité de Supervisión Bancaria de Basilea), C-02 (Nagle), C-03 (Nagle).
<!-- /cdo:cifras -->

## Decisiones cerradas

- Los nombres, Custodia y Ariadna, y la estructura: dos agentes, sus trece señales y sus comandos (decisión 0034).
- Procesa exportaciones y nunca se conecta a una base; no procesa los datos personales, solo sus metadatos (decisión 0015, conservada en la 0034).
- Lo que exige la ley de cada país sobre el registro de bases de datos personales no sostiene ninguna señal hasta verificarse país por país: mientras tanto, Custodia compara el catálogo con el registro de la organización.
- ISO 8000 queda fuera de la 0.1.0 hasta verificar sus partes vigentes.
