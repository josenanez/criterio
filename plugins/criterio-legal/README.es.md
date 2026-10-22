<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-clo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-clo-claro.svg" alt="Criterio CLO · Contratos y cumplimiento" height="48"></picture>

# Fidel · los contratos

<img src="../../docs/img/es/robot-fidel.gif" alt="Fidel" width="220" align="right">

**Fidel pone lo que la empresa firmó al lado de lo que está pasando.** Tú llevas los contratos y
respondes por ellos. Él llega con lo que vence, los preavisos que se acercan, quién firmó con qué
facultad y lo pagado contra lo pactado.

[English](README.md) · `criterio-legal` · Apache 2.0 · Una instancia por entidad

**Estado: los siete comandos construidos**, los cinco skills y el motor de cálculo, probado
contra material sintético de cuatro industrias con una clave que el agente no ve y una entidad
de control por país. **La extracción del agente pasó una [primera ronda pequeña](../../tests/evidencias/familias/clo/RONDAS.md)** —banca y el control de Colombia—; la ronda completa es el paso siguiente, y nada se ha corrido aún sobre los documentos de una organización. Nada se anuncia como terminado hasta que pasen los
[criterios de aceptación](ACCEPTANCE.md).

**Esta página se lee sola.** Fidel funciona sin Constanza: si solo llevas los contratos, aquí
está todo, incluidas sus pruebas. La familia —cómo se encuentra con Constanza y con Rostrum—
está en la [familia criterio-clo](../../families/criterio-clo/README.es.md).

---

## Qué es

| | |
|---|---|
| **A quién extiende** | Al abogado o al equipo que lleva los contratos de la entidad |
| **Sobre qué trabaja** | **Todos los contratos de una entidad**, uno por uno y en conjunto |
| **Qué mira** | La carpeta legal de la entidad, como esté: el registro de contratos, los pagos, la matriz de atribuciones y la carpeta de cada contrato con sus otrosíes, sus garantías, la contraparte y su ejecución |
| **Cadencia** | Cuando un vencimiento o un preaviso entra en la ventana configurada, cuando llega un documento nuevo, y una vez por semana |
| **Instancias** | Una por entidad |

## Qué hace

**Lo que hace y hoy no se hace: revisar todos los contratos, no una muestra, contra la matriz de
atribuciones, y todos los pagos contra el valor y la terminación de su contrato.** Una firma sin
facultad o un pago después de la terminación no avisan: están en cualquier contrato.

**Lo que puede responder que hoy cuesta días:** qué contrato vence sin una decisión registrada,
qué preaviso de no renovación se acerca —o ya pasó—, qué contrato reporta el registro como
vigente cuando ya terminó, quién firmó por encima de su facultad, qué garantía exigida no tiene
póliza y qué se pagó por encima del valor con sus otrosíes.

<!-- clo:comandos · generado por scripts/familias.py; no se edita a mano -->
### Los siete comandos

> Se escriben con el prefijo del plugin: `/criterio-legal:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-legal:legal-setup` | La configuración, el inventario y las primeras fichas de los contratos |
| `/criterio-legal:contract-scan` | Las fichas de los contratos al día, con lo que cambió y las señales nuevas |
| `/criterio-legal:contract-register` | El registro de contratos contra lo que dicen los documentos |
| `/criterio-legal:obligations-calendar` | Vencimientos, preavisos y obligaciones, con lo que venció sin evidencia |
| `/criterio-legal:authority-check` | Quién firmó cada contrato y con qué facultad |
| `/criterio-legal:contract-execution` | Lo pagado contra lo pactado, y las garantías contra lo exigido |
| `/criterio-legal:legal-wake` | Lo que toca hoy en los contratos; si no toca nada, se calla |
<!-- /clo:comandos -->

`legal-setup` va primero porque los demás lo necesitan, y `legal-wake` es el que se le pone a un
reloj. Entre los dos, los cinco que preparan el trabajo: qué cambió, el registro, el calendario,
las firmas y la ejecución.

<!-- clo:skills · generado por scripts/familias.py; no se edita a mano -->
### Los cinco skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se consultan como un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `contract-calendar` | El calendario de los contratos: la terminación con sus otrosíes, la fecha límite del preaviso de no renovación, la prórroga automática y cada obligación con fecha contra su evidencia | Propio |
| `contract-record` | La ficha de un contrato: partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías, certificado de la contraparte y obligaciones, cada dato con su cita | Propio |
| `legal-intake` | Qué documentos procesa la familia, dónde va cada uno, qué tablas procesa el motor directamente y qué extrae el agente a la ficha | Propio · también en Constanza |
| `payments-guarantees` | Lo pagado por cada contrato contra su valor y sus otrosíes, los pagos después de la terminación, y las garantías exigidas contra las pólizas aportadas y su vigencia | Propio |
| `signing-authority` | Quién firmó contra la matriz de atribuciones —tipo, monto y vigencia de la facultad, otrosíes incluidos—, el documento sin la firma de las dos partes y el certificado de la contraparte vencido al firmar | Propio |
<!-- /clo:skills -->

