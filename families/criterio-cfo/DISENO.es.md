# criterio-cfo · la familia de la función financiera

**Estado: en diseño.** Nada de lo que sigue está construido ni probado. Decisión de alcance en
[ADR 0006](../../docs/decisions/0006-scope-cfo.md).

Dos agentes que extienden la capacidad de la función financiera: preparan el trabajo del cierre
y del presupuesto, y lo contrastan contra todos los soportes para señalar qué no cuadra, qué no
tiene soporte y qué se reporta distinto de lo que dicen los documentos. El modelo de lenguaje
(LLM) extrae; el código calcula; el estado del cierre y del presupuesto lo declara siempre una
persona.

Primera versión: NIIF adoptadas localmente, en Colombia y Ecuador, con la factura electrónica de
la DIAN y del SRI.

**Cómo trabajan.** Automatizados: procesan los documentos, calculan las señales y preparan cada
entregable sin intervención. Semiautomatizados cuando falta un dato que ningún documento trae
—la entidad, el periodo, el umbral, quién aprueba—: entonces le preguntan a la persona, dicen qué
preguntaron y siguen con la respuesta.

**Fuentes.** Toda fuente que se usa para procesar —anexos técnicos, normas, cifras de terceros—
está en [`FUENTES.es.md`](FUENTES.es.md) con su versión, su enlace, la fecha de consulta y su
estado. El diseño, la documentación y las pruebas citan esas fuentes por su identificador.

## Un agente por rol

| Rol | Agente  | Plugin | Qué hace |
|---|---|---|---|
| Contralor | **Clara** — de *clarus*: que los libros digan lo mismo que los soportes | `criterio-finance` | El cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, la factura electrónica contra la contabilidad y el paquete para el auditor |
| FP&A | **Tomás** — «el gemelo»: pone el presupuesto al lado de su gemelo, la ejecución | `criterio-budget` | El presupuesto aprobado contra lo ejecutado y lo comprometido, la proyección al cierre del año, los traslados y el material del comité de presupuesto |

Como en la familia PMO, los dos no se hablan entre sí: se hablan por sus fichas.

## Las fichas: el único contrato

| Ficha | Una por | Qué lleva | Quién la escribe |
|---|---|---|---|
| Ficha del cierre | Entidad y periodo | Las tareas del checklist con responsable, fecha y evidencia; cada conciliación con sus partidas abiertas; las facturas electrónicas contra sus registros; el estado declarado del cierre | Clara; el estado, el contralor persona |
| Ficha del presupuesto | Área o centro de costo y año | Aprobado, ejecutado y comprometido por cuenta; la proyección del área; los traslados con su acta; el estado declarado | Tomás; el estado, el responsable del área |

Cada dato cita el documento del que sale y su fecha. Declarado y evidenciado van en campos
separados. «No encontrado» es una respuesta válida.

## Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| Balance de comprobación y libro mayor | Exportación del ERP en Excel o CSV | Los dos |
| Auxiliares de bancos y extractos bancarios | Excel, CSV o PDF con texto | Clara |
| Facturas electrónicas emitidas y recibidas, Colombia | XML de la DIAN (UBL 2.1, CUFE), según el anexo técnico vigente | Clara |
| Comprobantes electrónicos, Ecuador | XML del SRI, esquema offline, clave de acceso de 49 dígitos | Clara |
| Checklist de cierre | Excel o Markdown, con responsable y fecha | Clara |
| Requerimientos del auditor y sus respuestas | Word, PDF, correo | Clara |
| Presupuesto aprobado y sus versiones | Excel | Tomás |
| Órdenes de compra y compromisos | Exportación del ERP | Tomás |
| Proyecciones de cada área | Excel | Tomás |
| Actas del comité de presupuesto y de traslados | Word, PDF | Tomás |
| Fichas de proyectos de la familia PMO | `ficha-pm.json` y fichas de Vera | Tomás, solo lectura |

Los formatos de la DIAN (F-01) y del SRI (F-04) se leen desde su fuente técnica oficial y se
verifican campo por campo antes de escribir el lector ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 2).

## Las señales: lo que calcula el código

**Clara · contralor**

| Señal | Se levanta cuando |
|---|---|
| `close_task_overdue` | Una tarea del checklist pasó su fecha y no tiene evidencia |
| `close_task_done_without_evidence` | Una tarea figura cumplida y ningún documento la sostiene |
| `trial_balance_unbalanced` | Los débitos y los créditos del balance de comprobación no suman lo mismo |
| `ledger_vs_trial_balance` | El saldo de una cuenta en el mayor no es el del balance de comprobación |
| `bank_unreconciled` | Hay movimientos del extracto sin su registro, o registros sin su movimiento |
| `reconciling_item_aged` | Una partida conciliatoria lleva más días de los configurados |
| `reconciliation_stale` | La conciliación de una cuenta no se actualizó en el periodo |
| `einvoice_not_recorded` | Una factura electrónica emitida o recibida no tiene registro contable |
| `recorded_without_einvoice` | Un registro que la necesita no tiene factura electrónica que lo soporte |
| `einvoice_amount_mismatch` | El valor o el impuesto del XML no es el del registro |
| `einvoice_duplicate` | El mismo CUFE o la misma clave de acceso aparece registrado dos veces |
| `audit_request_unanswered` | Un requerimiento del auditor no tiene respuesta con soporte |
| `declared_close_vs_evidence` | El cierre se reporta como cerrado y hay señales abiertas que ese estado no explica |

**Tomás · FP&A**

