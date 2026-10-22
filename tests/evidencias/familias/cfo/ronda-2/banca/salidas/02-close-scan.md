# /criterio-finance:close-scan 

57 archivos nuevos, 0 cambiados y 0 borrados respecto del inventario anterior; 8 señales abiertas en 2026-09. Sofía León declaró el 2026-10-05 que el cierre está «en curso».

# Qué cambió en el cierre · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: el mayor suma débitos 0,00 y créditos 0,00; el balance dice 5.000,00 y 0,00 | -5.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: saldo inicial más movimientos no da el saldo final (5.000,00) | 5.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 15 |
| 3 | Los débitos y los créditos del balance de comprobación no suman lo mismo (`trial_balance_unbalanced`) | débitos 253.437.700,00 y créditos 253.432.700,00: diferencia 5.000,00 | 5.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` |
| 4 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 5 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-1101: cheque pendiente de cobro del 2026-07-20 por -3.000.000,00 (CH-0450) | -3.000.000,00 | — | 72 | `2026-09/20-bancos/andino-1101/auxiliar-libros.csv` fila 2 |
| 6 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-1101: nota débito sin registrar del 2026-09-30 por -400.000,00 (sin referencia) | -400.000,00 | — | 0 | `2026-09/20-bancos/andino-1101/extracto.csv` fila 17 |
| 7 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura SETP99000104: IVA 1.662.500,00 en el XML y 1.663.500,00 en libros | 1.000,00 | — | — | `2026-09/30-facturacion/emitidas/fe-SETP99000104.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` fila 16 |
| 8 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-1101: cheque pendiente de cobro lleva 72 días (CH-0450) | -3.000.000,00 | — | 72 | `2026-09/20-bancos/andino-1101/auxiliar-libros.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su país y su moneda? → Banco Andino, NIT 900123456, Colombia, COP (tomado del nombre de la carpeta)
- ¿Qué marco contable aplica? → grupo 1 (propuesta por defecto; ningún documento lo declara, por confirmar)
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué cuentas cruzan las facturas? → ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408 (visto en el balance)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (hay auxiliar); bancos andino-1101 y pacifico-1102
- ¿Qué checklist se usa? → el de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre? → Sofía León (Contraloría, responsable de C-09)
- ¿Festivos del calendario? → 2026-10-12 (festivo por defecto, por confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/balance-comprobacion.csv`
- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/andino-1101/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-1101/extracto.csv`
- `2026-09/30-facturacion/emitidas/fe-SETP99000104.xml`

La sección «El resultado» salió vacía en el reporte del motor y no la rellené. Los términos ya estaban aceptados a nombre de José Francisco Ñáñez (versión 1.2, 2026-10-06). La corrida quedó registrada como `2026-10-06-close-scan-1`, con 8 hallazgos.