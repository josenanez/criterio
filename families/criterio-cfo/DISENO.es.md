# criterio-cfo · la familia de la función financiera

![Clara, Tomás y Rostrum](../../docs/img/es/robots-cfo.gif)

**Estado: construida y en prueba.** Los dieciséis comandos, los doce skills y el motor de cálculo
están construidos; el motor pasa su prueba determinista contra el material de cuatro industrias y
dos entidades de control (`tests/criterio-cfo/`), y la prueba con el agente es el paso siguiente.
Alcance en [ADR 0006](../../docs/decisions/0006-scope-cfo.md); cómo se reparte el trabajo entre el
motor y el agente, en [ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md).

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

**De dónde sale este documento.** Las tablas de agentes, carpetas, señales, comandos y cifras no se
escriben aquí: salen de tres fuentes, [`familia.json`](familia.json), [`carpetas.json`](carpetas.json)
y [`fuentes.json`](fuentes.json), que `scripts/familias.py` escribe en este diseño, en `FUENTES.es.md`,
en los README de `criterio-finance` y, con `scripts/criterio-cfo.mjs`, en el portal. Una puerta de
`scripts/verificar.py` falla si alguna copia no cuadra, si un comando cita una carpeta que no está
en la estructura o si se apoya en una fuente por verificar.

## Un agente por rol

<!-- cfo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| Contralor | **Clara** — de *clarus*: que los libros digan lo mismo que los soportes | `criterio-finance` | El cierre mensual con su checklist y su evidencia, las conciliaciones bancarias y de cuentas, la factura electrónica contra la contabilidad y el paquete para el auditor |
| FP&A | **Tomás** — «el gemelo»: pone el presupuesto al lado de su gemelo, la ejecución | `criterio-budget` | El presupuesto aprobado contra lo ejecutado y lo comprometido, la proyección al cierre del año, los traslados y el material del comité de presupuesto |
<!-- /cfo:agentes -->

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

<!-- cfo:senales · generado por scripts/familias.py; no se edita a mano -->
**Clara · Contralor**

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
<!-- /cfo:senales -->

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

Recomendada, no obligatoria, como en la familia PMO ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)):
los agentes procesan la carpeta como esté. `finance-setup` y `budget-setup` comparan lo que
encuentran con esta estructura y, en cada corrida, dicen qué archivo está fuera de su lugar y dónde
iría; no crean, mueven ni renombran nada en los documentos de la organización. La numeración va de
diez en diez, como en la familia PMO, en el orden en que se trabaja el cierre y el presupuesto.

Cada documento tiene un solo lugar. La contabilidad del periodo vive en `10-contabilidad/`: Clara
la cierra y Tomás saca de ahí la ejecución del presupuesto, sin copias entre carpetas.

<!-- cfo:carpetas · generado por scripts/familias.py; no se edita a mano -->
Una carpeta por entidad, con el NIT o el RUC al inicio del nombre: `900123456-banco-andino`. Dentro, lo que la organización entrega una vez, una carpeta por periodo contable y una por año presupuestal.

```
finanzas/
└── <entidad>/
    ├── 00-referencia/
    ├── <AAAA-MM>/
    │   ├── 10-contabilidad/
    │   ├── 20-bancos/
    │   ├── 30-facturacion/
    │   ├── 40-soportes/
    │   └── 50-auditoria/
    └── presupuesto-<AAAA>/
        ├── 10-aprobado/
        ├── 20-compromisos/
        ├── 30-proyecciones/
        └── 40-actas/
estado-finanzas/
```

**`<entidad>/`** · Lo que la organización entrega una vez

| Carpeta | Qué va | Agente |
|---|---|---|
| `00-referencia/` | El plan de cuentas con la naturaleza de cada cuenta, `checklist-cierre.xlsx` en el modelo definido y el mapeo de cuentas a centros de costo y líneas presupuestales | Clara, Tomás |

