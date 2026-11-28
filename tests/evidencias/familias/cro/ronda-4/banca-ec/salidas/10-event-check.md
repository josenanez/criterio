# /criterio-risk-events:event-check 

Corrida de prueba al 2026-11-25. Los términos vigentes (versión 1.6) ya estaban aceptados. El reporte señala cuatro eventos: dos registrados tarde y dos incompletos.

# Cada evento con su registro · Banco del Pichincha Sur Sintético · periodo 2026-11

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 1.1.0 · **Comando:** `event-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-05 · Caída del canal digital: se descubrió el 2026-07-01 y se registró el 2026-08-20; la política da 30 días | 31,000,000.00 | — | 20 | `30-eventos/base_de_eventos.xlsx` fila 6 |
| 2 | Un evento se registró después del plazo de la política desde que se descubrió (`loss_event_registered_late`) | EV-22 · Suplantación en el canal telefónico: se descubrió el 2026-06-10 y se registró el 2026-07-25; la política da 30 días | 7,400,000.00 | — | 15 | `30-eventos/base_de_eventos.xlsx` fila 11 |
| 3 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-03 · Error de liquidación: la base no trae causa | 4,300,000.00 | — | — | `30-eventos/base_de_eventos.xlsx` fila 4 |
| 4 | Un evento de pérdida no tiene causa, monto o proceso (`loss_event_incomplete`) | EV-12 · Cheque devuelto mal procesado: la base no trae monto | — | — | — | `30-eventos/base_de_eventos.xlsx` fila 10 |

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
| EV-12 | Cheque devuelto mal procesado | Sucursales | 2026-09-02 | 2026-09-10 | — | monto | — |
| EV-22 | Suplantación en el canal telefónico | Canales | 2026-06-10 | 2026-07-25 | 7,400,000 | — | 15 |
| EV-321 | Faltante de efectivo | Sucursales | 2026-04-10 | 2026-04-15 | 2,300,000 | — | — |
| EV-322 | Faltante de efectivo | Sucursales | 2026-09-05 | 2026-09-10 | 2,700,000 | — | — |
| EV-42 | Sanción por tratamiento de datos | Mercadeo | 2026-08-12 | 2026-08-21 | 12,000,000 | — | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-eventos/base_de_eventos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---
La corrida quedó registrada como `2026-11-25-event-check-1`. La salida está en `estado-riesgos/1790123456001-banco-del-pichincha-sur-sintetico/corridas/salida-event-check.md`.

**Dos aclaraciones sobre el registro:**
- El motor no pidió aceptar los términos, así que no registré ninguna aceptación a nombre de José Francisco Ñáñez. La salida de `terminos` ya mostraba una aceptación en la versión 1.1.0.
- El motor reportó 12 hallazgos en la corrida registrada. El reporte muestra 4 señales en "Lo que hay que atender". No averigüé a qué corresponde la diferencia.