# /criterio-portfolio:product-view tarjeta débito

## Producto «tarjeta débito» al 2026-10-15

Salen de las fichas de `estado/records`, recalculadas con `portafolio.py compute`. Los términos ya estaban vigentes (v0.3.9), aceptados por José Francisco Ñáñez el 2026-10-15.

**«Tarjeta débito» tiene un solo proyecto, PRY-204 Débito contactless.** No armo sección de producto, porque la vista por producto no añade nada a la del proyecto.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| tarjeta débito | 1 (PRY-204) | 6 alertas | 2027-04-14 (PRY-204) | COP 18.000.000.000 | COP 14.381.676.241 (79,9 %) |

**Lo que hay que ver en PRY-204:**
- **Hito vencido:** «Integración con el core» vencía el 2026-10-08, hace 7 días.
- **Hitos declarados cumplidos sin evidencia:** «Diseño funcional aprobado» (vencía el 2026-04-04, hace 194 días) y «Ambiente de pruebas certificado» (vencía el 2026-07-07, hace 100 días).
- **Compromiso vencido:** Javier Hoyos, «Entregar el punto 11», vencía el 2026-09-27, hace 18 días.
- **Proveedor Redes del Norte Ltda. (CT-470):**
  - «Licenciamiento del motor» sigue pendiente. Vencía el 2026-05-09, hace 159 días.
  - «Bolsa de horas de desarrollo» figura aceptada sin evidencia de recibo.
- **Semáforo:** el gerente declara **rojo** (informe del 2026-10-05, hace 10 días). Es coherente con la evidencia, pero esa declaración no explica cuatro de las señales anteriores.
- **Avance declarado:** 67 %, frente a un plan que sustenta entre 40 y 60 % (2 de 5 hitos cumplidos). No cruza el umbral.

**Dinero:**
- Aprobado: 18.000.000.000.
- Comprometido: 14.381.676.241.
- Ejecutado: 4.037.464.048 (22,4 %).
- Proyección: 16.668.912.353, un 7,4 % por debajo de lo aprobado.
- Disponible real: 3.618.323.759.
- Proveedor: aceptado y facturado 1.822.428.850.

Las cuatro cifras están completas.

**Fecha del producto:** 2027-04-14, sin atraso contra la línea base. El proyecto no declara dependencias, y con un solo proyecto no hay dependencias internas que cruzar.

**Lo que no sé:**
- A la ficha le faltan `identity.authority` e `identity.phase`.
- Ninguna de las 19 fuentes está marcada como evidencia: 2 son declaraciones y 17 no están marcadas.

**Proyectos sin producto declarado:** PRY-202 Migración a la nube, PRY-205 Prevención de lavado de activos, PRY-208 Motor de decisión y PRY-210 Portal de proveedores. Nadie puede responder por el conjunto al que sirven. La ficha no trae el área dueña, así que no la tabulo. Ninguno afecta a «tarjeta débito».

La corrida quedó registrada como `2026-10-15-product-view-1` (20 segundos, 13 proyectos, 68 hallazgos). El texto íntegro de esta respuesta está en `estado/corridas/salida-product-view.md`.

Este es un borrador de trabajo, no una decisión ni asesoría. Cada cifra sale del cálculo sobre las fichas, y una persona debe verificarla contra los documentos citados.