# /criterio-risk-events:pattern-check 

Los términos están vigentes (versión 1.6, aceptada por José Francisco Ñáñez el 2026-11-25). El período 2026-10 salió de la configuración. El reporte es del motor y no le cambié nada.

# Lo que se repite · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `pattern-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Fraude com cartão» en Canais: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40.600.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 2 · `30-eventos/base_de_eventos.xlsx` fila 3 |
| 2 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-42 · Sanção por tratamento de dados: el riesgo R-08 no está en la matriz | 12.000.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 14 · `00-marco/matriz_de_riscos.xlsx` |
| 3 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidade: el riesgo R-09 no está en la matriz | 9.800.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riscos.xlsx` |
| 4 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Falta de numerário» en Agências: 2 eventos en los últimos 12 meses (EV-321, EV-322), del 2026-04-10 al 2026-09-05 | 5.000.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 12 · `30-eventos/base_de_eventos.xlsx` fila 13 |

## El resultado

| Proceso | Tipo de evento | Eventos en 12 meses | Monto |
|---|---|---|---|
| Agências | Falta de numerário | EV-321, EV-322 | 5,000,000 |
| Canais | Fraude com cartão | EV-01, EV-02 | 40,600,000 |

**Eventos sin un riesgo de la matriz:** EV-04, EV-42.

Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riscos.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-pattern-check-1`. La salida completa está en `corridas/salida-pattern-check.md` y el reporte del motor en `eventos/2026-10/reporte-pattern-check.md`.