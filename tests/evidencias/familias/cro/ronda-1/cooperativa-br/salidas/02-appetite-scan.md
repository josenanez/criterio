# /criterio-risk-appetite:appetite-scan 

Los 11 documentos llegan por primera vez al inventario. La ficha del periodo ya recogía lo que dicen la declaración y el acta. Del acta solo cuenta como aprobación de exceso la de L-04. Para L-03 el comité dice que "toma conocimiento" del plan, y eso no es una aprobación.

# Qué cambió en el apetito · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `appetite-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco (`appetite_statement_outdated`) | Declaração de apetite por riscos: la junta la revisó el 2025-08-28, y el marco pide revisarla cada 12 meses: tocaba el 2026-08-28 | — | — | 89 | `00-marco/declaracao_de_apetite.pdf` |
| 2 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Índice de liquidez de curto prazo: Tesouraria reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 8 | `10-exposicion/exposicao_2026-10.xlsx` fila 3 |
| 3 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Índice de liquidez de curto prazo: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Límites en el marco:** 5 · **Con exposición reportada:** 5 · **Excedidos:** 2 · **Riesgos altos o críticos en la matriz:** 5 · **Excesos aprobados en las actas:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/declaracao_de_apetite.pdf`
- `00-marco/limites.xlsx`
- `10-exposicion/exposicao_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)