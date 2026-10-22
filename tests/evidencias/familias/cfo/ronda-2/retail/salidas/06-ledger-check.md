# /criterio-finance:ledger-check 

Los términos vigentes (versión 1.2) ya estaban aceptados por José Francisco Ñáñez el 2026-10-06. El cuadre del periodo 2026-09 encontró dos cuentas donde el mayor no coincide con el balance.

# Cuadre del balance y el mayor · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `ledger-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 2505: el mayor suma débitos 16.000.000,00 y créditos 16.120.000,00; el balance dice 16.000.000,00 y 16.000.000,00 | -120.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 8 · `2026-09/10-contabilidad/libro-mayor.csv` |
| 2 | El saldo de una cuenta en el mayor no es el del balance de comprobación (`ledger_vs_trial_balance`) | cuenta 5195: el mayor suma débitos 4.388.000,00 y créditos 0,00; el balance dice 4.268.000,00 y 0,00 | 120.000,00 | — | — | `2026-09/10-contabilidad/balance-comprobacion.csv` fila 14 · `2026-09/10-contabilidad/libro-mayor.csv` |

## El resultado

Débitos 204.788.080,00 · créditos 204.788.080,00 · diferencia 0,00.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su NIT, país y moneda? → Almacenes Caribe, NIT 900765432, Colombia, COP (de la carpeta; sesión sin interfaz)
- ¿Qué marco contable aplica? → No encontrado en los documentos: queda «por confirmar»
- ¿Cuál es el periodo que se está cerrando? → 2026-09 (el último con 10-contabilidad)
- ¿Qué prefijos de cuentas cruzan las facturas? → Ventas 41, compras 14/51/52/61, IVA generado y descontable 2408 (los habituales; el balance tiene 4135, 5105-5305 y 2408)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205; bancos andino-3701 y pacifico-3702 (las carpetas de 20-bancos). Solo existe auxiliar de 1305
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada, queda como no aprobado
- ¿Quién aprueba el cierre y qué festivos hay? → Sofía León (Contraloría, responsable de C-09 en el checklist); festivo 2026-10-12 (el del ejemplo, sin confirmar)
- ¿Dónde se guarda el estado? → estado-finanzas/900765432-almacenes-caribe
- ¿Se acepta el texto de los términos? → Sí, José Francisco Ñáñez, 2026-10-06 (indicado en la sesión de prueba)

## Fuentes

- `2026-09/10-contabilidad/balance-comprobacion.csv`
- `2026-09/10-contabilidad/libro-mayor.csv`

La corrida quedó registrada como `2026-10-06-ledger-check-1`.