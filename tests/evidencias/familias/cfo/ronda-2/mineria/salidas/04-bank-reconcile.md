# /criterio-finance:bank-reconcile 

Términos vigentes (versión 1.2, ya aceptados), así que no hubo que registrar la aceptación otra vez. Concilié las dos cuentas del periodo 2026-09: la diferencia sin explicar es 0.00 en ambas. Quedan dos partidas abiertas, las dos en andino-4101.

# Conciliación bancaria · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4101: cheque pendiente de cobro del 2026-06-15 por -6,000.00 (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-4101/auxiliar-libros.csv` fila 2 |
| 2 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4101: nota débito sin registrar del 2026-09-30 por -800.00 (sin referencia) | -800.00 | — | 0 | `2026-09/20-bancos/andino-4101/extracto.csv` fila 17 |
| 3 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-4101: cheque pendiente de cobro lleva 107 días (CH-0450) | -6,000.00 | — | 107 | `2026-09/20-bancos/andino-4101/auxiliar-libros.csv` fila 2 |

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-4101 | 25,089.00 | 0.00 | -6,000.00 | 0.00 | -800.00 | 19,889.00 | 0.00 |
| pacifico-4102 | 60,000.00 | 0.00 | 0.00 | 0.00 | 0.00 | 60,000.00 | 0.00 |

**andino-4101 · partidas abiertas por antigüedad**

| Fecha | Clase | Referencia | Valor | Días | Tramo |
|---|---|---|---|---|---|
| 2026-06-15 | cheque pendiente de cobro | CH-0450 | -6,000.00 | 107 | más de 90 |
| 2026-09-30 | nota débito sin registrar | — | -800.00 | 0 | 0-30 |

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

- `2026-09/20-bancos/andino-4101/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-4101/extracto.csv`

La corrida quedó registrada como `2026-10-06-bank-reconcile-1`. La salida completa está en `estado-finanzas/0990054321001-minera-condor/corridas/salida-bank-reconcile.md`.