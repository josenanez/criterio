# /criterio-finance:ledger-check 

Términos vigentes (versión 1.2, aceptada por José Francisco Ñáñez el 2026-10-06). El balance de septiembre no cuadra: hay una diferencia entre débitos y créditos, y la señala una sola cuenta, la 5305.

# Cuadre del balance y el mayor · Banco Andino · periodo 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.7.0 · **Aprueba:** Sofía León · **Comando:** `ledger-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: el mayor suma débitos 0,00 y créditos 0,00; el balance dice 5.000,00 y 0,00 | -5.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 15 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5305: saldo inicial más movimientos no da el saldo final (5.000,00) | 5.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 15 |
| 3 | Los débitos y los créditos del balance de comprobación no suman lo mismo (`trial_balance_unbalanced`) | débitos 253.437.700,00 y créditos 253.432.700,00: diferencia 5.000,00 | 5.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` |

## El resultado

Débitos 253.437.700,00 · créditos 253.432.700,00 · diferencia 5.000,00.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su NIT, país y moneda? → Banco Andino, NIT 900123456, Colombia, COP (de la carpeta finanzas/900123456-banco-andino)
- ¿Qué marco contable aplica? → Grupo 1 (F-05); solo se registra
- ¿Cuál es el periodo que se está cierrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué prefijos cruzan las facturas? → Ventas 41; compras 14, 51, 52, 61; IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (las que tienen auxiliar); bancos andino-1101 y pacifico-1102 (carpetas de 20-bancos)
- ¿Qué checklist se usa y está aprobado? → El de la organización (00-referencia/checklist-cierre.csv); sin aprobación documentada, queda como no aprobado
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (responsable de C-09); festivo 2026-10-12
- ¿Dónde se guarda el estado? → estado-finanzas/900123456-banco-andino
- ¿Acepta los términos vigentes? → Sí, José Francisco Ñáñez, versión 1.2, 2026-10-06 (dado en el encargo de la prueba)
- ¿Se deja el archivo _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No; nadie autorizó escribir dentro de los documentos

## Fuentes

- `2026-09/10-contabilidad/balance-comprobacion.csv`
- `2026-09/10-contabilidad/libro-mayor.csv`

---
Corrida registrada como `2026-10-06-ledger-check-1`.