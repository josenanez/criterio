# /criterio-finance:bank-reconcile 

Los términos (versión 1.2) ya estaban vigentes y no hizo falta registrar la aceptación otra vez. Corrí la conciliación de 2026-09 de Almacenes Caribe con fecha de prueba 2026-10-06. Las dos cuentas cierran con diferencia sin explicar de 0,00.

# Conciliación bancaria · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `bank-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Movimientos del extracto sin su registro, o registros sin su movimiento (`bank_unreconciled`) | andino-3701: consignación en tránsito del 2026-09-30 por 8.330.000,00 (SETP99000107) | 8.330.000,00 | — | 0 | `2026-09/20-bancos/andino-3701/auxiliar-libros.csv` fila 17 |
| 2 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | cuenta 2205: no hay auxiliar del periodo para conciliarla | — | — | — | `2026-09/10-contabilidad/auxiliares/` |

## El resultado

| Cuenta | Saldo según banco | Consignaciones en tránsito | Cheques pendientes | Notas crédito sin registrar | Notas débito sin registrar | Saldo según libros | Diferencia sin explicar |
|---|---|---|---|---|---|---|---|
| andino-3701 | 8.040.800,00 | 8.330.000,00 | 0,00 | 0,00 | 0,00 | 16.370.800,00 | 0,00 |
| pacifico-3702 | 24.000.000,00 | 0,00 | 0,00 | 0,00 | 0,00 | 24.000.000,00 | 0,00 |

**andino-3701 · partidas abiertas por antigüedad**

| Fecha | Clase | Referencia | Valor | Días | Tramo |
|---|---|---|---|---|---|
| 2026-09-30 | consignación en tránsito | SETP99000107 | 8.330.000,00 | 0 | 0-30 |

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

- `2026-09/10-contabilidad/auxiliares/`
- `2026-09/20-bancos/andino-3701/auxiliar-libros.csv`

La salida quedó guardada en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-bank-reconcile.md`. La corrida quedó registrada como `2026-10-06-bank-reconcile-1`, con 8 hallazgos.

El motor escribió el reporte en la sesión y no encontré `reporte-bank-reconcile.md` en `cierre/2026-09/`. No lo busqué en disco, así que no sé si está guardado.