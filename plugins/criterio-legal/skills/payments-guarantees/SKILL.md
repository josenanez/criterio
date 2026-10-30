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

## Los contratos de una entidad pública

Si la configuración dice que la entidad es pública (`public_procurement.public`), el motor revisa cada contrato contra la ley de contratación pública de su país, del registro de países (`contratacion_publica`). Cada regla tiene su fuente en `families/criterio-clo/FUENTES.es.md`:

| País | La publicación | La garantía de cumplimiento |
|---|---|---|
| Colombia | En el SECOP, dentro de los 3 días hábiles siguientes a la firma (F-03) | Al menos el 10 % del valor del contrato (F-04) |
| Ecuador | — | El 5 % del valor, desde el umbral de la configuración (F-05) |
| Perú | — | El 10 % del monto del contrato original (F-06) |
| Chile | En trato directo, dentro de las 24 horas siguientes (F-07) | El 5 % del precio adjudicado, desde el umbral de la configuración (F-08) |
| México | — | Entregada a más tardar diez días naturales después de la firma (F-09) |
| Brasil | En el PNCP, dentro de 20 días hábiles si hubo licitación o 10 si fue contratación directa (F-10) | Hasta el 5 % del valor inicial, o hasta el 10 % si está justificada (F-10) |

La ficha del contrato trae `public` —el sistema, la fecha de publicación (`published_on`) de la constancia de `10-contrato/`, la modalidad (`modality`: licitación o directa) y la cita— y, en la garantía aportada, el valor asegurado (`amount`), la fecha de entrega (`delivered_on`) y, en Brasil, si el contrato justifica más del 5 % (`justified`). Los días hábiles se cuentan sin sábados, domingos ni los festivos de la configuración.

| Señal | Cuándo |
|---|---|
| `public_contract_not_published` | El contrato se publicó después del plazo, o no hay constancia y el plazo ya pasó |
| `public_guarantee_below_law` | La garantía de cumplimiento es menor que el mínimo de la ley |
| `public_guarantee_over_cap` | La garantía exigida supera el tope de la ley (Brasil) |
| `public_guarantee_late` | La garantía se entregó, o sigue sin entregarse, después del plazo de la ley (México) |

## Lo que nunca se hace

- Opinar si un sobrecosto está justificado o si una póliza cubre un riesgo: se muestra la diferencia y la fecha.
- Calificar a la aseguradora, o el monto asegurado fuera de lo que fija la ley de contratación pública de un contrato público.
- Sumar o restar a mano: todo monto sale de `legal.py`.
