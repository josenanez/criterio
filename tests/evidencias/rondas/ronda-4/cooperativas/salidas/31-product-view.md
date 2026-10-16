# /criterio-portfolio:product-view tarjeta débito

Corrí `/product-view` para «tarjeta débito» con las fichas de `estado/records` (13 proyectos) y el cálculo al 2026-10-15. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez, así que no hubo que registrarlos de nuevo.

**«Tarjeta débito» tiene un solo proyecto, PRY-204.** La vista por producto no aporta nada ahí, así que no armé sección de producto y dejé los datos del proyecto.

- **Alertas calculadas:** 0. Aun así, el gerente declara estado rojo y 70 % de avance en el informe del 2026-10-03. Las tres fuentes de esos datos son declaraciones y ninguna es evidencia, así que nada muestra qué hay detrás del rojo.
- **Fecha comprometida:** 2027-02-16, sin atraso contra la línea base original ni la vigente.
- **Dinero (COP, con las cuatro cifras):**

| Cifra | Valor | Porcentaje |
|---|---|---|
| Aprobado | 4.200.000.000 | |
| Comprometido | 2.044.466.248 | 48,7 % |
| Ejecutado | 2.463.577.669 | 58,7 % |
| Proyección | 4.389.905.182 | 4,5 % sobre lo aprobado |

  El ejecutado es mayor que el comprometido. Los documentos no lo explican y no lo corregí.
- **Dependencias:** no puede haber internas, porque el producto tiene un solo proyecto. La ficha registra, sin dueño, un riesgo declarado de dependencia del proveedor del core cooperativo. PRY-202 *Core cooperativo* no tiene producto declarado, así que esa dependencia no está confirmada.
- **Vacíos en la ficha:** faltan la autoridad y la fase.

**Cinco proyectos no declaran producto**, así que nadie responde por el conjunto al que sirven:

| Proyecto | Área dueña |
|---|---|
| PRY-202 Core cooperativo | Ahorro y aportes |
| PRY-205 Prevención de lavado de activos | Canales digitales |
| PRY-208 Motor de crédito | Canales digitales |
| PRY-209 Convenios de libranza con empresas | Cartera y cobranza |
| PRY-210 Corresponsales rurales | Operaciones |

Como no hay dependencias internas por llevar al comité de producto, solo queda una decisión: a qué producto pertenece PRY-202, para confirmar o descartar la dependencia de PRY-204.

La corrida quedó registrada como `2026-10-15-product-view-1`, con la salida completa en `estado/corridas/salida-product-view.md`. Tardó 28 segundos sobre 13 proyectos; el conteo de documentos no se midió.