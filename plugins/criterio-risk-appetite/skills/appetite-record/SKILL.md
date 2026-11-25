---
name: appetite-record
description: "Cómo se registra en la ficha del periodo de Severo la declaración de apetito con la fecha de su última revisión por la junta, y cada exceso de un límite que aprobó el comité de riesgos o la junta, con la cita. Úsalo al procesar `00-marco/` y `40-actas/`. Appetite record, board review, approved breaches."
---

# La ficha del periodo de Severo

Una ficha por periodo, en `<estado>/apetito/<AAAA-MM>/ficha.json`. La matriz, los límites, los indicadores, la exposición y los planes de acción no se copian aquí: los procesa el motor. Aquí va lo que solo traen la declaración y las actas.

```json
{
  "statement": {"name": "Declaración de apetito por riesgo", "board_review": "2025-08-28",
                "source": "00-marco/declaracion_de_apetito.pdf, p. 1"},
  "approvals": [{"limit": "L-03", "until": "2027-01-31", "source": "40-actas/acta_comite_riesgos_2026-10.pdf, p. 3"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`statement`**: la declaración de apetito, con el nombre que le da su documento y la fecha de la sesión en que la junta la aprobó o la revisó por última vez. Si un acta de la junta posterior dice que la revisó, vale esa fecha, y la cita es el acta. Si ningún documento dice la fecha, va vacía y se pregunta.
- **`approvals`**: cada exceso de un límite que el comité de riesgos o la junta aprobó, con el código del límite como lo escribe la tabla de límites, la fecha hasta la que vale la aprobación si el acta la dice y la cita del acta. Una discusión sin decisión no es una aprobación.
- **`reviewed`**: los documentos de `00-marco/` y `40-actas/` que se procesaron y no traen nada para la ficha. Un documento citado en otro campo no va aquí, ni las tablas que procesa el motor.

## Lo que nunca va

- Un límite, un umbral o un plazo que el documento no dice, completado para que la ficha se vea entera.
- Una aprobación deducida: si el acta no dice que se aprobó el exceso, no hay aprobación.
