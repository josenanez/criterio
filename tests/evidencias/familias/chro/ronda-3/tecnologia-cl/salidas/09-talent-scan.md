# /criterio-talent:talent-scan 

No llegó nada nuevo desde la corrida anterior. El inventario no muestra archivos nuevos, cambiados ni borrados, y las hojas de vida ya estaban en la ficha, así que no extraje ninguna.
El inventario marca los dos `foto.jpg` como formato no soportado: son fotografías. No los abrí, están en `protected` y el motor los deja fuera del análisis.

# Qué cambió en la selección · Nube Austral Software Sintética · periodo 2026-11

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `talent-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta (`retention_exceeded`) | CAN-309: su proceso terminó el 2026-07-09; la política conserva los datos 90 días, hasta el 2026-10-07, y siguen en la carpeta | — | — | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-23/CAN-309/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-304: no está en el registro de autorizaciones de tratamiento de datos | — | — | — | `30-candidatos/VAC-21/CAN-304/hoja-de-vida.pdf` |
| 3 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-307: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | — | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-22/CAN-307/hoja-de-vida.pdf` |
| 4 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-21 · TI-01: abierta desde el 2026-08-10; la política da 60 días y el plazo venció el 2026-10-09 | — | Tomás Vidal | 38 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 5 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-24 · TI-05: abierta desde el 2026-09-01; la política da 45 días y el plazo venció el 2026-10-16 | — | Tomás Vidal | 31 | `20-vacantes/registro-vacantes.xlsx` fila 5 |
| 6 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-302: el título «Ingeniería en informática · Universidad Sintética del Valle · 2018» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-21/CAN-302/hoja-de-vida.pdf` |
| 7 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-303: el empleo «Analista en Comercial Andina Sintética»: retiro 2022-08 en la hoja de vida y 2021-12 en el certificado | — | — | — | `30-candidatos/VAC-21/CAN-303/hoja-de-vida.pdf` · `30-candidatos/VAC-21/CAN-303/certificado-laboral.pdf` |
| 8 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-310: el empleo «Analista en Comercial Andina Sintética»: ingreso 2018-01 en la hoja de vida y 2018-06 en el certificado | — | — | — | `30-candidatos/VAC-21/CAN-310/hoja-de-vida.pdf` · `30-candidatos/VAC-21/CAN-310/certificado-laboral.pdf` |
| 9 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-302: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-21/CAN-302/foto.jpg` · `30-candidatos/VAC-21/CAN-302/hoja-de-vida.pdf` |
| 10 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-306: llegó fecha de nacimiento; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-21/CAN-306/hoja-de-vida.pdf` |
| 11 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-306: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-21/CAN-306/foto.jpg` · `30-candidatos/VAC-21/CAN-306/hoja-de-vida.pdf` |
| 12 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-301: el requisito esencial R1 «Programación en Python y Java» del perfil TI-01 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-21/CAN-301/hoja-de-vida.pdf` |
| 13 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-308: el requisito esencial R1 «Pensamiento crítico» del perfil TI-03 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-22/CAN-308/hoja-de-vida.pdf` |

## El resultado

**En la ficha:** 10 candidatos · **Vacantes en el registro:** 4 · **Perfiles de Norma:** 5 (periodo 2026-11).

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-vacantes/registro-vacantes.xlsx`
- `30-candidatos/VAC-21/CAN-301/hoja-de-vida.pdf`
- `30-candidatos/VAC-21/CAN-302/foto.jpg`
- `30-candidatos/VAC-21/CAN-302/hoja-de-vida.pdf`
- `30-candidatos/VAC-21/CAN-303/certificado-laboral.pdf`
- `30-candidatos/VAC-21/CAN-303/hoja-de-vida.pdf`
- `30-candidatos/VAC-21/CAN-304/hoja-de-vida.pdf`
- `30-candidatos/VAC-21/CAN-306/foto.jpg`
- `30-candidatos/VAC-21/CAN-306/hoja-de-vida.pdf`
- `30-candidatos/VAC-21/CAN-310/certificado-laboral.pdf`
- `30-candidatos/VAC-21/CAN-310/hoja-de-vida.pdf`
- `30-candidatos/VAC-22/CAN-307/hoja-de-vida.pdf`
- `30-candidatos/VAC-22/CAN-308/hoja-de-vida.pdf`
- `30-candidatos/VAC-23/CAN-309/hoja-de-vida.pdf`
- `40-autorizaciones/registro-autorizaciones.csv`
- `50-ats/exportacion-ats.csv`