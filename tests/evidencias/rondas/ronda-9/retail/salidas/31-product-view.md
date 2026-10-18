# /criterio-portfolio:product-view marca propia

## Producto «marca propia» al 2026-10-17

Fuentes: las fichas de `estado/records/` y el cálculo `compute` con corte 2026-10-17. Los términos estaban vigentes (v0.4.0, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que pedir nada.

«Marca propia» tiene un solo proyecto, PRY-207 (Marca propia de alimentos). Una vista por producto no aporta nada con un solo proyecto, así que no armé la sección de dependencias internas y lo que sigue es la lectura de ese proyecto.

**Cero alertas no significa que esté sano.**
- **Fecha vencida:** la fecha comprometida es 2026-04-17, anterior al corte. El proyecto sigue abierto con 66 % de avance declarado. El cálculo reporta atraso 0 porque la línea base es una sola (la del acta del 2025-05-27) y nadie la movió. El script no da días de atraso, así que no escribo ese número.
- **Sin hitos:** la ficha no tiene hitos, así que no pueden saltar las señales de hito vencido ni de avance contra plan. Ese cero es falta de dato.
- **Estado rojo:** el informe del 2026-10-15 (gerente Javier Hoyos) declara estado rojo. La ficha no tiene fuentes de evidencia, solo 2 declaraciones.
- **Dinero:** las cuatro cifras están completas.
  - Aprobado: COP 9.500.000.000.
  - Comprometido: COP 4.249.815.175 (44,7 %).
  - Ejecutado: COP 1.531.882.450 (16,1 %).
  - Proyección al cierre: COP 9.186.690.012 (−3,3 % frente a lo aprobado). Proyecta cerrar dentro del presupuesto un proyecto cuya fecha ya pasó.
- **Riesgos sin dueño:** hay dos riesgos abiertos, sin dueño, probabilidad, impacto ni fecha: el cambio en la regulación de datos personales y la fecha de la última entrega del proveedor. No hay proveedores registrados en la ficha, aunque el segundo riesgo habla de uno. Faltan además la autoridad y la fase.
- **Datos viejos:** 13 campos vienen del acta de hace 17 meses, por encima del umbral de 12.

**Proyectos sin producto declarado.** Son seis: PRY-202, 203, 206, 209, 210 y 211. Nadie responde por el conjunto al que sirven. Sin producto declarado tampoco puedo cruzarlos con «marca propia»; PRY-206 (Precios dinámicos) y PRY-211 (Pronóstico de demanda) son los candidatos obvios, pero es una sospecha mía, no un hallazgo. Un séptimo, PRY-199, declara «PRD-299», que es un código y no un nombre de producto.

**Lo que no sé.**
- Los días de atraso de PRY-207.
- Si hubo un cambio de fecha acordado fuera de los documentos.
- El área dueña de los seis proyectos sin producto, que no extraje en esta corrida.

La corrida quedó registrada como `2026-10-17-product-view-1` (37 segundos, 13 proyectos). El texto completo está en `estado/corridas/salida-product-view.md`. Todo es borrador de trabajo: la verificación contra los originales es suya.