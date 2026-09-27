# criterio-pmo

**Vera, un segundo cerebro para la oficina de proyectos.** Lee la documentación que tu PMO ya
tiene y dice qué cambió, qué se contradice y qué lleva semanas en silencio.

[English](README.md) · Apache 2.0 · Se instala en cuatro clics · **El primer resultado sale
en quince minutos, sobre tus propios documentos**

---

## La familia PMO

![La familia PMO: tres agentes, un solo contrato de datos](../../docs/img/es/familia-pmo.png)

La capacidad tiene más de un agente porque la organización tiene más de un rol. Llevan nombre
de persona porque **son capacidades extendidas de personas**, y el significado de cada
nombre apunta a lo que hace: **Vera** —de *verus*, lo verdadero— dice lo que los documentos
dicen y no lo que se reporta; **Samuel** —«el que escuchó»— recuerda el viernes lo que se
dijo en la reunión; **Alba** trabaja antes de que amanezca el proyecto.

**Los tres se instalan hoy**, cada uno con su propio plugin, y comparten el mismo contrato
de datos. Los tres tienen también la misma deuda, y está escrita en su página: construidos y
verificados sobre corpus sintético, **no probados todavía sobre la documentación real de una
organización.**

**Samuel**, el agente del gerente de proyecto, no va a las reuniones — el gerente va. Lo que hace es que el gerente llegue
con la semana preparada: la agenda armada antes, la minuta redactada después, el plan al día
contra la evidencia y el informe listo salvo una línea. Su función central no la hace ninguna
herramienta que un gerente use hoy: **el compromiso dicho y no cumplido.** Las reuniones están
llenas de *«yo lo tengo para el viernes»* y nadie los registra.

**Alba** trabaja antes de que exista el proyecto, y entrega el acta con la
que el proyecto nace.

---

## Instalar

![Instalación: cuatro clics, o dos comandos](../../docs/img/es/instalacion.png)

