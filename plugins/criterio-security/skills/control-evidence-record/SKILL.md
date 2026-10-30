---
name: control-evidence-record
description: "Cómo se registra en la ficha del periodo de Alexis lo que solo traen los documentos escritos: la evidencia de que un control operó, cada revisión de accesos y cada evaluación de un tercero, con su fecha y su cita. Úsalo al procesar `10-controles/`, `20-accesos/` o `30-terceros/`. Control evidence record, access review, third-party assessment."
---

# La ficha del periodo de Alexis

Una ficha por periodo, en `<estado>/seguridad/<AAAA-MM>/ficha.json`. La declaración de aplicabilidad, la tabla de sistemas, el registro de terceros y el de riesgos no se copian aquí: los procesa el motor. Aquí va solo lo que no es una tabla.

```json
{
  "evidence": [
    {"control": "A.8.13", "date": "2026-09-30", "title": "Informe de respaldos de septiembre",
     "source": "10-controles/A.8.13_informe-respaldos_2026-09.pdf, p. 1"}
  ],
  "access_reviews": [
    {"system": "Core bancario", "date": "2026-07-15", "reviewer": "Jefe de seguridad",
     "source": "20-accesos/revision-accesos_core-bancario_2026-07-15.pdf"}
  ],
  "third_party_assessments": [
    {"third_party": "Nube Andina S.A.S.", "date": "2026-03-10", "result": "con observaciones",
     "source": "30-terceros/evaluacion_nube-andina_2026-03-10.pdf, p. 4"}
  ],
  "reviewed": [{"source": "10-controles/borrador.docx", "motivo": "borrador sin firma: no es evidencia"}],
  "questions": [{"question": "¿El acta del comité de seguridad es de agosto o de septiembre?", "answer": "De septiembre",
                 "source": "conversación del 2026-10-15"}]
}
```

## Cómo se decide cada uno

- **`evidence`**: un registro por documento que muestra que un control **operó**. `control` es el número con que lo nombra la declaración de aplicabilidad —el mismo con que empieza el nombre del archivo—. `date` es **la fecha que cubre la evidencia**, no la de su archivo: un informe de respaldos de septiembre cubre el 30 de septiembre; un acta, el día de la reunión. Una política aprobada no es evidencia de que un control operó; un borrador sin firma tampoco: van a `reviewed` con su motivo.
- **`access_reviews`**: una revisión de accesos de un sistema con su fecha y quién la hizo. El sistema se escribe como lo nombra la tabla de sistemas. Una revisión sin fecha no va: va como pregunta.
- **`third_party_assessments`**: la evaluación de seguridad de un tercero —su cuestionario, su informe de auditoría, su certificación vigente— con su fecha y su resultado en las palabras del documento. El tercero se escribe como lo nombra el registro.
- **`reviewed`**: lo que se miró y no va, con su motivo. Así el motor no lo vuelve a pedir. **Lo que el motor excluye —credenciales, llaves y respaldos— no va aquí**: no se miró, y ya lo lista `seguridad.py excluidos`, que es lo que el reporte cita (CISO-3).
- **`questions`**: lo que se le preguntó a la persona y lo que respondió. Una pregunta sin respuesta lleva `"answer": null`.

## Lo que nunca va

- Una contraseña, una llave, un token o un fragmento de un respaldo, aunque aparezca en un documento.
- Una fecha que el documento no dice, o un control que el documento no nombra.
- Una calificación de la madurez del control.
