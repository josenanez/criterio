# /criterio-talent:talent-setup talento/901555123-banco-cordillera-sintetico

Cándido quedó instalado para Banco Cordillera Sintético (NIT 901555123). La configuración y la ficha de noviembre de 2026 están listas, y el motor encontró 15 señales en los 11 candidatos.

- **Carpeta:** `talento/901555123-banco-cordillera-sintetico`, la única candidata. Ya estaba marcada con `_CRITERIO_TALENTO.txt`, así que no volví a marcarla.
- **Columnas:** el motor reconoció todas las del registro de vacantes, el de autorizaciones y la exportación del ATS, incluidas las cabeceras en inglés del ATS, así que no hubo que registrar ninguna aparte.
- **Plazos:** de la política de selección tomé 45 días para cubrir una vacante y 180 días para conservar los datos de un candidato. También registré lo que la política prohíbe pedir: edad, sexo, estado civil y fotografía.
- **Lo demás:** el estándar es la CUOC, el mismo que usa Norma. Los reportes de candidatos no se publican en Rostrum.
- **Términos 1.5:** quedó registrada la aceptación de José Francisco Ñáñez con fecha 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-talent-0.1.0-2026-11-16.md` y `.pdf`.
- **Ficha 2026-11:** recoge 11 candidatos de VAC-01, VAC-02 y VAC-03. Las fotos de CAN-102 y CAN-106 y la fecha de nacimiento de CAN-106 quedaron registradas solo por su tipo y su ubicación, nunca por su valor. Las señales de las hojas de vida se ven con `/criterio-talent:cv-check` y `/criterio-talent:privacy-check`.
- **Ojo con la fila 2 del reporte:** los 90 días de VAC-04 vienen del registro de vacantes, no de la política, aunque el texto diga «la política da».

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

**Cuándo vuelvo:** sin reloj. En esta sesión nadie dio un sí explícito, así que no creé la tarea programada. A mano se corre con `/criterio-talent:talent-wake`.

La corrida quedó registrada como `2026-11-16-talent-setup-1`, y lo que se mostró está guardado en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-talent-setup.md`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.