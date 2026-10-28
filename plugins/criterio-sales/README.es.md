<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cso-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cso-claro.svg" alt="Criterio CSO · La función comercial" height="48"></picture>

# Augusto · el pronóstico

<img src="../../docs/img/es/robot-augusto.gif" alt="Augusto" width="220" align="right">

**Augusto pone el embudo al lado de su evidencia y el pronóstico al lado de lo que lo sostiene.**
Tú respondes por el pronóstico y llevas el comité comercial. Él llega con cada oportunidad contra el
documento que exige su etapa, las detenidas, los cierres que se corren, lo comprometido contra lo
que lo sostiene y la meta contra lo cerrado.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**El nombre.** Augusto, del latín *augur*, el que lee las señales antes de que pasen: el pronóstico contra lo que lo sostiene.
<!-- /agente:nombre -->

[English](README.md) · `criterio-sales` · Apache 2.0 · Una instancia por entidad

**Estado: en construcción.** Los seis comandos, los cuatro skills y el motor de cálculo, probado
contra material sintético de Colombia y México con una clave que el agente no ve y una entidad de
control por país. **La ronda con el agente es el siguiente paso**, y hasta entonces no se publica en
el marketplace. Nada se anuncia como terminado hasta que pasen los
[criterios de aceptación](ACCEPTANCE.md).

**Esta página se lee sola.** Augusto funciona sin Valeria: si solo respondes por el pronóstico, aquí
está todo, incluidas sus pruebas. La familia —cómo se encuentra con Valeria y con Rostrum— está en
la [familia criterio-cso](../../families/criterio-cso/README.es.md).

---

## Qué es

| | |
|---|---|
| **A quién extiende** | Al responsable comercial y a quien prepara el comité comercial |
| **Sobre qué trabaja** | **El embudo de una entidad**, periodo a periodo |
| **Qué mira** | Las exportaciones de oportunidades del CRM con su fecha, la evidencia de cada oportunidad, el acta del comité, la tabla de etapas y las metas |
| **Cadencia** | Cuando llega una exportación o un acta nueva, cuando el periodo cierra en la semana, y una vez por semana |
| **Instancias** | Una por entidad |

## Qué hace

**Lo que hace y hoy no se hace: revisar todas las oportunidades, no una muestra, contra el documento
que exige su etapa**, y separar lo comprometido que tiene documentos de lo que no.

**Lo que puede responder que hoy cuesta horas antes de cada comité:** qué oportunidad está en
negociación sin propuesta enviada, cuál lleva semanas sin actividad, cuál corrió su cierre tres veces,
cuánto de lo comprometido tiene respaldo en los documentos y cómo va lo cerrado contra la meta al
corte.

<!-- cso:comandos · generado por scripts/familias.py; no se edita a mano -->
### Los seis comandos

> Se escriben con el prefijo del plugin: `/criterio-sales:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-sales:sales-setup` | La configuración, el inventario y el formato de cada exportación del CRM |
| `/criterio-sales:pipeline-scan` | La ficha del periodo al día, con lo que cambió en el embudo y las señales nuevas |
| `/criterio-sales:pipeline-check` | Cada oportunidad contra su evidencia: la que no la tiene, la detenida y la que corre su cierre |
| `/criterio-sales:forecast-check` | El pronóstico comprometido contra lo que lo sostiene, oportunidad por oportunidad |
| `/criterio-sales:target-check` | La meta del periodo contra lo cerrado al corte, por línea |
| `/criterio-sales:sales-wake` | Lo que toca hoy en el embudo; si no toca nada, se calla |
<!-- /cso:comandos -->

`sales-setup` va primero porque los demás lo necesitan, y `sales-wake` es el que se le pone a un
reloj. Entre los dos, los cuatro que preparan el trabajo: qué cambió en el embudo, el embudo contra su
evidencia, el pronóstico contra su respaldo y la meta contra lo cerrado.

<!-- cso:skills · generado por scripts/familias.py; no se edita a mano -->
### Los cuatro skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan como un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `crm-exports` | Cómo se procesa cada exportación del CRM: Salesforce por sus nombres de campo o sus etiquetas, HubSpot por sus propiedades, y cualquier CSV o Excel con su mapeo de columnas; la tabla de etapas y el historial de la fecha de cierre | Propio · también en Valeria |
| `forecast-backing` | El pronóstico ponderado por etapa con y sin evidencia, la meta prorrateada por los días del periodo y por qué nunca se compara a las personas | Propio |
| `pipeline-record` | La ficha del periodo de Augusto: cada documento de evidencia con su oportunidad, su tipo, su monto y su fecha, y el pronóstico comprometido del acta del comité, cada dato con su cita | Propio |
| `sales-intake` | La estructura recomendada de la carpeta comercial, qué va en cada carpeta y qué agente la usa, y cómo se nombran las exportaciones y la evidencia | Propio · también en Valeria |
<!-- /cso:skills -->

## Lo que cuesta hoy

