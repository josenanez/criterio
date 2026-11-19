[English](DISENO.md) · [← La familia](README.es.md)

# criterio-chro · el diseño de la familia

**Estado: construida, en su versión 0.2.0, de laboratorio.** Los comandos, los skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista y la prueba de sesgo contra el
material de `tests/criterio-chro/`, y los dos agentes pasaron las rondas 1 y 2 sobre la banca de Colombia y su control. Alcance en [ADR 0031](../../docs/decisions/0031-la-familia-chro.md).

**Esta es la hoja de diseño de la familia**: las señales que calcula el código, cada comando con su
entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, la
estructura de carpetas y la hoja de ruta están en su [página](README.es.md).

El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —aprobar un perfil, decidir quién sigue
en un proceso— la toma siempre una persona. **El rol se define sobre estándares de ocupaciones**, no sobre
la ley de cada país: la CUOC del DANE (F-03), adaptada de la CIUO-08 (F-01), y O*NET (F-02). La ley de
datos de cada país entra por lo que un perfil no puede pedir y lo que no se trata de un candidato.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json).

## Un agente por rol

<!-- chro:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| Los perfiles de cargo | **Norma** — del latín *norma*, la escuadra del carpintero: cada perfil sobre un estándar | `criterio-roles` | Cada perfil de cargo contra la ocupación de su estándar —la CUOC del DANE u O*NET—: las destrezas y los conocimientos que no recoge, los requisitos sin tarea, lo que la ley del país y la política no permiten pedir, el nivel de estudios contra el nivel de competencia, los perfiles que se solapan y los que pasaron su revisión |
| La selección | **Cándido** — del latín *candidus*, «blanco»: de ahí *candidato*, el que en Roma vestía la toga blanca para pedir un cargo. Cada afirmación de la hoja de vida contra su soporte | `criterio-talent` | Cada hoja de vida contra sus soportes y cada candidato contra el perfil, requisito por requisito y con la cita; la autorización y la conservación de sus datos; cada vacante contra su plazo, y la búsqueda que corre quien recluta |
<!-- /chro:agentes -->

## Las señales: lo que calcula el código

<!-- chro:senales · generado por scripts/familias.py; no se edita a mano -->
**Norma · Los perfiles de cargo**

| Señal | Se levanta cuando |
|---|---|
| `profile_without_occupation` | Un perfil no tiene un código de ocupación que lo ate a un estándar, o su código no está en el estándar |
| `essential_skill_missing` | Una destreza o un conocimiento de la ocupación en el estándar no está en el perfil, ni el perfil dice por qué no aplica |
| `requirement_without_task` | Un requisito del perfil no se apoya en ninguna de sus tareas |
| `requirement_not_allowed` | Un requisito pide un dato sensible según la ley del país, o algo que la política de selección prohíbe pedir |
| `education_level_inconsistent` | El nivel de estudios que pide el perfil no corresponde al nivel de competencia de su ocupación |
| `profiles_overlap` | Dos perfiles comparten la ocupación y la mayor parte de sus requisitos |
| `profile_review_overdue` | Un perfil pasó su fecha de revisión |

**Cándido · La selección**

| Señal | Se levanta cuando |
|---|---|
| `claim_without_support` | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte |
| `certification_expired` | Una certificación que el perfil exige venció antes de la postulación |
| `employment_dates_differ` | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral |
| `requirement_not_evidenced` | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes |
| `protected_data_received` | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis |
| `consent_missing` | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos |
| `retention_exceeded` | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta |
| `vacancy_past_target` | Una vacante sigue abierta después del plazo de cobertura de la política |
<!-- /chro:senales -->

## Los comandos de Norma, en orden de importancia

