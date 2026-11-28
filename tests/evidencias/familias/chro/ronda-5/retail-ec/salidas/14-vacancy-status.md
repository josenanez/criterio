# /criterio-talent:vacancy-status 

Los términos (v1.6) están vigentes y quedaron aceptados en la versión 1.0.0 del plugin. La sesión no tenía interfaz, así que las preguntas del motor se contestaron con las respuestas sugeridas.

De las cuatro vacantes, dos pasaron el plazo de 30 días de la política.

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

La corrida quedó registrada como `2026-11-16-vacancy-status-1`. El reporte está en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/seleccion/2026-11/reporte-vacancy-status.md`. Lo mostrado quedó guardado en `estado-talento/1792345678001-almacenes-del-pacifico-sinteticos/corridas/salida-vacancy-status.md`.

No registré a José Francisco Ñáñez como quien acepta los términos. El motor ya tenía una aceptación vigente (1.0.0), el agente no mostró ninguna pantalla de aceptación y este comando no registra aceptaciones. Si hace falta dejar ese nombre en el comprobante, se hace con `/criterio-talent:talent-setup`.