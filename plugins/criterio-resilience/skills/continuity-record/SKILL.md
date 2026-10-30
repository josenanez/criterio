---
name: continuity-record
description: "El calendario de continuidad y cómo se registra en la ficha de Amparo cada prueba —del plan de continuidad, del de recuperación y de cada restauración de un respaldo— con su fecha y su resultado. Úsalo al procesar `90-continuidad/` o al revisar el calendario de `00-referencia/`. Continuity tests, restore tests, calendar."
---

# Las pruebas de continuidad

## El calendario

La tabla de `00-referencia/calendario`: cada prueba con su nombre, su tipo —**continuidad**, **recuperación** o **restauración**— el sistema o el respaldo que cubre y cada cuántos días tiene que hacerse. El motor separa las de restauración: un respaldo que nunca se restauró no se sabe si sirve.

## La ficha

```json
"tests": [
  {"test": "Restauración del core bancario", "date": "2026-06-20", "result": "exitosa",
   "source": "90-continuidad/prueba-restauracion_core-bancario_2026-06-20.pdf, p. 2"}
]
```

- **`test`**: el nombre de la prueba **como lo escribe el calendario**, para que el motor la cruce.
- **`date`**: el día en que se hizo la prueba, no el del informe.
- **`result`**: el que dice el informe, en sus palabras —exitosa, con observaciones, fallida—. Una prueba fallida cuenta como hecha; su resultado queda en el reporte para que una persona decida.

**El agente nunca ejecuta una prueba ni una restauración**, y nunca abre el respaldo: procesa el informe de la prueba.
