# /criterio-risk-events:event-check 

Los términos (versión 1.6) ya estaban vigentes, así que no registré ninguna aceptación nueva. Corrí el reporte del periodo 2026-11 con fecha de corte 2026-11-25.

# Cada evento con su registro · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `event-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-05 · Caída del canal digital: se descubrió el 2026-07-01 y se registró el 2026-08-20; la política da 30 días | 31.000.000,00 | — | 20 | `30-eventos/base_de_eventos.xlsx` fila 6 |
| 2 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-03 · Error de liquidación: la base no trae causa | 4.300.000,00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 4 |

## El resultado

**Plazo de la política para registrar un evento:** 30 días desde que se descubre.

| Evento | Tipo | Proceso | Ocurrió | Se registró | Monto | Le falta | Días tarde |
|---|---|---|---|---|---|---|---|
| EV-01 | Fraude con tarjeta | Canales | 2026-03-10 | 2026-03-20 | 18,500,000 | — | — |
| EV-02 | Fraude con tarjeta | Canales | 2026-08-02 | 2026-08-11 | 22,100,000 | — | — |
| EV-03 | Error de liquidación | Tesorería | 2026-09-14 | 2026-09-30 | 4,300,000 | causa | — |
| EV-04 | Multa por publicidad | Mercadeo | 2026-10-03 | 2026-10-10 | 9,800,000 | — | — |
| EV-05 | Caída del canal digital | Tecnología | 2026-07-01 | 2026-08-20 | 31,000,000 | — | 20 |
| EV-06 | Fraude con tarjeta | Sucursales | 2026-05-04 | 2026-05-15 | 6,200,000 | — | — |
| EV-07 | Error de desembolso | Crédito | 2025-06-01 | 2025-06-10 | 1,200,000 | — | — |
| EV-08 | Error de desembolso | Crédito | 2026-02-01 | 2026-02-10 | 900,000 | — | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-event-check-1`. El reporte está en `estado-riesgos/901777333-banco-andino-sintetico/eventos/2026-11/reporte-event-check.md`. Lo mostrado quedó en `corridas/salida-event-check.md`.