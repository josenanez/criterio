# /criterio-talent:cv-check 

El comando `/criterio-talent:cv-check` no está cargado en esta sesión. Su definición sí está en el plugin instalado (criterio-talent 0.1.0), y la seguí paso a paso con el mismo motor de Criterio. Los términos están vigentes, aceptados por José Francisco Ñáñez el 2026-11-16.

En la carpeta de CAN-406 hay un `diploma.jpg`, una imagen que no se tomó como soporte del título. Conviene que una persona lo revise antes de dar esta señal por cerrada.

# Las hojas de vida contra sus soportes · Cooperativa Control Sintética · periodo 2026-11

**Entidad:** Cooperativa Control Sintética (900777888) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `cv-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-406: el título «Contador público» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-31/CAN-406/hoja-de-vida.pdf` |

## El resultado

| Candidato | Vacante | Afirmaciones |
|---|---|---|
| CAN-401 | VAC-31 | 3 |
| CAN-402 | VAC-31 | 3 |
| CAN-403 | VAC-31 | 3 |
| CAN-404 | VAC-31 | 3 |
| CAN-405 | VAC-31 | 4 |
| CAN-406 | VAC-31 | 3 |
| CAN-407 | VAC-31 | 3 |
| CAN-408 | VAC-31 | 3 |
| CAN-409 | VAC-33 | 2 |
| CAN-410 | VAC-32 | 2 |

Cada afirmación se contrasta con su soporte; ninguna se da por falsa: se dice cuál no tiene soporte o no coincide.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Plazo de cobertura de una vacante? → 45 días calendario desde la apertura, salvo plazo propio en el registro · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Días de conservación de los datos de un candidato no seleccionado? → 180 días desde que termina su proceso · 00-referencia/politica-de-seleccion.pdf, Plazos · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se publican los reportes de candidatos en Rostrum? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)
- ¿Se marca la carpeta con _CRITERIO_TALENTO.txt? → No · Respuesta sugerida, tomada sin interlocutor (sesión de prueba, 2026-11-16)

## Fuentes

- `30-candidatos/VAC-31/CAN-406/hoja-de-vida.pdf`

---

- **Corrida registrada:** `2026-11-16-cv-check-1`. Lo que se mostró está guardado en `estado-talento/900777888-cooperativa-control-sintetica/corridas/salida-cv-check.md`.
- **Cifras que no cuadran:** al registrar la corrida, el motor contó 3 hallazgos, pero el reporte solo trae una señal. No investigué la diferencia; vale la pena revisarla en el motor.