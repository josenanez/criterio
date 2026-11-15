# /criterio-resilience:resilience-wake 

Hoy tocaba el `resilience-scan` por la revisión semanal, y no había peticiones abiertas. No hay documentos nuevos ni cambiados, y la ficha del periodo ya tenía todo lo de incidentes, revisiones y continuidad. El inventario marca como fuera de lugar los archivos de `80-revisiones/`, pero son revisiones posteriores, así que se quedan donde están. No notifiqué a nadie, no cerré ningún incidente y no corrí ninguna prueba. Eso le toca a una persona.

# Qué cambió en la respuesta · Banco Cordillera Sintético · periodo 2026-10

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.2.3 · **Comando:** `resilience-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BCO-103 → Superintendencia Financiera: notificado el 2026-09-23T13:30, 6 horas después del plazo de 24 horas (Reglamento sectorial de ciberseguridad (sintético)) | — | — | — | `00-referencia/matriz-notificaciones.csv` fila 2 · `70-incidentes/INC-BCO-103_notificacion-superintendencia-financiera.pdf` |
| 2 | Una notificación que pide la matriz —al supervisor, a la autoridad de datos, a los clientes— se hizo tarde o no se hizo (`incident_notification_late`) | INC-BCO-104 → Clientes afectados: la matriz pide notificar en 72 horas (Política de comunicación con clientes) y la ficha no registra la notificación | — | — | — | `00-referencia/matriz-notificaciones.csv` fila 4 · `70-incidentes/INC-BCO-104_informe.docx, línea de tiempo (cierre: abierto)` |
| 3 | La prueba del plan de continuidad o de recuperación pasó su fecha, o no hay ninguna (`continuity_test_overdue`) | Recuperación del centro de datos alterno: la última prueba es del 2026-02-20; tocaba el 2026-08-19 | — | Jefe de infraestructura | 57 | `00-referencia/calendario-continuidad.xlsx` fila 3 · `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf` |
| 4 | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna (`restore_test_overdue`) | Restauración del correo corporativo: la última prueba es del 2026-06-20; tocaba el 2026-09-18 | — | Jefe de infraestructura | 27 | `00-referencia/calendario-continuidad.xlsx` fila 5 · `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf` |
| 5 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BCO-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | — | — | `70-incidentes/INC-BCO-102_informe.docx, línea de tiempo` |
| 6 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BCO-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | — | `70-incidentes/INC-BCO-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)` |
| 7 | La prueba de restauración de un respaldo crítico pasó su fecha, o no hay ninguna (`restore_test_overdue`) | Restauración de la base de clientes: ninguna prueba registrada; el calendario pide una cada 180 días | — | Jefe de infraestructura | — | `00-referencia/calendario-continuidad.xlsx` fila 6 |
| 8 | Un incidente cerrado no tiene su revisión posterior dentro del plazo (`incident_without_review`) | INC-BCO-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 10 días | — | — | 41 | `70-incidentes/INC-BCO-105_informe.docx, línea de tiempo` |

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
- `70-incidentes/INC-BCO-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BCO-103_notificacion-superintendencia-financiera.pdf`
- `70-incidentes/INC-BCO-104_informe.docx, línea de tiempo (cierre: abierto)`
- `70-incidentes/INC-BCO-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BCO-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)`
- `90-continuidad/prueba_recuperacion-del-centro-de-datos-alterno_2026-02-20.pdf`
- `90-continuidad/prueba_restauracion-del-correo-corporativo_2026-06-20.pdf`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

---

Quedaron registradas dos corridas: `2026-10-15-resilience-scan-2` y `2026-10-15-resilience-wake-1`. Esta salida está guardada en `estado-seguridad/901555123-banco-cordillera-sintetico/corridas/salida-resilience-wake.md`.