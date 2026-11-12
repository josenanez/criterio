# /criterio-finance:close-scan 

Este es el primer inventario con huella, así que los 62 archivos aparecen como nuevos. Ninguno cambió, ninguno se borró y ninguno está fuera de su lugar. Los 7 tipos de señal y las 8 señales son los mismos que encontró `finance-setup`: respecto de esa corrida no hay ninguna señal nueva.

No hubo nada que extraer a la ficha. La declaración del correo de Sofía León («en curso», 2026-10-05) ya estaba registrada. Los tres archivos R-0x de `50-auditoria/respuestas/` son respuestas, no requerimientos nuevos, y el índice del auditor está en CSV, así que lo procesa el motor. La sección «El resultado» llegó vacía del motor.

**62 archivos nuevos o cambiados · 0 señales nuevas respecto de la corrida anterior (8 en total).**

# Qué cambió en el cierre · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 2505: el mayor suma débitos 360,000.00 y créditos 362,700.00; el balance dice 360,000.00 y 360,000.00 | -2,700.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 8 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5195: el mayor suma débitos 98,730.00 y créditos 0.00; el balance dice 96,030.00 y 0.00 | 2,700.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 14 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 3 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4301: consignación en tránsito del 2026-09-30 por 151,380.00 (A000107) | 151,380.00 | — | 0 | `2026-09/20-bancos/andino-4301/auxiliar-libros.csv` fila 16 |
| 5 | El mismo CUFE o la misma clave de acceso aparece registrado dos veces (`einvoice_duplicate`) | factura B000201 registrada en 2 asientos (C-021, C-022) | 69,840.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 · `2026-09/10-contabilidad/libro-mayor.csv` fila 56 · `2026-09/10-contabilidad/libro-mayor.csv` fila 57 |
| 6 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento B000202 en las cuentas de compras por 61,110.00 sin factura electrónica en recibidas/ | 61,110.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 59 · `2026-09/10-contabilidad/libro-mayor.csv` fila 60 |
| 7 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura B000201: base 34,920.00 en el XML y 69,840.00 en libros; IVA 5,587.20 en el XML y 11,174.40 en libros | 40,507.20 | — | — | `2026-09/30-facturacion/recibidas/fr-B000201.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 · `2026-09/10-contabilidad/libro-mayor.csv` fila 56 |
| 8 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | cuenta 2205: no hay auxiliar del periodo para conciliarla | — | — | — | `2026-09/10-contabilidad/auxiliares/` |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad: nombre, identificación fiscal, país y moneda? → Distribuidora del Noroeste, RFC DNO190402B43, México, MXN (sugerida desde el nombre de la carpeta y los CFDI 4.0 del periodo)
- ¿Qué marco contable adoptó la entidad? → NIF del CINIF (sugerida: la mayoría de las no listadas en México, F-20; ningún documento dice otro)
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado 2408; IVA descontable 2408 (las que sostienen las facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué cuentas bancarias se esperan? → 1305 y 2205; bancos andino-4301 y pacifico-4302
- ¿Qué checklist se usa? → El de la organización: 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (C-09 del checklist); sin festivos registrados
- ¿Dónde se guarda el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste
- ¿Acepta los términos de esta versión? → Sí, José Francisco Ñáñez, 2026-10-06

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/auxiliares/`
- `2026-09/10-contabilidad/balance-comprobacion.xlsx`
- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/andino-4301/auxiliar-libros.csv`
- `2026-09/30-facturacion/recibidas/fr-B000201.xml`