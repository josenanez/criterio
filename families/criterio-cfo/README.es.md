<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-cfo-claro.svg" alt="Criterio CFO · Cierre, control y reporte" height="48"></picture>

# criterio-cfo · la familia de la función financiera

**Dos agentes y un portal, alrededor de dos fichas.** Cada uno extiende a una persona distinta
de la función financiera —quien cierra los libros y quien lleva el presupuesto— y ninguno habla
con el otro directamente: se hablan por sus fichas.

[English](README.md) · [← Criterio](../../README.es.md) · Apache 2.0

![Clara, Tomás y Rostrum](../../docs/img/es/robots-cfo.gif)

| | |
|---|---|
| **Alcance** | El cierre, el control y el reporte financiero de una entidad: los libros contra sus soportes, y el presupuesto contra su ejecución |
| **Objetivo** | Que el cierre deje de depender de que alguien recuerde qué falta |
| **Compuesta por** | [Clara](../../plugins/criterio-finance/README.es.md) · [Tomás](../../plugins/criterio-budget/README.es.md) · [Rostrum](../../plugins/criterio-server/README.es.md) |
| **Estado** | Construida y en prueba: el motor, probado contra el material de cuatro industrias y dos entidades de control. Una primera ronda con el agente, pequeña —banca y el control de Colombia—, ya [corrió](../../tests/evidencias/familias/cfo/RONDAS.md). **La ronda completa es el paso siguiente**, y sin ella la familia no se declara probada |
| **Enfoque** | Control y reporte |
| **Compromiso** | Generar, difundir y conservar el conocimiento es una obligación profesional |
| **Qué no es** | No reemplaza al contralor ni al equipo de planeación financiera, y no decide por ellos: procesa lo que la función ya tiene y dice qué no cuadra |
| **Licencia** | [Apache 2.0](../../LICENSE) |
| **Qué viene** | La ronda completa con el agente, y después el despliegue en una organización: [la hoja de ruta](#hoja-de-ruta) |

---

## Qué hace la familia

La función financiera tiene dos roles que trabajan sobre los mismos libros y miran cosas
distintas, y por eso la familia tiene dos agentes. Llevan nombre de persona porque **son
capacidades extendidas de personas**, y el significado de cada nombre apunta a lo que hace:
**Clara** —de *clarus*— cuida que los libros digan lo mismo que los soportes; **Tomás** —«el
gemelo»— pone el presupuesto al lado de su gemelo, la ejecución.

**Clara**, la del contralor, prepara el cierre del mes: el checklist con su evidencia, las
conciliaciones bancarias y de cuentas, cada factura electrónica de la DIAN o del SRI contra su
registro y el paquete para el auditor. Lo que hoy no hace nadie y ella sí: **procesar todas las
facturas del periodo, no una muestra**, y todas las tareas del cierre contra su evidencia.

**Tomás**, el de planeación financiera (FP&A), pone lo aprobado al lado de lo ejecutado y lo
comprometido, proyecta el cierre del año con su supuesto escrito, cruza cada traslado con su
acta y arma el material del comité como un paquete de decisiones. Toma la ejecución de la misma
contabilidad que cierra Clara, sin copiarla.

**Los dos se instalan hoy**, cada uno con su propio plugin, y tienen la misma deuda, escrita en
su página: el motor está probado contra material sintético de cuatro industrias; **la extracción del agente pasó una primera ronda pequeña, y la completa es la que sigue; nada se ha probado todavía
sobre los documentos de una organización.**

Primera versión: NIIF adoptadas localmente en Colombia y Ecuador, con la factura electrónica de
la DIAN y del SRI procesada desde su fuente técnica oficial.

---

## Cómo trabajan los dos

El modelo de lenguaje (LLM) extrae; el código calcula; el estado del cierre y del presupuesto lo
declara siempre una persona. **El motor procesa las tablas directamente** —el balance, el mayor,
los extractos, las facturas, el presupuesto—, y el agente lleva a la ficha solo lo que trae un
documento escrito: lo que alguien declara, un requerimiento que llegó por correo, un acta
([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)).

**Automatizados**: procesan los documentos, calculan las señales y preparan cada entregable sin
intervención. **Semiautomatizados** cuando falta un dato que ningún documento trae —la entidad,
el periodo, el umbral, quién aprueba—: entonces le preguntan a la persona, dicen qué preguntaron
y siguen con la respuesta.

## Los dos agentes y sus fichas

Nada se habla con nada directamente. **Cada agente escribe su ficha, y la ficha es el contrato.**

| Ficha | Una por | Qué lleva | Quién la escribe |
|---|---|---|---|
| Ficha del cierre | Entidad y periodo | Las tareas del checklist con responsable, fecha y evidencia; cada conciliación con sus partidas abiertas; las facturas electrónicas contra sus registros; el estado declarado del cierre | Clara; el estado, el contralor persona |
| Ficha del presupuesto | Área o centro de costo y año | Aprobado, ejecutado y comprometido por cuenta; la proyección del área; los traslados con su acta; el estado declarado | Tomás; el estado, el responsable del área |

Cada dato cita el documento del que sale y su fecha. «No encontrado» es una respuesta válida.

### Las siete invariantes

1. **Los agentes no se hablan entre sí.** Se hablan por sus fichas.
2. **Rostrum, el portal, no escribe.** Sirve lo que el motor ya escribió y lo dice con su fecha;
   no recalcula nada.
3. **Cada documento tiene un solo lugar.** La contabilidad del periodo vive en
   `10-contabilidad/`: Clara la cierra y Tomás saca de ahí la ejecución, sin copias entre
   carpetas.
4. **Declarado y evidenciado nunca se fusionan.** Van en campos separados de la ficha.
5. **El modelo extrae, el código calcula.** Toda cifra de un reporte sale de `finanzas.py`, con
   todos sus dígitos; si el motor no la da, no se escribe.
6. **Ningún agente declara el estado.** El del cierre lo declara el contralor; el de cada área,
   su responsable.
7. **Un escritor por archivo.** La ficha la escribe el agente y los resultados, el motor; ninguno
   escribe el del otro.

La sexta es la más fácil de romper por conveniencia y la que se lleva el sistema entero si se
rompe: si el agente declara el cierre, la comparación entre lo declarado y lo evidenciado
compara al sistema consigo mismo. No es una recomendación de la documentación: es una
restricción del camino de escritura.

## Lo que sigue siendo de las personas

Los dos roles siguen existiendo completos. Esto extiende capacidad; no sustituye función. Y el
argumento no es de cortesía, es estructural:

> **El insumo de cada agente lo produce el trabajo no delegable de su persona.**

Clara necesita que alguien haga las tareas del cierre y deje su evidencia, porque sin soporte no
hay nada que contrastar, y que el contralor declare el estado, porque esa es la línea contra la
que se compara. Tomás necesita que cada área entregue su proyección y que el comité deje escrita
su decisión, porque un traslado sin acta es justamente lo que señala.

Quitar a la persona no deja al agente solo: lo deja sin insumo. **Y ninguno de los dos registra
un asiento, aprueba un traslado, presenta una declaración ni firma.**

## La estructura de carpetas recomendada

Recomendada, no obligatoria ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)):
los agentes procesan la carpeta como esté. `finance-setup` y `budget-setup` comparan lo que
encuentran con esta estructura y, en cada corrida, dicen qué archivo está fuera de su lugar y
dónde iría; no crean, mueven ni renombran nada en los documentos de la organización. La
numeración va de diez en diez, como en la familia PMO, en el orden en que se trabaja el cierre y
el presupuesto.

