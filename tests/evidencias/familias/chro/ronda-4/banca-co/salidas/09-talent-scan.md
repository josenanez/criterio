# /criterio-talent:talent-scan 

El inventario no trae documentos nuevos, cambiados ni borrados desde la corrida anterior. Todas las hojas de vida ya estaban en la ficha, así que no hubo nada que convertir. Las dos fotografías (`foto.jpg` de CAN-102 y de CAN-106) no se abrieron; ya están en la ficha como dato excluido.

# Qué cambió en la selección · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.2.0 · **Comando:** `talent-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta (`retention_exceeded`) | CAN-109: su proceso terminó el 2026-04-10; la política conserva los datos 180 días, hasta el 2026-10-07, y siguen en la carpeta | — | — | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-03/CAN-109/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-104: no está en el registro de autorizaciones de tratamiento de datos | — | — | — | `30-candidatos/VAC-01/CAN-104/hoja-de-vida.pdf` |
| 3 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-107: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | — | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-02/CAN-107/hoja-de-vida.pdf` |
| 4 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-01 · PC-01: abierta desde el 2026-08-01; la política da 45 días y el plazo venció el 2026-09-15 | — | Lucía Paredes | 62 | `20-vacantes/registro-vacantes.xlsx` fila 2 |
| 5 | Una vacante sigue abierta después del plazo de cobertura de la política (`vacancy_past_target`) | VAC-04 · PC-07: abierta desde el 2026-07-01; la política da 90 días y el plazo venció el 2026-09-29 | — | Andrés Mora | 48 | `20-vacantes/registro-vacantes.xlsx` fila 5 |
| 6 | Una certificación que el perfil exige venció antes de la postulación (`certification_expired`) | CAN-110: la certificación «Tarjeta profesional de contador vigente»: el perfil la exige (R4) y venció el 2026-06-30, antes de la postulación del 2026-09-05 | — | — | — | `30-candidatos/VAC-01/CAN-110/tarjeta-profesional.pdf` |
| 7 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-102: el título «Contador público · Universidad Sintética del Valle · 2018» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf` |
| 8 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-111: la certificación «Tarjeta profesional de contador vigente» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-01/CAN-111/hoja-de-vida.pdf` |
| 9 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-103: el empleo «Analista en Comercial Andina Sintética»: retiro 2022-08 en la hoja de vida y 2021-12 en el certificado | — | — | — | `30-candidatos/VAC-01/CAN-103/hoja-de-vida.pdf` · `30-candidatos/VAC-01/CAN-103/certificado-laboral.pdf` |
| 10 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-102: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-01/CAN-102/foto.jpg` · `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf` |
| 11 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-106: llegó fecha de nacimiento; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-01/CAN-106/hoja-de-vida.pdf` |
| 12 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-106: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-01/CAN-106/foto.jpg` · `30-candidatos/VAC-01/CAN-106/hoja-de-vida.pdf` |
| 13 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-101: el requisito esencial R1 «Contabilidad bajo NIIF» del perfil PC-01 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-01/CAN-101/hoja-de-vida.pdf` |
| 14 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-108: el requisito esencial R1 «Finanzas y análisis de estados financieros» del perfil PC-04 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf` |
| 15 | Un requisito esencial del perfil no tiene evidencia ni en la hoja de vida ni en sus soportes (`requirement_not_evidenced`) | CAN-108: el requisito esencial R3 «Criterio y toma de decisiones de crédito» del perfil PC-04 no tiene evidencia ni en la hoja de vida ni en sus soportes | — | — | — | `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf` |

## El resultado

**En la ficha:** 11 candidatos · **Vacantes en el registro:** 4 · **Perfiles de Norma:** 7 (periodo 2026-11).

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
- `30-candidatos/VAC-01/CAN-101/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-102/foto.jpg`
- `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-103/certificado-laboral.pdf`
- `30-candidatos/VAC-01/CAN-103/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-104/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-106/foto.jpg`
- `30-candidatos/VAC-01/CAN-106/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-110/tarjeta-profesional.pdf`
- `30-candidatos/VAC-01/CAN-111/hoja-de-vida.pdf`
- `30-candidatos/VAC-02/CAN-107/hoja-de-vida.pdf`
- `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf`
- `30-candidatos/VAC-03/CAN-109/hoja-de-vida.pdf`
- `40-autorizaciones/registro-autorizaciones.csv`
- `50-ats/exportacion-ats.csv`

---

La corrida quedó registrada como `2026-11-16-talent-scan-1`. Lo que se mostró arriba está en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-talent-scan.md`.