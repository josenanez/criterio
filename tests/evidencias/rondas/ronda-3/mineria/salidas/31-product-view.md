# /criterio-portfolio:product-view alerta de taludes

## Productos al 2026-10-15

Esta vista sale del cálculo de `portafolio.py compute` sobre las fichas en `estado`, con corte al 2026-10-15. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez, así que no hubo que registrar nada nuevo.

**Alerta de taludes tiene un solo proyecto, PRY-204 Monitoreo de taludes.** Por eso no armé sección de producto: la vista por producto no aporta nada distinto de la del proyecto.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| alerta de taludes | 1 (PRY-204) | 1 de 1, con 11 alertas | 2027-01-12 | COP 1.200.000.000 | COP 403.511.534 |

### Lo que hay que ver en PRY-204
- **Declarado vs. evidencia:** el informe del 2026-09-27, de hace 18 días, lo declara **verde**. El cálculo encuentra seis señales que ese informe no explica.
- **Silencio:** lleva 16 días sin movimiento, desde el 2026-09-29. El umbral es 15.
- **Avance contra plan:** declara 27 % y el plan sostiene entre 40 % y 60 %, una brecha de 13 puntos por debajo del plan.
- **Hito vencido:** «Licencia y permisos obtenidos» vencía el 2026-10-11, hace 4 días.
- **Hitos cumplidos sin evidencia:** «Ingeniería básica aprobada» e «Ingeniería de detalle aprobada».
- **Proveedor Montajes Industriales Ltda.:** hay tres entregables atrasados y ninguno aceptado.
  - CT-594: «Licenciamiento del software», 58 días de atraso.
  - CT-331: «Licenciamiento del software», 92 días de atraso.
  - CT-331: «Bolsa de horas de ingeniería», 41 días de atraso.
- **Facturado sin entrega:** CT-594 tiene COP 133.892.409 facturados y CT-331 tiene COP 120.184.897. No los sumé, porque el cálculo no los da sumados.
- **Dinero:** las cuatro cifras están.
  - Ejecutado: 577.323.500, el 48,1 % de lo aprobado.
  - Comprometido: 33,6 % de lo aprobado.
  - Proyección: 1.183.123.627, un 1,4 % por debajo de lo aprobado.
  - Disponible real: 796.488.466.
- **Fecha del producto:** 2027-01-12, que sale de PRY-204. No hay desviación de tiempo, replanificaciones ni cambios.
- **Dependencias internas:** ninguna, porque el producto tiene un solo proyecto.

### Lo que no sé
- La ficha no trae autoridad ni fase, así que nadie figura como dueño que responda por el producto.
- Lo ejecutado (577 millones) es mayor que lo comprometido (404 millones). La ficha no lo explica.
- «Licenciamiento del software» aparece en dos contratos, CT-594 y CT-331, con fechas distintas. No sé si es el mismo entregable contratado dos veces.
- No listé los proyectos sin producto declarado, porque pediste un producto concreto. Esa lista sale corriendo `/product-view` sin argumento.

### Qué haría con esto
Llevaría una sola decisión al comité del 2026-10-19: qué hacer con un proyecto reportado en verde que tiene 11 alertas, y qué pasa con lo facturado a Montajes Industriales sin ningún entregable aceptado.

La corrida quedó registrada como `2026-10-15-product-view-1` (28 segundos, 13 proyectos). La salida completa está en `estado/corridas/salida-product-view.md`.

*Pie de rigor: este es un borrador de trabajo de Criterio, no una decisión ni una asesoría. Las cifras salen del cálculo del 2026-10-15 sobre las fichas. La verificación contra los documentos citados es de quien lo lee.*