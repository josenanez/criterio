# /criterio-talent:talent-scan 

Desde la corrida anterior no entró, cambió ni se borró ningún documento. Las 10 hojas de vida de `30-candidatos/` ya estaban en la ficha del periodo, así que no hubo nada nuevo que extraer. Las dos fotografías (`CAN-202/foto.jpg` y `CAN-206/foto.jpg`) no se abrieron y siguen fuera del análisis.

# Qué cambió en la selección · Tiendas del Bajío Sintéticas · periodo 2026-11

**Entidad:** Tiendas del Bajío Sintéticas (TBA110315K21) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `talent-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta (`retention_exceeded`) | CAN-209: su proceso terminó el 2026-06-09; la política conserva los datos 120 días, hasta el 2026-10-07, y siguen en la carpeta | — | — | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-13/CAN-209/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-204: no está en el registro de autorizaciones de tratamiento de datos | — | — | — | `30-candidatos/VAC-11/CAN-204/hoja-de-vida.pdf` |
| 3 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-207: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | — | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-12/CAN-207/hoja-de-vida.pdf` |
| 4 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-11 · PT-01: abierta desde el 2026-09-15; la política da 30 días y el plazo venció el 2026-10-15 | — | Mariana Ríos | 32 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 5 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-14 · PT-04: abierta desde el 2026-10-01; la política da 30 días y el plazo venció el 2026-10-31 | — | Mariana Ríos | 16 | `20-vacantes/registro-vacantes.xlsx` fila 5 |
| 6 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-202: el título «Licenciatura en administración · Universidad Sintética del Valle · 2018» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-11/CAN-202/hoja-de-vida.pdf` |
| 7 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-203: el empleo «Analista en Comercial Andina Sintética»: retiro 2022-08 en la hoja de vida y 2021-12 en el certificado | — | — | — | `30-candidatos/VAC-11/CAN-203/hoja-de-vida.pdf` · `30-candidatos/VAC-11/CAN-203/certificado-laboral.pdf` |
| 8 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-210: el empleo «Analista en Comercial Andina Sintética»: ingreso 2018-01 en la hoja de vida y 2018-06 en el certificado | — | — | — | `30-candidatos/VAC-11/CAN-210/hoja-de-vida.pdf` · `30-candidatos/VAC-11/CAN-210/certificado-laboral.pdf` |
| 9 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-202: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-11/CAN-202/foto.jpg` · `30-candidatos/VAC-11/CAN-202/hoja-de-vida.pdf` |
| 10 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-206: llegó fecha de nacimiento; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-11/CAN-206/hoja-de-vida.pdf` |
| 11 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-206: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-11/CAN-206/foto.jpg` · `30-candidatos/VAC-11/CAN-206/hoja-de-vida.pdf` |
| 12 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-201: el requisito esencial R1 «Escucha activa con el cliente» del perfil PT-01 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-11/CAN-201/hoja-de-vida.pdf` |
| 13 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-208: el requisito esencial R1 «Coordinación del equipo de ventas» del perfil PT-03 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-12/CAN-208/hoja-de-vida.pdf` |

## El resultado

**En la ficha:** 10 candidatos · **Vacantes en el registro:** 4 · **Perfiles de Norma:** 4 (periodo 2026-11).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`
- `30-candidatos/VAC-11/CAN-201/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-202/foto.jpg`
- `30-candidatos/VAC-11/CAN-202/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-203/certificado-laboral.pdf`
- `30-candidatos/VAC-11/CAN-203/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-204/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-206/foto.jpg`
- `30-candidatos/VAC-11/CAN-206/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-210/certificado-laboral.pdf`
- `30-candidatos/VAC-11/CAN-210/hoja-de-vida.pdf`
- `30-candidatos/VAC-12/CAN-207/hoja-de-vida.pdf`
- `30-candidatos/VAC-12/CAN-208/hoja-de-vida.pdf`
- `30-candidatos/VAC-13/CAN-209/hoja-de-vida.pdf`
- `40-autorizaciones/registro-autorizaciones.csv`
- `50-ats/exportacion-ats.csv`

---

La corrida queda registrada como `2026-11-16-talent-scan-1`, con 13 hallazgos. Lo que se mostró está en `estado-talento/tba110315k21-tiendas-del-bajio-sinteticas/corridas/salida-talent-scan.md`.