# /criterio-portfolio:budget-tracking PRY-211

## Presupuesto — PRY-211 Cobranza digital al 2026-10-16

**Fuentes:** la ficha PRY-211 y las cifras recalculadas con `compute`. Los documentos son el acta de constitución (2025-07-08) y el informe de avance (2026-10-13). Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Moneda:** COP. Es la única, y no hubo conversiones.

| | Monto (COP) | % del aprobado | Fecha |
|---|---|---|---|
| Aprobado | 2.400.000.000 | 100% | 2025-07-08 |
| Comprometido | 1.243.793.744 | 51.8% | 2026-10-13 |
| Ejecutado | 949.227.038 | 39.6% | 2026-10-13 |
| Proyección al cierre | 2.771.140.444 | 15.5% por encima del aprobado | 2026-10-13 |

- **Disponible real** (aprobado menos comprometido): 1.156.206.256 COP.
- **Contra la línea base:** original y vigente son iguales (2.400.000.000), sin replanificaciones ni solicitudes de cambio. El aprobado se apoya solo en el acta, que tiene 15 meses, más que el umbral de 12.
- **Ejecución frente a avance:** el ejecutado es 39.6%, con 3 de 4 hitos cumplidos y un avance declarado de 89%. Puede ser trabajo hecho y no facturado, o un avance sobredeclarado. Los documentos no permiten distinguirlos.

**Alertas**
- **Proyección sobre el aprobado:** supera el umbral de 10% con 15.5%, y el informe del 2026-10-13 declara el proyecto en verde sin dar cuenta de ello.
- **Hitos cumplidos sin evidencia:** 2 de los 3 hitos cumplidos no tienen acta de recibo.
- **Ajuste de presupuesto pendiente:** hay un compromiso sin fecha de Laura Vélez ("Mandar el ajuste del presupuesto"). Ese ajuste no está en ningún documento.
- **Comprometido:** 51.8% frente al umbral de 90%, sin alerta.

**Sin dato**
- No escribí el monto en pesos de la desviación, porque el script no lo entrega. Solo va el 15.5%.
- No hay proveedores en la ficha, así que no hay detalle por proveedor.

Si quieres, preparo la solicitud de cambio de presupuesto con `/criterio-portfolio:change-control`, ya que la proyección excede el aprobado.

La salida quedó en `estado/corridas/salida-budget-tracking.md` y la corrida se registró como `2026-10-16-budget-tracking-1`.