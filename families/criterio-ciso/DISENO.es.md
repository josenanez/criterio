[English](DISENO.md) · [← La familia](README.es.md)

# criterio-ciso · el diseño de la familia

**Estado: de laboratorio, sin lanzar (versión 0.1.0).** Los veinte comandos, los siete skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista contra el material de banca,
retail, salud y tecnología (`tests/criterio-ciso/`), y la ronda con los agentes es el siguiente paso, en
la 0.2.0. Alcance en [ADR 0023](../../docs/decisions/0023-la-familia-ciso.md).

**Esta es la hoja de diseño de la familia**: los documentos que procesa, las señales que calcula el
código, cada comando con su entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la
familia, cómo se instala, sus fichas y sus invariantes, la estructura de carpetas, Rostrum, la cadencia,
las pruebas y la hoja de ruta están en su [página](README.es.md).

Tres agentes que extienden la capacidad de la seguridad de la información: procesan la declaración de
aplicabilidad, la evidencia de cada control, las exportaciones del escáner, los informes de incidentes y
de pruebas, y los contrastan contra la política, la matriz de notificaciones y los registros de la
organización. El modelo de lenguaje (LLM) extrae; el código calcula; la decisión —aceptar un riesgo,
aprobar una excepción, notificar— la toma siempre una persona.

**A diferencia de la CFO o la CLO, el rol se define sobre estándares internacionales**, no sobre la ley de
cada país: el NIST CSF 2.0 ordena la familia (F-02) y el NIST SP 800-61 Rev. 3 la respuesta a incidentes
(F-04). La regulación de cada país —la circular del supervisor financiero, la ley de datos— entra a la
matriz de notificaciones de la organización; el motor no la trae.

**Cómo trabajan.** Automatizados: procesan los documentos, calculan las señales y preparan cada entregable
sin intervención. Semiautomatizados cuando falta un dato que ningún documento trae —un plazo que la
política no dice, qué columna del escáner trae cada dato—: entonces le preguntan a la persona, dicen qué
preguntaron y siguen con la respuesta.

**Fuentes.** Toda fuente que se usa para procesar —el marco del rol, los marcos de la familia, la escala
del CVSS, el formato del catálogo KEV, las cifras de terceros— está en [`FUENTES.es.md`](FUENTES.es.md) con
su versión, su enlace, la fecha de consulta y su estado.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json),
que `scripts/familias.py` escribe en este diseño, en `FUENTES.es.md`, en la página de la familia, en los
README de los plugins y, con `scripts/criterio-familias.mjs`, en el portal.

