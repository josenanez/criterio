# criterio-pm

**Samuel se acuerda de lo que se prometió en tu reunión.** Tú vas al comité, negocias y
desbloqueas. Él llega con la semana lista y con la lista de lo que se dijo y no se hizo.

[English](README.md) · Apache 2.0 · Una instancia por proyecto

**Estado: los siete comandos construidos**, los ocho skills del método y la aritmética
verificada sobre un corpus con respuestas escritas a mano. **Lo que todavía no se ha
probado: la extracción sobre la documentación real de una organización** — el corpus
siembra la ficha, así que la cadena documento → modelo → ficha no se ha ejercitado. Nada se
anuncia como terminado hasta que pasen los [criterios de aceptación](ACCEPTANCE.md).

---

## Instalación

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pm@criterio
/pm-setup
```

Si gestionas el portafolio y no un proyecto, lo tuyo es
[`criterio-pmo`](../criterio-pmo/README.es.md).

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

## El compromiso dicho y no cumplido

Es la razón por la que Samuel existe, y **ninguna herramienta que uses hoy lo hace.**

Las reuniones están llenas de *«yo lo tengo para el viernes»*. No está en el plan,
porque no es una tarea del cronograma. No está en el acta, porque el acta la escribió
alguien de memoria dos días después. Está dicho, y se perdió.

`/pm-commitments` lo extrae de la minuta con doliente, fecha y fuente. Y hace algo más,
que es lo que separa un seguimiento útil de una lista que crece: **el mismo doliente
prometiendo lo mismo con fecha nueva es un compromiso reprogramado, no uno nuevo.**

> **Rubén** · Entregar el plan de pruebas de certificación
> Prometido para el 27 de noviembre, y antes para el 13, y antes para el 30 de octubre.
> **Tres veces no es un problema de seguimiento: es un bloqueo que nadie ha nombrado.**

Tres entradas sueltas son tres vencidos que se persiguen por separado. Una entrada con
tres reprogramaciones es una conversación que hay que tener.

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

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura
de la plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus
políticas antes de apuntarlo a material confidencial. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

---

## Tú y la PMO leen los mismos documentos

Samuel escribe tu ficha. Vera, el agente de la PMO, escribe la suya sobre los mismos
documentos. **No se fusionan nunca**, y eso es deliberado: la forma cómoda de resolverlo
—una ficha y un dueño— obliga a elegir mal en las dos direcciones.

`/pm-publish` pone tu ficha en la carpeta de gobierno del proyecto, y Vera la lee como
lee cualquier documento. **Cuando las dos citan y no coinciden, alguien vio un papel que
el otro no vio** — y la mitad de las veces el que tiene razón eres tú, porque tú
estuviste en la reunión donde cambió el patrocinador y el acta de constitución no se
actualizó nunca.

Lo que tú tienes y la PMO no —los compromisos de cada reunión— **no es una
contradicción**: es diferencia de profundidad, y no se reporta como hallazgo.

## Los siete comandos

| Comando | Qué hace |
|---|---|
| `/pm-setup` | **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y lee tu última minuta |
| `/pm-agenda` | La agenda con los puntos que necesitan a alguien en la sala, y con lo que esta reunión no puede mover |
| `/pm-minutes` | El acta sobre la transcripción o las notas, con cada cosa atribuida a una persona |
| `/pm-commitments` | Quién prometió qué, qué venció sin evidencia, y qué se viene reprogramando reunión tras reunión |
| `/pm-report` | El informe semanal completo **salvo el estado**, que lo declaras tú |
| `/pm-publish` | Publica tu ficha donde la PMO la puede leer |
| `/pm-wake` | **El que se le pone a un reloj.** Mira qué toca según tu reunión, y si no toca nada se calla |

Tres de ellos son un ciclo, y por eso están: **el que arma la agenda antes recibe la minuta
después.** El séptimo es de otra clase: `/pm-wake` es lo que convierte esto en un agente y no
en una caja de comandos — no espera a que lo llames. Sin la agenda la reunión hereda el orden del día de la semana pasada; sin el
acta, lo que se dijo se escribe de memoria dos días más tarde y deja de ser evidencia de
nada.

## Los ocho skills

Se cargan solos cuando el tema aparece. Son copias literales de `criterio-pmo`, porque
un riesgo es un riesgo lo mire quien lo mire y la ficha es el contrato de datos de toda
la familia.

| Skill | Qué encapsula |
|---|---|
| `project-record` | La ficha: esquema, extracción, citación, estados de campo, qué hacer cuando dos documentos se contradicen |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué |
| `commitment-tracking` | **La función central.** Extracción, estados, qué cuenta como evidencia, y el que se repite con fecha nueva cada vez |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, valoración, criterio de escalamiento |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y la vigente, las cuatro cifras del presupuesto |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno y quién decide qué |
| `vendor-control` | Contrato contra evidencia de recibo contra facturación |
| `project-diagnosis` | El diagnóstico desde cero: en qué orden se lee y cuándo no se puede diagnosticar |

No trae `portfolio-health` ni `portfolio-history`: solo tienen sentido mirando el
conjunto, y un gerente de proyecto no mira el conjunto.

## Cómo se verifica

```
python3 tests/criterio-pm/grade.py      19 comprobaciones sobre dos proyectos
python3 scripts/pmo.py selftest         la aritmética
python3 scripts/texto.py --selftest     la conversión de documentos
```

Con la librería estándar, sin instalar nada. Sobre un corpus sintético con respuestas
escritas a mano leyendo las minutas — **incluido un control negativo**: un proyecto con
reuniones y compromisos que no produce ni un hallazgo. Un agente que encuentra algo ahí
es un generador de ruido.

Qué prueba esa corrida y, con el mismo detalle, **qué no**, en
[`tests/criterio-pm/EVIDENCIA.md`](../../tests/criterio-pm/EVIDENCIA.md).

El diseño completo, con las tres clases de función y lo que sigue siendo de la persona,
en [`DISENO.es.md`](DISENO.es.md), que viaja con el plugin.

Los tres agentes juntos, y cómo se encuentran, en [`FAMILIA.es.md`](../criterio-pmo/FAMILIA.es.md).
