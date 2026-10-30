[English](DISENO.md) · [← La familia](README.es.md)

# criterio-clo · el diseño de la familia

**Estado: construida y probada sobre material sintético.** Los catorce comandos, los diez skills y el motor de cálculo están
construidos; el motor pasa su prueba determinista contra el material de cuatro industrias y dos
entidades de control (`tests/criterio-clo/`), y los agentes pasaron la ronda completa sobre las seis entidades ([las rondas](../../tests/evidencias/familias/clo/RONDAS.md)).
Alcance en [ADR 0009](../../docs/decisions/0009-scope-clo.md).

**Esta es la hoja de diseño de la familia**: los documentos que procesa, las señales que calcula el código, cada comando con su entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, sus fichas y sus invariantes, la estructura de carpetas, Rostrum, la cadencia, las pruebas y la hoja de ruta están en su [página](README.es.md).

Dos agentes que extienden la capacidad de la función legal: procesan lo que la empresa firmó y lo
que se obligó a cumplir, y lo contrastan contra todos los soportes para señalar qué vence, qué no
tiene evidencia, quién firmó sin facultad y qué se pagó por fuera de lo pactado. El modelo de
lenguaje (LLM) extrae; el código calcula; la decisión —renovar, terminar, cómo se interpreta una
cláusula o una norma— la toma siempre una persona.

Primera versión: Colombia y Ecuador. **Sin opinión jurídica**: ninguno de los dos interpreta una
cláusula, califica la validez de un contrato ni dice qué exige una norma. Lo que una obligación
exige lo define la organización en su matriz, con la cita de su fuente.

**Cómo trabajan.** Automatizados: procesan los documentos, calculan las señales y preparan cada
entregable sin intervención. Semiautomatizados cuando falta un dato que ningún documento trae
—la entidad, los días de aviso, quién decide renovar—: entonces le preguntan a la persona, dicen
qué preguntaron y siguen con la respuesta.

**Fuentes.** Toda fuente que se usa para procesar —marcos, normas, cifras de terceros— está en
[`FUENTES.es.md`](FUENTES.es.md) con su versión, su enlace, la fecha de consulta y su estado. El diseño,
la documentación y las pruebas citan esas fuentes por su identificador.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se
escriben aquí: salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y
[`fuentes.json`](fuentes.json), que `scripts/familias.py` escribe en este diseño, en
`FUENTES.es.md`, en la página de la familia, en los README de los plugins y, con `scripts/criterio-familias.mjs`, en el portal.

