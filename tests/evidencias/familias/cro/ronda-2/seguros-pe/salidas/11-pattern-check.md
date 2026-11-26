# /criterio-risk-events:pattern-check 

Los términos (versión 1.6) ya estaban vigentes, así que no hizo falta registrar la aceptación. No se hizo ninguna pregunta. Tomé el periodo 2026-10 (el mes anterior a la fecha de la prueba) porque nadie podía indicarlo.

# Lo que se repite · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra 0.2.0 · **Comando:** `pattern-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Evento repetido en el mismo proceso (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40,600,000.00 | `base_de_eventos.xlsx` filas 2 y 3 |
| 2 | Evento sin riesgo en la matriz (`loss_event_risk_unmapped`) | EV-42 · Sanción por tratamiento de datos: el riesgo R-08 no está en la matriz | 12,000,000.00 | `base_de_eventos.xlsx` fila 14 · `matriz_de_riesgos.xlsx` |
| 3 | Evento sin riesgo en la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidad: el riesgo R-09 no está en la matriz | 9,800,000.00 | `base_de_eventos.xlsx` fila 5 · `matriz_de_riesgos.xlsx` |
| 4 | Evento repetido en el mismo proceso (`loss_event_repeated`) | «Faltante de efectivo» en Sucursales: 2 eventos en 12 meses (EV-321, EV-322), del 2026-04-10 al 2026-09-05 | 5,000,000.00 | `base_de_eventos.xlsx` filas 12 y 13 |

## El resultado

| Proceso | Tipo de evento | Eventos en 12 meses | Monto |
|---|---|---|---|
| Canales | Fraude con tarjeta | EV-01, EV-02 | 40,600,000 |
| Sucursales | Faltante de efectivo | EV-321, EV-322 | 5,000,000 |

**Eventos sin un riesgo de la matriz:** EV-04, EV-42.

Si un evento cambia la calificación de un riesgo lo decide el área de riesgos. Aquí solo se dice qué se repite y qué no está en la matriz.

Todo lo que llegó se procesó.

**Fuentes:** `00-marco/matriz_de_riesgos.xlsx`, `30-eventos/base_de_eventos.xlsx`, F-01.

La corrida quedó registrada con el id `2026-11-25-pattern-check-1` y la salida está en `estado-riesgos/20607773331-seguros-del-sur-sintetica/corridas/salida-pattern-check.md`.