**Lo que más se pregunta**, en [`PREGUNTAS.es.md`](PREGUNTAS.es.md) ([English](PREGUNTAS.md)), y **hacia
dónde va**, en la [hoja de ruta](README.es.md#hoja-de-ruta).

## Un agente por rol

<!-- ciso:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| El gobierno y los controles | **Alexis** — del griego *Aléxios*, «el que defiende»: cada control contra la evidencia de que operó | `criterio-security` | La declaración de aplicabilidad contra la evidencia: cada control aplicable con su responsable y la evidencia de que operó en su periodicidad, las revisiones de acceso de cada sistema, las evaluaciones de cada tercero crítico y las aceptaciones de riesgo que pasaron su fecha |
| Las vulnerabilidades | **Guillermo** — del germánico *Wilhelm*, «protector decidido»: cada vulnerabilidad contra el plazo para corregirla | `criterio-vulnerability` | Cada vulnerabilidad de las exportaciones del escáner contra el plazo de su severidad en la política, el catálogo KEV, las excepciones aprobadas, los cierres que ningún escaneo prueba y los activos del inventario que ningún escaneo cubre |
| La respuesta y la recuperación | **Amparo** — del latín *ante parare*, «prevenir, proteger»: cada incidente contra los plazos que se comprometieron | `criterio-resilience` | Cada incidente contra los plazos de la política y la matriz de notificaciones: la contención de su severidad, cada notificación al supervisor, a la autoridad de datos o a los clientes, y su revisión posterior; y las pruebas de continuidad, de recuperación y de restauración contra su calendario |
<!-- /ciso:agentes -->

## Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| La declaración de aplicabilidad: cada control con si aplica, su estado, su responsable y su periodicidad | Excel o CSV | Alexis |
| La tabla de sistemas con cada cuántos días se revisan sus accesos, y el registro de terceros con los críticos y su evaluación | Excel o CSV | Alexis |
| El registro de riesgos, con la decisión sobre cada uno y su fecha de revisión | Excel o CSV | Alexis |
| La evidencia de cada control, cada revisión de accesos y cada evaluación de un tercero | Cualquier formato, con el control, el sistema o el tercero en el nombre | Alexis |
| La política de gestión de vulnerabilidades, con el plazo de cada severidad | Word o PDF | Guillermo |
| Cada exportación del escáner, con la fecha del escaneo en el nombre | CSV o Excel, con su mapeo de columnas si no se reconocen | Guillermo |
| El catálogo KEV de CISA, como se descarga (F-06) | CSV | Guillermo |
| El inventario de activos, el seguimiento de la remediación y el registro de excepciones | Excel o CSV | Guillermo |
| La política de respuesta a incidentes, con el plazo de contención de cada severidad y el de la revisión posterior | Word o PDF | Amparo |
| La matriz de notificaciones y el calendario de continuidad | Excel o CSV | Amparo |
| El informe de cada incidente con su línea de tiempo y la constancia de cada notificación, su revisión posterior y el informe de cada prueba | Word, PDF o correo, con el código del incidente al inicio del nombre | Amparo |

Las columnas que necesita cada tabla, y sus variantes, en el skill `security-intake`; cómo se procesa
cada exportación del escáner, en `scanner-exports`. Dónde va cada documento, en la
[estructura de carpetas recomendada](README.es.md#la-estructura-de-carpetas-recomendada).

### Lo que procesa el motor y lo que extrae el agente

Como en las demás familias ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)), el motor
procesa las tablas directamente, y el agente extrae a la ficha lo que solo trae un documento escrito:
**la evidencia de un control** con la fecha que cubre; **la revisión de accesos** de un sistema y **la
evaluación** de un tercero; **la línea de tiempo de un incidente** con la hora de la detección, de la
contención y del cierre, y **cada notificación** con su constancia; **cada prueba** con su fecha y su
resultado. En el setup, el agente extrae de la política los plazos de cada severidad, con su cita. Cada
dato con su cita.

**Lo que nunca se procesa.** Credenciales, llaves y respaldos —por su extensión o por su nombre— quedan
fuera por omisión: el motor los lista y cada reporte dice cuáles excluyó.

## Las señales: lo que calcula el código

<!-- ciso:senales · generado por scripts/familias.py; no se edita a mano -->
**Alexis · El gobierno y los controles**

| Señal | Se levanta cuando |
|---|---|
| `control_without_evidence` | Un control aplicable de la declaración figura implementado y no tiene ninguna evidencia de que operó |
| `control_evidence_stale` | La evidencia más reciente de un control periódico es anterior a su periodicidad |
| `soa_control_unassigned` | Un control aplicable no tiene responsable |
| `access_review_overdue` | La revisión de accesos de un sistema pasó su fecha, o no hay ninguna |
| `third_party_assessment_overdue` | La evaluación de seguridad de un tercero crítico pasó su fecha, o no hay ninguna |
| `risk_acceptance_expired` | Una aceptación de riesgo pasó su fecha de revisión |

**Guillermo · Las vulnerabilidades**

| Señal | Se levanta cuando |
|---|---|
| `vuln_past_sla` | Una vulnerabilidad sigue abierta después del plazo de su severidad en la política, sin una excepción vigente |
| `kev_past_due` | Una vulnerabilidad del catálogo KEV sigue abierta después de su fecha de corrección |
| `vuln_closed_without_rescan` | Una vulnerabilidad figura cerrada y ningún escaneo posterior la da por corregida |
| `vuln_exception_expired` | Una excepción a la corrección pasó su vencimiento y la vulnerabilidad sigue abierta |
| `asset_not_scanned` | Un activo del inventario no aparece en ningún escaneo de la ventana configurada |

**Amparo · La respuesta y la recuperación**

| Señal | Se levanta cuando |
|---|---|
| `incident_response_late` | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo |
| `incident_notification_late` | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo |
| `incident_without_review` | Un incidente cerrado no tiene su revisión posterior dentro del plazo |
| `continuity_test_overdue` | La prueba del plan de continuidad o de recuperación pasó su fecha, o no hay ninguna |
| `restore_test_overdue` | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna |
<!-- /ciso:senales -->

