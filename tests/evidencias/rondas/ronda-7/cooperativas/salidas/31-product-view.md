# /criterio-portfolio:product-view crédito de libranza

**Vista por producto: crédito de libranza, con corte al 2026-10-17.** Es un producto de un solo proyecto, PRY-200, así que no armé sección de grupo.

Los términos ya estaban vigentes (versión 0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17). No hizo falta registrarlos otra vez.

**Cifras de PRY-200 «Crédito de libranza digital»** (vienen de `portafolio.py compute`; las cuatro cifras del dinero están en la ficha, así que la suma está completa):

| Concepto | Valor |
|---|---|
| Aprobado | COP 2.400.000.000 |
| Comprometido | COP 1.398.098.317 (58,3 %) |
| Ejecutado | COP 929.267.306 (38,7 %) |
| Proyección | COP 2.644.653.523 (10,2 % sobre lo aprobado, con umbral de 10 %) |
| Fecha del producto | 2026-01-08 |

La fecha del producto sale de PRY-200 y ya pasó. El cálculo no registra replanificaciones, y no sé si la fecha se actualizó fuera de los documentos.

**Lo que hay que ver en PRY-200** (12 alertas):
- **Avance:** el gerente declara rojo y 28 % de avance. El plan da 4 de 4 hitos cumplidos, lo que sostendría 100 %. La brecha es de 72 puntos, y los documentos no dicen cuál de los dos tiene razón.
- **Hitos sin evidencia:** dos hitos figuran cumplidos sin evidencia: «Ambiente de pruebas certificado» e «Integración con el core cooperativo».
- **Compromisos vencidos:** hay cuatro sin evidencia, de 1 a 10 días de atraso.
- **Compromisos sin fecha:** hay dos.
- **Compromisos reprogramados:** dos, una 6 veces y otra 5.
- **Informe del gerente:** no recoge cinco de estas señales (compromisos vencidos, reprogramados, hitos sin evidencia, brecha de avance y sobrecosto).
- **Dependencias internas:** ninguna registrada.

**Proyectos sin producto declarado:** son 5 de 13: PRY-202, 205, 208, 209 y 210. Nadie puede responder por el conjunto al que sirven.
- **PRY-209 «Convenios de libranza con empresas»:** por el nombre toca libranza, pero no declara producto y no lo asigné por inferencia. Si sirve a este producto, el producto pasaría a tener dos proyectos, COP 5.700.000.000 aprobados y fecha más tardía 2027-09-10. PRY-209 declara verde con un hito vencido hace 8 días. La pregunta para el dueño del producto o la PMO es si PRY-209 sirve a crédito de libranza. Si es así, conviene llevarla al comité de producto como una sola decisión.
- **PRY-202 y PRY-208:** podrían tocar este producto, pero ningún documento lo declara.

**Lo que no sé:**
- Falta el área dueña de los proyectos sin producto.
- Faltan la autoridad y la fase de PRY-200.
- Los campos de identidad, plan y dinero de PRY-200 tienen fuente del 2025-06-26, con 16 meses de antigüedad.
- Ninguna de las 30 citas está marcada como evidencia o declaración.

La salida quedó en `estado/corridas/salida-product-view.md`. La corrida quedó registrada como `2026-10-17-product-view-1`, con 27 segundos medidos, 13 proyectos y 66 hallazgos en todo el portafolio.