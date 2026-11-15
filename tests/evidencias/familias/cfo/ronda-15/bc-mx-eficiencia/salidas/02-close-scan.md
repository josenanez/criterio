# /criterio-finance:close-scan 

Este es el primer inventario de la entidad, así que los 62 archivos aparecen como nuevos. Ninguno cambió, ninguno se borró y ninguno está fuera de su lugar. El correo de Sofía León del 2026-10-05, que dice que el cierre está «en curso», ya estaba en la ficha. Todos los requerimientos del auditor están en `pbc-2026-09.csv`, así que no hubo nada que extraer.

Hay 62 archivos nuevos y 0 cambiados. Las señales son 8, las mismas 8 que dejó la corrida anterior (finance-setup), así que no hay ninguna nueva.

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

- ¿Esta es la carpeta de documentos de la entidad? → Sí: finanzas/DNO190402B43-distribuidora-del-noroeste, la que trae el argumento
- ¿Cuál es la entidad (nombre, identificación fiscal, país y moneda)? → Distribuidora del Noroeste · RFC DNO190402B43 · México · MXN, del nombre de la carpeta y del emisor de los CFDI
- ¿Qué marco contable adoptó la entidad? → NIF del CINIF, el de la mayoría de las no listadas en México (F-20); ningún documento lo dice
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 4135 · compras 5135, 5145, 5195 · IVA generado 2408 · IVA descontable 2408, las que sostienen las facturas del periodo
- ¿Qué cuentas se concilian contra auxiliar y qué cuentas bancarias se esperan? → 1305 y 2205, con auxiliar en 2026-09 o 2026-08; bancos andino-4301 y pacifico-4302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre y qué festivos tiene el calendario? → Sofía León, responsable de C-09; sin festivos a mano
- ¿Dónde se guarda el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste
- ¿Se marca la carpeta con _CRITERIO_FINANZAS.txt? → No: nadie dio el sí en esta sesión de prueba

## Fuentes

- `00-referencia/checklist-cierre.csv`
- `2026-09/10-contabilidad/auxiliares/`
- `2026-09/10-contabilidad/balance-comprobacion.xlsx`
- `2026-09/10-contabilidad/libro-mayor.csv`
- `2026-09/20-bancos/andino-4301/auxiliar-libros.csv`
- `2026-09/30-facturacion/recibidas/fr-B000201.xml`

---

La corrida quedó registrada como `2026-10-06-close-scan-1`. Lo que se mostró está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-close-scan.md`.