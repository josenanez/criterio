# criterio-clo · la familia de la función legal

**Estado: construida y en prueba.** Los catorce comandos, los skills y el motor de cálculo están
construidos; el motor pasa su prueba determinista contra el material de cuatro industrias y dos
entidades de control (`tests/criterio-clo/`), y la prueba con el agente es el paso siguiente.
Alcance en [ADR 0009](../../docs/decisions/0009-scope-clo.md).

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

**De dónde sale este documento.** Las tablas de agentes, carpetas, señales, comandos y cifras no se
escriben aquí: salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y
[`fuentes.json`](fuentes.json), que `scripts/familias.py` escribe en este diseño, en
`FUENTES.es.md`, en los README de los plugins y, con `scripts/criterio-clo.mjs`, en el portal.

## Un agente por rol

<!-- clo:agentes · x -->
<!-- /clo:agentes -->

Como en las familias PMO y CFO, los dos no se hablan entre sí: se hablan por sus fichas. Constanza
toma de las fichas de Fidel las obligaciones de cumplimiento que traen los contratos.

## Lo que procesa el motor y lo que extrae el agente

Como en la familia CFO ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)), el
motor procesa las tablas directamente —el registro de contratos, los pagos, la matriz de
atribuciones, la matriz de obligaciones, el índice de políticas, el registro normativo y el de
casos—, y el agente extrae a la ficha lo que solo trae un documento escrito: **cada contrato**,
con sus partes, valor, fechas, renovación, preaviso, firmantes, otrosíes, garantías y
obligaciones; cada póliza con su vigencia; el certificado de la contraparte con su fecha; lo que
declara el informe de cumplimiento y las normas nuevas de un boletín. Cada dato con su cita.

## Las señales: lo que calcula el código

<!-- clo:senales · x -->
<!-- /clo:senales -->

Los días de aviso, la antigüedad máxima del certificado, el plazo del canal y los días para
evaluar una norma son configuración de cada organización, con un valor por defecto declarado;
ninguno es una norma.

## Las tres clases

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

## La estructura de carpetas

Recomendada, no obligatoria ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)): los
agentes procesan la carpeta como esté. `legal-setup` y `compliance-setup` comparan lo que
encuentran con esta estructura y dicen qué archivo está fuera de su lugar y dónde iría; no crean,
mueven ni renombran nada en los documentos de la organización.

<!-- clo:carpetas · x -->
<!-- /clo:carpetas -->

Un archivo sin el formato esperado no se adivina: se reporta con lo que le falta.

## Los comandos de Fidel, en orden de importancia

<!-- clo:comandos-fidel · x -->
<!-- /clo:comandos-fidel -->

## Los comandos de Constanza, en orden de importancia

<!-- clo:comandos-constanza · x -->
<!-- /clo:comandos-constanza -->

## El formato común de los reportes

El mismo de las familias PMO y CFO, y lo escribe el motor: encabezado, lo que hay que atender, el
resultado propio del comando, lo que no se pudo procesar, las preguntas que hizo y las fuentes.

## Cómo se prueba

Material sintético en `tests/criterio-clo/`: cuatro industrias —banca y retail en Colombia,
cooperativas y minería en Ecuador— y un control por país, con una clave que el motor no ve. Cada
señal de la familia se siembra al menos una vez; qué se siembra y dónde, en
[`tests/criterio-clo/EVIDENCIA.md`](../../tests/criterio-clo/EVIDENCIA.md). La extracción del
agente se prueba en la ronda, sobre el mismo material. La familia se declara probada con una ronda
completa.

## Cifras de terceros

<!-- clo:cifras · x -->
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
