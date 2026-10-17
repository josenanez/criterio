# /criterio-portfolio:product-view nómina empresarial

**Vista por producto: nómina empresarial, al 2026-10-17.** Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrar nada. Las cifras salen de las fichas, recalculadas con `portafolio.py compute`.

Nómina empresarial tiene un solo proyecto, PRY-209 Nómina electrónica. Por eso no armé una sección de producto aparte. Esto es lo que hay que ver:

- **Costo:** la proyección es COP 2.640.413.839 contra COP 2.400.000.000 aprobados, 10,0 % por encima. Ese es justo el umbral configurado (10 %).
- **Verde sin explicación:** el informe de avance del 2026-10-17 declara verde y 50 % de avance. No explica el sobrecosto.
- **Dinero:**
  - Ejecutado: COP 1.193.333.539 (49,7 %).
  - Comprometido: 70,8 %.
  - Disponible real: COP 700.111.916.
  - La ficha trae las cuatro cifras, así que la suma del producto está completa.
- **Fecha:** el fin vigente es 2026-09-21, anterior a la fecha de corte. El cálculo no marca atraso ni hitos vencidos, y las fichas no traen cierre ni fecha nueva. No lo doy por cerrado.
- **Dependencias:** ninguna entre proyectos del mismo producto, porque solo hay uno.
- **Lo que no sé:** si el sobrecosto tiene aprobación, porque a la ficha le falta `identity.authority`. Tampoco tiene `identity.phase`.

**Cuatro proyectos no declaran producto**, y nadie responde por el conjunto al que sirven:

| Proyecto | Área dueña |
|---|---|
| PRY-202 Migración a la nube | Riesgo y Cumplimiento |
| PRY-205 Prevención de lavado de activos | Riesgo y Cumplimiento |
| PRY-208 Motor de decisión | Banca Hipotecaria |
| PRY-210 Portal de proveedores | Tesorería |

Además, PRY-199 declara el producto como «PRD-299», un código y no un nombre. Así no cruza con los demás productos.

No hay dependencias internas que llevar al comité de producto. Para el comité del 2026-10-20 propongo una sola decisión: PRY-209 está en verde declarado con 10,0 % de sobrecosto proyectado.

La corrida quedó registrada como `2026-10-17-product-view-1`, en 30 segundos y sobre los 13 proyectos del portafolio. El texto completo está en `estado/corridas/salida-product-view.md`. La verificación de las citas es suya.