**Lo que más se pregunta**, en [`PREGUNTAS.es.md`](PREGUNTAS.es.md) ([English](PREGUNTAS.md)), y **hacia dónde va**, en la [hoja de ruta](README.es.md#hoja-de-ruta).

## Un agente por rol

<!-- clo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| Contratos | **Fidel** — del latín *fides*, la palabra dada: lo firmado se cumple | `criterio-legal` | Lo firmado y en qué términos: el registro de contratos contra sus documentos, los vencimientos y los preavisos de renovación, las obligaciones con su evidencia, quién firmó con qué facultad y lo pagado contra lo pactado y sus garantías |
| Cumplimiento | **Constanza** — del latín *constantia*, «constancia»: cumplir siempre, no solo el día de la auditoría | `criterio-compliance` | La matriz de obligaciones de la organización contra su evidencia, la revisión de las políticas, las normas nuevas con su evaluación, el canal de denuncias con sus plazos y las obligaciones de cumplimiento que traen los contratos |
<!-- /clo:agentes -->

Como en las familias PMO y CFO, los dos no se hablan entre sí: se hablan por sus fichas. Constanza
toma de las fichas de Fidel las obligaciones de cumplimiento que traen los contratos. Las fichas y las
invariantes que las gobiernan, en la [página de la familia](README.es.md#los-dos-agentes-y-sus-fichas).

## Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| Registro de contratos y exportación de pagos por contrato | Excel o CSV, con la fecha de corte en el nombre | Fidel |
| Matriz de atribuciones: quién firma qué y hasta qué monto | Excel o CSV | Fidel |
| El contrato firmado y cada otrosí | Word o PDF con texto | Fidel |
| Pólizas y garantías aportadas | PDF con texto | Fidel |
| Certificado de existencia y representación de la contraparte | PDF con texto | Fidel |
| Acta o correo en que alguien decide renovar o terminar | Word, PDF, correo | Fidel |
| Actas de entrega, informes y la evidencia de cada obligación | Cualquier formato, con el id de la obligación al inicio del nombre | Fidel, Constanza |
| Matriz de obligaciones de cumplimiento | Excel o CSV, en el modelo definido | Constanza |
| Índice de políticas, y cada política | Excel o CSV; la política, Word o PDF | Constanza |
| Registro normativo, boletines y evaluaciones de impacto | Excel o CSV; el boletín, PDF o correo | Constanza |
| Registro de casos del canal de denuncias | Excel o CSV, solo con sus fechas | Constanza |
| Informe de cumplimiento del periodo | Word o PDF | Constanza |

Las columnas que necesita cada tabla, y sus variantes, en el skill `legal-intake`. Dónde va cada
documento, en la [estructura de carpetas recomendada](README.es.md#la-estructura-de-carpetas-recomendada).

### Lo que procesa el motor y lo que extrae el agente

Como en la familia CFO ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)), el
motor procesa las tablas directamente —el registro de contratos, los pagos, la matriz de
atribuciones, la matriz de obligaciones, el índice de políticas, el registro normativo y el de
casos—, y el agente extrae a la ficha lo que solo trae un documento escrito: **cada contrato**,
con sus partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías y
obligaciones; cada póliza con su vigencia; el certificado de la contraparte con su fecha; lo que
declara el informe de cumplimiento y las normas nuevas de un boletín. Cada dato con su cita.

## Las señales: lo que calcula el código

<!-- clo:senales · generado por scripts/familias.py; no se edita a mano -->
**Fidel · Contratos**

| Señal | Se levanta cuando |
|---|---|
| `contract_expiring` | Un contrato vence dentro de los días configurados y no tiene una decisión registrada de renovar o terminar |
| `notice_deadline_near` | La fecha límite del preaviso de no renovación de un contrato con renovación automática cae dentro de los días configurados |
| `renewal_notice_missed` | Pasó la fecha límite del preaviso de un contrato con renovación automática sin una decisión registrada |
| `contract_expired_active` | El registro reporta vigente un contrato cuya fecha de terminación ya pasó |
| `register_mismatch` | Un contrato de la carpeta no está en el registro, o una fila del registro no tiene su documento |
| `register_differs_from_contract` | El valor o las fechas del registro no son los del documento |
| `contract_obligation_overdue` | Una obligación del contrato pasó su fecha sin evidencia |
| `signed_without_authority` | Quien firmó por la entidad no tenía facultad por el tipo o el monto según la matriz de atribuciones |
| `unsigned_contract` | El documento no tiene la firma de las dos partes y el contrato ya empezó |
| `counterparty_certificate_stale` | El certificado de la contraparte tenía más días de los configurados cuando se firmó |
| `payments_over_value` | Lo pagado supera el valor del contrato más sus otrosíes |
| `payment_after_termination` | Hay pagos con fecha posterior a la terminación del contrato |
| `guarantee_missing` | El contrato exige una garantía y no hay póliza aportada |
| `guarantee_expires_early` | La póliza aportada vence antes de lo que exige el contrato |
| `public_contract_not_published` | Un contrato de una entidad pública no se publicó en el sistema nacional dentro del plazo de la ley de su país |
| `public_guarantee_below_law` | La garantía de cumplimiento de un contrato público es menor que el mínimo de la ley de su país |
| `public_guarantee_over_cap` | La garantía exigida en un contrato público supera el tope de la ley de su país |
| `public_guarantee_late` | La garantía de cumplimiento de un contrato público se entregó después del plazo de la ley de su país |

**Constanza · Cumplimiento**

| Señal | Se levanta cuando |
|---|---|
| `compliance_obligation_overdue` | Una obligación de la matriz pasó su fecha límite sin evidencia |
| `compliance_done_without_evidence` | Una obligación figura cumplida y ninguna evidencia la sostiene |
| `compliance_evidence_stale` | La evidencia más reciente de una obligación periódica es de antes de su ventana |
| `obligation_without_owner` | Una obligación de la matriz no tiene responsable |
| `obligation_without_source` | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale |
| `declared_compliance_vs_evidence` | El informe declara el cumplimiento del periodo y hay señales abiertas que ese estado no explica |
| `policy_review_overdue` | Una política pasó su fecha de revisión |
| `regulatory_change_unassessed` | Una norma registrada lleva más días de los configurados sin evaluación de impacto |
| `applicable_norm_not_in_matrix` | Una norma que aplica no tiene ninguna obligación en la matriz |
| `report_case_overdue` | Un caso del canal de denuncias pasó el plazo de respuesta configurado |
| `contract_obligation_not_in_matrix` | Una obligación de cumplimiento de un contrato no está en la matriz |
<!-- /clo:senales -->

Los días de aviso, la antigüedad máxima del certificado, el plazo del canal y los días para
evaluar una norma son configuración de cada organización, con un valor por defecto declarado;
ninguno es una norma.

## Las tres clases, como en la familia PMO

**A · Lo que hace, y hoy consume tiempo de alguien:** armar el registro de contratos, llevar el
calendario de vencimientos y preavisos, revisar quién firmó cada contrato, cruzar los pagos contra
lo pactado, preparar el estado del cumplimiento contra su evidencia.

**B · Lo que hace, y hoy no se hace:** revisar todos los contratos, no una muestra, contra la
matriz de atribuciones; cruzar todos los pagos contra el valor y la terminación de su contrato;
verificar cada póliza contra la vigencia que exige el contrato; llevar al día la matriz de
obligaciones con lo que los contratos obligan.

**C · Lo que no hace:** no interpreta cláusulas ni normas; no califica la validez de un contrato ni
de una firma; no decide renovar ni terminar; no redacta ni negocia; no responde casos del canal de
denuncias ni procesa datos de quién denunció; no declara el estado del cumplimiento.

## Los comandos de Fidel, en orden de importancia

<!-- clo:comandos-fidel · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `legal-setup` | La carpeta raíz. Preguntas: entidad y NIT o RUC, país, la matriz de atribuciones de `00-referencia/`, con cuántos días de anticipación se avisa un vencimiento o un preaviso, la antigüedad máxima del certificado de la contraparte, quién decide renovar y si la entidad es pública | Inventario de lo que hay; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; los contratos de `contratos/` contra los del registro; las primeras fichas |
| 1 | `contract-scan` | `contratos/` completo y `10-registro/` | Extrae el texto de cada documento con su huella y solo reprocesa lo que cambió; el agente lleva a la ficha de cada contrato sus partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías y obligaciones, cada dato con su cita; el motor valida la ficha | Qué cambió; qué contratos son nuevos; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `contract-register` | `10-registro/registro-contratos` y las fichas | Cruza el registro con las carpetas y con las fichas: contrato sin registro, registro sin documento, estado declarado contra la fecha de terminación, y el valor y las fechas del registro contra lo que dice el documento | Por contrato: estado declarado y estado según sus fechas, y cada diferencia entre el registro y el documento |
| 3 | `obligations-calendar` | Las fichas y `40-ejecucion/` de cada contrato | Fecha de terminación, fecha límite del preaviso de no renovación (terminación menos los días de preaviso) y cada obligación con fecha contra su evidencia en `40-ejecucion/`, con su id al inicio del nombre | El calendario de los próximos días: vencimientos, preavisos y obligaciones; lo vencido sin evidencia y los preavisos que pasaron sin decisión |
| 4 | `authority-check` | Las fichas, `00-referencia/matriz-atribuciones` y `30-contraparte/` | Cada firmante de la entidad contra su facultad a la fecha de firma, por tipo y monto, otrosíes incluidos; los documentos sin la firma de las dos partes; el certificado de la contraparte contra la antigüedad configurada a la fecha de firma | Por contrato: quién firmó, su facultad y el monto; los que no tienen firma de las dos partes; los certificados vencidos; sin opinión sobre la validez del contrato |
| 5 | `contract-execution` | `10-registro/pagos`, las fichas y `20-garantias/` | Lo pagado contra el valor más los otrosíes; los pagos después de la terminación; las garantías exigidas contra las aportadas y su vigencia contra la que exige el contrato | Por contrato: valor, pagado, saldo y último pago; cada garantía exigida con la aportada y su vigencia |
| 6 | `legal-wake` | La configuración y las fichas | Decide qué toca: los vencimientos y preavisos que entran en la ventana, los documentos nuevos y una revisión semanal | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /clo:comandos-fidel -->

## Los comandos de Constanza, en orden de importancia

<!-- clo:comandos-constanza · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `compliance-setup` | La carpeta raíz. Preguntas: entidad, país, la matriz de obligaciones de `00-referencia/` en el modelo definido (F-01), el periodo, el plazo de respuesta del canal, los días para evaluar una norma nueva y, si la organización usa a Fidel, dónde están sus fichas | Inventario de lo que hay; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; la matriz cargada y lo que le falta a cada obligación —responsable, fuente—; el primer estado del periodo |
| 1 | `compliance-scan` | Toda la carpeta de la entidad | Reprocesa solo lo que cambió; el agente lleva a la ficha lo que declara el informe de `20-reportes/` y las normas nuevas de los boletines de `30-normativa/`, con su cita | Qué cambió; qué se agregó a la ficha; las señales nuevas; lo que no se pudo procesar |
| 2 | `compliance-status` | `00-referencia/matriz-obligaciones`, `10-evidencias/` del periodo y de los anteriores, y las fichas de Fidel si las hay | Cada obligación contra su evidencia en la ventana de su periodicidad y su fecha límite; las que no tienen responsable ni fuente; las obligaciones de cumplimiento de los contratos que la matriz no tiene; lo declarado contra lo evidenciado | Estado declarado contra evidenciado; tabla de obligaciones ordenada por criticidad y vencimiento: cumplida con evidencia, cumplida sin evidencia, vencida, en plazo |
| 3 | `policy-review` | `20-politicas/indice-politicas` | Cada política contra su fecha de revisión y su responsable | Las políticas con la revisión vencida o sin responsable, y las próximas a revisar |
| 4 | `regulatory-watch` | `30-normativa/registro-normativo` y las normas nuevas de la ficha | Cada norma registrada contra su evaluación de impacto en los días configurados; las que aplican sin una obligación en la matriz | Las normas sin evaluar y las que aplican sin obligación en la matriz; sin opinión sobre el alcance de ninguna norma |
| 5 | `reports-cases` | `40-canal/casos` | Cada caso contra el plazo de respuesta configurado | Los casos abiertos por antigüedad y los que pasaron su plazo; sin datos de quién denunció |
| 6 | `compliance-wake` | La configuración y la ficha | Decide qué toca: las obligaciones que vencen en la ventana, los documentos nuevos y una revisión semanal | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /clo:comandos-constanza -->

## El formato común de los reportes

El mismo de las familias PMO y CFO, y lo escribe el motor: encabezado, lo que hay que atender, el
resultado propio del comando, lo que no se pudo procesar, las preguntas que hizo y las fuentes.

## Lo que se reusa de las familias PMO y CFO

- `texto.py` para Word, Excel, PowerPoint, PDF y correo, `terminos.py` para la aceptación de los
  términos, `rastro.py` para el rastro de cada corrida y `raiz.py` para la carpeta raíz, copiados
  de la familia PMO por `scripts/sincronizar.py`.
- `nucleo.py` —tablas, fechas, inventario, señales y reporte—, copiado de `criterio-finance`.
- La forma de la ficha: cita por dato, declarado contra evidenciado, «no encontrado» válido.
- Los términos por versión con su comprobante, el registro de versiones y las puertas de
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, para publicar los reportes de los contratos y del cumplimiento
  ([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

Lo nuevo es el motor propio, `legal.py`, con librería estándar: procesa las tablas directamente, y
el agente extrae a la ficha solo lo que trae un documento escrito. Vive en `criterio-legal` y se
copia a `criterio-compliance`, con el skill `legal-intake`.

## Cómo se prueba

Material sintético en `tests/criterio-clo/`: cuatro industrias —banca y retail en Colombia,
cooperativas y minería en Ecuador— y un control por país, con una clave que el motor no ve. Cada
señal de la familia se siembra al menos una vez; qué se siembra y dónde, en
[`tests/criterio-clo/EVIDENCIA.md`](../../tests/criterio-clo/EVIDENCIA.md). La extracción del
agente se prueba en la ronda, sobre el mismo material. La familia se declara probada con una ronda
completa.

## Cifras de terceros

<!-- clo:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (World Commerce & Contracting con Deloitte), C-02 (EY Law y Harvard Law School Center on the Legal Profession), C-03 (EY Law y Harvard Law School Center on the Legal Profession), C-04 (NAVEX).
<!-- /clo:cifras -->

## Decisiones cerradas

- Los roles —contratos y cumplimiento— y los nombres, Fidel y Constanza. José, 2026-10-20.
- Los plugins: `criterio-legal` para Fidel, el que ya estaba declarado, y `criterio-compliance`
  para Constanza. José, 2026-10-20.
- Sin opinión jurídica en la primera versión. José, 2026-10-20.

## Decisiones abiertas

1. Un modelo recomendado de matriz de obligaciones por industria, y quién lo revisa antes de
   proponerlo como algo más que un borrador.
2. Los contratos públicos, con sus propias reglas de publicación y de garantías, quedan para otra
   versión.
