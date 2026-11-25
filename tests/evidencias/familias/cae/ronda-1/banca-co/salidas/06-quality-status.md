# /criterio-audit-plan:quality-status 

La evaluación externa de calidad de Banco Andino Sintético está vencida. Los términos estaban vigentes (versión 1.6, aceptación 0.1.0), así que corrí el reporte con `--today 2026-11-24`.

# La evaluación externa de calidad · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `quality-status`

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

---

- **Dónde quedó:** el motor escribió el reporte en `estado-auditoria/901777321-banco-andino-sintetico/plan/2026-11/reporte-quality-status.md`. La salida está en `corridas/salida-quality-status.md`.
- **Corrida registrada:** `2026-11-24-quality-status-1`.
- **Qué falta:** decidir cuándo se contrata la evaluación externa es del responsable de auditoría y el consejo. Este comando solo señala el vencimiento.