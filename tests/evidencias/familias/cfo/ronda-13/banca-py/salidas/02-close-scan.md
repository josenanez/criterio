# /criterio-finance:close-scan 

Primer barrido de la entidad: 65 archivos nuevos, 0 cambiados, 0 borrados, 0 fuera de su lugar. Salieron 9 señales, todas nuevas porque no había una corrida anterior de close-scan. El correo del 2026-10-05 de Sofía León declara el cierre «en curso». Esa declaración ya estaba en la ficha, así que no la modifiqué.

El motor generó el reporte completo en `estado-finanzas/88457812-7-banco-del-tebicuary-sintetico/cierre/2026-09/reporte-close-scan.md`. Es el que va debajo; no se pudo procesar nada.

# Qué cambió en el cierre · Banco del Tebicuary (sintético) · periodo 2026-09

**Entidad:** Banco del Tebicuary (sintético) (88457812-7) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.2.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: el mayor suma débitos 0,00 y créditos 0,00; el balance dice 75.000,00 y 0,00 | -75.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: saldo inicial más movimientos no da el saldo final (75.000,00) | 75.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 15 |
| 3 | Los débitos y los créditos del balance de comprobación no suman lo mismo (`trial_balance_unbalanced`) | débitos 3.183.420.010,00 y créditos 3.183.345.010,00: diferencia 75.000,00 | 75.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` |
| 4 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.xlsx` fila 3 |
| 5 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 001-001-0000109 del 2026-09-28 por 165.000.000,00 sin registro contable | 165.000.000,00 | — | — | `2026-09/30-facturacion/emitidas/fe-001-001-0000109.xml` |
| 6 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-13101: cheque pendiente de cobro del 2026-06-15 por -45.000.000,00 (CH-0450) | -45.000.000,00 | — | 107 | `2026-09/20-bancos/andino-13101/auxiliar-libros.csv` fila 2 |
| 7 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-13101: nota débito sin registrar del 2026-09-30 por -6.000.000,00 (sin referencia) | -6.000.000,00 | — | 0 | `2026-09/20-bancos/andino-13101/extracto.xlsx` fila 17 |
| 8 | El valor o el impuesto del XML no es el del registro (`einvoice_amount_mismatch`) | factura 001-001-0000104: IVA 14.250.000,00 en el XML y 14.250.010,00 en libros | 10,00 | — | — | `2026-09/30-facturacion/emitidas/fe-001-001-0000104.xml` · `2026-09/10-contabilidad/libro-mayor.csv` fila 15 · fila 16 |
| 9 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-13101: cheque pendiente de cobro lleva 107 días (CH-0450) | -45.000.000,00 | — | 107 | `2026-09/20-bancos/andino-13101/auxiliar-libros.csv` fila 2 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Las 9 respuestas ya estaban en la ficha desde finance-setup (entidad, marco contable, periodo 2026-09, cuentas, bancos, checklist, aprobadora, ruta del estado y términos). El reporte las muestra completas.

## Fuentes

`00-referencia/checklist-cierre.xlsx`, `2026-09/10-contabilidad/balance-comprobacion.xlsx`, `2026-09/10-contabilidad/libro-mayor.csv`, `2026-09/20-bancos/andino-13101/auxiliar-libros.csv`, `2026-09/20-bancos/andino-13101/extracto.xlsx`, `2026-09/30-facturacion/emitidas/fe-001-001-0000104.xml`, `2026-09/30-facturacion/emitidas/fe-001-001-0000109.xml`

La corrida quedó registrada como `2026-10-06-close-scan-1` con 9 hallazgos.

- **Términos:** `terminos` los dio vigentes, aceptados el 2026-10-06 por José Francisco Ñáñez (versión 1.3, plugin 1.2.0), así que no hizo falta registrar nada.
- **Sección «El resultado»:** salió vacía en el reporte del motor, y no inventé contenido para ella.
- **Salida registrada:** `corridas/salida-close-scan.md` lleva mi línea de apertura y el reporte del motor, sin la sección vacía «El resultado» ni el listado de preguntas, que acorté arriba. No es idéntica a lo que ves aquí.