<!-- cfo:carpetas · generado por scripts/familias.py; no se edita a mano -->
Una carpeta por entidad, con el NIT o el RUC al inicio del nombre: `900123456-banco-andino`. Dentro, lo que la organización entrega una vez, una carpeta por periodo contable y una por año presupuestal.

```
finanzas/
└── <entidad>/
    ├── 00-referencia/
    ├── <AAAA-MM>/
    │   ├── 10-contabilidad/
    │   ├── 20-bancos/
    │   ├── 30-facturacion/
    │   ├── 40-soportes/
    │   └── 50-auditoria/
    └── presupuesto-<AAAA>/
        ├── 10-aprobado/
        ├── 20-compromisos/
        ├── 30-proyecciones/
        └── 40-actas/
estado-finanzas/
```

**`<entidad>/`** · Lo que la organización entrega una vez

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | El plan de cuentas con la naturaleza de cada cuenta, `checklist-cierre.xlsx` en el modelo definido y el mapeo de cuentas a centros de costo y líneas presupuestales | Clara, Tomás |

**`<AAAA-MM>/`** · Un periodo contable, numerado en el orden en que se trabaja el cierre

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-contabilidad/` | Balance de comprobación y libro mayor exportados del ERP, y `auxiliares/` con un archivo por cuenta; de aquí sale también la ejecución del presupuesto | Clara, Tomás |
| `20-bancos/` | Una carpeta por cuenta, `<banco>-<últimos 4 dígitos>`, con el extracto y el auxiliar de libros | Clara |
| `30-facturacion/` | `emitidas/` y `recibidas/`, con el XML de la DIAN (F-01) o del SRI (F-04) | Clara |
| `40-soportes/` | La evidencia de cada tarea del checklist —actas, correos, conciliaciones firmadas—, con el id de la tarea al inicio del nombre | Clara |
| `50-auditoria/` | `requerimientos/` y `respuestas/` del auditor | Clara |

**`presupuesto-<AAAA>/`** · Un año presupuestal

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-aprobado/` | El presupuesto aprobado y cada versión, con su fecha en el nombre | Tomás |
| `20-compromisos/` | Órdenes de compra y compromisos exportados del ERP, con la fecha de corte en el nombre | Tomás |
| `30-proyecciones/` | La proyección de cada área, una por área y fecha | Tomás |
| `40-actas/` | Actas del comité de presupuesto, de aprobación y de traslados | Tomás |

