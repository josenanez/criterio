# /criterio-talent:privacy-check 

Los términos de la versión 1.5 ya estaban vigentes, así que no hizo falta registrar la aceptación. El reporte señala 1 candidato con la conservación vencida, 2 sin autorización válida y 2 con datos que no se deben tratar. No borré ni moví nada: la supresión la decide una persona.

# La autorización y la conservación de los datos · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `privacy-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta (`retention_exceeded`) | CAN-109: su proceso terminó el 2026-04-10; la política conserva los datos 180 días, hasta el 2026-10-07, y siguen en la carpeta | — | — | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-03/CAN-109/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-104: no está en el registro de autorizaciones de tratamiento de datos | — | — | — | `30-candidatos/VAC-01/CAN-104/hoja-de-vida.pdf` |
| 3 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-107: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | — | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-02/CAN-107/hoja-de-vida.pdf` |
| 4 | Llegó un dato que no se debe tratar (`protected_data_received`) | CAN-102: llegó fotografía; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-01/CAN-102/foto.jpg` · `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf` |
| 5 | Llegó un dato que no se debe tratar (`protected_data_received`) | CAN-106: llegó fecha de nacimiento; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-01/CAN-106/hoja-de-vida.pdf` |
| 6 | Llegó un dato que no se debe tratar (`protected_data_received`) | CAN-106: llegó fotografía; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-01/CAN-106/foto.jpg` · `30-candidatos/VAC-01/CAN-106/hoja-de-vida.pdf` |

## El resultado

**Conservación de la política:** 180 días.

| Candidato | Recibido | Autorización | Estado | Conservar hasta | Excluido |
|---|---|---|---|---|---|
| CAN-101 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-102 | 2026-09-05 | 2026-09-05 | Entrevista | — | fotografía |
| CAN-103 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-104 | 2026-09-05 | — | Entrevista | — | — |
| CAN-105 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-106 | 2026-09-05 | 2026-09-05 | Entrevista | — | fecha de nacimiento, fotografía |
| CAN-107 | 2026-09-05 | 2026-09-17 | Entrevista | — | — |
| CAN-108 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-109 | 2026-02-01 | 2026-02-01 | No seleccionado | 2026-10-07 | — |
| CAN-110 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-111 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |

Lo excluido no se copia ni se usa: aquí solo se dice que llegó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-candidatos/VAC-01/CAN-102/foto.jpg`
- `30-candidatos/VAC-01/CAN-102/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-104/hoja-de-vida.pdf`
- `30-candidatos/VAC-01/CAN-106/foto.jpg`
- `30-candidatos/VAC-01/CAN-106/hoja-de-vida.pdf`
- `30-candidatos/VAC-02/CAN-107/hoja-de-vida.pdf`
- `30-candidatos/VAC-03/CAN-109/hoja-de-vida.pdf`
- `40-autorizaciones/registro-autorizaciones.csv`
- `50-ats/exportacion-ats.csv`

La corrida quedó registrada como `2026-11-16-privacy-check-1`. La salida que mostré está en `estado-talento/901555123-banco-cordillera-sintetico/corridas/salida-privacy-check.md`.