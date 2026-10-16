# /criterio-portfolio:product-view venta en línea

## Producto «venta en línea» al 2026-10-16

Salen de las fichas en `estado/records`, recalculadas con `compute` al 2026-10-16. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**«venta en línea» tiene un solo proyecto: PRY-200 Tienda en línea.** Con un solo proyecto no hay suma entre proyectos, dependencias internas ni fecha que escoger, así que no armé sección de producto.

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |
|---|---|---|---|---|---|
| venta en línea | 1 (PRY-200) | 1 (5 alertas) | 2026-12-11 | COP 6.800.000.000 | COP 4.799.233.410 |

**Lo que hay que ver en PRY-200**
- **Estado declarado:** el informe del 2026-10-16 dice verde, pero las señales lo contradicen.
- **Avance:** el proyecto declara 46,0 %. El plan sustenta entre 75 y 100 % (3 de 4 hitos cumplidos), así que va 29,0 puntos por detrás.
- **Hitos sin evidencia:** «Ambiente de pruebas certificado» (vencía 2026-04-27) e «Integración con el ERP» (vencía 2026-08-19) están declarados cumplidos, pero no hay evidencia.
- **Compromiso vencido:** Javier Hoyos, «Entregar el punto 29», vencía el 2026-10-02 (14 días). Fuente: `PRY-200-tienda-en-línea/30-reuniones/2026-10-11-comite-semanal.md`.
- **Dinero:**
  - Ejecutado COP 2.855.071.580 (42,0 %).
  - Comprometido 70,6 %.
  - Proyección COP 6.930.747.093 (1,9 % sobre lo aprobado).
  - Disponible real COP 2.000.766.590.
  - Las cuatro cifras están completas.
- **Cronograma:** sin desviación contra la línea base ni replanificaciones.
- **Dependencias internas:** ninguna.

**Lo que no sé**
- Ninguna de las fuentes cuenta como evidencia (hay 3 declaraciones y 17 sin marcar), así que no puedo confirmar ni descartar los hitos.
- Faltan la autoridad y la fase del proyecto.
- Ocho campos de identidad y plan tienen 13 meses (fuente de 2025-09-01).

**Proyectos sin producto declarado.** Son seis, así que nadie puede responder por el conjunto al que sirven: PRY-202, PRY-203, PRY-206, PRY-209, PRY-210 y PRY-211. La salida del cálculo no trae el área dueña y no la inventé.

**Después.** No hay dependencias internas que llevar al comité de producto. Lo que sí merece el comité del 2026-10-23 es el verde contradicho de PRY-200.

**Pie de rigor:** esto es un borrador de trabajo, no una decisión ni asesoría. Las cifras vienen de `compute`. La verificación contra los documentos citados es suya.

**Corrida registrada:** `2026-10-16-product-view-1`, con la salida completa en `estado/corridas/salida-product-view.md`.