# /criterio-resilience:notifications 

Los términos vigentes (versión 1.5) ya estaban aceptados, así que no registré una aceptación nueva. El reporte señala tres notificaciones tardías o sin hacer.

# Las notificaciones · Banco Paulista Sintético · periodo 2026-10

**Fecha de corte:** 2026-10-15 · **Agente:** Amparo 1.4.0

## Lo que hay que atender

| # | Qué | Cita |
|---|---|---|
| 1 | INC-BPS-103 → ANPD: notificado el 2026-09-27T23:30, 47.5 horas después del plazo de 3 días hábiles (Resolução CD/ANPD nº 15/2024, art. 6º) | `matriz-notificaciones.xlsx` fila 3 · `INC-BPS-103_notificacion-anpd.pdf` |
| 2 | INC-BPS-103 → Banco Central do Brasil: notificado el 2026-09-23T13:30, 6 horas después del plazo de 24 horas (Resolução CMN nº 4.893/2021, art. 20, III) | `matriz-notificaciones.xlsx` fila 2 · `INC-BPS-103_notificacion-banco-central-do-brasil.pdf` |
| 3 | INC-BPS-104 → Clientes afectados: la matriz pide notificar en 72 horas y la ficha no registra la notificación | `matriz-notificaciones.xlsx` fila 5 · `INC-BPS-104_informe.docx` (cierre: abierto) |

## El resultado

Fueron a tiempo ocho de las once notificaciones de la matriz. Las tres que no lo fueron son las de arriba.

| Incidente | Destinatario | Tope | Hecha | A tiempo |
|---|---|---|---|---|
| INC-BPS-105 | Comité de riesgos | 2026-08-20T10:00 | 2026-08-18T22:00 | sí |
| INC-BPS-101 | Banco Central do Brasil | 2026-09-04T09:10 | 2026-09-04T09:10 | sí |
| INC-BPS-101 | Comité de riesgos | 2026-09-05T09:10 | 2026-09-03T15:10 | sí |
| INC-BPS-102 | Comité de riesgos | 2026-09-12T14:00 | 2026-09-11T00:00 | sí |
| INC-BPS-103 | Banco Central do Brasil | 2026-09-23T07:30 | 2026-09-23T13:30 | no |
| INC-BPS-103 | ANPD | 2026-09-25T23:59 | 2026-09-27T23:30 | no |
| INC-BPS-103 | Titulares afectados | 2026-09-25T23:59 | 2026-09-24T09:30 | sí |
| INC-BPS-103 | Comité de riesgos | 2026-09-24T07:30 | 2026-09-22T12:30 | sí |
| INC-BPS-106 | Comité de riesgos | 2026-09-30T16:45 | 2026-09-28T20:45 | sí |
| INC-BPS-104 | Clientes afectados | 2026-10-04T11:00 | — | no |
| INC-BPS-104 | Comité de riesgos | 2026-10-03T11:00 | 2026-10-01T19:00 | sí |

Los destinatarios y los plazos los fija la matriz de la organización. Ninguna notificación la hace el agente.

## Lo que no se pudo procesar

Tres archivos quedaron excluidos y no se abrieron, porque por su nombre o extensión son credenciales, llaves o respaldos:
- `00-referencia/credenciales-vpn.txt`
- `10-controles/A.8.24_certificados/servidor-web.pem`
- `90-continuidad/respaldo-correo-2026-06-20.zip`

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

`matriz-notificaciones.xlsx`, `INC-BPS-103_notificacion-anpd.pdf`, `INC-BPS-103_notificacion-banco-central-do-brasil.pdf` e `INC-BPS-104_informe.docx`.

---

El reporte completo está en `estado-seguridad/12345678000195-banco-paulista-sintetico/resiliencia/2026-10/reporte-notifications.md`. Dejé la salida en `corridas/salida-notifications.md` en la misma carpeta y la registré como `2026-10-15-notifications-1`.