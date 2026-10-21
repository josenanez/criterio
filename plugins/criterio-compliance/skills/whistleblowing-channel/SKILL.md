---
name: whistleblowing-channel
description: "Cómo se siguen los plazos de los casos del canal de denuncias sin procesar quién denunció ni qué dijo: el registro de casos con su fecha de recepción y de respuesta, y el caso abierto más allá del plazo configurado. Úsalo al revisar el canal de denuncias o el registro de casos. Whistleblowing channel case deadlines, ethics hotline."
---

# El canal de denuncias

## Solo los plazos

Constanza procesa **el registro de casos**, `40-canal/casos.csv` o `.xlsx`, con estas columnas y ninguna más:

| Columna | Qué va |
|---|---|
| `id` | El número del caso |
| `recibido` | La fecha de recepción |
| `respondido` | La fecha de la respuesta o del cierre; vacía si sigue abierto |
| `tipo` | La categoría que use la organización |
| `estado` | Abierto, en investigación, cerrado |

**El registro no lleva quién denunció, a quién se denuncia ni qué se denunció**, y Constanza no abre los expedientes. Si el archivo trae columnas con esos datos, no se procesan ni se muestran, y se le dice a la persona que el registro para Constanza va sin ellas.

## Lo que hace el motor

Calcula los días de cada caso —hasta la respuesta, o hasta hoy si sigue abierto— y levanta `report_case_overdue` para el caso abierto que pasó el plazo de respuesta de la configuración. El plazo lo fija la organización según su procedimiento; Constanza no lo propone como norma.

## Lo que nunca se hace

- Leer, resumir ni clasificar el contenido de una denuncia.
- Identificar o inferir quién denunció.
- Opinar sobre una investigación o su resultado.
