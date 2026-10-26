# /criterio-finance:close-scan 

63 archivos nuevos (0 cambiados, 0 borrados, 0 fuera de su lugar) y 8 señales. Son las mismas 8 que dejó la corrida anterior (finance-setup), así que no hay señales nuevas.

El correo del 2026-10-05 sigue declarando el cierre «en curso». R-01 a R-03 ya vienen en la tabla del auditor. Por eso no cambié la ficha. Los términos estaban vigentes (aceptada 0.9.0), así que no registré ninguna aceptación nueva.

**Reporte (`close-scan`, Banco Andino, periodo 2026-09)**

Lo que hay que atender:

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | `ledger_vs_trial_balance` | cuenta 5305: el mayor suma débitos 0,00 y créditos 0,00; el balance dice 5.000,00 y 0,00 | -5.000,00 | `balance-comprobacion.csv` fila 15 · `libro-mayor.csv` |
| 2 | `ledger_vs_trial_balance` | cuenta 5305: saldo inicial más movimientos no da el saldo final (5.000,00) | 5.000,00 | `balance-comprobacion.csv` fila 15 |
| 3 | `trial_balance_unbalanced` | débitos 253.437.700,00 y créditos 253.432.700,00: diferencia 5.000,00 | 5.000,00 | `balance-comprobacion.csv` |
| 4 | `close_task_done_without_evidence` | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte que empiece por C-02 (responsable: Andrés Paz) | — | `checklist-cierre.xlsx` fila 3 |
| 5 | `bank_unreconciled` | andino-1101: cheque pendiente de cobro del 2026-07-20 por -3.000.000,00 (CH-0450), 72 días | -3.000.000,00 | `andino-1101/auxiliar-libros.csv` fila 2 |
| 6 | `bank_unreconciled` | andino-1101: nota débito sin registrar del 2026-09-30 por -400.000,00 (sin referencia) | -400.000,00 | `andino-1101/extracto.xlsx` fila 17 |
| 7 | `einvoice_amount_mismatch` | factura SETP99000104: IVA 1.662.500,00 en el XML y 1.663.500,00 en libros | 1.000,00 | `fe-SETP99000104.xml` · `libro-mayor.csv` filas 15 y 16 |
| 8 | `reconciling_item_aged` | andino-1101: el cheque CH-0450 lleva 72 días | -3.000.000,00 | `andino-1101/auxiliar-libros.csv` fila 2 |

- **El resultado:** el motor dejó esta sección vacía y no escribí cifras en su lugar.
- **No se pudo procesar:** nada; todo lo que llegó se procesó.
- **Preguntas que hizo:** son las 7 respuestas por defecto que dejó la corrida anterior. Entre ellas, el marco (Grupo 1 NIIF) quedó sin confirmar y el checklist de la organización sin aprobación registrada.
- **Fuentes:** el checklist, el balance de comprobación, el mayor, el auxiliar y el extracto de andino-1101, y el XML de la factura SETP99000104.

La salida quedó en `estado-finanzas/900123456-banco-andino/corridas/salida-close-scan.md` y el reporte del motor en `estado-finanzas/900123456-banco-andino/cierre/2026-09/reporte-close-scan.md`. La corrida quedó registrada como `2026-10-06-close-scan-1`.