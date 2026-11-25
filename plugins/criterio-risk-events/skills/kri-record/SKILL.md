---
name: kri-record
description: "Cómo se registra en la ficha del periodo de Casandra cada acción sobre un indicador clave de riesgo que quedó en un acta del comité de riesgos o de la junta, con la cita. Úsalo al procesar `40-actas/`. KRI record, committee actions."
---

# La ficha del periodo de Casandra

Una ficha por periodo, en `<estado>/eventos/<AAAA-MM>/ficha.json`. Los indicadores, sus valores, la tabla de acciones y la base de eventos no se copian aquí: los procesa el motor. Aquí va lo que solo traen las actas.

```json
{
  "actions": [{"indicator": "KRI-01", "action": "Bloqueo preventivo de los BIN comprometidos",
               "source": "40-actas/acta_comite_riesgos_2026-10.pdf, p. 2"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`actions`**: cada acción que el acta acuerda sobre un indicador clave del periodo, con el código del indicador como lo escribe la tabla de indicadores —o su nombre, si el acta no trae el código—, la acción en las palabras del acta y la cita. Una mención del indicador sin una acción acordada no es una acción.
- **`reviewed`**: las actas de `40-actas/` que se procesaron y no traen ninguna acción sobre un indicador. Un acta citada en una acción no va aquí.

## Lo que nunca va

- Una acción deducida: si el acta solo dice que el indicador subió, no hay acción.
- Un umbral, una calificación o un monto que el acta no dice.
