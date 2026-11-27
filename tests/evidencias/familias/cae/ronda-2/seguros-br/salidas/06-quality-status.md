# /criterio-audit-plan:quality-status 

La evaluación externa de calidad de Seguradora Atlântica Sintética está vencida. Los términos estaban vigentes (versión 1.6), así que no hizo falta registrar una aceptación nueva.

# La evaluación externa de calidad · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.2.2 · **Comando:** `quality-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La última evaluación externa de calidad tiene más de cinco años (norma 8.4) (`external_assessment_overdue`) | la última evaluación externa de calidad fue el 2021-03-31; la siguiente tocaba a más tardar el 2026-03-28 (norma 8.4) | — | — | 241 | `00-referencia/metodologia-de-auditoria.pdf` |

## El resultado

**Última evaluación externa de calidad:** 2021-03-31 · **La siguiente, a más tardar:** 2026-03-28 (norma 8.4: al menos una vez cada cinco años).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/metodologia-de-auditoria.pdf`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

La corrida quedó registrada como `2026-11-24-quality-status-1`. El texto mostrado está en `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-quality-status.md`. El reporte del motor está en `plan/2026-11/reporte-quality-status.md`, dentro de la misma carpeta de estado.

Dos notas sobre la corrida:
- Pasé `--today 2026-11-24` al motor, como pediste. El calendario de la sesión marca el 2026-11-26, pero el reporte usa la fecha de la prueba.
- Creé por error una carpeta vacía `corridas` dentro de `.criterio/plan/…` y la borré enseguida.