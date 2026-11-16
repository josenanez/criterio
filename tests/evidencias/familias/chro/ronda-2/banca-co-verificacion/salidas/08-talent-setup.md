# /criterio-talent:talent-setup talento/901555123-banco-cordillera-sintetico

La ficha de 2026-11 recoge las 11 hojas de vida de `30-candidatos/`, cada una con sus soportes. Lo que el motor encontró en ellas va en `/criterio-talent:cv-check` y `/criterio-talent:privacy-check`. Este es el estado de las vacantes:

# Las vacantes contra su plazo · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `vacancy-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-01 · PC-01: abierta desde el 2026-08-01; la política da 45 días y el plazo venció el 2026-09-15 | — | Lucía Paredes | 62 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 2 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-04 · PC-07: abierta desde el 2026-07-01; la política da 90 días y el plazo venció el 2026-09-29 | — | Andrés Mora | 48 | `20-vacantes/registro-vacantes.xlsx` fila 5 |

## El resultado

| Vacante | Perfil | Apertura | Plazo | Tope | Cierre | Días | Responsable |
|---|---|---|---|---|---|---|---|
| VAC-01 | PC-01 | 2026-08-01 | 45 días | 2026-09-15 | — | 107 | Lucía Paredes |
| VAC-02 | PC-04 | 2026-10-20 | 45 días | 2026-12-04 | — | 27 | Lucía Paredes |
| VAC-03 | PC-03 | 2026-02-01 | 45 días | 2026-03-18 | 2026-03-10 | 37 | Andrés Mora |
| VAC-04 | PC-07 | 2026-07-01 | 90 días | 2026-09-29 | — | 138 | Andrés Mora |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`

---

**Reloj:** te propondría una tarea programada los días hábiles a las 7:00, pero solo se crea con un sí explícito y en esta sesión nadie puede darlo. Queda sin reloj. Para correrlo a mano: `/criterio-talent:talent-wake`.

**Cuándo vuelvo:** sin reloj.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.