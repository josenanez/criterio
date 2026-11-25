---
name: result-record
description: "Cómo se registra en la ficha del periodo de Próspero cada resultado del informe de mercadeo: su campaña, su indicador, su valor y la fecha de corte que el informe declara, con la cita. Úsalo al procesar el informe de resultados de `50-campanas/`. Result record, campaign results, cut-off."
---

# La ficha del periodo de Próspero

Una ficha por periodo, en `<estado>/campanas/<AAAA-MM>/ficha.json`. El plan, las facturas de pauta y la exportación de la plataforma no se copian aquí: los procesa el motor. Aquí va lo que solo trae el informe de resultados.

```json
{
  "reported": [{"campaign": "C-01", "indicator": "Ventas atribuidas", "cutoff": "2026-10-31", "value": 4600,
                "source": "50-campanas/informe_de_resultados_2026-10.pdf, p. 1"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`campaign`**: el código de la campaña como lo escribe el plan de mercadeo.
- **`indicator`**: el nombre del indicador como lo escribe el informe; el motor lo compara con el de la plataforma.
- **`value`**: la cifra como número, sin separadores: `4.600` es `4600`; «1,84 millones» es `1840000`.
- **`cutoff`**: la fecha de corte que el informe declara —«con corte al 31 de octubre de 2026» es `2026-10-31`—. Si el informe no la dice, va vacía y se pregunta.
- **`reviewed`**: los documentos de `50-campanas/` que se procesaron y no traen ningún resultado. Un informe citado en un resultado no va aquí, ni las tablas que procesa el motor.

## Lo que nunca va

- Un resultado corregido: si el informe trae una cifra distinta de la plataforma, se registra la del informe; la diferencia la calcula el motor.
- Una cifra de la plataforma copiada al informe.
