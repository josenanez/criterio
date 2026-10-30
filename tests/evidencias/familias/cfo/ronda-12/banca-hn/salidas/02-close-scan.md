# /criterio-finance:close-scan 

Primer barrido: 66 archivos nuevos, 0 cambiados y 0 borrados. Hay 7 señales, todas nuevas porque no había una corrida anterior con la que comparar.

Los términos ya estaban vigentes, así que no hubo que volver a mostrarlos. En el inventario no hay archivos fuera de lugar ni ilegibles. Convertí los soportes, los documentos de auditoría y las 17 facturas hondureñas. La ficha ya traía el estado declarado, R-09 y las facturas con su CAI, y coincide con los textos convertidos, así que no la modifiqué.

# Qué cambió en el cierre · Banco de Occidente Sintético · periodo 2026-09

**Entidad:** Banco de Occidente Sintético (08010004578120) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.1.0 · **Aprueba:** Contralor · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: el mayor suma débitos 0.00 y créditos 0.00; el balance dice 250.00 y 0.00 | -250.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 15 · `2026-09/10-contabilidad/libro-mayor.xlsx` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: saldo inicial más movimientos no da el saldo final (250.00) | 250.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 15 |
| 3 | Los débitos y los créditos del balance de comprobación no suman lo mismo (`trial_balance_unbalanced`) | débitos 11,608,110.00 y créditos 11,607,860.00: diferencia 250.00 | 250.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` |
| 4 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.xlsx` fila 3 |
| 5 | Una factura recibida de Honduras cae fuera de su rango autorizado o se emitió después de su fecha límite: no sustenta el crédito fiscal del ISV (`invoice_outside_authorization`) | factura recibida 001-001-01-00000201 del 8010000109301: se emitió el 2026-09-07, después de su fecha límite de emisión, el 2026-09-04 | 111,550.00 | — | — | `2026-09/30-facturacion/recibidas/fr-001-001-01-00000201.pdf` |
| 6 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-10901: nota débito sin registrar del 2026-09-30 por -20,000.00 (sin referencia) | -20,000.00 | — | 0 | `2026-09/20-bancos/andino-10901/extracto.pdf` fila 17 |
| 7 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura 000-001-01-00000104: ISV 75,000.00 en el XML y 75,010.00 en libros | 10.00 | — | — | `2026-09/30-facturacion/emitidas/fe-000-001-01-00000104.pdf` · `2026-09/10-contabilidad/libro-mayor.xlsx` fila 15 · `2026-09/10-contabilidad/libro-mayor.xlsx` fila 16 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Entidad, identificación fiscal, país y moneda → Banco de Occidente Sintético · RTN 08010004578120 · Honduras · HNL
- Marco contable → NIIF (la carpeta no lo declara; propuesta por defecto)
- Periodo que se está cerrando → 2026-09 (el último con 10-contabilidad/)
- Cuentas que cruzan las facturas → ventas 4135, IVA 2408, compras 5135/5145/5195: sus débitos con ISV 15 % cuadran con lo acreditado en 2205; `cuentas` no devolvió ninguna porque las facturas de Honduras no traen XML
- Cuentas que se concilian contra auxiliar y cuentas bancarias → 1305 y 2205 (tienen auxiliar en 2026-08 y 2026-09); bancos andino-10901 y pacifico-10902
- Checklist → el de la organización (00-referencia/checklist-cierre.xlsx), sin aprobar hasta que una persona lo apruebe
- Quién aprueba el cierre y festivos → Contralor (por defecto); sin festivos, nadie los dio
- Dónde se guarda el estado → estado-finanzas/08010004578120-banco-de-occidente-sintetico
- Términos → aceptados por José Francisco Ñáñez el 2026-10-06

## Fuentes

- `00-referencia/checklist-cierre.xlsx`
- `2026-09/10-contabilidad/balance-comprobacion.csv`
- `2026-09/10-contabilidad/libro-mayor.xlsx`
- `2026-09/20-bancos/andino-10901/extracto.pdf`
- `2026-09/30-facturacion/emitidas/fe-000-001-01-00000104.pdf`
- `2026-09/30-facturacion/recibidas/fr-001-001-01-00000201.pdf`

La corrida quedó registrada como `2026-10-06-close-scan-1` con 7 hallazgos. La salida completa está en `estado-finanzas/08010004578120-banco-de-occidente-sintetico/corridas/salida-close-scan.md`.