**`estado-finanzas/`** · Lo que escriben Clara y Tomás: la configuración, las fichas, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cfo:carpetas -->

Un archivo sin el formato esperado no se adivina: se reporta con lo que le falta.

## Instalación de la familia

Cada agente es un plugin y se instala solo. **No hace falta instalar los dos**: se instala el
que resuelve el rol que tienes.

```
/plugin marketplace add josenanez/criterio

/plugin install criterio-finance@criterio     si cierras los libros
/plugin install criterio-budget@criterio      si llevas el presupuesto
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez/criterio`.

Después de instalar, cada agente tiene su propio comando de instalación que mira la carpeta,
hace las preguntas que ningún documento responde y produce un primer resultado sobre tus
propios documentos. **Nadie edita un archivo de configuración a mano.**

Y si instalas los dos, se encuentran solos: **no hay nada que conectar.** Comparten el estado
de la entidad, y cada uno escribe solo lo suyo.

## De qué responde cada agente, y dónde está su detalle

Lo mismo para cada pieza: de qué responde, qué no hace, y dónde está todo su detalle. **Cada
página de agente se lee sola** — alguien puede instalar uno sin el otro.

<!-- cfo:familia-agentes · generado por scripts/familias.py; no se edita a mano -->
| | De qué responde | Lo que nunca hace | Su página | Sus pruebas |
|---|---|---|---|---|
| **Clara** · contralor | El cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, la factura electrónica contra la contabilidad y el paquete para el auditor | No registra asientos, no firma y no declara el estado del cierre | [criterio-finance](../../plugins/criterio-finance/README.es.md) · 9 comandos, 7 skills | [resultados](../../tests/criterio-finance/RESULTADOS.md) |
| **Tomás** · FP&A | El presupuesto aprobado contra lo ejecutado y lo comprometido, la proyección al cierre del año, los traslados y el material del comité de presupuesto | No aprueba traslados, no recomienda la decisión del comité y no declara el estado de ningún área | [criterio-budget](../../plugins/criterio-budget/README.es.md) · 7 comandos, 6 skills | [resultados](../../tests/criterio-budget/RESULTADOS.md) |
| **Rostrum** · el portal | Publicar lo que escriben los agentes donde el equipo lo vea, y recibir la pregunta de quien no abre una carpeta | **No escribe en el estado ni recalcula nada**, y no decide nada | [criterio-server](../../plugins/criterio-server/README.es.md) · 2 comandos, uno para todas las familias | [resultados](../../tests/criterio-server/RESULTADOS.md) |
<!-- /cfo:familia-agentes -->

Los comandos, uno por uno —qué hacen, qué reciben, qué procesan y qué escriben—, están en el
[manual de los comandos](../../docs/manual.es.md); su entrada, su proceso y su reporte, con las
señales que calcula el motor, en el [diseño de la familia](DISENO.es.md); y las respuestas a lo
que más se pregunta, en las [preguntas frecuentes](PREGUNTAS.es.md).

