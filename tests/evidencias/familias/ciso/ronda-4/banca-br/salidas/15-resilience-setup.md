# /criterio-resilience:resilience-setup seguridad/12345678000195-banco-paulista-sintetico

Soy Amparo. Pongo cada incidente al lado de los plazos que se comprometieron y cada prueba de continuidad al lado de su calendario; no notifico a nadie.

**Carpeta:** 1. `seguridad/12345678000195-banco-paulista-sintetico`. Está marcada con `_CRITERIO_SEGURIDAD.txt` (Banco Paulista Sintético, CNPJ 12345678000195) y tiene las diez subcarpetas de la estructura. Es la única candidata, así que la tomo.

**Lo que no abro** (credenciales, llaves y respaldos):
- `00-referencia/credenciales-vpn.txt`: por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: un .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: un .zip es una llave, una credencial o un respaldo.

**Sugerencia de estructura:** el motor sugiere llevar `80-revisiones/INC-BPS-101_revision.md`, `INC-BPS-102_revision.md` e `INC-BPS-103_revision.md` a `70-incidentes/`. No moví nada.

**Respuestas que tomé de los documentos**, porque es una prueba sin interfaz:
- **Entidad:** Banco Paulista Sintético, CNPJ 12345678000195, Brasil. Es la misma que ya fijaron Alexis y Guillermo.
- **Periodo:** 2026-10.
- **Plazos de contención** (política de respuesta a incidentes, versión 2, sección 5): crítica 4 horas, alta 24, media 72 y baja 168.
- **Revisión posterior** (sección 7): dentro de los 15 días calendario siguientes al cierre.
- **Matriz de notificaciones:**

| Destinatario | Cuándo aplica | Plazo |
|---|---|---|
| Banco Central do Brasil | crítica | 24 horas |
| ANPD | datos personales | 3 días hábiles |
| Titulares afectados | datos personales | 3 días hábiles |
| Clientes afectados | clientes afectados | 72 horas |
| Comité de riesgos | todos | 48 horas |

  El motor reconoce sus columnas, incluidos los días hábiles, así que no hizo falta llenar `columns.notifications`.
- **Calendario de continuidad:** 5 pruebas con su tipo y su frecuencia. El motor también reconoce sus columnas.
- **Dónde guardo lo que encuentro:** `estado-seguridad/12345678000195-banco-paulista-sintetico`.
- **Marca:** la carpeta ya estaba marcada, así que no dejé otra.

**Términos (versión 1.5):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

Los aceptó José Francisco Ñáñez el 2026-10-15. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-resilience-1.4.0-2026-10-15.md`, con su versión en `.pdf`.

**Configuración:** quedó en `.criterio/resiliencia/12345678000195/config.json` y el motor la validó sin problemas.

**Primera ficha (2026-10):** procesé 6 incidentes con 11 constancias de notificación, 3 revisiones posteriores y 4 informes de pruebas de continuidad. El motor dio 9 señales:
- 2 incidentes contenidos fuera de plazo.
- 1 incidente cerrado sin su revisión posterior.
- 3 notificaciones hechas tarde o sin hacer.
- 1 prueba de continuidad vencida.
- 2 pruebas de restauración vencidas o sin hacer.

Abajo va la línea de tiempo. Las notificaciones y las pruebas tienen sus propios comandos: `/criterio-resilience:notifications` y `/criterio-resilience:continuity-tests`.

# La línea de tiempo de cada incidente · Banco Paulista Sintético · periodo 2026-10

**Entidad:** Banco Paulista Sintético (12345678000195) · **Fecha de corte:** 2026-10-15 · **Procesado:** 2026-10-15 · **Agente:** Amparo, versión 1.4.0 · **Comando:** `incident-timeline`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BPS-102 · Acceso indebido a una cuenta privilegiada: alta, contenido en 30 horas y la política da 24 | — | — | — | `70-incidentes/INC-BPS-102_informe.docx, línea de tiempo` |
| 2 | Un incidente se contuvo después del plazo de su severidad en la política, o sigue sin contener pasado ese plazo (`incident_response_late`) | INC-BPS-106 · Malware en una estación de trabajo de finanzas: alta, detectado el 2026-09-28T16:45 y sin contención registrada; la política da 24 horas | — | — | — | `70-incidentes/INC-BPS-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)` |
| 3 | Un incidente cerrado no tiene su revisión posterior dentro del plazo (`incident_without_review`) | INC-BPS-105: cerrado el 2026-08-25 y sin revisión posterior; la política da 15 días | — | — | 36 | `70-incidentes/INC-BPS-105_informe.docx, línea de tiempo` |

## El resultado

**Plazos de contención de la política:** critica 4 h · alta 24 h · media 72 h · baja 168 h · **Revisión posterior:** 15 días

| Incidente | Severidad | Detectado | Contenido | Horas | Plazo | Cerrado | Revisión |
|---|---|---|---|---|---|---|---|
| INC-BPS-105 · Correo de suplantación con un enlace malicioso | baja | 2026-08-18T10:00 | 2026-08-19T16:00 | 30,00 | 168,00 | 2026-08-25 | — |
| INC-BPS-101 · Ransomware contenido en un servidor de archivos | critica | 2026-09-03T09:10 | 2026-09-03T12:40 | 3,50 | 4,00 | 2026-09-08 | 2026-09-12 |
| INC-BPS-102 · Acceso indebido a una cuenta privilegiada | alta | 2026-09-10T14:00 | 2026-09-11T20:00 | 30,00 | 24,00 | 2026-09-15 | 2026-09-20 |
| INC-BPS-103 · Exfiltración de una base de datos de clientes | critica | 2026-09-22T07:30 | 2026-09-22T11:00 | 3,50 | 4,00 | 2026-09-26 | 2026-09-30 |
| INC-BPS-106 · Malware en una estación de trabajo de finanzas | alta | 2026-09-28T16:45 | — | — | 24,00 | — | — |
| INC-BPS-104 · Indisponibilidad del portal por denegación de servicio | media | 2026-10-01T11:00 | 2026-10-02T07:00 | 20,00 | 72,00 | — | — |

## Lo que no se pudo procesar

- `00-referencia/credenciales-vpn.txt`: excluido por omisión: por su nombre es una credencial o una llave
- `10-controles/A.8.24_certificados/servidor-web.pem`: excluido por omisión: .pem es una llave, una credencial o un respaldo
- `90-continuidad/respaldo-correo-2026-06-20.zip`: excluido por omisión: .zip es una llave, una credencial o un respaldo

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `70-incidentes/INC-BPS-102_informe.docx, línea de tiempo`
- `70-incidentes/INC-BPS-105_informe.docx, línea de tiempo`
- `70-incidentes/INC-BPS-106_informe.docx, línea de tiempo (contención: pendiente; cierre: abierto)`
- Fuentes técnicas: F-04 (families/criterio-ciso/FUENTES.es.md)

**Cuándo vuelvo:** sin reloj. En esta prueba nadie dio un sí explícito a la tarea programada. Para correrlo a mano: `/criterio-resilience:resilience-wake`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.

---
La corrida quedó registrada como `2026-10-15-resilience-setup-1`. Lo que se mostró arriba está guardado en `estado-seguridad/12345678000195-banco-paulista-sintetico/corridas/salida-resilience-setup.md`.