# /criterio-portfolio:product-view puntos de fidelización

# Vista por producto: puntos de fidelización

Sale de las fichas de `estado/records/` y del cálculo `portafolio.py compute`, al 2026-10-16. El informe de avance de PRY-201 es del 2026-10-13. Los términos ya estaban vigentes (v1.1, José Francisco Ñáñez, 2026-10-16).

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| puntos de fidelización | 1 (PRY-201) | 0 | 2026-09-10 | COP 6.800.000.000 | COP 4.318.579.944 |

El producto tiene un solo proyecto, PRY-201 «Programa de fidelización». La vista por producto no aporta nada sobre la de proyecto, así que no armé una sección aparte. Esto es lo que conviene saber:

- **Alertas:** el cálculo da 0. Hay 3 días desde el último documento y no hay replanificaciones, compromisos vencidos ni cambios.
- **Fecha vencida:** la fecha comprometida era el 2026-09-10, hace 36 días. Es la fecha de la línea base v1, y no hay replanificación registrada. El informe declara verde y 81 % de avance.
- **Verde sin medir:** el script no marca atraso porque la ficha no tiene hitos. Por eso el verde ni se sustenta ni se contradice.
- **Dinero:**

| Concepto | COP | Porcentaje |
|---|---|---|
| Comprometido | 4.318.579.944 | 63,5 % |
| Ejecutado | 2.579.519.333 | 37,9 % |
| Proyección | 6.821.176.777 | 0,3 % sobre lo aprobado |

  Las cuatro cifras están, pero las tres distintas del aprobado salen solo del informe de avance, sin otro documento que las corrobore.
- **Incidencia sin dueño:** «La prueba de carga de temporada no alcanzó el umbral pactado y se repite» (desde 2026-10-13). El informe la declara y aun así reporta verde. Los dos riesgos registrados tampoco tienen dueño.
- **Huecos de la ficha:** faltan la autoridad que aprueba y la fase. El alcance del acta es genérico y el área dueña es Talento humano. No lo interpreto.
- **Dependencias internas y proveedores:** no hay ni una cosa ni la otra, así que no hay nada que llevar al comité de producto.

**Proyectos sin producto declarado.** Seis de los 13 proyectos no declaran producto, y nadie puede responder por el conjunto al que sirven. Son PRY-202, PRY-203, PRY-206, PRY-209, PRY-210 y PRY-211.

**Lo que no sé:**
- Si el proyecto va de verdad al 81 %.
- Si hubo una replanificación posterior al acta.
- Qué se habló fuera de los documentos.

**Decisión que se desprende:** hay que replanificar con aprobación o explicar el atraso de la fecha vencida, y nombrar quién responde por la incidencia de la prueba de carga.

La corrida quedó registrada como `2026-10-16-product-view-1`. Duró 60 segundos, sobre 13 proyectos. El texto completo está en `estado/corridas/salida-product-view.md`.

*Criterio produce borradores de trabajo, no decisiones ni asesoría. Cada dato viene con su ficha de origen y la verificación es suya.*