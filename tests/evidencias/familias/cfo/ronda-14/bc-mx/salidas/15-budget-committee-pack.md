# /criterio-budget:budget-committee-pack 

El compromiso que dejó el comité del 10 de septiembre de 2026 (acta 06) ya estaba anotado en la ficha. Ningún documento de la carpeta muestra que se haya revisado el contrato de vigilancia, así que sigue «abierto», sin evidencia.
El motor encontró un solo punto para que decida el comité. Este paquete no propone qué decidir; el comité decide y lo deja en su acta.

# Paquete del comité de presupuesto · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `budget-committee-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

Los puntos de decisión son las señales de arriba. Cada una lleva su cifra y su cita; quién decide lo dice el acta del comité.

| Compromiso del comité anterior | Responsable | Estado | Evidencia |
|---|---|---|---|
| Administración revisa el contrato de vigilancia antes del próximo comité | Administración | abierto | — |

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