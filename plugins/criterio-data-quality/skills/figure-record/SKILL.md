---
name: figure-record
description: "Cómo se registra en la ficha del periodo de Ariadna cada cifra de un informe de dirección, de junta o al supervisor: su indicador, su valor y la fecha de corte que el informe declara, con la cita. Úsalo al procesar `20-informes/`. Figure record, management report figures, cut-off."
---

# La ficha del periodo de Ariadna

Una ficha por periodo, en `<estado>/calidad/<AAAA-MM>/ficha.json`. El linaje, las cifras de la fuente, las reglas y sus resultados no se copian aquí: los procesa el motor. Aquí va lo que solo traen los informes.

```json
{
  "figures": [{"indicator": "Cartera vencida", "value": 1250000000, "cutoff": "2026-10-31",
               "source": "20-informes/informe_junta_2026-10.pdf, p. 2"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`indicator`**: el nombre del indicador como lo escribe el informe.
- **`value`**: la cifra como número, sin separadores ni símbolo de moneda: `1.250.000.000` es `1250000000`. Un porcentaje va como número: `14,2 %` es `14.2`.
- **`cutoff`**: la fecha de corte que el informe declara para esa cifra —«con corte al 31 de octubre de 2026» es `2026-10-31`—. Si el informe no la dice, va vacía y se pregunta.
- **`reviewed`**: los informes de `20-informes/` que se procesaron y no traen ninguna cifra. Un informe citado en una cifra no va aquí, ni las tablas que procesa el motor: el linaje, las cifras de la fuente, las reglas y sus resultados.

## Lo que nunca va

- Una cifra corregida: si el informe trae una cifra distinta de la fuente, se registra la del informe; la diferencia la calcula el motor.
- Un dato personal, ni siquiera de ejemplo.
