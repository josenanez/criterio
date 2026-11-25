# /criterio-risk-appetite:limit-check 

Los términos ya estaban vigentes (versión 1.6), así que no hizo falta registrar la aceptación. El reporte es del periodo 2026-10. Lo copio tal cual del motor.

# Cada exposición contra su límite · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Índice de liquidez de curto prazo: Tesouraria reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 8 | `10-exposicion/exposicao_2026-10.xlsx` fila 3 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | máximo 6 % | 5.8 | no | — | Crédito | 2026-11-06 |
| L-02 | Índice de liquidez de curto prazo | mínimo 120 % | 131 | no | — | Tesouraria | 2026-11-18 |
| L-03 | Concentração no maior devedor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Perdas por fraude externa sobre receitas | máximo 0.5 % | 0.62 | sí | aprobado | Operações | 2026-11-07 |
| L-05 | Exposição a contrapartes sem rating | máximo 15 % | 12 | no | — | Tesouraria | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-exposicion/exposicao_2026-10.xlsx`
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-limit-check-1`. El motor la cuenta con 3 hallazgos, mientras que el reporte solo lista 1 señal en "Lo que hay que atender". No sé qué incluye ese conteo, porque el motor no lo desglosa.

El reporte está en `estado-riesgos/12345678000190-cooperativa-vale-sintetica/apetito/2026-10/reporte-limit-check.md`. Lo que te mostré está guardado en `corridas/salida-limit-check.md`, dentro de esa misma carpeta de estado.