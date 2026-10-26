# /criterio-finance:close-scan 

Archivos nuevos o cambiados: 63 nuevos y 0 cambiados. No hay borrados ni fuera de su lugar. El motor encontró 5 señales, todas nuevas porque es el primer `close-scan`. El correo del estado del cierre, la carta del auditor y las respuestas se convirtieron, pero la ficha ya los tenía de `finance-setup`, así que no cambié nada.

# Qué cambió en el cierre · Minera Puna Alta · periodo 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida F001-00000109 del 2026-09-28 por 23,010.00 sin registro contable | 23,010.00 | — | — | `2026-09/30-facturacion/emitidas/fe-F001-00000109.xml` |
| 2 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento F002-00000202 en las cuentas de compras por 20,370.00 sin factura electrónica en recibidas/ | 20,370.00 | — | — | `2026-09/10-contabilidad/libro-mayor.xlsx` fila 53 · `2026-09/10-contabilidad/libro-mayor.xlsx` fila 54 |
| 3 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-7301: cheque pendiente de cobro del 2026-06-15 por -18,000.00 (CH-0450) | -18,000.00 | — | 107 | `2026-09/20-bancos/andino-7301/auxiliar-libros.csv` fila 2 |
| 4 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx` fila 6 |
| 5 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-7301: cheque pendiente de cobro lleva 107 días (CH-0450) | -18,000.00 | — | 107 | `2026-09/20-bancos/andino-7301/auxiliar-libros.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de documentos? → finanzas/20730000015-minera-puna-alta (la dio el argumento)
- ¿Entidad, identificación, país y moneda? → Minera Puna Alta, RUC 20730000015, PE, PEN (por el nombre de la carpeta; moneda por defecto del país)
- ¿Marco contable? → NIIF oficializadas por el Consejo Normativo de Contabilidad (F-15)
- ¿Periodo que se cierra? → 2026-09 (el último con 10-contabilidad)
- ¿Cuentas que cruzan las facturas? → ventas 41; compras 14/51/52/61; IVA 2408 (valores por defecto; el balance trae 4135, 1435, 51xx y 2408)
- ¿Cuentas a conciliar y bancos esperados? → 1305 y 2205 (hay auxiliar de ambas); bancos andino-7301 y pacifico-7302 (carpetas de 20-bancos)
- ¿Checklist? → 00-referencia/checklist-cierre.csv de la organización; queda sin aprobar hasta que una persona lo apruebe
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-08 y C-09 en el checklist); festivos: no se dieron
- ¿Dónde se guarda el estado? → estado-finanzas/20730000015-minera-puna-alta
- ¿Términos? → Aceptados por José Francisco Ñáñez el 2026-10-06 (indicado en la instrucción de la prueba)
- ¿Marcar la carpeta con _CRITERIO_FINANZAS.txt? → No: sin autorización dada en la prueba, no se escribe en los documentos

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.xlsx`
- `2026-09/20-bancos/andino-7301/auxiliar-libros.csv`
- `2026-09/30-facturacion/emitidas/fe-F001-00000109.xml`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx`

La sección "El resultado" salió vacía en el reporte del motor, y la dejé así. Dejé la corrida registrada como `2026-10-06-close-scan-1`, con la salida completa en `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-close-scan.md`.