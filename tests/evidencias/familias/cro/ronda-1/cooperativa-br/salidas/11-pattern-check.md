# /criterio-risk-events:pattern-check 

Corrí `pattern-check` sobre el periodo 2026-10 con fecha de corte 2026-11-25. Los términos ya estaban vigentes y registrados a nombre de José Francisco Ñáñez, así que no hizo falta aceptarlos de nuevo.

# Lo que se repite · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `pattern-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidade: el riesgo R-09 no está en la matriz | 9.800.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riscos.xlsx` |

## El resultado

**Eventos sin un riesgo de la matriz:** EV-04.

Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riscos.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-pattern-check-1`. El motor reporta 3 hallazgos, aunque el reporte solo muestra uno.