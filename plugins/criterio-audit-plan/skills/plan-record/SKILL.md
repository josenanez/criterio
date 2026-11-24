---
name: plan-record
description: "Cómo se registra en la ficha del periodo de Prudencia cada acta del comité o del consejo que aprueba el plan o lo cambia —qué trabajo agrega, cancela o aplaza, quién lo aprobó y la cita— y la razón cuando el plan no considera un área. Úsalo al procesar las actas de `10-plan/`. Audit plan record, committee minutes."
---

# La ficha del periodo de Prudencia

Una ficha por periodo, en `<estado>/plan/<AAAA-MM>/ficha.json`. El universo, la matriz y el plan no se copian aquí: los procesa el motor. Aquí va solo lo que traen las actas.

```json
{
  "approvals": [
    {"engagement": "TR-05", "change": "cancela", "approved_by": "Comité de auditoría", "date": "2026-07-15",
     "source": "10-plan/actas/acta-2026-07.pdf, p. 3"}
  ],
  "areas_not_considered": {"fraude": "lo cubre el trabajo de cumplimiento del área de riesgos, según el acta del 15 de julio"},
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`approvals`**: una entrada por cada trabajo que un acta aprueba agregar, cancelar o aplazar. `change` es `agrega`, `cancela` o `aplaza`; `approved_by`, el órgano tal como lo dice el acta. Un acta que solo menciona el cambio sin aprobarlo no va.
- **`areas_not_considered`**: solo si un documento dice por qué el plan no considera el gobierno de TI (`ti`), el riesgo de fraude (`fraude`) o los programas de cumplimiento y ética (`cumplimiento`). La razón va con su fuente; sin documento, no va.
- **`reviewed`**: los documentos de `10-plan/` que se procesaron y no traen nada para la ficha.

## Lo que nunca va

- Una aprobación que el acta no dice, ni un órgano distinto del que firma.
- Una prioridad, un trabajo o un riesgo inventado: el plan y la matriz los procesa el motor.
