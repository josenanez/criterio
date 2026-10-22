# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (57 documentos). Se releyeron las 3 actas y la ficha ya las recoge. Salen 5 señales; dos son cambios de la v2 del presupuesto sin acta que los apruebe.

# Qué cambió en el presupuesto · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto y 1 línea no lo sostiene: Servicios públicos | 4.050.000,00 | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 4.800.000,00 | `presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026-v1-2026-01-15.csv` |
| 3 | Ídem (`transfer_without_approval`) | Tecnología · Licencias: cambió -4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -4.800.000,00 | los mismos dos CSV |
| 4 | Lo ejecutado se aparta del presupuesto más del umbral (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %) | 4.050.000,00 | v2 fila 2 · libro mayor 2026-01 y 2026-02, fila 2 |
| 5 | El presupuesto de un proyecto en su ficha no es el que tiene asignado el área (`project_budget_mismatch`) | PRY-310: la ficha del proyecto dice 64.800.000,00 y el área tiene asignado 72.000.000,00 | -7.200.000,00 | `PRY-310.json` · v2 fila 7 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La 1: el acta 01 del 2026-01-20 es la única que aprueba una versión. La v2 (2026-06-30) no tiene acta de aprobación; el acta 05 solo aprueba un traslado de 3,000,000.00.
- ¿Quién es el responsable de cada área? → No encontrado en los documentos.
- ¿Umbrales? → Desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- ¿Fechas del comité de presupuesto? → No encontradas; el acta 06 habla de «el próximo comité» sin fecha.
- ¿Fichas PMO? → `estado-pmo/records`, con PRY-310.json.
- ¿Marcar la carpeta con `_CRITERIO_FINANZAS.txt`? → No: nadie lo autorizó.

## Fuentes

Los dos libros mayores (2026-01 y 2026-02), `PRY-310.json`, las versiones v1 y v2 del presupuesto y `correo-administracion.md`.

---
En esta versión del reporte abrevié las citas y la columna «Responsable»/«Días» (vacías en las cinco filas). El reporte completo del motor está en `estado-finanzas/900123456-banco-andino/presupuesto/2026/reporte-budget-scan.md`. La corrida quedó registrada como `2026-10-06-budget-scan-1`. Los términos v1.2 ya estaban aceptados a nombre de José Francisco Ñáñez (2026-10-06), así que no hizo falta registrarlos otra vez.

Una aclaración: en `salida-budget-scan.md` quedó el reporte completo del motor tal cual, no la versión abreviada de arriba.