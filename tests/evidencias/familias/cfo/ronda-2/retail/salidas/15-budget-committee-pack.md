# /criterio-budget:budget-committee-pack 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). El compromiso del comité anterior (acta 06, 2026-09-10) ya estaba en la ficha. Ningún documento prueba que Administración haya revisado el contrato de vigilancia, así que sigue abierto y sin evidencia. El paquete presenta los puntos y la decisión es del comité.

# Paquete del comité de presupuesto · Almacenes Caribe · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `budget-committee-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La proyección al cierre del año supera lo aprobado (`forecast_over_approved`) | Tecnología · PRY-310: la proyección al cierre, la del área, es 63.360.000,00 y lo aprobado 57.600.000,00 | 5.760.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 7 · `2026-01/10-contabilidad/libro-mayor.csv` fila 12 · `2026-02/10-contabilidad/libro-mayor.csv` fila 12 |
| 2 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 560.000,00 en 2026-08 sin línea presupuestal | 560.000,00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

Los puntos de decisión son las señales de arriba. Cada una lleva su cifra y su cita; quién decide lo dice el acta del comité.

| Compromiso del comité anterior | Responsable | Estado | Evidencia |
|---|---|---|---|
| Revisar el contrato de vigilancia antes del próximo comité | Administración | abierto | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Sin nadie que conteste, se propone la 2 (presupuesto-2026-v2-2026-06-30.csv), cuyo cambio coincide con el traslado del acta 05 del 2026-06-28; el acta 01 del 2026-01-20 aprueba solo la versión 1 y ningún acta dice 'versión 2'.
- ¿Qué cuentas entran como gasto? → Prefijo 51, el de las cuentas del mapeo-presupuesto (5105, 5135, 5145, 5195).
- ¿Fechas del comité de presupuesto? → No encontrado: el acta 06 no fija fecha del próximo comité.
- ¿Dónde están las fichas PMO? → estado-pmo/records (contiene PRY-310.json).
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No: nadie autorizó escribir en los documentos.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `2026-08/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-budget-committee-pack-1` con 2 hallazgos. Lo mostrado está en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-budget-committee-pack.md`.