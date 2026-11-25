# /criterio-risk-events:events-scan 

No llegaron documentos nuevos, cambiados ni borrados desde la corrida anterior. El acta del comité de riesgos de octubre no acuerda ninguna acción sobre un indicador. Sobre KRI-01 solo dice que "subió en el mes" y que "se revisará en la próxima sesión", así que no se cuenta como acción y queda anotada como acta revisada. Lo que se decida sobre cada señal les corresponde al comité de riesgos y a las áreas.

# Qué cambió en los eventos · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `events-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40.600.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 2 · `30-eventos/base_de_eventos.xlsx` fila 3 |
| 3 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-05 · Caída del canal digital: se descubrió el 2026-07-01 y se registró el 2026-08-20; la política da 30 días | 31.000.000,00 | — | 20 | `30-eventos/base_de_eventos.xlsx` fila 6 |
| 4 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidad: el riesgo R-09 no está en la matriz | 9.800.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riesgos.xlsx` |
| 5 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |
| 6 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-03 · Error de liquidación: la base no trae causa | 4.300.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 4 |

## El resultado

**Indicadores clave de riesgo:** 4 · **En alerta o en su límite:** 2 · **Eventos en la base:** 8 · **Acciones tomadas de las actas:** 0.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_clave.xlsx`
- `00-marco/matriz_de_riesgos.xlsx`
- `20-indicadores/valores_indicadores_2026-10.xlsx`
- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-events-scan-1`. Lo que se mostró está guardado tal cual en `<espacio>/estado-riesgos/901777333-banco-andino-sintetico/corridas/salida-events-scan.md`.