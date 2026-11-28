# /criterio-talent:privacy-check 

Los términos vigentes (versión 1.6) ya estaban aceptados, así que no registré ninguna aceptación nueva. Este es el reporte del motor, tal cual.

# La autorización y la conservación de los datos · Almacenes del Pacífico Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Pacífico Sintéticos (1792345678001) · **Fecha de corte:** 2026-11-16 · **Agente:** Cándido 1.0.0 · **Comando:** `privacy-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Datos que pasaron la conservación y siguen en la carpeta (`retention_exceeded`) | CAN-609: su proceso terminó el 2026-06-09. La política conserva 120 días, hasta el 2026-10-07. | 40 | `50-ats/exportacion-ats.csv` fila 10 · `30-candidatos/VAC-53/CAN-609/hoja-de-vida.pdf` |
| 2 | Sin autorización de tratamiento de datos (`consent_missing`) | CAN-604: no está en el registro de autorizaciones. | — | `30-candidatos/VAC-51/CAN-604/hoja-de-vida.pdf` |
| 3 | Autorización posterior a recibir los datos (`consent_missing`) | CAN-607: la autorización es del 2026-09-17 y sus datos llegaron el 2026-09-05. | — | `40-autorizaciones/registro-autorizaciones.csv` fila 7 · `30-candidatos/VAC-52/CAN-607/hoja-de-vida.pdf` |
| 4 | Dato que no se debe tratar (`protected_data_received`) | CAN-602: llegó fotografía. Se excluye del análisis. | — | `30-candidatos/VAC-51/CAN-602/foto.jpg` · `hoja-de-vida.pdf` |
| 5 | Dato que no se debe tratar (`protected_data_received`) | CAN-606: llegó fecha de nacimiento. Se excluye del análisis. | — | `30-candidatos/VAC-51/CAN-606/hoja-de-vida.pdf` |
| 6 | Dato que no se debe tratar (`protected_data_received`) | CAN-606: llegó fotografía. Se excluye del análisis. | — | `30-candidatos/VAC-51/CAN-606/foto.jpg` · `hoja-de-vida.pdf` |

## El resultado

Conservación de la política: 120 días.

| Candidato | Recibido | Autorización | Estado | Conservar hasta | Excluido |
|---|---|---|---|---|---|
| CAN-601 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-602 | 2026-09-05 | 2026-09-05 | Entrevista | — | fotografía |
| CAN-603 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-604 | 2026-09-05 | — | Entrevista | — | — |
| CAN-605 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-606 | 2026-09-05 | 2026-09-05 | Entrevista | — | fecha de nacimiento, fotografía |
| CAN-607 | 2026-09-05 | 2026-09-17 | Entrevista | — | — |
| CAN-608 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |
| CAN-609 | 2026-03-01 | 2026-03-01 | No seleccionado | 2026-10-07 | — |
| CAN-610 | 2026-09-05 | 2026-09-05 | Entrevista | — | — |

Lo excluido no se copia ni se usa: aquí solo se dice que llegó.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Las tres se resolvieron con respuestas sugeridas, porque la sesión no tiene interfaz:
- Plazo de cobertura de una vacante: 30 días.
- Días de conservación de los datos: 120.
- ¿Se publican los reportes en Rostrum?: no.

## Fuentes

Las fuentes son las hojas de vida y fotos de CAN-602, CAN-604, CAN-606, CAN-607 y CAN-609. También `40-autorizaciones/registro-autorizaciones.csv` y `50-ats/exportacion-ats.csv`.

---

No borré ni moví datos. La supresión de los de CAN-609 la hace una persona.

La corrida quedó registrada como `2026-11-16-privacy-check-1` (13 hallazgos). Lo que te mostré está en `corridas/salida-privacy-check.md`, dentro de la carpeta de estado de la entidad.