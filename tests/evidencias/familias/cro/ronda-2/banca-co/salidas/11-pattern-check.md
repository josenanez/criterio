# /criterio-risk-events:pattern-check 

Casandra: estos son los eventos que se repiten en el mismo proceso y los que no están en la matriz. El reporte lo escribió el motor.

# Lo que se repite · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `pattern-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | Evento repetido en el mismo proceso dentro de la ventana (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40.600.000,00 | `30-eventos/base_de_eventos.xlsx` filas 2 y 3 |
| 2 | Evento sin riesgo en la matriz (`loss_event_risk_unmapped`) | EV-42 · Sanción por tratamiento de datos: el riesgo R-08 no está en la matriz | 12.000.000,00 | `30-eventos/base_de_eventos.xlsx` fila 18 · `00-marco/matriz_de_riesgos.xlsx` |
| 3 | Evento repetido (`loss_event_repeated`) | «Error de conciliación» en Tesorería: 2 eventos (EV-331, EV-332), del 2026-01-15 al 2026-08-20 | 11.600.000,00 | `30-eventos/base_de_eventos.xlsx` filas 16 y 17 |
| 4 | Evento sin riesgo en la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidad: el riesgo R-09 no está en la matriz | 9.800.000,00 | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riesgos.xlsx` |
| 5 | Evento sin riesgo en la matriz (`loss_event_risk_unmapped`) | EV-43 · Pérdida de un litigio laboral: el riesgo R-07 no está en la matriz | 8.500.000,00 | `30-eventos/base_de_eventos.xlsx` fila 19 · `00-marco/matriz_de_riesgos.xlsx` |
| 6 | Evento repetido (`loss_event_repeated`) | «Faltante de efectivo» en Sucursales: 2 eventos (EV-321, EV-322), del 2026-04-10 al 2026-09-05 | 5.000.000,00 | `30-eventos/base_de_eventos.xlsx` filas 14 y 15 |

## El resultado

| Proceso | Tipo de evento | Eventos en 12 meses | Monto |
|---|---|---|---|
| Canales | Fraude con tarjeta | EV-01, EV-02 | 40,600,000 |
| Sucursales | Faltante de efectivo | EV-321, EV-322 | 5,000,000 |
| Tesorería | Error de conciliación | EV-331, EV-332 | 11,600,000 |

**Eventos sin un riesgo de la matriz:** EV-04, EV-42, EV-43.

Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---
Los términos ya estaban vigentes (versión 1.6, aceptada en 0.2.0), así que no registré una aceptación nueva. La corrida quedó registrada como `2026-11-25-pattern-check-1`. La salida está en `estado-riesgos/901777333-banco-andino-sintetico/corridas/salida-pattern-check.md` y el reporte en `eventos/2026-11/reporte-pattern-check.md`, dentro de esa misma carpeta.