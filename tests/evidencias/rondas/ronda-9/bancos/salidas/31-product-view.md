# /criterio-portfolio:product-view nómina empresarial

**Fuente:** fichas del portafolio, recalculadas con `compute` al 2026-10-17. Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

## Nómina empresarial

El producto tiene un solo proyecto, **PRY-209 Nómina electrónica**. La vista por producto no aporta nada sobre un solo proyecto, así que no armé la sección completa.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| nómina empresarial | 1 | 1 | 2026-06-28 (PRY-209) | COP 9.500.000.000 | COP 5.744.594.486 |

- **Silencio:** PRY-209 lleva 21 días sin movimiento, desde 2026-09-26. El umbral configurado es 15 días.
- **Último informe:** declara amarillo y 78 % de avance, con fecha 2026-09-26. No explica el silencio.
- **Dinero:** ejecutado COP 2.599.596.789 (27,4 %) y comprometido 60,5 %. La proyección es COP 9.715.554.033, un 2,3 % sobre lo aprobado. Trae las cuatro cifras, 1 de 1 proyecto.
- **Sin otras señales:** `compute` no da atraso contra la línea base, hitos vencidos ni compromisos vencidos.
- **Dependencias internas:** ninguna.

**Lo que no sé o no cuadra:**
- La fecha comprometida (2026-06-28) ya pasó, con 78 % de avance declarado. `compute` no la marca como atraso. No puedo decir si es la fecha vigente sin leer el plan.
- Los 14 datos de la ficha vienen sin marca de fuente: ninguno está marcado como evidencia ni como declaración. Todo esto es lo que dice la ficha, no lo que sustenta un documento.
- Faltan `identity.authority` e `identity.phase`.

**Proyectos sin producto declarado** (hallazgo de gobierno): PRY-202 Migración a la nube, PRY-205 Prevención de lavado de activos, PRY-208 Motor de decisión y PRY-210 Portal de proveedores. En ninguno consta el área dueña. Nadie puede responder por el conjunto al que sirven. Además, el producto de PRY-199 figura como «PRD-299», que parece un código y no un nombre.

**Siguiente paso sugerido:** pedir a quien lleva PRY-209 un informe actualizado y la fecha de cierre vigente.

La corrida quedó registrada como `2026-10-17-product-view-1`, con el texto de esta respuesta en `estado/corridas/salida-product-view.md`. Es un borrador de trabajo; la verificación contra los documentos es suya.