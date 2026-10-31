# /criterio-resilience:resilience-scan 

Los incidentes, las revisiones y las pruebas ya estaban en la ficha del periodo, así que no hubo documentos nuevos que llevar. El motor calculó 8 señales. Quién notifica y qué se hace es de una persona.

# Qué cambió en la respuesta · Energía Andina Sintética · periodo 2026-10

**Entidad:** Energía Andina Sintética (20587654321) · **Fecha de corte:** 2026-10-15 · **Agente:** Amparo, versión 0.2.0 · **Comando:** `resilience-scan`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Notificación tarde o sin hacer | INC-ENA-103 → Organismo supervisor de energía: notificado el 2026-09-23T13:30, 6 horas después del plazo de 24 horas | — | — | `matriz-notificaciones.csv` fila 2 · `INC-ENA-103_notificacion-organismo-supervisor-de-energia.pdf` |
| 2 | Notificación tarde o sin hacer | INC-ENA-104 → Clientes afectados: la matriz pide 72 horas y la ficha no registra la notificación | — | — | `matriz-notificaciones.csv` fila 4 · `INC-ENA-104_informe.docx` |
| 3 | Prueba de continuidad o recuperación vencida | Recuperación del centro de datos alterno: última prueba 2026-02-20; tocaba el 2026-08-19 | Jefe de infraestructura | 57 | `calendario-continuidad.xlsx` fila 3 |
| 4 | Prueba de restauración vencida | Restauración del correo corporativo: última prueba 2026-06-20; tocaba el 2026-09-18 | Jefe de infraestructura | 27 | `calendario-continuidad.xlsx` fila 5 |
| 5 | Contención fuera de plazo | INC-ENA-102 (alta): contenido en 30 horas; la política da 24 | — | — | `INC-ENA-102_informe.docx` |
| 6 | Contención fuera de plazo | INC-ENA-106 (alta): detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | `INC-ENA-106_informe.docx` |
| 7 | Prueba de restauración sin hacer | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | Jefe de infraestructura | — | `calendario-continuidad.xlsx` fila 6 |
| 8 | Sin revisión posterior | INC-ENA-105: cerrado el 2026-08-25 y sin revisión; la política da 15 días | — | 36 | `INC-ENA-105_informe.docx` |

**En la ficha:** 6 incidentes, 3 revisiones posteriores y 4 pruebas.

**Excluidos y no abiertos:** `credenciales-vpn.txt`, `servidor-web.pem` y `respaldo-correo-2026-06-20.zip`.

**Preguntas que hice:** ninguna.

El inventario también marcó como fuera de lugar tres revisiones (`80-revisiones/INC-ENA-101_revision.md`, `INC-ENA-102_revision.md` e `INC-ENA-103_revision.md`). El motor sugiere `70-incidentes/` y no las movió.

El reporte completo y la corrida registrada (`2026-10-15-resilience-scan-1`) quedaron en el directorio de estado.