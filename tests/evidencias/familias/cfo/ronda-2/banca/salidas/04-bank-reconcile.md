# /criterio-finance:bank-reconcile 

Conciliación de septiembre 2026: las dos cuentas quedan con diferencia sin explicar en cero. En andino-1101 hay un cheque de 72 días y una nota débito sin registrar.

# Conciliación bancaria · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-1101: cheque pendiente de cobro del 2026-07-20 por -3.000.000,00 (CH-0450) | -3.000.000,00 | — | 72 | `2026-09/20-bancos/andino-1101/auxiliar-libros.csv` fila 2 |
| 2 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-1101: nota débito sin registrar del 2026-09-30 por -400.000,00 (sin referencia) | -400.000,00 | — | 0 | `2026-09/20-bancos/andino-1101/extracto.csv` fila 17 |
| 3 | Una partida conciliatoria lleva más días de los configurados (`reconciling_item_aged`) | andino-1101: cheque pendiente de cobro lleva 72 días (CH-0450) | -3.000.000,00 | — | 72 | `2026-09/20-bancos/andino-1101/auxiliar-libros.csv` fila 2 |

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-1101 | 13.273.400,00 | 0,00 | -3.000.000,00 | 0,00 | -400.000,00 | 10.673.400,00 | 0,00 |
| pacifico-1102 | 30.000.000,00 | 0,00 | 0,00 | 0,00 | 0,00 | 30.000.000,00 | 0,00 |

**andino-1101 · partidas abiertas por antigüedad**

| Fecha | Clase | Referencia | Valor | Días | Tramo |
|---|---|---|---|---|---|
| 2026-07-20 | cheque pendiente de cobro | CH-0450 | -3.000.000,00 | 72 | 61-90 |
| 2026-09-30 | nota débito sin registrar | — | -400.000,00 | 0 | 0-30 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su país y su moneda? → Banco Andino, NIT 900123456, Colombia, COP (tomado del nombre de la carpeta)
- ¿Qué marco contable aplica? → grupo 1 (propuesta por defecto; ningún documento lo declara, por confirmar)
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué cuentas cruzan las facturas? → ventas 41; compras 14, 51, 52, 61; IVA generado y descontable 2408 (visto en el balance)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (hay auxiliar); bancos andino-1101 y pacifico-1102
- ¿Qué checklist se usa? → el de la organización, 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre? → Sofía León (Contraloría, responsable de C-09)
- ¿Festivos del calendario? → 2026-10-12 (festivo por defecto, por confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino

## Fuentes

- `2026-09/20-bancos/andino-1101/auxiliar-libros.csv`
- `2026-09/20-bancos/andino-1101/extracto.csv`

La corrida quedó registrada como `2026-10-06-bank-reconcile-1`. La salida está en `estado-finanzas/900123456-banco-andino/corridas/salida-bank-reconcile.md`.

Los términos (versión 1.2) ya estaban vigentes y aceptados para la versión 0.8.0. No hizo falta registrar la aceptación a nombre de José Francisco Ñáñez, así que no lo hice.