**Claude Code**

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pmo@criterio
/pmo-setup
```

## Los primeros quince minutos

![Los primeros quince minutos](../../docs/img/es/quince-minutos.png)

No hay archivo de configuración que editar, ni plantilla que llenar, ni carpeta que ordenar
antes de empezar. La configuración **es una conversación**, y termina con un resultado sobre
tus documentos.

| | |
|---|---|
| **0 – 2 min** | **Instalar.** Dos comandos en Claude Code, o cuatro clics en Cowork |
| **2 – 4 min** | **Mira antes de preguntar.** Le señalas la carpeta donde vive la documentación de proyectos, como esté. Lista lo que encontró: cuántos proyectos distingue, cuántos documentos, qué formatos, cuál es el más reciente, y cuáles no va a poder leer. Ahí sabes que está mirando tus cosas de verdad |
| **4 – 8 min** | **Cinco preguntas.** Quién eres, cuándo se reúne tu comité, quién recibe el informe y en qué forma, y los términos. Una a la vez, cada una con una respuesta sugerida a partir de lo que ya vio. *«No sé»* es una respuesta válida |
| **8 – 15 min** | **Un primer resultado.** Barre **tres proyectos**, no el portafolio completo, para que veas algo real en minutos: qué supo de cada uno, qué no está dicho en ninguna parte, y cualquier contradicción o compromiso vencido que haya aparecido de paso |

Al final te dice cuánto tomaría el portafolio completo, y qué le falta a tu carpeta para que
el análisis sea mejor. Pero como hallazgo, no como requisito: **esto funciona con lo que
haya.**

---

## El agente no espera a que lo llamen

![La cadencia: se activa solo, y casi siempre se calla](../../docs/img/es/cadencia.png)

Esta es la diferencia entre un comando y un agente. Un comando espera. **Este se programa y
corre solo.**

De las cinco preguntas del arranque sale una cadencia, y de la cadencia sale qué toca cada
día. La decisión es aritmética de fechas, así que la toma el código y no el criterio del
momento:

```
python3 scripts/pmo.py due --state <estado> --config <archivo>
```

Y `/pmo-wake` es el comando que el reloj invoca: mira qué toca, lo hace, y **si no toca nada
no produce nada.** Callarse cuando no pasó nada no es una omisión — es la única razón por la
que un agente que corre todos los días sigue instalado el mes siguiente.

Tres cosas pueden tocar. El **barrido**, que mira qué cambió en la carpeta y solo recalcula
los proyectos tocados. El **informe de comité**, que aterriza con la anticipación que
configuraste para que alcances a reaccionar a lo que encuentre. Y la **confirmación**, cinco
campos por corrida — los que envejecen peor: patrocinador, gerente, presupuesto aprobado,
fecha de cierre y alcance.

Ponerlo en un reloj es del lado de tu organización: una tarea programada en Cowork, o el
programador del sistema en Claude Code. **Y si no quieren corridas desatendidas** —en un
banco es una respuesta razonable— la cadencia sigue diciendo qué toca, corrida a mano. Lo
que se pierde es que avise sin que nadie pregunte.

## ¿Quieres que tu patrocinador vea esto sin pedírtelo?

![Rostrum: el informe, para quien no abre una carpeta](../../docs/img/es/servidor.png)

Hasta aquí el informe son archivos en tu equipo. **Un patrocinador no abre una carpeta
de archivos**: abre un enlace, o no abre nada. Para eso está **Rostrum**, el servidor de
esta familia. Una tribuna no mide ni corrige: sostiene lo que ya está escrito, a la
altura de quien lo va a leer.

```
/pmo-server
```

Levanta **un portal con tres secciones** —informes de la PMO, proyectos, productos—, y
el enlace entre proyecto y producto va **en los dos sentidos**. Ahí está lo que ninguna
otra página puede decir: cuando un producto lo construyen proyectos que reportan a
comités distintos, cada comité ve su proyecto y **ninguno ve el producto**.

Y tiene una cosa más, que es la que cambia cómo se usa: **quien mira puede dejarle una
pregunta escrita al agente.** No le contesta en el momento —el agente no está
corriendo— pero la pregunta queda en la cola, y la siguiente vez que Vera despierta
la atiende. *«Esto no coincide con lo que yo sé»* es la petición de más valor del
sistema: es una persona diciéndote qué documento falta.

**No autentica a nadie, y es a propósito**: se publica detrás del control de acceso que
tu organización ya tiene. Escucha solo en tu equipo salvo que le digas lo contrario.

→ **[Rostrum, con capturas de cada sección y qué pedirle a tu organización](SERVER.es.md)**

## Qué queda configurado

Lo escribe `/pmo-setup` a partir de lo que respondiste, en tu equipo y en un archivo tuyo:
dónde están los documentos, dónde vive el estado, tu cadencia de comité, la forma del
informe, los umbrales que le hacen levantar la voz, y el registro de que aceptaste los
términos, con tu nombre y la fecha.

Todo eso se cambia **hablando**. Si quieres que el silencio se reporte a los diez días y no a
los quince, se lo dices.

## Lo que nunca hace

Esto es lo que conviene tener claro antes de instalarlo, y no está en letra pequeña:

- **No escribe en tus carpetas.** Lee tus documentos; los informes y las fichas van a una
  carpeta de estado que tú eliges.
- **No decide.** Produce borradores de trabajo. Formula la decisión como pregunta con sus
  opciones; quién decide y asumiendo qué es de quien tiene la facultad.
- **No declara el estado de un proyecto.** Eso lo hace el gerente. El agente le muestra
  contra qué, y la diferencia entre las dos cosas es el hallazgo de más valor del sistema.
- **No sabe lo que no está escrito.** No conoce lo que se habló en el pasillo ni lo que se
  decidió en una llamada que nadie minutó. Todo hallazgo suyo es *«según los documentos»*, y
  lo declara.
- **No adivina.** Cada dato viene con la cita del documento de donde salió. *«No está dicho
  en ninguna parte»* es una respuesta válida y esperada.

Y una que sí hay que decir en voz alta: **tus documentos se procesan en la infraestructura de
la plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus políticas
antes de apuntarlo a material confidencial. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

---

De aquí para abajo es para quien quiera auditarlo antes de instalarlo. **Todo esto se puede
leer sin ejecutar nada**, y eso es deliberado.

## Cómo funciona

![Cómo funciona: el modelo extrae, el código calcula](../../docs/img/es/como-funciona.png)

La espina es la **ficha de proyecto**: un contrato de datos que todos los comandos leen y
escriben, con la cita al documento fuente y a su fecha en cada campo. Ningún comando lee
documentos crudos por su cuenta. Eso permite consolidar cuarenta proyectos sin volver a
leerlos, **calcular en vez de opinar**, y comparar una corrida contra la anterior.

Tres scripts, que son lo único que no opina. [`scripts/texto.py`](scripts/texto.py) convierte
el documento a texto: `.docx`, `.xlsx` y `.pptx` con la librería estándar —son ZIP con XML
adentro—, `.eml` con el parser de correo, y el PDF con `pdftotext`. Lo que no se puede leer
se declara con la razón. [`scripts/pmo.py`](scripts/pmo.py) hace la aritmética, y su
subcomando `index` decide el costo de cada corrida: dos hashes por documento, uno para saber
si vale extraer y otro para saber si vale releer. Y
[`scripts/informe.py`](scripts/informe.py) arma el informe impreso a partir de lo que los
otros dos produjeron, sin volver a leer un solo documento.

## Los diecisiete comandos

| Comando | Qué hace |
|---|---|
| `/pmo-setup` | **Lo primero que se corre.** Mira tus carpetas, hace cinco preguntas y produce el primer informe sobre tus propios documentos |
| `/pmo-wake` | **Lo que el reloj invoca.** Mira qué toca hoy, lo hace, y si no toca nada se calla |
| `/pmo-server` | Levanta **Rostrum**, el servidor: expone el informe para quien no abre una carpeta, y dice qué pedirle a la organización |
| `/document-index` | Qué documentos cambiaron de verdad, qué hay que releer y qué citas dejaron de resolver |
| `/portfolio-scan` | Lee la carpeta y produce o actualiza una ficha por proyecto. Puerta de entrada |
| `/portfolio-report` | Informe consolidado: qué cambió, qué se contradice, qué está en silencio, qué no tiene sustento |
| `/status-report` | Estado de un proyecto, y las señales que su semáforo declarado no explica |
| `/health-check` | Diagnostica un proyecto desde cero contra la evidencia, sin asumir nada de su informe |
| `/project-history` | Qué pasó en un proyecto, con la línea de tiempo y desde cuándo lo declarado no se sostiene |
| `/steering-pack` | Material de comité como paquete de decisiones, no como informe de avance |
| `/raid-log` | Riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron y nadie registró |
| `/change-control` | Evalúa un cambio en alcance, tiempo y costo, y crea línea base nueva sin borrar la anterior |
| `/budget-tracking` | Aprobado, comprometido, ejecutado y proyección, con desviación contra las dos líneas base |
| `/vendor-tracking` | Entregables contractuales contra evidencia de recibo y contra facturación |
| `/product-view` | El estado de un producto a través de todos los proyectos que lo construyen |
| `/project-charter` | Revisa o redacta el acta, señalando qué falta y qué consecuencia tiene |
| `/project-closure` | Cierra contra el criterio de éxito pactado, con lecciones que se puedan sustentar |

## Los diez skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se
pueden leer como se lee un manual.

| Skill | Qué encapsula |
|---|---|
| `project-record` | La ficha: esquema, reglas de extracción, citación, estados de campo, qué hacer cuando dos documentos se contradicen |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué, el renombrado, el borrado, y la cita que dejó de resolver |
| `portfolio-health` | Las dieciocho señales con lo que significa cada una, los umbrales que las gobiernan, y las tres defensas contra el dato que dejó de ser cierto |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y contra la vigente, la replanificación contra lo que autorizó el comité, las cuatro cifras del presupuesto |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, valoración, criterio de escalamiento |
| `commitment-tracking` | Compromisos dichos en reuniones: extracción, estados, qué cuenta como evidencia, y el que se repite con fecha nueva cada vez |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno y quién decide qué |
| `vendor-control` | Contrato contra evidencia de recibo contra facturación, con monto por entregable |
| `project-diagnosis` | El diagnóstico desde cero: en qué orden se lee y cuándo la respuesta es que no se puede diagnosticar |
| `portfolio-history` | La historia de un proyecto desde sus documentos, y el punto donde la evidencia se separó de lo reportado |

## Fuera de alcance, y por qué

**Capacidad y asignación de recursos**, y **materialización de beneficios**. No por poco
importantes: porque los datos no están en la carpeta. Capacidad exige horas reales y
beneficios exige medición posterior que casi ninguna organización tiene.

Un skill que promete lo que el insumo no permite quema la credibilidad del plugin entero.

**Sin contenido regulatorio.** La gestión de portafolio es método, no normativa: funciona
igual en Bogotá que en Santiago. Si una obligación regulatoria toca un proyecto, este plugin
la registra como restricción o como riesgo, y no opina sobre ella.

## Cómo se verifica

```
python3 scripts/pmo.py selftest          la aritmética y la cadencia
python3 scripts/texto.py --selftest      la conversión de documentos
python3 scripts/informe.py --selftest    el informe: cifras, concordancia y nombres
python3 scripts/servidor.py --selftest   el servidor: qué sirve y qué nunca toca
```

Los tres corren con la librería estándar, sin instalar nada. Sobre material sintético con
respuestas conocidas hay un grader y el resultado de la última corrida, con lo que prueba y
lo que no: [`tests/criterio-pmo/`](../../tests/criterio-pmo/).

Criterios de aceptación en [ACCEPTANCE.md](ACCEPTANCE.md). El diseño de la capacidad, con lo
que el agente no hace y lo que sigue siendo de las personas, en
[`DISENO.es.md`](DISENO.es.md).

Los tres agentes juntos —qué hace cada uno, cómo operan, cómo se trabaja con ellos— en [`FAMILIA.es.md`](FAMILIA.es.md).

**Cómo salió la última corrida, generado desde la corrida misma:** [`tests/criterio-pmo/RESULTADOS.md`](../../tests/criterio-pmo/RESULTADOS.md).
