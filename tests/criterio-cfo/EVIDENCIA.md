# criterio-cfo · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: la misma semilla da los
mismos archivos, byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la
escribe el generador al sembrar cada defecto; el motor no la ve.

## Las entidades

| Carpeta del material | País | Industria | Defectos sembrados | Señales esperadas |
|---|---|---|---:|---:|
| `banca` | Colombia | banca | 12 | 16 |
| `cooperativas` | Ecuador | cooperativas | 13 | 14 |
| `retail` | Colombia | retail | 10 | 12 |
| `mineria` | Ecuador | minería | 13 | 14 |
| `control-co` | Colombia | — | 0 | 0 |
| `control-ec` | Ecuador | — | 0 | 0 |

Cada una trae el cierre de septiembre de 2026 y el presupuesto del año: balance de
comprobación, libro mayor de enero a septiembre, auxiliares de cartera y de proveedores, dos
cuentas bancarias con su extracto y su auxiliar de libros, las facturas electrónicas emitidas y
recibidas —con la estructura de la DIAN (F-01) en Colombia, dentro de su contenedor, y la del
SRI (F-04, F-09) en Ecuador, dentro de su respuesta de autorización—, el checklist del cierre
con sus soportes, el índice de requerimientos del auditor con sus respuestas, dos versiones del
presupuesto, los compromisos, las proyecciones de cada área, las actas y la ficha del proyecto
de la familia PMO que ejecuta una de las líneas. Para Áurea, además, la política de tesorería, la
matriz de firmas, el registro de la deuda y sus covenants en `00-referencia/`, y el programa de
pagos y el flujo proyectado en `60-tesoreria/`.

## Lo que se siembra, y la señal que tiene que levantar

| Defecto | Señales | Dónde |
|---|---|---|
| El balance suma más débitos que créditos en una cuenta | `trial_balance_unbalanced`, `ledger_vs_trial_balance` (saldo y mayor de la cuenta) | banca |
| Un asiento que llegó al mayor y no al balance | `ledger_vs_trial_balance` en sus dos cuentas | retail |
| Un cheque de hace más de 60 días sin cobrar | `bank_unreconciled`, `reconciling_item_aged` | banca, minería |
| Una comisión del extracto sin registrar en libros | `bank_unreconciled` | banca, minería |
| Un cobro del 30 de septiembre que el banco todavía no abona | `bank_unreconciled` | retail |
| Una cuenta bancaria sin extracto | `reconciliation_stale` | cooperativas |
| Cartera con una partida que el auxiliar no tiene | `account_unreconciled` | cooperativas |
| Proveedores sin auxiliar del periodo | `reconciliation_stale` | retail |
| IVA del registro distinto del de la factura | `einvoice_amount_mismatch` | banca |
| Una factura emitida sin registro; una recibida sin registro | `einvoice_not_recorded` | cooperativas, minería |
| Una compra registrada sin su factura | `recorded_without_einvoice` | cooperativas |
| La misma factura en dos archivos | `einvoice_duplicate` | retail |
| La misma compra registrada en dos asientos | `einvoice_duplicate`, `einvoice_amount_mismatch` | retail |
| Una tarea marcada cumplida sin su soporte | `close_task_done_without_evidence` | banca, minería |
| Una tarea vencida sin soporte | `close_task_overdue` | cooperativas, minería |
| El cierre declarado cerrado con señales abiertas | `declared_close_vs_evidence` | retail |
| Un requerimiento «respondido» sin archivo; uno vencido | `audit_request_unanswered` | cooperativas, minería |
| Una línea ejecutada 15 % por encima de lo aprobado al corte | `variance_over_threshold` | banca, minería |
| Ejecutado más comprometido por encima del 95 % del año | `committed_near_approved` | cooperativas, minería |
| Un área que se declara dentro del presupuesto y no lo está | `declared_vs_evidence` | banca |
| Un traslado entre versiones sin acta | `transfer_without_approval` en sus dos líneas | banca, minería |
| Gasto en un centro de costo sin línea presupuestal | `spend_without_budget_line` | retail |
| La proyección de un área por encima de lo aprobado | `forecast_over_approved` | retail |
| La proyección de un área con 83 días | `forecast_stale` | cooperativas |
| Una proyección hecha sobre la versión anterior | `budget_version_mismatch` | cooperativas |
| El proyecto de la PMO con otro presupuesto que el de su línea | `project_budget_mismatch` | banca |
| Una cuenta con saldo bajo el mínimo de la política | `cash_below_minimum` | banca |
| Una cuenta con saldo 30 % por debajo de su proyección | `cash_vs_forecast` | cooperativas, minería |
| Una cuenta en dólares con su posición sobre el límite | `fx_exposure_over_limit` | retail |
| Un pago de 30 veces la escala con una aprobación y la política pide dos | `payment_without_approval` | banca, minería |
| Un pago aprobado por quien no está en la matriz de firmas | `signatory_without_authority` | cooperativas |
| La razón corriente a 5 % de su límite, calculada desde el balance | `covenant_at_risk` | banca, minería |
| El crédito de tesorería que vence en 20 días | `maturity_near` | cooperativas, retail |

Las 30 señales de la familia se siembran al menos una vez. **Los controles no tienen ningún
defecto**: un traslado aprobado con su acta, partidas que cruzan por referencia y por fecha,
facturas en su contenedor, tareas con su soporte y áreas que se declaran dentro del presupuesto
y lo están. Cualquier señal ahí es una falla.

## Cómo se califica

`evaluar.py` arma la configuración que dejaría el setup, escribe en la ficha lo que el agente
tendría que extraer de los documentos escritos —está en la clave—, corre el motor y compara cada
señal por su nombre y su clave. **Una señal de más cuenta igual que una de menos.** Comprueba
además que la diferencia sin explicar de cada cuenta bancaria sea cero, que el balance cuadre
donde no se sembró el descuadre y que cada factura cruce con su registro o tenga su señal.

## Lo que no prueba

La extracción. Que el agente procese el acta de traslado, el correo que declara el cierre o la carta
del auditor y lo registre bien en la ficha lo prueba la ronda con el agente, sobre este mismo
material y contra esta misma clave.
