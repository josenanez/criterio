# /criterio-budget:budget-committee-pack 

Paquete del comité con 5 puntos de decisión y 1 compromiso del comité anterior, abierto y sin evidencia. El paquete no recomienda: la decisión es del comité.

# Paquete del comité de presupuesto · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `budget-committee-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 4.050.000,00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %) | 4.050.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |
| 5 | El presupuesto de un proyecto en su ficha no es el que tiene asignado el área (`project_budget_mismatch`) | PRY-310: la ficha del proyecto dice 64.800.000,00 y el área tiene asignado 72.000.000,00 | -7.200.000,00 | — | — | `PRY-310.json` · `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 7 |

## El resultado

Los puntos de decisión son las señales de arriba. Cada una lleva su cifra y su cita; quién decide lo dice el acta del comité.

| Compromiso del comité anterior | Responsable | Estado | Evidencia |
|---|---|---|---|
| Revisar el contrato de vigilancia antes del próximo comité | Administración | abierto | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La 1: el acta 01 del 2026-01-20 es la única que aprueba una versión. La v2 (2026-06-30) no tiene acta de aprobación; el acta 05 solo aprueba un traslado de 3,000,000.00.
- ¿Quién es el responsable de cada área? → No encontrado en los documentos; sin responsable asignado.
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- ¿Fechas del comité de presupuesto? → No encontradas; el acta 06 habla de «el próximo comité» sin fecha.
- ¿Fichas PMO? → estado-pmo/records, con PRY-310.json.
- ¿Marcar la carpeta con _CRITERIO_FINANZAS.txt? → No: nadie lo autorizó; no se escribió nada en los documentos.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `PRY-310.json`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

---
Corrida registrada como `2026-10-06-budget-committee-pack-1` (5 hallazgos). El reporte quedó en `estado-finanzas/900123456-banco-andino/presupuesto/2026/reporte-budget-committee-pack.md`, y esta salida en `estado-finanzas/900123456-banco-andino/corridas/salida-budget-committee-pack.md`.

Dos cosas del proceso:
- Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez el 2026-10-06, así que no hubo que registrar nada.
- La ficha ya traía el compromiso del acta 06 como abierto. Busqué «vigilancia» en las carpetas de documentos y de PMO y no hay nada que pruebe la revisión, así que lo dejé abierto y sin evidencia.