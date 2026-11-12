# /criterio-finance:ledger-check 

En total, el balance de comprobación de septiembre cuadra. Pero el mayor y el balance no coinciden en dos cuentas, la 2505 y la 5195, por el mismo monto y con signo contrario. Eso sugiere un movimiento que está en el mayor y no llegó al balance, y conviene revisarlo antes de cerrar. El reporte no trae ningún saldo contrario a su naturaleza.

# Cuadre del balance y el mayor · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `ledger-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 2505: el mayor suma débitos 360,000.00 y créditos 362,700.00; el balance dice 360,000.00 y 360,000.00 | -2,700.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 8 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5195: el mayor suma débitos 98,730.00 y créditos 0.00; el balance dice 96,030.00 y 0.00 | 2,700.00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.xlsx` fila 14 · `2026-09/10-contabilidad/libro-mayor.csv` |

## El resultado

Débitos 4,397,875.20 · créditos 4,397,875.20 · diferencia 0.00.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad: nombre, identificación fiscal, país y moneda? → Distribuidora del Noroeste, RFC DNO190402B43, México, MXN (sugerida desde el nombre de la carpeta y los CFDI 4.0 del periodo)
- ¿Qué marco contable adoptó la entidad? → NIF del CINIF (sugerida: la mayoría de las no listadas en México, F-20; ningún documento dice otro)
- ¿Cuál es el periodo que se está cerrando? → 2026-09
- ¿Qué cuentas cruzan las facturas? → Ventas 4135; compras 5135, 5145, 5195; IVA generado 2408; IVA descontable 2408 (las que sostienen las facturas del periodo)
- ¿Qué cuentas se concilian contra auxiliar y qué cuentas bancarias se esperan? → 1305 y 2205; bancos andino-4301 y pacifico-4302
- ¿Qué checklist se usa? → El de la organización: 00-referencia/checklist-cierre.csv
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (C-09 del checklist); sin festivos registrados
- ¿Dónde se guarda el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste
- ¿Acepta los términos de esta versión? → Sí, José Francisco Ñáñez, 2026-10-06

## Fuentes

- `2026-09/10-contabilidad/balance-comprobacion.xlsx`
- `2026-09/10-contabilidad/libro-mayor.csv`