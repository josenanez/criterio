# /criterio-talent:talent-setup talento/901555123-banco-cordillera-sintetico

Cándido quedó listo sobre Banco Cordillera Sintético (NIT 901555123) para el periodo 2026-11, con fecha de corte 2026-11-16.

- **Configuración:** está en `.criterio/seleccion/901555123/config.json`. Tomé de la política de selección un plazo de cobertura de 45 días y una conservación de los datos de 180 días. El estándar es la CUOC, el mismo que usa Norma, y los reportes de candidatos no se publican en Rostrum.
- **Términos 1.6:** quedaron aceptados a nombre de José Francisco Ñáñez con fecha 2026-11-16. El comprobante está en `.criterio/terminos/aceptacion-criterio-talent-0.2.0-2026-11-16.md` y `.pdf`.
- **Ficha de candidatos:** tiene 11 candidatos, cada uno con su soporte y su cita. Los dos `foto.jpg` no se abrieron y quedaron registrados solo como fotografía. El motor encontró 15 señales en total; debajo van solo las 2 de las vacantes. Las otras 13 son de autorizaciones, conservación de datos, soportes que no llegaron, fechas que no coinciden, una tarjeta vencida, datos protegidos y requisitos sin evidencia. Se verán con `cv-check`, `privacy-check` y `candidate-fit`.
- **Columnas:** el motor reconoció todas las columnas de los registros, incluidas las de la exportación del ATS que vienen en inglés.

# Las vacantes contra su plazo · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.2.0 · **Comando:** `vacancy-status`

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

- Carpeta raíz de la entidad → talento/901555123-banco-cordillera-sintetico (única candidata, ya marcada)
- Entidad, identificación fiscal y país → Banco Cordillera Sintético, 901555123, CO (del setup de Norma)
- Periodo → 2026-11
- Plazo de cobertura de una vacante → 45 días, 00-referencia/politica-de-seleccion.pdf, «Plazos»
- Días de conservación de los datos de un candidato → 180 días, 00-referencia/politica-de-seleccion.pdf, «Plazos»
- Estándar de ocupaciones → CUOC, 00-referencia/estandar/PerfilesOcupacionales-Excel-CUOC-2026-sintetico.xlsx (el de Norma)
- Publicar los reportes de candidatos en Rostrum → no
- Dónde se guarda el estado → estado-talento/901555123-banco-cordillera-sintetico
- Términos 1.6 → aceptados por José Francisco Ñáñez el 2026-11-16
- Marcar la carpeta con _CRITERIO_TALENTO.txt → no se preguntó: ya estaba marcada

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`

---

**Cuándo vuelvo:** sin reloj. No creé la tarea programada porque necesita un sí explícito y en esta prueba nadie podía darlo. Para revisar a mano lo que toca cada día: `/criterio-talent:talent-wake`.

La corrida quedó registrada como `2026-11-16-talent-setup-1`.

Si Criterio te sirve, dale una estrella en https://github.com/josenanez/criterio: así lo encuentran otros que lo necesitan.