# /criterio-finance:close-scan 

Términos vigentes (versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-06).

Inventario: 64 archivos nuevos, 0 cambiados, 0 borrados, 0 fuera de su lugar. Revisé la ficha del cierre contra los 16 PDF de factura, el correo del estado y la tabla del auditor. Coincide, así que no la toqué.

Archivos nuevos o cambiados: 64. Señales: 7 en total y 0 nuevas respecto de la corrida anterior (`finance-setup`, que también dejó 7).

# Qué cambió en el cierre · Almacenes del Valle de Sula · periodo 2026-09

**Entidad:** Almacenes del Valle de Sula (08010006129040) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.1.0 · **Aprueba:** Sofía León · **Comando:** `close-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El cierre se reporta como cerrado y hay señales abiertas que ese estado no explica (`declared_close_vs_evidence`) | el cierre se reporta cerrado (2026-09/40-soportes/correo-estado-del-cierre.md, 2026-10-05) y hay 6 señales abiertas que ese estado no explica | — | — | — | `2026-09/40-soportes/correo-estado-del-cierre.md` |
| 2 | Una factura electrónica emitida o recibida no tiene registro contable (`einvoice_not_recorded`) | factura emitida 000-001-01-00000109 del 2026-09-28 por 161,000.00 sin registro contable | 161,000.00 | — | — | `2026-09/30-facturacion/emitidas/fe-000-001-01-00000109.pdf` |
| 3 | Un registro que la necesita no tiene factura electrónica que lo soporte (`recorded_without_einvoice`) | documento 001-001-01-00000202 en las cuentas de compras por 135,800.00 sin factura electrónica en recibidas/ | 135,800.00 | — | — | `2026-09/10-contabilidad/libro-mayor.csv` fila 53 · `2026-09/10-contabilidad/libro-mayor.csv` fila 54 |
| 4 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-11301: cheque pendiente de cobro del 2026-06-15 por -120,000.00 (CH-0450) | -120,000.00 | — | 107 | `2026-09/20-bancos/andino-11301/auxiliar-libros.csv` fila 2 |
| 5 | Una factura recibida de Honduras cae fuera de su rango autorizado o se emitió después de su fecha límite: no sustenta el crédito fiscal del ISV (`invoice_outside_authorization`) | factura recibida 001-001-01-00000203 del 8010000113303: está fuera del rango autorizado 001-001-01-00000001 a 001-001-01-00000198 | 89,240.00 | — | — | `2026-09/30-facturacion/recibidas/fr-001-001-01-00000203.pdf` |
| 6 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx` fila 6 |
| 7 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-11301: cheque pendiente de cobro lleva 107 días (CH-0450) | -120,000.00 | — | 107 | `2026-09/20-bancos/andino-11301/auxiliar-libros.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad/); tomada la sugerida, sin respuesta humana
- ¿Qué cuentas cruzan las facturas? → ventas 4135; compras 5135, 5145, 5195; ISV 2408 (propuestas por el motor desde las facturas)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (con auxiliar en 2026-08 y 2026-09); andino-11301 y pacifico-11302
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-09 en el checklist); festivos: ninguno dado
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta? → No se dejó: nadie dio un sí

## Fuentes

- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/andino-11301/auxiliar-libros.csv`
- `2026-09/30-facturacion/emitidas/fe-000-001-01-00000109.pdf`
- `2026-09/30-facturacion/recibidas/fr-001-001-01-00000203.pdf`
- `2026-09/40-soportes/correo-estado-del-cierre.md`
- `2026-09/50-auditoria/requerimientos/pbc-2026-09.xlsx`

La corrida quedó registrada como `2026-10-06-close-scan-1` (7 hallazgos). La salida está en `corridas/salida-close-scan.md`.

Dos cosas que conviene saber:
- La sección «El resultado» del reporte salió vacía; el motor la generó así y no agregué nada.
- El inventario marcó los 64 archivos como nuevos aunque `finance-setup` ya había corrido ese mismo día, así que no sirve para distinguir lo que cambió desde esa corrida.