# /criterio-risk-events:events-scan 

No llegaron documentos nuevos ni cambiados desde la corrida anterior. El acta del comité de riesgos menciona KRI-01, pero no acuerda ninguna acción sobre él: solo dice que se revisará en la próxima sesión. Por eso queda en la ficha como revisada y sin acciones. El motor encontró tres señales.

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

Corrida registrada como `2026-11-25-events-scan-1`. El reporte quedó en `estado-riesgos/20607773331-seguros-del-sur-sintetica/eventos/2026-10/reporte-events-scan.md`.