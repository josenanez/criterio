# /criterio-risk-events:events-scan 

No hay documentos nuevos, cambiados ni borrados. La única acción del acta del comité sobre un indicador (KRI-06) ya estaba en la ficha. KRI-01 aparece en el acta solo como mención, sin acción acordada, así que sale como «en alerta sin acción». Lo que se decida sobre cada señal les toca al comité de riesgos y a las áreas.

# Qué cambió en los eventos · Banco Mesoamericano Sintético · periodo 2026-10

**Entidad:** Banco Mesoamericano Sintético (BMS0907153R2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 1.0.0 · **Comando:** `events-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-01 · Transacciones fraudulentas por millón: dio 52 en 2026-10, en su zona de alerta (40), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Operaciones | — | `00-marco/indicadores_clave.xlsx` fila 2 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 2 |
| 2 | Un indicador clave está en su umbral de alerta o de límite y no tiene acción registrada (`kri_alert_without_action`) | KRI-12 · Reclamos por cada 10.000 clientes: dio 19 en 2026-10, en su zona de alerta (15), y no hay una acción registrada en la tabla de acciones ni en un acta | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 7 · `20-indicadores/valores_indicadores_2026-10.xlsx` fila 6 |
| 3 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Fraude con tarjeta» en Canales: 2 eventos en los últimos 12 meses (EV-01, EV-02), del 2026-03-10 al 2026-08-02 | 40,600,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 2 · `30-eventos/base_de_eventos.xlsx` fila 3 |
| 4 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-05 · Caída del canal digital: se descubrió el 2026-07-01 y se registró el 2026-08-20; la política da 30 días | 31,000,000.00 | — | 20 | `30-eventos/base_de_eventos.xlsx` fila 6 |
| 5 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-42 · Sanción por tratamiento de datos: el riesgo R-08 no está en la matriz | 12,000,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 14 · `00-marco/matriz_de_riesgos.xlsx` |
| 6 | Un evento no corresponde a ningún riesgo de la matriz (`loss_event_risk_unmapped`) | EV-04 · Multa por publicidad: el riesgo R-09 no está en la matriz | 9,800,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 5 · `00-marco/matriz_de_riesgos.xlsx` |
| 7 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-22 · Suplantación en el canal telefónico: se descubrió el 2026-06-10 y se registró el 2026-07-25; la política da 30 días | 7,400,000.00 | — | 15 | `30-eventos/base_de_eventos.xlsx` fila 11 |
| 8 | El mismo tipo de evento se repite en el mismo proceso dentro de la ventana de la política (`loss_event_repeated`) | «Faltante de efectivo» en Sucursales: 2 eventos en los últimos 12 meses (EV-321, EV-322), del 2026-04-10 al 2026-09-05 | 5,000,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 12 · `30-eventos/base_de_eventos.xlsx` fila 13 |
| 9 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotación del personal de crédito: no tiene valor en 2026-10 | — | Vicepresidencia de crédito | — | `00-marco/indicadores_clave.xlsx` fila 4 |
| 10 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-22 · Cancelaciones de productos en el primer mes: no tiene valor en 2026-10 | — | Mercadeo | — | `00-marco/indicadores_clave.xlsx` fila 8 |
| 11 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-03 · Error de liquidación: la base no trae causa | 4,300,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 4 |
| 12 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-12 · Cheque devuelto mal procesado: la base no trae monto | — | — | — | `30-eventos/base_de_eventos.xlsx` fila 10 |

## El resultado

**Indicadores clave de riesgo:** 7 · **En alerta o en su límite:** 4 · **Eventos en la base:** 13 · **Acciones tomadas de las actas:** 1.

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

Corrida registrada como `2026-11-25-events-scan-1`, con 12 hallazgos. El texto de arriba quedó guardado en `<espacio>/estado-riesgos/bms0907153r2-banco-mesoamericano-sintetico/corridas/salida-events-scan.md`.