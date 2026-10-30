# /criterio-budget:budget-scan 

Corrida sin archivos nuevos ni cambiados (0 nuevos, 0 cambiados, 0 borrados); las 3 actas de `40-actas/` ya estaban en la ficha. El motor marcó 5 señales.

# Qué cambió en el presupuesto · Minera del Motagua · presupuesto 2026, corte 2026-09

**Entidad:** Minera del Motagua (89090314) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 120,000.00 entre la versión 1 y la 2 sin acta que lo apruebe | 120,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -120,000.00 entre la versión 1 y la 2 sin acta que lo apruebe | -120,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx: Comercial · Eventos usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx` fila 3 |
| 4 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx: Comercial · Publicidad usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx` fila 2 |
| 5 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

(El reporte del motor trae esta sección vacía.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Sugerida por los documentos: la más reciente de 10-aprobado/ (v2, 2026-06-30), que nace del traslado del acta 05; el acta 01 (2026-01-20) aprueba la v1.
- ¿Umbrales? → Los de config.example.json (10 %, 95 %, 45 días), como configuración y no como norma.
- ¿Fechas del comité? → Ningún documento da la fecha del próximo comité; queda vacío.
- ¿Dónde están las fichas PMO? → estado-pmo/records (PRY-310.json).

## Fuentes

- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

Tres aclaraciones:
- **Términos:** ya estaban vigentes (versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-06). El agente no los mostró de nuevo ni se registró otra aceptación.
- **Sección "El resultado":** el motor la generó vacía y la dejé así. Escribí esa línea entre paréntesis en esta respuesta, pero no en el archivo guardado.
- **Registro:** el reporte del motor está en `presupuesto/2026/reporte-budget-scan.md` y lo que te mostré en `corridas/salida-budget-scan.md`. La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 5 hallazgos.