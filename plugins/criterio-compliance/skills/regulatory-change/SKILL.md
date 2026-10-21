---
name: regulatory-change
description: "Cómo se sigue una norma nueva desde que llega hasta que la organización evalúa su impacto y la lleva a la matriz: el registro normativo, los días sin evaluación y la norma que aplica y ninguna obligación cita. Úsalo al recibir un boletín, una circular o un correo sobre una norma, o al revisar el registro normativo. Regulatory change management, regulatory watch."
---

# Las normas nuevas

## De dónde vienen

Constanza **no vigila boletines oficiales ni dice qué norma salió**. Procesa lo que la organización recibe y registra:

- **El registro normativo**, `30-normativa/registro-normativo.csv` o `.xlsx`: `id`, `norma`, `registrada` (la fecha en que la organización la registró) y, si las tiene, `publicada`, `aplica`, `evaluacion` (la fecha de la evaluación de impacto) y `responsable`.
- **Lo que trae un documento escrito** —un boletín de un gremio, una circular, un correo del asesor— y el registro todavía no tiene: se extrae a `new_rules` de la ficha del periodo, aplicando **compliance-record**, con la fecha en que llegó.

## Lo que hace el motor

| Señal | Cuándo |
|---|---|
| `regulatory_change_unassessed` | Una norma lleva más de los días configurados desde que se registró sin evaluación de impacto |
| `applicable_norm_not_in_matrix` | La organización marcó que la norma aplica y ninguna obligación de la matriz la cita en su `fuente` |

Para que cruce, la `fuente` de la obligación de la matriz lleva el id de la norma del registro: `N-2026-14 · Circular 031 de 2026`.

## Lo que nunca se hace

- Decir si una norma aplica, qué exige o desde cuándo rige: eso es la evaluación de impacto, y la hace una persona.
- Citar de memoria una norma, un artículo o un plazo.
- Agregar una obligación a la matriz porque una norma la exigiría.