<!-- cso:cifras · generado por scripts/familias.py; no se edita a mano -->
| Cifra | Fuente |
|---|---|
| **4 de cada 5** líderes de ventas y de finanzas no acertaron al menos un pronóstico trimestral de ventas en el último año; el 52 % de los líderes de ventas dice que su pronóstico se desvía un 10 % o más | [Xactly con Regina Corso Consulting, 2024 Sales Forecasting Benchmark Report, 2024](https://www.xactlycorp.com/sites/default/files/file/2024-07/2024_sales_forecasting_benchmark_report.pdf) — 405 profesionales de ventas, finanzas y operaciones de ingresos en Norteamérica, del 19 al 28 de marzo de 2024 |
| **28 %** de su semana dedica un vendedor a vender; el 72 % se va en otras tareas, sobre todo gestionar los negocios y capturar datos | [Salesforce, State of Sales, quinta edición, 2022](https://www.salesforce.com/news/stories/sales-research-2023/) — 7.775 profesionales de ventas en 38 países de Norteamérica, América Latina, Asia-Pacífico y Europa, del 24 de agosto al 30 de septiembre de 2022 |
| **84 %** de los líderes de ventas dice que la analítica comercial influyó menos de lo esperado en el desempeño; el 44 % señala la mala calidad de los datos | [Gartner, 2023](https://www.gartner.com/en/newsroom/press-releases/2024-02-06-gartner-survey-finds-sales-analytics-has-less-influence-on-sales-performance-than-what-leadership-expected) — 303 líderes de ventas, julio de 2023 |
<!-- /cso:cifras -->

## Para qué sirve

`/criterio-sales:forecast-check` pone lo comprometido en el comité al lado de lo que lo sostiene: lo
cerrado y las oportunidades que cierran en el periodo con la evidencia de su etapa, cada una por la
probabilidad de su etapa. **Lo ponderado sin evidencia se muestra aparte y no sostiene nada.**

### Y para qué no sirve

- **No escribe ni cambia nada en el CRM**, y no se conecta a él: procesa lo que el CRM exporta.
- **No propone un pronóstico ni fija una meta.** Los dos son de una persona.
- **No califica ni compara a quien vende.** El pronóstico y la meta se miran por periodo y por línea,
  nunca por persona.
- **No contacta a un cliente**, y la ficha no guarda el correo ni el teléfono de nadie.
- **No mueve, renombra ni crea nada dentro de los documentos de la organización.** Lo único que deja,
  si la persona lo autoriza, es el archivo que marca la carpeta raíz.
- **No adivina.** Cada dato lleva la cita del documento y, en las tablas, la fila de donde salió.

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura de la
plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus políticas antes de
apuntarla a material confidencial. Descargo completo en [DISCLAIMER.es.md](../../DISCLAIMER.es.md),
términos en [TERMS.es.md](../../TERMS.es.md).

## Instalación y configuración

**Todavía no está en el marketplace**: sale con su primera versión, cuando pase la ronda con el
agente. Entonces:

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-sales@criterio
/criterio-sales:sales-setup
```

Si respondes por lo vendido hasta la factura y no por el pronóstico, lo tuyo es
[Valeria](../criterio-revenue/README.es.md).

### El primer resultado

`/criterio-sales:sales-setup` no te pide que ordenes nada antes de empezar. Mira la carpeta
comercial de la entidad, la compara con la
[estructura recomendada](../../families/criterio-cso/README.es.md#la-estructura-de-carpetas-recomendada),
reconoce el formato de cada exportación del CRM —Salesforce, HubSpot u otro— y hace las preguntas que
ningún documento responde: qué columna trae cada dato si el CRM no es uno de los dos, la tabla de
etapas, los días sin actividad. En los primeros quince minutos deja ver el embudo contra su
evidencia.

### Cada cuánto corre

`/criterio-sales:sales-wake` es el comando que el reloj invoca: hace lo que toca, responde primero
las preguntas que alguien dejó en Rostrum, y **si no toca nada no produce nada.** La decisión de qué
toca es aritmética de fechas, y la toma el código:

```
python3 scripts/ventas.py despertar --config <archivo>
```

## Trabajo en equipo

| Con quién | Qué pasa |
|---|---|
| **Valeria** | Comparten el estado de la entidad y las mismas exportaciones del CRM. Valeria toma de ahí lo ganado para cruzarlo con los contratos y las facturas. Cada uno escribe solo su ficha |
| **Rostrum** | Publica sus reportes, lo que vence en el embudo y sus señales, para quien no abre una carpeta, y le devuelve las preguntas que deja quien lo mira. **No escribe en el estado** |

## Pruebas

### Cómo está construido

La espina es la **ficha del periodo**: cada documento de evidencia de una oportunidad con su tipo, su
monto y su fecha, y el pronóstico comprometido del acta del comité, cada dato con su cita. La escribe
el agente; los resultados, el motor.

[`scripts/ventas.py`](scripts/ventas.py), con la librería estándar, hace todo lo que es cálculo: lee
cada exportación desde su fuente, compara un corte con otro, cuenta los cierres que se corren, pondera
el embudo por etapa y prorratea la meta, el mismo resultado cada vez. Vive aquí y se copia a
`criterio-revenue` con el skill `sales-intake` y el `crm-exports`; `scripts/sincronizar.py --check`
falla si alguna copia se separa.

Cada fuente que se usa está en
[`families/criterio-cso/FUENTES.es.md`](../../families/criterio-cso/FUENTES.es.md), con su versión, su
enlace y su estado.

### Cómo se verifica

```
python3 scripts/ventas.py selftest                       el motor
python3 tests/criterio-cso/generar.py                    el material de Colombia y México
python3 tests/criterio-cso/evaluar.py --agente augusto   cada señal contra la clave
```

**Cómo salió la última corrida, generado desde la corrida misma:**
[`tests/criterio-sales/RESULTADOS.md`](../../tests/criterio-sales/RESULTADOS.md). Qué se siembra en
cada entidad y **qué no prueba el material**, en
[`EVIDENCIA.md`](../../tests/criterio-cso/EVIDENCIA.md). El diseño, con la entrada, el proceso y el
reporte de cada comando, en el [diseño de la familia](../../families/criterio-cso/DISENO.es.md).
