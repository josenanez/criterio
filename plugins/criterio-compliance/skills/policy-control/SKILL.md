---
name: policy-control
description: "Cómo se lleva el índice de políticas de la organización —código, versión, responsable, aprobación y próxima revisión— y cuándo una revisión está vencida. Úsalo al revisar las políticas, al recibir una versión nueva o cuando alguien pregunta qué política toca revisar. Policy index, policy review cycle."
---

# Las políticas

## El índice

La organización lleva `20-politicas/indice-politicas.csv` o `.xlsx`, una fila por política:

| Columna | Qué va |
|---|---|
| `codigo` | `P-04` |
| `politica` | El nombre |
| `version` | La versión vigente |
| `responsable` | Quién la mantiene |
| `aprobada` | La fecha en que se aprobó la versión vigente |
| `proxima_revision` | La fecha en que se tiene que revisar |

Cada política va en la misma carpeta, con su código al inicio del nombre. La fecha de revisión la fija la organización: Constanza no propone ciclos.

## Lo que hace el motor

Ordena las políticas por su próxima revisión, con los días que faltan o que pasaron, y levanta `policy_review_overdue` para cada una cuya revisión ya venció. Una versión nueva se registra cuando la organización actualiza el índice; mientras el índice no cambie, la revisión sigue vencida aunque exista un borrador.

## Lo que nunca se hace

- Opinar sobre el contenido de una política, ni compararla con una norma.
- Redactar una política o su actualización.
- Mover la fecha de revisión.
