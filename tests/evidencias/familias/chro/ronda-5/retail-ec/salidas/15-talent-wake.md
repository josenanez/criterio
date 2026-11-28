# /criterio-talent:talent-wake 

Hoy tocaba solo `talent-scan`, por la revisión semanal, y no había peticiones en Rostrum. No llegó ningún documento nuevo, cambiado ni borrado, así que la ficha del periodo quedó igual y solo se volvió a calcular. Las dos fotografías (`foto.jpg`) no se abrieron y quedan fuera del análisis.

# Qué cambió en la selección · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 1.0.0 · **Comando:** `talent-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta (`retention_exceeded`) | CAN-609: su proceso terminó el 2026-06-09; la política conserva los datos 120 días, hasta el 2026-10-07, y siguen en la carpeta | — | — | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-53/CAN-609/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-604: no está en el registro de autorizaciones de tratamiento de datos | — | — | — | `30-candidatos/VAC-51/CAN-604/hoja-de-vida.pdf` |
| 3 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-607: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | — | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-52/CAN-607/hoja-de-vida.pdf` |
| 4 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-51 · PT-01: abierta desde el 2026-09-15; la política da 30 días y el plazo venció el 2026-10-15 | — | Gabriela Andrade | 32 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 5 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-54 · PT-04: abierta desde el 2026-10-01; la política da 30 días y el plazo venció el 2026-10-31 | — | Gabriela Andrade | 16 | `20-vacantes/registro-vacantes.xlsx` fila 5 |
| 6 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-602: el título «Licenciatura en administración de empresas · Universidad Sintética del Valle · 2018» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-51/CAN-602/hoja-de-vida.pdf` |
| 7 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-603: el empleo «Analista en Comercial Andina Sintética»: retiro 2022-08 en la hoja de vida y 2021-12 en el certificado | — | — | — | `30-candidatos/VAC-51/CAN-603/hoja-de-vida.pdf` · `30-candidatos/VAC-51/CAN-603/certificado-laboral.pdf` |
| 8 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-610: el empleo «Analista en Comercial Andina Sintética»: ingreso 2018-01 en la hoja de vida y 2018-06 en el certificado | — | — | — | `30-candidatos/VAC-51/CAN-610/hoja-de-vida.pdf` · `30-candidatos/VAC-51/CAN-610/certificado-laboral.pdf` |
| 9 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-602: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-51/CAN-602/foto.jpg` · `30-candidatos/VAC-51/CAN-602/hoja-de-vida.pdf` |
| 10 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-606: llegó fecha de nacimiento; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-51/CAN-606/hoja-de-vida.pdf` |
| 11 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-606: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-51/CAN-606/foto.jpg` · `30-candidatos/VAC-51/CAN-606/hoja-de-vida.pdf` |
| 12 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-601: el requisito esencial R1 «Escucha activa con el cliente» del perfil PT-01 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-51/CAN-601/hoja-de-vida.pdf` |
| 13 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-608: el requisito esencial R1 «Coordinación del equipo de ventas» del perfil PT-03 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-52/CAN-608/hoja-de-vida.pdf` |

## El resultado

**En la ficha:** 10 candidatos · **Vacantes en el registro:** 4 · **Perfiles de Norma:** 4 (periodo 2026-11).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- Plazo de cobertura de una vacante (selection.vacancy.target_days) → 30 días, de la política de selección (respuesta sugerida, sesión sin interfaz)
- Días de conservación de los datos de un candidato (selection.data.retention_days) → 120 días, de la política de selección (respuesta sugerida, sesión sin interfaz)
- ¿Se publican los reportes de candidatos en Rostrum? → No (propuesta por omisión, sesión sin interfaz)

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`
- `30-candidatos/VAC-51/CAN-601/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-602/foto.jpg`
- `30-candidatos/VAC-51/CAN-602/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-603/certificado-laboral.pdf`
- `30-candidatos/VAC-51/CAN-603/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-604/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-606/foto.jpg`
- `30-candidatos/VAC-51/CAN-606/hoja-de-vida.pdf`
- `30-candidatos/VAC-51/CAN-610/certificado-laboral.pdf`
- `30-candidatos/VAC-51/CAN-610/hoja-de-vida.pdf`
- `30-candidatos/VAC-52/CAN-607/hoja-de-vida.pdf`
- `30-candidatos/VAC-52/CAN-608/hoja-de-vida.pdf`
- `30-candidatos/VAC-53/CAN-609/hoja-de-vida.pdf`
- `40-autorizaciones/registro-autorizaciones.csv`
- `50-ats/exportacion-ats.csv`

---

Las dos corridas quedaron registradas con el caso 2026-11: `2026-11-16-talent-scan-2` y `2026-11-16-talent-wake-1`. Los términos ya estaban aceptados (versión 1.6, aceptados el 2026-11-16 por José Francisco Ñáñez), así que no hubo que registrarlos de nuevo.