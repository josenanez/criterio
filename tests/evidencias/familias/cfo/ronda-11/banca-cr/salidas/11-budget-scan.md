# /criterio-budget:budget-scan 

Inventario sin archivos nuevos ni cambiados frente a la corrida anterior. Las tres actas de `40-actas/` ya estaban en la ficha, así que no la modifiqué. Aparecieron 4 señales en el corte 2026-09.

# Qué cambió en el presupuesto · Banco del Valle Central (sintético) · presupuesto 2026, corte 2026-09

**Entidad:** Banco del Valle Central (sintético) (3101457812) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 4.050.000,00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %) | 4.050.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado (v2, 2026-06-30); el acta 01 del 2026-01-20 aprueba la v1 y el acta 05 del 2026-06-28 el traslado que origina la v2
- ¿Cuál es el año y el corte? → Presupuesto 2026, corte 2026-09 (último periodo con contabilidad)
- ¿Áreas y responsables? → Áreas tomadas del presupuesto: Administración, Comercial, Operaciones, Personal, Tecnología; responsables no declarados en los documentos
- ¿Umbrales? → Los de config.example.json: desviación 10%, comprometido 95%, proyección vencida 45 días
- ¿Fechas del comité? → Ninguna en los documentos; el acta 06 es del 2026-09-10
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 4 hallazgos. El texto mostrado está en `corridas/salida-budget-scan.md`.

No registré ninguna aceptación de términos, porque ya estaban vigentes (versión 1.3, aceptada con la 1.0.0). El comando `reporte` guardó el informe del motor en `presupuesto/2026/reporte-budget-scan.md`.