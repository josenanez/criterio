[English](DISENO.md)

# criterio-ea · el diseño de la familia

**Estado: en diseño.** Ni el motor ni el plugin existen todavía; esta hoja es la que se construye.
Alcance y reglas en [ADR 0012](../../docs/decisions/0012-scope-asistente-ejecutivo.md).

**Esta es la hoja de diseño de la familia**: los documentos que procesa, las señales que calcula el
código, cada comando con su entrada, su proceso y su reporte, y las decisiones tomadas. La página de
la familia se escribe cuando el plugin exista.

Una agente que extiende la capacidad de la oficina de dirección: procesa la agenda, las sesiones de
los órganos y la correspondencia del ejecutivo, y las contrasta contra sus compromisos para señalar
qué se cruza, qué sesión no tiene material ni acta, qué acuerdo no tiene dueño y qué correo espera
respuesta. El modelo de lenguaje (LLM) extrae; el código calcula; la decisión la toma siempre una
persona.

Primera versión: los países del registro del motor. **Prepara; no recomienda ni decide.** Para cada
punto que pide una decisión arma su ficha —las opciones que traen los documentos, la evidencia de
cada una, lo que falta saber y las fechas que fijan el plazo— y no las ordena. Las cuatro razones
están en el ADR.

**Cómo trabaja.** Automatizada: procesa los documentos, calcula las señales y prepara cada entregable
sin intervención. Semiautomatizada cuando falta un dato que ningún documento trae —quién integra un
órgano, los umbrales—: entonces le pregunta a la persona, dice qué preguntó y sigue con la respuesta.

**Fuentes.** Toda fuente que se usa para procesar —el rol, los formatos, las cifras de terceros— está
en [`FUENTES.es.md`](FUENTES.es.md) con su versión, su enlace, la fecha de consulta y su estado.

**De dónde sale este documento.** Las tablas de la agente, las señales, los comandos y las cifras no
se escriben aquí: salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y
[`fuentes.json`](fuentes.json), que `scripts/familias.py` escribe en este diseño y en
`FUENTES.es.md`.

## Una agente

<!-- ea:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| Asistente ejecutiva | **Ofelia** — del griego *ōphéleia*, «ayuda»: es la que prepara | `criterio-assistant` | El día a día del ejecutivo: la agenda contra sus compromisos, la preparación de cada sesión de un órgano con la ficha de cada decisión, el borrador del acta, el seguimiento de los compromisos y la correspondencia que pide respuesta |
<!-- /ea:agentes -->

Es para quien asiste al ejecutivo: la persona sigue siendo dueña de la agenda y de lo que se envía.
La frontera con el jefe de gabinete es la de O*NET (F-01): las iniciativas, la coordinación del
equipo directivo y las decisiones sobre procesos y recursos son del otro rol.

## Los documentos que procesa

| Documento | Dónde | Quién lo procesa |
|---|---|---|
| La agenda exportada, en .ics (F-02) | `10-agenda/` | El código: eventos, repeticiones y zonas horarias, con su autoprueba |
| Los correos guardados como archivo (F-03) | `20-correspondencia/` | El código procesa los encabezados; el LLM extrae qué se pide y para cuándo |
| La convocatoria y el orden del día | `organos/<órgano>/<fecha>/10-convocatoria/` | El LLM, con la cita de cada punto |
| El material de la sesión | `20-material/` | El código cuenta lo que está; no se resume |
| Las notas o la transcripción | `30-notas/` | El LLM extrae acuerdos y compromisos, cada uno con su cita |
| El acta firmada | `40-acta/` | El LLM extrae acuerdos y compromisos; el código calcula sus fechas |

Ofelia procesa exportaciones, no cuentas: no se conecta al buzón ni al calendario. Una conexión
directa es otra decisión, con su revisión de privacidad.

## Las señales: lo que calcula el código

<!-- ea:senales · generado por scripts/familias.py; no se edita a mano -->
**Ofelia · Asistente ejecutiva**

