# Samuel · el agente de un proyecto

**Samuel se acuerda de lo que se prometió en tu reunión.** Tú vas al comité, negocias y
desbloqueas. Él llega con la semana lista y con la lista de lo que se dijo y no se hizo.

[English](README.md) · `criterio-project` · Apache 2.0 · Una instancia por proyecto

**Estado: los nueve comandos construidos**, los ocho skills del método y la aritmética
verificada sobre un corpus con respuestas escritas a mano. **Lo que todavía no se ha
probado: la extracción sobre la documentación real de una organización** — el corpus
siembra la ficha, así que la cadena documento → modelo → ficha no se ha ejercitado. Nada se
anuncia como terminado hasta que pasen los [criterios de aceptación](DISENO.es.md#criterios-de-aceptación).

**Esta página se lee sola.** Samuel funciona sin sus hermanos: si solo gestionas tu proyecto,
aquí está todo, incluidas sus pruebas. La familia —cómo se encuentra con Vera y con Alba—
está en el [README de `criterio-portfolio`](../criterio-portfolio/README.es.md).

---

## El alcance

| | |
|---|---|
| **A quién extiende** | Al gerente de un proyecto |
| **Sobre qué trabaja** | **Un proyecto.** El suyo, y ninguno más |
| **Qué mira** | Su carpeta, y sobre todo **lo que la reunión deja escrito** |
| **Cadencia** | La de la reunión: la agenda antes, el acta después, el informe una vez por semana |
| **Instancias** | Una por proyecto |

**Lo que hace y nadie más hace: el compromiso dicho y no cumplido.** Las reuniones están
llenas de *«yo lo tengo para el viernes»*. No está en el plan, porque no es una tarea del
cronograma. No está en el acta, porque el acta la escribió alguien de memoria dos días
después. Está dicho, y se perdió. **Ninguna herramienta que un gerente de proyecto use hoy
lo recoge.**

**Lo que puede responder que hoy nadie responde:** quién prometió qué y para cuándo con la
cita de la minuta, qué venció sin evidencia en el expediente, y **qué se viene reprogramando
reunión tras reunión** — que no es un problema de seguimiento, es un bloqueo que nadie ha
nombrado.

## Dónde se superpone con los otros dos, y dónde no

La superposición es mínima **a propósito**: lo de Samuel es específico de su proyecto, lo de
Vera es general y de gobierno. Donde los dos pueden mirar lo mismo, lo que cambia es **la
profundidad, la cadencia y quién responde**.

| Lo que también toca otro | Quién más | Qué hace Samuel, y qué no |
|---|---|---|
| **Los compromisos** | Vera | Samuel los extrae **minuta a minuta**, con doliente, fecha y cita. Vera los ve de lejos, en su barrido. **El detalle es de Samuel**, y no se reporta como contradicción: es diferencia de profundidad |
| **El estado del proyecto** | Vera | **Samuel produce el informe; el estado lo declara el gerente.** Vera lo contrasta contra los documentos. La diferencia entre los dos es el hallazgo, y por eso ninguno de los dos sobra |
| **El plan y la línea base** | Vera | Samuel los mantiene al día contra la evidencia, día a día. Vera los mira cuando barre, con cadencia de comité |
| **El acta de constitución** | Alba | Alba la redacta y con ella nace la ficha. **Samuel la recibe**: su trabajo empieza donde el de Alba termina |

Sobre los mismos documentos, Samuel escribe tu ficha y Vera escribe la suya. **No se fusionan
nunca**, y eso es deliberado: la forma cómoda de resolverlo —una ficha y un dueño— obliga a
elegir mal en las dos direcciones. `/pm-publish` pone la tuya donde la PMO la lee, y **cuando
las dos citan y no coinciden, alguien vio un papel que el otro no vio** — la mitad de las veces
el que tiene razón eres tú, porque tú estuviste en la reunión donde cambió el patrocinador y el
acta de constitución no se actualizó nunca.

**Si solo instalas a Samuel, no pierdes nada de tu proyecto.** Lo que pierdes es la mirada de
conjunto —cómo se ve el tuyo al lado de los otros cuarenta—, que es de la PMO y no tuya.

## Instalación

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-project@criterio
/pm-setup
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez-company/criterio`.

Si gestionas el portafolio y no un proyecto, lo tuyo es
[Vera](../criterio-portfolio/README.es.md). Si defines un producto,
[Alba](../criterio-product/README.es.md).

## El primer resultado

`/pm-setup` no te pide que ordenes nada antes de empezar. Mira la carpeta de tu
proyecto, hace cuatro preguntas —una a la vez, cada una con una respuesta sugerida— y
**lee tu última minuta**. Con eso te muestra, en menos de diez minutos:

- **Quién prometió qué y para cuándo**, con la cita de la minuta donde se dijo.
- **Qué venció sin evidencia** en el expediente.
- **Qué quedó sin fecha** — *«lo vemos la otra semana»*. No puede estar vencido, y **por
  eso mismo es el que desaparece de todos los informes.**

Después te dice qué le falta a tu carpeta para que esto sea mejor. Como hallazgo, no
como requisito: **funciona con lo que haya.**

**Lo que queda configurado** lo escribe `/pm-setup` a partir de lo que respondiste, en tu
equipo y en un archivo tuyo: dónde está la carpeta del proyecto, qué día se reúnen, dónde vive
tu ficha, los umbrales, y el registro de que aceptaste los términos con tu nombre y la fecha.
Todo eso se cambia **hablando**.

## El hallazgo que nadie más produce

`/pm-commitments` extrae el compromiso de la minuta con doliente, fecha y fuente. Y hace algo
más, que es lo que separa un seguimiento útil de una lista que crece: **el mismo doliente
prometiendo lo mismo con fecha nueva es un compromiso reprogramado, no uno nuevo.**

> **Rubén** · Entregar el plan de pruebas de certificación
> Prometido para el 27 de noviembre, y antes para el 13, y antes para el 30 de octubre.
> **Tres veces no es un problema de seguimiento: es un bloqueo que nadie ha nombrado.**

Tres entradas sueltas son tres vencidos que se persiguen por separado. Una entrada con
tres reprogramaciones es una conversación que hay que tener.

Ese caso sale del corpus sintético, con la respuesta escrita a mano **antes** de correr el
cálculo, y es la razón por la que Samuel existe: no leer tu proyecto mejor que tú, sino
recoger lo que la reunión dejó dicho y **nadie escribió en ningún sistema.**

## No espera a que lo llamen

Esta es la diferencia entre un comando y un agente. Un comando espera. **Este se programa y
corre solo.**

Su cadencia es la de tu reunión, y de ahí sale qué toca cada día. La decisión es aritmética de
fechas, así que la toma el código y no el criterio del momento:

```
python3 scripts/portafolio.py due --state <estado> --config <archivo>
```

Y `/pm-wake` es el comando que el reloj invoca: el día antes de la reunión prepara la agenda,
el día después pide la minuta, una vez por semana arma el informe, y **si no toca nada no
produce nada.** Callarse cuando no pasó nada no es una omisión — es la única razón por la que
un agente que corre todos los días sigue instalado el mes siguiente.

Ponerlo en un reloj es del lado de tu organización: una tarea programada en Cowork, o el
programador del sistema en Claude Code. **Y si no quieren corridas desatendidas** —en un banco
es una respuesta razonable— la cadencia sigue diciendo qué toca, corrida a mano. Lo que se
pierde es que avise sin que nadie pregunte.

**Y si quieres que tu patrocinador vea el informe sin pedírtelo**, la familia tiene un servidor
que lo publica con una sección para proyectos, y quien mira puede dejarle una pregunta escrita
al agente. → **[Rostrum](../criterio-portfolio/SERVER.es.md)**

## Lo que nunca hace

- **No declara el estado de tu proyecto.** Eso lo declaras tú. Samuel te muestra contra
  qué, y la diferencia entre las dos cosas es el hallazgo de más valor del sistema. No
  es una recomendación: es una restricción del camino de escritura.
- **No va a tu reunión.** Trabaja sobre lo que la reunión deja escrito, y produce lo que
  la reunión necesita.
- **No escribe en tu carpeta de documentación.** Lo único que puede llegar a poner ahí
  es tu ficha, y solo cuando corras `/pm-publish`.
- **No le escribe a nadie.** Produce la lista; perseguir un compromiso es una
  conversación, no un recordatorio automático.
- **No marca cumplido lo que nadie documentó.** *«Rubén dice que lo entregó»* no cierra
  nada: cierra el acta de recibo.
- **No adivina.** Cada dato lleva la cita del documento de donde salió. *«No está dicho
  en ninguna parte»* es una respuesta válida y esperada.

**Y hay una cosa que deliberadamente no trae: la mirada de portafolio.** No tiene
`portfolio-health` ni `portfolio-history`, porque solo tienen sentido mirando el conjunto y un
gerente de proyecto no mira el conjunto. Tampoco trae contenido regulatorio: la gestión de
proyectos es método, no normativa. Si una obligación regulatoria toca el tuyo, la registra como
restricción o como riesgo y no opina sobre ella.

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura
de la plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus
políticas antes de apuntarlo a material confidencial. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

---

De aquí para abajo es para quien quiera auditarlo antes de instalarlo. **Todo esto se puede
leer sin ejecutar nada**, y eso es deliberado.

## Cómo se trabaja con Samuel

Los tres agentes comparten cinco conductas, y ninguna es estilo: son las que hacen que el
resultado se pueda poner frente a un comité. **Cada dato lleva la cita** del documento y su
fecha · **«no está dicho en ninguna parte» es una respuesta válida** · **se callan cuando no
hay novedad** · **ninguno declara** · **ninguno le escribe a nadie**. Están explicadas en el
[README de la familia](../../README.es.md#lo-que-comparten-los-tres).

Lo que cambia entre uno y otro es **el ritmo de la conversación**, y eso conviene saberlo
antes de instalar.

**Con Samuel se conversa todas las semanas.** Trabaja sobre un proyecto y su ciclo es la
reunión: la conversación es frecuente y corta, y casi siempre gira alrededor de un documento
que acaba de aparecer.

**El ritmo:** `/pm-setup` una vez; después, el día antes de la reunión `/pm-agenda`, el día
después `/pm-minutes` con la transcripción o las notas, y una vez por semana `/pm-report`.
`/pm-wake` en un reloj hace ese calendario solo.

**Lo que te va a pedir a ti:** **la minuta.** Es su insumo principal y sin ella se seca — un
gerente que no guarda lo que la reunión deja escrito necesita saberlo el primer día, y
`/pm-setup` se lo dice. Y **la declaración del estado**, que te pide siempre **después** de
mostrarte la evidencia y nunca antes: si te propusiera un estado, tu declaración dejaría de
ser información independiente.

**Lo que no le pidas:** que persiga un compromiso vencido. Te da el nombre, la fecha y la
cita; la llamada la haces tú, porque perseguir es una conversación.

## Cómo funciona

La espina es la **ficha de proyecto**: un contrato de datos que todos los comandos leen y
escriben, con la cita al documento fuente y a su fecha en cada campo. Ningún comando lee
documentos crudos por su cuenta. Eso permite armar el informe sin volver a leer nada,
**calcular en vez de opinar**, y comparar una semana contra la anterior.

Dos scripts, que son lo único que no opina. [`scripts/texto.py`](scripts/texto.py) convierte el
documento a texto: `.docx`, `.xlsx` y `.pptx` con la librería estándar —son ZIP con XML
adentro—, `.eml` con el parser de correo, y el PDF con `pdftotext`. Lo que no se puede leer se
declara con la razón. Y [`scripts/portafolio.py`](scripts/portafolio.py) hace la aritmética: la cadencia, la
desviación contra las dos líneas base, y el compromiso que se repite con fecha nueva.

**Los dos son copias literales de los de Vera, no importaciones**, y eso es deliberado: un
plugin instalado tiene que correr solo. En el repositorio, `scripts/sincronizar.py --check`
falla si las copias se separaron, porque dos copias que calculan distinto sobre los mismos
documentos dejarían sin saber a cuál creerle.

## Los nueve comandos

| Comando | Qué hace |
|---|---|
| `/pm-setup` | **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y lee tu última minuta |
| `/pm-agenda` | La agenda con los puntos que necesitan a alguien en la sala, y con lo que esta reunión no puede mover |
| `/pm-minutes` | El acta sobre la transcripción o las notas, con cada cosa atribuida a una persona |
| `/pm-commitments` | Quién prometió qué, qué venció sin evidencia, y qué se viene reprogramando reunión tras reunión |
| `/pm-report` | El informe semanal completo **salvo el estado**, que lo declaras tú |
| `/pm-publish` | Publica tu ficha donde la PMO la puede leer |
| `/pm-plan` | El primer borrador del plan y la WBS desde el acta, **sin comprometer ninguna fecha** |
| `/pm-escalate` | Lo que excede tu autoridad, como pregunta cerrada, con a quién alcanza calculado |
| `/pm-wake` | **El que se le pone a un reloj.** Mira qué toca según tu reunión, y si no toca nada se calla |

Tres de ellos son un ciclo, y por eso están: **el que arma la agenda antes recibe la minuta
después.** Sin la agenda la reunión hereda el orden del día de la semana pasada; sin el acta,
lo que se dijo se escribe de memoria dos días más tarde y deja de ser evidencia de nada.

## Los ocho skills

Se cargan solos cuando el tema aparece. Son copias literales de `criterio-portfolio`, porque
un riesgo es un riesgo lo mire quien lo mire y la ficha es el contrato de datos de toda
la familia.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `project-record` | La ficha: esquema, extracción, citación, estados de campo, qué hacer cuando dos documentos se contradicen | Copia de Vera · también en Alba |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué | Copia de Vera · también en Alba |
| `commitment-tracking` | **La función central.** Extracción, estados, qué cuenta como evidencia, y el que se repite con fecha nueva cada vez | Copia de Vera |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, valoración, criterio de escalamiento | Copia de Vera · también en Alba |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y la vigente, las cuatro cifras del presupuesto | Copia de Vera |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno y quién decide qué | Copia de Vera · también en Alba |
| `vendor-control` | Contrato contra evidencia de recibo contra facturación | Copia de Vera |
| `project-diagnosis` | El diagnóstico desde cero: en qué orden se lee y cuándo no se puede diagnosticar | Copia de Vera |

## Cómo se verifica

```
python3 tests/criterio-project/grade.py      19 comprobaciones sobre dos proyectos
python3 scripts/portafolio.py selftest         la aritmética
python3 scripts/texto.py --selftest     la conversión de documentos
```

Con la librería estándar, sin instalar nada. Sobre un corpus sintético con respuestas
escritas a mano leyendo las minutas — **incluido un control negativo**: un proyecto con
reuniones y compromisos que no produce ni un hallazgo. Un agente que encuentra algo ahí
es un generador de ruido.

**Cómo salió la última corrida, generado desde la corrida misma:**
[`tests/criterio-project/RESULTADOS.md`](../../tests/criterio-project/RESULTADOS.md). Qué prueba cada
pieza del material y, con el mismo detalle, **qué no**, en
[`EVIDENCIA.md`](../../tests/criterio-project/EVIDENCIA.md).

El diseño completo, con los criterios de aceptación y lo que sigue siendo de la persona, en
[`DISENO.es.md`](DISENO.es.md), que viaja con el plugin.

Y las pruebas del conjunto de la familia —lo que ningún agente puede responder solo— en el
[README de la familia](../../README.es.md#las-pruebas-de-la-familia).
