---
name: deal-record
description: "Cómo se registra en la ficha del periodo de Valeria cada cotización o pedido: su oportunidad, su precio de lista, su descuento y quién lo aprobó con qué cargo y en qué fecha, cada dato con su cita. Úsalo al procesar `40-cotizaciones/`. Quote and discount record."
---

# La ficha del periodo de Valeria

Una ficha por periodo, en `<estado>/ingresos/<AAAA-MM>/ficha.json`. La matriz de descuentos, la tabla de cuentas, el plan y la liquidación de comisiones no se copian aquí: las procesa el motor. Aquí va solo lo que no es una tabla.

```json
{
  "quotes": [
    {"id": "COT-2210", "opportunity": "OPP-1042", "list_amount": 132000000, "discount_pct": 18,
     "approved_by": "Marta Ruiz", "approver_role": "gerente comercial", "approved_on": "2026-09-16",
     "source": "40-cotizaciones/COT-2210_cotizacion.pdf, p. 2"}
  ],
  "questions": []
}
```

## Cómo se decide cada uno

- **`id`** es el de la cotización o el pedido, el mismo con que empieza el nombre del archivo; **`opportunity`**, el id de la oportunidad en el CRM, como lo dice el documento.
- **`list_amount`** es el precio antes del descuento; **`discount_pct`**, el descuento total en porcentaje. Si el documento trae el descuento en dinero, se registra el porcentaje que da la cuenta del documento y se dice en una pregunta. Un documento sin descuento lleva `0`.
- **`approved_by`, `approver_role` y `approved_on`** son los de la aprobación escrita en el documento o en el correo que la acompaña: el nombre, el cargo con sus palabras y la fecha. **Si nadie lo aprobó por escrito, se dejan vacíos**: una aprobación que alguien dice que existe y no está escrita no va.

## Lo que nunca va

- El correo o el teléfono de un contacto del cliente.
- Una aprobación que el agente supone.
- Una opinión sobre si el descuento estaba bien dado: eso lo dice la matriz, y lo decide una persona.
