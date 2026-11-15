# /criterio-resilience:incident-timeline 

Tres incidentes de 2026-10 piden atención: dos se contuvieron fuera de plazo o no se han contenido, y uno se cerró sin revisión posterior. La fecha de corte es 2026-10-15.

Los términos (versión 1.5) estaban vigentes, así que no se pidió aceptarlos de nuevo. No hubo preguntas en esta corrida.

# La línea de tiempo de cada incidente · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Agente:** Amparo 1.2.3 · **Comando:** `incident-timeline`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | `incident_response_late` | INC-BCO-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | `70-incidentes/INC-BCO-102_informe.docx, línea de tiempo` |
| 2 | `incident_response_late` | INC-BCO-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | `70-incidentes/INC-BCO-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)` |
| 3 | `incident_without_review` | INC-BCO-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 10 días | 41 | `70-incidentes/INC-BCO-105_informe.docx, línea de tiempo` |

## El resultado

**Plazos de contención de la política:** crítica 4 h · alta 24 h · media 72 h · baja 168 h. **Revisión posterior:** 10 días.

| Incidente | Severidad | Detectado | Contenido | Horas | Plazo | Cerrado | Revisión |
|---|---|---|---|---|---|---|---|
| INC-BCO-105 · Correo de suplantación con un enlace malicioso | baja | 2026-08-18T10:00 | 2026-08-19T16:00 | 30,00 | 168,00 | 2026-08-25 | — |
| INC-BCO-101 · Ransomware contenido en un servidor de archivos | crítica | 2026-09-03T09:10 | 2026-09-03T12:40 | 3,50 | 4,00 | 2026-09-08 | 2026-09-12 |
| INC-BCO-102 · Acceso indebido a una cuenta privilegiada | alta | 2026-09-10T14:00 | 2026-09-11T20:00 | 30,00 | 24,00 | 2026-09-15 | 2026-09-20 |
| INC-BCO-103 · Exfiltración de una base de datos de clientes | crítica | 2026-09-22T07:30 | 2026-09-22T11:00 | 3,50 | 4,00 | 2026-09-26 | 2026-09-30 |
| INC-BCO-106 · Malware en una estación de trabajo de finanzas | alta | 2026-09-28T16:45 | — | — | 24,00 | — | — |
| INC-BCO-104 · Indisponibilidad del portal por denegación de servicio | media | 2026-10-01T11:00 | 2026-10-02T07:00 | 20,00 | 72,00 | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión, por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión, .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión, .zip es una llave, una credencial o un respaldo.

## Fuentes

- `70-incidentes/INC-BCO-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BCO-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BCO-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

Lo que hay que hacer con cada incidente lo decide una persona. Este comando no declara, cierra ni notifica nada.

La salida quedó en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-incident-timeline.md`. La corrida quedó registrada como `2026-10-15-incident-timeline-1`, con 8 hallazgos.

Dos cosas de la salida guardada difieren de lo que ve arriba:

- **Texto de apertura:** al archivo le puse una línea de apertura antes del encabezado, y esa línea no usa cifras del reporte.
- **Formato:** arriba quité las columnas vacías de la tabla de "Lo que hay que atender" y puse el reporte en un formato más corto. El archivo guardado lleva el reporte del motor completo, tal cual.