| Señal | Se levanta cuando |
|---|---|
| `variance_over_threshold` | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado |
| `committed_near_approved` | Ejecutado más comprometido se acerca a lo aprobado sin holgura |
| `forecast_over_approved` | La proyección al cierre del año supera lo aprobado |
| `forecast_stale` | La proyección del área no se actualizó en los días configurados |
| `transfer_without_approval` | Un traslado o una modificación no tiene el acta que lo aprueba |
| `budget_version_mismatch` | El informe usa una versión del presupuesto distinta de la aprobada |
| `spend_without_budget_line` | Hay gasto en una cuenta o centro de costo sin línea presupuestal |
| `declared_vs_evidence` | El área se reporta dentro del presupuesto y los números no lo sostienen |
| `project_budget_mismatch` | El presupuesto de un proyecto en su ficha no es el que tiene asignado el área |

Los umbrales son configuración de cada organización, con un valor por defecto declarado; ninguno
es una norma.

## Las tres clases, como en la familia PMO

**A · Lo que hace, y hoy consume tiempo de alguien:** armar la ficha del cierre, conciliar
extractos contra auxiliares, cruzar cada factura electrónica con su registro, consolidar la
ejecución contra el presupuesto, preparar el informe y el material del comité.

**B · Lo que hace, y hoy no se hace:** cruzar todas las facturas electrónicas del periodo contra la
contabilidad, no una muestra; revisar todas las tareas del cierre contra su evidencia; comparar la
versión del presupuesto que usa cada informe con la aprobada; cruzar el presupuesto de cada
proyecto con el del área.

**C · Lo que no hace:** no registra asientos ni los corrige; no presenta declaraciones ni reportes a
supervisores; no opina sobre deducibilidad, tarifas ni tratamientos NIIF en la primera versión, y
no dice de memoria una tarifa, un plazo ni el valor de una unidad tributaria; no firma; no declara
el estado del cierre ni del presupuesto.

## Comandos propuestos

| Clara · `criterio-finance` | Qué produce |
|---|---|
| `finance-setup` | Mira las carpetas, hace pocas preguntas (entidad, país, periodo, ERP) y arma la primera ficha del cierre |
| `close-scan` | Procesa los documentos del periodo y actualiza la ficha con su cita |
| `close-status` | El estado del cierre contra el checklist, separando lo declarado de lo que sostienen los soportes |
| `bank-reconcile` | La conciliación de cada cuenta bancaria, con partidas abiertas y su antigüedad |
| `ledger-check` | El cuadre del balance de comprobación y del mayor |
| `einvoice-check` | Cada factura electrónica contra su registro, y cada registro contra su factura |
| `audit-pack` | El paquete para el auditor: requerimientos, respuestas y soportes, con lo que falta |
| `finance-wake` | Lo que toca hoy según la cadencia del cierre; si no toca nada, se calla |

| Tomás · `criterio-budget` | Qué produce |
|---|---|
| `fpa-setup` | Mira las carpetas, hace pocas preguntas (año, áreas, versión aprobada) y arma la primera ficha del presupuesto |
| `budget-scan` | Procesa presupuesto, ejecución, compromisos y actas, y actualiza cada ficha |
| `variance-report` | Aprobado, ejecutado, comprometido y desviación por área y cuenta |
| `forecast` | La proyección al cierre del año, con su supuesto declarado |
| `transfer-log` | Cada traslado con su acta, y los que no la tienen |
| `budget-committee-pack` | El material del comité de presupuesto como paquete de decisiones |
| `fpa-wake` | Lo que toca hoy según la cadencia del presupuesto; si no toca nada, se calla |

## Lo que se reusa de la familia PMO

- `texto.py` para Word, Excel, PowerPoint, PDF y correo, sincronizado como hoy entre plugins.
- La forma de la ficha: cita por dato, declarado contra evidenciado, «no encontrado» válido.
- Los términos por versión con su comprobante, el registro de versiones y las puertas de
  `scripts/verificar.py`.
- Rostrum, más adelante, para publicar el informe del cierre y del presupuesto.

Lo nuevo es un motor determinista propio (`finanzas.py`, librería estándar), con el XML de
facturas leído con `xml.etree`.

## Cómo se prueba, cuando se pruebe

Igual que la familia PMO: material sintético por industria con una clave que los agentes no ven,
una entidad de control que no debe levantar ninguna señal, y facturas electrónicas generadas con
la estructura oficial. Cada material de prueba deja escrito en su clave qué fuente y qué versión
usó para generarse (por ejemplo, F-01 anexo 1.9), así que una prueba se puede repetir contra la
misma versión y se sabe cuáles hay que regenerar cuando la fuente cambia. Nada se declara probado
sin una ronda completa.

## Cifras de terceros

Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md):
F-10 (Ventana Research / ISG) y F-11 (KPMG). Las de APQC (F-12) y Gartner (F-13), que hoy están en el
README de `criterio-finance`, quedan por verificar antes de publicarse en otro lugar.

## Decisiones cerradas

- Los nombres de los agentes: Clara (contralora) y Tomás (FP&A). José, 2026-10-20.
- Los plugins: `criterio-finance` para Clara, el que ya estaba declarado, y `criterio-budget` para
  Tomás, dentro de la familia `criterio-cfo`. José, 2026-10-20.

## Decisiones abiertas

1. Los formatos de exportación del ERP que se soportan primero: una plantilla de columnas por
   ERP, o un mapeo que `finance-setup` y `fpa-setup` preguntan.
2. Los umbrales por defecto de cada señal.
3. Si Rostrum publica los informes financieros desde la primera versión o después.