## En Rostrum, el portal de todas las familias

Hasta aquí el resultado de la familia son archivos en el equipo de quien corrió los agentes.
**Un director financiero no abre una carpeta de archivos**: abre un enlace, o no abre nada. Para
eso está **Rostrum**, un plugin aparte, `criterio-server`, que sirve a la CFO junto con las demás
familias, sin que el servidor sepa nada de finanzas
([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

**Cómo entra la CFO al portal.** `/criterio-finance:finance-setup` y
`/criterio-budget:budget-setup` dejan su configuración en `.criterio/finanzas/<entidad>/` y
`.criterio/presupuesto/<entidad>/`, con la carpeta de finanzas de la entidad marcada con
`_CRITERIO_FINANZAS.txt`. Clara y Tomás comparten el estado de la entidad, y cada uno ve en el
portal sus corridas y sus reportes, no los del otro. Después, `/criterio-server:server-setup`
encuentra las dos configuraciones y las suma al mapa, y `/criterio-server:server-start` levanta el
portal. Una entidad nueva entra volviendo a correr `server-setup`.

**Lo que la CFO tiene en Rostrum:**

| Dónde | Qué |
|---|---|
| Inicio | La tarjeta **Criterio CFO** con Clara y Tomás y sus señales abiertas |
| `/familia/cfo` | Lo último que escribió el motor de cada uno —el cierre de un mes, el presupuesto de un año—, con sus señales en palabras y la fecha de cálculo, y sus reportes tal como los dejó el motor |
| Lo que vence | Las tareas del cierre y los requerimientos del auditor con fecha, ordenados con los vencimientos de las otras familias |
| `/caso/<PRY>` | Una señal de presupuesto sobre un proyecto de la PMO aparece en la página de ese proyecto |
| Dónde trabaja | La ruta completa de la carpeta raíz, de los documentos de la entidad con su marca, del estado y de cada configuración |
| Preguntar a un agente | Una pregunta para Clara o para Tomás, que la atiende en su siguiente corrida |

**No autentica a nadie, y es a propósito**: se publica detrás del control de acceso que la
organización ya tiene. No recalcula nada y no escribe en el estado. Las páginas cumplen WCAG 2.2
nivel AA, comprobado con axe-core a cuatro anchos de pantalla
(`tests/criterio-server/accesibilidad/`).

→ **[Rostrum: instalación, configuración y uso con todas las familias](https://www.josenanez.com/es/agents/rostrum)** ·
[su README, con las rutas y qué pedirle a tu organización](../../plugins/criterio-server/README.es.md)

## Cómo se configura y cada cuánto corre cada uno

Esta es la tabla que responde tres preguntas a la vez: **dónde queda cada agente, qué le hace
falta configurado, y cada cuánto tiene sentido que corra.**

<!-- cfo:configuracion · generado por scripts/familias.py; no se edita a mano -->
| | Clara | Tomás |
|---|---|---|
| **Se instala** | `criterio-finance` | `criterio-budget` |
| **Instancias** | Una por entidad | Una por entidad |
| **Se configura con** | `/criterio-finance:finance-setup` | `/criterio-budget:budget-setup` |
| **Cuánto tarda eso** | Quince minutos | Quince minutos |
| **Qué le tienes que decir** | Entidad y NIT o RUC, país, grupo NIIF (F-05, F-06), ERP, moneda, periodo, umbrales, quién aprueba, plan de cuentas | Entidad, año presupuestal, áreas o centros de costo con su responsable, la versión aprobada y su acta, el mapeo de cuentas a líneas presupuestales (en `00-referencia/`), los umbrales de desviación y, si la organización usa la familia PMO, dónde están sus fichas |
| **Dónde queda** | `.criterio/finanzas/<entidad>/config.json`, escrito por el comando | `.criterio/presupuesto/<entidad>/config.json`, escrito por el comando |
| **El que se le pone a un reloj** | `/criterio-finance:finance-wake` | `/criterio-budget:budget-wake` |
| **Qué toca cada día** | Decide qué toca según la cadencia: a diario durante la ventana del cierre, semanal fuera de ella | Decide qué toca según la cadencia: cuando aparece un periodo nuevo en `10-contabilidad/`, antes de cada comité y una vez por semana para los compromisos |
| **Qué lo despierta además del reloj** | Una pregunta que alguien dejó en Rostrum | Una pregunta que alguien dejó en Rostrum |
<!-- /cfo:configuracion -->

**Nadie edita un archivo de configuración a mano.** Si para cambiar un umbral hay que abrir un
JSON, el umbral se queda como vino y la configuración deja de describir a la organización. Se
dice en la conversación y el comando lo reescribe. Cada plugin trae su
`scripts/config.example.json` para ver la forma completa sin instalar nada; los umbrales por
defecto son configuración, no norma.

### Por qué las dos cadencias son distintas

No es una preferencia: **cada agente mide contra otra cosa.**

- **Clara** mide contra la ventana del cierre. Mientras el cierre está abierto, una tarea vencida
  o una conciliación sin actualizar cambia el estado hoy, así que corre a diario; fuera de la
  ventana, una vez por semana alcanza.
- **Tomás** mide contra la contabilidad y el comité. Su ciclo no es el calendario: es *cuando
  llega un periodo nuevo* a `10-contabilidad/` y *antes de cada comité*, y una vez por semana
  revisa los compromisos.

### Los dos se callan cuando no hay nada

Es la regla que decide si un agente sigue instalado el mes siguiente. Los dos comandos de reloj
no producen nada cuando no toca nada, y entonces la salida es una línea: qué se revisó y cuándo
vuelve. Con una pregunta abierta en Rostrum nunca se callan: la responden primero.

Un agente que produce un informe para decir que no hay novedad enseña a ignorarlo, y el día que
sí hay novedad ya nadie lo abre.

### Qué es lo que **no** está programado

**Ninguno de los dos se programa solo.** Los dos traen el comando que un reloj invoca, y el reloj
vive fuera del plugin — una tarea programada de Claude Cowork, o el programador del sistema
operativo invocando Claude en modo no interactivo. Alguien tiene que ponerlo, una vez.

Y para que corra sin nadie delante hacen falta dos cosas que no dependen de este repositorio:
**que la sesión pueda correr sin aprobar cada paso**, y **que la carpeta esté montada cuando el
reloj dispare.** Si la organización no quiere corridas desatendidas —y en una función financiera
es una respuesta razonable—, los comandos sirven corridos a mano y la cadencia sigue diciendo qué
toca.

## Las pruebas de la familia

**Una sola puerta corre todo lo que este repositorio comprueba**, de todas las familias a la vez:

```
python3 scripts/verificar.py
```

Lo propio de la CFO está en [`tests/criterio-cfo/`](../../tests/criterio-cfo/): material
sintético por industria con una clave que el motor no ve, y una entidad de control por país que
no trae ningún defecto, donde cualquier señal es una falla. Cada señal de la familia se siembra
al menos una vez. `evaluar.py` corre el motor y compara cada señal por su nombre y su clave: **una
de más cuenta igual que una de menos.**

| Qué se comprueba del conjunto | Por qué es de la familia y no de un agente |
|---|---|
| Que cada señal sembrada se levante, y ninguna en los controles | Las señales de Clara y las de Tomás salen del mismo motor y del mismo material |
| **Que las copias compartidas no se hayan separado** | `finanzas.py` y `finance-intake` viajan copiados en los dos plugins. Dos copias que se separan calculan distinto sobre los mismos documentos, y nadie sabría a cuál creerle |
| Que el diseño, las páginas y el portal digan lo que dicen las fuentes | Las tablas de agentes, comandos, señales, carpetas y skills salen de `familia.json`, `carpetas.json` y `fuentes.json`; `scripts/familias.py --check` falla si una copia no cuadra |
| Que cada campo de factura que procesa el motor esté en su fuente oficial | Un campo que no está en el anexo de la DIAN o en la ficha del SRI no se procesa ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 2) |

**El resultado de cada agente, generado desde la corrida**, en su propia página:
[Clara](../../tests/criterio-finance/RESULTADOS.md) ·
[Tomás](../../tests/criterio-budget/RESULTADOS.md). Qué se siembra en cada entidad y la señal que
tiene que levantar, con el mismo detalle, **y qué no prueba el material**, en
[`EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md). El conjunto de todas las familias, en
[`docs/pruebas.md`](../../docs/pruebas.md).

**La primera ronda con el agente** corrió sobre banca y el control de Colombia: Clara y Tomás corren sus comandos y lo que extraen de las actas, los correos y las cartas del auditor se califica contra la misma clave. Cada salida, su costo, su calificación y los comandos que se repitieron tras corregir un defecto están en [las rondas de la familia](../../tests/evidencias/familias/cfo/RONDAS.md). La ronda completa, con las cuatro industrias y los dos controles, trae el análisis estadístico de la familia, con las mismas métricas que la PMO.

## Las industrias de prueba

Cuatro industrias de Suramérica y una entidad de control por país: **banca y retail en
Colombia**, con el XML de la DIAN, y **cooperativas y minería en Ecuador**, con el del SRI. Cada
una trae el cierre de un mes y el presupuesto del año.
Las entidades, los defectos sembrados y las señales esperadas de cada una, en
[`tests/criterio-cfo/EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md).

## Hoja de ruta

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->

La familia crece por incrementos. Cada uno es una versión con su prueba completa y su análisis estadístico publicados, con las mismas métricas, para que la evolución se pueda comparar.

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.8.0 | En curso | **Construida, con el motor probado y una primera ronda con el agente**<br>· Los dieciséis comandos de Clara y Tomás, sus doce skills y el motor de cálculo<br>· La factura electrónica de la DIAN y del SRI, procesada desde su fuente técnica oficial<br>· La carpeta raíz que cada agente busca y, con permiso, marca<br>· La familia en Rostrum, con lo que vence y dónde trabaja cada agente<br>· La primera ronda con el agente: Clara y Tomás sobre banca y el control de Colombia, con los defectos que encontró corregidos | El motor, contra 4 industrias y 2 entidades de control; el agente, sobre banca y el control de Colombia |
| Incremento 2 | Siguiente | **La ronda completa con el agente**<br>· Clara y Tomás corren sus comandos sobre el material de las cuatro industrias, como la PMO en cada ronda<br>· Lo que solo traen las actas, los correos y las cartas del auditor, extraído y calificado contra la clave<br>· Con la ronda completa, la familia se declara probada | 4 industrias y 2 entidades de control, con la clave que el agente no ve |
| Incremento 3 | Reservada | **El despliegue en una organización**<br>· El primer uso sobre la contabilidad y el presupuesto de una organización concreta | La documentación de esa organización |

<!-- /hoja de ruta -->

## Los doce skills de la familia

<!-- cfo:skills-familia · generado por scripts/familias.py; no se edita a mano -->
Doce skills distintos entre los dos agentes. **Los que comparten son copias literales, no un módulo importado**: un plugin instalado tiene que correr solo. `scripts/sincronizar.py` las copia y `scripts/sincronizar.py --check` falla si se separan.

| Skill | Clara | Tomás |
|---|:--:|:--:|
| `audit-support` | ● | · |
| `budget-record` | · | ● |
| `close-checklist` | ● | · |
| `close-record` | ● | · |
| `committee-pack` | · | ● |
| `einvoice-matching` | ● | · |
| `finance-intake` | ● | ● |
| `forecast-method` | · | ● |
| `ledger-tieout` | ● | · |
| `reconciliation` | ● | · |
| `transfer-control` | · | ● |
| `variance-analysis` | · | ● |
<!-- /cfo:skills-familia -->

## Estado

**Los dos están construidos y se pueden instalar hoy**, y los dos tienen la misma deuda, que
conviene no esconder: **el motor está probado sobre material sintético; la extracción del agente
todavía no.**

<!-- cfo:estado · generado por scripts/familias.py; no se edita a mano -->
| Agente | Se instala | Su prueba |
|---|---|---|
| **Clara** · Contralor | `criterio-finance` · 9 comandos, 7 skills | El motor, probado; una primera ronda con el agente; la completa, pendiente · [resultados](../../tests/criterio-finance/RESULTADOS.md) |
| **Tomás** · FP&A | `criterio-budget` · 7 comandos, 6 skills | El motor, probado; una primera ronda con el agente; la completa, pendiente · [resultados](../../tests/criterio-budget/RESULTADOS.md) |
| **Rostrum** · el portal | `criterio-server` · 2 comandos, para todas las familias | — |
<!-- /cfo:estado -->

La familia se declara probada con una ronda completa con el agente, y el primer uso sobre la
contabilidad de una organización concreta es el incremento siguiente. Las decisiones que siguen
abiertas, en el [diseño](DISENO.es.md#decisiones-abiertas).
