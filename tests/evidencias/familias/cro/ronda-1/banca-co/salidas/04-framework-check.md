# /criterio-risk-appetite:framework-check 

El marco de Banco Andino Sintético (901777333) tiene dos señales abiertas, las dos sobre L-02. La declaración de apetito no figura en la ficha del periodo, así que el reporte no trae su fecha de revisión.

Los términos (versión 1.6) ya estaban vigentes en la configuración, así que no registré ninguna aceptación nueva. Corrí todo con `--today 2026-11-25`.

# El marco y la declaración · Banco Andino Sintético · periodo 2026-11

**Fecha de corte:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Indicador de cobertura de liquidez: el límite no tiene un dueño que responda por él | — | `00-marco/limites.xlsx` fila 3 |
| 2 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

| Límite | Métrica | Dueño | Próxima revisión |
|---|---|---|---|
| L-01 | Cartera vencida de consumo | Vicepresidencia de crédito | 2027-03-31 |
| L-02 | Indicador de cobertura de liquidez | — | 2026-06-30 |
| L-03 | Concentración en el mayor deudor | Vicepresidencia de crédito | 2027-03-31 |
| L-04 | Pérdidas por fraude externo sobre ingresos | Operaciones | 2027-06-30 |
| L-05 | Exposición a contrapartes sin calificación | Tesorería | 2027-06-30 |

Quién es el dueño de un límite y cuándo se revisa lo fija el marco: aquí se dice cuál falta o se venció.

## Lo que no se pudo procesar

- `10-exposicion/exposicion_2026-10.xlsx`: ningún área reportó su exposición de 2026-11 para L-01, L-02, L-03, L-04 ni L-05.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01, F-10 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-framework-check-1`, con 6 hallazgos. La salida está en `estado-riesgos/901777333-banco-andino-sintetico/corridas/salida-framework-check.md`.