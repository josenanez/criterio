# /criterio-talent:candidate-fit 

Los términos están vigentes (versión 1.5, aceptados antes). Abajo está el reporte tal cual, en el orden del identificador de cada candidato y sin puntaje.

# Cada candidato contra el perfil · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555123) · **Fecha de corte:** 2026-11-16 · **Agente:** Cándido 0.1.0 · **Comando:** `candidate-fit`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Requisito esencial sin evidencia (`requirement_not_evidenced`) | CAN-101: R1 «Contabilidad bajo NIIF» del perfil PC-01 no tiene evidencia en la hoja de vida ni en sus soportes | `30-candidatos/VAC-01/CAN-101/hoja-de-vida.pdf` |
| 2 | Ídem | CAN-108: R1 «Finanzas y análisis de estados financieros» del perfil PC-04 | `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf` |
| 3 | Ídem | CAN-108: R3 «Criterio y toma de decisiones de crédito» del perfil PC-04 | `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf` |

## El resultado

Cada fila indica si el requisito es esencial (Esc.), cuántas evidencias hay y dónde. «Soporte» es sí o no según haya un documento de soporte, aparte de la hoja de vida.

**VAC-01 · perfil PC-01** (R1 Contabilidad bajo NIIF · R2 Análisis de procesos contables · R3 Evaluación y control de actividades del área · R4 Tarjeta profesional de contador vigente)

| Candidato | R1 (esc.) | R2 (esc.) | R3 | R4 (esc.) |
|---|---|---|---|---|
| CAN-101 | 0 · sin evidencia | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-102 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-103 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-104 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-105 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-106 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-110 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · soporte `tarjeta-profesional.pdf` |
| CAN-111 | 1 · HV p. 1 | 1 · HV p. 1 | 0 | 2 · solo HV p. 1, sin soporte |

**VAC-02 · perfil PC-04** (R1 Finanzas y análisis de estados financieros · R2 Contabilidad · R3 Criterio y toma de decisiones de crédito · R4 Gozar de buen estado de salud)

| Candidato | R1 (esc.) | R2 | R3 (esc.) | R4 |
|---|---|---|---|---|
| CAN-107 | 1 · HV p. 1 | 0 | 1 · HV p. 1 | 0 |
| CAN-108 | 0 · sin evidencia | 0 | 0 · sin evidencia | 0 |

**VAC-03 · perfil PC-03** (R1 Comprensión de lectura de documentos contables · R2 Contabilidad básica)

| Candidato | R1 | R2 (esc.) |
|---|---|---|
| CAN-109 | 0 | 1 · HV p. 1 |

Salvo CAN-111 en R4, ninguna evidencia de hoja de vida tiene soporte. Las rutas completas están en `<estado>/seleccion/2026-11/reporte-candidate-fit.md`; todas son del tipo `30-candidatos/<vacante>/<candidato>/hoja-de-vida.pdf`.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hice

Ninguna en esta corrida.

## Fuentes

- `30-candidatos/VAC-01/CAN-101/hoja-de-vida.pdf`
- `30-candidatos/VAC-02/CAN-108/hoja-de-vida.pdf`

La tabla de resultados arriba es un resumen mío del reporte. El texto íntegro del motor, con cada ruta, está en `estado-talento/901555123-banco-cordillera-sintetico/seleccion/2026-11/reporte-candidate-fit.md`. La salida que dejé en `corridas/salida-candidate-fit.md` es ese texto íntegro, no este resumen.

La corrida quedó registrada como `2026-11-16-candidate-fit-1`, con 15 hallazgos.

El requisito R4 «Gozar de buen estado de salud» del perfil PC-04 es un dato de salud. Este comando no lo evalúa. Conviene revisarlo con `/criterio-roles:profile-language`.