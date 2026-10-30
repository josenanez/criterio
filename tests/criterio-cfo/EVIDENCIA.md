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
| `banca-pe` | Perú | banca | 11 | 12 |
| `mineria-pe` | Perú | minería | 11 | 12 |
| `control-pe` | Perú | — | 0 | 0 |
| `retail-cl` | Chile | retail | 11 | 14 |
| `mineria-cl` | Chile | minería | 11 | 12 |
| `control-cl` | Chile | — | 0 | 0 |
| `banca-mx` | México | banca | 12 | 16 |
| `retail-mx` | México | retail | 11 | 11 |
| `control-mx` | México | — | 0 | 0 |
| `retail-br` | Brasil | retail | 11 | 12 |
| `mineria-br` | Brasil | minería | 11 | 12 |
| `control-br` | Brasil | — | 0 | 0 |
| `retail-ar` | Argentina | retail | 11 | 12 |
| `mineria-ar` | Argentina | minería | 11 | 12 |
| `control-ar` | Argentina | — | 0 | 0 |
| `banca-pa` | Panamá | banca | 12 | 16 |
| `retail-pa` | Panamá | retail | 11 | 11 |
| `control-pa` | Panamá | — | 0 | 0 |
| `retail-gt` | Guatemala | retail | 11 | 12 |
| `mineria-gt` | Guatemala | minería | 11 | 12 |
| `control-gt` | Guatemala | — | 0 | 0 |

Cada una trae el cierre de septiembre de 2026 y el presupuesto del año: balance de
comprobación, libro mayor de enero a septiembre, auxiliares de cartera y de proveedores, dos
cuentas bancarias con su extracto —que dice su moneda— y su auxiliar de libros, las facturas electrónicas emitidas y
recibidas —con la estructura de la DIAN (F-01) en Colombia, dentro de su contenedor, y la del
SRI (F-04, F-09) en Ecuador, dentro de su respuesta de autorización, la UBL 2.1 de la SUNAT
(F-13) en Perú, el DTE del SII (F-16) en Chile, el CFDI 4.0 del SAT (F-19) en México y la NF-e (F-21) en Brasil,
con el ICMS dentro del valor de la nota y la alícuota de São Paulo (F-22)—, el checklist del cierre
con sus soportes, el índice de requerimientos del auditor con sus respuestas, dos versiones del
presupuesto, los compromisos, las proyecciones de cada área, las actas y la ficha del proyecto
de la familia PMO que ejecuta una de las líneas. Para Áurea, además, la política de tesorería, la
matriz de firmas, el registro de la deuda y sus covenants en `00-referencia/`, y el programa de
pagos y el flujo proyectado en `60-tesoreria/`.

Los formatos son los de un área financiera real: parte de las tablas en Excel, con números y
fechas de verdad; parte de las actas, los soportes y las respuestas al auditor en Word y PDF; y
algunos extractos en PDF con texto, como los entrega el banco, que el motor procesa por columnas.

**Brasil, en portugués.** Las tres entidades de Brasil traen sus documentos como los tiene una
empresa de allá: las cabeceras de las tablas (`data`, `conta`, `histórico`, `débito`, `crédito`),
los nombres de los archivos (`livro-razao`, `balancete`, `extrato`, `orcamento-2026`), las cuentas,
las áreas y las líneas del orçamento, las atas, los e-mails, la carta del auditor y las personas.
La estructura de carpetas es la de la plataforma. Los bancos de Brasil facturan sus servicios con la
nota fiscal de servicios de su municipio, no con la NF-e: por eso Brasil entra con retail y minería.

**Argentina, con el comprobante de ARCA.** Las tres entidades de Argentina traen sus comprobantes
electrónicos como los archiva un ERP: la solicitud `FECAESolicitar` y su respuesta con el CAE, en un
solo archivo, con el CUIT de cada parte, el IVA al 21 % y los importes de ARCA (F-24, F-25). El
lector los identifica por su CAE. Solo una factura aprobada cruza valores; una nota de crédito o un
comprobante rechazado se identifican y no cruzan. El marco contable de cada una sale de su perfil
NIIF (F-26).

**Panamá, con la factura electrónica de la DGI.** Las tres entidades de Panamá traen la factura
electrónica de la Ficha Técnica 1.00 (F-27): `rFE` con el CUFE, el tipo y el número del documento
fiscal, el RUC de cada parte y los totales, con el ITBMS al 7 % (F-28). Sus montos van en dólares, así
que el material no les siembra exposición cambiaria. La tolerancia del país es la de la ficha: una
diferencia menor que B/0.50 no es error.

**Guatemala, con la factura electrónica en línea de la SAT.** Las tres entidades de Guatemala traen
el DTE certificado de la versión 0.2.1 del esquema (F-30): `GTDocumento` con el número de
autorización que asigna el certificador, la serie y el número, el NIT de cada parte y los totales,
con el IVA al 12 % (F-32) y las reglas de validación de la SAT (F-31). El lector identifica cada
factura por su número de autorización. El marco contable de cada una sale de su perfil NIIF (F-33).

