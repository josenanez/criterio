# /criterio-budget:budget-scan 

Inventario sin archivos nuevos, cambiados ni borrados (64 documentos). Las 3 actas ya estaban en la ficha y salieron 3 señales.

# Qué cambió en el presupuesto · Almacenes del Plata · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes del Plata (30714520780) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 6.075.000,00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 46.575.000,00 contra 40.500.000,00 aprobado al corte (+15,0 %) | 6.075.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |
| 3 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96,0 % de lo aprobado en el año | -1.425.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 3 · `2026-01/10-contabilidad/libro-mayor.csv` fila 4 · `2026-02/10-contabilidad/libro-mayor.csv` fila 4 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Rige la más reciente de 10-aprobado/ (v2, 2026-06-30), que nace del traslado del acta 05; la v1 la aprobó el acta 01 del 20 de enero. No fijé approved_version.
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma).
- ¿Fechas del comité? → No encontradas en los documentos; quedan vacías.
- ¿Fichas de proyectos PMO? → Encontradas en estado-pmo/records (PRY-310.json).

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

Corrida registrada como `2026-10-06-budget-scan-1` con 3 hallazgos.

Dos cosas sobre cómo corrió:
- Los términos ya estaban vigentes (v1.3, aceptada en la instalación 1.0.0), así que el motor no mostró nada que registrar a nombre de José Francisco Ñáñez.
- El reporte sale con la sección «El resultado» vacía: así lo entregó el motor y no le agregué cifras.