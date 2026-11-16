# /criterio-talent:candidate-fit 

Los términos están vigentes (versión 1.5). El requisito R4 del perfil PC-04, «Gozar de buen estado de salud», es un dato de salud, que la política no permite usar. El motor no lo usa para decidir, y conviene revisarlo con Norma.

# Cada candidato contra el perfil · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Procesado:** 2026-11-16 · **Agente:** Cándido, versión 0.1.0 · **Comando:** `candidate-fit`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Requisito esencial sin evidencia (`requirement_not_evidenced`) | CAN-101: R1 «Contabilidad bajo NIIF» del perfil PC-01 no tiene evidencia ni en la hoja de vida ni en sus soportes | `30-candidatos/VAC-01/CAN-101/hoja-de-vida.pdf` |
| 2 | Requisito esencial sin evidencia (`requirement_not_evidenced`) | CAN-108: R1 «Finanzas y análisis de estados financieros» del perfil PC-04 no tiene evidencia ni en la hoja de vida ni en sus soportes | `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf` |
| 3 | Requisito esencial sin evidencia (`requirement_not_evidenced`) | CAN-108: R3 «Criterio y toma de decisiones de crédito» del perfil PC-04 no tiene evidencia ni en la hoja de vida ni en sus soportes | `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf` |

## El resultado

Cada candidato tiene una tabla con sus requisitos. Cada fila trae si el requisito es esencial, cuántas evidencias hay, si tiene soporte y dónde está. La columna «Evidencias» viene del motor.

**VAC-01 · perfil PC-01** (R1 Contabilidad bajo NIIF, esencial; R2 Análisis de procesos contables, esencial; R3 Evaluación y control de actividades del área, no esencial; R4 Tarjeta profesional de contador vigente, esencial)

| Candidato | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| CAN-101 | 0 · sin evidencia | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-102 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-103 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-104 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-105 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-106 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-110 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 2 · con soporte: `tarjeta-profesional.pdf` |
| CAN-111 | 1 · hoja de vida p. 1 | 1 · hoja de vida p. 1 | 0 | 1 · solo la hoja de vida p. 1, sin soporte |

Cada ruta es `30-candidatos/VAC-01/<candidato>/hoja-de-vida.pdf` o `.../tarjeta-profesional.pdf`.

**VAC-02 · perfil PC-04** (R1 Finanzas y análisis de estados financieros, esencial; R2 Contabilidad, no esencial; R3 Criterio y toma de decisiones de crédito, esencial; R4 Gozar de buen estado de salud, no esencial)

| Candidato | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| CAN-107 | 1 · hoja de vida p. 1 | 0 | 1 · hoja de vida p. 1 | 0 |
| CAN-108 | 0 · sin evidencia | 0 | 0 · sin evidencia | 0 |

**VAC-03 · perfil PC-03** (R1 Comprensión de lectura de documentos contables, no esencial; R2 Contabilidad básica, esencial)

| Candidato | R1 | R2 |
|---|---|---|
| CAN-109 | 0 | 1 · `30-candidatos/VAC-03/CAN-109/hoja-de-vida.pdf`, p. 1 |

Los candidatos van en el orden de su identificador, por vacante. No hay puntaje ni orden por número: quien selecciona decide.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-candidatos/VAC-01/CAN-101/hoja-de-vida.pdf`
- `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf`

---

Resumí las tablas por vacante para esta vista, y los datos son los mismos que dio el motor. El reporte completo, con una tabla por candidato, está en `seleccion/2026-11/reporte-candidate-fit.md` dentro de la carpeta de estado. Ahí el motor lo dejó en el orden estricto de identificador (CAN-101 a CAN-111), mezclando vacantes. Mi resumen agrupa por vacante, así que CAN-110 y CAN-111 aparecen con VAC-01.

La salida quedó en `corridas/salida-candidate-fit.md`. Es el reporte tal cual, precedido de la nota sobre R4, y no esta versión resumida. La corrida quedó registrada como `2026-11-16-candidate-fit-1`, con 15 hallazgos.