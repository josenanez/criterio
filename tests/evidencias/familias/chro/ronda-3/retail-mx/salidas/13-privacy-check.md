# /criterio-talent:privacy-check 

Los términos (versión 1.6) están vigentes. Este comando no los registra, y no hizo falta. El reporte tiene seis señales: una de conservación, dos de autorización y tres de datos que no se deben tratar. No borré ni moví ningún dato; la supresión la hace una persona.

# La autorización y la conservación de los datos · Tiendas del Bajío Sintéticas · periodo 2026-11

**Entidad:** Tiendas del Bajío Sintéticas (TBA110315K21) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `privacy-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Los datos de un candidato pasaron el tiempo de conservación de la política y siguen en la carpeta (`retention_exceeded`) | CAN-209: su proceso terminó el 2026-06-09; la política conserva los datos 120 días, hasta el 2026-10-07, y siguen en la carpeta | — | — | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-13/CAN-209/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-204: no está en el registro de autorizaciones de tratamiento de datos | — | — | — | `30-candidatos/VAC-11/CAN-204/hoja-de-vida.pdf` |
| 3 | No hay autorización de tratamiento de datos del candidato, o es posterior a recibir sus datos (`consent_missing`) | CAN-207: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | — | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-12/CAN-207/hoja-de-vida.pdf` |
| 4 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-202: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-11/CAN-202/foto.jpg` · `30-candidatos/VAC-11/CAN-202/hoja-de-vida.pdf` |
| 5 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-206: llegó fecha de nacimiento; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-11/CAN-206/hoja-de-vida.pdf` |
| 6 | Llegó un dato que no se debe tratar —fotografía, edad, documento de identidad, salud—, y se excluye del análisis (`protected_data_received`) | CAN-206: llegó fotografia; se excluye del análisis y no se usa para nada | — | — | — | `30-candidatos/VAC-11/CAN-206/foto.jpg` · `30-candidatos/VAC-11/CAN-206/hoja-de-vida.pdf` |

## El resultado

**Conservación de la política:** 120 días.

| Candidato | Recibido | Autorización | Estado | Conservar hasta | Excluido |
|---|---|---|---|---|---|
| CAN-201 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-202 | 2026-09-05 | 2026-09-05 | Entrevista | — | fotografia |
| CAN-203 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-204 | 2026-09-05 | — | Entrevista | — | — |
| CAN-205 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-206 | 2026-09-05 | 2026-09-05 | Entrevista | — | fecha de nacimiento, fotografia |
| CAN-207 | 2026-09-05 | 2026-09-17 | Entrevista | — | — |
| CAN-208 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-209 | 2026-03-01 | 2026-03-01 | No seleccionado | 2026-10-07 | — |
| CAN-210 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |

Lo excluido no se copia ni se usa: aquí solo se dice que llegó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-candidatos/VAC-11/CAN-202/foto.jpg`
- `30-candidatos/VAC-11/CAN-202/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-204/hoja-de-vida.pdf`
- `30-candidatos/VAC-11/CAN-206/foto.jpg`
- `30-candidatos/VAC-11/CAN-206/hoja-de-vida.pdf`
- `30-candidatos/VAC-12/CAN-207/hoja-de-vida.pdf`
- `30-candidatos/VAC-13/CAN-209/hoja-de-vida.pdf`
- `40-autorizaciones/registro-autorizaciones.csv`
- `50-ats/exportacion-ats.csv`

La corrida quedó registrada como `2026-11-16-privacy-check-1`. La salida completa está en `corridas/salida-privacy-check.md` dentro de la carpeta de estado.