**`<AAAA-MM>/`** · Un periodo contable, numerado en el orden en que se trabaja el cierre

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-contabilidad/` | Balance de comprobación y libro mayor exportados del ERP, y `auxiliares/` con un archivo por cuenta; de aquí sale también la ejecución del presupuesto | Clara, Tomás |
| `20-bancos/` | Una carpeta por cuenta, `<banco>-<últimos 4 dígitos>`, con el extracto y el auxiliar de libros | Clara |
| `30-facturacion/` | `emitidas/` y `recibidas/`, con el XML de la DIAN (F-01) o del SRI (F-04) | Clara |
| `40-soportes/` | La evidencia de cada tarea del checklist —actas, correos, conciliaciones firmadas—, con el id de la tarea al inicio del nombre | Clara |
| `50-auditoria/` | `requerimientos/` y `respuestas/` del auditor | Clara |

**`presupuesto-<AAAA>/`** · Un año presupuestal

| Carpeta | Qué va | Agente |
|---|---|---|
| `10-aprobado/` | El presupuesto aprobado y cada versión, con su fecha en el nombre | Tomás |
| `20-compromisos/` | Órdenes de compra y compromisos exportados del ERP, con la fecha de corte en el nombre | Tomás |
| `30-proyecciones/` | La proyección de cada área, una por área y fecha | Tomás |
| `40-actas/` | Actas del comité de presupuesto, de aprobación y de traslados | Tomás |

**`estado-finanzas/`** · Lo que escriben Clara y Tomás: la configuración, las fichas, los informes y los índices. Ninguna persona lo edita, y ningún agente escribe fuera de aquí.
<!-- /cfo:carpetas -->

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

Todo reporte de Clara y de Tomás sale en Markdown, y Rostrum lo publica, con la misma estructura y en este
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

`finance-setup` va primero porque los demás lo necesitan: compara la carpeta con la estructura
recomendada, hace las preguntas que ningún documento responde y deja la configuración.

<!-- cfo:comandos-clara · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `finance-setup` | La carpeta raíz. Preguntas: entidad y NIT o RUC, país, grupo NIIF (F-05, F-06), ERP, moneda, periodo, umbrales, quién aprueba, plan de cuentas | Inventario de lo que hay; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta (qué hay, qué falta, qué está fuera de su lugar y dónde iría); checklist cargado o recomendado; la primera ficha del cierre |
| 1 | `close-scan` | El periodo completo | Extrae el texto de cada documento con su huella; solo reprocesa lo que cambió; actualiza la ficha con la cita de cada dato | Qué cambió en el periodo; qué se agregó a la ficha; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `close-status` | `00-referencia/checklist-cierre.xlsx`, `40-soportes/` y la ficha | Cruza cada tarea con su evidencia, su fecha y sus dependencias; calcula el avance con evidencia ponderado por criticidad | Estado declarado contra estado evidenciado; tabla de tareas ordenada por criticidad y vencimiento: cumplida con evidencia, cumplida sin evidencia, vencida, en plazo, bloqueada por otra; la ruta crítica del cierre |
| 3 | `bank-reconcile` | Cada carpeta de `20-bancos/`: extracto y auxiliar, con fecha, descripción, referencia, valor y saldo | Cruce por referencia exacta, después por valor y fecha dentro de la ventana configurada, después por valor; clasifica cada partida abierta | Por cuenta: saldo según banco, consignaciones en tránsito, cheques pendientes de cobro, notas bancarias sin registrar y saldo según libros, con la diferencia sin explicar (debe ser cero); partidas abiertas por antigüedad (0–30, 31–60, 61–90 y más de 90 días) |
| 4 | `account-reconcile` | `10-contabilidad/`: el mayor y `auxiliares/` de cuentas por cobrar, cuentas por pagar, inventarios, activos fijos e intercompañías | La lógica de `bank-reconcile`: el saldo del mayor contra el del auxiliar de cada cuenta, y las partidas abiertas con su antigüedad | Por cuenta: saldo según mayor, saldo según auxiliar, la diferencia y las partidas que la explican por antigüedad; las cuentas cuya conciliación no se actualizó en el periodo |
| 5 | `ledger-check` | `10-contabilidad/`: balance de comprobación y libro mayor; el plan de cuentas de `00-referencia/` | Débitos contra créditos; saldo inicial más movimientos contra saldo final; mayor contra balance, cuenta por cuenta; saldos contrarios a la naturaleza que declara el plan de cuentas de la organización | El cuadre general; las diferencias por cuenta con su monto; las cuentas con saldo contrario a su naturaleza |
| 6 | `einvoice-check` | `30-facturacion/` y los registros contables de las cuentas que la configuración asocia a ventas y compras | Procesa cada XML con la estructura oficial (F-01, F-04); cruza por CUFE o clave de acceso, número, NIT o RUC y valor | Facturas sin registro, registros sin factura, diferencias de valor o de impuesto, duplicados; sin opinión fiscal: lo que es criterio tributario queda como pregunta para la persona |
| 7 | `audit-pack` | `50-auditoria/` y la ficha | Cruza cada requerimiento con su respuesta y sus soportes | El índice del paquete: requerimiento, respuesta, soporte citado y estado (respondido con soporte, respondido sin soporte, sin responder, vencido); no mueve ni copia archivos |
| 8 | `finance-wake` | La configuración y la ficha | Decide qué toca según la cadencia: a diario durante la ventana del cierre, semanal fuera de ella | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /cfo:comandos-clara -->

### La conciliación contable

La conciliación de cuentas contra sus auxiliares —cuentas por cobrar, cuentas por pagar,
inventarios, activos fijos, intercompañías— es trabajo del contralor, así que es de Clara y de
este plugin, no de otro: es `account-reconcile`, con la lógica de `bank-reconcile`. La
consolidación de varias entidades queda fuera de la primera versión.

## Rostrum: el mismo, ampliado

Rostrum no se duplica: un solo servidor publica los informes de todas las familias. Desde la
0.7.0 es su propio plugin, `criterio-server`, y sirve las páginas del cierre y del presupuesto con
las de las otras familias, desde un mapa que arma por selección de carpeta
([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

Después de este diseño viene su evolución visual, con estándares internacionales de usabilidad y
accesibilidad: WCAG 2.2 nivel AA para accesibilidad y la serie ISO 9241 para el diseño centrado
en las personas.

## Los comandos de Tomás, en orden de importancia

`budget-setup` va primero por la misma razón que `finance-setup`. Tomás no recalcula la
contabilidad: toma la ejecución de `10-contabilidad/`, la lleva a cada línea con el mapeo de la
organización y la pone al lado del presupuesto aprobado. La proyección siempre sale con su
supuesto escrito, y la decisión del comité la toma una persona.

<!-- cfo:comandos-tomas · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `budget-setup` | La carpeta raíz. Preguntas: entidad, año presupuestal, áreas o centros de costo con su responsable, la versión aprobada y su acta, el mapeo de cuentas a líneas presupuestales (en `00-referencia/`), los umbrales de desviación y, si la organización usa la familia PMO, dónde están sus fichas | Inventario de `10-aprobado/` a `40-actas/` y de los periodos con `10-contabilidad/`; identifica la versión aprobada por su acta; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta (qué hay, qué falta, qué está fuera de su lugar y dónde iría); la versión aprobada que tomó y el acta que la sostiene; la primera ficha de cada área |
| 1 | `budget-scan` | `presupuesto-<AAAA>/` completo y `10-contabilidad/` de cada periodo del año | Extrae cada documento con su huella; solo reprocesa lo que cambió; lleva lo ejecutado y lo comprometido a su línea con el mapeo de `00-referencia/`; actualiza cada ficha con la cita de cada dato | Qué cambió; qué se agregó a cada ficha; las señales nuevas; lo que no se pudo procesar y por qué, incluido el gasto que no tiene línea en el mapeo |
| 2 | `variance-report` | Las fichas al corte y la versión aprobada vigente; si la organización usa la familia PMO, el presupuesto de cada proyecto en su ficha | Por área, línea y cuenta: aprobado, ejecutado, comprometido y disponible (aprobado menos ejecutado menos comprometido); la desviación del ejecutado contra el aprobado acumulado al corte, con su distribución mensual si existe, y si no existe lo dice; el presupuesto de cada proyecto contra el asignado al área | La tabla por área ordenada por desviación; las líneas sobre el umbral; el gasto sin línea presupuestal; los proyectos cuyo presupuesto no cuadra con el del área; estado declarado por el área contra estado evidenciado |
| 3 | `forecast` | La ejecución al corte, `20-compromisos/` y la proyección de cada área en `30-proyecciones/` | Dos proyecciones calculadas, cada una con su supuesto escrito: al ritmo (el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido) y al plan (el ejecutado más lo que falta del aprobado según su distribución mensual); las compara con la proyección que entregó el área | Por área: aprobado, la proyección del área y las dos calculadas, con la diferencia de cada una; las áreas cuya proyección supera lo aprobado; las proyecciones que no se actualizaron en los días configurados |
| 4 | `transfer-log` | Las versiones de `10-aprobado/` y las actas de `40-actas/` | Compara cada versión con la anterior, línea por línea: cada cambio de valor es un traslado, una adición o una reducción; lo cruza con el acta que lo aprueba por fecha, valor y líneas de origen y destino | El registro: fecha, origen, destino, valor, acta y estado (con acta, sin acta, acta sin cambio aplicado); los traslados dejan igual el total, y las adiciones y reducciones se muestran aparte |
| 5 | `budget-committee-pack` | Las fichas, `variance-report`, `forecast` y `transfer-log` del corte, y el acta del comité anterior en `40-actas/` | Arma los puntos de decisión: líneas sobre el umbral, proyecciones sobre lo aprobado, traslados sin acta y los compromisos del comité anterior con su evidencia | El paquete en el formato común: cada decisión con su cifra, su cita y quién la toma; los compromisos del acta anterior con su estado; no recomienda la decisión |
| 6 | `budget-wake` | La configuración y las fichas | Decide qué toca según la cadencia: cuando aparece un periodo nuevo en `10-contabilidad/`, antes de cada comité y una vez por semana para los compromisos | Lo que corrió y lo que encontró; si no toca nada, se calla |
<!-- /cfo:comandos-tomas -->

## Lo que se reusa de la familia PMO

- `texto.py` para Word, Excel, PowerPoint, PDF y correo, y `terminos.py` para la aceptación de
  los términos, copiados como hoy entre plugins por `scripts/sincronizar.py`.
- La forma de la ficha: cita por dato, declarado contra evidenciado, «no encontrado» válido.
- Los términos por versión con su comprobante, el registro de versiones y las puertas de
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, para publicar los reportes del cierre y del presupuesto (ADR 0010).

Lo nuevo es el motor propio, `finanzas.py`, con librería estándar: procesa las tablas y las
facturas directamente, y el agente extrae a la ficha solo lo que trae un documento escrito
([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)). Vive en `criterio-finance`
y se copia a `criterio-budget`.

## Cómo se prueba

Igual que la familia PMO: material sintético por industria con una clave que los agentes no ven
y entidades de control que no deben levantar ninguna señal. Está en `tests/criterio-cfo/`:
cuatro industrias —banca y retail en Colombia, cooperativas y minería en Ecuador— y un control
por país, con las facturas generadas con la estructura oficial de cada una. Cada señal de la
familia se siembra al menos una vez; qué se siembra y dónde, en
[`tests/criterio-cfo/EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md).

