# /criterio-talent:talent-setup talento/1792345678001-almacenes-del-pacifico-sinteticos

Soy Cándido. Pongo cada afirmación de una hoja de vida al lado de su soporte y cada candidato al lado del perfil; no doy puntajes ni decido sobre nadie.

**Carpeta:** solo encontré una, `talento/1792345678001-almacenes-del-pacifico-sinteticos`. Ya tenía la marca `_CRITERIO_TALENTO.txt` y trae las seis subcarpetas que se esperan. La tomé como confirmada.

**Lo que reconocí:** hay 43 documentos. El motor reconoció todas las columnas del registro de vacantes, del de autorizaciones y de la exportación del ATS, así que no hubo que registrar ninguna a mano. Llegaron dos fotografías, `CAN-602/foto.jpg` y `CAN-606/foto.jpg`. No las abrí: la ficha solo dice qué dato llegó y dónde está.

**Respuestas** (nadie respondía en esta sesión, así que tomé la sugerida por los documentos):
- **Entidad:** Almacenes del Pacífico Sintéticos, RUC 1792345678001, Ecuador, periodo 2026-11. Viene del setup de Norma.
- **Plazo para cubrir una vacante:** 30 días. Lo dice `00-referencia/politica-de-seleccion.pdf`, p. 1: «Una vacante se cubre en un máximo de 30 días calendario desde su apertura…»
- **Conservación de los datos de un candidato:** 120 días. Misma página: «se conservan 120 días desde que termina su proceso…»
- **Estándar de ocupaciones:** O*NET, el mismo que usa Norma.
- **Publicar los reportes de candidatos en Rostrum:** no.
- **Dónde guardo lo que encuentro:** `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos`.
- **Marca de la carpeta:** ya estaba puesta; no la volví a pedir.

**Términos (versión 1.6):**
> Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

José Francisco Ñáñez los aceptó el 2026-11-16. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-talent-1.0.0-2026-11-16.md` y en el `.pdf` del mismo nombre.

**Configuración:** quedó en `.criterio/seleccion/1792345678001/config.json`.

**Primera ficha:** los 10 candidatos de `30-candidatos/` están en `estado-talento/…/seleccion/2026-11/ficha.json`. El motor encontró 13 señales. El estado de las vacantes, tal como lo escribió el motor:

# Las vacantes contra su plazo · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 1.0.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-51 · PT-01: abierta desde el 2026-09-15; la política da 30 días y el plazo venció el 2026-10-15 | — | Gabriela Andrade | 32 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 2 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-54 · PT-04: abierta desde el 2026-10-01; la política da 30 días y el plazo venció el 2026-10-31 | — | Gabriela Andrade | 16 | `20-vacantes/registro-vacantes.xlsx` fila 5 |

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-51 | PT-01 | 2026-09-15 | 30 días | 2026-10-15 | — | 62 | Gabriela Andrade |
| VAC-52 | PT-03 | 2026-10-25 | 30 días | 2026-11-24 | — | 22 | Gabriela Andrade |
| VAC-53 | PT-02 | 2026-03-01 | 30 días | 2026-03-31 | 2026-04-10 | 40 | Gabriela Andrade |
| VAC-54 | PT-04 | 2026-10-01 | 30 días | 2026-10-31 | — | 46 | Gabriela Andrade |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Plazo de cobertura de una vacante (selection.vacancy.target_days) → 30 días, de la política de selección (respuesta sugerida, sesión sin interfaz)
- Días de conservación de los datos de un candidato (selection.data.retention_days) → 120 días, de la política de selección (respuesta sugerida, sesión sin interfaz)
- ¿Se publican los reportes de candidatos en Rostrum? → No (propuesta por omisión, sesión sin interfaz)

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`

**Cuándo vuelvo:** sin reloj. La tarea programada necesita un sí explícito y en esta sesión nadie lo dio. Para correrlo a mano: `/criterio-talent:talent-wake`.

La corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.