---
name: discount-policy
description: "Cómo se lee la matriz de descuentos: el nivel que cubre cada descuento, la aprobación que ese nivel pide y por qué un cargo de un nivel superior también la da. Úsalo al explicar el reporte de descuentos o al configurar la matriz. Discount approval matrix."
---

# La matriz de descuentos

`00-referencia/matriz-descuentos` trae un nivel por fila: su **tope** —el descuento máximo que cubre, en %— y el **cargo que lo aprueba** (`ninguno` si no pide aprobación).

| nivel | tope | aprueba |
|---|---|---|
| 1 | 10 | ninguno |
| 2 | 20 | gerente comercial |
| 3 | 30 | gerente general |

## Cómo se decide

1. El nivel de un descuento es **el primero cuyo tope lo cubre**: un 18 % cae en el nivel 2.
2. Si ese nivel no pide aprobación, el descuento está dentro de la política.
3. Si la pide, la da **el cargo de ese nivel o el de cualquier nivel superior**: un 18 % aprobado por el gerente general está dentro.
4. **Un descuento que ningún nivel cubre** —un 35 % en esta matriz— siempre se señala, lo haya aprobado quien lo haya aprobado.

El cargo se compara por sus palabras, sin tildes ni mayúsculas. Si la cotización dice un cargo que la matriz no tiene —«director de ventas» cuando la matriz dice «gerente comercial»—, el motor no lo da por equivalente: lo señala, y la persona decide si es el mismo cargo. Si lo es, se corrige la matriz o la ficha, no el motor.

`discount_outside_policy` dice el nivel, la aprobación que pide y la que tiene, con la cita de la cotización y de la fila de la matriz.
