# /criterio-resilience:notifications 

Dos notificaciones que pide la matriz se hicieron tarde o no se hicieron. Los términos están vigentes (versión 1.6, aceptada con la versión instalada 1.5.1). El agente no notifica a nadie: quién actúa lo decide una persona.

# Las notificaciones · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.5.1 · **Comando:** `notifications`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Notificación tarde (`incident_notification_late`) | INC-BGS-103 → Superintendencia de Bancos: notificado el 2026-09-23T13:30, 6 horas después del plazo de 24 horas (Reglamento sectorial de ciberseguridad (sintético)) | `00-referencia/matriz-notificaciones.csv` fila 2 · `70-incidentes/INC-BGS-103_notificacion-superintendencia-de-bancos.pdf` |
| 2 | Notificación sin hacer (`incident_notification_late`) | INC-BGS-104 → Clientes afectados: la matriz pide notificar en 72 horas (Política de comunicación con clientes) y la ficha no registra la notificación | `00-referencia/matriz-notificaciones.csv` fila 4 · `70-incidentes/INC-BGS-104_informe.docx, línea de tiempo` |

## El resultado

| Incidente | Destinatario | Norma | Tope | Hecha | A tiempo |
|---|---|---|---|---|---|
| INC-BGS-105 | Comité de riesgos | Política de respuesta a incidentes | 2026-08-20T10:00 | 2026-08-18T22:00 | sí |
| INC-BGS-101 | Superintendencia de Bancos | Reglamento sectorial de ciberseguridad (sintético) | 2026-09-04T09:10 | 2026-09-04T09:10 | sí |
| INC-BGS-101 | Comité de riesgos | Política de respuesta a incidentes | 2026-09-05T09:10 | 2026-09-03T15:10 | sí |
| INC-BGS-102 | Comité de riesgos | Política de respuesta a incidentes | 2026-09-12T14:00 | 2026-09-11T00:00 | sí |
| INC-BGS-103 | Superintendencia de Bancos | Reglamento sectorial de ciberseguridad (sintético) | 2026-09-23T07:30 | 2026-09-23T13:30 | no |
| INC-BGS-103 | Autoridad de protección de datos | Ley de protección de datos (sintética) | 2026-09-25T07:30 | 2026-09-23T23:30 | sí |
| INC-BGS-103 | Comité de riesgos | Política de respuesta a incidentes | 2026-09-24T07:30 | 2026-09-22T12:30 | sí |
| INC-BGS-106 | Comité de riesgos | Política de respuesta a incidentes | 2026-09-30T16:45 | 2026-09-28T20:45 | sí |
| INC-BGS-104 | Clientes afectados | Política de comunicación con clientes | 2026-10-04T11:00 | — | no |
| INC-BGS-104 | Comité de riesgos | Política de respuesta a incidentes | 2026-10-03T11:00 | 2026-10-01T19:00 | sí |

La matriz es de la organización: los destinatarios y los plazos que exige cada norma los fija ella. Ninguna notificación la hace el agente.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-notificaciones.csv`
- `70-incidentes/INC-BGS-103_notificacion-superintendencia-de-bancos.pdf`
- `70-incidentes/INC-BGS-104_informe.docx, línea de tiempo`

---

La salida quedó guardada en `corridas/salida-notifications.md` y la corrida quedó registrada como `2026-10-15-notifications-1`.

Dos puntos sobre el registro:
- El motor contó 8 hallazgos en la corrida, y el reporte solo muestra 2 en "Lo que hay que atender". No sé qué son los otros 6.
- Copié el reporte del motor tal cual a `corridas/salida-notifications.md` con `cp`, así que ese archivo es el mismo texto que ves arriba. Lo que mostré en pantalla lleva este resumen y el encabezado, pero quité las columnas vacías (Monto, Responsable, Días) de la tabla de atención.