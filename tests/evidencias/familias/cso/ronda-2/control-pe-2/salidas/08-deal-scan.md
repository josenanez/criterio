# /criterio-revenue:deal-scan 

Las tres cotizaciones de `40-cotizaciones/` (COT-2201, COT-2202 y COT-2203) ya están en la ficha del periodo 2026-10, y el motor no marcó ninguna señal.

Las cotizaciones no eran archivos nuevos, pero no estaban en la ficha de ingresos y las llevé a ella. Los términos (v1.3) ya estaban vigentes, con la aceptación de José Francisco Ñáñez del 2026-11-05. El inventario no encontró archivos nuevos, cambiados ni ilegibles.

| Cotización | Oportunidad | Precio de lista | Descuento | Aprobación escrita |
|---|---|---|---|---|
| COT-2201 | OPP-2201 | S/ 335,000 | 10 % | Ninguna. El documento dice "dentro del nivel sin aprobación", así que los campos quedan vacíos. |
| COT-2202 | OPP-2202 | S/ 550,000 | 18 % | Marta Gil, gerente comercial, 2026-10-05 |
| COT-2203 | OPP-2203 | S/ 725,000 | 14 % | Ricardo Paz, gerente general, 2026-10-20 |

El reporte lo escribió el motor y queda en `ingresos/2026-10/reporte-deal-scan.md`. Dice "Cotizaciones en la ficha: 3" y "Nada abierto en lo que procesa este comando"; no trae otras cifras ni fechas.

Si el descuento de COT-2201 necesitaba aprobación o no, lo dice la matriz, y eso lo revisa `/criterio-revenue:discount-check`. Este comando no lo juzga.

La corrida quedó registrada como `2026-11-05-deal-scan-1`, con 0 hallazgos. Lo que te mostré está en `corridas/salida-deal-scan.md`.