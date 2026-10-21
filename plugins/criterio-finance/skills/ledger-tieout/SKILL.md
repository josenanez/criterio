---
name: ledger-tieout
description: "El cuadre del balance de comprobación y del libro mayor: débitos contra créditos, saldo inicial más movimientos contra saldo final, el mayor contra el balance cuenta por cuenta y los saldos contrarios a la naturaleza. Úsalo al revisar el cuadre del periodo o explicar una diferencia de una cuenta. Trial balance, general ledger tie-out."
---

# El cuadre

El balance de comprobación (`10-contabilidad/balance-comprobacion`) y el libro mayor (`10-contabilidad/libro-mayor`) del periodo, contra sí mismos y entre ellos:

- **Débitos contra créditos** del balance. Si no suman lo mismo, `trial_balance_unbalanced`.
- **Saldo inicial más débitos menos créditos contra saldo final**, cuenta por cuenta.
- **El mayor contra el balance**, cuenta por cuenta: los movimientos del mayor de cada cuenta hoja del balance —incluidas sus subcuentas— contra sus débitos y créditos. Una cuenta con movimientos en el mayor que no está en el balance también es diferencia. Todo eso es `ledger_vs_trial_balance`.
- **Saldos contrarios a la naturaleza** que declara el plan de cuentas de la organización (`00-referencia/plan-de-cuentas`, columna `naturaleza` con D o C). No es una señal: se lista, porque puede tener explicación.

La tolerancia es la de la configuración; si no la fija, la del país: en Colombia, la holgura de ±2,00 que el anexo técnico de la DIAN permite en valores monetarios (F-01, 5.2.1.1).

Clara no registra ni corrige asientos.
