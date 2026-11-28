# /criterio-resilience:resilience-setup seguridad/1790987654001-banco-del-guayas-sintetico

Soy Amparo. Pongo cada incidente al lado de los plazos que se comprometieron y cada prueba de continuidad al lado de su calendario; no notifico a nadie.

**Carpeta:** solo había una candidata, `seguridad/1790987654001-banco-del-guayas-sintetico`. Ya tiene la marca `_CRITERIO_SEGURIDAD.txt` (Banco del Guayas Sintético, RUC 1790987654001, del 2026-10-15) y las diez subcarpetas. La usé. Como ya estaba marcada, no pregunté por la marca.

**Lo que no abrí** (de 60 archivos en el inventario):
- `00-referencia/credenciales-vpn.txt`: por su nombre es una credencial o una llave.
- `10-controles/A.8.24_certificados/servidor-web.pem`: un .pem es una llave, una credencial o un respaldo.
- `90-continuidad/respaldo-correo-2026-06-20.zip`: un .zip es una llave, una credencial o un respaldo.

**Sugerencia del inventario (no moví nada):** dice que las tres revisiones de `80-revisiones/` irían en `70-incidentes/`. Las dejé donde están, porque este comando las procesa desde `80-revisiones/`.

**Respuestas tomadas de los documentos:**
1. **Entidad:** Banco del Guayas Sintético, RUC 1790987654001, Ecuador, USD. Es la misma que ya fijó el setup de Alexis.
2. **Periodo:** 2026-10.
3. **Contención** (política de respuesta a incidentes, sección 5): crítica 4 h, alta 24 h, media 72 h, baja 168 h.
4. **Revisión posterior** (sección 7): 15 días calendario desde el cierre.
5. **Matriz de notificaciones:**
   - Superintendencia de Bancos: incidentes críticos, 24 h.
   - Autoridad de protección de datos: con datos personales, 72 h.
   - Clientes afectados: 72 h.
   - Comité de riesgos: todos los incidentes, 48 h.

   El motor reconoce sus columnas; no hizo falta mapeo.
6. **Calendario de continuidad:** cinco pruebas, cada 365, 180, 90, 90 y 180 días. El motor reconoce sus columnas.
7. **Estado:** `estado-seguridad/1790987654001-banco-del-guayas-sintetico`.

**Términos (versión 1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-10-15. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-resilience-1.5.1-2026-10-15.md` y `.pdf`. La configuración está en `.criterio/resiliencia/1790987654001/config.json` y se validó sin problemas.

**Primera ficha (2026-10):** procesé 6 incidentes con 9 constancias de notificación, 3 revisiones y 4 informes de prueba. El motor contó 8 señales:
- 2 contenciones fuera de plazo
- 2 notificaciones tarde
- 1 incidente cerrado sin revisión
- 1 prueba de continuidad vencida
- 2 restauraciones vencidas

Este reporte cubre las contenciones y la revisión que falta. Las notificaciones y las pruebas se ven con `/criterio-resilience:notifications` y `/criterio-resilience:continuity-tests`.

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

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie podía darlo. A mano se corre con `/criterio-resilience:resilience-wake`.

La corrida quedó registrada como `2026-10-15-resilience-setup-1`, con la salida en `estado-seguridad/1790987654001-banco-del-guayas-sintetico/corridas/salida-resilience-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.