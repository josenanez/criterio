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
| `account_unreconciled` | El saldo de una cuenta en el mayor no es el de su auxiliar (cuentas por cobrar, por pagar, inventarios, activos fijos, intercompañías) |
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

## La estructura de carpetas

Clara procesa una carpeta por entidad y, dentro, una por periodo. Cada tipo de documento tiene su
lugar, numerado en el orden en que se trabaja el cierre. `finance-setup` crea la estructura vacía
si no existe y, en cada corrida, dice qué archivo está fuera de su lugar y dónde va; no lo mueve.

```
finanzas/
└── <entidad>/                          una por entidad (NIT o RUC en la configuración)
    ├── configuracion/                  la escribe finance-setup: país, marco, ERP, moneda, umbrales,
    │                                   quién aprueba, plan de cuentas con la naturaleza de cada cuenta
    ├── checklist/
    │   └── checklist-cierre.xlsx       el checklist vigente, en el modelo definido (abajo)
    └── <AAAA-MM>/                      un periodo
        ├── 01-contabilidad/
        │   ├── balance-comprobacion.xlsx|csv
        │   ├── libro-mayor.xlsx|csv
        │   └── auxiliares/<cuenta>.xlsx|csv
        ├── 02-bancos/
        │   └── <banco>-<últimos 4 dígitos de la cuenta>/
        │       ├── extracto.csv|xlsx|pdf
        │       └── auxiliar-libros.xlsx|csv
        ├── 03-facturacion/
        │   ├── emitidas/               XML de la DIAN (F-01) o del SRI (F-04)
        │   └── recibidas/
        ├── 04-soportes/                la evidencia de cada tarea del checklist: actas, correos,
        │                               conciliaciones firmadas; el nombre empieza con el id de la tarea
        └── 05-auditoria/
            ├── requerimientos/
            └── respuestas/
estado-finanzas/                        lo que escribe Clara: fichas, informes, índices; nunca lo edita
                                        una persona
```

Un archivo sin el formato esperado no se adivina: se reporta con lo que le falta.

## El checklist del cierre

El checklist llega de una de dos formas, y la persona elige:

1. **Lo carga la organización** en el modelo definido.
2. **Clara recomienda uno por industria** —banca, cooperativas, retail y minería, las cuatro de las
   pruebas— como borrador. Una persona lo revisa y lo aprueba antes de usarlo; hasta entonces el
   estado del cierre se calcula, pero el informe dice que el checklist no está aprobado.

El modelo es una hoja con estas columnas:

| Columna | Qué lleva | Obligatoria |
|---|---|---|
| `id` | Identificador único de la tarea, por ejemplo `C-07` | Sí |
| `tarea` | Qué se hace | Sí |
| `area` | Contabilidad, tesorería, impuestos, nómina… | Sí |
| `responsable` | Una persona, no un área | Sí |
| `dia_limite` | Día hábil del cierre en que vence (D+3) o fecha | Sí |
| `depende_de` | Ids de las tareas que tienen que estar antes | No |
| `evidencia_esperada` | Qué documento la prueba: «conciliación firmada», «acta del comité» | Sí |
| `criticidad` | Alta, media o baja | Sí |

## El formato común de los reportes

Todo reporte de Clara sale en Markdown, y Rostrum lo publica, con la misma estructura y en este
orden, de lo más importante a lo menos:

1. **Encabezado:** entidad, periodo, fecha de corte, versión del agente.
2. **Lo que hay que atender:** las señales abiertas ordenadas por importancia (criticidad, monto y
   antigüedad), cada una con su responsable y su cita.
3. **El resultado:** la tabla propia de cada comando.
4. **Lo que no se pudo procesar:** cada archivo con el motivo y dónde debería estar.
5. **Las preguntas que hizo** y la respuesta que tomó.
6. **Fuentes:** cada documento citado, con su ruta y su fecha, y las fuentes normativas o técnicas
   por su identificador de [`FUENTES.es.md`](FUENTES.es.md).

## Los comandos de Clara, en orden de importancia

`finance-setup` va primero porque los demás lo necesitan: crea la estructura de carpetas, hace
las preguntas que ningún documento responde y deja la configuración.

| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `finance-setup` | La carpeta raíz. Preguntas: entidad y NIT o RUC, país, grupo NIIF, ERP, moneda, periodo, umbrales, quién aprueba, plan de cuentas | Crea las carpetas que falten; inventario de lo que hay | Configuración guardada; inventario por carpeta (qué hay, qué falta, qué está fuera de lugar); checklist cargado o recomendado; la primera ficha del cierre |
| 1 | `close-scan` | El periodo completo | Extrae el texto de cada documento con su huella; solo relee lo que cambió; actualiza la ficha con la cita de cada dato | Qué cambió en el periodo; qué se agregó a la ficha; las señales nuevas; lo que no se pudo leer y por qué |
| 2 | `close-status` | `checklist/checklist-cierre.xlsx`, `04-soportes/` y la ficha | Cruza cada tarea con su evidencia, su fecha y sus dependencias; calcula el avance con evidencia ponderado por criticidad | Estado declarado contra estado evidenciado; tabla de tareas ordenada por criticidad y vencimiento: cumplida con evidencia, cumplida sin evidencia, vencida, en plazo, bloqueada por otra; la ruta crítica del cierre |
| 3 | `bank-reconcile` | Cada carpeta de `02-bancos/`: extracto y auxiliar, con fecha, descripción, referencia, valor y saldo | Cruce por referencia exacta, después por valor y fecha dentro de la ventana configurada, después por valor; clasifica cada partida abierta | Por cuenta: saldo según banco, consignaciones en tránsito, cheques pendientes de cobro, notas bancarias sin registrar y saldo según libros, con la diferencia sin explicar (debe ser cero); partidas abiertas por antigüedad (0–30, 31–60, 61–90 y más de 90 días) |
| 4 | `ledger-check` | `01-contabilidad/`: balance de comprobación y libro mayor; el plan de cuentas de la configuración | Débitos contra créditos; saldo inicial más movimientos contra saldo final; mayor contra balance, cuenta por cuenta; saldos contrarios a la naturaleza que declara el plan de cuentas de la organización | El cuadre general; las diferencias por cuenta con su monto; las cuentas con saldo contrario a su naturaleza |
| 5 | `einvoice-check` | `03-facturacion/` y los registros contables de las cuentas que la configuración asocia a ventas y compras | Lee cada XML con la estructura oficial (F-01, F-04); cruza por CUFE o clave de acceso, número, NIT o RUC y valor | Facturas sin registro, registros sin factura, diferencias de valor o de impuesto, duplicados; sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona |
| 6 | `audit-pack` | `05-auditoria/` y la ficha | Cruza cada requerimiento con su respuesta y sus soportes | El índice del paquete: requerimiento, respuesta, soporte citado y estado (respondido con soporte, respondido sin soporte, sin responder, vencido); no mueve ni copia archivos |
| 7 | `finance-wake` | La configuración y la ficha | Decide qué toca según la cadencia: a diario durante la ventana del cierre, semanal fuera de ella | Lo que corrió y lo que encontró; si no toca nada, se calla |

### La conciliación contable

La conciliación de cuentas contra sus auxiliares —cuentas por cobrar, cuentas por pagar,
inventarios, activos fijos, intercompañías— es trabajo del contralor, así que es de Clara y de
este plugin, no de otro. Entra como un comando propio, **`account-reconcile`**, después de
`bank-reconcile` y con su misma lógica: el mayor contra el auxiliar de cada cuenta, las partidas
abiertas y su antigüedad. Su entrada es `01-contabilidad/auxiliares/`. La consolidación de varias
entidades queda fuera de la primera versión.

## Rostrum: el mismo, ampliado

Rostrum no se duplica: un solo servidor publica los informes de todas las familias. Hoy vive
dentro de `criterio-portfolio`, y eso obliga a instalar la familia PMO para publicar el cierre.
La propuesta es sacarlo a un plugin propio, compartido, y ampliarlo con las páginas del cierre y
del presupuesto.

Después de este diseño viene su evolución visual, con estándares internacionales de usabilidad y
accesibilidad: WCAG 2.2 nivel AA para accesibilidad y la serie ISO 9241 para el diseño centrado
en las personas.

## Los comandos de Tomás (por detallar)

| Tomás · `criterio-budget` | Qué produce |
|---|---|
| `budget-setup` | Mira las carpetas, hace pocas preguntas (año, áreas, versión aprobada) y arma la primera ficha del presupuesto |
| `budget-scan` | Procesa presupuesto, ejecución, compromisos y actas, y actualiza cada ficha |
| `variance-report` | Aprobado, ejecutado, comprometido y desviación por área y cuenta |
| `forecast` | La proyección al cierre del año, con su supuesto declarado |
| `transfer-log` | Cada traslado con su acta, y los que no la tienen |
| `budget-committee-pack` | El material del comité de presupuesto como paquete de decisiones |
| `budget-wake` | Lo que toca hoy según la cadencia del presupuesto; si no toca nada, se calla |

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
   ERP, o un mapeo que `finance-setup` y `budget-setup` preguntan.
2. Los umbrales por defecto de cada señal.
3. Sacar Rostrum de `criterio-portfolio` a un plugin propio compartido: el nombre y el momento.
4. Los checklists recomendados por industria: quién los redacta y con qué fuente.
