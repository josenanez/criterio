---
name: claim-record
description: "Cómo se registra en la ficha del periodo de Lucía cada afirmación de una pieza aprobada con su soporte, si es comparativa y la fuente que cita, y cada promoción con su vigencia y sus condiciones, con la cita. Úsalo al procesar `10-piezas/`, `20-soportes/` y `30-promociones/`. Claim record, substantiation, promotion terms."
---

# La ficha del periodo de Lucía

Una ficha por periodo, en `<estado>/piezas/<AAAA-MM>/ficha.json`. El registro de piezas, el de bases de contactos y el plan no se copian aquí: los procesa el motor. Aquí va lo que solo traen las piezas y las bases de las promociones.

```json
{
  "claims": [{"piece": "P-02", "claim": "El precio más bajo del mercado en la canasta básica",
              "support": "20-soportes/comparativo_de_precios_2026-10.pdf", "comparative": true,
              "comparative_source": "Comparativo de precios de un tercero independiente, octubre de 2026",
              "source": "10-piezas/pieza_P-02.pdf"}],
  "promotions": [{"name": "Navidad", "start": "2026-12-01", "end": "2026-12-24", "conditions": true,
                  "source": "30-promociones/bases_promocion_navidad.pdf"}],
  "reviewed": [],
  "questions": []
}
```

## Cómo se decide cada uno

- **`claims`**: cada afirmación objetiva de una pieza —una cifra, un plazo, un origen, una comparación—, en las palabras de la pieza, con el código de la pieza como lo escribe el registro. Una opinión o una emoción no es una afirmación.
- **`support`**: la ruta del documento de `20-soportes/` que sostiene esa afirmación, si hay uno que trate de lo mismo. Si ninguno trata de lo mismo, va vacío: el motor dice que falta. Si el soporte basta, no lo decides tú: lo decide legal.
- **`comparative`** y **`comparative_source`**: si la afirmación compara con la competencia —«el más», «más que», «el único»—, y la fuente y la fecha que la pieza misma cita. Si la pieza no las cita, `comparative_source` va vacío.
- **`promotions`**: cada promoción con su nombre, su inicio y su fin tal como los publican sus bases, y `conditions` verdadero solo si las bases dicen el modo y el lugar. Una fecha que las bases no dicen va vacía.
- **`reviewed`**: las piezas y las bases que se procesaron y no traen nada para la ficha. Un documento citado en otro campo no va aquí.

## Lo que nunca va

- Un juicio sobre si una afirmación es verdadera o si la creatividad funciona.
- Un soporte asignado porque está en la carpeta: tiene que tratar de lo mismo que la afirmación.
- Los datos de una persona, ni siquiera de ejemplo.
