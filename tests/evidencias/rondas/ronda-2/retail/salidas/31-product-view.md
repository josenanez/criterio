# /criterio-portfolio:product-view venta en línea

**Vista por producto: venta en línea.** Sale de las fichas en `estado/records/` y del cálculo de `portafolio.py compute`, con corte al 2026-10-15. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

Venta en línea tiene un solo proyecto, PRY-200 (Tienda en línea). Por eso no armé sección de producto y dejo lo que hay que ver en ese proyecto:

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| venta en línea | 1 (PRY-200) | 1 (4 alertas) | 2027-01-19 (PRY-200) | COP 800.000.000 | COP 407.557.334 |

- **Avance:** el proyecto declara 41 %, pero sus hitos cumplidos (3 de 4) respaldan entre 75 % y 100 %. Son 34 puntos de diferencia, hacia atrás.
- **Hitos sin evidencia:** tres hitos están dados por cumplidos sin evidencia:
  - «Diseño de la experiencia aprobado», vencía el 2026-02-10.
  - «Ambiente de pruebas certificado», vencía el 2026-06-04.
  - «Integración con el ERP», vencía el 2026-09-27.
- **Estado declarado:** rojo, según el informe del 2026-10-04. El informe no explica ninguna de las dos señales anteriores.
- **Fecha:** 2027-01-19, sin desviación ni replanificaciones. Como hay tres hitos sin sustento, eso es lo que dice el plan y no está comprobado.
- **Dinero:** las cuatro cifras están presentes.
  - Ejecutado: COP 204.484.564 (25,6 %).
  - Proyección: COP 822.388.023, 2,8 % sobre lo aprobado, por debajo del umbral de 10 %.
- **Datos que faltan o están viejos:** faltan la autoridad que aprueba y la fase. La identidad, el plan y el monto aprobado vienen de un documento del 2025-10-09, con 12 meses de antigüedad.
- **Dependencias internas:** ninguna, porque es un solo proyecto.

**Proyectos sin producto declarado:** son 6 de 13, y nadie puede responder por el conjunto al que sirven.

| Proyecto | Área dueña |
|---|---|
| PRY-202 Centro de distribución norte | Logística |
| PRY-203 Reposición automática | Finanzas |
| PRY-206 Precios dinámicos | Mercadeo |
| PRY-209 Migración del ERP | Tecnología |
| PRY-210 Etiquetas electrónicas de precio | Tecnología |
| PRY-211 Pronóstico de demanda | Comercio electrónico |

Dos de ellos podrían tocar venta en línea, pero ninguna ficha lo declara, así que son preguntas y no hallazgos. PRY-211 viene del área de comercio electrónico. PRY-209 tiene relación posible con el hito «Integración con el ERP» de PRY-200, el que está sin evidencia.

Lo que no sé es a qué producto sirve cada uno de esos 6 proyectos, ni si PRY-200 depende de PRY-209 o de PRY-211. Para el comité del 2026-10-22 propongo una sola decisión de gobierno: declarar el producto de esos 6, empezando por PRY-209 y PRY-211. No hay dependencias internas sin confirmar que llevar como punto de producto.

Corrida registrada como `2026-10-15-product-view-1` (32 segundos, 13 proyectos). La salida completa está en `estado/corridas/salida-product-view.md`.