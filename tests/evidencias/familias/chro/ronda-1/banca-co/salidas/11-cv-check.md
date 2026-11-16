# /criterio-talent:cv-check 

Los términos (versión 1.5) ya estaban aceptados por José Francisco Ñáñez el 2026-11-16, así que seguí con el reporte. Salieron 4 señales para atender, y ninguna afirmación se da por falsa: cada una dice qué falta o qué no coincide.

# Las hojas de vida contra sus soportes · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `cv-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una certificación que el perfil exige venció antes de la postulación (`certification_expired`) | CAN-110: la certificación «Tarjeta profesional de contador vigente»: el perfil la exige (R4) y venció el 2026-06-30, antes de la postulación del 2026-09-05 | — | — | — | `30-candidatos/VAC-01/CAN-110/tarjeta-profesional.pdf` |
| 2 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-102: el título «Contador público» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf` |
| 3 | La hoja de vida afirma un título, una certificación o un empleo sin el documento que lo soporte (`claim_without_support`) | CAN-111: la certificación «Tarjeta profesional de contador vigente» no tiene el documento que lo soporte | — | — | — | `30-candidatos/VAC-01/CAN-111/hoja-de-vida.pdf` |
| 4 | Las fechas de un empleo en la hoja de vida no son las de su certificado laboral (`employment_dates_differ`) | CAN-103: el empleo «Analista en Comercial Andina Sintética»: retiro 2022-08 en la hoja de vida y 2021-12 en el certificado | — | — | — | `30-candidatos/VAC-01/CAN-103/hoja-de-vida.pdf` · `30-candidatos/VAC-01/CAN-103/certificado-laboral.pdf` |

## El resultado

| Candidato | Vacante | Afirmaciones |
|---|---|---|
| CAN-101 | VAC-01 | 3 |
| CAN-102 | VAC-01 | 3 |
| CAN-103 | VAC-01 | 3 |
| CAN-104 | VAC-01 | 3 |
| CAN-105 | VAC-01 | 3 |
| CAN-106 | VAC-01 | 3 |
| CAN-107 | VAC-02 | 2 |
| CAN-108 | VAC-02 | 0 |
| CAN-109 | VAC-03 | 2 |
| CAN-110 | VAC-01 | 3 |
| CAN-111 | VAC-01 | 3 |

Cada afirmación se contrasta con su soporte; ninguna se da por falsa: se dice cuál no tiene soporte o no coincide.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-103/certificado-laboral.pdf`
- `30-candidatos/VAC-01/CAN-103/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-110/tarjeta-profesional.pdf`
- `30-candidatos/VAC-01/CAN-111/hoja-de-vida.pdf`

La corrida quedó registrada como `2026-11-16-cv-check-1`. La salida completa está en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-cv-check.md`.