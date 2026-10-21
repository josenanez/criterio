---
name: reconciliation
description: "Cómo concilia el motor: el extracto contra el auxiliar de libros en tres pasadas, la clasificación de cada partida abierta, la antigüedad, y el mayor contra el auxiliar de cada cuenta. Úsalo al conciliar bancos o cuentas, al explicar una partida abierta o una diferencia sin explicar. Bank reconciliation, account reconciliation, aging."
---

# La conciliación

## Bancos

Una carpeta por cuenta en `<AAAA-MM>/20-bancos/`, `<banco>-<últimos 4 dígitos>`, con el **extracto** y el **auxiliar de libros** del periodo. Cada movimiento con fecha, valor (o débito y crédito), referencia y, si la trae, saldo.

El motor cruza en tres pasadas, y ninguna se salta:

1. **Referencia exacta y valor.**
2. **Valor y fecha** dentro de la ventana de `bank_match_window_days` (5 días por defecto); si hay varias, la más cercana.
3. **Valor solo**, cuando es único de los dos lados.

Lo que queda abierto se clasifica:

| Queda en | Valor | Es |
|---|---|---|
| Libros, no en el banco | positivo | consignación en tránsito |
| Libros, no en el banco | negativo | cheque pendiente de cobro |
| Banco, no en libros | positivo | nota crédito sin registrar |
| Banco, no en libros | negativo | nota débito sin registrar |

Saldo según banco más consignaciones en tránsito menos cheques pendientes debe ser igual a saldo según libros más notas crédito menos notas débito sin registrar. **La diferencia sin explicar debe ser cero**; si no lo es, hay un cruce que no cerró y se señala.

Cada partida abierta es `bank_unreconciled`; si además lleva más de `reconciling_item_days` (30 por defecto) a la fecha de corte, `reconciling_item_aged`. La antigüedad se muestra en tramos de 0–30, 31–60, 61–90 y más de 90 días. Una cuenta sin extracto o sin auxiliar del periodo es `reconciliation_stale`.

## Cuentas contra auxiliares

Un archivo por cuenta en `10-contabilidad/auxiliares/`, con el número de la cuenta al inicio del nombre, y una fila por partida abierta con su valor. El saldo del balance contra la suma del auxiliar; la diferencia mayor que la tolerancia es `account_unreconciled`, y una cuenta de `accounts.reconcile` sin auxiliar es `reconciliation_stale`.

## Lo que no se hace

No se propone el asiento que cuadra una diferencia, ni se reclasifica una partida: se muestra y la decide una persona.
