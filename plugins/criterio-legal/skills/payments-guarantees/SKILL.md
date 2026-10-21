---
name: payments-guarantees
description: "Cómo se cruza lo pagado por cada contrato con su valor y sus otrosíes, los pagos después de la terminación, y las garantías exigidas con las pólizas aportadas y su vigencia. Úsalo al revisar la ejecución de un contrato, al recibir una exportación de pagos o una póliza nueva. Contract payments vs value, insurance bonds, guarantees."
---

# Lo pagado y lo garantizado

## Los pagos

Los pagos vienen de la exportación del ERP en `10-registro/pagos…`, una fila por pago con `contrato`, `fecha` y `valor`. El código del contrato se escribe como en el registro. El motor procesa la tabla completa, no una muestra, y por contrato calcula:

- **El valor con sus otrosíes**: el valor inicial más el `added_value` de cada otrosí firmado.
- **Lo pagado, el saldo y el último pago.**
- **Los pagos después de la terminación efectiva**, que con renovación automática es la de la prórroga vigente.

| Señal | Cuándo |
|---|---|
| `payments_over_value` | Lo pagado supera el valor con sus otrosíes, más la tolerancia configurada |
| `payment_after_termination` | Hay pagos con fecha posterior a la terminación |

Un pago que no cruza con ningún contrato no se asigna por parecido: se reporta y se pregunta.

## Las garantías

Lo que el contrato exige —`guarantees_required` de la ficha— contra lo que dice cada póliza de `20-garantias/` —`guarantees_provided`—, por tipo de garantía. La vigencia exigida es la fecha que escribe el contrato o los meses después de la terminación que pide.

| Señal | Cuándo |
|---|---|
| `guarantee_missing` | El contrato exige una garantía y no hay póliza aportada de ese tipo |
| `guarantee_expires_early` | La póliza vence antes de la vigencia que exige el contrato |

Los tipos se escriben igual en lo exigido y en lo aportado —`cumplimiento`, `calidad`, `salarios`, `responsabilidad civil`…— para que crucen. Si la póliza los llama de otra forma, se pregunta.

## Lo que nunca se hace

- Opinar si un sobrecosto está justificado o si una póliza cubre un riesgo: se muestra la diferencia y la fecha.
- Calificar a la aseguradora o el monto asegurado.
- Sumar o restar a mano: todo monto sale de `legal.py`.
