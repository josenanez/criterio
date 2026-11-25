---
name: governance-record
description: "Cómo se registra en la ficha del periodo de Custodia cada política con su fecha de aprobación y de revisión, cada plazo de conservación por tipo de dato y cada término de los informes de dirección, con la cita. Úsalo al procesar `00-referencia/` y `20-informes/`. Governance record, policies, retention, glossary terms."
---

# La ficha del periodo de Custodia

Una ficha por periodo, en `<estado>/gobierno/<AAAA-MM>/ficha.json`. El catálogo, el registro de bases y el glosario no se copian aquí: los procesa el motor. Aquí va lo que solo traen los documentos.

```json
{
  "policies": [{"name": "Política de datos", "approved": "2023-06-01", "next_review": "2025-06-01",
                "source": "00-referencia/politica_de_datos.pdf, p. 1"}],
  "retention": [{"type": "Clientes", "months": 120, "source": "00-referencia/politica_de_conservacion.pdf, p. 3"}],
  "report_terms": [{"term": "Cartera vencida", "source": "20-informes/informe_junta_2026-10.pdf, p. 2"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`policies`**: cada política con el nombre que le da su documento, su fecha de aprobación y la fecha en que debe revisarse, tal como constan. Si el documento no dice la fecha de revisión, va vacía y se pregunta.
- **`retention`**: cada tipo de dato con el plazo de conservación que fija la política, en meses, y el tipo escrito como lo nombra el catálogo.
- **`report_terms`**: cada indicador o término que un informe de dirección usa para presentar una cifra, en las palabras del informe, una vez por término.
- **`reviewed`**: los documentos de `00-referencia/` y `20-informes/` que se procesaron y no traen nada para la ficha. Un documento citado en otro campo no va aquí, ni las tablas que procesa el motor: el catálogo, el registro de bases y el glosario.

## Lo que nunca va

- Un dato personal, ni siquiera de ejemplo.
- Una fecha o un plazo que el documento no dice, completado para que la ficha se vea entera.
