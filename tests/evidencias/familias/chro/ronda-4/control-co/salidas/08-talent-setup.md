# /criterio-talent:talent-setup talento/900777888-cooperativa-control-sintetica

Soy Cándido. Pongo cada afirmación de una hoja de vida al lado de su soporte y cada candidato al lado del perfil; no doy puntajes ni decido sobre nadie.

**La carpeta.** Solo encontré una: `talento/900777888-cooperativa-control-sintetica` (Cooperativa Control Sintética · NIT 900777888). Ya tenía la marca `_CRITERIO_TALENTO.txt` y tiene las carpetas de la 00 a la 50. La tomé con un sí. No volví a marcarla.

**Lo que reconocí**
- **Vacantes** (`20-vacantes/registro-vacantes.xlsx`): Vacante, Perfil, Apertura, Cierre, Estado, Plazo días y Responsable.
- **Autorizaciones** (`40-autorizaciones/registro-autorizaciones.csv`): candidato, fecha y finalidad.
- **Exportación del ATS** (`50-ats/exportacion-ats.csv`): Candidate ID, Requisition ID, Applied Date, Stage y Last Activity. No hizo falta anotar ninguna en `columns`.
- **No se pudo convertir:** `30-candidatos/VAC-31/CAN-406/diploma.jpg` (el motor no convierte .jpg). Lo abrí solo para confirmar que es un diploma escaneado, y quedó como soporte.

**Las respuestas** (tomé la propuesta de los documentos y del setup de Norma)
1. **Entidad:** Cooperativa Control Sintética, NIT 900777888, Colombia, COP.
2. **Periodo:** 2026-11.
3. **Plazo para cubrir una vacante:** 45 días. Lo dice `00-referencia/politica-de-seleccion.pdf`, en «Plazos»: «se cubre en un máximo de 45 días calendario desde su apertura».
4. **Conservación de los datos:** 180 días. Lo dice la misma política: «se conservan 180 días desde que termina su proceso».
5. **Lo que no se pide:** edad, sexo, estado civil y fotografía. Está en la política, en «Lo que no se pide».
6. **Estándar:** CUOC, el mismo que usa Norma.
7. **Publicar en Rostrum:** no.
8. **Dónde guardo el estado:** `estado-talento/900777888-cooperativa-control-sintetica`.
9. **Términos 1.6:**
   > Criterio entrega a la dirección análisis contrastado contra la evidencia: cada cifra, cada señal y cada vencimiento con la cita del documento del que sale. No sustituye el juicio de quien decide ni la asesoría profesional: la decisión, y su verificación, son de quien la firma. Procesa los documentos que usted le indique y dice lo que muestran; lo que se acordó fuera de ellos no lo conoce. Lo ejecuta un modelo de lenguaje (LLM), que puede equivocarse, y por eso ningún dato llega sin su fuente. Sus documentos se procesan en la infraestructura de la plataforma de IA donde lo ejecuta, no solo en su equipo. Cada versión se prueba antes de publicarse y su evidencia es pública; la garantía y la responsabilidad son las de la licencia Apache 2.0. Se acepta una vez y deja un comprobante en Markdown y PDF con su huella SHA-256; actualizar no pide aceptar de nuevo, salvo que estos términos cambien. Términos completos y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal

   Los aceptó José Francisco Ñáñez el 2026-11-16. El comprobante quedó en `.criterio/terminos/aceptacion-criterio-talent-0.2.0-2026-11-16.md` y en el `.pdf` del mismo nombre.

**La configuración** quedó en `.criterio/seleccion/900777888/config.json` y la validación no encontró problemas.

**La primera ficha.** Procesé las 10 hojas de vida con sus soportes:
- CAN-401 a CAN-408, de la vacante VAC-31.
- CAN-409, de VAC-33.
- CAN-410, de VAC-32.

Los nombres y los correos no van a la ficha. La hoja de vida de CAN-408 trae un dato de sexo: la ficha guarda solo el tipo de dato y dónde está, y el motor lo deja fuera del análisis.

# Las vacantes contra su plazo · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.2.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-31 | PC-11 | 2026-10-05 | 45 días | 2026-11-19 | — | 42 | Rosa Díaz |
| VAC-32 | PC-13 | 2026-08-01 | 120 días | 2026-11-29 | — | 107 | Rosa Díaz |
| VAC-33 | PC-12 | 2026-04-01 | 45 días | 2026-05-16 | 2026-05-20 | 49 | Rosa Díaz |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.

---

**El reloj.** Propuse una tarea los días hábiles a las 7:00 que revise lo que toca cada día. Crearla requiere un sí explícito y en esta sesión no lo hubo, así que no creé ninguna. Para correrlo a mano: `/criterio-talent:talent-wake`.

**Cuándo vuelvo:** sin reloj.

La corrida quedó registrada como `2026-11-16-talent-setup-1`, y esta misma salida está en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-talent-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.