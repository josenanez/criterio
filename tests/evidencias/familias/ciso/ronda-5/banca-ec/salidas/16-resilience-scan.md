# /criterio-resilience:resilience-scan 

No había documentos nuevos ni cambiados. La ficha del periodo ya coincidía con cada informe, revisión y prueba, así que no se agregó nada. El inventario ubica las tres revisiones `INC-BGS-10x_revision.md` en `70-incidentes/` por su nombre, pero son revisiones posteriores y se quedan en `80-revisiones/`.

# Qué cambió en la respuesta · Banco del Guayas Sintético · periodo 2026-10

**Entidad:** Banco del Guayas Sintético (1790987654001) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.5.1 · **Comando:** `resilience-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BGS-103 → Superintendencia de Bancos: notificado el 2026-09-23T13:30, 6 horas después del plazo de 24 horas (Reglamento sectorial de ciberseguridad (sintético)) | — | — | — | `00-referencia/matriz-notificaciones.csv` fila 2 · `70-incidentes/INC-BGS-103_notificacion-superintendencia-de-bancos.pdf` |
| 2 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BGS-104 → Clientes afectados: la matriz pide notificar en 72 horas (Política de comunicación con clientes) y la ficha no registra la notificación | — | — | — | `00-referencia/matriz-notificaciones.csv` fila 4 · `70-incidentes/INC-BGS-104_informe.docx, línea de tiempo` |
| 3 | La prueba del plan de continuidad o de recuperación pasó su fecha, o no hay ninguna (`continuity_test_overdue`) | Recuperación del centro de datos alterno: la última prueba es del 2026-02-20; tocaba el 2026-08-19 | — | Jefe de infraestructura | 57 | `00-referencia/calendario-continuidad.xlsx` fila 3 · `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf` |
| 4 | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna (`restore_test_overdue`) | Restauración del correo corporativo: la última prueba es del 2026-06-20; tocaba el 2026-09-18 | — | Jefe de infraestructura | 27 | `00-referencia/calendario-continuidad.xlsx` fila 5 · `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf` |
| 5 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BGS-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | — | — | `70-incidentes/INC-BGS-102_informe.docx, línea de tiempo` |
| 6 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BGS-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | — | `70-incidentes/INC-BGS-106_informe.docx, línea de tiempo` |
| 7 | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna (`restore_test_overdue`) | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | — | Jefe de infraestructura | — | `00-referencia/calendario-continuidad.xlsx` fila 6 |
| 8 | Un incidente cerrado no tiene su revisión posterior dentro del plazo (`incident_without_review`) | INC-BGS-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 15 días | — | — | 36 | `70-incidentes/INC-BGS-105_informe.docx, línea de tiempo` |

## El resultado

**En la ficha:** 6 incidentes, 3 revisiones posteriores y 4 pruebas.

**Excluidos por omisión:** 3 archivos —credenciales, llaves o respaldos— que el motor no abre: `00-referencia/credenciales-vpn.txt`, `10-controles/A.8.24_certificados/servidor-web.pem`, `90-continuidad/respaldo-correo-2026-06-20.zip`.

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/calendario-continuidad.xlsx`
- `00-referencia/matriz-notificaciones.csv`
- `70-incidentes/INC-BGS-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BGS-103_notificacion-superintendencia-de-bancos.pdf`
- `70-incidentes/INC-BGS-104_informe.docx, línea de tiempo`
- `70-incidentes/INC-BGS-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BGS-106_informe.docx, línea de tiempo`
- `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf`
- `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)