Los plazos de corrección, de contención y de revisión, los de cada notificación y la frecuencia de cada
revisión y de cada prueba salen de la política, la matriz y los registros de la organización. La ventana
de escaneo es configuración, con un valor por defecto declarado. La fecha de corrección del catálogo KEV
la trae el catálogo, y la fija una directiva para las agencias federales de los Estados Unidos (F-07): para
la organización es una referencia.

## Las tres clases, como en la familia PMO

**A · Lo que hace, y hoy consume tiempo de alguien:** preparar la evidencia de los controles para la
auditoría, armar el reporte de vulnerabilidades fuera de plazo para el comité, reconstruir la línea de
tiempo de un incidente para el supervisor, y llevar el calendario de pruebas.

**B · Lo que hace, y hoy no se hace:** revisar todos los controles aplicables, no una muestra, contra su
evidencia; cruzar cada hallazgo de cada escaneo con el catálogo de lo que se explota; probar cada cierre
con un escaneo posterior; poner cada notificación al lado de su plazo con la hora de su constancia.

**C · Lo que no hace:** no corre un escaneo ni se conecta a un sistema; no acepta un riesgo ni aprueba una
excepción; no declara cumplido un control ni califica la madurez; no certifica contra la ISO/IEC 27001; no
notifica a nadie ni declara un incidente; no ejecuta una prueba ni una restauración; no abre credenciales,
llaves ni respaldos.

## Los comandos de Alexis, en orden de importancia

