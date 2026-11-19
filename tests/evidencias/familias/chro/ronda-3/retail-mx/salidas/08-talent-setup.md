# /criterio-talent:talent-setup talento/tba110315k21-tiendas-del-bajio-sinteticas

Soy Cándido. Pongo cada afirmación de una hoja de vida al lado de su soporte y cada candidato al lado del perfil; no doy puntajes ni decido sobre nadie.

**La carpeta:** 1. `talento/tba110315k21-tiendas-del-bajio-sinteticas`. Ya estaba marcada con `_CRITERIO_TALENTO.txt` (Tiendas del Bajío Sintéticas · RFC TBA110315K21) y tiene las carpetas de `00-referencia/` a `50-ats/`. Es la única candidata, así que la tomé y no la volví a marcar.

**Los registros que reconocí:**
- **Vacantes:** `Vacante, Perfil, Apertura, Cierre, Estado, Plazo días, Responsable`.
- **Autorizaciones:** `candidato, fecha, finalidad`.
- **Exportación del ATS:** `Candidate ID, Requisition ID, Applied Date, Stage, Last Activity`.
- **Base interna:** `persona, ocupacion, cargo, area`.

El motor procesó los cuatro sin pedir columnas, así que `columns` queda vacío. Tomé por fotografías dos imágenes, `CAN-202/foto.jpg` y `CAN-206/foto.jpg`, y no las abrí.

**Las respuestas que tomé de los documentos:**
- **Entidad:** Tiendas del Bajío Sintéticas · RFC TBA110315K21 · México (MXN), la que ya había fijado Norma.
- **Periodo:** 2026-11.
- **Plazo de cobertura: 30 días.** «Una vacante se cubre en un máximo de 30 días calendario desde su apertura…» (`00-referencia/politica-de-seleccion.pdf`, p. 1).
- **Conservación de los datos: 120 días.** «Los datos de un candidato que no quedó en el cargo se conservan 120 días desde que termina su proceso» (ídem).
- **Lo que un perfil no puede pedir:** edad, sexo, estado civil, fotografía y apariencia (ídem).
- **Estándar:** O*NET (`00-referencia/onet-31-0-sintetico`), el mismo de Norma.
- **Publicar en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-talento/tba110315k21-tiendas-del-bajio-sinteticas`.

**Los términos:**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-16 (versión 1.6). El comprobante quedó en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y en su `.pdf`.

**La configuración** quedó en `.criterio/seleccion/TBA110315K21/config.json`.

**La primera ficha** tiene 10 candidatos y está en `seleccion/2026-11/ficha.json`. El cálculo del periodo dejó 13 señales; el reporte de vacantes va tal cual:

---

# Las vacantes contra su plazo · Tiendas del Bajío Sintéticas · periodo 2026-11

**Entidad:** Tiendas del Bajío Sintéticas (TBA110315K21) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-11 · PT-01: abierta desde el 2026-09-15; la política da 30 días y el plazo venció el 2026-10-15 | — | Mariana Ríos | 32 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 2 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-14 · PT-04: abierta desde el 2026-10-01; la política da 30 días y el plazo venció el 2026-10-31 | — | Mariana Ríos | 16 | `20-vacantes/registro-vacantes.xlsx` fila 5 |

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-11 | PT-01 | 2026-09-15 | 30 días | 2026-10-15 | — | 62 | Mariana Ríos |
| VAC-12 | PT-03 | 2026-10-25 | 30 días | 2026-11-24 | — | 22 | Mariana Ríos |
| VAC-13 | PT-02 | 2026-03-01 | 30 días | 2026-03-31 | 2026-04-10 | 40 | Mariana Ríos |
| VAC-14 | PT-04 | 2026-10-01 | 30 días | 2026-10-31 | — | 46 | Mariana Ríos |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`

---

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta prueba nadie lo dio. Para correrlo a mano: `/criterio-talent:talent-wake`.

La corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.