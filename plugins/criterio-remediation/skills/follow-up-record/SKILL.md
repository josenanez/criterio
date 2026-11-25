---
name: follow-up-record
description: "Cómo se registra en la ficha del periodo de Remedios cada evidencia de implementación, cada explicación de atraso y cada hallazgo de un informe del revisor fiscal, del auditor externo o del supervisor, con la cita. Úsalo al procesar `30-seguimiento/`. Follow-up record, implementation evidence, external findings."
---

# La ficha del periodo de Remedios

Una ficha por periodo, en `<estado>/seguimiento/<AAAA-MM>/ficha.json`. El registro de hallazgos y el de riesgos aceptados no se copian aquí: los procesa el motor. Aquí va lo que solo traen los documentos.

```json
{
  "evidence": [{"finding": "H-10", "date": "2025-09-18", "what": "Constancia de constitución de las garantías",
                "source": "30-seguimiento/H-10/evidencia.pdf"}],
  "delay_explanations": [{"finding": "H-04", "date": "2026-10-02", "what": "El proveedor entrega el ajuste en diciembre",
                          "source": "30-seguimiento/H-04/explicacion.pdf"}],
  "external_findings": [{"id": "RF-03", "issuer": "Revisor fiscal", "title": "Caja menor sin arqueo",
                         "source": "30-seguimiento/informe_revisor_2026.pdf, p. 9"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`evidence`**: un documento por cada hallazgo que lo soporta, con la fecha que consta en él y, en `what`, el título del documento en sus palabras. Que la evidencia **sostenga** el cierre lo valida el auditor; aquí solo se registra que existe y qué dice.
- **`delay_explanations`**: la explicación documentada de un atraso, con la fecha que consta en ella y, en `what`, su título (norma 15.2).
- **`external_findings`**: cada hallazgo de un informe externo con el identificador y el título que le da ese informe, en sus palabras. El motor lo busca en el registro por su identificador o por su `referencia_externa`.
- **`reviewed`**: los documentos de `30-seguimiento/` que se procesaron y no traen nada para la ficha. Un documento citado en otro campo —una evidencia, una explicación, el informe externo— no va aquí.

## Lo que nunca va

- Una evidencia que no está en la carpeta, ni una explicación de palabra.
- Un cierre o una validación: los registra la organización en su registro de hallazgos, no la ficha.
