---
name: finding-record
description: "Cómo se registra en la ficha del periodo de Justo cada trabajo de auditoría: la aprobación del programa, la fecha del informe y cada hallazgo de los papeles y del informe con su criterio, su condición, su causa o la razón por la que no se identificó, su efecto, su impacto, su probabilidad, su prioridad, los papeles que cita y sus cifras, con la cita. Úsalo al procesar `20-trabajos/`. Audit finding record, working papers, report."
---

# La ficha del periodo de Justo

Una ficha por periodo, en `<estado>/trabajos/<AAAA-MM>/ficha.json`. El programa y el índice de papeles no se copian aquí: los procesa el motor. Aquí va lo que solo traen los documentos escritos.

```json
{
  "engagements": [
    {"id": "TR-01", "program_approved": "2026-02-01", "program_source": "20-trabajos/TR-01_credito/programa-aprobado.pdf",
     "report_date": "2026-04-30", "report_source": "20-trabajos/TR-01_credito/informe.pdf",
     "findings": [
       {"id": "H-01", "criteria": "Política de crédito, numeral 4.2", "condition": "12 de 60 créditos desembolsados sin garantía constituida",
        "cause": "El desembolso no espera la constancia de la garantía", "cause_unknown_reason": null,
        "effect": "Pérdida esperada sin cobertura", "impact": 4, "likelihood": 4, "priority": "Alta",
        "workpapers": ["PT-01"], "figures": [1200000000], "source": "20-trabajos/TR-01_credito/PT-01.pdf, p. 4"}],
     "report_findings": [
       {"id": "H-01", "priority": "Alta", "figures": [1200000000], "source": "20-trabajos/TR-01_credito/informe.pdf, p. 6"}]}
  ],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`id`** del trabajo: el código de su carpeta en `20-trabajos/`, el que va antes del primer guion bajo.
- **`program_approved`**: la fecha en que el responsable de auditoría aprobó el programa, tal como consta en el documento; sin constancia, va vacío y el motor levanta la señal.
- **`findings`**: cada hallazgo **como lo escriben los papeles**. `criteria`, `condition`, `cause` y `effect` en sus palabras; si los papeles dicen por qué no se pudo identificar la causa, va en `cause_unknown_reason`. `impact` y `likelihood` en la escala de la metodología; `priority`, la que puso el auditor. `workpapers`, las referencias que cita; `figures`, las cifras del hallazgo.
- **`report_findings`**: cada hallazgo **como lo dice el informe**, con su prioridad y sus cifras. Si el informe no se ha emitido, la lista no va.
- **`reviewed`**: los documentos de `20-trabajos/` que se procesaron y no traen nada para la ficha: un papel sin hallazgo. Un documento citado en otro campo —el papel de un hallazgo, el informe, la aprobación del programa— no va aquí.

## Lo que nunca va

- Un elemento que el papel no trae, completado para que el hallazgo se vea entero: si falta la causa, va vacía y el motor levanta la señal.
- Una prioridad distinta de la que puso el auditor, aunque la metodología dé otra: esa diferencia la calcula el motor.