<!-- ciso:comandos-alexis · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `security-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, dónde está la declaración de aplicabilidad de `00-referencia/` y qué columna trae el control, si aplica, su estado, su responsable y su periodicidad, la tabla de sistemas con la frecuencia de su revisión de accesos, el registro de terceros con los críticos y la frecuencia de su evaluación, y el registro de riesgos de `40-riesgos/` | Inventario de lo que hay; lista lo que excluye por ser una credencial, una llave o un respaldo; reconoce las columnas de cada tabla; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; lo excluido y por qué; las columnas que faltan; la primera ficha del periodo |
| 1 | `security-scan` | `10-controles/`, `20-accesos/` y `30-terceros/` completos | El agente lleva a la ficha del periodo cada evidencia de `10-controles/` con su control y la fecha que cubre, cada revisión de `20-accesos/` con su sistema, su fecha y quién revisó, y cada evaluación de `30-terceros/` con su tercero, su fecha y su resultado, cada dato con su cita; el motor valida la ficha y dice qué documento no está en ella | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `soa-status` | La declaración de aplicabilidad de `00-referencia/` | Cada control de la declaración con si aplica, su estado, su responsable y su periodicidad; el motor no califica la madurez ni declara cumplido un control | Los controles aplicables sin responsable, con su fila; la declaración completa |
| 3 | `control-evidence` | La declaración de aplicabilidad y la ficha del periodo | Cada control aplicable que figura implementado contra la evidencia de la ficha: si tiene alguna, y si la más reciente cae dentro de su periodicidad | Los controles sin evidencia y los que tienen la evidencia vencida, cada uno con su cita y su responsable |
| 4 | `access-reviews` | La tabla de sistemas de `00-referencia/` y la ficha del periodo | Cada sistema contra la frecuencia de su revisión de accesos: la última revisión de la ficha y cuándo tocaba la siguiente | Los sistemas con la revisión vencida o sin ninguna, con su cita |
| 5 | `third-parties` | El registro de terceros de `00-referencia/` y la ficha del periodo | Cada tercero crítico contra la frecuencia de su evaluación de seguridad: la última de la ficha, su resultado y cuándo tocaba la siguiente | Los terceros críticos con la evaluación vencida o sin ninguna, con su cita |
| 6 | `risk-register` | El registro de riesgos de `40-riesgos/` | Cada riesgo con su decisión; los aceptados contra su fecha de revisión. El agente no acepta ni cierra un riesgo | Las aceptaciones que pasaron su fecha de revisión, con quién las aceptó y su fila |
| 7 | `security-wake` | El estado y los documentos nuevos | Si hay documentos nuevos o pasó una semana, la revisión completa; si hay señales abiertas, el reporte de su grupo; una pregunta que alguien dejó en Rostrum | Qué corrió y por qué, o que no tocaba nada |
<!-- /ciso:comandos-alexis -->

## Los comandos de Guillermo, en orden de importancia

<!-- ciso:comandos-guillermo · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `vuln-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, los plazos de corrección de cada severidad que da la política de gestión de vulnerabilidades de `00-referencia/`, de qué escáner salen las exportaciones de `50-escaneos/` y, si sus columnas no se reconocen, qué columna trae el activo, la vulnerabilidad, la severidad o el puntaje CVSS y la primera detección, cuántos días sin escaneo dejan un activo sin cobertura y si sus reportes se publican en Rostrum | Inventario de lo que hay; lista lo que excluye; reconoce las columnas de cada exportación del escáner y del catálogo KEV (F-06); el agente extrae de la política los plazos de cada severidad, con su cita; no crea, mueve ni renombra nada | Configuración guardada, con los plazos y su cita; inventario por carpeta; cada exportación con su fecha, sus activos y sus hallazgos; las columnas que faltan |
| 1 | `vuln-scan` | `50-escaneos/` y `60-remediacion/` completos | El código procesa cada exportación con su fecha: lo abierto es lo que encontró el último escaneo de cada activo, con la fecha de su primera detección; la severidad es la del escáner o, si solo trae el puntaje, la de la escala del CVSS (F-05); cruza el catálogo KEV (F-06), el seguimiento y las excepciones | Los escaneos con sus activos y sus hallazgos; lo abierto; el catálogo KEV que se usó; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `vuln-sla` | Las exportaciones de `50-escaneos/`, las excepciones de `60-remediacion/` y los plazos de la configuración | Cada vulnerabilidad abierta contra el plazo de su severidad, contado desde su primera detección; una excepción vigente la suspende; una excepción vencida sobre algo que sigue abierto es una señal | Las vulnerabilidades fuera de plazo y las excepciones vencidas, cada una con su activo, su severidad, sus días y su cita |
| 3 | `kev-check` | Las exportaciones de `50-escaneos/` y el catálogo KEV de CISA (F-06) | Cada vulnerabilidad abierta cuyo CVE está en el catálogo, contra la fecha de corrección que trae el catálogo; dice si se conoce su uso en ransomware | Las vulnerabilidades del catálogo que siguen abiertas después de su fecha, con su activo y su cita |
| 4 | `scan-coverage` | El inventario de activos de `00-referencia/`, las exportaciones de `50-escaneos/` y el seguimiento de `60-remediacion/` | Cada activo del inventario en alcance contra el último escaneo que lo incluye y la ventana configurada; cada vulnerabilidad cerrada en el seguimiento contra los escaneos posteriores a su cierre | Los activos sin escaneo en la ventana; los cierres que ningún escaneo posterior prueba o que el escaneo sigue encontrando; lo escaneado fuera del inventario |
| 5 | `vuln-wake` | El estado y los documentos nuevos | Si llegó una exportación, un catálogo o un seguimiento nuevo, o pasó una semana, la revisión completa; si hay señales abiertas, el reporte de su grupo; una pregunta que alguien dejó en Rostrum | Qué corrió y por qué, o que no tocaba nada |
<!-- /ciso:comandos-guillermo -->

Los reportes de Guillermo no se publican en Rostrum salvo que `vulnerability.publish` lo diga.

## Los comandos de Amparo, en orden de importancia

