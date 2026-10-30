# /criterio-finance:close-scan 

Primera corrida del barrido: 65 archivos nuevos, 0 cambiados y 0 borrados, y 9 señales. Todas son nuevas porque no había un close-scan anterior. Los documentos escritos se convirtieron sin fallos. La ficha ya traía el estado declarado ("en curso", correo de Sofía León del 2026-10-05). El índice del auditor es una tabla y lo procesa el motor. Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-06, así que no hizo falta registrar nada.

# Qué cambió en el cierre · Banco Istmeño · periodo 2026-09

**Entidad:** Banco Istmeño (155731001-2-2016) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: el mayor suma débitos 0.00 y créditos 0.00; el balance dice 10.00 y 0.00 | -10.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 15 · `2026-09/10-contabilidad/libro-mayor.xlsx` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: saldo inicial más movimientos no da el saldo final (10.00) | 10.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 15 |
| 3 | Los débitos y los créditos del balance de comprobación no suman lo mismo (`trial_balance_unbalanced`) | débitos 409,355.20 y créditos 409,345.20: diferencia 10.00 | 10.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` |
| 4 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 5 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 001-0000000109 del 2026-09-28 por 6,955.00 sin registro contable | 6,955.00 | — | — | `2026-09/30-facturacion/emitidas/fe-001-0000000109.xml` |
| 6 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-7301: cheque pendiente de cobro del 2026-06-15 por -6,000.00 (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-7301/auxiliar-libros.xlsx` fila 2 |
| 7 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-7301: nota débito sin registrar del 2026-09-30 por -800.00 (sin referencia) | -800.00 | — | 0 | `2026-09/20-bancos/andino-7301/extracto.pdf` fila 17 |
| 8 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura 001-0000000104: ITBMS 770.00 en el XML y 780.00 en libros | 10.00 | — | — | `2026-09/30-facturacion/emitidas/fe-001-0000000104.xml` · `2026-09/10-contabilidad/libro-mayor.xlsx` fila 15 · `2026-09/10-contabilidad/libro-mayor.xlsx` fila 16 |
| 9 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-7301: cheque pendiente de cobro lleva 107 días (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-7301/auxiliar-libros.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz? → finanzas/155731001-2-2016-banco-istmeno (la del argumento)
- ¿Entidad, identificación, país y moneda? → Banco Istmeño · RUC 155731001-2-2016 · PA · USD (del nombre de la carpeta y el registro de países; el nombre es una propuesta)
- ¿Marco contable? → NIIF (propuesta; ningún documento lo confirma)
- ¿Periodo que se cierra? → 2026-09 (el último con 10-contabilidad/)
- ¿Cuentas que cruzan las facturas? → ventas 4135; compras 5135, 5145, 5195; ITBMS generado y descontable 2408 (las que sostienen las facturas)
- ¿Cuentas que se concilian contra auxiliar y cuentas bancarias? → 1305 y 2205 (con auxiliar en 2026-08 y 2026-09); bancos andino-7301 y pacifico-7302
- ¿Checklist? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada, queda como no aprobado
- ¿Quién aprueba el cierre y festivos? → Sofía León (responsable de C-08 y C-09 del checklist); festivos: no encontrados
- ¿Dónde se guarda el estado? → estado-finanzas/155731001-2-2016-banco-istmeno
- ¿Términos? → Aceptados por José Francisco Ñáñez, 2026-10-06 (dado en las instrucciones de la prueba)

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/balance-comprobacion.xlsx`
- `2026-09/10-contabilidad/libro-mayor.xlsx`
- `2026-09/20-bancos/andino-7301/auxiliar-libros.xlsx`
- `2026-09/20-bancos/andino-7301/extracto.pdf`
- `2026-09/30-facturacion/emitidas/fe-001-0000000104.xml`
- `2026-09/30-facturacion/emitidas/fe-001-0000000109.xml`

La corrida quedó registrada como `2026-10-06-close-scan-1` con 9 hallazgos. El motor dejó vacía la sección "El resultado" del reporte y la mostré tal cual.