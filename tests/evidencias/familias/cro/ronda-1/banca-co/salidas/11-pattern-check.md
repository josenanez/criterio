# /criterio-risk-events:pattern-check 

Corrí `pattern-check` para Banco Andino Sintético (901777333), periodo 2026-10, con fecha 2026-11-25. Hay dos señales abiertas. Los términos (versión 1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva.

# Lo que se repite · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `pattern-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40.600.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 2 · `30-eventos/base_de_eventos.xlsx` fila 3 |
| 2 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidad: el riesgo R-09 no está en la matriz | 9.800.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riesgos.xlsx` |

## El resultado

| Proceso | Tipo de evento | Eventos en 12 meses | Monto |
|---|---|---|---|
| Canales | Fraude con tarjeta | EV-01, EV-02 | 40,600,000 |

**Eventos sin un riesgo de la matriz:** EV-04.

Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

El reporte quedó en `estado-riesgos/901777333-banco-andino-sintetico/eventos/2026-10/reporte-pattern-check.md`. Copié lo mostrado, entero, a `corridas/salida-pattern-check.md`. La corrida quedó registrada como `2026-11-25-pattern-check-1`, con 6 hallazgos.