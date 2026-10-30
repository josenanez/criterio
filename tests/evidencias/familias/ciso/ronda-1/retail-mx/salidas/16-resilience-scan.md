# /criterio-resilience:resilience-scan 

La ficha de 2026-10 ya tenía los 6 incidentes, las 3 revisiones y las 4 pruebas, y coinciden con los documentos. No hubo nada nuevo que llevar. Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez, así que no los registré de nuevo.

El motor calculó 8 señales, y el reporte quedó en `resiliencia/2026-10/reporte-resilience-scan.md`. Corrí todo con `--today 2026-10-15`.

# Qué cambió en la respuesta · Tiendas del Bajío Sintéticas · periodo 2026-10

**Entidad:** Tiendas del Bajío Sintéticas (TBA110315K21) · **Fecha de corte:** 2026-10-15 · **Agente:** Amparo 0.1.0 · **Comando:** `resilience-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días |
|---|---|---|---|---|
| 1 | Notificación tarde o sin hacer | INC-TDA-103 → Comisión supervisora: notificada el 2026-09-23T13:30, 6 horas después del plazo de 24 horas | — | — |
| 2 | Notificación tarde o sin hacer | INC-TDA-104 → Clientes afectados: la matriz pide 72 horas y la ficha no registra la notificación | — | — |
| 3 | Prueba de continuidad o recuperación vencida | Recuperación del centro de datos alterno: última prueba el 2026-02-20, tocaba el 2026-08-19 | Jefe de infraestructura | 57 |
| 4 | Prueba de restauración vencida | Restauración del correo corporativo: última prueba el 2026-06-20, tocaba el 2026-09-18 | Jefe de infraestructura | 27 |
| 5 | Contención fuera de plazo | INC-TDA-102 (alta): contenido en 30 horas y la política da 24 | — | — |
| 6 | Contención fuera de plazo | INC-TDA-106 (alta): detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — |
| 7 | Prueba de restauración vencida | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | Jefe de infraestructura | — |
| 8 | Incidente cerrado sin revisión posterior | INC-TDA-105: cerrado el 2026-08-25 y sin revisión; la política da 15 días | — | 36 |

Las citas de cada fila están en el reporte.

## El resultado

**En la ficha:** 6 incidentes, 3 revisiones posteriores y 4 pruebas.

**Excluidos sin abrir:** `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem` y `90-continuidad/respaldo-correo-2026-06-20.zip`.

## Preguntas que hizo

Ninguna en esta corrida.

La salida quedó en `corridas/salida-resilience-scan.md` y la corrida quedó registrada como `2026-10-15-resilience-scan-1`. Quién notifica y qué se hace con cada señal lo decide una persona.