## Lo que se siembra, y la señal que tiene que levantar

La columna «Dónde» nombra las entidades de Colombia, Ecuador y Perú. Las de Chile y México siembran los mismos casos con su propio lector de factura; la lista exacta de cada una está en su clave, `material/<entidad>/clave.json`, en `siembra` y `esperado`.

| Defecto | Señales | Dónde |
|---|---|---|
| El balance suma más débitos que créditos en una cuenta | `trial_balance_unbalanced`, `ledger_vs_trial_balance` (saldo y mayor de la cuenta) | banca |
| Un asiento que llegó al mayor y no al balance | `ledger_vs_trial_balance` en sus dos cuentas | retail |
| Un cheque de hace más de 60 días sin cobrar | `bank_unreconciled`, `reconciling_item_aged` | banca, minería, minería de Perú |
| Una comisión del extracto sin registrar en libros | `bank_unreconciled` | banca, minería |
| Un cobro del 30 de septiembre que el banco todavía no abona | `bank_unreconciled` | retail, banca de Perú |
| Una cuenta bancaria sin extracto | `reconciliation_stale` | cooperativas |
| Cartera con una partida que el auxiliar no tiene | `account_unreconciled` | cooperativas |
| Proveedores sin auxiliar del periodo | `reconciliation_stale` | retail |
| IVA o IGV del registro distinto del de la factura | `einvoice_amount_mismatch` | banca, banca de Perú |
| Una factura emitida sin registro; una recibida sin registro | `einvoice_not_recorded` | cooperativas, minería, minería de Perú |
| Una compra registrada sin su factura | `recorded_without_einvoice` | cooperativas, minería de Perú |
| La misma factura en dos archivos | `einvoice_duplicate` | retail, banca de Perú |
| La misma compra registrada en dos asientos | `einvoice_duplicate`, `einvoice_amount_mismatch` | retail |
| Una tarea marcada cumplida sin su soporte | `close_task_done_without_evidence` | banca, minería, banca de Perú |
| Una tarea vencida sin soporte | `close_task_overdue` | cooperativas, minería |
| El cierre declarado cerrado con señales abiertas | `declared_close_vs_evidence` | retail, banca de Perú |
| Un requerimiento «respondido» sin archivo; uno vencido | `audit_request_unanswered` | cooperativas, minería, minería de Perú |
| Una línea ejecutada 15 % por encima de lo aprobado al corte | `variance_over_threshold` | banca, minería, banca de Perú |
| Ejecutado más comprometido por encima del 95 % del año | `committed_near_approved` | cooperativas, minería, minería de Perú |
| Un área que se declara dentro del presupuesto y no lo está | `declared_vs_evidence` | banca, banca de Perú |
| Un traslado entre versiones sin acta | `transfer_without_approval` en sus dos líneas | banca, minería, banca de Perú |
| Gasto en un centro de costo sin línea presupuestal | `spend_without_budget_line` | retail |
| La proyección de un área por encima de lo aprobado | `forecast_over_approved` | retail |
| La proyección de un área con 83 días | `forecast_stale` | cooperativas, minería de Perú |
| Una proyección hecha sobre la versión anterior | `budget_version_mismatch` | cooperativas, minería de Perú |
| El proyecto de la PMO con otro presupuesto que el de su línea | `project_budget_mismatch` | banca |
| Una cuenta con saldo bajo el mínimo de la política | `cash_below_minimum` | banca, minería de Perú |
| Una cuenta con saldo 30 % por debajo de su proyección | `cash_vs_forecast` | cooperativas, minería, minería de Perú |
| Una cuenta en dólares, dicha en su extracto, con su posición sobre el límite | `fx_exposure_over_limit` | retail, banca de Perú |
| Un pago de 30 veces la escala con una aprobación y la política pide dos | `payment_without_approval` | banca, minería |
| Un pago aprobado por quien no está en la matriz de firmas | `signatory_without_authority` | cooperativas, banca de Perú |
| La razón corriente a 5 % de su límite, calculada desde el balance | `covenant_at_risk` | banca, minería, minería de Perú |
| El crédito de tesorería que vence en 20 días | `maturity_near` | cooperativas, retail, banca de Perú |

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

- **La NF-e completa.** El lector procesa la identificación, las partes y los totales del Anexo I
  del MOC 7.0 (F-21). El protocolo de autorización de la SEFAZ y el dígito verificador de la chave
  no se validan en esta versión: su regla está en el MOC, Visión General, que no se consultó. Los
  campos del IBS y la CBS de la reforma tributaria no se procesan: en esta versión no son
  obligatorios en producción.
- **La nota fiscal de servicios.** La de cada municipio de Brasil no se procesa todavía.

La extracción. Que el agente procese el acta de traslado, el correo que declara el cierre o la carta
del auditor y lo registre bien en la ficha lo prueba la ronda con el agente, sobre este mismo
material y contra esta misma clave.
