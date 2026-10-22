# /criterio-compliance:regulatory-watch 

Los términos ya estaban vigentes (versión 1.2), así que no hizo falta registrar una aceptación nueva. Dejé el reporte de normas nuevas del periodo 2026-10 y la corrida registrada.

# Normas nuevas · Banco Andino · periodo 2026-10

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.7.0 · **Comando:** `regulatory-watch`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una norma registrada lleva más días de los configurados sin evaluación de impacto (`regulatory_change_unassessed`) | N-2026-05 · Circular sintética 005 de 2026: registrada el 2026-08-14, lleva 53 días sin evaluación de impacto | — | Andrés Vela | 53 | `30-normativa/registro-normativo.csv` fila 4 |

## El resultado

| Id | Norma | Registrada | Aplica | Evaluada |
|---|---|---|---|---|
| N-2026-01 | Resolución sintética 001 de 2026 | 2026-03-10 | sí | sí |
| N-2026-02 | Circular sintética 002 de 2026 | 2026-05-02 | no | sí |
| N-2026-05 | Circular sintética 005 de 2026 | 2026-08-14 | por evaluar | no |

Sin opinión sobre el alcance de ninguna norma: si aplica y qué exige lo decide la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-normativa/registro-normativo.csv`

---

- **Corrida registrada:** `2026-10-06-regulatory-watch-1`. La salida completa quedó en `estado-legal/900123456-banco-andino/corridas/salida-regulatory-watch.md`.
- **Nota de la corrida:** una norma sin evaluar (N-2026-05) y ninguna norma que aplique sin obligación en la matriz.
- **Hallazgos:** el motor reportó 4 al registrar la corrida, y el reporte de arriba muestra una sola señal. No revisé de dónde salen los otros.