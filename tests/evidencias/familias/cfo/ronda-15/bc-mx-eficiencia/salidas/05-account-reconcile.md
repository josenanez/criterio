# /criterio-finance:account-reconcile 

La conciliación de cuentas de 2026-09 quedó corrida: la cuenta 1305 cuadra y la 2205 no se pudo conciliar. Los términos estaban vigentes (versión 1.5, aceptada en 1.5.4), así que no hubo que registrar la aceptación de nuevo.

# Conciliación de cuentas · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | cuenta 2205: no hay auxiliar del periodo para conciliarla | — | — | — | `2026-09/10-contabilidad/auxiliares/` |

## El resultado

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |
|---|---|---|---|---|---|---|---|---|
| 1305 | Clientes | 398,700.00 | 398,700.00 | 0.00 | 313,200.00 | 85,500.00 | 0.00 | 0.00 |

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

- `2026-09/10-contabilidad/auxiliares/`

La corrida quedó registrada como `2026-10-06-account-reconcile-1`, con la salida guardada en `corridas/salida-account-reconcile.md`.