| Señal | Se levanta cuando |
|---|---|
| `meeting_conflict` | Dos reuniones del ejecutivo se cruzan en la agenda exportada |
| `meeting_without_material` | A los días configurados de una sesión de un órgano, su material no está en la carpeta |
| `meeting_without_minutes` | Pasados los días configurados de una sesión, su acta firmada no está |
| `agreement_without_owner` | Un acuerdo del acta no tiene responsable |
| `agreement_without_date` | Un acuerdo del acta no tiene fecha |
| `commitment_overdue` | Un compromiso venció y ningún documento lo sostiene como cumplido |
| `commitment_rescheduled` | Un compromiso se movió más veces de las configuradas |
| `correspondence_unanswered` | Un correo guardado pide respuesta y su plazo venció sin una respuesta guardada |
| `decision_deadline` | Una decisión pendiente tiene una fecha que la fija dentro de los días configurados |
<!-- /ea:senales -->

Los días, las veces y la antigüedad máxima de la agenda son configuración de cada oficina, con un
valor por defecto declarado. Se calla cuando nada cruza un umbral.

## Las tres clases, como en la familia PMO

**A · Lo que hace, y hoy consume tiempo de alguien:** cruzar la agenda contra las sesiones, armar el
orden del día con lo abierto, perseguir el material, levantar el borrador del acta, llevar la lista
de compromisos, clasificar la correspondencia.

**B · Lo que hace, y hoy no se hace:** revisar cada acuerdo de cada acta contra su responsable y su
fecha; contar cuántas veces se movió cada compromiso; preparar la ficha de cada decisión con la
evidencia de cada opción citada.

**C · Lo que no hace:** no envía, no agenda, no acepta ni mueve nada; no recomienda una opción ni
prioriza por el ejecutivo; no declara cumplido un compromiso sin evidencia; no edita actas, agendas ni
correos originales; no evalúa a una persona ni a un área.

## Los comandos de Ofelia, en orden de importancia

<!-- ea:comandos-ofelia · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `ea-setup` | La carpeta raíz. Preguntas: el ejecutivo y quién lo asiste, los órganos de `00-referencia`, las carpetas excluidas, los umbrales —días antes de una sesión para el material, días para el acta, cambios de fecha que cuentan, antigüedad máxima de la agenda—, si publica en Rostrum y los términos | Inventario de lo que hay; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las carpetas excluidas; los órganos con sus sesiones encontradas |
| 1 | `ea-scan` | La agenda de `10-agenda`, cada sesión de `organos/` y la correspondencia de `20-correspondencia` (F-02, F-03) | El código normaliza la agenda —repeticiones y zonas horarias— y los correos; el modelo de lenguaje (LLM) extrae de actas, notas y correos los acuerdos, los compromisos y lo que se pide, cada uno con su cita | Las fichas nuevas y las que cambiaron; lo que no se pudo procesar y por qué |
| 2 | `ea-agenda` | La ficha de la agenda y las de las reuniones | Cruza la semana del ejecutivo contra sus sesiones y sus compromisos; si la exportación es más vieja que el umbral, avisa y no calcula cruces | Los cruces, las sesiones sin material y las sesiones sin acta, con la fecha de la exportación |
| 3 | `ea-prep` | El órgano y la fecha de la próxima sesión; la ficha de la anterior | Arma el orden del día con lo que quedó abierto, lista el material que falta en `20-material` y prepara la ficha de cada decisión: las opciones que traen los documentos, la evidencia de cada una con su cita, lo que falta saber y las fechas que fijan el plazo | El paquete de la sesión. No ordena las opciones ni dice cuál conviene |
| 4 | `ea-minutes` | Las notas o la transcripción de `30-notas` | El modelo de lenguaje (LLM) extrae cada acuerdo y cada compromiso con su cita; el código marca los que no tienen responsable o fecha | El borrador en `90-borradores`, con «BORRADOR» en el nombre y en el texto, y la lista de lo que falta para cerrarlo |
| 5 | `ea-commitments` | Las fichas de las reuniones; las de los proyectos, si Samuel las tiene | Calcula con las reglas de compromiso del núcleo común cuáles vencieron sin evidencia, cuáles no tienen fecha y cuáles se movieron más del umbral; los de proyecto los cita de la ficha de Samuel y no los recalcula | El estado de los compromisos de dirección, por órgano y por responsable |
| 6 | `ea-mail` | Las fichas de la correspondencia | Calcula qué pide respuesta y su plazo; para lo rutinario, el modelo de lenguaje (LLM) escribe un borrador de respuesta | Lo que pide respuesta y para cuándo; los borradores en `90-borradores`. Nunca envía |
| 7 | `ea-weekly` | La configuración y las fichas | Reúne lo que llegó, lo que vence y lo que falta preparar | Un solo resumen a la semana; no se publica en Rostrum salvo que la configuración lo diga |
| 8 | `ea-wake` | La configuración y las fichas | Decide qué toca: las sesiones que entran en la ventana, las actas pendientes, los plazos de la correspondencia y una revisión semanal | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /ea:comandos-ofelia -->

