# /criterio-risk-appetite:framework-check 

Los términos (versión 1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva. La ficha no trae ninguna declaración de apetito, así que el reporte no pudo contrastarla con el plazo de revisión de la junta.

# El marco y la declaración · Seguros del Sur Sintética · periodo 2026-11

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | Tesorería | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

| Límite | Métrica | Dueño | Próxima revisión |
|---|---|---|---|
| L-01 | Cartera vencida de consumo | Vicepresidencia de crédito | 2027-03-31 |
| L-02 | Indicador de cobertura de liquidez | Tesorería | 2026-06-30 |
| L-03 | Concentración en el mayor deudor | Vicepresidencia de crédito | 2027-03-31 |
| L-04 | Pérdidas por fraude externo sobre ingresos | Operaciones | 2027-06-30 |
| L-05 | Exposición a contrapartes sin calificación | Tesorería | 2027-06-30 |

## Lo que no se pudo procesar

Ningún área reportó su exposición de 2026-11 para L-01, L-02, L-03, L-04 ni L-05. El archivo que hay es `10-exposicion/exposicion_2026-10.xlsx`.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01, F-11

La corrida quedó registrada como `2026-11-25-framework-check-1`, con 3 hallazgos. El reporte está en `apetito/2026-11/reporte-framework-check.md` y lo que te mostré, en `corridas/salida-framework-check.md`.