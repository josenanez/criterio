# /criterio-portfolio:product-view aportes sociales

# Producto: aportes sociales, al 2026-10-16

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo. Los datos salen de las fichas del estado y del cálculo `compute` de hoy.

**«Aportes sociales» tiene un solo proyecto, PRY-203 Aportes sociales en línea.** En ese caso la vista por producto no aporta más que la ficha del proyecto, así que no armé una sección aparte.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| aportes sociales | 1 (PRY-203) | 0 | 2026-07-25 | COP 800.000.000 | COP 336.456.745 |

- **Señales:** el cálculo no marca ninguna alerta. El proyecto no tiene atraso contra la línea base, ni replanificaciones, ni compromisos vencidos. Lleva 2 días en silencio.
- **Dinero:** las cuatro cifras vienen completas.
  - Ejecutado: 441.454.741 (55,2 %).
  - Comprometido: 42,1 %.
  - Proyección: 767.281.484 (−4,1 % sobre lo aprobado).
  - Disponible real: 463.543.255.
- **Declarado por el gerente:** amarillo, con 36 % de avance al 2026-10-14.
- **Dependencias internas:** ninguna declarada.

**Lo que no cuadra y el cálculo no marca**
- **Fecha de fin vencida:** la fecha de fin vigente es 2026-07-25 y ya pasó, con el avance declarado en 36 %. El cálculo no emitió señal de atraso ni de hito vencido, y no sé por qué sin leer el plan. No inventé una cifra de atraso. Conviene que el gerente confirme si esa fecha sigue vigente.
- **Datos sin evidencia:** ningún dato de la ficha tiene evidencia (2 son declaraciones y 17 no tienen marca). Los campos de identidad y plan vienen de un documento de 2025-05-15, de hace 17 meses, sobre el umbral de 12.
- **Campos que faltan:** la autoridad que aprueba (`identity.authority`) y la fase (`identity.phase`).

**Proyectos sin producto declarado:** PRY-202, PRY-205, PRY-208, PRY-209 y PRY-210. Nadie puede responder por el conjunto al que sirven. El cálculo no entrega su área dueña, así que no la pude llenar. Aparte, PRY-199 declara el producto «PRD-299», que es un código y no un nombre como los demás; vale confirmarlo.

La salida quedó guardada en `estado/corridas/salida-product-view.md`. La corrida quedó registrada como `2026-10-16-product-view-1`: tardó 21 segundos, sobre 13 proyectos, con caso «aportes sociales».