`tests/criterio-cfo/evaluar.py` corre el motor con la extracción correcta y compara cada señal
por su nombre y su clave: una de más cuenta igual que una de menos. La extracción del agente se
prueba en la ronda, sobre el mismo material. La familia se declara probada con una ronda completa.

## Cifras de terceros

<!-- cfo:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (Ventana Research / ISG), C-02 (KPMG), C-03 (APQC), C-04 (Gartner).
<!-- /cfo:cifras -->

## Decisiones cerradas

- Los nombres de los agentes: Clara (contralora) y Tomás (FP&A). José, 2026-10-20.
- Los plugins: `criterio-finance` para Clara, el que ya estaba declarado, y `criterio-budget` para
  Tomás, dentro de la familia `criterio-cfo`. José, 2026-10-20.

## Decisiones de la construcción

Tomadas al construir, con su razón; cada una se puede revertir con una decisión nueva.

- **Las columnas de las exportaciones** se reconocen por su nombre y sus variantes; la que no se
  reconoce se pregunta y queda en `columns` de la configuración. No hay una plantilla por ERP.
- **Los umbrales por defecto** están en `config.example.json` de cada plugin y el setup los
  propone como configuración, no como norma. En Colombia, la tolerancia de los valores es la
  holgura que el anexo de la DIAN permite: ±2,00 y ±5,00 en el IVA (F-01, 5.2.1).
- **La versión vigente del presupuesto** es la más reciente, salvo que la configuración fije
  otra; que cada cambio tenga su acta lo revisa `transfer-log`.
- **El checklist recomendado por industria** es un borrador del plugin, sin fuente normativa,
  y el reporte dice que no está aprobado hasta que una persona lo apruebe.
- **La estructura de carpetas** se sugiere y nunca se crea dentro de los documentos de la
  organización ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)).

## Decisiones abiertas

1. ~~Sacar Rostrum de `criterio-portfolio` a un plugin propio compartido: el nombre y el momento.~~
   Cerrada en el [ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md): `criterio-server`, en la 0.7.0.
2. Quién revisa el checklist recomendado de cada industria antes de proponerlo como algo más que
   un borrador.
