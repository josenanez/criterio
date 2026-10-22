# /criterio-finance:account-reconcile 

Se concilió la cuenta 1305 contra su auxiliar. La cuenta 2205 no tiene auxiliar del periodo, y el reporte la señala como conciliación desactualizada.

# Conciliación de cuentas · Almacenes Caribe · periodo 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `account-reconcile`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La conciliación de una cuenta no se actualizó en el periodo (`reconciliation_stale`) | cuenta 2205: no hay auxiliar del periodo para conciliarla | — | — | — | `2026-09/10-contabilidad/auxiliares/` |

## El resultado

| Cuenta | Nombre | Saldo según mayor | Saldo según auxiliar | Diferencia | 0–30 | 31–60 | 61–90 | Más de 90 |
|---|---|---|---|---|---|---|---|---|
| 1305 | Clientes | 22.982.000,00 | 22.982.000,00 | 0,00 | 21.182.000,00 | 1.800.000,00 | 0,00 | 0,00 |

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

La corrida quedó registrada como `2026-10-06-account-reconcile-1`.