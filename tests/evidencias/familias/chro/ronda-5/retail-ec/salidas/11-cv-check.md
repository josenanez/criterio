# /criterio-talent:cv-check 

Los términos (versión 1.6) ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-11-16, así que no hubo que registrar nada. El reporte de periodo 2026-11 tiene tres señales abiertas y dos preguntas sin respuesta de una persona. Al registrar la corrida, el motor contó 13 hallazgos. El reporte no explica esa cifra, así que no la desgloso.

# Las hojas de vida contra sus soportes · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 1.0.0 · **Comando:** `cv-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-602: el título «Licenciatura en administración de empresas · Universidad Sintética del Valle · 2018» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-51/CAN-602/hoja-de-vida.pdf` |
| 2 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-603: el empleo «Analista en Comercial Andina Sintética»: retiro 2022-08 en la hoja de vida y 2021-12 en el certificado | — | — | — | `30-candidatos/VAC-51/CAN-603/hoja-de-vida.pdf` · `30-candidatos/VAC-51/CAN-603/certificado-laboral.pdf` |
| 3 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-610: el empleo «Analista en Comercial Andina Sintética»: ingreso 2018-01 en la hoja de vida y 2018-06 en el certificado | — | — | — | `30-candidatos/VAC-51/CAN-610/hoja-de-vida.pdf` · `30-candidatos/VAC-51/CAN-610/certificado-laboral.pdf` |

## El resultado

| Candidato | Vacante | Afirmaciones |
|---|---|---|
| CAN-601 | VAC-51 | 2 |
| CAN-602 | VAC-51 | 2 |
| CAN-603 | VAC-51 | 2 |
| CAN-604 | VAC-51 | 2 |
| CAN-605 | VAC-51 | 2 |
| CAN-606 | VAC-51 | 2 |
| CAN-607 | VAC-52 | 2 |
| CAN-608 | VAC-52 | 0 |
| CAN-609 | VAC-53 | 2 |
| CAN-610 | VAC-51 | 2 |

Cada afirmación se contrasta con su soporte; ninguna se da por falsa: se dice cuál no tiene soporte o no coincide.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Plazo de cobertura de una vacante (selection.vacancy.target_days) → 30 días, de la política de selección (respuesta sugerida, sesión sin interfaz)
- Días de conservación de los datos de un candidato (selection.data.retention_days) → 120 días, de la política de selección (respuesta sugerida, sesión sin interfaz)
- ¿Se publican los reportes de candidatos en Rostrum? → No (propuesta por omisión, sesión sin interfaz)

## Fuentes

- `30-candidatos/VAC-51/CAN-602/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-603/certificado-laboral.pdf`
- `30-candidatos/VAC-51/CAN-603/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-610/certificado-laboral.pdf`
- `30-candidatos/VAC-51/CAN-610/hoja-de-vida.pdf`

La corrida quedó registrada como `2026-11-16-cv-check-1`. La salida completa está en `corridas/salida-cv-check.md`, dentro de la carpeta de estado de talento.

Los tres hallazgos son afirmaciones sin soporte o fechas que no coinciden. Ninguna se da por falsa y el reporte no decide nada sobre las personas.