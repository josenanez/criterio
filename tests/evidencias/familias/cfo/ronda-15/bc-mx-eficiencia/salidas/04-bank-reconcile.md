# /criterio-finance:bank-reconcile 

Conciliación de 2026-09: dos cuentas conciliadas con diferencia sin explicar en cero; una partida abierta en andino-4301 y la cuenta 2205 sin auxiliar del periodo.

# Conciliación bancaria · Distribuidora del Noroeste · periodo 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-4301: consignación en tránsito del 2026-09-30 por 151,380.00 (A000107) | 151,380.00 | — | 0 | `2026-09/20-bancos/andino-4301/auxiliar-libros.csv` fila 16 |
| 2 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | cuenta 2205: no hay auxiliar del periodo para conciliarla | — | — | — | `2026-09/10-contabilidad/auxiliares/` |

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-4301 | 164,232.00 | 151,380.00 | 0.00 | 0.00 | 0.00 | 315,612.00 | 0.00 |
| pacifico-4302 | 540,000.00 | 0.00 | 0.00 | 0.00 | 0.00 | 540,000.00 | 0.00 |

**andino-4301 · partidas abiertas por antigüedad**

| Fecha | Clase | Referencia | Valor | Días | Tramo |
|---|---|---|---|---|---|
| 2026-09-30 | consignación en tránsito | A000107 | 151,380.00 | 0 | 0-30 |

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
- `2026-09/20-bancos/andino-4301/auxiliar-libros.csv`

La salida quedó en `corridas/salida-bank-reconcile.md` y la corrida se registró como `2026-10-06-bank-reconcile-1`.

Los términos ya estaban vigentes (aceptados en la versión 1.5.4), así que no hubo que registrar de nuevo la aceptación de José Francisco Ñáñez.