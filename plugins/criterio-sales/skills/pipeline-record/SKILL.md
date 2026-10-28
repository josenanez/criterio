---
name: pipeline-record
description: "Cómo se registra en la ficha del periodo de Augusto lo que solo traen los documentos escritos: cada documento de evidencia de una oportunidad —la propuesta, la orden de compra, el acta de aceptación— con su tipo, su monto y su fecha, y el pronóstico que se comprometió en el comité, cada dato con su cita. Úsalo al procesar `30-evidencia/` o un acta del comité comercial. Pipeline evidence record, committed forecast."
---

# La ficha del periodo de Augusto

Una ficha por periodo, en `<estado>/comercial/<AAAA-MM>/ficha.json`. Las exportaciones del CRM y las tablas de referencia no se copian aquí: las procesa el motor. Aquí va solo lo que no es una tabla.

```json
{
  "evidence": [
    {"opportunity": "OPP-1042", "type": "propuesta", "amount": 120000000, "date": "2026-09-18",
     "source": "30-evidencia/OPP-1042_propuesta.pdf, p. 1"},
    {"opportunity": "OPP-1042", "type": "orden_compra", "amount": 118500000, "date": "2026-10-09",
     "source": "30-evidencia/OPP-1042_orden-compra.pdf"}
  ],
  "declared_forecast": {"value": 950000000, "date": "2026-10-02",
                        "source": "20-comite/acta-comite-2026-10-02.pdf, p. 2"},
  "questions": [{"question": "¿La orden de OPP-1077 es la del 9 de octubre?", "answer": "Sí",
                 "source": "conversación del 2026-10-15"}]
}
```

## Cómo se decide cada uno

- **`evidence`**: un registro por documento. `opportunity` es el id con que el CRM la exporta —el mismo con que empieza el nombre del archivo—. `type` es lo que el documento es: `propuesta`, `orden_compra` o `acta_aceptacion`, el mismo vocabulario de la columna `exige` de la tabla de etapas. `amount` y `date` son los del documento, no los del CRM; si el documento no los trae, se dejan vacíos. **Un documento que dice ser una propuesta y no lo es** —un borrador sin enviar, una cotización interna— no va como propuesta: va como pregunta.
- **`declared_forecast`**: el valor que el comité **comprometió** para el periodo, con sus palabras —«comprometemos», «commit», «el pronóstico del mes es»—. No es el mejor escenario ni el pipeline total: si el acta trae varios, va el comprometido y los demás no. Si el acta no compromete un valor, no va; el motor dice que falta.
- **`questions`**: lo que se le preguntó a la persona y lo que respondió. Una pregunta sin respuesta lleva `"answer": null`.

## Lo que nunca va

- El correo, el teléfono o el nombre de un contacto del cliente. La ficha guarda la cuenta y la oportunidad.
- Un monto o una fecha que el documento no dice.
- Una calificación de la oportunidad o de quien la lleva.
