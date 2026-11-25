# /criterio-risk-events:events-wake 

Hoy tocaba la revisión semanal de los indicadores y los eventos, así que corrí el escaneo. Los términos estaban vigentes, no había peticiones abiertas y ningún documento era nuevo ni había cambiado. El acta del comité acuerda una sola acción sobre un indicador, la de KRI-01, y ya estaba en la ficha del periodo.

# Qué cambió en los eventos · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `events-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-05 · Queda do canal digital: se descubrió el 2026-07-01 y se registró el 2026-08-20; la política da 30 días | 31.000.000,00 | — | 20 | `30-eventos/base_de_eventos.xlsx` fila 6 |
| 2 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidade: el riesgo R-09 no está en la matriz | 9.800.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riscos.xlsx` |
| 3 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotatividade da equipe de crédito: no tiene valor en 2026-10 | — | Diretoria de crédito | — | `00-marco/indicadores_chave.xlsx` fila 4 |

## El resultado

**Indicadores clave de riesgo:** 5 · **En alerta o en su límite:** 2 · **Eventos en la base:** 8 · **Acciones tomadas de las actas:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_chave.xlsx`
- `00-marco/matriz_de_riscos.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

Dejé registradas las dos corridas con el caso 2026-10: `2026-11-25-events-scan-2` y `2026-11-25-events-wake-1`. Lo que se mostró quedó guardado en `<espacio>/estado-riesgos/12345678000190-cooperativa-vale-sintetica/corridas/salida-events-scan.md` y en `<espacio>/estado-riesgos/12345678000190-cooperativa-vale-sintetica/corridas/salida-events-wake.md`.

Un aviso sobre la sesión: no había herramienta Glob, así que busqué los archivos con `find`.