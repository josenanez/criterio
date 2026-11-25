# /criterio-risk-events:events-wake 

Hoy tocaba la revisión semanal de eventos (`events-scan`). No llegaron documentos nuevos y no había peticiones. El acta del comité menciona KRI-01 solo con «se revisará en la próxima sesión», sin medida, responsable ni fecha, así que no cuenta como acción registrada y la señal 1 sigue abierta. Las tres señales las decide el comité de riesgos con las áreas.

# Qué cambió en los eventos · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `events-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40,600,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 2 · `30-eventos/base_de_eventos.xlsx` fila 3 |
| 3 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-03 · Error de liquidación: la base no trae causa | 4,300,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 4 |

## El resultado

**Indicadores clave de riesgo:** 4 · **En alerta o en su límite:** 2 · **Eventos en la base:** 8 · **Acciones tomadas de las actas:** 0.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- `20-indicadores/valores_indicadores_2026-10.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

Las dos corridas quedaron registradas con el caso 2026-10: `2026-11-25-events-scan-2` y `2026-11-25-events-wake-1`.