# /criterio-talent:privacy-check 

Revisé a los diez candidatos del periodo contra el registro de autorizaciones y la conservación de la política. No borré ni moví nada: la supresión la hace una persona.

Los términos (versión 1.6) ya estaban vigentes, así que no hizo falta registrar una aceptación nueva.

# La autorización y la conservación de los datos · Nube Austral Software Sintética · periodo 2026-11

**Entidad:** Nube Austral Software Sintética (76543210k) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `privacy-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Los datos pasaron el tiempo de conservación y siguen en la carpeta (`retention_exceeded`) | CAN-309: su proceso terminó el 2026-07-09; la política conserva los datos 90 días, hasta el 2026-10-07, y siguen en la carpeta | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-23/CAN-309/hoja-de-vida.pdf` |
| 2 | No hay autorización de tratamiento de datos, o es posterior a recibir los datos (`consent_missing`) | CAN-304: no está en el registro de autorizaciones | — | `30-candidatos/VAC-21/CAN-304/hoja-de-vida.pdf` |
| 3 | Igual que la anterior (`consent_missing`) | CAN-307: la autorización es del 2026-09-17, después de recibir sus datos el 2026-09-05 | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-22/CAN-307/hoja-de-vida.pdf` |
| 4 | Llegó un dato que no se debe tratar y se excluye del análisis (`protected_data_received`) | CAN-302: llegó fotografía | — | `30-candidatos/VAC-21/CAN-302/foto.jpg` · `30-candidatos/VAC-21/CAN-302/hoja-de-vida.pdf` |
| 5 | Ídem (`protected_data_received`) | CAN-306: llegó fecha de nacimiento | — | `30-candidatos/VAC-21/CAN-306/hoja-de-vida.pdf` |
| 6 | Ídem (`protected_data_received`) | CAN-306: llegó fotografía | — | `30-candidatos/VAC-21/CAN-306/foto.jpg` · `30-candidatos/VAC-21/CAN-306/hoja-de-vida.pdf` |

## El resultado

**Conservación de la política:** 90 días.

| Candidato | Recibido | Autorización | Estado | Conservar hasta | Excluido |
|---|---|---|---|---|---|
| CAN-301 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-302 | 2026-09-05 | 2026-09-05 | Entrevista | — | fotografía |
| CAN-303 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-304 | 2026-09-05 | — | Entrevista | — | — |
| CAN-305 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-306 | 2026-09-05 | 2026-09-05 | Entrevista | — | fecha de nacimiento, fotografía |
| CAN-307 | 2026-09-05 | 2026-09-17 | Entrevista | — | — |
| CAN-308 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-309 | 2026-06-01 | 2026-06-01 | No seleccionado | 2026-10-07 | — |
| CAN-310 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |

Lo excluido no se copia ni se usa: aquí solo se dice que llegó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

La corrida quedó registrada como `2026-11-16-privacy-check-1`. El reporte completo está en `estado-talento/76543210k-nube-austral-software-sintetica/seleccion/2026-11/reporte-privacy-check.md`. Quité la columna "Monto" y "Responsable" de la tabla de arriba porque iban vacías; el archivo original las conserva.