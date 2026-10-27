# /criterio-budget:budget-scan 

Términos vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-06). El inventario no trae archivos nuevos ni cambiados, y las tres actas (01, 05 y 06) y el correo de Administración ya estaban en la ficha, así que no extraje nada. El motor levantó 4 señales.

# Qué cambió en el presupuesto · Banco Valle de Anáhuac · presupuesto 2026, corte 2026-09

**Entidad:** Banco Valle de Anáhuac (BVA150301K21) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.11.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 81,000.00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 96,000.00 entre la versión 1 y la 2 sin acta que lo apruebe | 96,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -96,000.00 entre la versión 1 y la 2 sin acta que lo apruebe | -96,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 621,000.00 contra 540,000.00 aprobado al corte (+15.0 %) | 81,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado/: la v2 del 2026-06-30, que nace del traslado del acta 05; la v1 fue aprobada en el acta 01 del 2026-01-20
- ¿Cuál es la entidad y el año presupuestal? → Banco Valle de Anáhuac (BVA150301K21), presupuesto 2026, corte 2026-09
- ¿Dónde está el mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Qué umbrales se usan? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida a 45 días (configuración, no norma)
- ¿Fechas del comité de presupuesto? → No encontradas en los documentos; la última acta de comité es del 2026-09-10
- ¿Dónde están las fichas de proyectos PMO? → estado-pmo/records (contiene PRY-310.json)
- ¿Dónde se guarda lo que se encuentra? → estado-finanzas/BVA150301K21-banco-valle-de-anahuac

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con la salida en `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/corridas/salida-budget-scan.md`.