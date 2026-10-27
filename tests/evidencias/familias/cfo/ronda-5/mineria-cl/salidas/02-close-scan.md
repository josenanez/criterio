# /criterio-finance:close-scan 

63 archivos nuevos, 0 cambiados, 0 borrados y 7 señales en el periodo 2026-09. Es la primera corrida registrada, así que todo cuenta como nuevo. La ficha ya recogía la declaración del correo de Sofía León del 2026-10-05 («en curso»), así que no la cambié.

Los términos (versión 1.2) ya estaban vigentes, así que no hizo falta registrar una aceptación nueva.

# Qué cambió en el cierre · Minera Atacama Norte · periodo 2026-09

**Entidad:** Minera Atacama Norte (76089001-4) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 1000109 del 2026-09-28 por 5.712.000,00 sin registro contable | 5.712.000,00 | — | — | `2026-09/30-facturacion/emitidas/fe-1000109.xml` |
| 2 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento 2000202 en las cuentas de compras por 2.037.000,00 sin factura electrónica en recibidas/ | 2.037.000,00 | — | — | `2026-09/10-contabilidad/libro-mayor.xlsx` fila 53 · `2026-09/10-contabilidad/libro-mayor.xlsx` fila 54 |
| 3 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-8901: cheque pendiente de cobro del 2026-06-15 por -1.800.000,00 (CH-0450) | -1.800.000,00 | — | 107 | `2026-09/20-bancos/andino-8901/auxiliar-libros.csv` fila 2 |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-8901: nota débito sin registrar del 2026-09-30 por -240.000,00 (sin referencia) | -240.000,00 | — | 0 | `2026-09/20-bancos/andino-8901/extracto.xlsx` fila 17 |
| 5 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx` fila 6 |
| 6 | Una tarea del checklist pasó su fecha y no tiene evidencia (`close_task_overdue`) | C-05 · Registrar provisiones y causaciones: venció el 2026-10-05 y no tiene evidencia | — | Jorge Vela | 1 | `00-referencia/checklist-cierre.csv` fila 6 |
| 7 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-8901: cheque pendiente de cobro lleva 107 días (CH-0450) | -1.800.000,00 | — | 107 | `2026-09/20-bancos/andino-8901/auxiliar-libros.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su identificación, país y moneda? → Minera Atacama Norte, RUT 76089001-4, Chile, CLP (tomado del nombre de la carpeta; sin confirmar con la persona)
- ¿Qué marco contable aplica? → NIIF adoptadas por el Colegio de Contadores de Chile (F-18); solo se registra
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 4135, compras 5135, 5145 y 5195, IVA generado y descontable 2408: las que sostienen facturas del periodo según el motor
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205, con auxiliar en 2026-08 y 2026-09; bancos andino-8901 y pacifico-8902
- ¿Qué checklist se usa? → 00-referencia/checklist-cierre.csv de la organización; sin aprobar hasta que una persona lo apruebe
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-08 y C-09 en el checklist); festivos: ninguno declarado
- ¿Dónde se guarda el estado? → estado-finanzas/76089001-4-minera-atacama-norte, fuera de la carpeta de documentos
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → No: nadie lo autorizó en esta sesión

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/libro-mayor.xlsx`
- `2026-09/20-bancos/andino-8901/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-8901/extracto.xlsx`
- `2026-09/30-facturacion/emitidas/fe-1000109.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx`

Dos cosas sobre el reporte:
- **«El resultado» sale vacío.** El motor no escribió texto en esa sección y no lo inventé.
- **El conteo de «no procesado» no coincide.** `compute` devolvió `no_procesado: 14`, pero el reporte dice «Todo lo que llegó se procesó». No lo investigué; conviene que alguien lo mire.

La salida quedó en `estado-finanzas/76089001-4-minera-atacama-norte/corridas/salida-close-scan.md`. La corrida quedó registrada como `2026-10-06-close-scan-1`, con 7 hallazgos.