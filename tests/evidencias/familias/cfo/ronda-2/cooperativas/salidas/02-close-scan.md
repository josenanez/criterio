# /criterio-finance:close-scan 

53 archivos nuevos, 0 cambiados y 7 señales en esta corrida. Es el primer barrido, así que no hay corrida anterior de close-scan con la que comparar.

Los términos de la versión 0.8.0 ya estaban vigentes, con aceptación registrada el 2026-10-06, así que no hizo falta pedirla otra vez. La ficha del cierre ya recogía el correo de Sofía León del 2026-10-05 («en curso»), y `compute` no reportó problemas de registro.

# Qué cambió en el cierre · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 001-001-000000109 del 2026-09-28 por 4,887.50 sin registro contable | 4,887.50 | — | — | `2026-09/30-facturacion/emitidas/fe-001-001-000000109.xml` |
| 2 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento 002-001-000000202 en las cuentas de compras por 3,395.00 sin factura electrónica en recibidas/ | 3,395.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 |
| 3 | El saldo de una cuenta en el mayor no es el de su auxiliar (cuentas por cobrar, por pagar, inventarios, activos fijos, intercompañías) (`account_unreconciled`) | cuenta 1305: el mayor dice 14,612.50 y el auxiliar suma 12,362.50 | 2,250.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 4 · `2026-09/10-contabilidad/auxiliares/1305-clientes.csv` |
| 4 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 6 |
| 5 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-03 · Detalle de facturas emitidas: respondido sin soporte, venció el 2026-10-03 | — | Lucía Mora | 3 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 4 |
| 6 | Una tarea del checklist pasó su fecha y no tiene evidencia (`close_task_overdue`) | C-05 · Registrar provisiones y causaciones: venció el 2026-10-05 y no tiene evidencia | — | Jorge Vela | 1 | `00-referencia/checklist-cierre.csv` fila 6 |
| 7 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | pacifico-2302: falta el extracto del periodo | — | — | — | `2026-09/20-bancos/pacifico-2302/` |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su RUC, país y moneda? → Cooperativa Sierra Alta, RUC 1790012345001, Ecuador, USD (por el nombre de la carpeta y las facturas del SRI)
- ¿Qué marco contable aplica? → NIIF para PYMES, por confirmar: ningún documento lo dice
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41, compras 5135/5145/5195, IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (los auxiliares que hay); bancos andino-2301 y pacifico-2302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada
- ¿Quién aprueba el cierre? → Sofía León, responsable de C-09 en el checklist
- ¿Hay festivos del calendario? → No encontrado: ningún documento los trae

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/auxiliares/1305-clientes.csv`
- `2026-09/10-contabilidad/balance-comprobacion.csv`
- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/pacifico-2302/`
- `2026-09/30-facturacion/emitidas/fe-001-001-000000109.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv`

La sección «El resultado» salió vacía en el reporte del motor, y la dejé así.

La corrida quedó registrada como `2026-10-06-close-scan-1` con 7 hallazgos. La salida completa está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-close-scan.md`.