# /criterio-finance:bank-reconcile 

Las dos cuentas bancarias de septiembre quedan conciliadas y en ninguna hay diferencia sin explicar. La única partida abierta es una consignación en tránsito del último día del mes en andino-4301. Aparte, la cuenta 2205 no tiene auxiliar del periodo, así que no se puede conciliar.

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

- `2026-09/10-contabilidad/auxiliares/`
- `2026-09/20-bancos/andino-4301/auxiliar-libros.csv`

---

Corrida registrada como `2026-10-06-bank-reconcile-1`. Lo que mostré quedó en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-bank-reconcile.md`.