<!-- chro:comandos-norma · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `roles-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, el estándar de ocupaciones —la CUOC o O*NET— y dónde está su descarga oficial en `00-referencia/`, con O*NET el umbral de importancia, la equivalencia de los niveles de estudio de la organización con la CINE, cada cuántos meses se revisa un perfil y lo que la política prohíbe pedir | Inventario de lo que hay; lee la descarga del estándar y dice cuántas ocupaciones trae; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; el estándar con sus ocupaciones; la primera ficha del periodo |
| 1 | `roles-scan` | Los perfiles de `10-perfiles/` y la ficha del periodo | Lleva a la ficha cada perfil nuevo o cambiado —su ocupación, sus tareas, sus requisitos con la tarea que los apoya, sus estudios y su revisión—, con la cita; recalcula las señales | Lo que entró a la ficha; los perfiles que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `profile-build` | El código de una ocupación de la CUOC u O*NET, o el nombre del cargo para buscarla | El motor trae la ocupación del estándar —su descripción, sus funciones, sus destrezas, sus conocimientos y su nivel de competencia—; el agente propone el perfil con cada requisito atado a una tarea y a un elemento del estándar, y lo deja como borrador para que una persona lo apruebe | El borrador del perfil, con la fuente de cada requisito y lo que la persona tiene que decidir |
| 3 | `profile-check` | La ficha del periodo y la descarga del estándar en `00-referencia/` | Cada perfil contra su ocupación: si tiene código, qué destreza o conocimiento del estándar no recoge sin decir por qué, qué requisito no se apoya en una tarea, si el nivel de estudios corresponde al nivel de competencia (CUOC 2026, numeral 3.2, F-03) y si pasó su revisión | Cada perfil con su ocupación, su nivel, sus estudios, lo que le falta frente al estándar y su revisión; las señales con su cita |
| 4 | `profile-language` | Los requisitos de la ficha del periodo, la ley de datos personales del país y la política de selección | Cada requisito contra los datos sensibles de la ley del país —F-10 a F-17, con su artículo— y contra lo que la política de la organización prohíbe pedir, como la edad, el sexo o el estado civil | Cada requisito que pide algo que no se puede pedir, con la norma o la política que lo dice |
| 5 | `profile-map` | La ficha del periodo y la descarga del estándar | Agrupa los perfiles por ocupación; dice cuáles comparten la ocupación y la mayor parte de sus requisitos, y cuáles ocupaciones afines a las de la organización no tienen perfil | Los perfiles por ocupación, los que se solapan con su porcentaje en común y las ocupaciones afines sin perfil |
| 6 | `roles-wake` | La configuración, el registro de corridas y lo que cambió en la carpeta | Decide si toca procesar perfiles nuevos o un reporte con señales abiertas; si no toca nada, se calla | Lo que tocaba y lo que hizo, o una línea si no tocaba nada |
| 7 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /chro:comandos-norma -->

## Los comandos de Cándido, en orden de importancia

<!-- chro:comandos-candido · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `talent-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, el plazo de cobertura de una vacante y los días de conservación de los datos de la política de selección, el registro de vacantes de `20-vacantes/`, el de autorizaciones de `40-autorizaciones/` y la exportación del ATS de `50-ats/` con sus columnas | Inventario de lo que hay; reconoce las columnas de cada tabla; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las columnas que faltan; la primera ficha del periodo |
| 1 | `talent-scan` | Las carpetas de `30-candidatos/` y la ficha del periodo | Lleva a la ficha cada hoja de vida nueva: cada título, certificación y empleo con su soporte y sus fechas, la evidencia de cada requisito del perfil y lo que llegó y no se debe tratar —solo el tipo de dato y dónde, nunca su valor—; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `talent-search` | Una vacante del registro de `20-vacantes/`, su perfil de Norma, el estándar y la base interna de `50-ats/` | Arma las cadenas para el buscador de quien recluta desde las denominaciones de la ocupación y los requisitos esenciales, y cruza la base interna por la misma ocupación o una afín, en el orden del identificador | Las cadenas de búsqueda y las personas de la base interna con la ocupación, sin ningún orden por número |
| 3 | `cv-check` | La ficha del periodo y los soportes de `30-candidatos/` | Cada título, certificación y empleo de la hoja de vida contra su soporte: el que no lo tiene, las fechas de un empleo que no son las de su certificado y la certificación que el perfil exige y venció antes de la postulación | Cada afirmación sin soporte o que no coincide, con su cita; ninguna se da por falsa |
| 4 | `candidate-fit` | La ficha del periodo y el perfil de la vacante, de Norma | Cada requisito del perfil con la evidencia de cada candidato, de la hoja de vida o de un soporte, con la cita; el requisito esencial sin evidencia es una señal. Sin puntaje y sin orden por número: los candidatos van por su identificador | Una tabla por candidato, requisito por requisito, con su evidencia y dónde está; quien selecciona decide |
| 5 | `privacy-check` | La ficha del periodo, el registro de `40-autorizaciones/`, la exportación de `50-ats/` y los días de conservación de la política | Cada candidato contra su autorización de tratamiento de datos —que exista y sea anterior a recibir sus datos— y contra la conservación de la política cuando su proceso terminó; lo que llegó y no se debe tratar se dice y se excluye | Cada candidato con su autorización, hasta cuándo se conservan sus datos y lo que se excluyó |
| 6 | `vacancy-status` | El registro de `20-vacantes/` y el plazo de cobertura de la política | Cada vacante abierta contra el plazo de la política, o el suyo si el registro lo trae, contado desde su apertura | Cada vacante con su perfil, su apertura, su plazo, su tope y los días que lleva; las que pasaron su plazo |
| 7 | `talent-wake` | La configuración, el registro de corridas y lo que cambió en la carpeta | Decide si tocan hojas de vida nuevas, una vacante que vence o un reporte con señales abiertas; si no toca nada, se calla | Lo que tocaba y lo que hizo, o una línea si no tocaba nada |
| 8 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /chro:comandos-candido -->

## La prueba de sesgo

Además del material con su clave, la familia lleva una prueba que ninguna otra necesita: **pares de
candidatos idénticos salvo en un dato protegido** —la fotografía, la fecha de nacimiento, el sexo, el
origen—. El motor tiene que entregar exactamente lo mismo para los dos miembros de cada par, salvo el aviso
de lo que excluyó; cualquier diferencia es un defecto que bloquea la versión. En la ronda, la misma prueba
se le pide al agente.

## Cifras de terceros

<!-- chro:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (ManpowerGroup), C-02 (HireRight), C-03 (SHRM).
<!-- /chro:cifras -->

## Decisiones cerradas

- Los nombres, Norma y Cándido, y la estructura: dos agentes, sus quince señales y sus comandos (decisión 0031).
- Los estándares de la 0.1.0: la CUOC 2026 y O*NET 31.0, desde su descarga oficial. ESCO entra cuando se verifiquen su descarga y sus términos.
- SFIA queda fuera hasta confirmar con la SFIA Foundation si una herramienta de código abierto que la cita necesita su licencia de socio.
