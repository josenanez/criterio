# /criterio-resilience:incident-timeline 

Tres señales en el periodo 2026-10: dos incidentes con la contención fuera de plazo (INC-BGS-102 y INC-BGS-106) y un incidente cerrado sin revisión posterior (INC-BGS-105).

Los términos 1.6 ya estaban vigentes y aceptados, así que no pedí ninguna aceptación. Tampoco hizo falta responder preguntas.

# La línea de tiempo de cada incidente · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.5.1 · **Comando:** `incident-timeline`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BGS-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | — | — | `70-incidentes/INC-BGS-102_informe.docx, línea de tiempo` |
| 2 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BGS-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | — | `70-incidentes/INC-BGS-106_informe.docx, línea de tiempo` |
| 3 | Un incidente cerrado no tiene su revisión posterior dentro del plazo (`incident_without_review`) | INC-BGS-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 15 días | — | — | 36 | `70-incidentes/INC-BGS-105_informe.docx, línea de tiempo` |

## El resultado

**Plazos de contención de la política:** critica 4 h · alta 24 h · media 72 h · baja 168 h · **Revisión posterior:** 15 días

| Incidente | Severidad | Detectado | Contenido | Horas | Plazo | Cerrado | Revisión |
|---|---|---|---|---|---|---|---|
| INC-BGS-105 · Correo de suplantación con un enlace malicioso | baja | 2026-08-18T10:00 | 2026-08-19T16:00 | 30.00 | 168.00 | 2026-08-25 | — |
| INC-BGS-101 · Ransomware contenido en un servidor de archivos | critica | 2026-09-03T09:10 | 2026-09-03T12:40 | 3.50 | 4.00 | 2026-09-08 | 2026-09-12 |
| INC-BGS-102 · Acceso indebido a una cuenta privilegiada | alta | 2026-09-10T14:00 | 2026-09-11T20:00 | 30.00 | 24.00 | 2026-09-15 | 2026-09-20 |
| INC-BGS-103 · Exfiltración de una base de datos de clientes | critica | 2026-09-22T07:30 | 2026-09-22T11:00 | 3.50 | 4.00 | 2026-09-26 | 2026-09-30 |
| INC-BGS-106 · Malware en una estación de trabajo de finanzas | alta | 2026-09-28T16:45 | — | — | 24.00 | — | — |
| INC-BGS-104 · Indisponibilidad del portal por denegación de servicio | media | 2026-10-01T11:00 | 2026-10-02T07:00 | 20.00 | 72.00 | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `70-incidentes/INC-BGS-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BGS-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BGS-106_informe.docx, línea de tiempo`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

La salida quedó en `corridas/salida-incident-timeline.md` y la corrida se registró con el id `2026-10-15-incident-timeline-1`.