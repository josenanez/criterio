# /criterio-finance:close-scan 

Es la primera corrida del barrido: 65 archivos nuevos, 0 cambiados, 0 borrados y 0 fuera de su lugar. El motor encontró 9 señales; no hay corrida anterior con qué compararlas.

El correo de Sofía León del 2026-10-05 declara el cierre «en curso», y la ficha ya lo tenía. Los requerimientos R-01 a R-05 vienen en la tabla del auditor, así que no extraje nada nuevo a la ficha.

# Qué cambió en el cierre · Banco Valle de Anáhuac · periodo 2026-09

**Entidad:** Banco Valle de Anáhuac (BVA150301K21) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.11.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: el mayor suma débitos 0.00 y créditos 0.00; el balance dice 100.00 y 0.00 | -100.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: saldo inicial más movimientos no da el saldo final (100.00) | 100.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 15 |
| 3 | Los débitos y los créditos del balance de comprobación no suman lo mismo (`trial_balance_unbalanced`) | débitos 4,518,886.00 y créditos 4,518,786.00: diferencia 100.00 | 100.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` |
| 4 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 5 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida A000109 del 2026-09-28 por 92,800.00 sin registro contable | 92,800.00 | — | — | `2026-09/30-facturacion/emitidas/fe-A000109.xml` |
| 6 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-1301: cheque pendiente de cobro del 2026-06-15 por -60,000.00 (CH-0450) | -60,000.00 | — | 107 | `2026-09/20-bancos/andino-1301/auxiliar-libros.csv` fila 2 |
| 7 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-1301: nota débito sin registrar del 2026-09-30 por -8,000.00 (sin referencia) | -8,000.00 | — | 0 | `2026-09/20-bancos/andino-1301/extracto.xlsx` fila 17 |
| 8 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura A000104: IVA 12,000.00 en el XML y 12,010.00 en libros | 10.00 | — | — | `2026-09/30-facturacion/emitidas/fe-A000104.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` fila 16 |
| 9 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-1301: cheque pendiente de cobro lleva 107 días (CH-0450) | -60,000.00 | — | 107 | `2026-09/20-bancos/andino-1301/auxiliar-libros.csv` fila 2 |

## El resultado

(El motor dejó esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su identificación fiscal, país y moneda? → Banco Valle de Anáhuac, RFC BVA150301K21, México, MXN (tomado del nombre de la carpeta)
- ¿Cuál es el marco contable? → NIF (CINIF), sugerido por defecto: ningún documento lo dice; por confirmar
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado y descontable 2408 (las que sostienen facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (con auxiliar en 2026-08 y 2026-09); bancos andino-1301 y pacifico-1302
- ¿Hay checklist de la organización? → Sí, 00-referencia/checklist-cierre.csv; sin aprobación confirmada, queda como no aprobado
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-08 y C-09 en el checklist)
- ¿Hay festivos del calendario? → No encontrado; queda vacío
- ¿Dónde se guarda el estado? → estado-finanzas/BVA150301K21-banco-valle-de-anahuac
- ¿Se acepta los términos v1.2? → Sí, José Francisco Ñáñez, 2026-10-06
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta? → No: la prueba no autoriza escribir dentro de los documentos

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/balance-comprobacion.xlsx`
- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/andino-1301/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-1301/extracto.xlsx`
- `2026-09/30-facturacion/emitidas/fe-A000104.xml`
- `2026-09/30-facturacion/emitidas/fe-A000109.xml`

La corrida quedó registrada como `2026-10-06-close-scan-1`, con la salida completa guardada en `corridas/salida-close-scan.md`.