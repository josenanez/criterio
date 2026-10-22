# /criterio-finance:close-scan 

57 archivos nuevos, 0 cambiados y 0 borrados. Hay 7 señales, todas nuevas porque es la primera corrida de close-scan. Los términos (versión 1.2) ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06.

El correo del 2026-10-05 declara el cierre «en curso». La carta del auditor del 2026-10-02 trae el requerimiento R-09, con vencimiento el 2026-10-09. Ambos ya estaban en la ficha, así que no la modifiqué. En esta corrida solo convertí los documentos y calculé.

# Qué cambió en el cierre · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una tarea figura cumplida y ningún documento la sostiene (`close_task_done_without_evidence`) | C-02 · Conciliar cada cuenta bancaria: figura cumplida y no hay soporte en 2026-09/40-soportes/ que empiece por C-02 | — | Andrés Paz | — | `00-referencia/checklist-cierre.csv` fila 3 |
| 2 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4101: cheque pendiente de cobro del 2026-06-15 por -6,000.00 (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-4101/auxiliar-libros.csv` fila 2 |
| 3 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura recibida 002-001-000000290 del 2026-09-27 por 4,600.00 sin registro contable | 4,600.00 | — | — | `2026-09/30-facturacion/recibidas/fr-002-001-000000290.xml` |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4101: nota débito sin registrar del 2026-09-30 por -800.00 (sin referencia) | -800.00 | — | 0 | `2026-09/20-bancos/andino-4101/extracto.csv` fila 17 |
| 5 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 6 |
| 6 | Una tarea del checklist pasó su fecha y no tiene evidencia (`close_task_overdue`) | C-05 · Registrar provisiones y causaciones: venció el 2026-10-05 y no tiene evidencia | — | Jorge Vela | 1 | `00-referencia/checklist-cierre.csv` fila 6 |
| 7 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-4101: cheque pendiente de cobro lleva 107 días (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-4101/auxiliar-libros.csv` fila 2 |

## El resultado

La sección salió vacía del motor.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de documentos? → finanzas/0990054321001-minera-condor (la del argumento)
- ¿Entidad, país y moneda? → Minera Cóndor, RUC 0990054321001, Ecuador, USD (por el RUC de las facturas y la carpeta)
- ¿Qué marco contable aplica? → No indicado en los documentos; queda registrado así
- ¿Qué periodo se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14/51/52/61; IVA 2408 (los del balance de comprobación)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); andino-4101 y pacifico-4102 (carpetas de 20-bancos)
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin constancia de aprobación, queda como no aprobado
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-09 en el checklist)
- ¿Festivos? → Ninguno a mano; la lista queda vacía

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/20-bancos/andino-4101/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-4101/extracto.csv`
- `2026-09/30-facturacion/recibidas/fr-002-001-000000290.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv`

La corrida quedó registrada como `2026-10-06-close-scan-1`, con 7 hallazgos. Lo que se mostró está en `estado-finanzas/0990054321001-minera-condor/corridas/salida-close-scan.md`.

Dos cosas que no coinciden: el texto que escribí a mano en ese archivo (la línea de conteos y el aviso de términos) no figura en lo que se te mostró aquí. Tampoco corrí el paso del reporte que lo guarda en `reporte-close-scan.md`, así que no confirmé que ese archivo exista.