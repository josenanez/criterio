---
name: transfer-control
description: "Los traslados, adiciones y reducciones del presupuesto: cómo se detectan comparando versiones, cómo se cruzan con el acta que los aprueba y qué es un acta sin cambio aplicado. Úsalo al revisar los traslados del año o una versión nueva del presupuesto. Budget transfers, approvals, minutes."
---

# Los traslados y sus actas

El motor compara cada versión de `10-aprobado/` con la anterior, línea por línea. Cada línea que cambió es un movimiento:

- **Traslado**, si el total del presupuesto no cambió: lo que sube en una línea baja en otra.
- **Adición** o **reducción**, si el total cambió.

Cada movimiento se cruza con los de las actas de la ficha (`minutes`, tipos `traslado`, `adicion` y `reduccion`): la línea de origen con lo que bajó, la de destino con lo que subió, y el valor. Un cambio sin acta es `transfer_without_approval`. Un movimiento de un acta que no aparece en ninguna versión se lista como *acta sin cambio aplicado*: lo aprobado no llegó al presupuesto.

Tomás no aprueba ni registra traslados: muestra cuáles tienen su acta y cuáles no.
