---
name: compliance-record
description: "Cómo se registra en la ficha del periodo lo que solo dicen los documentos escritos de cumplimiento: el estado que declara el informe del periodo, las normas nuevas que trae un boletín o un correo y las preguntas que se le hicieron a la persona, cada una con su cita. Úsalo al procesar el informe de cumplimiento, un boletín normativo o una respuesta del responsable. Compliance period record, declared status."
---

# La ficha del periodo de cumplimiento

Una ficha por periodo, en `<estado>/cumplimiento/<AAAA-MM>/ficha.json`. Las tablas —la matriz, el índice de políticas, el registro normativo, los casos— no se copian aquí: las procesa el motor. Aquí va solo lo que no es una tabla.

```json
{
  "declared": {"status": "cumplido", "date": "2026-10-05",
               "source": "cumplimiento-2026-09/20-reportes/informe-cumplimiento-sep.pdf, p. 1"},
  "new_rules": [{"id": "N-2026-14", "rule": "Circular externa 031 de 2026", "date": "2026-09-22", "applies": "por evaluar",
                 "source": "30-normativa/boletin-2026-09.pdf, p. 3"}],
  "questions": [{"question": "¿La evidencia de OB-04 es el acta del 2 de octubre?", "answer": "Sí, la subo con su id",
                 "source": "conversación del 2026-10-06"}]
}
```

## Cómo se decide cada uno

- **`declared`** es lo que dice el informe del periodo o quien lo firma, con sus palabras: `cumplido`, `en cumplimiento`, `sin novedades`, `con hallazgos`. Si el informe no declara un estado, no va. **Lo declarado no se fusiona con lo evidenciado**: el motor los pone uno al lado del otro y levanta `declared_compliance_vs_evidence` cuando se declara cumplido con señales abiertas.
- **`new_rules`**: cada norma nueva que trae un documento escrito y que el registro normativo todavía no tiene, con la fecha en que llegó. `applies` es lo que dice el documento o la persona —`sí`, `no`, `por evaluar`—, nunca lo que el agente cree. En cuanto la organización la lleva al registro normativo, la tabla manda.
- **`questions`**: lo que se le preguntó a la persona y lo que respondió. Una pregunta sin respuesta lleva `"answer": null`.

## Lo que nunca se hace

- Resumir el informe ni calificarlo.
- Decidir si una norma aplica a la organización o qué exige.
- Registrar como declarado lo que el agente concluye: declarar es de una persona.
