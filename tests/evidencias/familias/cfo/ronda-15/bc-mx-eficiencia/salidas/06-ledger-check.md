# /criterio-finance:ledger-check 

Los débitos y los créditos cuadran. Dos cuentas, 2505 y 5195, no coinciden entre el mayor y el balance de comprobación, y las dos diferencias van en sentido contrario. El reporte las lista para que alguien las mire.

Los términos (versión 1.5) ya estaban vigentes, así que no registré ninguna aceptación nueva.

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

- `2026-09/10-contabilidad/balance-comprobacion.xlsx`
- `2026-09/10-contabilidad/libro-mayor.csv`

La corrida quedó registrada como `2026-10-06-ledger-check-1`, y lo mostrado está guardado en `corridas/salida-ledger-check.md`.