# /criterio-budget:budget-scan 

Los términos están vigentes (los aceptó José Francisco Ñáñez el 2026-10-06). Frente a la corrida anterior no hay archivos nuevos, cambiados ni borrados. Las tres actas ya estaban en la ficha tal como las dicen, y el cálculo no encontró nada que corregir en ella. Queda una señal. La sección «El resultado» viene vacía porque el motor no escribió nada en ella.

# Qué cambió en el presupuesto · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Distribuidora del Noroeste (RFC DNO190402B43), 2026 — tomado de la configuración de Clara y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → La vigente es la 2 (la más reciente de 10-aprobado/); la 1 la aprueba el acta 01 del 2026-01-20 y la 2 nace del traslado del acta 05
- ¿Quién responde por cada área? → No sé — ningún documento lo dice
- ¿Umbrales? → Los propuestos: desviación 10 %, comprometido 95 %, proyección vencida a 45 días
- ¿Fechas del comité de presupuesto? → Ninguna fijada en los documentos
- ¿Dónde están las fichas PMO? → estado-pmo/records (PRY-310)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste, el mismo que usa Clara

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

---

La salida quedó guardada en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-budget-scan.md` y la corrida quedó registrada como `2026-10-06-budget-scan-1`, con 1 hallazgo.