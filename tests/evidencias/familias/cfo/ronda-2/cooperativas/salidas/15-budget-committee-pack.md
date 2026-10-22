# /criterio-budget:budget-committee-pack 

Paquete del comité de presupuesto de Cooperativa Sierra Alta, con corte a septiembre de 2026. El acta 06 deja un compromiso abierto, sin evidencia. El paquete no recomienda la decisión: presenta cada punto con su cifra y su cita, y la decisión es del comité.

# Paquete del comité de presupuesto · Cooperativa Sierra Alta · presupuesto 2026, corte 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Comité de presupuesto · **Comando:** `budget-committee-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv: Comercial · Eventos usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv` fila 3 |
| 2 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv: Comercial · Publicidad usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv` fila 2 |
| 3 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Tecnología · Licencias: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -2,390.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 6 · `2026-01/10-contabilidad/libro-mayor.csv` fila 10 · `2026-02/10-contabilidad/libro-mayor.csv` fila 10 |
| 4 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

Los puntos de decisión son las señales de arriba. Cada una lleva su cifra y su cita; quién decide lo dice el acta del comité.

| Compromiso del comité anterior | Responsable | Estado | Evidencia |
|---|---|---|---|
| Revisar el contrato de vigilancia antes del próximo comité | Administración | abierto | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Cooperativa Sierra Alta (RUC 1790012345001), presupuesto 2026; tomado del nombre de la carpeta y de presupuesto-2026/
- ¿Cuál es la versión aprobada y su acta? → El acta 01 (2026-01-20) aprueba la versión 1; el acta 05 (2026-06-28) aprueba un traslado de 3,000.00 que coincide con la versión 2 (2026-06-30), pero ningún acta nombra esa versión. Se registró lo que dicen las actas.
- ¿Áreas y responsables? → No encontrado: ningún documento nombra a los responsables de las áreas. Áreas tomadas del mapeo: Administración, Comercial, Tecnología, Operaciones, Personal.
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité? → No encontrado en los documentos; quedó vacío
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Dónde se guarda lo que se encuentra? → estado-finanzas/1790012345001-cooperativa-sierra-alta, fuera de la carpeta de documentos
- ¿Términos? → Aceptados por José Francisco Ñáñez, 2026-10-06, versión 1.2

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

La corrida quedó registrada como `2026-10-06-budget-committee-pack-1` con 4 hallazgos. Lo mostrado está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/corridas/salida-budget-committee-pack.md`.

Los términos ya estaban vigentes (versión 1.2, aceptada por José Francisco Ñáñez el 2026-10-06), así que no hizo falta registrarlos de nuevo. La ficha ya traía el compromiso del acta 06 tal como está en el acta, y no la modifiqué.