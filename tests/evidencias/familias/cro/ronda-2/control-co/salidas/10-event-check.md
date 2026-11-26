# /criterio-risk-events:event-check 

Los términos vigentes (versión 1.6) ya estaban aceptados, así que no hizo falta registrar la aceptación. Corrí el reporte con `--today 2026-11-25`.

Las 8 filas de la base de eventos (EV-01 a EV-08) salieron completas, con causa, monto y proceso. Ninguna se registró fuera del plazo de la política, que es de 30 días desde que se descubre el evento. El reporte dice "Nada abierto en lo que procesa este comando" y todo lo que llegó se procesó.

**Lo que muestra cada evento**

| Evento | Tipo | Proceso | Ocurrió | Se registró | Monto |
|---|---|---|---|---|---|
| EV-01 | Fraude con tarjeta | Canales | 2026-03-10 | 2026-03-20 | 18,500,000 |
| EV-02 | Fraude con tarjeta | Canales | 2024-08-02 | 2024-08-11 | 22,100,000 |
| EV-03 | Error de liquidación | Tesorería | 2026-09-14 | 2026-09-30 | 4,300,000 |
| EV-04 | Multa por publicidad | Mercadeo | 2026-10-03 | 2026-10-10 | 9,800,000 |
| EV-05 | Caída del canal digital | Tecnología | 2026-07-01 | 2026-07-31 | 31,000,000 |
| EV-06 | Fraude con tarjeta | Sucursales | 2026-05-04 | 2026-05-15 | 6,200,000 |
| EV-07 | Error de desembolso | Crédito | 2025-06-01 | 2025-06-10 | 1,200,000 |
| EV-08 | Error de desembolso | Crédito | 2026-02-01 | 2026-02-10 | 900,000 |

La corrida quedó registrada como `2026-11-25-event-check-1` con 0 hallazgos. La salida completa está en `.criterio/eventos/901888444/corridas/salida-event-check.md`. El reporte del motor quedó en el estado de la entidad, como siempre.

Nadie respondió preguntas en esta sesión de prueba, y la corrida tampoco hizo ninguna.