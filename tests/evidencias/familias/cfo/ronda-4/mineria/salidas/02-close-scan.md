# /criterio-finance:close-scan 

63 archivos nuevos y 0 cambiados desde el inventario anterior; el motor registra 7 señales abiertas en 2026-09. La ficha ya traía el correo de Sofía León («en curso») y la carta del auditor (R-09), sin cambios.

# Qué cambió en el cierre · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 2 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4101: cheque pendiente de cobro del 2026-06-15 por -6,000.00 (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-4101/auxiliar-libros.csv` fila 2 |
| 3 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura recibida 002-001-000000290 del 2026-09-27 por 4,600.00 sin registro contable | 4,600.00 | — | — | `2026-09/30-facturacion/recibidas/fr-002-001-000000290.xml` |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4101: nota débito sin registrar del 2026-09-30 por -800.00 (sin referencia) | -800.00 | — | 0 | `2026-09/20-bancos/andino-4101/extracto.xlsx` fila 17 |
| 5 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx` fila 6 |
| 6 | Una tarea del checklist pasó su fecha y no tiene evidencia (`close_task_overdue`) | C-05 · Registrar provisiones y causaciones: venció el 2026-10-05 y no tiene evidencia | — | Jorge Vela | 1 | `00-referencia/checklist-cierre.csv` fila 6 |
| 7 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-4101: cheque pendiente de cobro lleva 107 días (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-4101/auxiliar-libros.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de la entidad? → finanzas/0990054321001-minera-condor (la del argumento)
- ¿Entidad, país y moneda? → Minera Cóndor, RUC 0990054321001, Ecuador, USD (el RUC y los lectores del SRI en las facturas)
- ¿Qué marco aplica? → Marco aplicable en Ecuador (F-06); ningún documento dice el grupo, queda sin precisar
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA 2408 (las que sostienen facturas del periodo)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); bancos andino-4101 y pacifico-4102 (los del periodo)
- ¿Qué checklist se usa? → 00-referencia/checklist-cierre.csv, de la organización, sin aprobar
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivos: no encontrado
- ¿Dónde se guarda el estado? → estado-finanzas/0990054321001-minera-condor
- ¿Se acepta la versión de términos? → Sí: José Francisco Ñáñez, 2026-10-06
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → No: sin respuesta de la persona, no se escribe nada en los documentos

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/20-bancos/andino-4101/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-4101/extracto.xlsx`
- `2026-09/30-facturacion/recibidas/fr-002-001-000000290.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx`

La corrida quedó registrada como `2026-10-06-close-scan-1`.