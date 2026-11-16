# /criterio-resilience:resilience-scan 

Desde la corrida anterior no llegó ningún documento nuevo ni cambiado. La ficha ya tenía cada incidente, revisión y prueba, y el cálculo no dejó documentos fuera de ella (`record_issues` vacío).
El inventario propone pasar las tres revisiones posteriores a `70-incidentes/` porque las ve "fuera de lugar". La respuesta que tomo de los documentos es dejarlas en `80-revisiones/`, porque son revisiones posteriores y esa es su carpeta.

# Qué cambió en la respuesta · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.4.0 · **Comando:** `resilience-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BPS-103 → ANPD: notificado el 2026-09-27T23:30, 47.5 horas después del plazo de 3 días hábiles (Resolução CD/ANPD nº 15/2024, art. 6º) | — | — | — | `00-referencia/matriz-notificaciones.xlsx` fila 3 · `70-incidentes/INC-BPS-103_notificacion-anpd.pdf` |
| 2 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BPS-103 → Banco Central do Brasil: notificado el 2026-09-23T13:30, 6 horas después del plazo de 24 horas (Resolução CMN nº 4.893/2021, art. 20, III: comunicação tempestiva; 24 horas según la política de la entidad) | — | — | — | `00-referencia/matriz-notificaciones.xlsx` fila 2 · `70-incidentes/INC-BPS-103_notificacion-banco-central-do-brasil.pdf` |
| 3 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BPS-104 → Clientes afectados: la matriz pide notificar en 72 horas (Política de comunicación con clientes) y la ficha no registra la notificación | — | — | — | `00-referencia/matriz-notificaciones.xlsx` fila 5 · `70-incidentes/INC-BPS-104_informe.docx, línea de tiempo (cierre: abierto)` |
| 4 | La prueba del plan de continuidad o de recuperación pasó su fecha, o no hay ninguna (`continuity_test_overdue`) | Recuperación del centro de datos alterno: la última prueba es del 2026-02-20; tocaba el 2026-08-19 | — | Jefe de infraestructura | 57 | `00-referencia/calendario-continuidad.csv` fila 3 · `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf` |
| 5 | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna (`restore_test_overdue`) | Restauración del correo corporativo: la última prueba es del 2026-06-20; tocaba el 2026-09-18 | — | Jefe de infraestructura | 27 | `00-referencia/calendario-continuidad.csv` fila 5 · `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf` |
| 6 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BPS-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | — | — | `70-incidentes/INC-BPS-102_informe.docx, línea de tiempo` |
| 7 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BPS-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | — | `70-incidentes/INC-BPS-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)` |
| 8 | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna (`restore_test_overdue`) | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | — | Jefe de infraestructura | — | `00-referencia/calendario-continuidad.csv` fila 6 |
| 9 | Un incidente cerrado no tiene su revisión posterior dentro del plazo (`incident_without_review`) | INC-BPS-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 15 días | — | — | 36 | `70-incidentes/INC-BPS-105_informe.docx, línea de tiempo` |

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

- `00-referencia/calendario-continuidad.csv`
- `00-referencia/matriz-notificaciones.xlsx`
- `70-incidentes/INC-BPS-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BPS-103_notificacion-anpd.pdf`
- `70-incidentes/INC-BPS-103_notificacion-banco-central-do-brasil.pdf`
- `70-incidentes/INC-BPS-104_informe.docx, línea de tiempo (cierre: abierto)`
- `70-incidentes/INC-BPS-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BPS-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)`
- `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf`
- `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

---

La corrida quedó registrada como `2026-10-15-resilience-scan-1`, con 9 hallazgos. La salida mostrada está en `<espacio>/estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-resilience-scan.md`.