## Para qué sirve

`/criterio-legal:obligations-calendar` calcula la terminación de cada contrato con sus otrosíes
y la fecha límite de su preaviso de no renovación. Y hace algo más, que es lo que separa un
calendario útil de una lista de fechas: **un contrato con renovación automática que nadie decide
se renueva solo**, y el informe lo dice antes de que pase la fecha.

> **Banco Andino** · contratos al 6 de octubre de 2026
> Un contrato con renovación automática tiene su preaviso dentro de la ventana configurada, y
> ningún documento registra la decisión de renovarlo o terminarlo.
> **Si nadie decide, el contrato decide solo.**

Ese caso sale del material sintético, sembrado con su clave **antes** de correr el motor, y es
la razón por la que Fidel existe: no decidir por ti, sino que la decisión llegue a tiempo.

### Lo que cuesta hoy

<!-- clo:cifras · generado por scripts/familias.py; no se edita a mano -->
| Cifra | Fuente |
|---|---|
| **8,6 %** del valor de los contratos se erosiona en promedio por una gestión contractual deficiente; los mejores, poco más de 3 %, los peores, más de 20 % | [World Commerce & Contracting con Deloitte, 2022](https://www.deloitte.com/us/en/services/tax/articles/contract-management-lifecycle-insights.html) — Más de 1.200 organizaciones |
| **90 %** de las organizaciones tiene dificultad para encontrar sus propios contratos | [EY Law y Harvard Law School Center on the Legal Profession, 2021](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) — 1.000 líderes de contratación, dentro de una investigación de más de 2.000 personas en 22 países, enero de 2021 |
| **19.000** contratos al año gestiona en promedio el equipo de contratación de una organización grande | [EY Law y Harvard Law School Center on the Legal Profession, 2021](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) — 1.000 líderes de contratación, enero de 2021 |
<!-- /clo:cifras -->

Una empresa que no encuentra sus propios contratos no puede saber qué firmó, qué vence ni a qué
se obligó.

### Y para qué no sirve

- **No opina sobre la validez de un contrato, de una cláusula, de una firma ni de una
  garantía.** Lo que es criterio jurídico queda como pregunta para la persona.
- **No recomienda renovar, terminar ni renegociar.** La decisión es de una persona, y Fidel la
  registra cuando un documento la toma.
- **No redacta, firma ni envía contratos, otrosíes ni preavisos.**
- **No dice de memoria una norma, un plazo legal ni una facultad que la matriz no tiene.**
- **No mueve, renombra ni crea nada dentro de los documentos de la organización.** Lo único que
  deja, si la persona lo autoriza, es el archivo que marca la carpeta raíz para que se reconozca
  a primera vista.
- **No adivina.** Cada dato lleva la cita del documento y, en las tablas, la fila de donde salió.
  *«No encontrado»* es una respuesta válida.

**Y hay una cosa que deliberadamente no trae: el cumplimiento de la organización.** La matriz de
obligaciones, las políticas, las normas y el canal de denuncias son de Constanza, que toma de las
fichas de Fidel las obligaciones de cumplimiento de los contratos. Los contratos públicos, con sus
propias reglas, quedan para otra versión.

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura de la
plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus políticas antes de
apuntarlo a material confidencial. Descargo completo en [DISCLAIMER.es.md](../../DISCLAIMER.es.md),
términos en [TERMS.es.md](../../TERMS.es.md).

## Instalación y configuración

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-legal@criterio
/criterio-legal:legal-setup
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez/criterio`.

Si respondes por el cumplimiento y no por los contratos, lo tuyo es
[Constanza](../criterio-compliance/README.es.md).

### El primer resultado

`/criterio-legal:legal-setup` no te pide que ordenes nada antes de empezar. Mira la carpeta legal
de la entidad, la compara con la
[estructura recomendada](../../families/criterio-clo/README.es.md#la-estructura-de-carpetas-recomendada)
y hace las preguntas que ningún documento responde —la entidad, la matriz de atribuciones, con
cuántos días se avisa un vencimiento, quién decide renovar—. En los primeros quince minutos deja
ver el calendario de los contratos: lo que vence, los preavisos que se acercan o que ya pasaron
sin decisión y las obligaciones vencidas sin evidencia, con las señales que el motor levantó en
el registro, las firmas y los pagos.

Desde ahí, cada comando entrega su reporte en el mismo orden: lo que hay que atender, el
resultado, lo que no se pudo procesar, las preguntas que hizo y las fuentes.

**Lo que queda configurado** lo escribe `/criterio-legal:legal-setup` a partir de lo que
respondiste, en `.criterio/legal/<entidad>/config.json`: la entidad, la matriz, los días de
aviso, la antigüedad máxima del certificado de la contraparte, quién decide renovar y el registro
de que aceptaste los términos con tu nombre y la fecha. Todo eso se cambia **hablando**.

### Cada cuánto corre

Un comando espera. **Este se programa y corre solo.** Su cadencia es la de las fechas de los
contratos: corre cuando un vencimiento o un preaviso entra en la ventana configurada, cuando llega
un documento nuevo y una vez por semana. La decisión es aritmética de fechas, así que la toma el
código:

```
python3 scripts/legal.py despertar --config <archivo>
```

Y `/criterio-legal:legal-wake` es el comando que el reloj invoca: hace lo que toca, responde
primero las preguntas que alguien dejó en Rostrum, y **si no toca nada no produce nada.** Ponerlo
en un reloj es del lado de tu organización: una tarea programada en Cowork, o el programador del
sistema en Claude Code. Si no quieren corridas desatendidas, la cadencia sigue diciendo qué toca,
corrida a mano.

**Y si quieres que el director legal vea lo que vence sin pedírtelo**, la familia tiene un portal
que lo publica, y quien mira puede dejarle una pregunta escrita a Fidel. →
**[Rostrum](../criterio-server/README.es.md)**

## Trabajo en equipo

Fidel funciona solo. Si están los otros, **no hay nada que conectar**: se encuentran por el
estado de la entidad y por las fichas de los contratos, que son documentos.

| Con quién | Qué pasa |
|---|---|
| **Constanza** | Comparten el estado de la entidad. Fidel escribe la ficha de cada contrato y Constanza toma de ella las obligaciones de cumplimiento que trae, para ponerlas al lado de la matriz. Cada uno escribe solo sus fichas |
| **Rostrum** | Publica sus reportes, lo que vence en los contratos y sus señales, para quien no abre una carpeta, y le devuelve las preguntas que deja quien lo mira. **No escribe en el estado** |

## Pruebas

### Cómo está construido

La espina es la **ficha del contrato**, una por contrato: partes, valor, fechas, renovación,
preaviso, firmantes, otrosíes, garantías, el certificado de la contraparte y las obligaciones,
cada dato con la cita del documento y su fecha. La escribe el agente; el motor la valida y
calcula sobre ella.

[`scripts/legal.py`](scripts/legal.py), con la librería estándar, hace todo lo que es cálculo:
vencimientos, límites de preaviso, prórrogas, facultades contra la matriz, lo pagado contra lo
pactado y las garantías contra lo exigido, el mismo resultado cada vez. Procesa las tablas
directamente —el registro, los pagos, la matriz— y el agente lleva a la ficha solo lo que trae
cada contrato escrito. [`scripts/texto.py`](scripts/texto.py) convierte a texto el Word, el
Excel, el PowerPoint, el PDF y el correo, y es copia literal del de la familia PMO; `legal.py`
viaja copiado en `criterio-compliance`. `scripts/sincronizar.py --check` falla si alguna copia se
separa.

Cada marco y cada cifra que se usa está en
[`families/criterio-clo/FUENTES.es.md`](../../families/criterio-clo/FUENTES.es.md), con su
versión, su enlace y su estado.

### Cómo se verifica

```
python3 scripts/legal.py selftest                     el motor
python3 tests/criterio-clo/generar.py                  el material de las cuatro industrias
python3 tests/criterio-clo/evaluar.py --agente fidel   cada señal contra la clave
```

Con la librería estándar, sin instalar nada. Sobre material sintético con una clave que el motor
no ve — **incluidos los controles**: una entidad por país sin ningún defecto, con los casos que
se parecen a uno, como un contrato que vence con el acta que decide renovarlo. Cualquier señal
ahí es una falla.

**Cómo salió la última corrida, generado desde la corrida misma:**
[`tests/criterio-legal/RESULTADOS.md`](../../tests/criterio-legal/RESULTADOS.md). Qué se siembra
en cada entidad y, con el mismo detalle, **qué no prueba el material**, en
[`EVIDENCIA.md`](../../tests/criterio-clo/EVIDENCIA.md).

El diseño, con la entrada, el proceso y el reporte de cada comando y las señales del motor, en
el [diseño de la familia](../../families/criterio-clo/DISENO.es.md); los criterios de aceptación,
en [ACCEPTANCE.md](ACCEPTANCE.md).

Y las pruebas del conjunto de la familia —lo que ningún agente puede responder solo— en la
[página de la familia](../../families/criterio-clo/README.es.md#las-pruebas-de-la-familia).