<!-- ciso:comandos-amparo · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `resilience-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, los plazos de contención de cada severidad y los días para la revisión posterior que da la política de respuesta a incidentes de `00-referencia/`, la matriz de notificaciones con cada destinatario, cuándo aplica y su plazo, y el calendario de continuidad con cada prueba, su tipo y su frecuencia | Inventario de lo que hay; lista lo que excluye; el agente extrae de la política los plazos de cada severidad y el de la revisión posterior, con su cita; reconoce las columnas de la matriz y del calendario; no crea, mueve ni renombra nada | Configuración guardada, con los plazos y su cita; inventario por carpeta; las columnas que faltan; la primera ficha del periodo |
| 1 | `resilience-scan` | `70-incidentes/`, `80-revisiones/` y `90-continuidad/` completos | El agente lleva a la ficha del periodo cada incidente de `70-incidentes/` con su severidad, la detección, la contención y el cierre con su hora, si hubo datos personales o clientes afectados, y cada notificación con su destinatario, su hora y su constancia; cada revisión de `80-revisiones/` y cada prueba de `90-continuidad/` con su fecha y su resultado; cada dato con su cita (F-04); el motor valida la ficha | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `incident-timeline` | La ficha del periodo y los plazos de la configuración | Cada incidente: las horas de la detección a la contención contra el plazo de su severidad, y su revisión posterior contra los días de la política desde el cierre | Los incidentes contenidos fuera de plazo o sin contener, y los cerrados sin revisión o revisados tarde, con su cita |
| 3 | `notifications` | La matriz de notificaciones de `00-referencia/` y la ficha del periodo | Cada incidente contra cada fila de la matriz que le aplica —por su severidad, por los datos personales o por los clientes afectados—: la notificación registrada y su hora contra el plazo desde la detección. El agente no notifica a nadie | Las notificaciones tardías y las que no se hicieron, con su destinatario, su norma y su cita |
| 4 | `continuity-tests` | El calendario de continuidad de `00-referencia/` y la ficha del periodo | Cada prueba del calendario —el plan de continuidad, el de recuperación, la restauración de cada respaldo crítico— contra su frecuencia: la última de la ficha, su resultado y cuándo tocaba la siguiente | Las pruebas vencidas o sin ninguna, separadas las de restauración, con su cita |
| 5 | `resilience-wake` | El estado y los documentos nuevos | Si llegó un incidente, una revisión o una prueba nueva, o pasó una semana, la revisión completa; si hay señales abiertas, el reporte de su grupo; una pregunta que alguien dejó en Rostrum | Qué corrió y por qué, o que no tocaba nada |
<!-- /ciso:comandos-amparo -->

## El formato común de los reportes

El mismo de las demás familias, y lo escribe el motor: encabezado, lo que hay que atender, el resultado
propio del comando, lo que no se pudo procesar —incluido lo excluido—, las preguntas que hizo y las
fuentes.

## Lo que se reusa de las demás familias

- `texto.py` para Word, Excel, PowerPoint, PDF y correo, `terminos.py` para la aceptación de los
  términos, `rastro.py` para el rastro de cada corrida y `raiz.py` para la carpeta raíz, copiados por
  `scripts/sincronizar.py`.
- `nucleo.py` —tablas, fechas, inventario, señales y reporte—, copiado de `criterio-finance`.
- La forma de la ficha: cita por dato, «no encontrado» válido.
- Los términos por versión con su comprobante, el registro de versiones y las puertas de
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, para publicar los reportes, con lo privado fuera por omisión
  ([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md), ADR 0019).

Lo nuevo es el motor propio, `seguridad.py`, con librería estándar. Vive en `criterio-security` y se copia
a `criterio-vulnerability` y `criterio-resilience`, con el skill `security-intake`.

## Cómo se prueba

Material sintético en `tests/criterio-ciso/`: una entidad de banca, una de retail, una de salud y una de
tecnología, en Colombia, México, Perú y Chile, y dos controles, con una clave que el motor no ve. Cada
señal de la familia se siembra al menos una vez, con casos que se parecen a un defecto y no lo son; qué
se siembra y dónde, en [`tests/criterio-ciso/EVIDENCIA.md`](../../tests/criterio-ciso/EVIDENCIA.md). La
extracción del agente se prueba en la ronda, sobre el mismo material.

## Cifras de terceros

<!-- ciso:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Verizon), C-02 (Verizon), C-03 (Verizon).
<!-- /ciso:cifras -->

## Decisiones cerradas

- El alcance, los tres agentes, sus dieciséis señales y lo que nunca hacen (ADR 0023). José, 2026-10-30.
- Los nombres, Alexis, Guillermo y Amparo, y la estructura de la familia. José, 2026-10-30.
- Los plugins: `criterio-security`, `criterio-vulnerability` y `criterio-resilience`.
- La primera versión procesa cualquier exportación de escáner con su mapeo; cada producto entra después
  desde su fuente verificada.

## Decisiones abiertas

1. El formato de exportación de Tenable, Qualys, Rapid7 y Microsoft Defender, cada uno desde su fuente.
2. La ISO/IEC 27001:2022 (F-03) sigue por verificar: el motor no la necesita, porque toma los controles
   de la declaración de la organización; si algún día se cita, se verifica antes.
3. La BOD 26-04 de CISA (F-07) sigue por verificar en la página de CISA; el motor no aplica sus plazos.
