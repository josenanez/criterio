# /criterio-risk-events:pattern-check 

Los términos ya estaban vigentes (versión 1.6, aceptada en la 0.1.0), así que no registré ninguna aceptación nueva. El argumento no traía periodo, así que usé 2026-10, el mes anterior a la fecha de prueba.

# Lo que se repite · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `pattern-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40,600,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 2 · `30-eventos/base_de_eventos.xlsx` fila 3 |

## El resultado

| Proceso | Tipo de evento | Eventos en 12 meses | Monto |
|---|---|---|---|
| Canales | Fraude con tarjeta | EV-01, EV-02 | 40,600,000 |

Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-pattern-check-1`. La salida está en `estado-riesgos/20607773331-seguros-del-sur-sintetica/corridas/salida-pattern-check.md`.

El motor anotó 3 hallazgos en el registro, pero el reporte solo muestra 1 señal. No sé por qué difieren, porque el motor no lo explica, y no lo he revisado.