## Las reglas para la operación real

Son las del ADR 0012, y cada una tiene que poder comprobarse en la prueba:

- Escribe solo en `estado-direccion/`, en `.criterio/direccion/` y en `90-borradores/`, más el
  archivo que marca su carpeta raíz (ADR 0011).
- Cada borrador lleva «BORRADOR» en el nombre y en el texto; nunca lo archiva en `40-acta/`.
- Su informe no se publica en Rostrum por omisión.
- Procesa solo las carpetas indicadas y respeta la lista de excluidas, que dice en cada informe.
- Cada compromiso es del acta donde nació; los de proyecto son de Samuel y se citan de su ficha.
- Si la agenda es más vieja que el umbral, avisa y no calcula cruces.
- Un evento ambiguo se declara, no se adivina.

## Lo que se reusa

- Las reglas de compromiso de Samuel —vencido sin evidencia, sin fecha, reprogramado—, que pasan de
  `portafolio.py` al núcleo común (`nucleo.py`). Las pruebas de Samuel tienen que dar exactamente lo
  mismo antes y después.
- `nucleo.py` —tablas, fechas, inventario, señales, reporte y el registro de países—, y `texto.py`,
  `terminos.py`, `rastro.py` y `raiz.py`, copiados por `scripts/sincronizar.py`.
- El skill `commitment-tracking`.
- Rostrum, para quien decida publicar.

Lo nuevo es la lectura del .ics y del correo guardado, con librería estándar y su autoprueba.

## Cómo se prueba

Material sintético por industria y una oficina de control por país, con una clave que el motor no
ve, en `tests/criterio-ea/`. Cada señal se siembra al menos una vez, además de los casos de las
reglas: una agenda vieja, un evento recurrente que cruza un cambio de hora, un borrador puesto en
`40-acta/`. Va con el mismo arnés, `tests/ronda_familia.py`: primero el motor contra la clave y
después la ronda con la agente. La familia se declara probada con una ronda completa.

## Cifras de terceros

<!-- ea:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Microsoft), C-02 (Microsoft), C-03 (Microsoft). Por verificar, y fuera de cualquier publicación hasta verificarse: C-04.
<!-- /ea:cifras -->

## Decisiones cerradas

- El rol, desde O*NET 43-6011, y el nombre, Ofelia. José, 2026-10-23.
- La sigla de la familia, EA. José, 2026-10-23.
- Prepara; no recomienda ni decide. José, 2026-10-23.
- La secretaría de junta es un modo de Ofelia, no un agente aparte. José, 2026-10-23.

## Decisiones abiertas

1. El nombre del plugin. La propuesta es `criterio-assistant`, con comandos `ea-*`.
2. La estructura numerada de carpetas (`10-agenda/`, `20-correspondencia/`, `90-borradores/`,
   `organos/<órgano>/<fecha>/`), que ajusta la del ADR a la convención de la ADR 0007.
