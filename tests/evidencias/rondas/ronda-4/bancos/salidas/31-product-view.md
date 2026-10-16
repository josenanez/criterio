# /criterio-portfolio:product-view nómina empresarial

## Productos al 2026-10-15

Esta vista sale del cálculo del estado (`compute`) sobre 13 proyectos. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

**Nómina empresarial tiene un solo proyecto: PRY-209 Nómina electrónica.** La vista por producto no aporta nada con un solo proyecto, así que no armé sección de producto. Esto es lo que dice la ficha de ese proyecto:

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| nómina empresarial | 1 (PRY-209) | 4 señales | 2026-12-05 (PRY-209) | COP 9.500.000.000 | COP 6.750.954.901 |

**Lo que hay que ver en PRY-209**
- **Verde sin sustento.** El informe del 2026-09-28 declara verde con 24,0 % de avance. Con 3 de 4 hitos cumplidos, el plan sostiene entre 75 % y 100 %, una brecha de 51,0 puntos.
- **Dos hitos "cumplidos" sin evidencia.**
  - «Diseño funcional aprobado» vencía el 2026-03-22 (207 días).
  - «Ambiente de pruebas certificado» vencía el 2026-06-16 (121 días).
- **Dinero (traen las cuatro cifras).** Lo ejecutado es COP 3.509.937.301 (36,9 %) y lo comprometido es 71,1 %. La proyección es COP 9.666.666.238, 1,8 % sobre lo aprobado. Queda disponible COP 2.749.045.099.
- **Fechas.** Tiene línea base, sin replanificaciones y con 0 días de desviación. No hay proveedores registrados ni compromisos vencidos.
- **Faltan en la ficha** la autoridad (`identity.authority`) y la fase (`identity.phase`).

**Dependencias internas:** ninguna. El cálculo tampoco registra dependencias declaradas de PRY-209.

### Proyectos sin producto declarado
- PRY-202 Migración a la nube
- PRY-205 Prevención de lavado de activos
- PRY-208 Motor de decisión
- PRY-210 Portal de proveedores

Mientras no declaren producto, nadie puede responder por el conjunto al que sirven. No pude decir el área dueña de ninguno, porque el cálculo no la entrega y no la inventé.

La corrida quedó registrada como `2026-10-15-product-view-1`, con la salida completa en `estado/corridas/salida-product-view.md`. Las cifras salen del cálculo y las alertas contrastan lo declarado con la evidencia de la ficha. No sé qué se habló fuera de los documentos, y la verificación es de quien lea.