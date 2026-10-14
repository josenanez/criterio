# /criterio-portfolio:budget-tracking PRY-210

## Presupuesto de PRY-210 (Etiquetas electrónicas de precio) al 2026-10-14

Salen de la ficha PRY-210 y del `compute` de hoy. Los términos 1.0 ya estaban aceptados en la configuración (José Francisco Ñáñez, 2026-10-14).

**Moneda:** COP, la única que hay, sin conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 2.400.000.000 | 100 % | Acta de constitución | 2026-01-21 |
| Comprometido | 1.049.743.627 | 43,7 % | Informe de avance (declaración) | 2026-09-28 |
| Ejecutado | 469.411.976 | 19,6 % | Informe de avance (declaración) | 2026-09-28 |
| Proyección al cierre | 2.698.160.369 | 112,4 % | Informe de avance (declaración) | 2026-09-28 |

**Disponible real** (aprobado menos comprometido): 1.350.256.373 COP.

- **Contra la línea base:** no hay replanificaciones ni solicitudes de cambio. La ficha guarda un solo aprobado, así que el original y el vigente coinciden. La proyección excede el aprobado en 12,4 %, es decir 298.160.369 COP. Esa resta la hice yo; `compute` solo da el porcentaje.
- **Ejecución frente a avance:** el ejecutado es 19,6 % y el avance declarado es 32 %, con 1 hito cumplido de 4. No hay gasto adelantado. Pero el único hito cumplido, "Diseño de la experiencia aprobado", no tiene evidencia.
- **Alertas:**
  - **Proyección:** supera el umbral de 10 %.
  - **Comprometido:** está bajo el umbral de 90 %, sin alerta de tope.
  - **Declaraciones:** comprometido, ejecutado y proyección salen de un informe de avance, no de un documento contable.
  - **Otras señales:** hay 16 días de silencio y el hito "Ambiente de pruebas certificado" lleva 12 días vencido. El informe declara verde pese a eso y al sobrecosto.
- **Sin dato:** el presupuesto original y el vigente como dos cifras separadas, la evidencia contable de comprometido y ejecutado, y los proveedores (la ficha no registra ninguno).

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/change-control`. No ofrezco el detalle por proveedor: el comprometido está lejos del tope y no hay proveedores registrados.

La corrida quedó registrada como `2026-10-14-budget-tracking-1`, con la salida completa en `estado-portafolio/corridas/salida-budget-tracking.md`.