# /criterio-finance:bank-reconcile 

Se concilió una de las dos cuentas del periodo. Los términos (v1.2) ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-06, así que no hizo falta registrarlos otra vez.

La cuenta pacifico-2302 no tiene extracto, así que quedó sin conciliar. La falta se registró como señal `reconciliation_stale`. Para cerrarla hay que cargar el extracto en `2026-09/20-bancos/pacifico-2302/`. Es la acción que sigue.

# Conciliación bancaria · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | pacifico-2302: falta el extracto del periodo | — | — | — | `2026-09/20-bancos/pacifico-2302/` |

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-2301 | 6,560.00 | 0.00 | 0.00 | 0.00 | 0.00 | 6,560.00 | 0.00 |

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

- `2026-09/20-bancos/pacifico-2302/`

La salida quedó guardada en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-bank-reconcile.md`. La corrida quedó registrada como `2026-10-06-bank-reconcile-1`, con 7 hallazgos según el motor.